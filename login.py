from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
CSRF_ENABLED = True


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])