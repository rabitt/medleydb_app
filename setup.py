"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import py2app

APP = ['new_multitrack.py']
DATA_FILES = ['taxonomy.yaml', 'medley-icon.png']
OPTIONS = {'argv_emulation': True,
	'iconfile': 'homer.icns',
	'includes': ['glob', 'PyQt4', 'sys', 'os', 'yaml', 'functools', 'medleydb',
				 'copy', 're', 'struct','wave']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
