from app.models.message import Message
from app import db

def send_message(sender_id, receiver_id, content):
    message = PrivateMessage(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.session.add(message)
    db.session.commit()
    return message

def get_messages(user1_id, user2_id):
    messages = PrivateMessage.query.filter(
        db.or_(
            db.and_(
                PrivateMessage.sender_id == user1_id,
                PrivateMessage.receiver_id == user2_id
            ),
            db.and_(
                PrivateMessage.sender_id == user2_id,
                PrivateMessage.receiver_id == user1_id
            )
        )
    ).order_by(PrivateMessage.sent_at.asc()).all()
    return messages
