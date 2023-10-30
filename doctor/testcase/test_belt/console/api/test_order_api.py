#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestOrderApi(object):
    """ order Api测试"""

    @pytest.fixture(scope="class", autouse=True)
    def init_func(self, config_obj):
        # 初始化测试集
        # 所有test运行前运行一次，接收外部参数env_obj，初始化测试环境
        log().info("==========%s测试开始==========" % self.__class__.__name__)

    def teardown_class(self):
        # 所有test运行完后运行一次
        log().info("==========%s测试结束==========\n" % self.__name__)
        log().info("clear tasks finish")

    def setup_method(self, method):
        # 每个测试用例执行之前做操作
        log().info("用例%s开始" % method.__name__)

    def teardown_method(self, method):
        # 每个测试用例执行之后做操作
        log().info("用例%s结束" % method.__name__)

    def test_api_ConsoleOrderService_GetAllOrder(self, config_obj, OrderApi):
        """  获取所有订单 """
        status = None
        date_request_start_at = None
        date_request_end_at = None
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = 100
        created_sort_type = None
        resp = OrderApi.ConsoleOrderService_GetAllOrderGetApi(status=status,
                                                              date_request_start_at=date_request_start_at,
                                                              date_request_end_at=date_request_end_at,
                                                              page_request_offset=page_request_offset,
                                                              page_request_limit=page_request_limit,
                                                              page_request_total=page_request_total,
                                                              created_sort_type=created_sort_type)
        assert resp.status_code == 200

    def test_api_ConsoleOrderService_GetOneOrder(self, config_obj, OrderApi):
        """  按order_id获取订单详情 """
        order_id = None
        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=order_id)
        assert resp.status_code == 200

    @pytest.mark.skip("退订用例暂不执行")
    def test_api_ConsoleOrderService_CreatePayPostOrder(self, config_obj, OrderApi, ProductApi):
        """  创建订单 """
        #后付费-银行卡
        spu_code = "OCRBankcard"
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code)
        n = len(resp.json_get("all_spus.0.all_skus"))
        for i in range(n):
            if(resp.json["all_spus"][0]["all_skus"][i]["bill_mode"]=="PAY_TYPE_POST"):
                #后付费
                payPostSkuId = resp.json["all_spus"][0]["all_skus"][i]["all_prices"][0]["sku_id"]
                payPostSkuSiteId = resp.json["all_spus"][0]["all_skus"][i]["sites"][0]["site_id"]
                break

        #创建后付费订单
        all_items = [{"sku_id": payPostSkuId, "count": "1", "site_id": payPostSkuSiteId}]
        resp = OrderApi.ConsoleOrderService_CreateOrderPostApi(all_items=all_items)
        assert resp.status_code == 200
        m_order_id = resp.json_get("order_info.order_id")

        #退订订单
        resp = OrderApi.ConsoleOrderService_UnsubscribeOrderPostApi(order_id=m_order_id)
        assert resp.status_code == 200

    def test_api_ConsoleOrderService_CreatePayPreOrder(self, config_obj, OrderApi, ProductApi):
        """  创建订单 """
        # 预付费-银行卡
        spu_code = "OCRBankcard"
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code)
        n = len(resp.json_get("all_spus.0.all_skus"))
        for i in range(n):
            if (resp.json["all_spus"][0]["all_skus"][i]["bill_mode"] == "PAY_TYPE_PRE"):
                # 后付费
                payPreSkuId = resp.json["all_spus"][0]["all_skus"][i]["all_prices"][0]["sku_id"]
                payPreSkuSiteId = resp.json["all_spus"][0]["all_skus"][i]["sites"][0]["site_id"]
                break

        # 创建预付费订单
        all_items = [{"sku_id": payPreSkuId, "count": "1", "site_id": payPreSkuSiteId}]
        resp = OrderApi.ConsoleOrderService_CreateOrderPostApi(all_items=all_items)
        assert resp.status_code == 200


    def test_api_ConsoleOrderService_GetOrderNum(self, config_obj, OrderApi):
        """  获取订单数目 """
        status = None
        resp = OrderApi.ConsoleOrderService_GetOrderNumGetApi(status=status)
        assert resp.status_code == 200

    @pytest.mark.skip("退订用例暂不执行")
    def test_api_ConsoleOrderService_UnsubscribeOrder(self, config_obj, OrderApi):
        """  后付费订单退订（beta1版本新增） """
        order_id = None
        resp = OrderApi.ConsoleOrderService_UnsubscribeOrderPostApi(order_id=order_id)
        assert resp.status_code == 200

    def test_api_ConsoleOrderService_GetValidOrderNum(self, config_obj, OrderApi):
        """  获取有效的后付费订单和非0元预付费订单数目 """
        resp = OrderApi.ConsoleOrderService_GetValidOrderNumGetApi()
        assert resp.status_code == 200
