# The data produced by Perceval can be stored in persistent storage.
# It can be uploaded to a database.
# In this section we will do it with ElasticSearch

# ElasticSearch provides a REST API

from perceval.backends.core.git import Git
import elasticsearch

# Url for the git repo
repo_url = 'https://github.com/grimoirelab/perceval.git'
# Directory for letting Perceval clone the git repo
repo_dir = '/tmp/perceval.git'

# ElasticSearch instance
es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

# Create the 'commits' index in ElasticSearch
es.indices.create('commits')

# create a Git object, pointing to repo_url, using repo_dir for cloning
repo = Git(uri=repo_url, gitpath=repo_dir)

# fetch all commits as an iterator, and iterate it uploading to ElasticSearch
for commit in repo.fetch():
	summary = {'hash': commit['data']['commit']}
	print(summary)
	# upload the object to ElasticSearch
	es.index(index='commits', doc_type='summary', body=summary)