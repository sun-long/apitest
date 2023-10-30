#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.order_service_swagger import OrderSwaggerApi


"""
使用说明：


"""


class OrderSwaggerBusiness(OrderSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(OrderSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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
        inte_obj.set_headers("X-Belt-Version", "v1")
        if inte_obj.path == '/console/v1/all_order':
            inte_obj.set_headers('X-Belt-Action', 'GetAllOrder')
        elif inte_obj.path == '/console/v1/order':
            if inte_obj.method == "get":
                inte_obj.set_headers('X-Belt-Action', 'GetOneOrder')
                inte_obj.set_headers('X-Belt-Version', 'v1')
            if inte_obj.method == "post":
                inte_obj.set_headers('X-Belt-Action', 'CreateOrder')
                inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/order_num':
            inte_obj.set_headers('X-Belt-Action', 'GetOrderNum')

        elif inte_obj.path == '/console/v1/valid_order_num':
            inte_obj.set_headers('X-Belt-Action', 'GetValidOrderNum')
        elif inte_obj.path == '/console/v1/unsubscribe_order':
            inte_obj.set_headers('X-Belt-Action', 'UnsubscribeOrder')
        elif inte_obj.path == '/console/v1/valid_order_num':
            inte_obj.set_headers('X-Belt-Action', 'GetValidOrderNum')


    def CreatePostPayOrder(self, spu_code , ProductApi, loginToken):
        """  创建后付费订单 """
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code, loginToken=loginToken)
        n = len(resp.json_get("all_spus.0.all_skus"))
        for i in range(n):
            if(resp.json["all_spus"][0]["all_skus"][i]["bill_mode"]=="PAY_TYPE_POST"):
                #后付费
                payPostSkuId = resp.json["all_spus"][0]["all_skus"][i]["all_prices"][0]["sku_id"]
                payPostSkuSiteId = resp.json["all_spus"][0]["all_skus"][i]["sites"][0]["site_id"]
                break

        #创建后付费订单
        all_items = [{"sku_id": payPostSkuId, "count": "1", "site_id": payPostSkuSiteId}]
        resp = self.ConsoleOrderService_CreateOrderPostApi(all_items=all_items, loginToken=loginToken)
        return resp


    def CreatePrePayOrder(self, spu_code, ProductApi, loginToken):
        """  创建预付费订单 """
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code, loginToken=loginToken)
        n = len(resp.json_get("all_spus.0.all_skus"))
        for i in range(n):
            if (resp.json["all_spus"][0]["all_skus"][i]["bill_mode"] == "PAY_TYPE_PRE"):
                # 预付费
                payPreSkuId = resp.json["all_spus"][0]["all_skus"][i]["all_prices"][0]["sku_id"]
                payPreSkuSiteId = resp.json["all_spus"][0]["all_skus"][i]["sites"][0]["site_id"]
                break

        # 创建预付费订单
        all_items = [{"sku_id": payPreSkuId, "count": "1", "site_id": payPreSkuSiteId}]
        resp = self.ConsoleOrderService_CreateOrderPostApi(all_items=all_items, loginToken=loginToken)
        return resp



