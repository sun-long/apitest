#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class BillSwaggerApi(BaseApi):
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

    def ConsoleBillService_GetAllBillGroupGetApi(self, date_request_start_at=None, date_request_end_at=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有账期账单
route: prefix=console action=GetAllBillGr... """
        """  path: [get]/console/v1/all_bill API """
        """  params: 
                参数名称：date_request.start_at　类型：string　描述：过滤起始时间.
                参数名称：date_request.end_at　类型：string　描述：过滤结束时间
        """
        """  resp:
                200(A successful response.):
                {
                    "all_bill_groups": [
                        {
                            "account_status": "[STATUS_UNLIMITED]STATUS_UNLIMITED/STATUS_UNCONFIRMED/STATUS_CONFIRMED/STATUS_DOUBT/STATUS_DOUBT_CONFIRMED/STATUS_NONE",
                            "build_at": "",
                            "create_at": "",
                            "due_fee": "",
                            "fee": "",
                            "pay_status": "[NONE]NONE/NOT_PAY/PAY",
                            "send_at": "",
                            "status": "[UNKOWN]UNKOWN/NOT_SEND/SEND",
                            "updated_at": ""
                        }
                    ]
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
        intef = collections.interface("bill", "ConsoleBillService_GetAllBillGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("date_request.start_at", date_request_start_at)
        intef.update_params("date_request.end_at", date_request_end_at)
        return intef.request() if sendRequest else intef

    def ConsoleBillService_GetOneBillGroupGetApi(self, create_at=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取单个账期账单详情
route: prefix=console action=GetOneBill... """
        """  path: [get]/console/v1/bill API """
        """  params: 
                参数名称：create_at　类型：string　描述：账期 用该时间的年月查询账单
        """
        """  resp:
                200(A successful response.):
                {
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
                    ]
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
        intef = collections.interface("bill", "ConsoleBillService_GetOneBillGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("create_at", create_at)
        return intef.request() if sendRequest else intef

    def ConsoleBillService_GetBillNumGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  按状态获取账单数
route: prefix=console action=GetBillNum v... """
        """  path: [get]/console/v1/bill_num API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "num": 0
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
        intef = collections.interface("bill", "ConsoleBillService_GetBillNum")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleBillService_DownloadBillDetailPostApi(self, create_at=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账单明细（ga版本新增）
route: prefix=console action=Download... """
        """  path: [post]/console/v1/download API """
        """  body: 
                {
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
        intef = collections.interface("bill", "ConsoleBillService_DownloadBillDetail")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("create_at", create_at)
        return intef.request() if sendRequest else intef

    def ConsoleBillService_UpdateBillStatusPostApi(self, create_at=None, account_status=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新账期账单状态
route: prefix=console action=UpdateBillSt... """
        """  path: [post]/console/v1/update_bill_status API """
        """  body: 
                {
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
        intef = collections.interface("bill", "ConsoleBillService_UpdateBillStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("create_at", create_at)
        intef.update_body("account_status", account_status)
        return intef.request() if sendRequest else intef

