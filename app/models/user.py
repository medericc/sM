from app import db
from datetime import datetime
from .follow import Follow  

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)
    role = db.Column(db.String(20))
    badge_level = db.Column(db.String(20))
    branch = db.Column(db.String(50))
    parish = db.Column(db.String(100))
    tiktok_handle = db.Column(db.String(100))
    discord_id = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relation avec les fichiers uploadés
    files = db.relationship(
        "File",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    # Relation avec les forums créés
    created_forums = db.relationship(
        "Forum",
        back_populates="created_by_user",
        cascade="all, delete-orphan"
    )

    # Relation avec les messages envoyés
    sent_messages = db.relationship(
        "Message",
        foreign_keys="[Message.sender_id]",
        back_populates="sender",
        cascade="all, delete-orphan"
    )

    # Relation avec les messages reçus
    received_messages = db.relationship(
        "Message",
        foreign_keys="[Message.receiver_id]",
        back_populates="receiver",
        cascade="all, delete-orphan"
    )

    # Relation avec Log
    logs = db.relationship("Log", back_populates="user", cascade="all, delete-orphan")

    # Relations pour le suivi (following/followers)
    following = db.relationship(
        'Follow',
        foreign_keys='Follow.following_user_id',
        back_populates='following_user',
        cascade="all, delete-orphan"
    )

    followers = db.relationship(
        'Follow',
        foreign_keys='Follow.followed_user_id',
        back_populates='followed_user',
        cascade="all, delete-orphan"
    )

    # Forums suivis
    watched_forums = db.relationship("WatchedForum", back_populates="user", cascade="all, delete-orphan")

    # Relation avec les notifications
    notifications = db.relationship(
        "Notification",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "badge_level": self.badge_level,
            "branch": self.branch,
            "parish": self.parish,
            "tiktok_handle": self.tiktok_handle,
            "discord_id": self.discord_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }