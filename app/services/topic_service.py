from app.models.topic import Topic
from app import db
from .log_service import log_action

def create_topic(title, content, user_id, category_id):
    topic = Topic(title=title, content=content, user_id=user_id, category_id=category_id)
    db.session.add(topic)
    db.session.commit()
    return topic

def get_topic_by_id(topic_id):
    return Topic.query.get(topic_id)

def update_topic(topic, new_data):
    for key, value in new_data.items():
        setattr(topic, key, value)
    db.session.commit()
    return topic

def delete_topic(topic, user_id):
    db.session.delete(topic)
    db.session.commit()

    log_action(
        user_id=user_id,
        action="delete_topic",
        target_type="topic",
        target_id=topic.id,
        details=f"Topic '{topic.title}' deleted"
    )