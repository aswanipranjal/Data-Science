import email.utils

from perceval.backends.core.mbox import MBox
import elasticsearch

mbox_uri = 'http://mail-archives.apache.org/mod_mbox/httpd-announce/'
mbox_dir = 'archives'

es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

try:
	es.indices.create('message')
except elasticsearch.exception.RequestError:
	print('Index already exists, remove it before running this script again.')
	exit()

repo = MBox(uri=mbox_uri, dirpath=mbox_dir)

print('Analysing mbox archives')
for message in repo.fetch():
	summary = {
		'from': message['data']['From'],
		'subject': message['data']['Subject'],
		'date': email.utils.parsedate_to_datetime(message['data']['Date'])
	}
	print('.', end='')
	es.index(index='message', doc_type='summary', body=summary)