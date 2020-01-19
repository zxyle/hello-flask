#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc:

import logging
import os
import socket

from flask import request, render_template, jsonify
from redis import Redis

from . import main_blue

redis = Redis(host="redis")

logger = logging.getLogger("app.access")

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', "xlsx", "xls", "log"}


@main_blue.route('/')
def index():
    return "It worked!"


@main_blue.route('/ping')
def ping():
    return "pong"


@main_blue.route('/redis')
def hello():
    redis.incr('hits')
    return 'Hello Container World! I have been seen %s times and my hostname is %s.\n' % (
        redis.get('hits'), socket.gethostname())


@main_blue.route('/get_version')
def get_version():
    latest_version = 1
    return jsonify({"version": latest_version})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main_blue.route('/upload', methods=['POST'])
def transfer():
    if request.method != 'POST':
        return render_template("transfer.html")

    if 'file' not in request.files:
        return {"msg": "No file part."}

    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return {"msg": "No selected file."}

    if file and allowed_file(file.filename):
        print(file.filename)
        # filename = secure_filename(file.filename)
        filename = file.filename
        file.save(os.path.join("/uploads", os.path.join(".", filename)))

        return {"status": 1}

    return {"msg": "file error."}
