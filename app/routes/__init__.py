from flask import Blueprint
from .auth_routes import auth_bp
from .user_routes import user_bp
from .topic_routes import topic_bp
from .reply_routes import reply_bp
from .like_routes import like_bp
from .message_routes import message_bp
from .notification_routes import notification_bp
from .file_routes import file_bp
from .follow_routes import follow_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(topic_bp, url_prefix="/api/topics")
    app.register_blueprint(reply_bp, url_prefix="/api/replies")
    app.register_blueprint(like_bp, url_prefix="/api/likes")
    app.register_blueprint(message_bp, url_prefix="/api/messages")
    app.register_blueprint(notification_bp, url_prefix="/api/notifications")
    app.register_blueprint(file_bp, url_prefix="/api/files")
    app.register_blueprint(follow_bp, url_prefix="/api/follow")
