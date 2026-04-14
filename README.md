# VRCMT-stub — Mejora de YouTube para VRChat (uso con VRCMT)

Este repositorio público está pensado **solo para distribución y actualizaciones**: aquí **no hay código fuente**. Lo que necesita la aplicación **VRCMT** para funcionar con el stub son el archivo **manifest** (en la raíz del repositorio) y el **ejecutable** publicado en la sección **Releases** de GitHub.

---

## ¿Qué es el “stub”?

**VRChat** incluye una pequeña utilidad encargada de **abrir enlaces de YouTube** dentro del juego (la herramienta suele llamarse popularmente *yt-dlp* y vive en la carpeta de datos de VRChat en tu PC). Esa versión puede **quedarse antigua** o no encajar bien con vídeos que exigen **inicio de sesión por cookies** (edad, región, etc.).

El **stub de VRCMT** es un **ejecutable sustituto** del que trae VRChat por defecto: hace **el mismo papel** (que VRChat pueda pedir el vídeo a YouTube), pero **actualizado** y con mejor **soporte de cookies** cuando tú las configuras desde VRCMT.

**Importante:** el stub **no es** la aplicación VRCMT completa. Solo reemplaza **ese único programa** dentro de la carpeta de herramientas de VRChat cuando tú activas la opción en VRCMT y sigues los pasos (incluido **cerrar VRChat** antes de instalar o quitar la mejora).

---

## Qué archivos ves aquí y para qué sirven

### Manifest (lista de actualización)

En la raíz hay un archivo de manifiesto que **VRCMT descarga automáticamente** desde internet cuando pulsas **instalar o actualizar desde internet** en la configuración del stub. Ese archivo indica, en lenguaje sencillo:

- **Qué versión** del stub se considera la actual (número de versión tipo 1.x.x).
- **Desde qué dirección** debe descargarse el ejecutable publicado (enlace a **Releases**).
- Una **comprobación de integridad** (huella digital del archivo) para asegurarse de que lo que se descargó coincide con lo publicado.
- **Qué versión mínima de VRCMT** hace falta para usar esa actualización, y así evitar mezclar versiones incompatibles.
- Un **texto de cambios** breve para el usuario (qué se mejoró respecto a la versión anterior).

Si en VRCMT dejas la URL del manifiesto en blanco, se usa **por defecto** la de este repositorio.

### Releases (el ejecutable)

En **Releases** está el archivo **ejecutable** que VRCMT copia en el sitio correcto cuando instalas la mejora. **No hace falta** descargarlo a mano salvo que quieras conservar una copia; VRCMT puede hacerlo por ti desde **Configuración → YouTube en VRChat**.

---

## Cómo se usa con VRCMT (pantalla de ajustes)

Todo el flujo se controla desde **VRCMT → Configuración → sección “YouTube en VRChat”**:

1. **Lee la ayuda** del propio apartado (botón de información) si quieres entender el proceso antes de tocar nada.
2. **Cierra VRChat por completo** antes de instalar, actualizar o quitar la mejora (si VRChat está abierto, los archivos pueden estar en uso).
3. **Activa** la casilla de usar la mejora del stub para VRChat (el texto exacto depende del idioma de la interfaz).
4. Pulsa **Instalar o actualizar desde internet** para que VRCMT baje el manifiesto, compare versiones, descargue el ejecutable si hace falta y lo coloque donde VRChat lo espera.
5. **Opcional — cookies:** en **opciones avanzadas** puedes indicar un archivo de cookies exportado desde tu navegador para vídeos con restricción; VRCMT te guía en la interfaz sin necesidad de tocar archivos a mano en este repositorio.
6. Si algo no te convence, usa **Quitar mejora** para volver al ejecutable original de VRChat (de nuevo con VRChat cerrado).

La sección también permite **instalar desde un archivo** que ya tengas en disco, o **guardar opciones avanzadas** (ruta personalizada del ejecutable de VRChat, manifiesto alternativo, etc.) si tu caso lo requiere; eso es opcional y está pensado para usuarios avanzados.

---

## Resumen

| Qué | Para qué |
|-----|----------|
| **Manifiesto en la raíz** | Que VRCMT sepa qué versión del stub ofrecer y desde dónde descargarla con comprobación de integridad. |
| **Releases** | Alojar el ejecutable sustituto que VRChat usará tras la instalación desde VRCMT. |
| **Este README** | Explicar en qué consiste el stub y cómo encaja con los botones y apartados de VRCMT, **sin publicar código**. |

Si solo usas VRCMT como reproductor de biblioteca y **no** activas la mejora de YouTube para VRChat, **no necesitas** hacer nada con este repositorio: el stub es **opcional** y solo afecta a cómo VRChat pide los vídeos de YouTube cuando tú decides activarlo desde VRCMT.
