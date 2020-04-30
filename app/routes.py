import json
import jwt
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
# create user
# log user in

jwt_secret="top secret secret"
users = [
    {
        'name': 'John',
        'email': 'John@John.com',
        'password': 'password' 
    },
        {
        'name': 'Ako',
        'email': 'Ako@Ako.com',
        'password': 'password'
    },
        {
        'name': 'Ivo',
        'email': 'Ivo@Ivo.com',
        'password': 'password' 
    }
]

@app.route('/get-users')
def get_users():
    return json.dumps(users)


@app.route('/add-user', methods=["POST"])
def add_user():
    user_dictionary = request.get_json()
    user_dictionary['password'] = generate_password_hash(user_dictionary['password'])
    users.append(request.get_json())
    return json.dumps(users) # return JWT

@app.route('/login', methods=["PUT"])
def login():
    body = request.get_json()
    username = body["name"]
    password = body["password"]
    for u in users:
        if u['name'] == username and check_password_hash(u['password'], password):
            return jwt.encode({'username': username}, jwt_secret, algorithm="HS256")
    return "Your credentials have been rejected" # return JWT

@app.route('/make-change', methods=['POST'])
def do_something():
    body = request.get_data()
    credentials = jwt.decode(body, jwt_secret, algorithms=['HS256'])
    return credentials
# @app.route('verify-jwt')
# def verify():

