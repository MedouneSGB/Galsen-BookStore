from flask import render_template, redirect, request, url_for, session, Blueprint

from app.models import Livres

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


@views.route("/login", methods=["POST", "GET"])
def login():
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        return redirect(url_for("user"))
    else:
        if "username" in session:
            return redirect(url_for("user"))
        return render_template("login/login.html")
    """
    return render_template("login/login.html")


@views.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))
