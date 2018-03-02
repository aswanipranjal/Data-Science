import email.utils

from perceval.backends.core.mbox import MBox
import elasticsearch

# uri (label) for the mailing list to analyze
mbox_uri = 'http://mail-archives.apache.org/mod_mbox/httpd-announce/'
# directory for letting Perceval where mbox archives are
# you need to have the archives to analyzed there before running the script
mbox_dir = 'archives'
# ElasticSearch instance (url)
es = elasticsearch.Elasticsearch(['http://localhost:9200/'])

# Create the 'messages' index in ElasticSearch
try:
    es.indices.create('messages')
except elasticsearch.exceptions.RequestError:
    print('Index already exisits, remove it before running this script again.')
    exit()

# create a mbox object, using mbox_uri as label, mbox_dir as directory to scan
repo = MBox(uri=mbox_uri, dirpath=mbox_dir)

# Fetch all commits as an iteratoir, and iterate it uploading to ElasticSearch
print('Analyzing mbox archives...')
# fetch all messages as an iteratoir
for message in repo.fetch():
    # Create the object (dictionary) to upload to ElasticSearch
    summary = {
        'from': message['data']['From'],
        'subject': message['data']['Subject'],
        'date': email.utils.parsedate_to_datetime(message['data']['Date'])
        }
    print('.', end='')
    # Upload the object to ElasticSearch
    es.index(index='messages', doc_type='summary', body=summary)