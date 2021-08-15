from flask import render_template, redirect, url_for, request
from . import main
from flask_login import login_required, current_user
from .forms import PostForm
from ..models import Post, Category
from ..import db
import re


@main.route('/')
def index():
    '''
    View function that returns the index page
    '''
    title = "Pitches - home"
    form = PostForm()
    return render_template('index.html', title=title, post_form=form)


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
