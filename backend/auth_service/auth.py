from flask_cors import CORS
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
CORS(app)

from auth_service import routes

@app.route('/')
def index():
    return 'Index Page'
