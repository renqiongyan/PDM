from flask import render_template
from flask_login import login_required

from ..utilities import role_required

from . import bp_welcome


@bp_welcome.route('/welcome')
@login_required
def welcome():
    return render_template('welcome/welcome.html')


@bp_welcome.route('/teacher')
@login_required
@role_required('teacher')
def teacher():
    return render_template('welcome/teacher.html')


@bp_welcome.route('/student')
@login_required
@role_required('student')
def student():
    return render_template('welcome/student.html')


