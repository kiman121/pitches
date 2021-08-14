from flask import render_template, redirect, url_for,flash,request
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Function that handles a login request
    '''
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
        
        flash('Invalid username or password')
    
    title = 'Pitches - login'
    return render_template('auth/login.html', login_form, title=title)
