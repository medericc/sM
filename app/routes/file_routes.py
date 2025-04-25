from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.file_service import upload_file

file_bp = Blueprint('file', __name__)

@file_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    return upload_file(request.files, get_jwt_identity())
