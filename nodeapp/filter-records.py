import certifi
import pymongo
from bson.objectid import ObjectId

# myclient=pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient(
    "mongodb+srv://hsynhsyn77:yExK37723vGw69kN@cluster0.ydhqrjt.mongodb.net/node-app?retryWrites=true&w=majority",
    tlsCAFile=certifi.where())

mydb = myclient["node-app"]
mycollection = mydb["products"]

result = mycollection.find_one({"name": "Samsung S6"})
# result=mycollection.find_one({"_id":ObjectId("63fba946d5279fdfb39ae3fe")})

# result=mycollection.find({
#    "name":{
#        "$in":["Samsung S6","Samsung S7"]
#    }
# })

# result=mycollection.find({
#    "price":{
#        "$gte":2000
#    }
# })

# result=mycollection.find({
#    "price":{
#        "$lte":2000
#    }
# })

result = mycollection.find({
    "name": {"$regex": "^S"}
})

for i in result:
    print(i)
