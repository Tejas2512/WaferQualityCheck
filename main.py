# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi



# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

from pymongo import MongoClient


mongo_pwd = "zfpvdQzVsLcRcgvM"

uri = f"mongodb+srv://waferQuality:{mongo_pwd}@cluster0.va0if0g.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(uri)
db = client["waferquality"]
collection = db["sensors"]

# Document to insert
document = {
    "name": "John Doe"}

# Insert the document into the collection
result = collection.delete_many(document)

# Print the inserted document's ID
# print("Inserted document ID:", result.inserted_ids)
