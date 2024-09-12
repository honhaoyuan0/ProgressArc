from models.user import User
from auth_service.auth import app

@app.route('/register', methods=['POST'])
def register():
    return User().register()

@app.route('/login', methods=['POST'])
def login():
    return User().login()

@app.route('/logout')
def logout():
    return User().logout()

@app.route('/get_current_user', methods=['GET'])
def get_current_user():
    return User().get_current_user()
