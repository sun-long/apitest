#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class SpuopSwaggerApi(BaseApi):
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

    def ConsoleSPUopService_GetAllSPUGetApi(self, code=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有SPU列表
route: prefix=console-internal action=Ge... """
        """  path: [get]/console-internal/v1/all_spuop API """
        """  params: 
                参数名称：code　类型：string　描述：spu code.
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
                    "all_infos": [
                        {
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
                            "code": "",
                            "id": "",
                            "name": ""
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
        intef = collections.interface("spuop", "ConsoleSPUopService_GetAllSPU")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("code", code)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleSPUopService_CheckSKUValidForAccountPostApi(self, account_id=None, sku_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  检查用户是否能订阅指定的SKU(console内部使用) """
        """  path: [post]/console-internal/v1/skuop/check API """
        """  body: 
                {
                    "account_id": "",
                    "sku_name": ""
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
        intef = collections.interface("spuop", "ConsoleSPUopService_CheckSKUValidForAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("sku_name", sku_name)
        return intef.request() if sendRequest else intef

    def ConsoleSPUopService_CheckAccountListPostApi(self, all_account_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  检查输入的白名单账号是否存在
route: prefix=console-internal acti... """
        """  path: [post]/console-internal/v1/skuop/check_account_list API """
        """  body: 
                {
                    "all_account_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "all_account_results": [
                        {
                            "info": {
                                "account_id": "",
                                "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                                "enterprise_name": ""
                            },
                            "result": 0
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
        intef = collections.interface("spuop", "ConsoleSPUopService_CheckAccountList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("all_account_ids", all_account_ids)
        return intef.request() if sendRequest else intef

    def ConsoleSPUopService_GetSKUFilterGetApi(self, name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取单个SKU设置的白名单
route: prefix=console-internal actio... """
        """  path: [get]/console-internal/v1/skuop/filter API """
        """  params: 
                参数名称：name　类型：string　描述：sku name（sku白名单需要以sku name为关键字）
        """
        """  resp:
                200(A successful response.):
                {
                    "all_accounts": [
                        {
                            "account_id": "",
                            "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                            "enterprise_name": ""
                        }
                    ],
                    "filter_account_type": "[NONE]NONE/PERSION/ENTERPRISE/ALL"
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
        intef = collections.interface("spuop", "ConsoleSPUopService_GetSKUFilter")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("name", name)
        return intef.request() if sendRequest else intef

    def ConsoleSPUopService_SetSKUFilterPostApi(self, name=None, filter_account_type=None, all_account_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  设置单个SKU的白名单
route: prefix=console-internal action=... """
        """  path: [post]/console-internal/v1/skuop/filter API """
        """  body: 
                {
                    "all_account_ids": [],
                    "filter_account_type": "[NONE]NONE/PERSION/ENTERPRISE/ALL",
                    "name": ""
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
        intef = collections.interface("spuop", "ConsoleSPUopService_SetSKUFilter")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("filter_account_type", filter_account_type)
        intef.update_body("all_account_ids", all_account_ids)
        return intef.request() if sendRequest else intef

    def ConsoleSPUopService_GetSPUInfoByPoliceNameGetApi(self, spu_id=None, policy_name=None, spu_code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据spu_id或者policy_name获取SPU数据(bot使用) """
        """  path: [get]/console-internal/v1/spu_info_by_policy_name API """
        """  params: 
                参数名称：spu_id　类型：string　描述：spu id（可选，优先判断）.
                参数名称：policy_name　类型：string　描述：policy name（可选）.
                参数名称：spu_code　类型：string　描述：spu_code（可选）
        """
        """  resp:
                200(A successful response.):
                {
                    "bot_name": "",
                    "device_policy_groups": [],
                    "spu_info": {
                        "categories": [
                            {
                                "created_at": "",
                                "description": "",
                                "id": "",
                                "level": 0,
                                "name": "",
                                "parent_id": "",
                                "path_code": "",
                                "status": "[CATEGORY_UNLIMITED]CATEGORY_UNLIMITED/CATEGORY_USED/CATEGORY_DELETED/CATEGORY_NONE",
                                "updated_at": ""
                            }
                        ],
                        "code": "",
                        "content": {
                            "applications": "",
                            "bill_mode": {
                                "postpaid": "",
                                "prepaid": ""
                            },
                            "description": "",
                            "experience": "",
                            "functions": "",
                            "help_doc": "",
                            "img_url": "",
                            "intro": "",
                            "specifications": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            }
                        },
                        "created_at": "",
                        "id": "",
                        "name": "",
                        "properties": "",
                        "purchase_type": "[PURCHASE_TYPE_UNSPECIFIED]PURCHASE_TYPE_UNSPECIFIED/PURCHASE_TYPE_PUCHASABLE/PURCHASE_TYPE_UNPUCHASABLE",
                        "sell_attr": {
                            "attr": "",
                            "created_at": "",
                            "spu_id": "",
                            "status": "[STATUS_UNLIMITED]STATUS_UNLIMITED/STATUS_VALID/STATUS_INVALID/STATUS_NONE",
                            "updated_at": ""
                        },
                        "specs": [
                            {
                                "created_at": "",
                                "id": "",
                                "key": "",
                                "key_name": "",
                                "spec_values": [
                                    {
                                        "created_at": "",
                                        "id": "",
                                        "spec_id": "",
                                        "status": "[STATUS_UNLIMITED]STATUS_UNLIMITED/STATUS_VALID/STATUS_INVALID/STATUS_NONE",
                                        "updated_at": "",
                                        "value": "",
                                        "value_name": ""
                                    }
                                ],
                                "spu_id": "",
                                "status": "[STATUS_UNLIMITED]STATUS_UNLIMITED/STATUS_VALID/STATUS_INVALID/STATUS_NONE",
                                "updated_at": "",
                                "value_type": "[VALUE_TYPE_UNKNOWN]VALUE_TYPE_UNKNOWN/VALUE_TYPE_STRING/VALUE_TYPE_INTEGER/VALUE_TYPE_DOUBLE"
                            }
                        ],
                        "status": "[STATUS_UNLIMITED]STATUS_UNLIMITED/STATUS_DISABLED/STATUS_ENABLED/STATUS_DELETED/STATUS_NONE",
                        "updated_at": ""
                    },
                    "spu_policy_groups": []
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
        intef = collections.interface("spuop", "ConsoleSPUopService_GetSPUInfoByPoliceName")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("spu_id", spu_id)
        intef.update_params("policy_name", policy_name)
        intef.update_params("spu_code", spu_code)
        return intef.request() if sendRequest else intef

    def ConsoleSPUopService_GetSPUGetApi(self, id=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取单个SPU详情
route: prefix=console-internal action=Ge... """
        """  path: [get]/console-internal/v1/spuop API """
        """  params: 
                参数名称：id　类型：string　描述：spu id.
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
                    "all_infos": [
                        {
                            "customized": false,
                            "filter_account_type": "[NONE]NONE/PERSION/ENTERPRISE/ALL",
                            "id": "",
                            "name": "",
                            "num": 0,
                            "spec_metric": ""
                        }
                    ],
                    "code": "",
                    "id": "",
                    "name": "",
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
        intef = collections.interface("spuop", "ConsoleSPUopService_GetSPU")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

