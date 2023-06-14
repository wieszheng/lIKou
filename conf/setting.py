import os

current_path = os.path.abspath(__file__)
dirname_path = os.path.dirname(os.path.dirname(current_path))

BROWSER_TYPE = 2
LOG_PATH = os.path.abspath(os.path.join(dirname_path, 'logs/log.log'))
CHROME_PATH = os.path.abspath(os.path.join(dirname_path, 'driver/chromedriver.exe'))
EDGE_PATH = os.path.abspath(os.path.join(dirname_path, 'driver/msedgedriver.exe'))

LOGGING_DIC = {
    'version': 1.0,
    'disableexisting_loggers': False,
    # 日志格式
    'formatters': {
        'standard': {
            'format': '%(asctime)s - [line:%(lineno)d] %(name)s - %(levelname)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s [%(name)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'filters': {},
    # 日志处理器
    'handlers': {
        'console_debug_handler': {
            'level': 'DEBUG',  # 日志处理的级别限制
            'class': 'logging.StreamHandler',  # 输出到终端
            'formatter': 'standard'  # 日志格式
        },
        'file_debug_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'filename': LOG_PATH,  # 日志存放的路径
            'encoding': 'utf-8',  # 日志文件的编码
            'formatter': 'standard',
        },
    },
    # 日志记录器
    'loggers': {
        '': {  # 导入时logging.getLogger时使用的app_name
            'handlers': ['console_debug_handler', 'file_debug_handler'],  # 日志分配到哪个handlers中
            'level': 'DEBUG',  # 日志记录的级别限制
            'propagate': False,  # 默认为True，向上（更高级别的logger）传递，设置为False即可，否则会一份日志向上层层传递
        },
    }
}
"""
        'file_info_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler', # 保存到文件,日志轮转
            'filename': 'user.logs',
            'maxBytes': 1024*1024*10, # 日志大小 10M
            'backupCount': 10, # 日志文件保存数量限制
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
"""

# import logging.config
#
#
# logging.config.dictConfig(LOGGING_DIC)
# logger1 = logging.getLogger('logger33')
# for i in range(10):
#     logger1.info('登录了')
