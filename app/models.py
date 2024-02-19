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

    def get_id(self):
        return str(self._id)
