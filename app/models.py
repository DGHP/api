from app import db
import datetime


users = db.users
# users.drop()
collection = db.user_collection


def addUser(user):
    users.insert_one(user)

def getUser(username):
    return users.find_one({'name': username})

def getFromDatabase():
    print(db.list_collection_names())
    results = db.users.find()
    return_value = []
    for res in results:
        return_value.append(res)
    return return_value

