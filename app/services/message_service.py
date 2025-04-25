from app.models.private_message import PrivateMessage
from app import db

def send_message(sender_id, receiver_id, content):
    message = PrivateMessage(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.session.add(message)
    db.session.commit()
    return message
