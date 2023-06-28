from pymongo import MongoClient

db_connection = MongoClient('MONGO_URL')
db = db_connection.database_name
collection = db['collection_name']

