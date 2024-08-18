from flask_cors import CORS
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.secret_key = os.getenv('FLASK_SECRET_KEY')
CORS(app)

# Setup connection to MongoDB
mongodb_client = PyMongo(app)
db = mongodb_client.db

from auth_service import routes

@app.route('/')
def index():
    return 'Index Page'
