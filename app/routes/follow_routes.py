from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.follow_service import *

follow_bp = Blueprint('follow', __name__)

@follow_bp.route('/<int:user_id>', methods=['POST'])
@jwt_required()
def follow(user_id):
    return follow_user(get_jwt_identity(), user_id)

@follow_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def unfollow(user_id):
    return unfollow_user(get_jwt_identity(), user_id)
