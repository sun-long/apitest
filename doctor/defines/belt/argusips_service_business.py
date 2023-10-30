#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from commonlib import utils
from defines.belt.api.argusips_service_swagger import ArgusipsSwaggerApi


"""
使用说明：


"""


class ArgusipsSwaggerBusiness(ArgusipsSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(ArgusipsSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息
        self.configMap = utils.readConfigMap("argus.yaml", "http://lambor-http.argus:80")

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        if inte_obj.path in self.configMap:
            info = self.configMap[inte_obj.path][inte_obj.method]
            inte_obj.set_headers('X-Belt-Action', info["action"])
            inte_obj.set_headers('X-Belt-Version', info["version"])
            inte_obj.set_path_prefix(info["paths"])
        else:
            raise Exception("no support PATH:%s" % inte_obj.path)