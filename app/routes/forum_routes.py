from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services import forum_service

forum_bp = Blueprint('forum', __name__)

@forum_bp.route('/forums', methods=['GET'])
@jwt_required()
def list_forums():
    return forum_service.list_forums()

@forum_bp.route('/forums', methods=['POST'])
@jwt_required()
def create_forum():
    return forum_service.create_forum(request.get_json(), get_jwt_identity())

@forum_bp.route('/forums/<int:forum_id>', methods=['PUT'])
@jwt_required()
def update_forum(forum_id):
    return forum_service.update_forum(forum_id, request.get_json(), get_jwt_identity())

@forum_bp.route('/forums/<int:forum_id>', methods=['DELETE'])
@jwt_required()
def delete_forum(forum_id):
    return forum_service.delete_forum(forum_id, get_jwt_identity())
