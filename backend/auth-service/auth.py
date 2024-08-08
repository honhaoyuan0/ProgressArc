from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
CORS(app)

# Setup connection to MongoDB
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    # To do
    return 'Login'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            
            # Check if email already exists
            existing_user = db.users.find_one({'email': email})
            if existing_user:
                return jsonify({'message': 'Email already exists', 'status': 'fail'}), 400
            
            # Insert new user
            db.users.insert_one({
                'email': email,
                'password': password
            })
            
            response_data = {
                'message': "Account registered successfully",
                'status': 'success',
            }
            return jsonify(response_data), 200
        else:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415
    else:
        return jsonify({'error': 'Method Not Allowed'}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)