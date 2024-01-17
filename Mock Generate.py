import pymongo
import datetime
import time

myclient = pymongo.MongoClient('mongodb+srv://nisamanee:passw0rd!@ct-pj-iot.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000')
mydb = myclient["Project"]
mycol = mydb["Light-status"]
 

for i in range(10):
    time_now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    # print(time_now)
    database_list = [
    {"Date_time": time_now,"Room": "Bedroom", "Device_id": "1","Status": "1"},
    {"Date_time": time_now,"Room": "Bathroom", "Device_id": "1","Status": "1"},
    {"Date_time": time_now,"Room": "Livingroom", "Device_id": "2","Status": "1"},
    ]
    x = mycol.insert_many(database_list)
    time.sleep(60)

    if i == 10:
        break







# for i in range(10):   
#      data_entry = {
#           'Device_id' : i+1,
#           'Room' : f'Bedroom-{i+1}',
#           'Status' :1+i,
    
#      }

# for entry in database_list:
#      print(entry)


