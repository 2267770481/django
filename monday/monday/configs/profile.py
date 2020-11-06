"""flask 相关配置"""

import os
import datetime
import time
import logging
from logging import handlers, StreamHandler
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

# 日志配置
LOG_PATH = os.getcwd() + '\\logs\\'
if os.path.exists(LOG_PATH) is False:
    os.mkdir(LOG_PATH)
LOG_DATE = time.strftime('%Y%m%d', time.localtime(time.time()))
LOG_FILE_NAME = LOG_PATH + LOG_DATE + '_log.log'
FILE_HANDLE = handlers.RotatingFileHandler(filename=LOG_FILE_NAME, maxBytes=10 * 1024 * 1024,
                                           backupCount=3, encoding='utf-8')  # 最多备份3个日志文件，每个日志文件最大10M
FILE_HANDLE.setLevel(logging.INFO)  # 输出到file的log等级的开关
FORMATTER = logging.Formatter("%(asctime)s - %(filename)s[:%(lineno)d] - %(levelname)s: %(message)s")  # 定义输出格式
FILE_HANDLE.setFormatter(FORMATTER)  # 添加格式化输出
