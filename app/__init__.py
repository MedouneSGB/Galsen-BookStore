from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .config.config import Config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # initialisation de la db
    db.init_app(app)
    # creation de la db
    from app.views import views

    app.register_blueprint(views)

    return app
