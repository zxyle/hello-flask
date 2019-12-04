#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc: 

from flask import request

from . import auth_blue


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
    pass


@auth_blue.route('/change-password', methods=['GET', 'POST'])
def change_password():
    pass
