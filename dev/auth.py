from dev import db
from flask_login import login_user
from .models import User
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/register", methods=["GET", "POST"])
def register_page():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        c_password = request.form.get("c_password")

        if password == c_password:
            h_password = generate_password_hash(password)

            # enter data into the database
        
            # step 1 create a user
            new_user = User(username=username, email=email, password=h_password)
            db.session.add(new_user)
            db.session.commit()

            # here were are done hence rediect the user to log in
            return redirect(url_for('auth.login_page'))

        else:
            return "passwords dont match"


    return render_template("reg.html")


@auth.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        # grab user data first
        email = request.form.get("email")
        password = request.form.get("password")

        # check the database if it has this user data
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # the user exists now we can redirect the user to the dashbord
            login_user(user)
            return redirect(url_for('view.home_page'))

        else:
            return "invalid password or email"


    return render_template("login.html")













        




























