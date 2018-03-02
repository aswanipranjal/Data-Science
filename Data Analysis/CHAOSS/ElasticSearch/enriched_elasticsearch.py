from datetime import datetime
from pprint import pprint

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

es = Elasticsearch(['http://localhost:9200'])
index = 'git'

# counting total number of commits
s = Search(using=es, index=index)
total = s.count()
print('Count of total number of commits in index: ', total)

# counting number of unique commits
s = Search(using=es, index=index)
s.aggs.metric('commits', 'cardinality', field='hash')
unique = s.count()
print('Count of unique commits in index: ', unique)