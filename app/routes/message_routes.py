from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.message_service import *

message_bp = Blueprint('message', __name__)

@message_bp.route('/', methods=['POST'])
@jwt_required()
def send():
    sender_id = get_jwt_identity()
    data = request.get_json()
    receiver_id = data.get('receiver_id')
    content = data.get('content')

    if not receiver_id or not content:
        return jsonify({'message': 'receiver_id and content are required'}), 400

    message = send_message(sender_id, receiver_id, content)
    return jsonify(format_message(message)), 201

@message_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_conversation(user_id):
    messages = get_messages(get_jwt_identity(), user_id)
    return jsonify([format_message(m) for m in messages]), 200

