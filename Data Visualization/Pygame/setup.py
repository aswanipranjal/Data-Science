import cx_Freeze

executables = [cx_Freeze.Executable('pg2.py')]

cx_Freeze.setup(
	name='Smart Rockets',
	options={'build_exe': {'packages':['pygame'],
						   'include_files':['C:/Users/Aman Deep Singh/Documents/Python/Data Science/Data Visualization/Pygame/racecar.png']}},
	executables=executables
	)