from . import db
from datetime import datetime

class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action = db.Column(db.String(100), nullable=False) 
    target_type = db.Column(db.String(100), nullable=False)  
    target_id = db.Column(db.Integer, nullable=False)  
    details = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="logs")

    def __repr__(self):
        return f"<Log(id={self.id}, action='{self.action}', target={self.target_type}:{self.target_id})>"
