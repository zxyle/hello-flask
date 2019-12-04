#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc: 


from . import oss_blue


@oss_blue.app_errorhandler(404)
def page_not_found(e):
    return "404"
    # return render_template()


@oss_blue.app_errorhandler(500)
def internal_server_error(e):
    return "505"
