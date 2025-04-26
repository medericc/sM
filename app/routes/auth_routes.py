from flask import Blueprint, request, jsonify
from ..services.auth_service import register_user, validate_registration_data, authenticate_user
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    # Validation
    error = validate_registration_data(data)
    if error:
        return jsonify({'error': error}), 400

    tiktok_handle = data.get('tiktok_handle')  # facultatif
    discord_id = data.get('discord_id')        # facultatif

    user = register_user(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        role=data['role'],
        badge_level=data['badge_level'],
        branch=data['branch'],
        parish=data['parish'],
        tiktok_handle=tiktok_handle,
        discord_id=discord_id,
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
        
        print('Login data received:', data)
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