# -*- coding: utf-8 -*-
"""
    models
    ~~~~~~~~~~~~~~~~

    Model classes.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from app import db

post_tag = db.Table('post_tag',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), nullable=False, primary_key=True),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), nullable=False,
                              primary_key=True))


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False, unique=True, index=True, comment='类别名称')
    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def __repr__(self):
        return "<Category@{} '{}'>".format(self.id, self.name)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    tags = db.relationship('Tag', secondary=post_tag, backref=db.backref('posts', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<Post@%d "%s">' % (self.id, self.title)


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False, unique=True, index=True, comment='标签名称')

    def __repr__(self):
        return "<Tag@{} '{}'>".format(self.id, self.name)
