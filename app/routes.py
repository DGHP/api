from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash

from flask import request, make_response

from app import app, models
from app.helpers import token_required, make_jwt, validate_message
from app.factories.newgame import new_game_factory
from app.factories.player import player_factory


@app.route('/users', methods=["GET"])
def get_users():
    data = dumps(models.get_from_database(collection="users"))
    res = make_response(data, 200, {'content-type': 'application/json'})
    return res


@app.route('/users', methods=["POST"])
def add_user():
    user = validate_message(request.get_json(), 'username', 'password')
    if not user:
        return make_response("Your request body must contain username and password fields", 400)
    if models.get_user(user['username']):
        return make_response("Username is already in database", 401)
    user['password'] = generate_password_hash(
        user['password'])
    models.add_user(user)
    username = user['username']
    # decode converts bites into string # but why?
    token = {"token": make_jwt(username).decode()}
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
    # decode converts bites into string
    token = {"token": make_jwt(username).decode()}
    res = make_response(token, 200, {'content-type': 'application/json'})
    return res


@app.route('/games', methods=["POST"])
@token_required
def create_game(current_user):
    game = validate_message(request.get_json(), 'gameName',
                            'playerCount', 'mode', 'playerUsernames')
    if not game:
        return make_response("Your request body must contain gameName, playerCount, mode and playerUsernames fields", 400)
    body = request.get_json()
    game = new_game_factory(game_name=body['gameName'], player_count=body['playerCount'],
                            mode=body['mode'], first_player=current_user['username'])
    models.create_game(game)
    return {"message": "new game created"}


@app.route('/games', methods=['GET'])
def get_games():
    data = dumps(models.get_from_database(collection="games"))
    res = make_response(data, 200, {"content-type": "application/json"})
    return res


@app.route('/games', methods=['PUT'])
@token_required
# example of a good request: http://127.0.0.1:5000/games?gamename=fac19
def route_games_put(current_user):
    game_name = request.args.get('gamename')
    if game_name:
        user = current_user["username"]
        if user:
            player_dict = player_factory(user)
            models.add_user_to_game(game_name=game_name, user=player_dict)
            return make_response("User added", 200)
        return make_response("Could not find username", 400)
    return make_response("could not find game name field", 400)
