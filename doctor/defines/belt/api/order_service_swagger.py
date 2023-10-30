#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class OrderSwaggerApi(BaseApi):
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

    def ConsoleOrderService_GetAllOrderGetApi(self, status=None, date_request_start_at=None, date_request_end_at=None, page_request_offset=None, page_request_limit=None, page_request_total=None, created_sort_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有订单
route: prefix=console action=GetAllOrder ve... """
        """  path: [get]/console/v1/all_order API """
        """  params: 
                参数名称：status　类型：string　描述：订单状态筛选，可选.

 - UNLIMITED: 不限制，只是用来筛选状态用
 - AUDITING: 后付费订单待审核状态
 - AUDIT_APPROVED: 后付费订单审核通过状态
 - AUDIT_REJECTED: 后付费订单审核不通过状态
 - TO_BE_PAID: 预付费订单待支付状态
 - PAID: 预付费订单已支付状态
 - CANCEL_PAID: 预付费订单取消支付状态
 - DELETED: 订单已删除（内部用）
 - UNSUBSCRIBED: 退订（后付费订单终止服务）
 - FREEZED: 账户禁用: 1)已购后付费服务全部失效，后付费订单作废 2) 预付费订单冻结，无法使用 3)不能新增购买
                参数名称：date_request.start_at　类型：string　描述：过滤起始时间.
                参数名称：date_request.end_at　类型：string　描述：过滤结束时间.
                参数名称：page_request.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条; 默认值为0.
返回本次请求返回的第一条记录实际位置(一般与输入一致).
[EN] Optional, start position, value: > = 0, 0 is the first line; the
default value is 0. In response, actual offset of the first returned record
is returned (generally equals to the offset in request).
                参数名称：page_request.limit　类型：integer　描述：长度, 取值范围[1,100], 如果超出范围, 则返回失败;
在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准. [EN] Length,
default value range [1,100], if it is out of the range, error will be
returned; as the limit range may be redefined in some APIs, please refer to
the supplementary description of these APIs.
                参数名称：page_request.total　类型：integer　描述：可选, 总数, 请求无须填此参数, 响应时填写.
[EN] Optional, this parameter is not required for request, but will be
filled in response.
                参数名称：created_sort_type　类型：string　描述：排序方式.

 - DESC: 倒序排序
 - ASC: 正序排
        """
        """  resp:
                200(A successful response.):
                {
                    "all_orders": [
                        {
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("order", "ConsoleOrderService_GetAllOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("status", status)
        intef.update_params("date_request.start_at", date_request_start_at)
        intef.update_params("date_request.end_at", date_request_end_at)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        intef.update_params("created_sort_type", created_sort_type)
        return intef.request() if sendRequest else intef

    def ConsoleOrderService_GetOneOrderGetApi(self, order_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  按order_id获取订单详情
route: prefix=console action=GetOn... """
        """  path: [get]/console/v1/order API """
        """  params: 
                参数名称：order_id　类型：string　描述：订单ID
        """
        """  resp:
                200(A successful response.):
                {
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
        intef = collections.interface("order", "ConsoleOrderService_GetOneOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("order_id", order_id)
        return intef.request() if sendRequest else intef

    def ConsoleOrderService_CreateOrderPostApi(self, all_items=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建订单
route: prefix=console action=CreateOrder vers... """
        """  path: [post]/console/v1/order API """
        """  body: 
                {
                    "all_items": [
                        {
                            "count": "",
                            "site_id": "",
                            "sku_group_id": "",
                            "sku_id": ""
                        }
                    ]
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "flag": 0,
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
        intef = collections.interface("order", "ConsoleOrderService_CreateOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("all_items", all_items)
        return intef.request() if sendRequest else intef

    def ConsoleOrderService_GetOrderNumGetApi(self, status=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取订单数目
route: prefix=console action=GetOrderNum ve... """
        """  path: [get]/console/v1/order_num API """
        """  params: 
                参数名称：status　类型：string　描述：订单状态筛选，可选.

 - UNLIMITED: 不限制，只是用来筛选状态用
 - AUDITING: 后付费订单待审核状态
 - AUDIT_APPROVED: 后付费订单审核通过状态
 - AUDIT_REJECTED: 后付费订单审核不通过状态
 - TO_BE_PAID: 预付费订单待支付状态
 - PAID: 预付费订单已支付状态
 - CANCEL_PAID: 预付费订单取消支付状态
 - DELETED: 订单已删除（内部用）
 - UNSUBSCRIBED: 退订（后付费订单终止服务）
 - FREEZED: 账户禁用: 1)已购后付费服务全部失效，后付费订单作废 2) 预付费订单冻结，无法使用 3)不能新增购
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
        intef = collections.interface("order", "ConsoleOrderService_GetOrderNum")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("status", status)
        return intef.request() if sendRequest else intef

    def ConsoleOrderService_UnsubscribeOrderPostApi(self, order_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后付费订单退订（beta1版本新增）
route: prefix=console action=Un... """
        """  path: [post]/console/v1/unsubscribe_order API """
        """  body: 
                {
                    "order_id": ""
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
        intef = collections.interface("order", "ConsoleOrderService_UnsubscribeOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("order_id", order_id)
        return intef.request() if sendRequest else intef

    def ConsoleOrderService_GetValidOrderNumGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取有效的后付费订单和非0元预付费订单数目
route: prefix=console action... """
        """  path: [get]/console/v1/valid_order_num API """
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
        intef = collections.interface("order", "ConsoleOrderService_GetValidOrderNum")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

