from db.db import db
from flask import jsonify, make_response, redirect, request, session
from passlib.hash import pbkdf2_sha256
import uuid

class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
    
    def register(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415

        user = {
            '_id': uuid.uuid4().hex,
            'email': request.json.get('email'),
            'password': request.json.get('password')
        }

        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        if db.users.find_one({'email': user['email']}):
            return jsonify({
                'error': 'Email already exists',
                'status': 'failed',
            }), 400
        
        if db.users.insert_one(user):
            self.start_session(user)
            return jsonify({
                'message': "Account registered successfully",
                'status': 'success',
            }), 200
        
        return jsonify({
            'error': 'Register failed',
            'status': 'failed',
        }), 500
    
    def login(self):
        user = db.users.find_one({'email': request.json.get('email')})

        if user and pbkdf2_sha256.verify(request.json.get('password'), user['password']):
            self.start_session(user)
            return jsonify({
                'message': "Logged in successfully",
                'user': session['user'],
                'status': 'success',
            }), 200
        
        return jsonify({
            'message': 'Invalid login credentials',
            'status': 'failed',
        }), 401

    def logout(self):
        session.clear()
        return redirect('/')

    def get_current_user(self):
        if 'logged_in' in session:
            response = make_response(jsonify({
                'user': session['user'],
                'status': 'success'
            }), 200)
        else:
            response = make_response(jsonify({
                'message': None,
                'status': 'failed'
            }), 401)
        
        response.headers['Content-Type'] = 'application/json'
        return response
