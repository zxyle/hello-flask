#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/22
# Desc: 


import os
from itertools import islice

import oss2

from app.config import access_key_id, access_key_secret, endpoint


class OSS:
    def __init__(self):
        self.__access_key_id = access_key_id
        self.__access_key_secret = access_key_secret
        self.__endpoint = endpoint
        self.__auth = oss2.Auth(self.__access_key_id, self.__access_key_secret)

    def get_bucket(self, bucket_name):
        """
        得到一个bucket对象
        :param bucket_name:
        :return:
        """
        if not bucket_name:
            raise ValueError("bucket not null.")

        return oss2.Bucket(self.__auth, self.__endpoint, bucket_name)

    def put(self, filename, bytes_data, bucket_name="zx-test-oss"):
        """
        upload file
        :param filename: 文件名
        :param bytes_data: 二进制文件
        :param bucket_name:
        :return:
        """
        bucket = self.get_bucket(bucket_name)
        result = bucket.put_object(filename, bytes_data)
        return result.status

    def download(self, obj_name, bucket_name="zx-test-oss"):
        """
        download file
        :return:
        """
        bucket = self.get_bucket(bucket_name)
        bucket.get_object_to_file(obj_name, './' + obj_name)

    def list_objects(self, bucket_name="zx-test-oss"):
        """
        列出bucket所有文件名
        :param bucket_name:
        :return:
        """
        bucket = self.get_bucket(bucket_name)
        for b in islice(oss2.ObjectIterator(bucket), 10):
            print(b.key)

    def delete(self, obj_name, bucket_name="zx-test-oss"):
        bucket = self.get_bucket(bucket_name)
        result = bucket.delete_object(obj_name)
        print(result.delete_marker)
        print(result.headers)
        print(result.request_id)
        print(result.resp)
        print(result.status)
        print(result.versionid)

    @staticmethod
    def _exist(pathname):
        return os.path.exists(pathname)


if __name__ == '__main__':
    o = OSS()
    print(o.put("bd_logo1.png", open("./bd_logo1.png", 'rb'), "zx-hotel"))
