#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.auth_service_swagger import AuthSwaggerApi


"""
使用说明：


"""


class AuthSwaggerBusiness(AuthSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(AuthSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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
        inte_obj.set_headers("X-Belt-Version", "v1")
        if inte_obj.path == '/console/v1/accounts/account_info':
            inte_obj.set_headers('X-Belt-Action', 'GetAccountInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/auth_status':
            inte_obj.set_headers('X-Belt-Action', 'GetAccountStatus')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/enterprise':
            inte_obj.set_headers('X-Belt-Action', 'GetEnterpriseAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/enterprise/unredacted_info':
            inte_obj.set_headers('X-Belt-Action', 'GetEnterpriseAccountUnRedactedInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/enterprise_submit':
            inte_obj.set_headers('X-Belt-Action', 'SubmitEnterpriseAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/enterprise_update':
            inte_obj.set_headers('X-Belt-Action', 'UpdateEnterpriseAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/industry_info':
            inte_obj.set_headers('X-Belt-Action', 'GetIndustryInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/person':
            inte_obj.set_headers('X-Belt-Action', 'GetPersonAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/person/unredacted_info':
            inte_obj.set_headers('X-Belt-Action', 'GetPersonAccountUnRedactedInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/person_submit':
            inte_obj.set_headers('X-Belt-Action', 'SubmitPersonAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/person_update':
            inte_obj.set_headers('X-Belt-Action', 'UpdatePersonAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')