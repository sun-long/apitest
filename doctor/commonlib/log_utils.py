#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   log_utils.py
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/26 上午9:49   wangan      1.0         None
'''

import logging
import os


def log():
    """使用pytest自带的log组件，格式在pytest.ini中设置"""
    log_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    result_path = os.path.join(log_path, "result")
    if not os.path.exists(result_path):
        os.mkdir(result_path)
    log = logging.getLogger()
    if not log.handlers:
        log.setLevel(logging.INFO)
        # fh = logging.FileHandler(os.path.join(result_path, "log_" + str(datetime.date.today()) + ".log"))
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
        # fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # log.addHandler(fh)
        log.addHandler(ch)
    return log
    # return logging.getLogger()


class LogCollect(object):
    def __init__(self):
        self._log_list = []

    @property
    def log_list(self):
        return self._log_list

    def add_log(self, message, level="info"):
        self._log_list.append((level, message))

    def print(self):
        for _log in self._log_list:
            if _log[0] == "warning":
                log().warning(_log[1])
            elif _log[0] == "error":
                log().error(_log[1])
            elif _log[0] == "debug":
                log().debug(_log[1])
            else:
                log().info(_log[1])
        self._log_list = []