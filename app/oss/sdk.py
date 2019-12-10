#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/7/22
# Desc: 


import os
from itertools import islice

import oss2

from app.config import ACCESS_KEY_ID, ACCESS_KEY_SECRET, ENDPOINT


class OSS:
    def __init__(self):
        self.__access_key_id = ACCESS_KEY_ID
        self.__access_key_secret = ACCESS_KEY_SECRET
        self.__endpoint = ENDPOINT
        self.__auth = oss2.Auth(self.__access_key_id, self.__access_key_secret)

    def get_bucket(self, bucket_name):
        """
        Get an authenticated bucket object
        :param bucket_name:
        :return:
        """
        if not bucket_name:
            raise ValueError("bucket not null.")

        return oss2.Bucket(self.__auth, self.__endpoint, bucket_name)

    def put(self, filename, bytes_data, bucket_name="zx-test-oss"):
        """
        upload file
        :param filename:
        :param bytes_data:
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
        List all filenames in  this bucket
        :param bucket_name:
        :return:
        """
        bucket = self.get_bucket(bucket_name)
        for b in islice(oss2.ObjectIterator(bucket), 10):
            print(b.key)

    def delete(self, obj_name, bucket_name="zx-test-oss"):
        bucket = self.get_bucket(bucket_name)
        return bucket.delete_object(obj_name)

    @staticmethod
    def _exist(pathname):
        return os.path.exists(pathname)
