import json
import os
from logging import debug, info
from pathlib import Path
from pprint import pformat

from backend.env_manager import setup_env
from elasticsearch import Elasticsearch


class Search:
    def __init__(self):
        setup_env()
        elastic_url = os.getenv("ELASTIC_URL")
        password = os.getenv("ELASTIC_PASSWORD")

        info(f"Connecting to elasticsearch at '{elastic_url}'")
        self.es = Elasticsearch(elastic_url, basic_auth=("elastic", password))
        client_info = self.es.info()
        info("Connected to Elasticsearch!")
        debug(pformat(client_info.body))

    def create_index(self):
        self.es.indices.delete(index="my_documents", ignore_unavailable=True)
        self.es.indices.create(index="my_documents")

    def insert_document(self, document):
        return self.es.index(index="my_documents", body=document)

    def insert_documents(self, documents):
        operations = []
        for document in documents:
            operations.append({"index": {"_index": "my_documents"}})
            operations.append(document)
        return self.es.bulk(operations=operations)

    def reindex(self):
        self.create_index()
        with open(Path(__file__).parents[1] / "data/quotes.json", "r") as file:
            documents = json.load(file)
        return self.insert_documents(documents)

    def search(self, **query_args):
        return self.es.search(index="my_documents", **query_args)

    def retrieve_document(self, id):
        return self.es.get(index="my_documents", id=id)


search_engine = Search()
