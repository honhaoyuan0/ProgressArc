from flask import Flask
from blueprints.auth_service.auth_service import auth_bp
from blueprints.frontend.frontend import frontend_bp
from blueprints.content_service.content_service import content_bp
from blueprints.user_service.user_service import user_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth_service")
app.register_blueprint(frontend_bp, url_prefix="/frontend")
app.register_blueprint(content_bp, url_prefix="/content_service")
app.register_blueprint(user_bp, url_prefix="/user_service")

@app.route("/")
def homepage():
    return "Inside of Homepage !"

if __name__ == '__main__':
    app.run(debug=True)