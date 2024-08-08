from flask_cors import CORS
from flask import Flask, jsonify, redirect, request, session
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
from passlib.hash import pbkdf2_sha256
import uuid

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.secret_key = os.getenv('FLASK_SECRET_KEY')
CORS(app)

# Setup connection to MongoDB
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/')
def index():
    return 'Index Page'

def start_session(user):
    session['logged_in'] = True
    session['user'] = user

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    user = db.users.find_one({'email': email})

    if user and pbkdf2_sha256.verify(password, user['password']):
        start_session(user)
        return jsonify({
            'message': "Logged in successfully",
            'status': 'success',
        }), 200

    return jsonify({
        'error': 'Invalid login credentials',
        'status': 'failed',
    }), 401

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415
    
    data = request.get_json()

    _id = uuid.uuid4().hex
    email = data.get('email')
    password = pbkdf2_sha256.encrypt(data.get('password'))
    
    # Check if email already exists
    existing_user = db.users.find_one({'email': email})
    if existing_user:
        return jsonify({
            'error': 'Email already exists',
            'status': 'failed',
        }), 400
    
    # Insert new user
    user = {
        '_id': _id,
        'email': email,
        'password': password
    }
    if db.users.insert_one(user):
        start_session(user)
        return jsonify({
            'message': "Account registered successfully",
            'status': 'success',
        }), 200
    
    return jsonify({
        'error': 'Register failed',
        'status': 'failed',
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)