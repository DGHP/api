
from time import time

from flask import request, jsonify
from functools import wraps
import jwt

from app.models import get_user

jwt_secret = "top secret secret"


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].replace("Bearer ", "")

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, jwt_secret, algorithm="HS256")
            current_user = get_user(data['username'])
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator


def make_jwt(username):
    now = int(time())
    week_later = now + 604800
    token = jwt.encode({'username': username, 'iat': now,
                        'exp': week_later}, jwt_secret, algorithm="HS256")
    return token
