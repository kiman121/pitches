from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from . import main
from .forms import PostForm, AddComment
from ..models import Post, Category, Comment
from ..request import get_posts, get_comments
from ..import db


@main.route('/')
def index():
    '''
    View function that returns the index page
    '''
    posts = get_posts()
    comments = get_comments()
    title = "Pitches - home"

    post_form = PostForm()
    comment_form = AddComment()

    return render_template('index.html', title=title, post_form=post_form, posts=posts, comment_form=comment_form, comments=comments)


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

    return redirect(url_for('.index'))
