from pymongo import MongoClient  # type: ignore

# wrg2RWZEmi70BPCM

# conn = MongoClient("mongodb://localhost:27017/")
conn = MongoClient(
    "mongodb+srv://subhadipdas4521:wrg2RWZEmi70BPCM@cluster0.6ad5a.mongodb.net/"
)

db = conn.Users
collection = db.User
