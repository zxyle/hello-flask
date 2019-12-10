#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/29
# Desc: main app

import os

from app import create_app

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
