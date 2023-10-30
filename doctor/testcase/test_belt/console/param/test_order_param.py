#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestOrderParam(object):
    """ order Param测试"""

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

    @pytest.mark.parametrize("invalidParam", [
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
        ('date_request_start_at', 'invaliddate_request_start_at'),
        ('date_request_start_at', ''),
        ('date_request_start_at', None),
        ('date_request_end_at', 'invaliddate_request_end_at'),
        ('date_request_end_at', ''),
        ('date_request_end_at', None),
        ('page_request_offset', 'invalidpage_request_offset'),
        ('page_request_offset', ''),
        ('page_request_offset', None),
        ('page_request_limit', 'invalidpage_request_limit'),
        ('page_request_limit', ''),
        ('page_request_limit', None),
        ('page_request_total', 'invalidpage_request_total'),
        ('page_request_total', ''),
        ('page_request_total', None),
        ('created_sort_type', 'invalidcreated_sort_type'),
        ('created_sort_type', ''),
        ('created_sort_type', None),
    ])
    def test_api_ConsoleOrderService_GetAllOrderInvalidParam(self, invalidParam, config_obj, OrderApi):
        """  获取所有订单
route: prefix=console action=GetAllOrder ve... """
        status = None
        date_request_start_at = None
        date_request_end_at = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        created_sort_type = None
        intef = OrderApi.ConsoleOrderService_GetAllOrderGetApi(status=status, date_request_start_at=date_request_start_at, date_request_end_at=date_request_end_at, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, created_sort_type=created_sort_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('order_id', 'invalidorder_id'),
        ('order_id', ''),
        ('order_id', None),
    ])
    def test_api_ConsoleOrderService_GetOneOrderInvalidParam(self, invalidParam, config_obj, OrderApi):
        """  按order_id获取订单详情
route: prefix=console action=GetOn... """
        order_id = None
        intef = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=order_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('all_items', 'invalidall_items'),
        ('all_items', ''),
        ('all_items', None),
    ])
    def test_api_ConsoleOrderService_CreateOrderInvalidParam(self, invalidParam, config_obj, OrderApi):
        """  创建订单
route: prefix=console action=CreateOrder vers... """
        all_items = None
        intef = OrderApi.ConsoleOrderService_CreateOrderPostApi(all_items=all_items, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
    ])
    def test_api_ConsoleOrderService_GetOrderNumInvalidParam(self, invalidParam, config_obj, OrderApi):
        """  获取订单数目
route: prefix=console action=GetOrderNum ve... """
        status = None
        intef = OrderApi.ConsoleOrderService_GetOrderNumGetApi(status=status, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200
