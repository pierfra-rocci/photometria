# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['rapas_app.py'],
    pathex=[],
    binaries=[],
    datas=[("C:/Users/pierf/astronomy/.astronomy/Lib/site-packages/altair/vegalite/v5/schema/vega-lite-schema.json",
        "./altair/vegalite/v5/schema/"),
        ("C:/Users/pierf/astronomy/.astronomy/Lib/site-packages/streamlit/static",
        "./streamlit/static"),
        ("C:/Users/pierf/astronomy/.astronomy/Lib/site-packages/streamlit/runtime",
        "./streamlit/runtime"),
("C:/Users/pierf/astronomy/.astronomy/Lib/site-packages/astroquery/CITATION", 'astroquery'),
("C:/Users/pierf/astronomy/.astronomy/Lib/site-packages/astroquery/simbad/data/query_criteria_fields.json", 
        'astroquery/simbad/data'),
         ("C:/Users/pierf/astronomy/.astronomy/Lib/site-packages/streamlit-X.Y.Z.dist-info", 
        "streamlit-1.42.2.dist-info")],
    hiddenimports=['streamlit'],
    hookspath=['./hooks'],
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
    name='rapas_app',
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
