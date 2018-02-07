# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~~~~~~~~~~~

    configurations

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""


class Config:
    DEBUG = False
    SECRET_KEY = '8e4b6d17d7f632ba2ca16eaa1a9d9952'
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://ling:@localhost/flask_blog'
    SQLALCHEMY_ECHO = True
    BOOTSTRAP_SERVE_LOCAL = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_ECHO = False


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'pro': ProductionConfig,
    'default': DevelopmentConfig,
}
