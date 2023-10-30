#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.rechargelog_service_swagger import RechargelogSwaggerApi


"""
使用说明：


"""


class RechargelogSwaggerBusiness(RechargelogSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(RechargelogSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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
        if inte_obj.path == "/console-internal/v1/cur_recharge":
            inte_obj.set_headers('X-Belt-Action', 'GetCurRechargeLog')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/last_three_month_bill_amount/all":
            inte_obj.set_headers('X-Belt-Action', 'GetLatestRechargelogsByAccountIDList')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge":
            inte_obj.set_headers('X-Belt-Action', 'Recharge')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/account_amount":
            inte_obj.set_headers('X-Belt-Action', 'UpdateAccountAmountInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/account_amount_info":
            inte_obj.set_headers('X-Belt-Action', 'GetAccountAmountInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/accounts/second_confirm/count":
            inte_obj.set_headers('X-Belt-Action', 'CountSecondConfirmRechargeLogByAccountIDs')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/accounts/unprocessed/count":
            inte_obj.set_headers('X-Belt-Action', 'CountUnprocessedRechargelogByAccountIDs')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/all":
            inte_obj.set_headers('X-Belt-Action', 'GetAllRechargeLog')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/balance_logs":
            inte_obj.set_headers('X-Belt-Action', 'GetBalancelogs')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/cancel":
            inte_obj.set_headers('X-Belt-Action', 'CancelRecharge')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/create":
            inte_obj.set_headers('X-Belt-Action', 'CreateRecharge')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/latest/all":
            inte_obj.set_headers('X-Belt-Action', 'GetLatestRechargelogsByAccountIDList')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/owed_amount":
            inte_obj.set_headers('X-Belt-Action', 'UpdateOwedAmount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/reject":
            inte_obj.set_headers('X-Belt-Action', 'RejectRecharge')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/second_confirm":
            inte_obj.set_headers('X-Belt-Action', 'SecondConfirmationRecharge')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/second_confirm/all":
            inte_obj.set_headers('X-Belt-Action', 'GetSecondConfirmationRechargelogList')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/recharge/unprocessed/all":
            inte_obj.set_headers('X-Belt-Action', 'GetUnprocessedRechargelogList')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console/v1/recharge/amount":
            inte_obj.set_headers('X-Belt-Action', 'GetAmount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix("api")
        elif inte_obj.path == "/console/v1/recharge/apply":
            inte_obj.set_headers('X-Belt-Action', 'ApplyRecharge')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix("api")
        elif inte_obj.path == "/console-internal/v1/recharge/amount":
            inte_obj.set_headers('X-Belt-Action', 'GetInternalAmount')
            inte_obj.set_headers('X-Belt-Version', 'v1')

