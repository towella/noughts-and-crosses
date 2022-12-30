# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Noughts_and_Crosses.py'],
             pathex=['/Users/towell/Documents/Andrew/python/Noughts_and_Crosses'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('freesansbold.ttf', '/Users/towell/Documents/Andrew/python/Noughts_and_Crosses/freesansbold.ttf', "DATA")]
a.scripts += [('text_box.py', '/Users/towell/Documents/Andrew/python/Noughts_and_Crosses/text_box.py', "SCRIPT")]
a.scripts += [('board.py', '/Users/towell/Documents/Andrew/python/Noughts_and_Crosses/board.py', "SCRIPT")]
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Noughts_and_Crosses',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='Noughts_and_Crosses.app',
             icon='/Users/towell/Documents/Andrew/python/Noughts_and_Crosses/app_icon',
             bundle_identifier=None)
