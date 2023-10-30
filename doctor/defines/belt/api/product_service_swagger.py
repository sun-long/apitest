#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class ProductSwaggerApi(BaseApi):
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

    def ConsoleProductService_ListProductByCodeGetApi(self, spu_code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取商品的可购买选项列表信息
route: prefix=console action=ListPr... """
        """  path: [get]/console/v1/product API """
        """  params: 
                参数名称：spu_code　类型：string　描述：spu或者spugroup的唯一码
        """
        """  resp:
                200(A successful response.):
                {
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
        intef = collections.interface("product", "ConsoleProductService_ListProductByCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("spu_code", spu_code)
        return intef.request() if sendRequest else intef

    def ConsoleProductService_ListOrderedProductGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有订阅商品信息
route: prefix=console action=ListOrdere... """
        """  path: [get]/console/v1/product/order API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "all_products": [
                        {
                            "code": "",
                            "descriptoin": "",
                            "detailed_charging": "",
                            "id": "",
                            "name": "",
                            "notice": ""
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
        intef = collections.interface("product", "ConsoleProductService_ListOrderedProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleProductService_ListRealtimeUsageByCodeGetApi(self, spu_code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取某个商品的实时用量信息
route: prefix=console action=ListRea... """
        """  path: [get]/console/v1/product/realtime_usage API """
        """  params: 
                参数名称：spu_code　类型：string　描述：spu或者spugroup的唯一码
        """
        """  resp:
                200(A successful response.):
                {
                    "left_count": "",
                    "max_gauge": "",
                    "total_count": ""
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
        intef = collections.interface("product", "ConsoleProductService_ListRealtimeUsageByCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("spu_code", spu_code)
        return intef.request() if sendRequest else intef

    def ConsoleProductService_ListAllSiteGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有计算节点
route: prefix=console action=ListAllSite ... """
        """  path: [get]/console/v1/product/site API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "sites": [
                        {
                            "name": "",
                            "site_id": ""
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
        intef = collections.interface("product", "ConsoleProductService_ListAllSite")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleProductService_ListUsageByCodeGetApi(self, spu_code=None, date_request_start_at=None, date_request_end_at=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取某个商品的用量信息
route: prefix=console action=ListUsage... """
        """  path: [get]/console/v1/product/usage API """
        """  params: 
                参数名称：spu_code　类型：string　描述：spu或者spugroup的唯一码.
                参数名称：date_request.start_at　类型：string　描述：过滤起始时间.
                参数名称：date_request.end_at　类型：string　描述：过滤结束时间
        """
        """  resp:
                200(A successful response.):
                {
                    "all_usages": [
                        {
                            "max_gauge": "",
                            "total_count": "",
                            "usage_time": ""
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
        intef = collections.interface("product", "ConsoleProductService_ListUsageByCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("spu_code", spu_code)
        intef.update_params("date_request.start_at", date_request_start_at)
        intef.update_params("date_request.end_at", date_request_end_at)
        return intef.request() if sendRequest else intef

