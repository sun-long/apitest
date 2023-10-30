#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from commonlib import time_utils, config
from commonlib.decorator import wait
from defines.nova.api.internalapi_service_postman import InternalPostmanApi
import time


class InternalSwaggerBusiness(InternalPostmanApi):
    """ 内部接口"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(InternalSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Sensenova-Signature" # 默认token的key
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        if "Authorization" in inte_obj.headers:
            inte_obj.set_headers("Authorization")
        # 限流1qps
        time.sleep(1)