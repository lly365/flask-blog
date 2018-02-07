# -*- coding: utf-8 -*-
"""
    views
    ~~~~~~~~~~~~~~~~

    Backend views.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from . import backend
from .forms import LoginForm
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user
from app.models import User
from app.decorators import admin_required


@backend.route('/login', methods=['GET', 'POST'])
def login():  # TODO：提取到单独的BP
    form = LoginForm()
    next_url = request.args.get('next')
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            if not next_url:
                next_url = url_for('backend.index')
            return redirect(next_url)
        flash('用户名或密码错误。')

    return render_template('backend/login.html', form=form)


@backend.route('/logout')
@login_required
def logout():  # TODO：提取到单独的BP
    logout_user()
    return redirect(url_for('.index'))


@backend.route('/')
@login_required
@admin_required
def index():
    return 'admin index'


@backend.route('/post/add')
@login_required
def post_add():
    pass
