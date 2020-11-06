"""
    mysql 数据库连接池
    使用时只需要导入该文件最下边的 mysql 实例即可
    用例：
        from monday.public.db_util import mysql
        sql = 'select id, username from db_UserInfo where username=%(username)s'
        res = mysql.fetch_all(sql, {'username': 'abc'})
        -- 查询 db_UserInfo 表中 username 为 'abc' 的所有数据 并以 字典形式返回

        from monday.public.db_util import mysql
        sql = 'select id, username from db_UserInfo where username=%(username)s'
        res = mysql.fetch_one(sql, {'username': 'abc'}, res_dict=None)
        -- 查询 db_UserInfo 表中 username 为 'abc' 的数据 用元组的形式只返回一条

        insert update and delete 是使用事务进行操作的
"""

import pymysql
from dbutils.pooled_db import PooledDB
from ..configs.setting import MYSQL_CONFIG
from flask import current_app

class MySql:
    def __init__(self):
        self._poolDB = PooledDB(
            # 指定数据库连接驱动
            creator=pymysql,
            # 连接池允许的最大连接数,0和None表示没有限制
            maxconnections=3,
            # 初始化时,连接池至少创建的空闲连接,0表示不创建
            mincached=2,
            # 连接池中空闲的最多连接数,0和None表示没有限制
            maxcached=5,
            # 连接池中最多共享的连接数量,0和None表示全部共享(其实没什么卵用)
            maxshared=3,
            # 连接池中如果没有可用共享连接后,是否阻塞等待,True表示等等,
            # False表示不等待然后报错
            blocking=True,
            # 开始会话前执行的命令列表
            setsession=[],
            # ping Mysql服务器检查服务是否可用, 0 =无=从不，1 =默认=每当从池中获取时，2 =创建游标时，4 =查询时被执行，7 =总是
            ping=0,
            **MYSQL_CONFIG
        )

    def _get_one_connect(self, res_dict):
        self._conn = self._poolDB.connection()
        self._cursor = self._conn.cursor(cursor=res_dict)

    def _close(self):
        self._cursor.close()
        self._conn.close()

    def fetch_one(self, sql, args=None, res_dict=pymysql.cursors.DictCursor):
        """
        返回第一条结果
        :param sql: 查询命令
        :param args: 查询参数
        :param res_dict: 返回结果类型 -默认是字典 -传None 返回元组
        :return:
        """
        self._get_one_connect(res_dict)
        self._cursor.execute(sql, args)
        # 随便取一条查询结果
        result = self._cursor.fetchone()
        self._close()
        return result

    def fetch_all(self, sql, args=None, res_dict=pymysql.cursors.DictCursor):
        """
        返回所有结果
        :param sql: 查询命令
        :param args: 查询参数
        :param res_dict: 返回结果类型 -默认是字典 -传None 返回元组
        :return:
        """
        self._get_one_connect(res_dict)
        self._cursor.execute(sql, args)
        # 随便取一条查询结果
        result = self._cursor.fetchall()
        self._close()
        return result

    def _transaction(self, sql, args):
        """事务处理"""
        self._get_one_connect(None)
        self._conn.begin()  # 开启事务
        try:
            self._cursor.execute(sql, args)
            self._conn.commit()  # 提交事务
        except Exception as e:
            self._conn.rollback()  # 事务回滚
            current_app.logger.error(f"""数据库执行失败:[sql: {sql}] {e}""")
            raise e

    def insert(self, sql, args=None):
        self._transaction(sql, args)

    def update(self, sql, args=None):
        self._transaction(sql, args)

    def delete(self, sql, args=None):
        self._transaction(sql, args)


# 实例，使用的时候引入该实例就行
mysql = MySql()
