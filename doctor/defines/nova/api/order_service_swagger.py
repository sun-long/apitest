#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


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

    def NovaOrderService_CreateOrderPostApi(self, all_items=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建订单
route: prefix=console action=CreateOrder vers... """
        """  path: [post]/console/v1/order API """
        """  body: 
                {
                    "all_items": [
                        {
                            "count": "",
                            "sku_id": ""
                        }
                    ]
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "flag": 0,
                    "order_id": ""
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
        intef = collections.interface("Order", "NovaOrderService_CreateOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("all_items", all_items)
        return intef.request() if sendRequest else intef

    def NovaOrderService_CreateOrderByCodePostApi(self, all_items=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据spu名称创建订单
route: prefix=console action=CreateOrd... """
        """  path: [post]/console/v1/order_by_name API """
        """  body: 
                {
                    "all_items": [
                        {
                            "code": "",
                            "count": ""
                        }
                    ]
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "flag": 0,
                    "order_id": ""
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
        intef = collections.interface("Order", "NovaOrderService_CreateOrderByCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("all_items", all_items)
        return intef.request() if sendRequest else intef

    def NovaOrderService_UnsubscribeOrderPostApi(self, order_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后付费订单退订
route: prefix=console action=UnsubscribeOr... """
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("Order", "NovaOrderService_UnsubscribeOrder")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("order_id", order_id)
        return intef.request() if sendRequest else intef

    def NovaOrderService_UnsubscribeOrderByCodePostApi(self, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据spu名称退订
route: prefix=console action=Unsubscribe... """
        """  path: [post]/console/v1/unsubscribe_order_by_name API """
        """  body: 
                {
                    "code": ""
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
        intef = collections.interface("Order", "NovaOrderService_UnsubscribeOrderByCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

