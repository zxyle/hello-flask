#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019/7/22
# Desc: 


import os

import requests


def download(url):
    filename = os.path.basename(url)
    path = os.path.join("temp", filename)
    resp = requests.get(url)

    with open(path, "wb") as f:
        f.write(resp.content)

    return path, filename


if __name__ == '__main__':
    download("https://www.baidu.com/img/bd_logo1.png")
