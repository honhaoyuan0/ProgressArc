from flask_cors import CORS
from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Setup connection to MongoDB
mongodb_client = PyMongo(app)
db = mongodb_client.db
