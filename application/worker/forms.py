from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Optional, ValidationError

from application.models import User, Transport


class TransportForm(FlaskForm):
    number = StringField('商品物流编号', validators=[DataRequired('编号不能为空')])
    worker = StringField('员工账户', validators=[DataRequired('账号不能为空')])
    state = StringField('物流状态', validators=[DataRequired('物流状态不能为空')])

    def validate_name(form, field):
        trans = Transport.get_or_none(Transport.name == field.data)
        if trans is not None:
            raise ValidationError('商品物流编号已经被使用')
