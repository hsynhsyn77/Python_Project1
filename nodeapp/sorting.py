import certifi
import pymongo
from bson.objectid import ObjectId

# myclient=pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient(
    "mongodb+srv://hsynhsyn77:yExK37723vGw69kN@cluster0.ydhqrjt.mongodb.net/node-app?retryWrites=true&w=majority",
    tlsCAFile=certifi.where())

mydb = myclient["node-app"]
mycollection = mydb["products"]

#result=mycollection.find().sort("name",-1)
#result=mycollection.find().sort("price",-1)
result=mycollection.find().sort([("name",1),("price",-1)])

for i in result:
    print(i)