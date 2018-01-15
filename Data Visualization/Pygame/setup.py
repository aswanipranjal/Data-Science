import cx_Freeze

executables = [cx_Freeze.Executable('pg2.py')]

cx_Freeze.setup(
	name='Smart Rockets',
	options={'build_exe': {'packages':['pygame'],
						   'include_files':['racecar.png']}},
	executables=executables
	)