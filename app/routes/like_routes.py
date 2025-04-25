from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.like_service import *

like_bp = Blueprint('like', __name__)

@like_bp.route('/topic/<int:topic_id>', methods=['POST'])
@jwt_required()
def like_topic(topic_id):
    return like_topic_service(topic_id, get_jwt_identity())

@like_bp.route('/reply/<int:reply_id>', methods=['POST'])
@jwt_required()
def like_reply(reply_id):
    return like_reply_service(reply_id, get_jwt_identity())
