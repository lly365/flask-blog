# -*- coding: utf-8 -*-
"""
    manage
    ~~~~~~~~~~~~~~~~

    bootstrap manager.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from app import create_app, db
from flask_script import Server, Shell, Manager
from flask_migrate import MigrateCommand, Migrate
from os import getenv
from app.models import Category, Post, Tag

app = create_app(getenv('FLASK_BLOG_ENV', 'default'))

migrate = Migrate(app, db)

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Category=Category, Post=Post, Tag=Tag)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host=app.config.get('HOST', '127.0.0.1'), port=app.config.get('PORT', 5000)))
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
