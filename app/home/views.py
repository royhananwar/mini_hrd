from flask import render_template

from . import home


@home.route('/')
def index():
    '''
    index page
    '''

    return render_template('home/base.html')