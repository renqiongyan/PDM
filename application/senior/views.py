from flask import render_template, flash
from werkzeug.security import generate_password_hash
from application.models import User, Transport, Goods
from application.senior import bp_senior
from .forms import ShopOwnerForm


#查看店长或店员信息
@bp_senior.route('/list_users')
def list_users():
    users = User.select().where(User.role == 'work' or User.role == 'shopowner')
    return render_template('senior/list_users.html', users=users )


#查看（该店长或店员）详细信息
@bp_senior.route('/user_info/<int:id>')
def user_info(id):
    user = User.select().where(User.id == id)
    return render_template('senior/user_info.html', users=user)


#删除店长信息
@bp_senior.route('/del_user')
def del_user():
    user = User.select().where(User.id == id).get()
    user.delete_instance()
    flash('删除成功')
    return render_template('senior/del_user.html', user=user)


#增加店长信息
@bp_senior.route('/add_user')
def add_user():
    form = ShopOwnerForm()
    if form.validate_on_submit():
        User.create(
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
    return render_template('senior/add_user.html', user = form )


#修改店长信息
@bp_senior.route('/edit_user')
def edit_user():
    form = ShopOwnerForm()
    if form.validate_on_submit():
        User.create(
            account=form.account.data,
            password=generate_password_hash(form.password.data),
            name=form.name.data,
            gender=form.gender.data,
            birthday = form.birthday.data,
            phone = form.phone.data,
            workaddress = form.workaddress.data,
            role = form.role.data,
        )
        flash('修改成功')
    return render_template('senior/edit_user.html', user = form )


#查看商品信息
@bp_senior.route('/list_goods')
def list_goods():
    goods = Goods.select()
    return render_template('senior/list_goods.html', goods=goods )


#查看该商品物流详细详细信息
@bp_senior.route('/list_trans/<int:id>')
def list_trans(id):
    trans = Transport.select().where(Transport.id == id)
    return render_template('senior/list_trans.html', trans=trans)

