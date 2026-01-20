from dev import db
from .models import User
from flask import Blueprint, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/register", methods=["GET", "POST"])
def register_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        h_password = generate_password_hash(password)

        # enter data into the database
        
        # step 1 create a user
        new_user = User(username=username, password=h_password)
        db.session.add(new_user)
        db.session.commit()


    return render_template("reg.html")


@auth.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        # grab user data first
        username = request.form.get("username")
        password = request.form.get("password")

        # check the database if it has this user data
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            # the user exists now we can redirect the user to the dashbord
            return "welcome you are registered"

        else:
            return "user not found"


    return render_template("login.html")













        




























