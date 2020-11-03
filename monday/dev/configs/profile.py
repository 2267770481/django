import os
import datetime

DEBUG = True

# 数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/test'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.urandom(16)
PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=10)  # 设置session过期时间为10分钟
