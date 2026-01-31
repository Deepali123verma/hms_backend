from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from flask import current_app

def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hashed):
    return check_password_hash(hashed, password)

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
