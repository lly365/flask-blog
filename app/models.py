# -*- coding: utf-8 -*-
"""
    models
    ~~~~~~~~~~~~~~~~

    Model classes.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager
from flask_login import UserMixin, AnonymousUserMixin

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
    dateline = db.Column(db.DateTime(timezone=True), default=db.func.now())
    tags = db.relationship('Tag', secondary=post_tag, backref=db.backref('posts', lazy='dynamic'), lazy='dynamic')
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post@%d "%s">' % (self.id, self.title)


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False, unique=True, index=True, comment='标签名称')

    def __repr__(self):
        return "<Tag@{} '{}'>".format(self.id, self.name)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False, unique=True, index=True)
    password_hash = db.Column('password', db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):
        return '<User@{} "{}">'.format(self.id, self.username)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMIN)


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True)
    permissions = db.Column(db.Integer, default=0)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'user': Permission.FRONTEND_BROWSER,
            'author': (Permission.FRONTEND_BROWSER | Permission.SUBMISSION),
            'admin': (Permission.FRONTEND_BROWSER | Permission.SUBMISSION | Permission.ADMIN)
        }

        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r]
            db.session.add(role)
        db.session.commit()


class Permission:
    FRONTEND_BROWSER = 1
    SUBMISSION = 2
    ADMIN = 4
