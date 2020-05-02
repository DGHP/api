from bson.json_util import dumps
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

from app.helpers import token_required, make_jwt
from app import models
from app.factories.newgame import new_game_factory
from app.factories.player import player_factory
from app import app

@app.route('/users', methods=["GET"])
def get_users():
    return dumps(models.get_from_database(collection="users"))


@app.route('/users', methods=["POST"])
def add_user():
    user_dictionary = request.get_json()
    user_dictionary['password'] = generate_password_hash(
        user_dictionary['password'])
    models.add_user(user_dictionary)
    username = user_dictionary['name']
    return make_jwt(username)


@app.route('/login', methods=["POST"])
def login():
    body = request.get_json()
    username = body["username"]
    password = body["password"]
    db_user = models.get_user(username)
    if db_user == None or not check_password_hash(db_user['password'], password):
        return "Your credentials have been rejected"
    return make_jwt(username)


@app.route('/games', methods=["POST"])
@token_required
def create_game(current_user):
    print(current_user)
    body = request.get_json()
    game = new_game_factory(name=body['name'], players=body['playerCount'], mode=body['mode'], first_player=body['playerUsernames'][0])
    models.create_game(game)
    return "new game created"

@app.route('/games', methods=['GET'])
def get_games():
    return dumps(models.get_from_database(collection="games"))

@app.route('/games', methods=['PUT'])
@token_required
def route_games_put(current_user): # example of a good request: http://127.0.0.1:5000/games?name=fac19&username=ivo
    game = request.args.get('name')
    if game:
        user = request.args.get('username')
        if user:
            player_dict = player_factory(user)
            models.add_user_to_game(game=game, user=player_dict)
            return "User added"
        return "Could not find username field"
    return "could not find game name field"

# this function is currently for adding a user to a game, but it could turn into a router for different kinds of put requests.



