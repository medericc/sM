from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.follow_service import (
    follow_user, unfollow_user, get_followers, get_following
)

follow_bp = Blueprint('follow', __name__)

# Suivre un utilisateur
@follow_bp.route('/<int:user_id>', methods=['POST'])
@jwt_required()
def follow(user_id):
    return follow_user(get_jwt_identity(), user_id)

# Se désabonner d’un utilisateur
@follow_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def unfollow(user_id):
    return unfollow_user(get_jwt_identity(), user_id)

# Voir qui suit un utilisateur
@follow_bp.route('/<int:user_id>/followers', methods=['GET'])
@jwt_required()
def followers(user_id):
    return get_followers(user_id)

# Voir qui l’utilisateur suit
@follow_bp.route('/<int:user_id>/following', methods=['GET'])
@jwt_required()
def following(user_id):
    return get_following(user_id)
