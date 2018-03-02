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

# ignoring commits touching no files
s = Search(using=es, index=index)
s = s.filter('range', files={'gt':0})
s.aggs.metric('commits', 'cardinality', field='hash')
unique_no_empty = s.count()
print('Count of unique commits in index: ', unique_no_empty)

# counting number of unique commits, ignoring those touching no files, and newer than a certain date
s = Search(using=es, index=index)
s = s.filter('range', files={'gt':0})
s = s.filter('range', author_date={'gt': datetime(2016, 7, 1)})
s.aggs.metric('commits', 'cardinality', field='hash')
unique_after = s.count()
print('Count of unique commits in index, authored later than July 1st, 2016: ', unique_after)

# counting number of unique commits, ignoring thouse touching no files, and newer than a certain date, grouping them by quarter
s = Search(using=es, index=index)
s = s.filter('range', files={'gt':0})
s = s.filter('range',author_date={'gt':datetime(2016, 7, 1)})
s.aggs.metric('commits', 'cardinality', field='hash')
s.aggs.bucket('histogram', 'date_histogram', field='author_date', interval='quarter')
by_quarter = s.execute()
print('Aggregations returned by quarter')
pprint(by_quarter.to_dict()['aggregations'])
for quarter in by_quarter.to_dict()['aggregations']['histogram']['buckets']:
	print('Unique commits for quarter starting on', quarter['key_as_string'], ':', quarter['doc_count'])