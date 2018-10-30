from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegistrationForm(FlaskForm):
    username = StringField('username')
    email = StringField('email')
    passvowd = PasswordField('password')
    confirm_password = PasswordField('confirm_password')

    submit = SubmitField('sign up')


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')

    submit = SubmitField('sign up')