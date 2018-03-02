from perceval.backends.core.git import Git
import elasticsearch

# A more complex index for git metadata.
# For each commit, it will have fields for hash, author, committer, author date

repo_url = 'https://github.com/grimoirelab/perceval.git'
repo_dir = '/tmp/perceval.git'

es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

try:
	es.indices.create('commits')
except elasticsearch.exceptions.RequestError:
	print('Index already exists, remove it before running this script again')
	exit()

repo = Git(uri=repo_url, gitpath=repo_dir)

print('Analysing git repo')	
for commit in repo.fetch():
	summary = {
		'hash': commit['data']['commit'],
		'author': commit['data']['Author'],
		'author_date': commit['data']['AuthorDate'],
		'commit': commit['data']['Commit']
		'commit_date': commit['data']['CommitDate'],
		'files_no': len(commit['data']['files'])
	}
	print('.', end='')
	es.index(index='commits', doc_type='summary', body=summary)

print('\nCreated new index with commits')