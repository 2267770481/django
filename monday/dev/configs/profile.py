import os

DEBUG = True

# 数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/test'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.urandom(16)
