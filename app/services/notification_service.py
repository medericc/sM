from app.models.notification import Notification
from app import db

def create_notification(user_id, message, type_):
    notif = Notification(user_id=user_id, message=message, type=type_)
    db.session.add(notif)
    db.session.commit()
    return notif

def get_user_notifications(user_id):
    return Notification.query.filter_by(user_id=user_id).order_by(Notification.created_at.desc()).all()
