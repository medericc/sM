from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.reply_service import *

reply_bp = Blueprint('reply', __name__)

@reply_bp.route('/', methods=['POST'])
@jwt_required()
def create():
    return create_reply(request.json, get_jwt_identity())

@reply_bp.route('/topic/<int:topic_id>', methods=['GET'])
def get_for_topic(topic_id):
    return list_replies_for_topic(topic_id)

@reply_bp.route('/<int:reply_id>', methods=['PUT'])
@jwt_required()
def update(reply_id):
    return update_reply(reply_id, request.json, get_jwt_identity())

@reply_bp.route('/<int:reply_id>', methods=['DELETE'])
@jwt_required()
def delete(reply_id):
    return delete_reply(reply_id, get_jwt_identity())
