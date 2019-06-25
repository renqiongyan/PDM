from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Optional, ValidationError

from application.models import User


class ShopOwnerForm(FlaskForm):
    account = StringField('账户', validators=[DataRequired('账户不能为空')])
    password = StringField('密码', validators=[DataRequired('密码不能为空')])
    name = StringField('姓名', validators=[Optional()])
    gender = StringField('性别', validators=[DataRequired()])
    role = StringField('角色', validators=[DataRequired('角色不能为空')])
    birthday = StringField('生日', validators=[DataRequired('生日不能为空')])
    phone = StringField('手机号', validators=[DataRequired('手机号不能为空')])
    workaddress = StringField('工作区域', validators=[DataRequired('工作区域不能为空')])

    def validate_name(form, field):
        user = User.get_or_none(User.name == field.data)
        if user is not None:
            raise ValidationError('用户名已经被使用')

