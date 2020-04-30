from app import db
import datetime


posts = db.posts
# posts.drop()
collection = db.user_collection

def addToDatabase(dictionary):
    posts.insert_many(dictionary)


def addUser(user):
    posts.insert_one(user)

def getUser(username):
    return posts.find_one({'name': username})

def getFromDatabase():
    results = db.posts.find()
    return_value = []
    for res in results:
        return_value.append(res)
    return return_value

