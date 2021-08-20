from flask import render_template, redirect, url_for, request, abort
from flask_login import login_required, current_user
from . import main
from .forms import PostForm, AddComment, UpdateProfile
from ..auth.forms import LoginForm, RegistrationForm
from ..models import User, Post, Category, Comment
from ..request import get_posts, get_comments, get_posts_by_user_id, get_posts_by_post_id
from ..import db, photos
from sqlalchemy import func


@main.route('/')
def index():
    '''
    View function that returns the index page
    '''
    # posts = get_posts()
    # comments = get_comments()
    title = "Pitches - home"

    # login_form = LoginForm()
    # registration_form = RegistrationForm()
    # post_form = PostForm()
    # comment_form = AddComment()

    # return render_template('index.html', title=title, post_form=post_form, posts=posts, comment_form=comment_form, comments=comments)
    return render_template('index.html', title=title)


@main.route('/home/<int:cid>', methods=['GET'])
@login_required
def home(cid):
    '''
    View function that returns the home page
    '''
    categories = Category.get_categories()

    posts = get_posts(cid)
    # comments = get_comments()

    if cid == 0:
        category_name = "All Categories"
    else:
        selected_category = Category.get_category_by_id(cid)
        category_name = selected_category.category_name

    # login_form = LoginForm()
    # registration_form = RegistrationForm()
    post_form = PostForm()
    # comment_form = AddComment()

    title = 'Pitches - home'

    return render_template('home.html', title=title, posts=posts, categories=categories, category_name=category_name)
    # return render_template('home.html', title=title)


@main.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    '''
    View function that handles a post request
    '''
    form = PostForm()

    if form.validate_on_submit():
        new_post = Post(post=form.post.data, user_id=current_user.get_id(
        ), category_id=form.category.data.id)

        db.session.add(new_post)
        db.session.commit()

    return redirect(url_for('.index'))


@main.route('/post/comment/<int:pid>/<int:uid>', methods=['POST'])
@login_required
def add_comment(pid, uid):
    '''
    View function that handles an add comment request
    '''
    form = AddComment()

    if form.validate_on_submit():
        new_comment = Comment(post_id=pid, user_id=uid,
                              comments=form.comment.data)
        db.session.add(new_comment)
        db.session.commit()

    return redirect(url_for('.post', pid=pid))


@main.route('/post/vote/<int:pid>/<votetype>')
@login_required
def add_comment_vote(pid, votetype):

    post = Post.query.filter_by(id=pid).first()

    # initial_tally = None

    if votetype == 'upvote':

        if post.upvote == None:
            post.upvote = 1
        else:
            post.upvote += 1
    elif votetype == 'downvote':
        if post.downvote == None:
            post.downvote = 1
        else:
            post.downvote += 1

    db.session.commit()

    return redirect(url_for('.post', pid=pid))


@main.route('/user/profile/<int:userid>')
@login_required
def profile(userid):
    '''
    View function that displays a user profile
    '''
    user = User.query.filter_by(id=userid).first()
    posts = get_posts_by_user_id(userid)
    title = "Pitches - profile"

    return render_template('user-profile.html', user=user, title=title, posts=posts)


@main.route('/user/profile/update/<int:userid>', methods=['GET', 'POST'])
@login_required
def update_profile(userid):
    '''
    Function that handles the update user profile request
    Args:
        userid: user id
    Return:
        User profile page
    '''

    user = User.query.filter_by(id=userid).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('.profile', userid=userid))

@main.route('/post/<int:pid>', methods=['GET','POST'])
@login_required
def post(pid):
    '''
    View function that displays a selected post
    '''
    comments = get_comments()
    post = get_posts_by_post_id(pid)
    title = "Pitches - post"

    login_form = LoginForm()
    registration_form = RegistrationForm()
    post_form = PostForm()
    comment_form = AddComment()

    return render_template('post.html', title=title, post_form=post_form, post=post, comment_form=comment_form, comments=comments)



