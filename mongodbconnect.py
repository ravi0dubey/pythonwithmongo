#install pymongo and pymongo[srv]
# pip install pymongo
# $ python -m pip install 'pymongo[srv]'

import pymongo

# client = pymongo.MongoClient("mongodb+srv://ravi0dubey:Logi1234@cluster0.9hjidow.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# # print(db)

client = pymongo.MongoClient("mongodb+srv://ravi0dubey:Logiw@cluster0.0zxmnkl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# print(db)




#document1 is called document which is placed inside collections
document1 = {
    "fname":"Ravi Dubey",
    "lname":"Dubey",
    "email": "r@gmail.com",
}

database1 = client['raviinfo1'] #equivalent of database in SQL
collection1 = database1['comments'] #equivalent of tables in SQL is called collection
collection1.insert_one(document1) #insert document document1 in collection comments inside database



document2 = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}]

#insert document document2 in collection comments inside database
collection1.insert_many(document2)



#creating new collection collection3
collection3 = database1['datapacket']
document3 =[
 {"packetType":"D","data":{"checkEngineLightFlag":"F","batteryVoltageStableTime":0,"batteryVoltageStable":"0","batteryVoltageOff":"12.42","batteryCrankParamTN":"-0.08","batteryCrankParamVN":"0.00","batteryCrankParamTP":"-0.08","batteryCrankParamVP":"0.00","batteryCrankParamTT":"-0.00008","batteryCrankParamV0":"0.00","batteryVoltageMaxOn":"13.05","batteryVoltageMinOn":"12.97","batteryVoltageMaxOff":"12.46","batteryVoltageMinOff":"12.36","batteryVoltageOnAverage":"13.02","engineLoadMax":"84","engineLoadAverage":"39.98","rpmMax":"3487","rpmAverage":"1431.29","gpsSpeedAverage":"21.99","vssMax":"53.44","vssAverage":"23.06","tcuTemperatureMin":"82.40","tcuTemperatureMax":"109.40","tcuTemperatureAverage":"104.87","coolantMin":"158.00","coolantMax":"188.60","coolantAverage":"180.20","packetStartLocal":1508143346000,"tripStartLocal":1508143346000,"milIndicator":"F","monitorsNotReady":0,"imei":"60DF5417","gatewayTs":1515613306592,"diagnosticTroubleCodeData":[],"diagnosticPidData":[[64768,47,100],[64768,1,517376],[64800,1,262144],[64768,5,125]]},"header":{"iwrapVer":"1.9.20","sourceSystem":"CDP","configVer":"1.1","oemName":"HUM","unitType":0,"cpVer":"7.50.1.9","igpsVer":"1.3.7","messageType":"Notification","pomVer":"1.0","headerVer":"V6","timestamp":0,"deviceType":"InDrive","visorVer":"1.4.35","transactionId":"53098471-7787-4160-94b3-cd69dcc70416","deviceSerialNo":"60DF5417","subOrganization":"HUM","organization":"HUM","imei":"60DF5417","operation":"Notification"}}]
#insert document document3 in collection datapacket inside database datbase1
collection3.insert_many(document3)


# Select query equivalent of SQL is find. It will store all values fetched
record = collection1.find()
for i in record:
    print(i)


#
#to fetch a particular value CompanyName = ineuron
data = collection1.find({"'companyName": "ineuron"})
for i in record:
    print(i)


#to fetch a particular value courseOffered is greater than E
data = collection1.find({"'courseOffered": {"$gt": "E"}})
for i in record:
    print(i)


#fetching values form sample
database4= client['sample_training']
collection4= database4['companies']
# Select query equivalent of SQL is find. It will store all values fetched
record = collection1.find()
for i in record:
    print(i)



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


client = pymongo.MongoClient("mongodb+srv://ravi0dubey:Logiw@cluster0.0zxmnkl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database5 = client['inventory1']
collection5 = database5["table"]
collection5.insert_many(data)

d = collection5.find({'status':'A'})
for i in d:
    print(i)

#To find specific values with status equal to A or P
d = collection5.find({'status':{'$in': ['A','P']}})
for i in d:
    print(i)


#To find status greater than D
d = collection5.find({'status':{'$gt': 'D'}})
for i in d:
    print(i)


#To find where quantity is  100
d = collection5.find({'qty': 100})
for i in d:
    print(i)

#To find where quantity is greater than eual to 75
d = collection5.find({'qty':{'$gte': 75}})
for i in d:
    print(i)


#To find where item is sketch pad and quantity is 95
d = collection5.find({'item':'sketch pad','qty': 95})
for i in d:
    print(i)


#To find where item is sketch pad and quantity is greater than equal to 75
d = collection5.find({'item':'sketch pad','qty': {'$gte': 75}})
for i in d:
    print(i)

#To find where item is sketch pad OR quantity is greater than equal to 100
d = collection5.find({'$or' : [{'item':'sketch pad'},{'qty': {'$gte': 100}}]})
for i in d:
    print(i)
