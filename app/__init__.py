#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc:

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config
from app.flask_logs import LogSetup

logs = LogSetup()

db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    logs.init_app(app)

    from .oss import oss_blue
    app.register_blueprint(oss_blue, url_prefix='/oss')

    from .auth import auth_blue
    app.register_blueprint(auth_blue)

    from .main import main_blue
    app.register_blueprint(main_blue)

    return app
