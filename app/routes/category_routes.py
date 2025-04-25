from flask import Blueprint, jsonify
from app.services.category_service import get_topics_by_category, get_categories

category_bp = Blueprint('category', __name__)

@category_bp.route('/', methods=['GET'])
def get_all_categories():
    categories = get_categories()
    return jsonify([
        {
            "id": cat.id,
            "name": cat.name,
            "description": cat.description
        } for cat in categories
    ])

@category_bp.route('/<int:category_id>/topics', methods=['GET'])
def get_category_topics(category_id):
    topics = get_topics_by_category(category_id)
    if topics is None:
        return jsonify({"error": "Category not found"}), 404

    return jsonify([
        {
            "id": topic.id,
            "title": topic.title,
            "content": topic.content,
            "user_id": topic.user_id,
            "created_at": topic.created_at.isoformat(),
            "updated_at": topic.updated_at.isoformat()
        }
        for topic in topics
    ])
