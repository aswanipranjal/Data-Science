import sys
from cx_Freeze import setup, Executable
base = None

executables = [Executable("C:\\Users\\Aman Deep Singh\\Documents\\Python\\Data Science\\Data Visualization\\car_ai_genes.py", base)]

packages = ["idna"]
options = {
	'build-exe': {
	'packages':packages,
	},
}
# exe = Executable(
# 	script = r"C:\\Users\\Aman Deep Singh\\Documents\\Python\\Data Science\\Data Visualization\\car_ai_genes.py",
# 	base="Win32GUI",
# 	)

setup(
	name="Genes",
	options=options,
	version="1.0",
	description="Plots genetic data live",
	executables=executables
	)