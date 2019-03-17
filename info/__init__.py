from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from config import Config
import redis


# 数据库
db = SQLAlchemy()
redis_store = None


# 通过传入的不同的配置名字，初始化其对应的应用实例
def create_app(config_name):
    # 创建app
    app = Flask(__name__)
    app.config.from_object(config_name)

    # 配置数据库
    db.init_app(app)
    # 配置Redis
    global redis_store
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    # 设置session 保存的位置
    Session(app)
    return app



