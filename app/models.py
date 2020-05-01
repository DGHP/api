from app import db

users = db.users
# users.drop()
games = db.games


def getFromDatabase():
    print(db.list_collection_names())
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
    print(games.find_one())
