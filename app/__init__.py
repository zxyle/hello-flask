#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc: 

from flask import Flask


def create_app():
    app = Flask(__name__)

    from .oss import oss_blue
    app.register_blueprint(oss_blue, url_prefix='/oss')

    from .auth import auth_blue
    app.register_blueprint(auth_blue)

    return app
