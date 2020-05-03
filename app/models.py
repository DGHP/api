from app import db

users = db.users
# users.drop()

games = db.games
# games.drop()

# right now returns password - good for debugging but not for production. TBH this whole route is probably like that
def get_from_database(collection):
    results = db[collection].find()
    return_value = []
    for res in results:
        return_value.append(res)
    return return_value


def add_user(user):
    users.insert_one(user)


def get_user(username):
    return users.find_one({'username': username})

def get_game(game_name):
    return games.find_one({'gameName': game_name})

def create_game(game):
    games.insert_one(game)


def add_user_to_game(game_name, user):
    games.update_one({'gameName': game_name}, {'$push': {'players': user}})
    print(db.games.find_one({'gameName': game_name}))
