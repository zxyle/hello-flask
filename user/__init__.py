#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/2
# Desc: 

from flask import Blueprint

user_blue = Blueprint('user', __name__)

from user import hh
