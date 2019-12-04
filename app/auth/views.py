#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc: 

from flask import request

from app import db
from . import auth_blue
from ..models import User


@auth_blue.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    return "{}-{}".format(username, password)


@auth_blue.route('/logout', methods=['GET', 'POST'])
def logout():
    pass


@auth_blue.route('/register', methods=['GET', 'POST'])
def register():
    content_type = request.content_type
    form = None
    if "json" in content_type:
        form = request.get_json()
    elif "x-www-form-urlencoded" in content_type:
        form = request.form
    elif "form-data" in content_type:
        form = request.form

    username = form.get("username")
    password = form.get("password")
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return "Welcome {}!".format(username)


@auth_blue.route('/change-password', methods=['GET', 'POST'])
def change_password():
    pass
