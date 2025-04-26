from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.like_service import *

like_bp = Blueprint('like', __name__)

@like_bp.route('/topic/<int:topic_id>', methods=['POST'])
@jwt_required()
def like_topic_route(topic_id):
    like = like_topic(get_jwt_identity(), topic_id)
    return jsonify({'message': 'Topic liked', 'like': like.id}), 201

@like_bp.route('/topic/<int:topic_id>', methods=['DELETE'])
@jwt_required()
def unlike_topic_route(topic_id):
    success = unlike_topic(get_jwt_identity(), topic_id)
    if success:
        return jsonify({'message': 'Topic unliked'}), 200
    return jsonify({'message': 'Like not found'}), 404

@like_bp.route('/reply/<int:reply_id>', methods=['POST'])
@jwt_required()
def like_reply_route(reply_id):
    like = like_reply(get_jwt_identity(), reply_id)
    return jsonify({'message': 'Reply liked', 'like': like.id}), 201

@like_bp.route('/reply/<int:reply_id>', methods=['DELETE'])
@jwt_required()
def unlike_reply_route(reply_id):
    success = unlike_reply(get_jwt_identity(), reply_id)
    if success:
        return jsonify({'message': 'Reply unliked'}), 200
    return jsonify({'message': 'Like not found'}), 404
