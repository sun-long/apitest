#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from datetime import date, timedelta, datetime, time
import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


@pytest.mark.ConsoleRegression
@pytest.mark.Skiponline
class TestOrderScenario(object):
    """ Order scenario test"""

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

    def test_scenario_000_order_detail(self, OrderApi):
        """ 查看订单详情 """
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
        mOrderIdListOne = resp.json_get('all_orders.0.order_id')
        mAccountIdListOne = resp.json_get('all_orders.0.account_id')
        mCreatedAtListOne = resp.json_get('all_orders.0.created_at')
        mStartAtListOne = resp.json_get('all_orders.0.product_info.all_spus.0.all_skus.0.start_at')
        mEndAtListOne = resp.json_get('all_orders.0.product_info.all_spus.0.all_skus.0.end_at')
        mStatus = resp.json_get('all_orders.0.status')

        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=mOrderIdListOne)
        assert resp.status_code == 200
        assert resp.json_get('order_info.account_id') == mAccountIdListOne
        assert resp.json_get('order_info.created_at') == mCreatedAtListOne
        assert resp.json_get('order_info.product_info.all_spus.0.all_skus.0.start_at') == mStartAtListOne
        assert resp.json_get('order_info.product_info.all_spus.0.all_skus.0.end_at') == mEndAtListOne
        assert resp.json_get('order_info.status') == mStatus

    @pytest.mark.skip("在user 场景用例里面已实现")
    def test_scenario_001_order_Prepaid_createOrder(self, OrderApi):
        """ 创建预付费订单 """
        # 0 查看有无该类型订单
        # 1 有该类型订单，退订，后创建-2
        # 2 无该类型订单，创建，预付费/后付费
        # 3 创建后拿order_id, created_at
        # 4 搜索查订单列表，有此订单，预付费-支付成功，后付费-待审核
        # 5 预付费-查看详情-对细节
        # 6 后付费-查看详情-对待审核的细节
        # 7 后付费-内部订单审核成功-查看详情-对审核成功的细节
        # 8 后付费-内部订单审核不通过-查看详情-对审核不通过的细节
        # 9 查看用量
        all_items = [{"sku_id": "161097230663580123", "count": 1, "site_id": "157004481618262811"}]
        resp = OrderApi.ConsoleOrderService_CreateOrderPostApi(all_items=all_items)
        assert resp.status_code == 200
        assert resp.json_get('flag') == 2
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
        mOrderIdListOne = resp.json_get('all_orders.0.order_id')
        mAccountIdListOne = resp.json_get('all_orders.0.account_id')
        mCreatedAtListOne = resp.json_get('all_orders.0.created_at')
        mStartAtListOne = resp.json_get('all_orders.0.product_info.all_spus.0.all_skus.0.start_at')
        mEndAtListOne = resp.json_get('all_orders.0.product_info.all_spus.0.all_skus.0.end_at')
        mStatus = resp.json_get('all_orders.0.status')

        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=mOrderIdListOne)
        assert resp.status_code == 200
        assert resp.json_get('order_info.account_id') == mAccountIdListOne
        assert resp.json_get('order_info.created_at') == mCreatedAtListOne
        assert resp.json_get('order_info.product_info.all_spus.0.all_skus.0.start_at') == mStartAtListOne
        assert resp.json_get('order_info.product_info.all_spus.0.all_skus.0.end_at') == mEndAtListOne
        assert resp.json_get('order_info.status') == mStatus

    @pytest.mark.skip("在user 场景用例里面已实现")
    def test_scenario_002_order_Postpaid_createOrder(self, OrderApi):
        """ 创建后付费订单 """
        # 0 查看有无该类型订单
        # 1 有该类型订单，退订，后创建-2
        # 2 无该类型订单，创建，预付费/后付费
        # 3 创建后拿order_id, created_at
        # 4 搜索查订单列表，有此订单，预付费-支付成功，后付费-待审核
        # 5 预付费-查看详情-对细节
        # 6 后付费-查看详情-对待审核的细节
        # 7 后付费-内部订单审核成功-查看详情-对审核成功的细节
        # 8 后付费-内部订单审核不通过-查看详情-对审核不通过的细节
        # 9 查看用量
        all_items = [{"sku_id": "160673316217059806", "count": 1, "site_id": "157004481618262811"}]
        resp = OrderApi.ConsoleOrderService_CreateOrderPostApi(all_items=all_items)
        assert resp.status_code == 200
        assert resp.json_get('flag') == 2
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
        mOrderIdListOne = resp.json_get('all_orders.0.order_id')
        mAccountIdListOne = resp.json_get('all_orders.0.account_id')
        mCreatedAtListOne = resp.json_get('all_orders.0.created_at')
        mStartAtListOne = resp.json_get('all_orders.0.product_info.all_spus.0.all_skus.0.start_at')
        mEndAtListOne = resp.json_get('all_orders.0.product_info.all_spus.0.all_skus.0.end_at')
        mStatus = resp.json_get('all_orders.0.status')

        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=mOrderIdListOne)
        assert resp.status_code == 200
        assert resp.json_get('order_info.account_id') == mAccountIdListOne
        assert resp.json_get('order_info.created_at') == mCreatedAtListOne
        assert resp.json_get('order_info.product_info.all_spus.0.all_skus.0.start_at') == mStartAtListOne
        assert resp.json_get('order_info.product_info.all_spus.0.all_skus.0.end_at') == mEndAtListOne
        assert resp.json_get('order_info.status') == mStatus


    def test_scenario_003_freeOrder(self, config_obj, loginTokenFreeOrder, OrderApi):
        """ 订阅免费的sku，可以发送免费的sku订单"""
        # 获取免费的sku订单
        resp = OrderApi.ConsoleOrderService_GetAllOrderGetApi(status=None, date_request_start_at=None,
                                                              date_request_end_at=None, page_request_offset=0,
                                                              page_request_limit=20, page_request_total=10,
                                                              created_sort_type=None, loginToken=loginTokenFreeOrder)
        num = len(resp.json_get("all_orders"))
        if config_obj.Console.User.testConsoleMainUser.freeOrderPeriod == "0":
            """ test env 每天发送一个免费的订单"""
            created_at = str(date.today() - timedelta(days=1))
            print('created_at123 {}'.format(created_at))

            skuId = None
            n = 0
            for i in range(num):
                if resp.json["all_orders"][i]["product_info"]["all_spus"][0]["all_skus"][0][
                    "id"] == config_obj.Console.User.testConsoleMainUser.skuIdforFree and resp.json["all_orders"][i][
                                                                                              "created_at"][
                                                                                          :10] == created_at:
                    n = n + 1
                    assert n == 1
                    print('++n {}'.format(n))
                    skuId = config_obj.Console.User.testConsoleMainUser.skuIdforFree

            assert skuId == config_obj.Console.User.testConsoleMainUser.skuIdforFree

        elif config_obj.Console.User.testConsoleMainUser.freeOrderPeriod == "1":
            """ staging env 每个月发送一个免费的订单"""
            given_date = datetime.today().date()
            print('今天的日期： ', given_date)
            # 获取当月的第一天
            first_day_of_month = given_date.replace(day=1)

            print("\nFirst day of month: ", first_day_of_month, "\n")

            today = date.today()
            last_day_of_last_month = d = date(today.year, today.month, 1) - timedelta(1)
            print("\nFirst last_day: ", last_day_of_last_month, "\n")
            last_day_of_last_month1 = last_day_of_last_month.strftime('%Y-%m-%d')
            print("\nFirst last_day1: ", last_day_of_last_month1, "\n")


            skuId = None
            n = 0
            for i in range(num):
                if resp.json["all_orders"][i]["product_info"]["all_spus"][0]["all_skus"][0][
                    "id"] == config_obj.Console.User.testConsoleMainUser.skuIdforFree and resp.json["all_orders"][i][
                                                                                              "created_at"][
                                                                                          :10] == last_day_of_last_month1:
                    n = n + 1
                    assert n == 1
                    skuId = config_obj.Console.User.testConsoleMainUser.skuIdforFree
                    print("\n skuId First day of month: ", skuId, "\n")

            assert skuId == config_obj.Console.User.testConsoleMainUser.skuIdforFree
