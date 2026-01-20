from flask import Blueprint, render_template, request
from fileinput import filename
view = Blueprint("view", __name__, template_folder="templates")



@view.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        file = request.files["user_file"]
        file.save(file.filename)
    return render_template("index.html") 

@view.route("/download")
def download_page():
    return render_template("download.html")
