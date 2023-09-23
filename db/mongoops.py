from pymongo import MongoClient
import json


class MongoOps:
    def __init__(self, credentials='default'):
        # Load the credentials from the JSON file
        with open('cred.json') as file:
            cred_file = json.loads(file.read())

        # Use the specified credentials or the default if not provided
        selected_cred = cred_file.get(credentials, cred_file.get('default'))

        uri = selected_cred['uri']
        self.client = MongoClient(uri)
        self.db = self.client[selected_cred['database']]
        self.col = self.db[selected_cred['collection']]

    def drop(self, database=True):
        if database:
            self.client.drop_database(self.db)
        else:
            self.db.drop_collection(self.col)

    def update(self):
        pass

    def add(self, documents: list):
        self.col.insert_many(documents)

    def remove(self, one=True):
        pass

    def fetch_data(self):
        return self.col.find()
