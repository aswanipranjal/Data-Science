import datetime

from perceval.backends.core.git import Git
import elasticsearch

# Url for the git repo to analyze
repo_url = 'http://github.com/grimoirelab/perceval.git'
# Directory for letting Perceval clone the git repo
repo_dir = '/tmp/perceval.git'
# ElasticSearch instance (url)
es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

# Create the 'commits' index in ElasticSearch
try:
    es.indices.create('commits')
except elasticsearch.exceptions.RequestError:
    print('Index already exisits, remove it before running this script again.')
    exit()
# Create a Git object, pointing to repo_url, using repo_dir for cloning
repo = Git(uri=repo_url, gitpath=repo_dir)
# Fetch all commits as an iteratoir, and iterate it uploading to ElasticSearch
print('Analyzing git repo...')
for commit in repo.fetch():
    # Create the object (dictionary) to upload to ElasticSearch
    summary = {
        'hash': commit['data']['commit'],
        'author': commit['data']['Author'],
        'author_date': datetime.datetime.strptime(commit['data']['AuthorDate'],
                                                "%a %b %d %H:%M:%S %Y %z"),
        'commit': commit['data']['Commit'],
        'commit_date': datetime.datetime.strptime(commit['data']['CommitDate'],
                                                "%a %b %d %H:%M:%S %Y %z"),
        'files_no': len(commit['data']['files'])
        }
    print('.', end='')
    # Upload the object to ElasticSearch
    es.index(index='commits', doc_type='summary', body=summary)

print('\nCreated new index with commits.')