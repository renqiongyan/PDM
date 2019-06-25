from flask import render_template, flash
from werkzeug.security import generate_password_hash

from application.models import User, Goods, Transport
from application.shopowner import bp_shopowner

from application.shopowner.forms import WorkerForm

#删除物流信息
@bp_transport.route('/del_trans')
def del_trans():
    trans = Trans.select().where(Transport.number == number).get()
    trans.delete_instance()
    flash('删除成功')
    return render_template('senior/del_trans.html', trans=trans)

#查看物流信息
@bp_transport.route('/list_trans')
def list_trans():
    trans = Trans.select().where(Transport.number == number).get()
    flash('查看成功')
    return render_template('senior/list_trans.html', trans=trans)

#增加物流信息
@bp_transport.route('/add_trans')
def add_trans():
    form = TransportForm()
    if form.validate_on_submit():
        Transport.create(
            number=form.number.data,
            worker=form.worker.data,
            state=form.state.data,
        )
        flash('增加成功')
    return render_template('senior/add_trans.html', trans=form)

#修改物流信息
@bp_transport.route('/edit_trans')
def edit_user():
    trans = Trans.select().where(Transport.number == number).get()
    flash('修改成功')
    return render_template('senior/edit_user.html', trans=trans)

