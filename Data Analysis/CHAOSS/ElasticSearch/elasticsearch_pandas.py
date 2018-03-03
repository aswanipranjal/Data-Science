from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import pandas as pd

# We will create an object for accessing the ElasticSearch instance.
# In this case, we will assume that it is running on our system with its REST interface available in port 9200
# verify_certs will be necessary if you're connecting to an ElasticSearch over TLS (https) with a bad certificate
es = Elasticsearch('http://localhost:9200', verify_certs=False)

# The enriched indexes store one document per commit
# The query builds buckets of commits, grouped by author name,
# aggregated as first commit for each of these authors
s = Search(using=es, index='git')
s.aggs.buckets('by_authors', 'terms', field='author_name', size=10000).metric('first_commit', 'min', field='author_date')
s = s.sort('author_date')