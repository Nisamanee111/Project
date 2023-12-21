from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# เชื่อมต่อ MongoDB
client = MongoClient('mongodb+srv://nisamanee:passw0rd!@ct-pj-iot.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000')
db = client['Project']  
collection = db['Door']  

# สร้าง API endpoint สำหรับดึงข้อมูลบางส่วน
@app.route('/api/data', methods=['GET'])
def get_partial_data():
    data = list(collection.find())
    for item in data:
        item['_id'] = str(item['_id'])
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
