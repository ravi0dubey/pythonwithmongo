#install pymongo and pymongo[srv]
# pip install pymongo
# $ python -m pip install 'pymongo[srv]'

import pymongo

#ravi04
# client_connect = pymongo.MongoClient("mongodb+srv://ravi0dubey:Logiw>@cluster0.0zxmnkl.mongodb.net/?retryWrites=true&w=majority")
# db_connect = client_connect.test

#ravi0d
client_connect = pymongo.MongoClient("mongodb+srv://ravi0dubey:Logiw@cluster0.9hjidow.mongodb.net/?retryWrites=true&w=majority")
db = client_connect.test


data1=[
    {
        "Schoolid": 10001,
        "SchoolName": "St Michael",
        "Location": "Toronto",
        "No_of_Students": 500
    },
]
database2= client_connect["schooldb"]
collection = database2["school_inventory"]
collection.insert_many(data1)



d = collection.find({'Schoolid':1001})
for i in d:
    print(i)
