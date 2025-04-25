from . import db
from datetime import datetime

class Forum(db.Model):
    __tablename__ = 'forums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    created_by_user = db.relationship("User", back_populates="created_forums")
    watched_forums = db.relationship("WatchedForum", back_populates="forum", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Forum(id={self.id}, title='{self.title}')>"
