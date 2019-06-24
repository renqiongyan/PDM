from flask import render_template, flash

from application.models import Shopowners
from application.senior import bp_senior


@bp_senior.route('/list_senior')
def list_users():
    seniors = Shopowners.select()
    flash('查看成功')
    return render_template('senior/list_senior.html', seniors = seniors )
