# Query data from this index
import elasticsearch

es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

es_result = es.search(index='messages')

print(f'Found {es_result['hits']['total']} messages')
for message in es_result['hits']['hits']:
	print(f'Sender: {message['_source']['from']}\nSubject: {message['_source']['subject']}')