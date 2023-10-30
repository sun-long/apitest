#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.bill_service_swagger import BillSwaggerApi


"""
使用说明：


"""


class BillSwaggerBusiness(BillSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(BillSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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
        if inte_obj.path == '/console/v1/all_bill':
            inte_obj.set_headers('X-Belt-Action', 'GetAllBillGroup')
        elif inte_obj.path == '/console/v1/bill':
            inte_obj.set_headers('X-Belt-Action', 'GetOneBillGroup')
        elif inte_obj.path == '/console/v1/bill_num':
            inte_obj.set_headers('X-Belt-Action', 'GetBillNum')
        elif inte_obj.path == '/console/v1/update_bill_status':
            inte_obj.set_headers('X-Belt-Action', 'UpdateBillStatus')
        elif inte_obj.path == '/console/v1/download':
            inte_obj.set_headers('X-Belt-Action', 'DownloadBillDetail')
