from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db


class Livres(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    nomLivre = db.Column(db.String(100), nullable=False)
    categorie = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text(), nullable=True, default="images")
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    qteStock = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user._id'))

    def get_id(self):
        return str(self._id)


class User(db.Model, UserMixin):
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(1000), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    livres = db.relationship('Livres')
    isAdmin = db.Column(db.Boolean, nullable=False, default=True)

    def get_id(self):
        return str(self._id)

