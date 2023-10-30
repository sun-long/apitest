#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.galaxybeltoplog_service_swagger import GalaxybeltoplogSwaggerApi


"""
使用说明：


"""


class GalaxybeltoplogSwaggerBusiness(GalaxybeltoplogSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None, prefix_path=None):
        super(GalaxybeltoplogSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息
        self.prefix_path = prefix_path

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        inte_obj.set_path_prefix(self.prefix_path)
        if inte_obj.path == '/openapi/v2/oplog/abnormal':
            inte_obj.set_headers('X-Belt-Action', 'ReportOplogAbnormal')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        elif inte_obj.path == '/openapi/v2/oplog/queryById':
            inte_obj.set_headers('X-Belt-Action', 'QueryOplogByID')
            inte_obj.set_headers('X-Belt-Version', 'v2')
        else:
            raise Exception("no support PATH:%s" % inte_obj.path)