from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash

from flask import request, make_response

from app import app, models
from app.helpers import token_required, make_jwt
from app.factories.newgame import new_game_factory
from app.factories.player import player_factory


@app.route('/users', methods=["GET"])
def get_users():
    data = dumps(models.get_from_database(collection="users"))
    res = make_response(data, 200, {'content-type': 'application/json'})
    return res


@app.route('/users', methods=["POST"])
def add_user():
    user = request.get_json()
    user['password'] = generate_password_hash(
        user['password'])
    models.add_user(user)
    username = user['username']
    token = {"token": make_jwt(username)}
    res = make_response(token, 200, {'content-type': 'application/json'})
    return res


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
    game = new_game_factory(game_name=body['gameName'], player_count=body['playerCount'],
                            mode=body['mode'], first_player=body['playerUsernames'][0])
    models.create_game(game)
    return "new game created"


@app.route('/games', methods=['GET'])
def get_games():
    return dumps(models.get_from_database(collection="games"))


@app.route('/games', methods=['PUT'])
@token_required
# example of a good request: http://127.0.0.1:5000/games?name=fac19&username=ivo
def route_games_put(current_user):
    game_name = request.args.get('gamename')
    if game_name:
        user = request.args.get('username')
        if user:
            player_dict = player_factory(user)
            models.add_user_to_game(game_name=game_name, user=player_dict)
            return "User added"
        return "Could not find username field"
    return "could not find game name field"

# this function is currently for adding a user to a game, but it could turn into a router for different kinds of put requests.

