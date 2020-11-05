def seat(bucket: list) -> int:
    """
        Check the bucket and return the max distance position
    :param bucket: this is a list. Integer number 1 means someone and 0 means nobody.
    :return:  Maximum distance position
        example:
            bucket = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
            res = seat(bucket)

            the res is 8.
    """
    slot = {'length': -1, 'bit': -1}
    length = 0
    bit = -1
    counter = 0
    for item in bucket:
        if item:
            if bit != 0:
                length //= 2
                bit += length
            if length > slot['length'] and bit != -1:
                slot['length'] = length
                slot['bit'] = bit
            bit = -1
        else:
            if bit == -1:
                bit = counter
                length = 0
            else:
                length += 1

        counter += 1

    if length > slot['length']:
        slot['length'] = length
        slot['bit'] = counter - 1

    return slot['bit']


class A:
    c = 8

    def __init__(self, a=None, b=None):
        self._a = a
        self.b = b


class B(A):
    pass


class Singleton(type):
    inst = {}

    def __call__(cls, *args, **kwargs):
        if cls.inst.get('cls', None) is None:
            cls.inst['cls'] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.inst['cls']

    # def __new__(cls, *args, **kwargs):
    #     print('new')
    #     super(Singleton, cls).__new__(*args, **kwargs)
    #
    # def __init__(cls):
    #     print('init')
    #     super(Singleton, cls).__init__()


class DD(metaclass=Singleton):
    def __init__(self, a, b):
        self.a = a
        self.b = b


C = type("C", (A,), {})

if __name__ == '__main__':
    # a = [1, 0, 0,0,0,0]
    # res = seat(a)
    # # print(res)
    # d1 = DD(1, 2)
    # d2 = DD(4, 6)
    # print(d1.a, d1.b)
    # print(d2.a, d2.b)
    # print(DD.mro())

    # import logging  # 引入logging模块
    # import os.path
    # import time
    #
    # # 第一步，创建一个logger
    # logger = logging.getLogger()
    # logger.setLevel(logging.INFO)  # Log等级总开关
    # # 第二步，创建一个handler，用于写入日志文件
    # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    # log_name = log_path + rq + '.log'
    # logfile = log_name
    # fh = logging.FileHandler(logfile, mode='w+')
    # fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    #
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
    # # 第三步，定义handler的输出格式
    # formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    # fh.setFormatter(formatter)
    #
    # ch.setFormatter(formatter)
    # # 第四步，将logger添加到handler里面
    # logger.addHandler(fh)
    #
    # logger.addHandler(ch)
    # # 日志
    # logger.debug('this is a logger debug message')
    # logger.info('this is a logger info message')
    # logger.warning('this is a logger warning message')
    # logger.error('this is a logger error message')
    # logger.critical('this is a logger critical message')

    import logging
    import os
    import time
    from logging import handlers

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Log等级总开关

    log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    rq = time.strftime('%Y%m%d', time.localtime(time.time()))
    log_name = log_path + rq + '_Log.log'

    # fh = handlers.TimedRotatingFileHandler(filename=log_file, when="S", interval=5,
    #                                        backupCount=3)  # filename定义将信息输入到指定的文件，
    # when指定单位是s(秒),interval是时间间隔的频率,单位是when所指定的哟（所以，你可以理解频率是5s）；backupCount表示备份的文件个数，我这里是指定的3个文件。

    fh = handlers.RotatingFileHandler(filename=log_name, maxBytes=10 * 1024 * 1024,
                                      backupCount=3)  # 最多备份3个日志文件，每个日志文件最大10M
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

    formatter = logging.Formatter("%(asctime)s - %(filename)s[:%(lineno)d] - %(levelname)s: %(message)s")  # 定义输出格式
    fh.setFormatter(formatter)  # 添加格式化输出
    logger.addHandler(fh)

    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.debug("test1")
    logger.info("test2")
    logger.warning("test3")
    logger.error("test4")
    logger.critical('test5')
