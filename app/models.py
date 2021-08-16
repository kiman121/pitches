from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    '''
    Callback function that retrieves a user when a unique identifier is passed
    '''
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
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
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    # def __init__(self, first_name, other_names,username,email):
    #     '''
    #     Method that defines User object properties.
    #     Args: 
    #         first_name: New user first name
    #         other_names: New user other names
    #         username: New user username
    #     '''
    #     self.first_name = first_name
    #     self.other_names = other_names
    #     self.username = username
    #     self.email = email

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

    def __init__(self, category_name):
        '''
        Method that defines Category object properties.
        Args: 
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
    post = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    comments = db.relationship('Comment', backref='comment', lazy='dynamic')

    def __init__(self, post,user_id,category_id):
        '''
        '''
        self.post = post
        self.user_id = user_id
        self.category_id = category_id
    
    # def save_post(self):
    #     '''
    #     Method that saves the instance of post model
    #     '''
    #     db.session.add(self)
    #     db.session.commit()
    
    # def get_posts():
    #     '''
    #     Method that retrives posts
    #     Args: 
    #         # id: post id
    #     '''
    #     return Post.query.all()

class PostDetails:
    '''
    Post details class to define post details objects
    '''
    def __init__(self, post_id,post_date ,post_detail,category,posted_by,profile_pic_path):
        self.post_id = post_id
        self.post_date = post_date
        self.post_detail = post_detail
        self.category=category
        self.posted_by = posted_by
        self.profile_pic_path = profile_pic_path
        # self.post_comments = post_comments
class Comment(db.Model):
    '''
    Clas that creates comment objects
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, post_id, user_id, comments):
        '''
        Method that defines Comment object properties.
        Args: 
            post_id: New comment post id
            user_id: New comment user id
            comments: New comment comments
            created_at: New comment date time
        '''
        self.post_id = post_id
        self.user_id = user_id
        self.comments = comments
        # self.created_at =created_at
    
    def save_comment(self):
        '''
        Method that saves the instance of the comment model
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_comments(cls, id):
        '''
        Method that retrieves post comments based on the post id
        Args:
            id: post id
        '''
        comments = Comment.query.filter_by(post_id=id).all()
        return comments
    
class CommentDetails:
    def __init__(self,post_id, comment_date,commented_by,profile_pic_path):
        self.post_id = post_id
        self.comment_date =comment_date
        self.commented_by = commented_by
        self.profile_pic_path = profile_pic_path