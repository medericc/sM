from flask import Blueprint, request, jsonify
from ..services.auth_service import register_user, authenticate_user
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    
    required_fields = ['username', 'email', 'password', 'role', 'badge_level', 'branch']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f"'{field}' is required"}), 400

    user = register_user(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        role=data['role'],
        badge_level=data['badge_level'],
        branch=data['branch']
    )
    return jsonify(user.serialize()), 201

@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS preflight successful'})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response, 200

    try:
        data = request.json
        user = authenticate_user(data['email'], data['password'])
        if not user:
            return jsonify({'error': 'Invalid credentials'}), 401
        access_token = create_access_token(identity=user.id)
        response = jsonify({'access_token': access_token})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        return response, 200
    except Exception as e:
        print(f"Error in /login: {e}")
        return jsonify({'error': 'Internal server error'}), 500