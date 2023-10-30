#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.ipsocr_service_swagger import IpsocrSwaggerApi


"""
使用说明：


"""


class IpsocrSwaggerBusiness(IpsocrSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(IpsocrSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "Authorization"
        self.TOKEN_VALUE = "Bearer %s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)

        inte_obj.set_headers('X-Resource-Type', 'ips')
        inte_obj.set_headers('X-Object-Type', 'ocr')
        inte_obj.set_headers('X-Object-Version', '2.5.0-dev')
        inte_obj.set_headers('X-Bot-Name', 'bot-ids')
