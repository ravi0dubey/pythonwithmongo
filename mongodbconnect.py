#install pymongo and pymongo[srv]
# pip install pymongo
# $ python -m pip install 'pymongo[srv]'

import pymongo

# client = pymongo.MongoClient("mongodb+srv://ravi0dubey:Logi1234#@cluster0.9hjidow.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d1 = {
    "fname":"Ravi Dubey",
    "lname":"Dubey",
    "email": "r@gmail.com",

}
db1 = client['mongotest1']
coll= db1['test']
coll.insert_one(d1)


d2 = {
    "fname":"Ravi Dubey",
    "lname":"Dubey",
    "email": "r@gmail.com",

}
db2 = client['mongotest1']
coll= db2['test']
coll.insert_one(d2)
