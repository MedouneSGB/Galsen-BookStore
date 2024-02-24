from flask import render_template, Blueprint, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user

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


@views.route("params", methods=["POST", "GET"])
def params():
    return render_template("params/params.html")


@views.route("/card/search", methods=["POST", "GET"])
def search():
    q = request.args.get("q")
    print(q)
    if q:
        q = q.strip()
        images = Livres.query.filter(
            Livres.nomLivre.ilike(f'%{q}%') | Livres.author.ilike(f'%{q}%') | Livres.categorie.ilike(f'%{q}%'))
        return render_template("card/search.html", books=images, query=q)

    images = Livres.query.filter(Livres.image is not None).all()
    return render_template("card/card.html", books=images, query=q)


all_books = []


@views.route("add_store/<int:card_id>/", methods=["POST", "GET"])
def add_to_store(card_id):
    book = Livres.query.get(card_id)

    if book:
        if card_id in all_books:
            flash(f"Le livre '{book.nomLivre}' est déjà dans votre panier.", "warning")
        else:

            all_books.append(card_id)
            flash(f"Le livre '{book.nomLivre}' a été ajouté à votre panier avec succès.", "success")
    else:
        flash("Livre non trouvé.", "error")
        return redirect(url_for("views.detail", card_id=book._id))

    return redirect(url_for("views.detail", card_id=card_id))


@views.route("store/<int:card_id>/", methods=["POST", "GET"])
def store(card_id):
    book = Livres.query.get(card_id)

    if book:
        if card_id in all_books:
            flash(f"Le livre '{book.nomLivre}' est déjà dans votre panier.", "warning")
        else:
            all_books.append(card_id)
            flash(f"Le livre '{book.nomLivre}' a été ajouté à votre panier avec succès.", "success")
    else:
        flash("Livre non trouvé.", "error")
        return redirect(url_for("views.detail", card_id=card_id))

    return redirect(url_for("views.shop"))


@views.route("shop", methods=["POST", "GET"])
def shop():
    books = [Livres.query.get(card_id) for card_id in all_books]
    return render_template("shop/shop.html", books=books)


@views.route("remove_book/<int:card_id>/", methods=["POST", "GET"])
def remove_book(card_id):
    if card_id in all_books:
        book = Livres.query.get(card_id)
        all_books.remove(card_id)
        flash(f"Le livre '{book.nomLivre}' a été supprimé de votre panier avec succès.", "success")
    else:
        flash("Le livre que vous essayez de supprimer n'est pas dans votre panier.", "error")
    return redirect(url_for("views.shop"))


