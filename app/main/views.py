#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc:

import logging

from . import main_blue

logger = logging.getLogger("app.access")


@main_blue.route('/')
def index():
    logger.info('logged in successfully')
    return "Page is empty"
