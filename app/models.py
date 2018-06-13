from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager, db


class Division(db.Model):
    '''
    Model for Division
    '''

    __tablename__ = 'divisions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    note = db.Column(db.String(100), unique=True)
    employees = db.relationship('Employee', backref='division', lazy='dynamic') 

    def __repr__(self):
        return self.name


class Employee(db.Model):
    '''
    Model for Employee
    '''

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(32), index=True, unique=True)
    address = db.Column(db.String(250))
    gender = db.Column(db.String(1), index=True, unique=True)
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'))
    user = db.relationship('User', backref='employee', lazy='dynamic')

    def __repr__(self):
        return self.name


class User(UserMixin, db.Model):
    '''
    Model for User
    '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    is_admin = db.Column(db.Boolean, default=False)
    is_hrd = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.username

    @property
    def password(self):
        '''
        set password is not readable
        '''

        raise AttributeError('Password is not readable')
    
    @password.setter
    def password(self, password):
        '''
        set password to hash password
        '''

        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        '''
        check if password is match
        '''
    
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)