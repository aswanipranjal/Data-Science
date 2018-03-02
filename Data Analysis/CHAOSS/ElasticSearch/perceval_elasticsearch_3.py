from perceval.backends.core.git import Git
import elasticsearch

# A more complex index for git metadata.
# For each commit, it will have fields for hash, author, committer, author date

repo_url = 'https://github.com/grimoirelab/perceval.git'
repo_dir = '/tmp/perceval.git'

es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

try:
