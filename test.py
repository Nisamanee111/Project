from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# เชื่อมต่อ MongoDB
client = MongoClient('mongodb+srv://nisamanee:passw0rd!@ct-pj-iot.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000')
db = client['Project']  
collection = db['Light Status']  

# สร้าง API endpoint สำหรับดึงข้อมูลบางส่วน
@app.route('/api/data', methods=['GET'])
def get_partial_data():
    data = list(collection.find())
    for item in data:
        item['_id'] = str(item['_id'])
    return jsonify(data), 200

@app.route('/health', methods=['GET'])
def health_check():
    # ทำการตรวจสอบสถานะของระบบ หรือใส่ตรวจสอบอื่น ๆ ตามต้องการ
    status = 'ok'  # สถานะที่กำหนดเอง (สามารถใช้ 'ok', 'error', 'warning', หรืออื่น ๆ)

    response = {
        'status': status,
        'message': 'Health check passed successfully'
    }

    if status != 'ok':
        response['message'] = 'Health check failed'

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
