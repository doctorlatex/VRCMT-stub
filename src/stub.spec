# stub.spec -- PyInstaller 6.x spec para VRCMT yt-dlp stub
# Uso: cd src && pyinstaller stub.spec --clean --noconfirm
# Output: src/dist/yt-dlp.exe

block_cipher = None

a = Analysis(
    ['stub_main.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=['yt_dlp'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='yt-dlp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
