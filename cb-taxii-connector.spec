from PyInstaller.utils.hooks import get_package_paths, collect_data_files

datas = [(get_package_paths('cbint')[1], 'cbint')]
datas.extend([(get_package_paths('cbfeeds')[1], 'cbfeeds')])
datas.extend([(get_package_paths('cybox')[1], 'cybox')])
datas.extend([(get_package_paths('orderedmultidict')[1] + "/__version__.py", 'orderedmultidict')])
datas.extend([(HOMEPATH + '/cbapi/response/models/*', 'cbapi/response/models/'),
             (HOMEPATH + '/cbapi/protection/models/*', 'cbapi/protection/models/'),
             (HOMEPATH + '/cbapi/psc/threathunter/models/*', 'cbapi/psc/threathunter/models/'),
             (HOMEPATH + '/cbapi/psc/livequery/models/*', 'cbapi/psc/livequery/models/'),
             (HOMEPATH + '/cbapi/psc/defense/models/*', 'cbapi/psc/defense/models/'),
             (HOMEPATH + '/cbapi/psc/models/*', 'cbapi/psc/models/') ])

a = Analysis(['scripts/cb-taxii-connector'],
             pathex=['.'],
             hiddenimports=['cbint','cbint.utils.cbserver', 'cbint.utils.bridge', 'cbfeeds', 'cbfeeds.feed', 'unicodedata',
                            'parsedatetime.pdt_locales.de_DE',
                            'parsedatetime.pdt_locales.en_AU',
                            'parsedatetime.pdt_locales.en_US',
                            'parsedatetime.pdt_locales.es',
                            'parsedatetime.pdt_locales.nl_NL',
                            'parsedatetime.pdt_locales.pt_BR',
                            'parsedatetime.pdt_locales.ru_RU',
                            'parsedatetime.pdt_locales.fr_FR'
],
             datas=datas,
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='cb-taxii-connector',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='cb-taxii-connector')
