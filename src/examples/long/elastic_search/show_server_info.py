""" show_server_info.py """

from elasticsearch import Elasticsearch
client = Elasticsearch(hosts="http://localhost:9200")
print(client.info())
