from flask import render_template, flash

from application.models import Shopowners
from application.senior import bp_senior


@bp_senior.route('/list_senior')
def list_users():
    seniors = Shopowners.select()
    flash('查看成功')
    return render_template('senior/list_senior.html', seniors = seniors )

#
# @bp_user.route('/add_user',methods=['GET', 'POST'])
# def add_user():
#     form = AddForm()
#     if form.validate_on_submit():
#         User.create(
#             username=form.username.data,
#             password = generate_password_hash(form.password.data),
#             nickname = form.nickname.data,
#             gender = form.gender.data,
#             role = form.role.data,
#         )
#         flash('增加成功')
#         return redirect(url_for('bp_user.list_users'))
#
#     return render_template('user/add_user.html', form=form)
