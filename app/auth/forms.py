from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtfforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
    '''
    Class to create a login form
    '''
    email = StringField('Email address', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Signin')