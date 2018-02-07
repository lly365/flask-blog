# -*- coding: utf-8 -*-
"""
    forms
    ~~~~~~~~~~~~~~~~

    <NO DESCRIPTION>.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    re_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password', message='两次输入的密码不一致')])
    submit = SubmitField('注册')
