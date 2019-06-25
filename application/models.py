from flask_login import UserMixin
from peewee import CharField
from wtforms import StringField

from .extensions import flask_db


class User(UserMixin, flask_db.Model):
    account = CharField(null=False)
    password = CharField(null=False)
    name = CharField(null=False, index=True, unique=True)
    gender = CharField(null=False, choices=(('M', '男'), ('F', '女')))
    birthday = StringField(null=False, max_length=15)
    phone = CharField(null=False, max_length=15)
    workaddress = StringField(null=False, max_length=50)
    role = StringField(null=False, choices=(('C', '总经理'), ('S', '店长'), ('W', '店员')))

    class Meta:
        database = flask_db.database


class Goods(UserMixin, flask_db.Model):
    number = CharField(null=False)
    name = CharField(null=False, index=True, unique=True)
    sender = CharField(null=False)
    receiver = CharField(null=False)
    type = StringField(null=False, choices=(('Y', '生活用品'),('S', '食品'),('D', '电子产品'), ('Q', '其他')))

    class Meta:
        database = flask_db.database


class Transport(UserMixin, flask_db.Model):
    number = CharField(null=False)
    worker = CharField(null=False)
    state = StringField(null=False, choices=(('D', '待发货'),('Y', '运输中'),('S', '已收货')))

    class Meta:
        database = flask_db.database


class Customer(UserMixin, flask_db.Model):
    sname = CharField(null=False)
    sphone = CharField(null=False, max_length=15)
    saddress = CharField(null=False, max_length=50)
    rname = CharField(null=False)
    rphone = CharField(null=False, max_length=15)
    raddress = StringField(null=False, max_length=50)

    class Meta:
        database = flask_db.database