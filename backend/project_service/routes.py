from models.project import Project
from project_service.project import app

@app.route('/create_project', methods=['POST'])
def create_project():
    return Project().create_project()

@app.route('/get_projects')
def get_projects():
    return Project().get_projects()

@app.route('/update_project', methods=['PATCH'])
def update_project():
    return Project().update_project()

@app.route('/delete_project', methods=['DELETE'])
def delete_project():
    return Project().delete_project()
