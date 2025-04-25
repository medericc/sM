from app.models.reply import Reply
from app import db

def add_reply(topic_id, user_id, content, parent_reply_id=None):
    reply = Reply(topic_id=topic_id, user_id=user_id, content=content, parent_reply_id=parent_reply_id)
    db.session.add(reply)
    db.session.commit()
    return reply
