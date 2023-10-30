#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from commonlib import utils
from commonlib.decorator import wait
from defines.nova.api.user_service_swagger import UserSwaggerApi
from commonlib import utils

"""
使用说明：


"""


class UserSwaggerBusiness(UserSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(UserSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Sensenova-Token" # 默认token的key
        self.TOKEN_VALUE = "%s"  # token默认信息
        self.configMap = utils.readConfigMap("nova-console.yaml", "http://nova-console.nova-platform:9421",
                                             action_name="X-Sensenova-Action")

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        self.set_nova_defines(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)