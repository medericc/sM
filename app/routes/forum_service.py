from flask import jsonify
from ..models import Forum, User
from .. import db
from ..utils.auth_utils import check_permissions

def list_forums():
    forums = Forum.query.all()
    return jsonify([forum.serialize() for forum in forums])

def create_forum(data, user_id):
    forum = Forum(**data, created_by=user_id)
    db.session.add(forum)
    db.session.commit()
    return jsonify(forum.serialize()), 201

def update_forum(forum_id, data, user_id):
    forum = Forum.query.get_or_404(forum_id)
    if not check_permissions(user_id, forum.created_by):
        return jsonify({'error': 'Forbidden'}), 403
    for key, value in data.items():
        setattr(forum, key, value)
    db.session.commit()
    return jsonify(forum.serialize())

def delete_forum(forum_id, user_id):
    forum = Forum.query.get_or_404(forum_id)
    if not check_permissions(user_id, forum.created_by, allow_subadmin=True):
        return jsonify({'error': 'Forbidden'}), 403
    db.session.delete(forum)
    db.session.commit()
    return jsonify({'message': 'Forum deleted'})