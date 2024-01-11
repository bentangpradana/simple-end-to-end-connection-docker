from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/service1', methods=['GET'])
def get_service1_data():
    return jsonify({'message': 'Data from Service 1'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
