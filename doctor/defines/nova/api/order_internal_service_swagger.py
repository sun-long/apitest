#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class Order_internalSwaggerApi(BaseApi):
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

    def NovaOrderInternalService_GetAllSPUGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有spu
route: prefix=console-internal action=GetA... """
        """  path: [get]/console-internal/v1/all_spu API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "all_spus": [
                        {
                            "code": "",
                            "id": "",
                            "name": ""
                        }
                    ]
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
        intef = collections.interface("Order_internal", "NovaOrderInternalService_GetAllSPU")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NovaOrderInternalService_GetAllValuePointGetApi(self, account_id=None, order_id=None, spu_code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有计费点（全部返回，前端分页）
route: prefix=console-internal ... """
        """  path: [get]/console-internal/v1/all_vp API """
        """  params: 
                参数名称：account_id　类型：string　描述：账户筛选，可选
                参数名称：order_id　类型：string　描述：订单筛选，可选
                参数名称：spu_code　类型：string　描述：服务code，可
        """
        """  resp:
                200(A successful response.):
                {
                    "all_vps": [
                        {
                            "account_id": "",
                            "account_name": "",
                            "order_id": "",
                            "order_item_id": "",
                            "price": {
                                "created_at": "",
                                "end_time": "",
                                "id": "",
                                "is_specific": false,
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
                                "sku_id": "",
                                "start_time": "",
                                "status": "[STATUS_UNLIMITED]STATUS_UNLIMITED/STATUS_VALID/STATUS_DELETED/STATUS_NONE",
                                "type": "[TYPE_TIERED]TYPE_TIERED/TYPE_VOLUME/TYPE_STAIR_STEP",
                                "unit": {
                                    "factor": "",
                                    "name": ""
                                },
                                "updated_at": "",
                                "value_point_id": ""
                            },
                            "spu_Id": "",
                            "spu_name": "",
                            "vp_id": "",
                            "vp_name": ""
                        }
                    ]
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
        intef = collections.interface("Order_internal", "NovaOrderInternalService_GetAllValuePoint")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        intef.update_params("order_id", order_id)
        intef.update_params("spu_code", spu_code)
        return intef.request() if sendRequest else intef

    def NovaOrderInternalService_GetValuePointModifyRecordGetApi(self, order_id=None, order_item_id=None, vp_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取订单修改记录
route: prefix=console-internal action=Get... """
        """  path: [get]/console-internal/v1/modify_vp API """
        """  params: 
                参数名称：order_id　类型：string　描述：订单ID
                参数名称：order_item_id　类型：string　描述：订单子项ID
                参数名称：vp_id　类型：string　描述：计费点I
        """
        """  resp:
                200(A successful response.):
                {
                    "all_modify_records": [
                        {
                            "new_prices": [],
                            "op_at": "",
                            "op_user": "",
                            "order_id": "",
                            "order_item_id": "",
                            "remark": "",
                            "vp_id": ""
                        }
                    ],
                    "price": {
                        "created_at": "",
                        "end_time": "",
                        "id": "",
                        "is_specific": false,
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
                        "sku_id": "",
                        "start_time": "",
                        "status": "[STATUS_UNLIMITED]STATUS_UNLIMITED/STATUS_VALID/STATUS_DELETED/STATUS_NONE",
                        "type": "[TYPE_TIERED]TYPE_TIERED/TYPE_VOLUME/TYPE_STAIR_STEP",
                        "unit": {
                            "factor": "",
                            "name": ""
                        },
                        "updated_at": "",
                        "value_point_id": ""
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
        intef = collections.interface("Order_internal", "NovaOrderInternalService_GetValuePointModifyRecord")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("order_id", order_id)
        intef.update_params("order_item_id", order_item_id)
        intef.update_params("vp_id", vp_id)
        return intef.request() if sendRequest else intef

    def NovaOrderInternalService_ModifyValuePointPostApi(self, modify_record=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  修改订单
route: prefix=console-internal action=ModifyV... """
        """  path: [post]/console-internal/v1/modify_vp API """
        """  body: 
                {
                    "modify_record": {
                        "new_prices": [],
                        "op_at": "",
                        "op_user": "",
                        "order_id": "",
                        "order_item_id": "",
                        "remark": "",
                        "vp_id": ""
                    }
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
        intef = collections.interface("Order_internal", "NovaOrderInternalService_ModifyValuePoint")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("modify_record", modify_record)
        return intef.request() if sendRequest else intef

