#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/3
# Desc: 


from flask import Blueprint

oss_blue = Blueprint('oss', __name__)


from . import views, errors


