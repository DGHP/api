from app import db

class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(64), unique=True)
    email = db.column(db.String(120), unique=True)
    password_hash = db.column(db.string(128))
