from perceval.backends.core.git import Git
import elasticsearch

repo_url = 'https://github.com/grimoirelab/perceval.git'
repo_dir = '/tmp/perceval.git'

es = elasticsearch.Elasticsearch(['https://localhost:9200/'])

# create the 'commits' index in ElasticSearch
# if it already exists, first delete it and then create it
try:
	es.indices.create('commits')
except elasticsearch.exceptions.RequestError:
	es.indices.delete('commits')
	es.indices.create('commits')

repo = Git(uri=repo_url, gitpath=repo_dir)

for commit in repo.fetch():
	summary = {'hash': commits['data']['commit']}
	print(summary)

	es.index(index='commits', doc_type='summary', body=summary)