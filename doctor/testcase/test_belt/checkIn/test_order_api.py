#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.checkin
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
        """  获取所有订单"""
        status = None
        date_request_start_at = None
        date_request_end_at = None
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = 100
        created_sort_type = None
        resp = OrderApi.ConsoleOrderService_GetAllOrderGetApi(status=status, date_request_start_at=date_request_start_at, date_request_end_at=date_request_end_at, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, created_sort_type=created_sort_type)
        assert resp.status_code == 200

    def test_api_ConsoleOrderService_GetOneOrder(self, config_obj, OrderApi):
        """  按order_id获取订单详情"""
        resp = OrderApi.ConsoleOrderService_GetAllOrderGetApi(page_request_offset=0,
                                                              page_request_limit=100,
                                                              page_request_total=100,)

        order_id = resp.json_get("all_orders.0.order_id")
        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=order_id)
        assert resp.status_code == 200

    def test_api_ConsoleOrderService_GetOrderNum(self, config_obj, OrderApi):
        """  获取订单数目 """
        status = None
        resp = OrderApi.ConsoleOrderService_GetOrderNumGetApi(status=status)
        assert resp.status_code == 200

    def test_api_ConsoleOrderService_GetValidOrderNum(self, config_obj, OrderApi):
        """  获取有效的后付费订单和非0元预付费订单数目 """
        resp = OrderApi.ConsoleOrderService_GetValidOrderNumGetApi()
        assert resp.status_code == 200
