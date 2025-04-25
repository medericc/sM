from . import db
from datetime import datetime

class WatchedForum(db.Model):
    __tablename__ = 'watched_forums'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    forum_id = db.Column(db.Integer, db.ForeignKey('forums.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relation avec Forum
    forum = db.relationship("Forum", back_populates="watched_forums")

    # Relation avec User
    user = db.relationship("User", back_populates="watched_forums")

    def __repr__(self):
        return f"<WatchedForum(id={self.id}, user_id={self.user_id}, forum_id={self.forum_id})>"