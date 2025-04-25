from app.models.user import User
from app.models.topic import Topic
from app.models.reply import Reply

def search_users(query):
    return User.query.filter(User.username.ilike(f"%{query}%")).all()

def search_topics(query):
    return Topic.query.filter(Topic.title.ilike(f"%{query}%")).all()

def search_replies(query):
    return Reply.query.filter(Reply.content.ilike(f"%{query}%")).all()
