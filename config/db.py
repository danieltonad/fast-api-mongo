from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.environ.get("MG_CONN_STR"))

db = client.fast_api_mongodb

collection_name = db["fast_api_mongodb"]