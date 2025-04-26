from flask import Blueprint, request, jsonify
from ..services.search_service import search_users, search_topics, search_replies

search_bp = Blueprint('search', __name__)

@search_bp.route('/users', methods=['GET'])
def search_users_route():
    query = request.args.get('q', '')
    results = search_users(query)
    return jsonify([{'id': u.id, 'username': u.username, 'email': u.email} for u in results]), 200

@search_bp.route('/topics', methods=['GET'])
def search_topics_route():
    query = request.args.get('q', '')
    results = search_topics(query)
    return jsonify([{'id': t.id, 'title': t.title, 'content': t.content} for t in results]), 200

@search_bp.route('/replies', methods=['GET'])
def search_replies_route():
    query = request.args.get('q', '')
    results = search_replies(query)
    return jsonify([{'id': r.id, 'content': r.content, 'user_id': r.user_id} for r in results]), 200
