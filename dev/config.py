# this file contains configurations of the app

import os

class Config(object):
    UPLOAD_FOLDER = "uploads/"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "HARD TO GUESS"
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
