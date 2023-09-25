import os
import unittest
import shutil
from WaferQualityCheck.db.mongoops import MongoOps
from WaferQualityCheck.db import qualitychecks


class TestMongoOps(unittest.TestCase):

    def setUp(self):
        """
        Set up the test case by creating an instance of MongoOps for testing with 'test' credentials.
        """
        self.mongo_obj = MongoOps(credentials='test')

    def test_db1_insert_data(self):
        """
        Test inserting data into the collection and check if the count matches.
        """
        # Set the data directory for quality checks
        qualitychecks.DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "db", "Unittest_Batch_Files"))
        qualitychecks.main(credentials="test")

        # Count the documents in the collection
        count = self.mongo_obj.col.count_documents({})

        # Assert that the count matches the expected value
        self.assertEqual(count, 5)

    def test_db2_delete_collection(self):
        """
        Test deleting the collection and check if it's not in the list of collections.
        """
        # Delete the collection
        self.mongo_obj.drop(database=False)

        # Get the list of collections in the database
        collections = self.mongo_obj.db.list_collection_names()

        # Assert that the collection name is not in the list of collections
        self.assertNotIn(self.mongo_obj.col.name, collections)

    def test_db3_delete_database(self):
        """
        Test deleting the database and check if it's not in the list of databases.
        """
        # Delete the entire database
        self.mongo_obj.drop()

        # Get the list of databases in the MongoDB server
        databases = self.mongo_obj.client.list_database_names()

        # Assert that the database name is not in the list of databases
        self.assertNotIn(self.mongo_obj.db.name, databases)

    def test_db4_revert_data(self):
        """
        Test reverting data files.
        """
        FILES = ["Wafer_31022023_000000.csv", "Wafer_31022023_111.csv"]
        UNITTEST_DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "db", "Unittest_Batch_Files"))
        for file in FILES:
            shutil.move(src=os.path.join(qualitychecks.INVALID_FILES_DIR, file),
                        dst=UNITTEST_DATA_DIR)

        # Check if the number of files in the test directory matches the expected count
        self.assertEqual(len(os.listdir(UNITTEST_DATA_DIR)), 3)


if __name__ == '__main__':
    unittest.main()

