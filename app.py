from flask import Flask, request, jsonify, send_file
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

# Initialize the data file if it doesn't exist yet
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump({"tasks": [], "notes": ""}, f)

@app.route('/')
def index():
    # Serves your HTML file when you visit the Pi's IP address
    return send_file('study_planner.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    # Sends the saved data to the browser
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return jsonify(json.load(f))

@app.route('/api/data', methods=['POST'])
def save_data():
    # Receives updated data from the browser and overwrites the file
    data = request.json
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    # host='0.0.0.0' makes the server accessible to other devices on your network
    app.run(host='0.0.0.0', port=5000)
