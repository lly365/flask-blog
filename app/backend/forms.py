# -*- coding: utf-8 -*-
"""
    forms
    ~~~~~~~~~~~~~~~~

    Backend forms.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')
