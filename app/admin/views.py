from flask import render_template, url_for, request, flash, jsonify

from . import admin
from .. import db
from ..models import Division, User, Employee
from .forms import DivisionForm


@admin.route('/')
def index():
    return render_template('admin/dashboard.html')

@admin.route('/divisions')
def list_divisions():
    
    divisions = Division.query.all()
    form = DivisionForm()

    return render_template(
        '/admin/division/index.html',
         divisions=divisions,
         form=form)

@admin.route('/division/create', methods=['POST'])
def create_division():

    form = DivisionForm()
    if form.validate_on_submit():
        division = Division(
            name=form.name.data,
            note=form.note.data
        )
        try:
            db.session.add(division)
            db.session.commit()
            flash('Success add new Division :)')
            return url_for('admin.list_division')
        except Exception as e:
            flash('Something error :(')
            return url_for('admin.list_division')

@admin.route('/division/<int:id>')
def detail_divisions(id):

    division = Division.query.get(id)
    division_json = {
        'id': division.id,
        'name': division.name,
        'note': division.note
    }
    return jsonify(division_json)

@admin.route('/division/edit/<int:id>')
def edit_division(id):

    division = Division.query.get(id)
    form = DivisionForm()
    if form.validate_on_submit():
        division.name = form.name.data
        division.note = form.note.data

        try:
            db.session.add(division)
            db.session.commit
            flask('Success edit division :)')
            return url_for('admin.list_division')
        except Exception as e:
            flash('Something errpr :(')
            return url_for('admin.list_division')

@admin.route('/division/delete/<int:id>', methods=['POST'])
def delete_division(id):
    
    if request.method == 'POST':
        division = Division.query.get(id)
        try:
            db.session.delete(division)
            db.session.commit()
            flash('Success delete some division')
            return url_for('admin.list_division')
        except Exception as e:
            flash('Failed delete some division')
            return url_for('admin.list_division')