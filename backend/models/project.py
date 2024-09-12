from db.db import db
from flask import jsonify, request
import uuid

class Project:

    def create_project(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415
        
        user = db.users.find_one({"_id": request.json.get('_id')})

        if not user:
            return jsonify({
            'error': 'User not found',
            'status': 'failed',
        }), 500

        for project in user.get('projects', []):
            if project.get('name') == request.json.get('name'):
                return jsonify({
                    'error': f"Project name '{request.json.get('name')}' already exists.",
                    'status': 'failed',
                }), 400
        
        project = {
            '_id': uuid.uuid4().hex,
            'name': request.json.get('name'),
            'components': request.json.get('components')
        }

        if db.users.update_one({'_id': request.json.get('_id')}, {'$push': {'projects': project }}):
            return jsonify({
                'message': "Project created successfully",
                'status': 'success',
            }), 200
        
        return jsonify({
            'error': 'Failed to create project',
            'status': 'failed',
        }), 500

    def get_projects(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415
        
        user = db.users.find_one({"_id": request.json.get('_id')})

        if not user:
            return jsonify({
                'error': 'User not found',
                'status': 'failed',
            }), 500

        return jsonify({
            'message': user.get('projects', []),
            'status': 'success',
        }), 200

    def update_project(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415

        if (db.users.update_one(
            {'_id': request.json.get('user_id'), 'projects._id': request.json.get('project_id')},
            {'$set': {'projects.$.name': request.json.get('name'), 'projects.$.components': request.json.get('components')}}
        )).matched_count == 1:
            return jsonify({
                'message': "Project updated successfully",
                'status': 'success',
            }), 200
        
        return jsonify({
            'error': 'Failed to update project',
            'status': 'failed',
        }), 500               

    def delete_project(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415
        
        user = db.users.find_one({"_id": request.json.get('_id')})

        if not user:
            return jsonify({
            'error': 'User not found',
            'status': 'failed',
        }), 500

        for project in user.get('projects', []):
            if project.get('name') == request.json.get('name'):
                db.users.update_one({'_id': request.json.get('_id')}, {'$pull': {'projects': {'name': request.json.get('name')}}})
                return jsonify({
                    'message': "Project deleted successfully",
                    'status': 'success',
                }), 200
        
        return jsonify({
            'error': 'Project not found',
            'status': 'failed',
        }), 400
