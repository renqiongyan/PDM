from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('用户名不能为空')])
    password = StringField('密码', validators=[DataRequired('密码不能为空')])
