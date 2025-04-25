from app.models.user import User
from app import db

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def update_user(user_id, data):
    user = get_user_by_id(user_id)
    if not user:
        return None
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user

def update_user_password(user_id, new_password_hash):
    user = get_user_by_id(user_id)
    if not user:
        return None
    user.password_hash = new_password_hash
    db.session.commit()
    return user

def delete_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return False
    db.session.delete(user)
    db.session.commit()
    return True
