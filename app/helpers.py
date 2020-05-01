
from flask import request, jsonify
import jwt
from functools import wraps
from app.models import getUser

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
            current_user = getUser(data['username'])
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator