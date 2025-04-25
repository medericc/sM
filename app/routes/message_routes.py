from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.message_service import *

message_bp = Blueprint('message', __name__)

@message_bp.route('/', methods=['POST'])
@jwt_required()
def send():
    return send_message(request.json, get_jwt_identity())

@message_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_conversation(user_id):
    return get_conversation_with(user_id, get_jwt_identity())
