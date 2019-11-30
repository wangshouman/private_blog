import logging

import redis


class Config(object):

    """工程配置信息"""
    SECRENT_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    DEBUG = True
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:J$qK4E92QoCT@101.132.98.181:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis 配置
    REDIS_HOST = "101.132.98.181"
    REDIS_PORT = "6379"
    REDIS_PWD = 'redis'
    # flask_seesion 的配置信息
    SESSION_TYPE = "redis"
    # SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PWD)
    PERMANWENT_SESSION_LIFETIME = 86400


class DevelopementConfig(Config):
    """开发模式的配置"""
    DEBUG = True
    # 默认日志等级
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """生产模式下的配置"""
    LOG_LEVEL = logging.WARN
    pass