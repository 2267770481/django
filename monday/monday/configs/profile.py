import os
import datetime
from redis import Redis

DEBUG = True

# 数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/test'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# session 配置
SESSION_TYPE = 'redis'
SESSION_REDIS = Redis(host='localhost', password=12345)
SECRET_KEY = os.urandom(16)
PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=10)  # 设置session过期时间为10分钟
