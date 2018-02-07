# -*- coding: utf-8 -*-
"""
    __init__.py
    ~~~~~~~~~~~~~~~~

    create app.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    db.init_app(app)

    return app
