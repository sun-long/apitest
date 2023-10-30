#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.oplog_service_swagger import OplogSwaggerApi


"""
使用说明：


"""


class OplogSwaggerBusiness(OplogSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(OplogSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Token"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        if inte_obj.path == '/console-internal/v1/oplogs':
            if inte_obj.method == 'get':
                inte_obj.set_headers('X-Belt-Action', 'GetOplogs')
                inte_obj.set_headers('X-Belt-Version', 'v1')
            elif inte_obj.method == 'post':
                inte_obj.set_headers('X-Belt-Action', 'CreateOplog')
                inte_obj.set_headers('X-Belt-Version', 'v1')
