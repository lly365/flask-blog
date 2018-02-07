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
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'backend.login'
login_manager.login_message = '请登录'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    from app.frontend import frontend as frontend_bp
    from app.backend import backend as backend_bp
    from app.errors import error_403, error_404
    app.register_blueprint(frontend_bp)
    app.register_blueprint(backend_bp)

    return app
