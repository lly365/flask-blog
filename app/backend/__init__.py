# -*- coding: utf-8 -*-
"""
    __init__.py
    ~~~~~~~~~~~~~~~~

    Backend bluepoint.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from flask import Blueprint
from app.models import Permission

backend = Blueprint('backend', __name__, url_prefix='/admin')

from . import views


@backend.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
