# -*- coding: utf-8 -*-
"""
    views
    ~~~~~~~~~~~~~~~~

    <NO DESCRIPTION>.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from . import frontend
from flask import render_template, redirect, url_for, flash
from app.models import Post, Category, Tag, Permission, User, Role
from .forms import RegisterForm
from flask_login import login_required, current_user
from app.forms import PostForm
from app.decorators import permission_required
from app import db


def get_cat_list():
    return Category.query.order_by(Category.id).all()


@frontend.route('/')
def index():
    return redirect(url_for('.post_index'))


@frontend.route('/post')
def post_index():
    posts = Post.query.order_by(-Post.id).all()
    cats = get_cat_list()
    return render_template('frontend/post/index.html', posts=posts, cats=cats)


@frontend.route('/post/<int:id>')
def post_detail(id):
    post = Post.query.get_or_404(id)
    return render_template('frontend/post/detail.html', post=post, cats=get_cat_list())


@frontend.route('/tag')
def tag_index():
    tags = Tag.query.order_by(Tag.name).all()
    return render_template('frontend/tag/index.html', tags=tags)


@frontend.route('/tag/<int:id>')
def tag_detail(id):
    tag = Tag.query.get_or_404(id)
    posts = tag.posts
    return render_template('frontend/tag/detail.html', tag=tag, posts=posts, cats=get_cat_list())

@frontend.route('/cat/<int:id>')
def cat_detail(id):
    cat = Category.query.get_or_404(id)
    posts = cat.posts
    return render_template('frontend/cat/detail.html', cat=cat, posts=posts, cats=get_cat_list())


@frontend.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        role = Role.query.filter_by(name='author').first()
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            flash('重复的用户名')
            return redirect(url_for('.register'))
        user = User()
        user.username = form.username.data
        user.password = form.password.data
        user.role = role
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('backend.login'))

    return render_template('frontend/register.html', form=form)


@frontend.route('/submission', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.SUBMISSION)
def submission():
    form = PostForm()
    form.tag(placeholder='aaa')
    if form.validate_on_submit():
        save_to_db_objs = []
        post = Post()
        post.title = form.titile.data
        post.content = form.content.data
        post.category_id = form.category.data
        post.author_id = current_user.id
        if form.tag.data:
            tags = form.tag.data.split(',')
            for t in tags:
                tag_obj = Tag.query.filter_by(name=t).first()
                if tag_obj is None:
                    tag_obj = Tag(name=t)
                post.tags.append(tag_obj)
                save_to_db_objs.append(tag_obj)
        save_to_db_objs.append(post)
        db.session.add_all(save_to_db_objs)
        db.session.commit()
        return redirect(url_for('.post_index'))

    return render_template('frontend/submission.html', form=form)
