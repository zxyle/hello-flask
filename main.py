#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/29
# Desc: 主程序

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
