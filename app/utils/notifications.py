from app.models.notification import Notification
from . import db

def create_notification(user_id, message, notif_type):
    notif = Notification(
        user_id=user_id,
        message=message,
        type=notif_type
    )
    db.session.add(notif)
    db.session.commit()
    return notif
