import certifi
import pymongo
from bson.objectid import ObjectId

# myclient=pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient(
    "mongodb+srv://hsynhsyn77:yExK37723vGw69kN@cluster0.ydhqrjt.mongodb.net/node-app?retryWrites=true&w=majority",
    tlsCAFile=certifi.where())

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print("*"*50)

#mycollection.delete_one({"name":"Samsung S8"})
#mycollection.delete_many({"name":{"$regex":"^S"}})
result=mycollection.delete_many({})

print(f"{result.deleted_count} adet kayıt silindi.")


for i in mycollection.find():
    print(i)