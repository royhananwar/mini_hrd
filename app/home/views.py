from flask import render_template
from flask_login import login_required

from . import home


@home.route('/')
@login_required
def index():
    '''
    index page
    '''

    return render_template('home/base.html')