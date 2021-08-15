from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
    '''
    Class to create a login form
    '''
    email = StringField('Email address', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Signin')

# id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(255))
#     other_names = db.Column(db.String(255))
#     username = db.Column(db.String(255))
#     email = db.Column(db.String(255), unique=True, index=True)

class RegistrationForm(FlaskForm):
    '''
    Class to create a registration form
    '''
    first_name = StringField("First name", validators=[Required()])
    other_names = StringField("Other names", validators=[Required()])
    username = StringField("Enter your username", validators=[Required()])
    email = StringField("Your Email Address", validators=[Required(), Email()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self, data_field):
        '''
        Method to confirm if there is no user registered with that email address
        Args:
            data_field: email or username
        Return: 
            validation error if user exists
        '''
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('Email exists!')
    
    def validate_username(self, data_field):
        '''
        Method to confirm if username is unique and raise validation error if another user 
        has the same username
        Args:
            data_field: email or username
        Return: 
            validation error if user exists
        '''
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken!')