import datetime

from perceval.backends.core.git import Git
import elasticsearch

repo_url = 'http://github.com/grimoirelab/perceval.git'
repo_dir = '/tmp/perceval.git'

es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

try:
	es.indices.create('commits')
except elasticsearch.exceptions.RequestError:
	print('Index already exists, remove it before running this script again.')
	exit()

repo = Git(uri=repo_url, gitpath=repo_dir)

print('Analysing the repo')
for commit in repo.fetch():
	summary = {
		'hash': commit['data']['commit'],
		'author': commit['data']['Author'],
		'author_date': datetime.datetime.strptime(commit['data']['AuthorDate'], "%a %b %d %H:%M:%S %Y %z"),
		'commit': commit['data']['Commit'],
		'commit_date': datetime.datetime.strptime(commit['data']['CommitDate'], "%a %b %d %H:%M:%S %Y %z"),
		'files_no': len(commit['data']['files'])
	}
	print('.', end='')
	es.index(index='commits', doc_type='summary', body=summary)

print('\nCreated new index with commits.')