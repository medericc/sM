from flask import Blueprint, request, jsonify
from ..services.auth_service import register_user, authenticate_user
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    
    # Vérifiez que les champs obligatoires sont présents
    required_fields = ['username', 'email', 'password', 'role', 'badge_level', 'branch']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f"'{field}' is required"}), 400

    # Créez l'utilisateur
    user = register_user(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        role=data['role'],
        badge_level=data['badge_level'],
        branch=data['branch']
    )
    return jsonify(user.serialize()), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = authenticate_user(data['email'], data['password'])
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token})