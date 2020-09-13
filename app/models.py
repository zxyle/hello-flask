#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc:

from sqlalchemy.sql import func

from . import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='pk')
    create_time = db.Column(db.DATETIME, server_default=func.current_timestamp(), nullable=False)
    update_time = db.Column(db.DATETIME, server_default=func.current_timestamp(), nullable=False)
