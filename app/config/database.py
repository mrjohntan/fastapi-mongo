from pymongo import MongoClient

client = MongoClient("mongodb://testadmin:Passw0rd123@localhost:27017/?tls=false&authSource=admin")

db = client.todo_db

collection_name = db["todo_collection"]