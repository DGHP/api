from app import db

users = db.users
# users.drop()
games = db.games
games.drop()


def getFromDatabase(collection): # right now returns password - good for debugging but not for production. TBH this whole route is probably like that
    # print(db.list_collection_names())
    if collection == "games":
        results = db.games.find()
    else:
        results = db.users.find()
    return_value = []
    for res in results:
        return_value.append(res)
    return return_value

def addUser(user):
    users.insert_one(user)

def getUser(username):
    return users.find_one({'name': username})

def createGame(game):
    games.insert_one(game)

def addUser(game, user):
    games.update({'name': game}, {'$push': {'players': user}})
    # print(db.games.find_one({'name': game}))
