import pymongo
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

client = pymongo.MongoClient("mongodb+srv://ravi0dubey:logiw@cluster0.0zxmnkl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['inventory']
collection = database["table"]
collection.insert_many(data)

d = collection.find({'status':'A'})
for i in d:
    print(i)

#To find specific values with status equal to A or P
d = collection.find({'status':{'$in': ['A','P']}})
for i in d:
    print(i)


#To find status greater than D
d = collection.find({'status':{'$gt': 'D'}})
for i in d:
    print(i)


#To find where quantity is  100
d = collection.find({'qty': 100})
for i in d:
    print(i)

#To find where quantity is greater than eual to 75
d = collection.find({'qty':{'$gte': 75}})
for i in d:
    print(i)


#To find where item is sketch pad and quantity is 95
d = collection.find({'item':'sketch pad','qty': 95})
for i in d:
    print(i)


#To find where item is sketch pad and quantity is greater than equal to 75
d = collection.find({'item':'sketch pad','qty': {'$gte': 75}})
for i in d:
    print(i)

#To find where item is sketch pad OR quantity is greater than equal to 100
d = collection.find({'$or' : [{'item':'sketch pad'},{'qty': {'$gte': 100}}]})
for i in d:
    print(i)


#updating record rename item name from canvas to raviitem
collection.update_one({'item':'canvas'},{'$set': {'item':"raviitem"}})


#delete
collection.delete_one({'item':'raviitem'})