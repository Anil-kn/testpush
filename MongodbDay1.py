import pymongo

client = pymongo.MongoClient("mongodb+srv://anilkumar:anil123@cluster0.dsrswfm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name": "anil",
    "email": "anilkumarkn298@gmail.com",
    "surname": "kumar"
}

db1 = client['mongotest']
coll=db1['test']
coll.insert_one(d)
