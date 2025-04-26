from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.user_service import (
    get_user_by_id,
    get_user_by_username,
    get_user_by_email,
    update_user,
    update_user_password,
    delete_user
)

user_bp = Blueprint('user', __name__)

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    }), 200

@user_bp.route('/me', methods=['PUT'])
@jwt_required()
def update_me():
    user_id = get_jwt_identity()
    data = request.json
    user = update_user(user_id, data)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'Profile updated'}), 200

@user_bp.route('/me/password', methods=['PUT'])
@jwt_required()
def update_password():
    user_id = get_jwt_identity()
    data = request.json
    new_password_hash = data.get('new_password_hash')
    if not new_password_hash:
        return jsonify({'message': 'New password hash required'}), 400
    user = update_user_password(user_id, new_password_hash)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'Password updated'}), 200

@user_bp.route('/me', methods=['DELETE'])
@jwt_required()
def delete_me():
    user_id = get_jwt_identity()
    success = delete_user(user_id)
    if not success:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'User deleted'}), 200

# Optionnel : endpoints d’admin ou pour debug

@user_bp.route('/by-username/<string:username>', methods=['GET'])
def user_by_username(username):
    user = get_user_by_username(username)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200

@user_bp.route('/by-email/<string:email>', methods=['GET'])
def user_by_email(email):
    user = get_user_by_email(email)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200
