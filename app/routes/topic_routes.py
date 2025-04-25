from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.topic_service import *

topic_bp = Blueprint('topic', __name__)

@topic_bp.route('/', methods=['POST'])
@jwt_required()
def create():
    return create_topic(request.json, get_jwt_identity())

@topic_bp.route('/', methods=['GET'])
def list_all():
    return list_topics()

@topic_bp.route('/<int:topic_id>', methods=['GET'])
def get(topic_id):
    return get_topic(topic_id)

@topic_bp.route('/<int:topic_id>', methods=['PUT'])
@jwt_required()
def update(topic_id):
    return update_topic(topic_id, request.json, get_jwt_identity())

@topic_bp.route('/<int:topic_id>', methods=['DELETE'])
@jwt_required()
def delete(topic_id):
    return delete_topic(topic_id, get_jwt_identity())
