from pymongo import MongoClient

client = MongoClient("mongodb+srv://bitfliplive:Hh7N5bWdimzuoeLI@cluster0.cuzkoiv.mongodb.net/?retryWrites=true&w=majority")

db = client.fast_api_mongodb

collection_name = db["fast_api_mongodb"]