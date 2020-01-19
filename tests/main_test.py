#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/5
# Desc: 
import main


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/ping')
    assert r.status_code == 200
