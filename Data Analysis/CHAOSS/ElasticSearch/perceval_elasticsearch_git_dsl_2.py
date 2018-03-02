import elasticsearch
import elasticsearch_dsl
# get only some fields

es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

# Build a DSL search object on the `commits` index, `summary` document type
request = elasticsearch_dsl.Search(using=es, index='commits', doc_type='summary')
request = request.source(['hash', 'author_date', 'author'])

# run the search, using the scan interface to get all results
response = request.scan()
for commit in response:
	print(commit.hash, commit.author_date, commit.author)