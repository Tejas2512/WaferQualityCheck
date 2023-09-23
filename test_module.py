import unittest
from db.mongoops import MongoOps  # Assuming your class is defined in 'mongo_ops.py'


class TestMongoOps(unittest.TestCase):

    def setUp(self):
        self.mongo_obj = MongoOps(credentials='test')

    # def tearDown(self):
    #     # Drop the collection after each test
    #     self.mongo_obj.drop(self.mongo_obj.col, database=False)

    # def tearDownClass(self):
    #     # Drop the database at the end of all tests
    #     self.mongo_obj.drop(self.mongo_obj.db)

    def test_insert_data(self):
        # Test inserting data into the collection
        documents = [{"name": "John"}, {"name": "Alice"}]
        self.mongo_obj.add(documents)
        count = self.mongo_obj.col.count_documents({})
        self.assertEqual(count, 2)

    # def test_update_data(self):
    #     # Test updating data in the collection
    #     document = {"name": "Bob"}
    #     self.mongo_obj.add([document])
    #     self.mongo_obj.update()
    #     updated_document = self.mongo_obj.col.find_one({"name": "Bob"})
    #     self.assertIsNotNone(updated_document)
    #
    # def test_remove_data(self):
    #     # Test removing data from the collection
    #     document = {"name": "Eve"}
    #     self.mongo_obj.add([document])
    #     self.mongo_obj.remove()
    #     removed_document = self.mongo_obj.col.find_one({"name": "Eve"})
    #     self.assertIsNone(removed_document)

    # def test_create_collection(self):
    #     # Test creating a collection
    #     self.mongo_obj.create(database=False)
    #     collections = self.db.list_collection_names()
    #     self.assertIn(self.collection_name, collections)

    # def test_delete_collection(self):
    #     # Test deleting a collection
    #     self.mongo_ops.remove(one=False)
    #     collections = self.db.list_collection_names()
    #     self.assertNotIn(self.collection_name, collections)

if __name__ == '__main__':
    unittest.main()
