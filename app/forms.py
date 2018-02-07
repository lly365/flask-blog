# -*- coding: utf-8 -*-
"""
    forms
    ~~~~~~~~~~~~~~~~

    <NO DESCRIPTION>.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired
from app.models import Category, Tag


class PostForm(FlaskForm):
    titile = StringField('标题', validators=[DataRequired()])
    category = SelectField('分类', validators=[DataRequired()], coerce=int)
    content = TextAreaField('内容', validators=[DataRequired()])
    #tags = SelectMultipleField('标签', validators=[DataRequired()])
    tag = StringField('标签')
    submit = SubmitField('发布')

    def __init__(self):
        super(PostForm, self).__init__()
        self.category.choices = [(c.id, c.name) for c in Category.query.all()]
        #self.tags.choices = [(t.id, t.name) for t in Tag.query.all()]
