from pymongo import MongoClient
import json
import os


class MongoOps:
    def __init__(self, credentials='default'):
        """
        Initializes a MongoDB connection using the specified credentials or the default credentials.

        Args:
            credentials (str): The name of the credentials to use from the 'cred.json' file.

        Raises:
            FileNotFoundError: If the 'cred.json' file is not found.
            KeyError: If the specified or default credentials are missing keys.

        """
        # Load the credentials from the JSON file
        file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cred.json'))
        with open(file_name) as file:
            cred_file = json.loads(file.read())

        # Use the specified credentials or the default if not provided
        selected_cred = cred_file.get(credentials, cred_file.get('default'))

        # Extract relevant information from the credentials
        uri = selected_cred['uri']
        database_name = selected_cred['database']
        collection_name = selected_cred['collection']

        # Create a MongoDB client, database, and collection
        self.client = MongoClient(uri)
        self.db = self.client[database_name]
        self.col = self.db[collection_name]

    def drop(self, database=True):
        """
        Drops the database or collection.

        Args:
            database (bool): If True, drops the entire database; if False, drops the collection.

        """
        if database:
            self.client.drop_database(self.db.name)
        else:
            self.col.drop()

    def update(self):
        """
        Placeholder for an update operation.
        """
        pass

    def add(self, documents: list):
        """
        Adds documents to the collection.

        Args:
            documents (list): A list of dictionaries representing documents to be inserted.

        """
        self.col.insert_many(documents)

    def remove(self, one=True):
        """
        Placeholder for a remove operation.

        Args:
            one (bool): If True, removes one document; if False, removes multiple documents.

        """
        pass

    def fetch_data(self):
        """
        Retrieves data from the collection.

        Returns:
            pymongo.cursor.Cursor: A cursor for querying the collection.

        """
        return self.col.find()
