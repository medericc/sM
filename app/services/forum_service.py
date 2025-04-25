from app.models.forum import Forum
from app import db

def create_forum(title, description, created_by):
    forum = Forum(title=title, description=description, created_by=created_by)
    db.session.add(forum)
    db.session.commit()
    return forum

def get_all_forums():
    return Forum.query.all()
