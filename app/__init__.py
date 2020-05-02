from flask import Flask
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

client = MongoClient()

app = Flask(__name__)
CORS(app)
db = client.dev_database

# db = SQLAlchemy(app)

from app import routes