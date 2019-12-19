# -*- coding:utf-8 -*-

import os
import logging
from conf import settings


class Logger(object):
    __instance = None

    def __init__(self):
        self.info_log_file = settings.INFO_LOG_FILE
        self.error_log_file = settings.ERROR_LOG_FILE
        self.info_logger = None
        self.error_logger = None

        self.initialize_info_log()
        self.initialize_error_log()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    @staticmethod
    def check_path_exist(log_abs_file):
        log_path = os.path.split(log_abs_file)[0]
        if not os.path.exists(log_path):
            os.mkdir(log_path)

    def initialize_info_log(self):
        self.check_path_exist(self.info_log_file)
        file_1_1 = logging.FileHandler(self.info_log_file, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(levelname)s - %(asctime)s - %(module)s - %(lineno)d - %(message)s")
        file_1_1.setFormatter(fmt)
        logger1 = logging.Logger('info_log', level=logging.INFO)
        logger1.addHandler(file_1_1)
        self.info_logger = logger1

    def initialize_error_log(self):
        self.check_path_exist(self.error_log_file)
        file_1_1 = logging.FileHandler(self.error_log_file, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(levelname)s - %(asctime)s - %(module)s - %(lineno)d - %(message)s")
        file_1_1.setFormatter(fmt)
        logger1 = logging.Logger('error_log', level=logging.ERROR)
        logger1.addHandler(file_1_1)
        self.error_logger = logger1

    def log(self, message, mode=True):
        """
        写入日志
        :param message: 日志信息
        :param mode: True表示运行信息，False表示错误信息
        :return:
        """
        if mode:
            self.info_logger.info(message)
        else:
            self.error_logger.error(message)
