#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zhengxiang@upg.cn>
"""gunicorn 配置文件"""
# 使用以下命令执行
# gunicorn -c gunicorn.conf.py main:app
# 详细配置参数请参考以下url
# http://docs.gunicorn.org/en/latest/settings.html

import multiprocessing

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1

# Daemonize the Gunicorn process.
daemon = False

# restart workers when code changes.
reload = True

# process id
pidfile = "/tmp/spider_server.pid"

# logfile
errorlog = "/tmp/spider_server.log"

# the Access log file to write to.
accesslog = "/tmp/spider_server.log"
