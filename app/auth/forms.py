from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, 
    SubmitField, RadioField,
    ValidationError, SubmitField
)
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User, Employee


class RegisterForm(FlaskForm):
    '''
    Creating Employee, User
    '''

    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    gender = RadioField('Gender', validators=[DataRequired()], coerce=str, choices=[
        ('M', 'Male'),
        ('F', 'Female')
    ])

    username = StringField('Username', validators=[DataRequired()])
    password_hash = PasswordField('Password')
    password_confirm = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password_hash')
    ])
    submit = SubmitField('Register')


    def validate_email(self, field):
        employee = Employee.query.filter_by(email=field.data).first()
        if employee:
            return ValidationError('Email already in use')
    
    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            return ValidationError('Username already in use')


class LoginForm(FlaskForm):
    '''
    Form for handling Login
    '''

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
