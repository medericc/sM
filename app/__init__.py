from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate 
from config import Config

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate() 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    from .models import user, category, topic, reply, like, follow, message, notification, forum, file

    from .routes import register_routes
    register_routes(app)

    return app

