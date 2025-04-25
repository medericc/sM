from app.models.topic_like import TopicLike
from app.models.reply_like import ReplyLike
from app import db

def like_topic(user_id, topic_id):
    like = TopicLike(user_id=user_id, topic_id=topic_id)
    db.session.add(like)
    db.session.commit()
    return like

def like_reply(user_id, reply_id):
    like = ReplyLike(user_id=user_id, reply_id=reply_id)
    db.session.add(like)
    db.session.commit()
    return like
