from werkzeug.security import generate_password_hash
from flask import render_template

from application.misc import bp_misc
from application.models import Shopowners
from ..extensions import flask_db



@bp_misc.route('/generate_date')
def generate_date():
    flask_db.database.create_tables([Shopowners], safe=True)

    seniors = [
        {'username': 'pdmc01', 'password': generate_password_hash('pdmc01'),
         'nickname': 'Physical distribution management', 'gender': 'M', 'role': 'ceo'},
        {'username': 'pdmp01', 'password': generate_password_hash('pdmp01'),
         'nickname': 'Physical distribution management', 'gender': 'F', 'role': 'president'}
    ]
    Senior.insert_many(seniors).execute()
    return '高层用户数据初始化成功，开始你的创业吧！'


@bp_misc.route('/base1')
def base1():
    return render_template('base1.html')
