from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

client = MongoClient()
app = Flask(__name__)
CORS(app)
db = client.dev_database

# from app import routes