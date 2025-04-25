from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.notification_service import *

notification_bp = Blueprint('notification', __name__)

@notification_bp.route('/', methods=['GET'])
@jwt_required()
def get_all():
    return get_notifications(get_jwt_identity())
