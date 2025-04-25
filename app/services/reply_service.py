from app.models.reply import Reply
from app import db
from .log_service import log_action

def create_reply(topic_id, user_id, content, parent_reply_id=None):
    reply = Reply(topic_id=topic_id, user_id=user_id, content=content, parent_reply_id=parent_reply_id)
    db.session.add(reply)
    db.session.commit()

    log_action(
        user_id=user_id,
        action="create_reply",
        target_type="reply",
        target_id=reply.id,
        details=f"Reply added to topic_id={topic_id}"
    )

    return reply

def get_replies(topic_id):
    return Reply.query.filter_by(topic_id=topic_id).order_by(Reply.created_at.asc()).all()

def update_reply(reply_id, content):
    reply = Reply.query.get(reply_id)
    if reply:
        reply.content = content
        db.session.commit()
        log_action(
            user_id=reply.user_id,
            action="update_reply",
            target_type="reply",
            target_id=reply.id,
            details="Reply content updated"
        )
        return reply
    return None

def delete_reply(reply_id):
    reply = Reply.query.get(reply_id)
    if reply:
        db.session.delete(reply)
        db.session.commit()
        log_action(
            user_id=reply.user_id,
            action="delete_reply",
            target_type="reply",
            target_id=reply.id,
            details="Reply deleted"
        )
        return True
    return False
    
def get_nested_replies(reply_id):
    def build_tree(reply):
        return {
            "id": reply.id,
            "content": reply.content,
            "user_id": reply.user_id,
            "created_at": reply.created_at,
            "children": [build_tree(child) for child in reply.children]
        }

    parent_reply = Reply.query.get(reply_id)
    if not parent_reply:
        return None

    return build_tree(parent_reply)
