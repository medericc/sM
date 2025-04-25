from . import db
from sqlalchemy import UniqueConstraint
from datetime import datetime

class TopicLike(db.Model):
    __tablename__ = 'topic_likes'

    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (UniqueConstraint('topic_id', 'user_id', name='_user_topic_uc'),)

    topic = db.relationship("Topic", back_populates="likes")
    user = db.relationship("User")

    def __repr__(self):
        return f"<TopicLike(user_id={self.user_id}, topic_id={self.topic_id})>"

class ReplyLike(db.Model):
    __tablename__ = 'reply_likes'

    id = db.Column(db.Integer, primary_key=True)
    reply_id = db.Column(db.Integer, db.ForeignKey('replies.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (UniqueConstraint('reply_id', 'user_id', name='_user_reply_uc'),)

    reply = db.relationship("Reply", back_populates="likes")
    user = db.relationship("User")

    def __repr__(self):
        return f"<ReplyLike(user_id={self.user_id}, reply_id={self.reply_id})>"