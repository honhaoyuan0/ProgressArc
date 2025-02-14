from models.project import Project
from project_service.project import app

@app.route('/create_project', methods=['POST'])
def create_project():
    return Project().create_project()

@app.route('/get_projects')
def get_projects():
    return Project().get_projects()

@app.route('/get_project_by_id', methods=['GET'])
def get_project_by_id():
    return Project().get_project_by_id()

@app.route('/update_project', methods=['PATCH'])
def update_project():
    return Project().update_project()

@app.route('/update_project_name', methods=['PATCH'])
def update_project_name():
    return Project().update_project_name()

@app.route('/delete_component', methods=['DELETE'])
def delete_component():
    return Project().delete_component()

@app.route('/add_component', methods=['POST'])
def add_component():
    return Project().add_component()

@app.route('/update_component_name', methods=['PATCH'])
def update_component_name():
    return Project().update_component_name()

@app.route('/update_component_task', methods=['PATCH'])
def update_component_task():
    return Project().update_component_task()

@app.route('/update_component_completion_status', methods=['PATCH'])
def update_component_completion_status():
    return Project().update_component_completion_status()

@app.route('/delete_project', methods=['DELETE'])
def delete_project():
    return Project().delete_project()
