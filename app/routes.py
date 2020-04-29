import json
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
# create user
# log user in

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
            return "True"
    return "False" # return JWT

# @app.route('verify-jwt')
# def verify():

