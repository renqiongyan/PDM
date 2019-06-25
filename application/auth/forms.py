from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, ValidationError
from wtforms.validators import DataRequired, Optional, Email

from ..models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('用户名不能为空')])
    password = StringField('密码', validators=[DataRequired('密码不能为空')])


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('用户名不能为空')])
    password = StringField('密码', validators=[DataRequired('密码不能为空')])
    nickname = StringField('昵称', validators=[Optional()])
    gender = StringField('性别', validators=[DataRequired()])
    role = StringField('角色', validators=[DataRequired('角色不能为空')])

    def validate_username(form, field):
        user = User.get_or_none(User.username == field.data)
        if user is not None:
            raise ValidationError('用户名已经被使用')