import bcrypt
from flask import Blueprint
from flask_login import login_user, logout_user, login_required, current_user

from app import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, redirect, request, url_for, session, Blueprint, flash

authentication = Blueprint('auth', __name__, url_prefix="/")


@authentication.route("/inscription", methods=["POST", "GET"])
def inscription():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        user = User.query.filter_by(email=email).first()

        if user:
            flash(f"Cette email {email} existe deja", category="error")
        elif password1 != password2:
            flash("Veillez confirmer le vrai mot de passe", category="error")
        else:
            hashed = bcrypt.hashpw(password1.encode("utf-8"), bcrypt.gensalt())

            new_user = User(
                email=email,
                password=hashed,
                username=username
            )
            db.session.add(new_user)
            db.session.commit()

            if new_user._id is not None:
                login_user(new_user, remember=True)
                flash("Inscription reussi. Vous etes maintenant connecter.", category="success")
                return redirect(url_for("views.card"))
            else:
                flash("Échec de l'inscription Veuillez réessayer.", category="error")

    return render_template("inscription/signUp.html", user=current_user)


@authentication.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.checkpw(password.encode("utf-8"), user.password):
                flash("Connexion reussi", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.card"))
            else:
                flash("Mot de passe incorrect veillez reessayer", category="error")
        else:
            flash("Cette email n'existe pas !", category="error")

    return render_template("login/login.html", user=current_user)


@authentication.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))