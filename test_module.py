import unittest
from db.mongoops import MongoOps


class TestMongoOps(unittest.TestCase):
    def setUp(self):
        # Create an instance of MongoOps for testing with 'test' credentials
        self.mongo_obj = MongoOps(credentials='test')

    def test_insert_data(self):
        """
        Test inserting data into the collection and check if the count matches.
        """
        # Prepare sample data
        documents = [{"name": "John"}, {"name": "Alice"}]

        # Insert data into the collection
        self.mongo_obj.add(documents)

        # Count the documents in the collection
        count = self.mongo_obj.col.count_documents({})

        # Assert that the count matches the expected value
        self.assertEqual(count, 2)

    def test_delete_collection(self):
        """
        Test deleting the collection and check if it's not in the list of collections.
        """
        # Delete the collection
        self.mongo_obj.drop(database=False)

        # Get the list of collections in the database
        collections = self.mongo_obj.db.list_collection_names()

        # Assert that the collection name is not in the list of collections
        self.assertNotIn(self.mongo_obj.col.name, collections)

    def test_delete_database(self):
        """
        Test deleting the database and check if it's not in the list of databases.
        """
        # Delete the entire database
        self.mongo_obj.drop()

        # Get the list of databases in the MongoDB server
        databases = self.mongo_obj.client.list_database_names()

        # Assert that the database name is not in the list of databases
        self.assertNotIn(self.mongo_obj.db.name, databases)


if __name__ == '__main__':
    unittest.main()
