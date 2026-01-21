from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()
UPLOAD_FOLDER = "uploads/"
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    

    # import database model
    #from .models import User
    from .auth import auth
    from .views import view

    # register the blueprints
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(view, url_prefix="/")
    # create the database
    db.init_app(app)
    create_database(app)

    return app

def create_database(app):
    if not os.path.exists("users.db"):
        with app.app_context():
            db.create_all()
                                                                                                                                                                                                                                                                        

