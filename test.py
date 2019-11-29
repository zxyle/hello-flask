#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/11/29
# Desc: 


import requests

url = "http://127.0.0.1:5000/upload"
files = {'file': open("./heigui.jpg", 'rb')}
resp = requests.post(url, files=files, data={"bucket_name": "zx-hotel"})
print(resp.text)
