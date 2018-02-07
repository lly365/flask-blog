# -*- coding: utf-8 -*-
"""
    __init__.py
    ~~~~~~~~~~~~~~~~

    create app.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)

    from app.frontend import frontend as frontend_bp
    app.register_blueprint(frontend_bp)

    return app
