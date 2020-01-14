#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2020-01-14
# Desc: 测试redis联通

import redis

host = "redis"

pool = redis.ConnectionPool(host=host)

r = redis.Redis(connection_pool=pool)
print(r.get("name"))
