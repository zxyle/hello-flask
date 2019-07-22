#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@BoardCAM.org>
# Date: 2019/7/22
# Desc: 


import os
from itertools import islice

import oss2

from config import access_key_id, access_key_secret, bucket_name, endpoint


class OSS:
    def __init__(self):
        self.__access_key_id = access_key_id
        self.__access_key_secret = access_key_secret
        self.__endpoint = endpoint
        self.__bucket_name = bucket_name
        self.__auth = oss2.Auth(self.__access_key_id, self.__access_key_secret)
        self.__bucket = oss2.Bucket(self.__auth, self.__endpoint,
                                    self.__bucket_name)

    def put(self, abspath):
        """
        upload file
        :param abspath:
        :return:
        """
        if not self._exist(abspath):
            raise FileNotFoundError
        dirname = os.path.dirname(abspath)
        print(dirname)

        filename = os.path.basename(abspath)

        result = self.__bucket.put_object_from_file(filename, abspath)
        return result.status

    def download(self, obj_name):
        """
        download file
        :return:
        """
        self.__bucket.get_object_to_file(obj_name, 'D:/a.jpg')

    def list_bucket(self):
        for b in islice(oss2.ObjectIterator(self.__bucket), 10):
            print(b.key)

    def delete(self, obj_name):
        result = self.__bucket.delete_object(obj_name)
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
    print(o.put(r"./README.md"))
    # o.download("a.jpg")
    # print(o.delete("BugCode_taskkill_1_1_2_8.exe"))
    # o.delete("D:\Projects\BoardCAM\README.md")
