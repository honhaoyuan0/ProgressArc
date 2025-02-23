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

        # Allow duplicate project name for now as long as they have different IDs
        # for project in user.get('projects', []):
        #     if project.get('name') == request.json.get('name'):
        #         return jsonify({
        #             'error': f"Project name '{request.json.get('name')}' already exists.",
        #             'status': 'failed',
        #         }), 400
        
        project = {
            '_id': uuid.uuid4().hex,
            'name': request.json.get('name'),
            'components': request.json.get('components')
        }

        if db.users.update_one({'_id': request.json.get('_id')}, {'$push': {'projects': project }}):
            # Return the updated users object
            user = db.users.find_one({"_id": request.json.get('_id')})
            return jsonify({
                'message': "Project created successfully",
                'user': user,
                'project': project,
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

    def get_project_by_id(self):
        user_id = request.args.get('user_id')
        project_id = request.args.get('project_id')

        if not user_id or not project_id:
            return jsonify({'error': 'Missing user_id or project_id'}), 400

        user = db.users.find_one({"_id": user_id})

        if not user:
            return jsonify({
                'error': 'User not found',
                'status': 'failed',
            }), 500
        
        project = next((proj for proj in user.get('projects', []) if proj.get('_id') == project_id), None)

        if project:
            return jsonify(project['components']), 200
        
        else:
            return jsonify({
                'error': 'Project not found',
                'status': 'failed',
            }), 404

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

    def update_project_name(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415

        user_id = request.json.get('user_id')
        project_id = request.json.get('project_id')
        new_name = request.json.get('new_name')

        if db.users.update_one(
            {'_id': user_id, 'projects._id': project_id},
            {'$set': {'projects.$.name': new_name}}
        ).matched_count == 1:
            # Return the updated users object
            user = db.users.find_one({"_id": user_id})
            return jsonify({
                'message': "Project name updated successfully",
                'user': user,
                'status': 'success',
            }), 200
        
        return jsonify({
            'error': 'Failed to update project name',
            'status': 'failed',
        }), 500

    def add_component(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415
        
        user_id = request.json.get('user_id')
        project_id = request.json.get('project_id')
        parent_id = request.json.get('parent_id')

        user = db.users.find_one({"_id": user_id})

        if not user:
            return jsonify({
            'error': 'User not found',
            'status': 'failed',
            }), 500

        project = next((proj for proj in user.get('projects', []) if proj.get('_id') == project_id), None)

        if not project:
            return jsonify({
            'error': 'Project not found',
            'status': 'failed',
            }), 404

        new_component_info = {
            'id': uuid.uuid4().hex,
            'parentId': str(parent_id),
            'size': '',
            'name': 'New Task',
            'tasks': 'Type in your task description here',
            'is_completed': 'false'
        }
        if db.users.update_one(
            {'_id': user_id, 'projects._id': project_id},
            {'$push': {'projects.$.components': new_component_info}}
        ).matched_count == 1:
            return jsonify({
                'message': "Component added successfully",
                'status': 'success',
                'component': new_component_info
            }), 200

        return jsonify({
            'error': 'Failed to add component',
            'status': 'failed',
        }), 500

    def _find_component(self, user_id, project_id, component_id):
        user = db.users.find_one({"_id": user_id})

        if not user:
            return None, jsonify({
                'error': 'User not found',
                'status': 'failed',
            }), 500
        
        project = next((proj for proj in user.get('projects', []) if proj.get('_id') == project_id), None)

        if not project:
            return None, jsonify({
                'error': 'Project not found',
                'status': 'failed',
            }), 404
        
        component = next((comp for comp in project.get('components', []) if comp.get('id') == component_id), None)
        
        if not component:
            return None, jsonify({
                'error': 'Component not found',
                'status': 'failed',
            }), 404

        return component, None, None

    def _update_component_field(self, user_id, project_id, component_id, field, new_value):
        if db.users.update_one({'_id': user_id, 'projects._id': project_id, 'projects.components.id': component_id},
                               {'$set': {f'projects.$.components.$[comp].{field}': new_value}},
                               array_filters=[{'comp.id': component_id}]).matched_count == 1:
            return jsonify({
                'message': f"Component's field '{field}' updated successfully",
                'status': 'success',
            }), 200
        
        return jsonify({
            'error': 'Failed to update component',
            'status': 'failed',
        }), 500

    def delete_component(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415
        
        user_id = request.json.get('user_id')
        project_id = request.json.get('project_id')
        component_id = request.json.get('component_id')

        component, error_response, status_code = self._find_component(user_id, project_id, component_id)

        if error_response:
            return error_response, status_code

        if component and db.users.update_one({'_id': user_id, 'projects._id': project_id},
                               {'$pull': {'projects.$.components': {'id': component_id}}}).matched_count == 1:
            return jsonify({
                'message': "Component deleted successfully",
                'status': 'success',
            }), 200
        
        return jsonify({
            'error': 'Failed to delete component',
            'status': 'failed',
        }), 500

    def update_component_name(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415
        
        user_id = request.json.get('user_id')
        project_id = request.json.get('project_id')
        component_id = request.json.get('component_id')
        new_name = request.json.get('new_name')

        component, error_response, status_code = self._find_component(user_id, project_id, component_id)

        if error_response:
            return error_response, status_code
        
        return self._update_component_field(user_id, project_id, component_id, 'name', new_name)

    def update_component_task(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415

        user_id = request.json.get('user_id')
        project_id = request.json.get('project_id')
        component_id = request.json.get('component_id')
        new_tasks = request.json.get('new_tasks')

        component, error_response, status_code = self._find_component(user_id, project_id, component_id)

        if error_response:
            return error_response, status_code

        return self._update_component_field(user_id, project_id, component_id, 'tasks', new_tasks)            

    def update_component_completion_status(self):
        if not request.is_json:
            return jsonify({'error': 'Unsupported Media Type, content type must be application/json'}), 415

        user_id = request.json.get('user_id')
        project_id = request.json.get('project_id')
        component_id = request.json.get('component_id')
        new_completion_status = request.json.get('new_completion_status')

        component, error_response, status_code = self._find_component(user_id, project_id, component_id)

        if error_response:
            return error_response, status_code

        return self._update_component_field(user_id, project_id, component_id, 'is_completed', new_completion_status)

    def delete_project(self):
        
        
        user = db.users.find_one({"_id": request.args.get('user_id')})

        if not user:
            return jsonify({
            'error': 'User not found',
            'status': 'failed',
        }), 500

        for project in user.get('projects', []):
            if project.get('_id') == request.args.get('project_id'):
                db.users.update_one({'_id': request.args.get('user_id')}, {'$pull': {'projects': {'_id': request.args.get('project_id')}}})
                user = db.users.find_one({"_id": request.args.get('user_id')})
                return jsonify({
                    'message': "Project deleted successfully",
                    'user': user,
                    'status': 'success',
                }), 200
        
        return jsonify({
            'error': 'Project not found',
            'status': 'failed',
        }), 400
