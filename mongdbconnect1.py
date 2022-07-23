#install pymongo and pymongo[srv]
# pip install pymongo
# $ python -m pip install 'pymongo[srv]'

import pymongo

#ravi04
# client_connect = pymongo.MongoClient("mongodb+srv://ravi0dubey:Logiw>@cluster0.0zxmnkl.mongodb.net/?retryWrites=true&w=majority")
# db_connect = client_connect.test

#ravi0d
client_connect = pymongo.MongoClient("mongodb+srv://ravi0dubey:Logiw@cluster0.9hjidow.mongodb.net/?retryWrites=true&w=majority")
# db = client_connect.test

#Hierarchy of MONGODB
# 1. Database at top level
# 2. Collections
# 2. Data

#data1 is called document which is placed inside collections
data1=[
    {
        "Schoolid": 10001,
        "SchoolName": "St Michael",
        "Location": "Toronto",
        "No_of_Students": 500
    },
    {
        "Schoolid": 10002,
        "SchoolName": "St Paul's",
        "Location": "Mississauga",
        "No_of_Students": 342
    },
    {
        "Schoolid": 10003,
        "SchoolName": "St Thomas",
        "Location": "Mississauga",
        "No_of_Students": 578
    },
    {
        "Schoolid": 10004,
        "SchoolName": "Notre Dam Academy",
        "Location": "Brampton",
        "No_of_Students": 207
    },
    {
        "Schoolid": 10005,
        "SchoolName": "Bishop Cotton",
        "Location": "Toronto",
        "No_of_Students": 198
    },
    {
        "Schoolid": 10007,
        "SchoolName": "Alexander HighSchool",
        "Location": "Toronto",
        "No_of_Students": 698
    },
]

# Database name is schooldb
# Collection/table name is school_inventory

database2= client_connect["schooldb"]
collection = database2["school_inventory"]

# Inserting Data1 into collection
collection.insert_many(data1)

#Search Query

# Finding school id with specific values of Schoolid
print("Finding records with school id 10002")
find1 = collection.find({'Schoolid':10002})
for i in find1:
    print(i)

# Finding records for multiple values of schoolid
print("Finding records with school id 10001,10004,10005")
d = collection.find({'Schoolid':{'$in': [10001,10004,10005]}})
for i in d:
    print(i)

#Finding school with no of students greater than 550
print("Finding records with no of students greater than 550")
d = collection.find({'No_of_Students':{'$gte': 550}})
for i in d:
    print(i)


#Finding school which is either in Mississauga and Brampton and number of students in more than 300
print("#Finding school which is either in Mississauga and Brampton and number of students in more than 300")
d = collection.find({"Location":{'$in' : ['Mississauga','Brampton']}, 'No_of_Students':{'$gte': 300}})

for i in d:
    print(i)

#Finding school which is either in Mississauga and Brampton or number of students in more than 300.
print("Finding school which is either in Mississauga and Brampton or number of students in more than 300")

d = collection.find({'$or' : [{"Location":{'$in': ['Mississauga','Brampton']}},{'No_of_Students':{'$gte': 300}}]})
for i in d:
    print(i)


#update query

#updating No of Students in Brampton to 320
collection.find_one_and_update({'Location':'Brampton'},{'$set': {'No_of_Students': 320}})

#Finding school which is either in Mississauga and Brampton and number of students in more than 300
print("#Finding school which is either in Mississauga and Brampton and number of students in more than 300")
d = collection.find({"Location":{'$in' : ['Mississauga','Brampton']}, 'No_of_Students':{'$gte': 300}})

for i in d:
    print(f"Details : {i['SchoolName'], i['Location'],i['No_of_Students']}")


#delete query

collection.delete_many({'SchoolName': 'St Michael'})

#Printing details after deleting records with SchoolName St. Michael
print("#Printing details after deleting records with SchoolName St. Michael")
d = collection.find()

for i in d:
    print(f"Details : {i['SchoolName'], i['Location'],i['No_of_Students']}")