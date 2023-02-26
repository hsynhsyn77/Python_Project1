import certifi
import pymongo

#myclient=pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient(
    "mongodb+srv://hsynhsyn77:yExK37723vGw69kN@cluster0.ydhqrjt.mongodb.net/node-app?retryWrites=true&w=majority", tlsCAFile=certifi.where())

mydb = myclient["node-app"]
mycollection = mydb["products"]

#result=mycollection.find_one()
for i in mycollection.find({},{"_id":0}):
    print(i)

#print(result)