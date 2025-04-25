from app.models.topic_like import TopicLike
from app.models.reply_like import ReplyLike
from app import db

def like_topic(user_id, topic_id):
    existing_like = TopicLike.query.filter_by(user_id=user_id, topic_id=topic_id).first()
    if existing_like:
        return existing_like
    like = TopicLike(user_id=user_id, topic_id=topic_id)
    db.session.add(like)
    db.session.commit()
    return like

def unlike_topic(user_id, topic_id):
    like = TopicLike.query.filter_by(user_id=user_id, topic_id=topic_id).first()
    if like:
        db.session.delete(like)
        db.session.commit()
        return True
    return False

def get_likes_topic(topic_id):
    return TopicLike.query.filter_by(topic_id=topic_id).count()

def like_reply(user_id, reply_id):
    existing_like = ReplyLike.query.filter_by(user_id=user_id, reply_id=reply_id).first()
    if existing_like:
        return existing_like
    like = ReplyLike(user_id=user_id, reply_id=reply_id)
    db.session.add(like)
    db.session.commit()
    return like

def unlike_reply(user_id, reply_id):
    like = ReplyLike.query.filter_by(user_id=user_id, reply_id=reply_id).first()
    if like:
        db.session.delete(like)
        db.session.commit()
        return True
    return False

def get_likes_reply(reply_id):
    return ReplyLike.query.filter_by(reply_id=reply_id).count()
