# -*- coding: utf-8 -*-
"""
    errors
    ~~~~~~~~~~~~~~~~

    <NO DESCRIPTION>.

    :copyright: (c) 2018 by WRDLL <4ever@wrdll.com>
"""

from .frontend import frontend


@frontend.app_errorhandler(404)
def error_404(e):
    return '404错误', 404


@frontend.app_errorhandler(403)
def error_403(e):
    return '你没有权限', 403
