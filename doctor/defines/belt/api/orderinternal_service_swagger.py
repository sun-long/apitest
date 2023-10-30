#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class OrderinternalSwaggerApi(BaseApi):
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

    def ConsoleOrderInternalService_GetAuditAllOrderGetApi(self, status=None, account_id=None, user_id=None, user_name=None, order_id=None, category1=None, category2=None, bill_mode=None, created_sort_type=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有订单
route: prefix=console-internal action=GetAu... """
        """  path: [get]/console-internal/v1/all_order API """
        """  params: 
                参数名称：status　类型：string　描述：审核状态筛选，可选.

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
                参数名称：account_id　类型：string　描述：账户筛选，可选.
                参数名称：user_id　类型：string　描述：主用户ID筛选，可选.
                参数名称：user_name　类型：string　描述：主用户筛选，可选.
                参数名称：order_id　类型：string　描述：订单筛选，可选.
                参数名称：category1　类型：string　描述：一级类目筛选，可选.
                参数名称：category2　类型：string　描述：二级类目筛选，可选.
                参数名称：bill_mode　类型：string　描述：付费方式，可选.

 - PAY_TYPE_UNKNOWN: 未知模式
 - PAY_TYPE_PRE: 预付费(前向付费)模式
 - PAY_TYPE_POST: 后付费模式
 - PAY_TYPE_PRE_FREE: 预付费(免费/赠送)模式
                参数名称：created_sort_type　类型：string　描述：排序方式.

 - DESC: 倒序排序
 - ASC: 正序排序
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
filled in response
        """
        """  resp:
                200(A successful response.):
                {
                    "all_orders": [
                        {
                            "account_info": {
                                "account_id": "",
                                "account_name": "",
                                "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                                "business_user": "",
                                "enterprise_name": ""
                            },
                            "all_modify_records": [
                                {
                                    "new_prices": [],
                                    "oa_number": "",
                                    "op_at": "",
                                    "op_user": "",
                                    "order_id": "",
                                    "remark": "",
                                    "spu_id": ""
                                }
                            ],
                            "category1": {
                                "category_id": "",
                                "display_name": "",
                                "level": 0,
                                "name": ""
                            },
                            "category2": {
                                "category_id": "",
                                "display_name": "",
                                "level": 0,
                                "name": ""
                            },
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
                            },
                            "user_id": "",
                            "user_name": ""
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
        intef = collections.interface("orderInternal", "ConsoleOrderInternalService_GetAuditAllOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("status", status)
        intef.update_params("account_id", account_id)
        intef.update_params("user_id", user_id)
        intef.update_params("user_name", user_name)
        intef.update_params("order_id", order_id)
        intef.update_params("category1", category1)
        intef.update_params("category2", category2)
        intef.update_params("bill_mode", bill_mode)
        intef.update_params("created_sort_type", created_sort_type)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleOrderInternalService_GetAllCategoryGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有类目信息（二期接口）
route: prefix=console-internal acti... """
        """  path: [get]/console-internal/v1/category API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "all_categories": [
                        {
                            "category_id": "",
                            "display_name": "",
                            "level": 0,
                            "name": ""
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
        intef = collections.interface("orderInternal", "ConsoleOrderInternalService_GetAllCategory")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleOrderInternalService_GetOrderModifyRecordGetApi(self, order_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取订单修改记录（beta1版本修改）
route: prefix=console-internal... """
        """  path: [get]/console-internal/v1/modify_order API """
        """  params: 
                参数名称：order_id　类型：string　描述：订单ID
        """
        """  resp:
                200(A successful response.):
                {
                    "all_modify_records": [
                        {
                            "new_prices": [],
                            "oa_number": "",
                            "op_at": "",
                            "op_user": "",
                            "order_id": "",
                            "remark": "",
                            "spu_id": ""
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
        intef = collections.interface("orderInternal", "ConsoleOrderInternalService_GetOrderModifyRecord")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("order_id", order_id)
        return intef.request() if sendRequest else intef

    def ConsoleOrderInternalService_ModifyOrderPostApi(self, all_modify_records=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  修改订单（beta1版本修改）
route: prefix=console-internal act... """
        """  path: [post]/console-internal/v1/modify_order API """
        """  body: 
                {
                    "all_modify_records": [
                        {
                            "new_prices": [],
                            "oa_number": "",
                            "op_at": "",
                            "op_user": "",
                            "order_id": "",
                            "remark": "",
                            "spu_id": ""
                        }
                    ]
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
        intef = collections.interface("orderInternal", "ConsoleOrderInternalService_ModifyOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("all_modify_records", all_modify_records)
        return intef.request() if sendRequest else intef

    def ConsoleOrderInternalService_GetAuditOneOrderGetApi(self, order_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  按order_id获取订单详情
route: prefix=console-internal act... """
        """  path: [get]/console-internal/v1/order API """
        """  params: 
                参数名称：order_id　类型：string　描述：订单ID
        """
        """  resp:
                200(A successful response.):
                {
                    "order_info": {
                        "account_info": {
                            "account_id": "",
                            "account_name": "",
                            "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                            "business_user": "",
                            "enterprise_name": ""
                        },
                        "all_modify_records": [
                            {
                                "new_prices": [],
                                "oa_number": "",
                                "op_at": "",
                                "op_user": "",
                                "order_id": "",
                                "remark": "",
                                "spu_id": ""
                            }
                        ],
                        "category1": {
                            "category_id": "",
                            "display_name": "",
                            "level": 0,
                            "name": ""
                        },
                        "category2": {
                            "category_id": "",
                            "display_name": "",
                            "level": 0,
                            "name": ""
                        },
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
                        },
                        "user_id": "",
                        "user_name": ""
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
        intef = collections.interface("orderInternal", "ConsoleOrderInternalService_GetAuditOneOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("order_id", order_id)
        return intef.request() if sendRequest else intef

    def ConsoleOrderInternalService_AuditOrderPostApi(self, order_id=None, operate=None, reason=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  审核订单
route: prefix=console-internal action=AuditOr... """
        """  path: [post]/console-internal/v1/order API """
        """  body: 
                {
                    "operate": "[OP_REJECT]OP_REJECT/OP_AGREE",
                    "order_id": "",
                    "reason": ""
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
        intef = collections.interface("orderInternal", "ConsoleOrderInternalService_AuditOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("order_id", order_id)
        intef.update_body("operate", operate)
        intef.update_body("reason", reason)
        return intef.request() if sendRequest else intef

    def ConsoleOrderInternalService_UnsubscribeOrderPostApi(self, order_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后付费订单退订（ga版本新增）
route: prefix=console-internal act... """
        """  path: [post]/console-internal/v1/unsubscribe_order API """
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
        intef = collections.interface("orderInternal", "ConsoleOrderInternalService_UnsubscribeOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("order_id", order_id)
        return intef.request() if sendRequest else intef

