import os

from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

# on heroku there is variable setted up with MONGO_URI key and db url as a value
client = MongoClient(os.getenv('MONGODB_URI'))
app = Flask(__name__)
CORS(app)
if not os.getenv('MONGODB_URI'):
  db = client.dev_database
else:
  db = client.get_default_database()
print(db)

from app import routes