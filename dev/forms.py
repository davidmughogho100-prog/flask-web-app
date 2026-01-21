from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField("enter email", validators=[DataRequired()])
    password = PasswordField("enter password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    full_name = StringField("Full name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    c_password = PasswordField("confirm password", validators=[DataRequired()])
    submit = SubmitField("submit")


