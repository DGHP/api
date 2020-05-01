
from bson.json_util import dumps
import jwt
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from time import time

from app import models # camelcase bad
from app.factories.newgame import new_game
from app import app
# create user
# log user in

jwt_secret = "top secret secret"

@app.route('/get-users')
def get_users():
    return dumps(models.getFromDatabase(collection="users"))


@app.route('/add-user', methods=["POST"])
def add_user():
    user_dictionary = request.get_json()
    user_dictionary['password'] = generate_password_hash(
        user_dictionary['password'])
    # users.append(request.get_json())
    models.addUser(user_dictionary)
    username = user_dictionary['name']
    return make_jwt(username)


@app.route('/login', methods=["POST"])
def login():
    body = request.get_json()
    username = body["name"]
    password = body["password"]
    db_user = models.getUser(username)
    if db_user == None or not check_password_hash(db_user['password'], password):
        return "Your credentials have been rejected"
    return make_jwt(username)


@app.route('/make-change', methods=['POST'])
def do_something():
    body = request.get_data()
    credentials =  check_jwt(body)
    return credentials


def make_jwt(username):
    now = int(time())
    week_later = now + 604800
    return jwt.encode({'username': username, 'iat': now, 'exp': week_later}, jwt_secret, algorithm="HS256")

def check_jwt(payload):
    try: 
        return jwt.decode(payload, jwt_secret, algorithms=['HS256'])
    except jwt.exceptions.InvalidSignatureError:
        return "token is invalid"


@app.route('/games', methods=["POST"])
def create_game():
    body = request.get_json()
    game = new_game(name=body['name'], players=body['playerCount'], mode=body['mode'], first_player=body['playerUsernames'][0])
    models.createGame(game)
    return "new game created"

@app.route('/games', methods=['GET'])
def get_games():
    return dumps(models.getFromDatabase(collection="games"))



# @app.route('/games')
# def get_all_games():
