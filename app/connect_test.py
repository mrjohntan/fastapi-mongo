from pymongo.mongo_client import MongoClient

uri = "mongodb://testadmin:Passw0rd123@localhost:27017/?tls=false&authSource=admin"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)