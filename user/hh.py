#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/2
# Desc: 


from user import user_blue


@user_blue.route('/viewmodel')
def viewmodel():
    return 'viewmodel'
