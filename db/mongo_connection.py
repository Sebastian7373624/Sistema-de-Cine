from pymongo import MongoClient # type: ignore

MONGO_URI = "mongodb+srv://admin-cine:cine12345@cluster0.si5yrhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client['cine_db']
