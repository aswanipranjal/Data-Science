import subprocess
from sys import argv

token = argv[1]
repos = ['perceval', 'arthur', 'grimoireelk', 'sortinghat', 'mordred', 'panels', 'training']

for repo in repos:
	subprocess.run(['p2o.py', '--enrich', '--index', 'git_raw', '--index-enrich', 'git', '-e', 'http://localhost:9200', '--no_inc', '--debug', 'git', 'http://github.com/grimoirelab/' + repo])