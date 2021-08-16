from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import Required, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField
from ..models import Category
from wtforms import ValidationError


class PostForm(FlaskForm):
    '''
    Class to create a post form
    '''
    def category_query():
        return Category.query

    category = QuerySelectField(query_factory = category_query, allow_blank=True,blank_text="Select category", get_label='category_name',validators=[Required()])
    post = StringField('Your post...', validators=[Required()])
    submit = SubmitField('Post')

class AddComment(FlaskForm):
    '''
    Class to create add comment form
    '''
    comment = StringField('Add comment', validators=[Required()])
    submit = SubmitField('Add')