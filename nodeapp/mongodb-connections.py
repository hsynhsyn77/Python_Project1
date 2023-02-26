import pymongo

# myclient=pymongo.MongoClient("mongodb://localhost:27017")
myclient = pymongo.MongoClient(
    "mongodb+srv://hsynhsyn77:5pgvIG7INN0WrVtN@cluster0.ydhqrjt.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
# mycollection = mydb["products"]
print(myclient.list_database_names())

# product = {"name": "Samsung S5", "price": 2000}
#
# result = mycollection.insert_one(product)
# print(result)
# print(type(result))
# print(result.inserted_id)

# productList = [
#    {"name": "Samsung S6", "price": 3000,"description":"iyi"},
#    {"name": "Samsung S7", "price": 4000,"catagories":['telefon','elektronik'},
#    {"name": "Samsung S8", "price": 5000,"description":"iyi"},
#    {"name": "Samsung S9", "price": 6000,"description":"iyi"},
#    {"name": "Samsung S10", "price": 7000,"description":"iyi"},
#    {"name": "Samsung S11", "price": 8000,"description":"iyi"}
# ]
# result=mycollection.insert_many(productList)
# print(result.inserted_ids)
