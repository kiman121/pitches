from flask import render_template, redirect, url_for, request
from . import main


@main.route('/')
def index():
    '''
    View function that returns the index page
    '''
    title = "Pitches - home"
    return render_template('index.html', title=title)