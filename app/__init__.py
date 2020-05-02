import os

from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

# on heroku there is variable setted up with MONGO_URI key and db url as a value
client = MongoClient(os.getenv('MONGODB_URI', default='mongodb://localhost:27017/'))
app = Flask(__name__)
CORS(app)
db = client.dev_database

from app import routes