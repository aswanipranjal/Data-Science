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

	