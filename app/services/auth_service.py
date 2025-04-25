from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(username, email, password):
    hashed = generate_password_hash(password)
    user = User(username=username, email=email, password_hash=hashed)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        return user
    return None
