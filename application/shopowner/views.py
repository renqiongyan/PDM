from flask import render_template, flash
from werkzeug.security import generate_password_hash

from application.models import User, Goods, Transport
from application.shopowner import bp_shopowner

from application.shopowner.forms import WorkerForm

#删除员工信息
@bp_shopowner.route('/del_user/<int:id>')
def del_user(id):
    user = User.select().where(User.id == id).get()
    user.delete_instance()
    flash('删除成功')
    return render_template('worker/del_user.html', user=user)

#查看员工信息
@bp_shopowner.route('/list_users')
def list_users():
    users = User.select().where(User.role == 'worker' )
    flash('查看成功')
    return render_template('shopowner/list_users.html', users=users )

#增加员工信息
@bp_shopowner.route('/add_user')
def add_user():
    form = WorkerForm()
    if form.validate_on_submit():
        User.create(
            number=form.number.data,
            account=form.account.data,
            password=generate_password_hash(form.password.data),
            name=form.name.data,
            gender=form.gender.data,
            birthday=form.birthday.data,
            phone=form.phone.data,
            workaddress=form.workaddress.data,
            role=form.role.data,
        )
        flash('增加成功')
    return render_template('worker/add_user.html', user=form)

#修改员工信息
@bp_shopowner.route('/edit_user')
def edit_user():
    user = User.select()
    flash('修改成功')
    return render_template('worker/edit_user.html', user=user)

#查看商品信息
@bp_shopowner.route('/list_goods')
def list_goods():
    goods = Goods.select()
    return render_template('senior/list_goods.html', goods=goods)

#查看商品物流信息
@bp_shopowner.route('/list_trans/<int:number>')
def list_trans(number):
    trans = Transport.select().where(Transport.number == number)
    return render_template('senior/list_trans.html', trans=trans)
