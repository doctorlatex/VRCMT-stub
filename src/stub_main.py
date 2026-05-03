"""
VRCMT yt-dlp Stub — Entry point
================================
Reemplaza el yt-dlp.exe de VRChat/Tools para agregar:
  - Soporte de cookies (archivo y navegador)
  - Filtro de flags legacy que VRChat puede inyectar y rompen yt-dlp moderno
  - Fallback para YouTube con player_client estable

Configuracion:
  %LOCALAPPDATA%\\VRCMT\\vrchat_stub.json
  {
    "cookies_file": "C:/ruta/a/cookies.txt",
    "cookies_from_browser": "chrome",
    "youtube_player_client": "android,web"
  }
  Nota: cookies_from_browser y youtube_player_client son opcionales.

Compilar con PyInstaller:
  cd src && pyinstaller stub.spec --clean --noconfirm
  El output sera dist/yt-dlp.exe
"""
from __future__ import annotations

import json
import os
import sys


def _sidecar_path() -> str:
    la = os.environ.get("LOCALAPPDATA", "")
    if not la:
        return ""
    return os.path.join(la, "VRCMT", "vrchat_stub.json")


def _filter_legacy_flags(argv: list[str]) -> list[str]:
    """Quita flags legacy que VRChat puede pasar y yt-dlp reciente no acepta."""
    drop_single = {
        "--exp-allow",
        "--all-subs",      # alias legacy no usado por VRChat moderno
    }
    drop_value_flags = {
        "--exp-allow",
    }
    drop_prefix = (
        "--exp-allow=",
    )
    out: list[str] = []
    i = 0
    n = len(argv)
    while i < n:
        a = argv[i]
        if a in drop_single:
            if a in drop_value_flags:
                i += 1
                if i < n and not argv[i].startswith("-"):
                    i += 1
                continue
            i += 1
            continue
        if any(a.startswith(p) for p in drop_prefix):
            i += 1
            continue
        out.append(a)
        i += 1
    return out


def _inject_cookies(argv: list[str], cookies_path: str) -> list[str]:
    if not cookies_path or not os.path.isfile(cookies_path):
        return argv
    if "--cookies" in argv:
        return argv
    return [argv[0], "--cookies", cookies_path] + argv[1:]


def _inject_browser_cookies(argv: list[str], browser: str) -> list[str]:
    if not browser:
        return argv
    if "--cookies" in argv or "--cookies-from-browser" in argv:
        return argv
    return [argv[0], "--cookies-from-browser", browser] + argv[1:]


def _is_youtube_invocation(argv: list[str]) -> bool:
    for a in argv[1:]:
        u = (a or "").lower()
        if "youtube.com/" in u or "youtu.be/" in u:
            return True
    return False


def _has_youtube_extractor_args(argv: list[str]) -> bool:
    n = len(argv)
    for i in range(1, n):
        a = argv[i]
        if a == "--extractor-args" and i + 1 < n:
            if "youtube:" in (argv[i + 1] or "").lower():
                return True
        if a.startswith("--extractor-args=") and "youtube:" in a.lower():
            return True
    return False


def _inject_youtube_client_defaults(argv: list[str], player_client: str) -> list[str]:
    if not player_client:
        return argv
    if not _is_youtube_invocation(argv):
        return argv
    if _has_youtube_extractor_args(argv):
        return argv
    value = f"youtube:player_client={player_client}"
    return [argv[0], "--extractor-args", value] + argv[1:]


def main() -> int:
    argv = _filter_legacy_flags(list(sys.argv))
    cookies = ""
    browser = ""
    youtube_player_client = ""
    sp = _sidecar_path()
    if sp and os.path.isfile(sp):
        try:
            with open(sp, encoding="utf-8") as f:
                data = json.load(f)
            cookies = (data.get("cookies_file") or "").strip()
            browser = (data.get("cookies_from_browser") or browser).strip()
            youtube_player_client = (
                data.get("youtube_player_client") or youtube_player_client
            ).strip()
        except Exception:
            pass
    argv = _inject_cookies(argv, cookies)
    # Si no hay archivo de cookies, intentar cookies del navegador por defecto.
    if "--cookies" not in argv:
        argv = _inject_browser_cookies(argv, browser)
    # Fallback opcional para YouTube solo si el usuario lo configuró en sidecar.
    argv = _inject_youtube_client_defaults(argv, youtube_player_client)
    sys.argv = argv
    import yt_dlp
    return yt_dlp.main()


if __name__ == "__main__":
    raise SystemExit(main())
