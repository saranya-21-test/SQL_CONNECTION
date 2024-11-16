import pymongo
cliet=pymongo.MongoClient("mongodb://localhost:27017")
db=cliet["ACT_DB"]
coll=db["STU_DB"]
for i in coll.find():
    print("student details:\n",i)