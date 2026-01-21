from dev import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))

