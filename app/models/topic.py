from datetime import datetime
from . import db

class Topic(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relation avec Reply
    replies = db.relationship("Reply", back_populates="topic", cascade="all, delete-orphan")

    # Relation avec User
    user = db.relationship('User', backref='topics')

    # Relation avec Category
    category = db.relationship('Category', back_populates='topics')

    # Relation avec TopicLike
    likes = db.relationship("TopicLike", back_populates="topic", cascade="all, delete-orphan")

    # Relation avec File
    files = db.relationship("File", back_populates="topic", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Topic(id={self.id}, title='{self.title}')>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "user_id": self.user_id,
            "category_id": self.category_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }