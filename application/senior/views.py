from flask import render_template, flash
from flask_login import login_required, logout_user
from werkzeug.security import generate_password_hash

from application.auth import bp_auth
from application.models import User
from application.senior import bp_senior

from .forms import AddShopOwnerForm


@bp_senior.route('/list_shopowners')
def list_seniors():
    user = User.select()
    flash('查看成功')
    return render_template('senior/list_seniors.html', user = user )


@bp_senior.route('/add_shopowner')
def add_shopowner():
    form = AddShopOwnerForm()
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            password=generate_password_hash(form.password.data),
            nickname=form.nickname.data,
            gender=form.gender.data,
            role=form.role.data,
        )
        flash('增加店长成功')
    return render_template('senior/list_seniors.html', user = form )


@bp_senior.route('/del_shopowner')
def del_shopowner():
    return 'xxxx'

#-----------------


@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    return '成功退出系统'