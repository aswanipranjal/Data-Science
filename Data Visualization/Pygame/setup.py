import cx_Freeze
import sys
import os
import pygame

os.environ['TCL_LIBRARY'] = r'C:\Users\Aman Deep Singh\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Aman Deep Singh\Anaconda3\tcl\tk8.6'

base = None

if sys.platform == 'win32':
	base = "Win32GUI"
executables = [cx_Freeze.Executable("pg2.py", base=base)]

cx_Freeze.setup(
	name="Smart Rockets",
	options={"build_exe": {"packages":["pygame"],
						   "include_files":["racecar.png",
						   					"C:/Users/Aman Deep Singh/Anaconda3/DLLs/tcl86t.dll",
						   					"C:/Users/Aman Deep Singh/Anaconda3/DLLs/tk86t.dll"]}},
	executables=executables,
	version='1.0.0'
	)