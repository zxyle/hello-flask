#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <zxyful@gmail.com>
# Date: 2019/12/4
# Desc:

import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    LOG_TYPE = os.environ.get("LOG_TYPE", "watched")
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    LOG_DIR = "./data/logs"
    APP_LOG_NAME = "app.log"
    WWW_LOG_NAME = "www.log"

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://zheng:VJtgG2AsIOw4Yklg@mysql/spider?charset=utf8mb4"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://zheng:VJtgG2AsIOw4Yklg@mysql/spider?charset=utf8mb4"


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://zheng:VJtgG2AsIOw4Yklg@127.0.0.1:3307/spider?charset=utf8mb4"


config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': TestingConfig
}
