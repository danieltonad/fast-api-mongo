from pymongo import MongoClient

client = MongoClient("")

db = client.fast_api_mongodb

collection_name = db["fast_api_mongodb"]