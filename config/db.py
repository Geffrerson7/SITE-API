from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("DATABASE_URI"))

