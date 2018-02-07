# -*- coding: utf-8 -*-
"""
    __init__.py
    ~~~~~~~~~~~~~~~~

    <NO DESCRIPTION>.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from flask import Blueprint

frontend = Blueprint('frontend', __name__, url_prefix='')

from . import views