#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc:

from sqlalchemy.sql import func

from . import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='comment')
    create_time = db.Column(db.TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    modify_time = db.Column(db.TIMESTAMP, server_default=func.current_timestamp(), nullable=False)


class User(BaseModel):
    __tablename__ = 'user'

    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
