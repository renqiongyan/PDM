from flask_login import UserMixin
from peewee import CharField

from .extensions import flask_db


class Senior(UserMixin, flask_db.Model):
    username = CharField(null=False, index=True, unique=True)
    nickname = CharField(null=False)
    password = CharField(null=False)
    gender = CharField(null=False, choices=(('M', '男'), ('F', '女')))
    address = CharField(null=True, max_length=500)
    mail = CharField(null=True, max_length=100)
    role = CharField(null=False, choices=(('ceo', '总裁'), ('president', '总经理')))

    class Meta:
        database = flask_db.database

#
# class Shopowner(UserMixin, flask_db.Model):
#     username = CharField(null=False, index=True, unique=True)
#     nickname = CharField(null=False)
#     password = CharField(null=False)
#     gender = CharField(null=False, choices=(('M', '男'), ('F', '女')))
#     address = CharField(null=True, max_length=500)
#     mail = CharField(null=True, max_length=100)
#     role = CharField(null=False, choices=(('shopowner1', '店长1'), ('shopowner2', '店长2'),('shopowner3', '店长3')))
#
#     class Meta:
#         database = flask_db.database