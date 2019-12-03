#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/29
# Desc: 主程序

from flask import Flask

from oss import oss_blue

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(oss_blue, url_prefix='/oss')

if __name__ == '__main__':
    app.run()
