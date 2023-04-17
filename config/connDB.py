from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
# user_collection = db['user']
