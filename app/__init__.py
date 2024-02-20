from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from .config.config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .models import db, User
    # initialisation de la db
    db.init_app(app)
    # creation de la db
    from app.views import views
    from app.authentification.routes import authentication

    login_manager.init_app(app)

    app.register_blueprint(views)
    app.register_blueprint(authentication)

    # Pour charger l'utilisateur à partir de la session
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
