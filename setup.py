from setuptools import setup

APP = ['main.py']
PKGS = ['pandas', 'cryptography']
OPTIONS = {'iconfile': '64.png', 'argv_emulation': False, 'includes': ['cryptography.fernet', '_cffi_backend'], 'packages': ['pandas'] }
DATA_FILES = ['theme.stylesheet', 'data.csv']

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['pandas', 'py2app']
)
