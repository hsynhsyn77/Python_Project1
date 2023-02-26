import certifi
import pymongo
from bson.objectid import ObjectId

# myclient=pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient(
    "mongodb+srv://hsynhsyn77:yExK37723vGw69kN@cluster0.ydhqrjt.mongodb.net/node-app?retryWrites=true&w=majority",
    tlsCAFile=certifi.where())

mydb = myclient["node-app"]
mycollection = mydb["products"]

#mycollection.update_one(
#    {"name":"Samsung S6"},
#    {"$set":{
#        "name":"Iphone XS MAX",
#        "price":15000
#    }}
#)
query={"name":"Samsung S7"}
newvalues= {"$set":{
            "name":"Iphone 11",
            "price":20000
            }}
result=mycollection.update_many(query,newvalues)

print(f"{result.modified_count} adet kayıt güncellendi.")

for i in mycollection.find():
    print(i)