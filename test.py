#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/29
# Desc: 


import requests

url = "http://127.0.0.1:5000/oss"
data = {"bucket_name": "i-pro", "img_url": "https://www.baidu.com/img/bd_logo1.png"}
resp = requests.post(url, data=data)
print(resp.text)
