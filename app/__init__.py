from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

client = MongoClient()

app = Flask(__name__)
db = client.dev_database

# db = SQLAlchemy(app)

from app import routes