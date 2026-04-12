# VRCMT-stub

> Reemplazo del `yt-dlp.exe` de VRChat para agregar soporte de cookies y compatibilidad con yt-dlp moderno.

Este repositorio está **dedicado exclusivamente** al stub de yt-dlp usado por [VRCMT](https://github.com/doctorlatex/VRCMT). Mantiene un historial limpio de versiones del binario, separado de la app principal.

---

## ¿Qué es el stub?

VRChat incluye una versión antigua de `yt-dlp.exe` en su carpeta de herramientas. VRCMT puede reemplazarla temporalmente con este stub, que:

- **Inyecta cookies** automáticamente (Netflix, Crunchyroll, etc.) para que el reproductor de VRChat pueda acceder a contenido que requiere login
- **Filtra flags incompatibles** que VRChat pasa a yt-dlp y que versiones modernas no reconocen
- **Pasa todos los demás argumentos** tal cual al yt-dlp real del sistema

## Configuración

El stub lee su configuración desde:
```
%LOCALAPPDATA%\VRCMT\vrchat_stub.json
```

```json
{
  "cookies_file": "C:/ruta/completa/a/cookies.txt"
}
```

VRCMT gestiona este archivo automáticamente desde sus Ajustes.

---

## Versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| v1.1.0  | 2026-04-12 | Repositorio dedicado. Soporte cookies mejorado, filtrado --exp-allow |
| v1.0.0  | 2026-04 | Primera versión |

## Auto-actualización

La app VRCMT detecta nuevas versiones del stub automáticamente leyendo:

```
https://raw.githubusercontent.com/doctorlatex/VRCMT-stub/main/manifest.json
```

Para publicar una nueva versión del stub:
1. Compilar: `cd src && pyinstaller stub.spec --clean --noconfirm`
2. Calcular SHA256 del `yt-dlp.exe` generado
3. Actualizar `manifest.json` con la nueva versión, URL y SHA256
4. Crear un nuevo GitHub Release con el `yt-dlp.exe`

## Compilar desde fuente

```bash
pip install pyinstaller yt-dlp
cd src
pyinstaller stub.spec --clean --noconfirm
# Output: src/dist/yt-dlp.exe
```

## Estructura

```
VRCMT-stub/
├── manifest.json       ← Leído por VRCMT para auto-actualizar el stub
├── src/
│   ├── stub_main.py    ← Código fuente del stub
│   └── stub.spec       ← Spec de PyInstaller
└── README.md
```

---

**Repositorio principal de VRCMT:** [github.com/doctorlatex/VRCMT](https://github.com/doctorlatex/VRCMT)
