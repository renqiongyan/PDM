from werkzeug.security import generate_password_hash
from flask import render_template
from ..extensions import flask_db
from ..models import Senior

from . import bp_misc


@bp_misc.route('/generate_date')
def generate_date():
    flask_db.database.create_tables([Senior], safe=True)

    seniors = [
        {'username': 'pdmc01', 'password': generate_password_hash('pdmc01'),
         'nickname': 'Physical distribution management', 'gender': 'M', 'role': 'ceo'},
        {'username': 'pdmp01', 'password': generate_password_hash('pdmp01'),
         'nickname': 'Physical distribution management', 'gender': 'F', 'role': 'president'}
    ]
    Senior.insert_many(seniors).execute()
    return '高层用户数据初始化成功，开始你的创业吧！'


    # shopowners = [
    #     {'username': '2017001', 'password': generate_password_hash('2017001'), 'nickname': '张三', 'gender': 'M',
    #      'role': 'student'},
    #     {'username': '2017002', 'password': generate_password_hash('2017002'), 'nickname': '李四', 'gender': 'M',
    #      'role': 'student'},
    #     {'username': '2017003', 'password': generate_password_hash('2017003'), 'nickname': '小红', 'gender': 'M',
    #      'role': 'student'},
    #     {'username': '2017004', 'password': generate_password_hash('2017004'), 'nickname': '韩梅梅', 'gender': 'M',
    #      'role': 'student'},
    #     {'username': '101', 'password': generate_password_hash('101'), 'nickname': '张老师', 'gender': 'M',
    #      'role': 'teacher'},
    #     {'username': '102', 'password': generate_password_hash('102'), 'nickname': '王老师', 'gender': 'M',
    #      'role': 'teacher'}
    # ]
    # Shopowners.insert_many(users).execute()
    # return '初始化用户数据成功'
    #
    # workers= [
    #     {'username': '2017001', 'password': generate_password_hash('2017001'), 'nickname': '张三', 'gender': 'M',
    #      'role': 'student'},
    #     {'username': '2017002', 'password': generate_password_hash('2017002'), 'nickname': '李四', 'gender': 'M',
    #      'role': 'student'},
    #     {'username': '2017003', 'password': generate_password_hash('2017003'), 'nickname': '小红', 'gender': 'M',
    #      'role': 'student'},
    #     {'username': '2017004', 'password': generate_password_hash('2017004'), 'nickname': '韩梅梅', 'gender': 'M',
    #      'role': 'student'},
    #     {'username': '101', 'password': generate_password_hash('101'), 'nickname': '张老师', 'gender': 'M',
    #      'role': 'teacher'},
    #     {'username': '102', 'password': generate_password_hash('102'), 'nickname': '王老师', 'gender': 'M',
    #      'role': 'teacher'}
    # ]
    # Worker.insert_many(users).execute()
    # return '初始化用户数据成功'


@bp_misc.route('/base1')
def base1():
    return render_template('base1.html')
