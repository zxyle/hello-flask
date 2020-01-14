#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc:

import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    DEBUG = True
    LOG_TYPE = os.environ.get("LOG_TYPE", "watched")
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    LOG_DIR = "./data/logs"
    APP_LOG_NAME = "app.log"
    WWW_LOG_NAME = "www.log"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://zheng:VJtgG2AsIOw4Yklg@mysql:3306/fund?charset=utf8mb4"


config = {
    'testing': TestingConfig,
    'default': TestingConfig
}
