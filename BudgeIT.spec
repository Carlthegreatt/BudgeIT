# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('budgeit/assets', 'budgeit/assets'),
        ('requirements.txt', '.'),
    ],
    hiddenimports=[
        'PySide6.QtSql',
        'PySide6.QtWidgets',
        'PySide6.QtCore', 
        'PySide6.QtGui',
        'sqlite3',
        'email.mime.multipart',
        'email.mime.text',
        'smtplib',
        'matplotlib.backends.backend_qt5agg',
        'matplotlib.backends.backend_qtagg', 
        'matplotlib.figure',
        'matplotlib.pyplot',
        'numpy',
        'budgeit.assets.icons.icons_rc',
        'budgeit.assets.images.images_rc',
    ],
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
    name='BudgeIT',
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
    icon='budgeit/assets/icons/favicon.ico',
)
