# -*- coding: utf-8 -*-
"""
    views
    ~~~~~~~~~~~~~~~~

    <NO DESCRIPTION>.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from . import frontend
from flask import render_template
from app.models import Post, Category, Tag


def get_cat_list():
    return Category.query.order_by(Category.id).all()


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
