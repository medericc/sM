from app.models.user import User
from app import db

def get_admins():
    return User.query.filter(User.role.in_(["admin", "subadmin"])).all()

def add_admin(user_id, level="admin"):
    user = User.query.get(user_id)
    if user:
        user.role = level  # "admin" or "subadmin"
        db.session.commit()
    return user

def remove_admin(user_id):
    user = User.query.get(user_id)
    if user and user.role in ["admin", "subadmin"]:
        user.role = "user"
        db.session.commit()
    return user
