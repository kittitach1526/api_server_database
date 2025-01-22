from flask import Flask, jsonify, request,render_template
from connect_database import Database
import json

app = Flask(__name__)
database = Database() 

@app.route('/') # Home page
def home():
    return render_template('index.html')

#------------------------------------GET------------------------------------#

@app.route('/api/railway/all', methods=['GET'])
def get_railway():
    # สร้างออบเจกต์ฐานข้อมูล
    try:
        # ดึงข้อมูลทั้งหมดจาก tb_railway_type
        result = database.fetch_all_railway_types()  # `result` เป็น list ของ dictionary อยู่แล้ว
        # คืนค่า JSON response โดยตรง
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        # คืนค่า JSON response เมื่อเกิดข้อผิดพลาด
        return jsonify({"status": "error", "message": str(e)})


@app.route('/api/station/all', methods=['GET'])
def get_station():
    try:
        result = database.fetch_all_stations()
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/evaluation/all', methods=['GET'])
def get_evaluation():
    try:
        result = database.fetch_all_evaluations()
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/account/username', methods=['GET'])
def get_account():
    try:
        result = database.fetch_all_accounts()
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/test_model/all', methods=['GET'])
def get_model_testing():
    try:
        result = database.fetch_all_model_testings()
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    

#------------------------------------POST------------------------------------#

@app.route('/api/evaluation/add', methods=['POST'])
def add_evaluation():
    new_data = request.get_json()
    print(new_data)

    event = new_data['event']
    gyro_x = new_data['gyro_x']
    gyro_y = new_data['gyro_y']
    gyro_z = new_data['gyro_z']
    station_start = new_data['station_start']
    station_end = new_data['station_end']
    evaluation_date = new_data['evaluation_date']
    evaluation_score = new_data['evaluation_score']

    print(event, gyro_x, gyro_y, gyro_z, station_start, station_end, evaluation_date, evaluation_score)
    database.insert_evaluation(event, gyro_x, gyro_y, gyro_z, station_start, station_end, evaluation_date, evaluation_score)
    return jsonify(new_data), 201

@app.route('/api/test_model/add', methods=['POST'])
def add_model_testing():

    new_data = request.get_json()
    # print(new_data)
    gyro_x = new_data['gyro_x']
    gyro_y = new_data['gyro_y']
    gyro_z = new_data['gyro_z']
    test_result = new_data['test_result']
    is_correct =  new_data['is_correct']
    correct_result = new_data['correct_result']

    print(gyro_x, gyro_y, gyro_z, test_result, is_correct, correct_result)  
    database.insert_model_testing(gyro_x, gyro_y, gyro_z, test_result, is_correct, correct_result)

    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(debug=True)