import elasticsearch
import elasticsearch_dsl
# get the last commits

es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

# Build a DSL search object on the `commits` index, `summary` document type
request = elasticsearch_dsl.Search(using=es, index='commits', doc_type='summary')
request = request.sort('-commit_date')
request = request.source(['hash', 'author_date', 'author'])
request = request[0:20]

# run the search, using the scan interface to get all results
response = request.execute()
# instead of `scan()` we use `execute()` which allows for slicing, and preserves order.
for commit in response:
	print(commit.hash, commit.author_date, commit.author)