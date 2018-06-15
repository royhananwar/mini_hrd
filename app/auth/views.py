from flask import render_template, abort, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, login_required

from . import auth
from .forms import RegisterForm, LoginForm
from .. import db
from ..models import Employee, User


@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if form.validate_email(form.email) or form.validate_username(form.username):
            flash('Sorry, username or email has already taken', category='warning')
            return render_template('auth/register.html', form=form, title='Register')
        else:
            employee = Employee(
                name=form.name.data,
                email=form.email.data,
                address=form.address.data,
                gender=form.gender.data,
                division_id=1
            )
            db.session.add(employee)
            db.session.commit()

            employee = Employee.query.filter_by(email=form.email.data).first()

            user = User(
                username=form.username.data,
                password=form.password_hash.data,
                employee_id=employee.id
            )
            db.session.add(user)
            db.session.commit()

            flash('Success create an account, please login')
            return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['POST', 'GET'])
def login():
    '''
    login function
    '''

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        password_hash = user.verify_password(form.password.data)

        if user:
            if password_hash:
                login_user(user)
                return redirect(url_for('home.index'))
            else:
                flash('Invalid password')
        else:
            flash('Username is not exists, you can register')
    
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    '''
    Handle for user logout
    '''

    logout_user()
    flash('You have successfuly been logged out.')

    return redirect(url_for('auth.login'))