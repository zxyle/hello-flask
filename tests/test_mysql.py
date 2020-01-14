#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2020-01-14
# Desc: 测试mysql 联通性

from mysql.connector import Error, MySQLConnection

PROD_DB_CONFIG = {
    "user": "zheng",
    "password": "VJtgG2AsIOw4Yklg",
    "host": "mysql",
    "port": 3306,
    "database": "spider",
    # 'charset': 'utf8',
    # 创建buffered游标
    'buffered': True,
    'connect_timeout': 2,
}


def connect_db():
    query = "SELECT * FROM name;"
    try:
        conn = MySQLConnection(**PROD_DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(query, )
        result = cursor.fetchall()
        print(result)
    except Error as e:
        return False
    else:
        return True


if __name__ == '__main__':
    print(connect_db())
