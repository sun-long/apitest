#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.galaxyproduct_service_swagger import GalaxyproductSwaggerApi
from commonlib.galaxy import authToken
from commonlib.galaxy import iamToken

"""
使用说明：


"""


class GalaxyproductSwaggerBusiness(GalaxyproductSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None, user_info=None):
        super(GalaxyproductSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "Authorization" # 默认token的key
        self.TOKEN_VALUE = "%s"  # token默认信息
        self.user_info = user_info

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        # self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if 'v1' in inte_obj.path:
            dd, Authorization = iamToken(self.user_info.ak, self.user_info.sk)
            inte_obj.set_headers("Authorization", Authorization)
            inte_obj.set_headers("date", dd)
            inte_obj.set_path_prefix("/openapi/v1/product-management")
        elif 'v2' in inte_obj.path:
            token = authToken(self.user_info.ak, self.user_info.sk, self.host)
            inte_obj.set_headers("Authorization", token)
            inte_obj.set_path_prefix("/openapi/v2/product-management")
        else:
            raise Exception("该路径中不存在v1,v2")