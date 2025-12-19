# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('choco_install.bat', '.'), ('codeblocks_install.bat', '.'), ('java_install.bat', '.'), ('jetbrain_install.bat', '.'), ('mingw_install.bat', '.'), ('netbeans_install.bat', '.'), ('python_install.bat', '.'), ('vsc_install.bat', '.'), ('Iverilog.bat', '.'), ('Gtkwave.bat', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Byte_Wizard_Ready',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
