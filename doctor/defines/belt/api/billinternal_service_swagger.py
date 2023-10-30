#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class BillinternalSwaggerApi(BaseApi):
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

    def ConsoleInternalBillService_GetInternalAllBillGetApi(self, create_at=None, account_id=None, user_id=None, user_name=None, enterprise_name=None, pay_status=None, page_request_limit=None, page_request_marker=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有账单
route: prefix=console-internal action=GetIn... """
        """  path: [get]/console-internal/v1/all_bill API """
        """  params: 
                参数名称：create_at　类型：string　描述：账期 用该时间的年月查询账单，可选.
                参数名称：account_id　类型：string　描述：账户筛选，可选.
                参数名称：user_id　类型：string　描述：主用户ID筛选，可选.
                参数名称：user_name　类型：string　描述：主用户筛选，可选.
                参数名称：enterprise_name　类型：string　描述：认证主体，可选.
                参数名称：pay_status　类型：string　描述：月账单状态，可选（ga版本新增，TODO可能会修改成bss定义的状态）.

 - NONE: 无效状态，未确认的账单会是这个状态
 - NOT_PAY: 未支付
 - PAY: 已支付
                参数名称：page_request.limit　类型：integer　描述：分页大小.
[EN] Page size, range [10, 100].
                参数名称：page_request.marker　类型：string　描述：分页标志, 第一页传空. 默认为空.
[EN] Page marker, first page is empty. Empty by default
        """
        """  resp:
                200(A successful response.):
                {
                    "all_bills": [
                        {
                            "account_info": {
                                "account_id": "",
                                "account_name": "",
                                "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                                "business_user": "",
                                "enterprise_name": ""
                            },
                            "bill_group_info": {
                                "account_status": "[STATUS_UNLIMITED]STATUS_UNLIMITED/STATUS_UNCONFIRMED/STATUS_CONFIRMED/STATUS_DOUBT/STATUS_DOUBT_CONFIRMED/STATUS_NONE",
                                "build_at": "",
                                "create_at": "",
                                "due_fee": "",
                                "fee": "",
                                "pay_status": "[NONE]NONE/NOT_PAY/PAY",
                                "send_at": "",
                                "status": "[UNKOWN]UNKOWN/NOT_SEND/SEND",
                                "updated_at": ""
                            },
                            "user_id": "",
                            "user_name": ""
                        }
                    ],
                    "page_response": {
                        "limit": 0,
                        "marker": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("billInternal", "ConsoleInternalBillService_GetInternalAllBill")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("create_at", create_at)
        intef.update_params("account_id", account_id)
        intef.update_params("user_id", user_id)
        intef.update_params("user_name", user_name)
        intef.update_params("enterprise_name", enterprise_name)
        intef.update_params("pay_status", pay_status)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.marker", page_request_marker)
        return intef.request() if sendRequest else intef

    def ConsoleInternalBillService_GetInternalOneBillGetApi(self, create_at=None, account_id=None, op_user=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取单个账单详情
route: prefix=console-internal action=Get... """
        """  path: [get]/console-internal/v1/bill API """
        """  params: 
                参数名称：create_at　类型：string　描述：账期 用该时间的年月查询账单.
                参数名称：account_id　类型：string　描述：AccountID.
                参数名称：op_user　类型：string　描述：账单发送人
        """
        """  resp:
                200(A successful response.):
                {
                    "account_info": {
                        "account_id": "",
                        "account_name": "",
                        "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                        "business_user": "",
                        "enterprise_name": ""
                    },
                    "all_bills": [
                        {
                            "all_bill_subs": [
                                {
                                    "bill_mode": "[PAY_TYPE_UNKNOWN]PAY_TYPE_UNKNOWN/PAY_TYPE_PRE/PAY_TYPE_POST/PAY_TYPE_PRE_FREE",
                                    "create_at": "",
                                    "due_fee": "",
                                    "end_at": "",
                                    "fee": "",
                                    "pay_status": "[NONE]NONE/NOT_PAY/PAY",
                                    "spu_id": "",
                                    "start_at": ""
                                }
                            ],
                            "bill_id": "",
                            "order_info": {
                                "account_id": "",
                                "audit_user_id": "",
                                "audit_user_name": "",
                                "before_fee": "",
                                "bill_mode": "[PAY_TYPE_UNKNOWN]PAY_TYPE_UNKNOWN/PAY_TYPE_PRE/PAY_TYPE_POST/PAY_TYPE_PRE_FREE",
                                "checked_at": "",
                                "created_at": "",
                                "fee": "",
                                "order_id": "",
                                "paid_at": "",
                                "pay_means": "[PAY_MEANS_UNKNOWN]PAY_MEANS_UNKNOWN/PAY_MEANS_BANK_CARD/PAY_MEANS_ALIPAY/PAY_MEANS_WECHAT/PAY_MEANS_OFFLINE/PAY_MEANS_E_WALLET",
                                "product_info": {
                                    "all_spus": [
                                        {
                                            "all_skus": [
                                                {
                                                    "all_prices": [
                                                        {
                                                            "created_at": "",
                                                            "end_time": "",
                                                            "id": "",
                                                            "rules": [
                                                                {
                                                                    "description": "",
                                                                    "end": 0,
                                                                    "start": 0,
                                                                    "unit_discount": 0,
                                                                    "unit_price": ""
                                                                }
                                                            ],
                                                            "scale": 0,
                                                            "site_id": "",
                                                            "sku_id": "",
                                                            "start_time": "",
                                                            "status": "[STATUS_UNLIMITED]STATUS_UNLIMITED/STATUS_VALID/STATUS_DELETED/STATUS_NONE",
                                                            "type": "[TYPE_TIERED]TYPE_TIERED/TYPE_VOLUME/TYPE_STAIR_STEP",
                                                            "unit": {
                                                                "factor": "",
                                                                "name": ""
                                                            },
                                                            "updated_at": ""
                                                        }
                                                    ],
                                                    "bill_mode": "[PAY_TYPE_UNKNOWN]PAY_TYPE_UNKNOWN/PAY_TYPE_PRE/PAY_TYPE_POST/PAY_TYPE_PRE_FREE",
                                                    "count": "",
                                                    "end_at": "",
                                                    "free_trial": false,
                                                    "id": "",
                                                    "sites": [
                                                        {
                                                            "name": "",
                                                            "site_id": ""
                                                        }
                                                    ],
                                                    "spec_values": {
                                                        "additionalProp1": "",
                                                        "additionalProp2": "",
                                                        "additionalProp3": ""
                                                    },
                                                    "start_at": "",
                                                    "status": "[UNLIMITED]UNLIMITED/TO_BE_VALID/VALID/UNVALID/DELETED"
                                                }
                                            ],
                                            "info": {
                                                "code": "",
                                                "descriptoin": "",
                                                "detailed_charging": "",
                                                "id": "",
                                                "name": "",
                                                "notice": ""
                                            }
                                        }
                                    ],
                                    "spu_group": {
                                        "all_sku_groups": [
                                            {
                                                "all_units": [
                                                    {
                                                        "sku_id": "",
                                                        "spu_id": ""
                                                    }
                                                ]
                                            }
                                        ],
                                        "info": {
                                            "code": "",
                                            "descriptoin": "",
                                            "detailed_charging": "",
                                            "id": "",
                                            "name": "",
                                            "notice": ""
                                        }
                                    }
                                },
                                "result": "",
                                "status": "[UNLIMITED]UNLIMITED/AUDITING/AUDIT_APPROVED/AUDIT_REJECTED/TO_BE_PAID/PAID/CANCEL_PAID/DELETED/UNSUBSCRIBED/FREEZED"
                            }
                        }
                    ],
                    "create_at": "",
                    "op_user": "",
                    "send_at": "",
                    "status": "[UNKOWN]UNKOWN/NOT_SEND/SEND",
                    "user_id": "",
                    "user_name": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("billInternal", "ConsoleInternalBillService_GetInternalOneBill")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("create_at", create_at)
        intef.update_params("account_id", account_id)
        intef.update_params("op_user", op_user)
        return intef.request() if sendRequest else intef

    def ConsoleInternalBillService_UpdateInternalBillStatusPostApi(self, create_at=None, account_id=None, account_status=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新账单状态
route: prefix=console-internal action=Updat... """
        """  path: [post]/console-internal/v1/bill API """
        """  body: 
                {
                    "account_id": "",
                    "account_status": "[STATUS_UNLIMITED]STATUS_UNLIMITED/STATUS_UNCONFIRMED/STATUS_CONFIRMED/STATUS_DOUBT/STATUS_DOUBT_CONFIRMED/STATUS_NONE",
                    "create_at": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("billInternal", "ConsoleInternalBillService_UpdateInternalBillStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("create_at", create_at)
        intef.update_body("account_id", account_id)
        intef.update_body("account_status", account_status)
        return intef.request() if sendRequest else intef

    def ConsoleInternalBillService_DownloadBillDetailPostApi(self, create_at=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账单明细
route: prefix=console-internal action=Downloa... """
        """  path: [post]/console-internal/v1/download API """
        """  body: 
                {
                    "account_id": "",
                    "create_at": ""
                }
        """
        """  resp:
                200(A successful response.(streaming responses)):
                ""
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("billInternal", "ConsoleInternalBillService_DownloadBillDetail")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("create_at", create_at)
        intef.update_body("account_id", account_id)
        return intef.request() if sendRequest else intef

    def ConsoleInternalBillService_SendInternalBillPostApi(self, create_at=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  发送账单
route: prefix=console-internal action=SendInt... """
        """  path: [post]/console-internal/v1/send_bill API """
        """  body: 
                {
                    "account_id": "",
                    "create_at": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("billInternal", "ConsoleInternalBillService_SendInternalBill")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("create_at", create_at)
        intef.update_body("account_id", account_id)
        return intef.request() if sendRequest else intef

