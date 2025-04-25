from . import db
from datetime import datetime

class Follow(db.Model):
    __tablename__ = 'follows'

    following_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    followed_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relations vers User
    following_user = db.relationship("User", foreign_keys=[following_user_id], back_populates="following")
    followed_user = db.relationship("User", foreign_keys=[followed_user_id], back_populates="followers")

    def __repr__(self):
        return f"<Follow(following_user_id={self.following_user_id}, followed_user_id={self.followed_user_id})>"
