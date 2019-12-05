#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc: 

from flask import request
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from . import auth_blue
from ..models import User


@auth_blue.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if not user:
        return "未注册"
    password_hash = user.password
    password = request.form.get("password")
    status = check_password_hash(password_hash, password)

    return "Login {}".format(status)


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
    password_hash = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
    user = User(username=username, password=password_hash)
    db.session.add(user)
    db.session.commit()
    return "Welcome {}!".format(username)


@auth_blue.route('/change-password', methods=['GET', 'POST'])
def change_password():
    username = request.form.get("username")
    old_password = request.form.get("old_password")
    new_password = request.form.get("new_password")
    user = User.query.filter_by(username=username).first()
    if not user:
        return "未注册"
    password_hash = user.password
    status = check_password_hash(password_hash, old_password)
    if not status:
        return "旧密码错误"

    password_hash = generate_password_hash(new_password, method="pbkdf2:sha256", salt_length=8)
    user.password = password_hash
    db.session.add(user)
    db.session.commit()

    return "change password success."
