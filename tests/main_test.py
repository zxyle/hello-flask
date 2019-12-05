#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/5
# Desc: 
import main


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    filename = r"D:\demo.png"
    r = client.post('/oss/transfer', data={"bucket_name": "zx-hotel", 'file': open(filename, 'rb')})
    print(r.get_json())
    assert r.status_code == 200
