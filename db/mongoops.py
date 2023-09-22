from pymongo import MongoClient


class MongoOps:
     def __init__(self):
         mongo_pwd = "zfpvdQzVsLcRcgvM"
         uri = f"mongodb+srv://waferQuality:{mongo_pwd}@cluster0.va0if0g.mongodb.net/?retryWrites=true&w=majority"
         client = MongoClient(uri)
         db = client["waferquality"]
         self.col = db["sensors"]
     
     def create(self, database=True):
         pass
     
     def update(): 
         pass
     
     def add(self, documents:list):
         self.col.insert_many(documents)
              
     def remove(self, one=True):
         pass
     