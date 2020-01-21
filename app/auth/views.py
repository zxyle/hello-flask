#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc: User authentication view functions

from flask import request
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from . import auth_blue
from ..models import User


@auth_blue.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if not user:
        return {"msg": "unregistered."}
    hashed_password = user.password
    raw_password = request.form.get("password")

    if not check_password_hash(hashed_password, raw_password):
        return {"msg": "Incorrect username or password."}

    return {"msg": f"Welcome back {username}!"}


@auth_blue.route('/logout', methods=['GET'])
def logout():
    pass


@auth_blue.route('/register', methods=['POST'])
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
    user = User.query.filter_by(username=username).first()
    if user:
        return {"msg": "Account name already exists."}

    raw_password = form.get("password")
    hashed_password = generate_password_hash(raw_password, method="pbkdf2:sha256", salt_length=8)
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return {"msg": f"Welcome {username}!"}


@auth_blue.route('/change-password', methods=['POST'])
def change_password():
    username = request.form.get("username")
    old_password = request.form.get("old_password")
    new_password = request.form.get("new_password")
    user = User.query.filter_by(username=username).first()
    if not user:
        return {"msg": "unregistered."}
    hashed_password = user.password
    is_right = check_password_hash(hashed_password, old_password)
    if not is_right:
        return {"msg": "Old password is wrong."}

    new_hashed_password = generate_password_hash(new_password, method="pbkdf2:sha256", salt_length=8)
    user.password = new_hashed_password
    db.session.add(user)
    db.session.commit()

    return {"msg": "change password success."}


@auth_blue.route('/delete', methods=['POST'])
def del_user():
    return "not support."
