# We will query items whose `from` property includes the string 'Jim'
import elasticsearch

es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

es_result = es.search(index='messages', doc_type='summary', body={'query': {'match': {'from': 'Jim'}}})
print(f"Found {es_result['hits']['total']} messages")

for message in es_result['hits']['hits']:
	print(f"Sender: {message['_source']['from']}\nSubject: {message['_source']['subject']}")