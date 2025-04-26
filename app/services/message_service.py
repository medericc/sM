from app.models.message import Message
from app import db

def send_message(sender_id, receiver_id, content):
    message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.session.add(message)
    db.session.commit()
    return message

def get_messages(user1_id, user2_id):
    messages = Message.query.filter(
        db.or_(
            db.and_(
                Message.sender_id == user1_id,
                Message.receiver_id == user2_id
            ),
            db.and_(
                Message.sender_id == user2_id,
                Message.receiver_id == user1_id
            )
        )
    ).order_by(Message.sent_at.asc()).all()
    return messages
