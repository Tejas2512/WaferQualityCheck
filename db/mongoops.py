from pymongo import MongoClient
import json


class MongoOps:
    def __init__(self):
        with open('cred.json') as file:
            cred = json.loads(file.read())
        uri = cred['uri']
        client = MongoClient(uri)
        db = client[cred['database']]
        self.col = db[cred['collection']]

    def create(self, database=True):
        pass

    def update(self):
        pass

    def add(self, documents: list):
        self.col.insert_many(documents)

    def remove(self, one=True):
        pass

    def fetch_data(self):
        return self.col.find()