#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class Wallet_internalSwaggerApi(BaseApi):
    """ web接口"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        self.host = host
        self.ext_info = ext_info
        self.config_obj = config_obj
        self.token = token
        self.host_map = self.readHostMap(collections.name)
        self.TOKEN_NAME = ""
        self.TOKEN_VALUE = "%s"  # token默认信息
        collections.init(self, conf=config_obj, ext_info=ext_info)

    def genPostMan(self):
        """ 生成postman接口文件"""
        self.ext_info.isRequestOpened = True
        self.genPostManFromSwagger(collections)

    def NovaWalletInternalService_AddCouponPostApi(self, account_id=None, account_type=None, amount=None, loop_mode=None, period=None, send_at=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  添加优惠券发放方式
route: prefix=console-internal action=Ad... """
        """  path: [post]/console-internal/v1/add_coupon API """
        """  body: 
                {
                    "account_id": "",
                    "account_type": "[Identity_Unauthenticated]Identity_Unauthenticated/Business/Individual",
                    "amount": "",
                    "loop_mode": "[LOOP_NONE]LOOP_NONE/LOOP_MONTH",
                    "period": "[PERIOD_MONTH]PERIOD_MONTH/PERIOD_MONTH_FROM_NOW/PERIOD_YEAR/PERIOD_YEAR_FROM_NOW",
                    "send_at": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("Wallet_internal", "NovaWalletInternalService_AddCoupon")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("account_type", account_type)
        intef.update_body("amount", amount)
        intef.update_body("loop_mode", loop_mode)
        intef.update_body("period", period)
        intef.update_body("send_at", send_at)
        return intef.request() if sendRequest else intef

    def NovaWalletInternalService_GetAllCreditLimitGetApi(self, account_id=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有信用额度
route: prefix=console-internal action=Get... """
        """  path: [get]/console-internal/v1/all_credit API """
        """  params: 
                参数名称：account_id　类型：string　描述：账户筛选，可选
                参数名称：page_request.offset　类型：integer　描述：null
                参数名称：page_request.limit　类型：integer　描述：null
                参数名称：page_request.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "all_credits": [
                        {
                            "account_id": "",
                            "account_name": "",
                            "account_type": "[Identity_Unauthenticated]Identity_Unauthenticated/Business/Individual",
                            "amount": "",
                            "coupon_amount": "",
                            "credit_limit": "",
                            "left_credit_limit": ""
                        }
                    ],
                    "page_response": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("Wallet_internal", "NovaWalletInternalService_GetAllCreditLimit")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def NovaWalletInternalService_GetCouponListGetApi(self, account_id=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有发放记录
route: prefix=console-internal action=Get... """
        """  path: [get]/console-internal/v1/coupon API """
        """  params: 
                参数名称：account_id　类型：string　描述：账户ID 可选
                参数名称：page_request.offset　类型：integer　描述：null
                参数名称：page_request.limit　类型：integer　描述：null
                参数名称：page_request.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "all_coupons": [
                        {
                            "account_id": "",
                            "account_type": "[Identity_Unauthenticated]Identity_Unauthenticated/Business/Individual",
                            "amount": "",
                            "created_at": "",
                            "deleted_at": "",
                            "id": "",
                            "loop_mode": "[LOOP_NONE]LOOP_NONE/LOOP_MONTH",
                            "period": "[PERIOD_MONTH]PERIOD_MONTH/PERIOD_MONTH_FROM_NOW/PERIOD_YEAR/PERIOD_YEAR_FROM_NOW",
                            "send_at": "",
                            "status": "[STATUS_NORMAL]STATUS_NORMAL/STATUS_SEND_START/STATUS_SEND_END/STATUS_DELETED"
                        }
                    ],
                    "page_response": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("Wallet_internal", "NovaWalletInternalService_GetCouponList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def NovaWalletInternalService_DeleteCouponPostApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  作废优惠券
route: prefix=console-internal action=Delete... """
        """  path: [post]/console-internal/v1/delete_coupon API """
        """  body: 
                {
                    "id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("Wallet_internal", "NovaWalletInternalService_DeleteCoupon")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def NovaWalletInternalService_ModifyCreditLimitPostApi(self, account_id=None, credit_limit=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  修改信用额度
route: prefix=console-internal action=Modif... """
        """  path: [post]/console-internal/v1/modify_credit API """
        """  body: 
                {
                    "account_id": "",
                    "credit_limit": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("Wallet_internal", "NovaWalletInternalService_ModifyCreditLimit")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("credit_limit", credit_limit)
        return intef.request() if sendRequest else intef

    def NovaWalletInternalService_SendCouponPostApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  立刻执行发送优惠券任务
route: prefix=console-internal action=... """
        """  path: [post]/console-internal/v1/send_coupon API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                {
                    "job_start_time": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("Wallet_internal", "NovaWalletInternalService_SendCoupon")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

