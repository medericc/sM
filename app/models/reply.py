from app import db
from datetime import datetime

class Reply(db.Model):
    __tablename__ = 'replies'

    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    parent_reply_id = db.Column(db.Integer, db.ForeignKey('replies.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    topic = db.relationship("Topic", back_populates="replies")
    user = db.relationship("User")
    parent = db.relationship("Reply", remote_side=[id], back_populates="children")
    children = db.relationship("Reply", back_populates="parent", cascade="all, delete-orphan")
    likes = db.relationship("ReplyLike", back_populates="reply", cascade="all, delete-orphan")
