import logging
import os
import time
from logging import handlers


def logger_init(path: str = None, debug: bool = False):
    """
    日志模块初始化
    :param path: 日志存放路径, 默认是在初始化该函数代码的当前路径下创建一个Logs目录，
                按天存放日志 如：Logs.20201105_Log.log
    :param debug: 是否是调试模式 如果是调试模式，会在控制台也输出日志
    :return:
    """
    logger = logging.getLogger(__name__)
    """
    日志等級：
        debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上
    
        info : 打印info,warning,error,critical级别的日志,确认一切按预期运行
        
        warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作
        
        error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能
        
        critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行
    """
    logger.setLevel(logging.DEBUG)  # Log等级总开关

    if path:
        log_path = path + '/Logs/'
    else:
        log_path = os.path.dirname(os.getcwd()) + '/Logs/'

    if not os.path.exists(log_path):
        os.mkdir(log_path)

    rq = time.strftime('%Y%m%d', time.localtime(time.time()))
    log_name = log_path + rq + '_Log.log'

    # fh = handlers.TimedRotatingFileHandler(filename=log_file, when="S", interval=5,
    #                                        backupCount=3)  # filename定义将信息输入到指定的文件，
    # when指定单位是s(秒),interval是时间间隔的频率,单位是when所指定的哟（所以，你可以理解频率是5s）；backupCount表示备份的文件个数，我这里是指定的3个文件。

    fh = handlers.RotatingFileHandler(filename=log_name, maxBytes=10 * 1024 * 1024,
                                      backupCount=3)  # 最多备份3个日志文件，每个日志文件最大10M
    fh.setLevel(logging.INFO)  # 输出到file的log等级的开关
    formatter = logging.Formatter("%(asctime)s - %(filename)s[:%(lineno)d] - %(levelname)s: %(message)s")  # 定义输出格式
    fh.setFormatter(formatter)  # 添加格式化输出
    logger.addHandler(fh)

    if debug:
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
