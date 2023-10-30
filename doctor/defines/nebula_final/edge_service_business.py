#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.nebula_final.api.edge_service_swagger import EdgeSwaggerApi


"""
使用说明：


"""


class EdgeSwaggerBusiness(EdgeSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(EdgeSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)

    def getToken(self, user_name, password):
        resp = self.AgentUserService_UserLoginPostApi(user_name, password)
        token = resp.json_get("token")
        return token

    def freshToken(self):
        password = "TmVidWxhMTIzJCVe"
        user_name = "admin"
        self.token = self.getToken(user_name, password)
