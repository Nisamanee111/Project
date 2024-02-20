import requests
from pymongo import MongoClient

def send_line_notify(message):
    token = 'tWL6dYjuQRCk3S88MdjAeLAQI3yRH6Nkj8QwMtJrddC'
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': message}
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

def check_and_alert():
    client = MongoClient('mongodb+srv://nisamanee:passw0rd!@ct-pj-iot.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000')
    db = client['Project']
    collection = db['Humidity']
    cursor = collection.find().sort("_id", -1).limit(1)
    last_document = next(cursor, None)
    Humidity = last_document.get("Status")
    print(Humidity)

    if Humidity >= 25:
        message = "status", " Humidity over 60"
        send_line_notify(message)
    #     send_line_notify("27: {}".format(document))
    # else:
    #     print("ไม่ต้องแจ้งเตือน: {}".format(document))


if __name__ == "__main__":
    # ใส่ Token ที่ได้จาก Line Notify ที่นี่
    
    # message = 'Hi pam!'
    check_and_alert()

    # send_line_notify(message, line_notify_token)

