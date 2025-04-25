from . import db
from datetime import datetime

class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    url = db.Column(db.String(255), nullable=False, comment='Firebase Storage URL')
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    related_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=True)

    user = db.relationship("User", back_populates="files")
    topic = db.relationship("Topic", back_populates="files")

    def __repr__(self):
        return f"<File(id={self.id}, url='{self.url}')>"
