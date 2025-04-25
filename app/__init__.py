from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate  # Import de Flask-Migrate
from config import Config

# Initialisation de SQLAlchemy, JWTManager et Flask-Migrate
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()  # Création de l'objet Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)  # Initialisation de Flask-Migrate avec l'app et la base de données

    # Import des modèles
    from .models import user, category, topic, reply, like, follow, message, notification, forum, file

    return app
