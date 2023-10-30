# --*--coding: utf-8 --*--
import json

import requests

from commonlib.log_utils import log


class BaseService(object):
    """ base service class"""
    def __init__(self, env):
        self.env = env
        self._variable = {}  # 共用用的变量
        self._extract = {}  # 从返回结果中提取的数据，储存测试用例间，数据的传递

    @property
    def variable(self):
        """ 数据提取
        """
        return self._variable

    @property
    def extract(self):
        """ 数据提取
        """
        return self._extract

    @staticmethod
    def log_request_info(data_obj):
        """ 打印接口信息"""
        log().info("发送url：%s" % data_obj.url)
        log().info("发送headers：%s" % data_obj.request_headers)
        log().info("发送报文：%s" % data_obj.request_data_str)

    def get_extract(self, key, default=None):
        """获取提取数据"""
        if key in self.extract:
            return self.extract[key]
        else:
            return default

    def get_variable(self, key, default=None):
        """获取变量数据"""
        if key in self.variable:
            return self.variable[key]
        else:
            return default

    def add_variable(self, key, value):
        """ 变量的添加"""
        self.variable[key] = value

    def add_extract(self, key, value):
        """ 提取的添加"""
        self.extract[key] = value

    def add_variable_batch(self, data):
        """ 批量添加变量"""
        for k, v in data.items():
            self.variable[k] = v

    def request_post(self, data_obj):
        """ post请求"""
        self.log_request_info(data_obj)
        rp = requests.post(data_obj.url, data_obj.request_data_str, headers=data_obj.request_headers)
        rp = rp.json()
        log().info("响应报文：%s" % json.dumps(rp))
        return rp
