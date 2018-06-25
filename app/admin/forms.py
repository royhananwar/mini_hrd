from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, 
    SubmitField, SelectField,
    ValidationError
)
from wtforms.validators import DataRequired, Email

from ..models import Division, Employee, User


class DivisionForm(FlaskForm):

    name = StringField('Division Name', validators=[DataRequired])
    note = StringField('Division Note', validators=[DataRequired])