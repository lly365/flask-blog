# -*- coding: utf-8 -*-
"""
    test_basic
    ~~~~~~~~~~~~~~~~

     Basic tests.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

import unittest
from app import create_app, db
from flask import current_app


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_is_testing_env(self):
        self.assertTrue(self.app.config['TESTING'])
