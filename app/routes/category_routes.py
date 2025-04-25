from flask import Blueprint, jsonify
from app.services.category_services import get_topics_by_category

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['GET'])
def get_all_categories():
    from app.services.category_services import get_categories  # <-- attention ici
    categories = get_categories()
    return jsonify([
        {
            "id": cat.id,
            "name": cat.name,
            "description": cat.description
        } for cat in categories
    ])



@category_bp.route('/categories/<int:category_id>/topics', methods=['GET'])
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
