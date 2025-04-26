from app.models.notification import Notification
from app import db

def create_notification(user_id, message, notif_type):
    notif = Notification(
        user_id=user_id,
        message=message,
        type=notif_type
    )
    db.session.add(notif)
    db.session.commit()
    return notif

def create_formatted_notification(user_id, notif_type, extra_info=None):
    message = format_notification_message(notif_type, extra_info)
    return create_notification(user_id, message, notif_type)

def get_user_notifications(user_id):
    return Notification.query.filter_by(user_id=user_id).order_by(Notification.created_at.desc()).all()

def get_unread_notifications(user_id):
    return Notification.query.filter_by(user_id=user_id, is_read=False).order_by(Notification.created_at.desc()).all()

def mark_notification_as_read(notification_id):
    notif = Notification.query.get(notification_id)
    if notif:
        notif.is_read = True
        db.session.commit()
        return True
    return False

def delete_notification(notification_id):
    notif = Notification.query.get(notification_id)
    if notif:
        db.session.delete(notif)
        db.session.commit()
        return True
    return False

def format_notification_message(notif_type, extra_info=None):
    if notif_type == "post_reply":
        return f"Quelqu’un a répondu à votre post : {extra_info}"
    elif notif_type == "mention":
        return f"Vous avez été mentionné : {extra_info}"
    elif notif_type == "forum_watch":
        return f"Nouveau message dans un forum que vous suivez : {extra_info}"
    elif notif_type == "new_topic":
        return f"Nouveau sujet créé : {extra_info}"
    elif notif_type == "tiktok_live":
        return "Un live TikTok a commencé"
    return "Nouvelle notification"
