from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import get_jwt_identity

def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hash_):
    return check_password_hash(hash_, password)

def get_current_user_id():
    return get_jwt_identity()
