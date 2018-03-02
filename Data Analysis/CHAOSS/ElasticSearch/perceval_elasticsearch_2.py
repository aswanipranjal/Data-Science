from perceval.backends.core.git import Git
import elasticsearch

# Url for the git repo to analyze
repo_url = 'http://github.com/grimoirelab/perceval.git'
# Directory for letting Perceval clone the git repo
repo_dir = '/tmp/perceval.git'
# ElasticSearch instance (url)
es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

# Create the 'commits' index in ElasticSearch
# if it already exisits, first delete it and then create it.
try:
    es.indices.create('commits')
except elasticsearch.exceptions.RequestError:
    es.indices.delete('commits')
    es.indices.create('commits')
# Create a Git object, pointing to repo_url, using repo_dir for cloning
repo = Git(uri=repo_url, gitpath=repo_dir)
# Fetch all commits as an iteratoir, and iterate it uploading to ElasticSearch
for commit in repo.fetch():
    # Create the object (dictionary) to upload to ElasticSearch
    summary = {'hash': commit['data']['commit']}
    print(summary)
    # Upload the object to ElasticSearch
es.index(index='commits', doc_type='summary', body=summary)