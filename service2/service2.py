from flask import Flask, jsonify
import requests

app = Flask(__name__)

service1_url = "http://service1:5001/api/service1"

@app.route('/api/service2', methods=['GET'])
def get_service2_data():
    response = requests.get(service1_url)
    data_from_service1 = response.json()
    return jsonify({'message': 'Data from Service 2', 'data_from_service1': data_from_service1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
