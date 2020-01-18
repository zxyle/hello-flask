#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc:

import logging
import socket

from redis import Redis

from . import main_blue

redis = Redis(host="redis")

logger = logging.getLogger("app.access")


@main_blue.route('/')
def index():
    logger.info('logged in successfully')
    return "Page is empty"


@main_blue.route('/ping')
def ping():
    return "pong"


@main_blue.route('/redis')
def hello():
    redis.incr('hits')
    return 'Hello Container World! I have been seen %s times and my hostname is %s.\n' % (
        redis.get('hits'), socket.gethostname())
