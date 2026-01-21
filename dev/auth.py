from dev import db
from .forms import LoginForm, RegisterForm
from .models import User
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        c_password = request.form.get("c_password")

        if password == c_password:
            # set up a use in the database
            h_password = generate_password_hash(password)
            new_user = User(full_name=full_name, email=email, password=h_password)
            db.session.add(new_user)
            db.session.commit()
            # here were are done hence rediect the user to log in
            return redirect(url_for('auth.login_page'))

        else:
            return "passwords dont match"
        # step 1 create a user
        
    return render_template("reg.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if request.method == "POST":
        # grab user data first
        email = request.form.get("email")
        password = request.form.get("password")

        # check the database if it has this user data
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # the user exists now we can redirect the user to the dashbord
            return redirect(url_for('view.home_page'))

        else:
            return "invalid password or email"


    return render_template("login.html", form=form)













        




























