from flask import render_template, Blueprint, request
from flask_login import login_required

from app import db
from app.models import Livres, User

views = Blueprint('views', __name__, url_prefix="/")


@views.route("/")
def home():
    books = Livres.query.limit(4).all()
    return render_template("table/table.html", books=books, is_card_view=True)


@views.route("/card", methods=["POST", "GET"])
def card():
    images = Livres.query.filter(Livres.image is not None).all()
    return render_template("card/card.html", books=images)


@views.route("/card/<int:card_id>", methods=["POST", "GET"])
def detail(card_id):
    card_detail = Livres.query.get(card_id)
    return render_template("card/detail.html", book=card_detail)


@views.route("/table", methods=["POST", "GET"])
def table():
    books = Livres.query.limit(4).all()
    return render_template("table/table.html", books=books)


@views.route("/card/<int:card_id>/edit", methods=["POST", "GET"])
@login_required
def update(card_id: int):
    card_detail = Livres.query.get(card_id)
    if request.method == "POST":
        nom = request.form["nomLivre"]
        author = request.form["author"]
        description = request.form["description"]

        card_detail.nomLivre = nom
        card_detail.author = author
        card_detail.description = description
        db.session.commit()

        print(f"{nom} - {description} {author}")
        return render_template("card/detail.html", book=card_detail)

    return render_template("card/edit.html", book=card_detail)
