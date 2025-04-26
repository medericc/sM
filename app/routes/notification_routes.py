from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.notification_service import (
    get_user_notifications,
    get_unread_notifications,
    mark_notification_as_read,
    delete_notification,
    create_formatted_notification
)

notification_bp = Blueprint('notification', __name__, url_prefix="/notifications")

@notification_bp.route('/', methods=['GET'])
@jwt_required()
def get_all():
    user_id = get_jwt_identity()
    notifications = get_user_notifications(user_id)
    return jsonify([notif.to_dict() for notif in notifications]), 200

@notification_bp.route('/unread', methods=['GET'])
@jwt_required()
def get_unread():
    user_id = get_jwt_identity()
    notifications = get_unread_notifications(user_id)
    return jsonify([notif.to_dict() for notif in notifications]), 200

@notification_bp.route('/<int:notification_id>/read', methods=['PATCH'])
@jwt_required()
def mark_as_read(notification_id):
    if mark_notification_as_read(notification_id):
        return jsonify({"message": "Notification marked as read"}), 200
    return jsonify({"error": "Notification not found"}), 404

@notification_bp.route('/<int:notification_id>', methods=['DELETE'])
@jwt_required()
def delete_notif(notification_id):
    if delete_notification(notification_id):
        return jsonify({"message": "Notification deleted"}), 200
    return jsonify({"error": "Notification not found"}), 404

@notification_bp.route('/', methods=['POST'])
@jwt_required()
def create_notif():
    data = request.get_json()
    user_id = data.get("user_id")
    notif_type = data.get("type")
    extra_info = data.get("extra_info")

    if not user_id or not notif_type:
        return jsonify({"error": "Missing user_id or type"}), 400

    notif = create_formatted_notification(user_id, notif_type, extra_info)
    return jsonify(notif.to_dict()), 201
