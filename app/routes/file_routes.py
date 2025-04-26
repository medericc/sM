from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.file_service import upload_file
from ..services.file_db_service import get_file, delete_file

file_bp = Blueprint('file', __name__, url_prefix="/files")

@file_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    return upload_file(request.files, get_jwt_identity())

@file_bp.route('/<int:file_id>', methods=['GET'])
@jwt_required()
def retrieve_file(file_id):
    file = get_file(file_id)
    if file:
        return jsonify({
            "id": file.id,
            "url": file.url,
            "uploaded_at": file.uploaded_at.isoformat(),
            "related_topic_id": file.related_topic_id
        }), 200
    return jsonify({"error": "File not found"}), 404

@file_bp.route('/<int:file_id>', methods=['DELETE'])
@jwt_required()
def remove_file(file_id):
    if delete_file(file_id):
        return jsonify({"message": "File deleted"}), 200
    return jsonify({"error": "File not found"}), 404
