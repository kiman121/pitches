from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model):
    '''
    Class that creates new users
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    other_names = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    profile_pic_path = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    @property
    def password(self):
        '''
        Method to block access to the password property
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        '''
        Method to generate a password hash
        Args:
            password: password to hash
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        '''
        Method to verify the password on login
        Args:
            password: password to verify
        '''
        return check_password_hash(self.password_hash, password)


class Category(db.Model):
    '''
    Class that creates a pitch Category Object
    '''
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255))
    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def __init__(self, id, category_name):
        '''
        Method that defines Category object properties.
        Args: 
            id: New category id
            category_name: New category name
        '''
        self.id = id
        self.category_name = category_name

    def save_category(self):
        '''
        Method that saves the instance of review model
        '''
        db.session.add(self)
        db.session.commit()

    def get_categories(self):
        '''
        Method that retrieves pitch categories (all)
        '''
        categories = Category.query.all()
        return categories


class Post(db.Model):
    '''
    Class that creates a post object
    '''
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories'))
