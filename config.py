from logging.handlers import RotatingFileHandler
import redis
import logging


class Config(object):
    """工程配置信息"""
    DEBUG = True
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis的配置信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # 配置密钥
    SECRET_KEY = "itheima"
    # flask_session 的配置信息
    SESSION_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400    # session 的有效期，单位是秒


class DevelopementConfig(Config):
    """开发模式下配置"""
    DEBUG = True
    # 设置默认的日志等级
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """生产模式下的配置"""
    pass
    LOG_LEVEL = logging.WARN


def setup_log(config_name):
    """配置日志"""
    # 设置日志的记录等级
    logging.basicConfig(level=config_name.LOG_LEVEL)   # 调试debug级
    # 创建日志记录器，指明日志保存的路径，每个日志文件最大大小，保存的日志文件数上线
    file_log_hanlder = RotatingFileHandler('logs/log', maxBytes=1024*1024*100, backupCount=10)
    # 创建日志的记录格式， 日志等级， 输入日志信息的文件名，行数， 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚闯进啊的日志记录器设置日志记录格式
    file_log_hanlder.setFormatter(formatter)
    # 为全局的日志工具对象(flask app使用的) 添加日志记录器
    logging.getLogger().addFilter(file_log_hanlder)
