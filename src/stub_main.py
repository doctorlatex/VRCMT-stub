"""
VRCMT yt-dlp Stub — Entry point
================================
Reemplaza el yt-dlp.exe de VRChat/Tools para agregar:
  - Soporte de cookies (Netflix, Crunchyroll, etc.)
  - Filtrado de flags --exp-allow incompatibles con yt-dlp reciente

Configuracion:
  %LOCALAPPDATA%\VRCMT\vrchat_stub.json
  {
    "cookies_file": "C:/ruta/a/cookies.txt"
  }

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


def _filter_exp_allow(argv: list[str]) -> list[str]:
    """Quita flags --exp-allow que VRChat pasa pero yt-dlp reciente no entiende."""
    out: list[str] = []
    i = 0
    n = len(argv)
    while i < n:
        a = argv[i]
        if a == "--exp-allow":
            i += 1
            if i < n and not argv[i].startswith("-"):
                i += 1
            continue
        if a.startswith("--exp-allow="):
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


def main() -> int:
    argv = _filter_exp_allow(list(sys.argv))
    cookies = ""
    sp = _sidecar_path()
    if sp and os.path.isfile(sp):
        try:
            with open(sp, encoding="utf-8") as f:
                data = json.load(f)
            cookies = (data.get("cookies_file") or "").strip()
        except Exception:
            pass
    argv = _inject_cookies(argv, cookies)
    sys.argv = argv
    import yt_dlp
    return yt_dlp.main()


if __name__ == "__main__":
    raise SystemExit(main())
