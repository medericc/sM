from app.models.file import File
from app import db

def save_file(user_id, url, related_topic_id=None):
    file = File(user_id=user_id, url=url, related_topic_id=related_topic_id)
    db.session.add(file)
    db.session.commit()
    return file
