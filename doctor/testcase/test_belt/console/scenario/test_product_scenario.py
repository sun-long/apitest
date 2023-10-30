#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import datetime
import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestProductScenario(object):
    """ Product scenario test"""

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

    @pytest.mark.ConsoleRegression
    def test_scenario_000_product_info(self, ProductApi):
        """商品"""
        #1.获取所有订阅商品信息
        resp = ProductApi.ConsoleProductService_ListOrderedProductGetApi()
        assert resp.status_code == 200
        mProductsList = resp.json['all_products']
        mProducts = []
        mNums = len(mProductsList)
        for i in range(mNums):
            mProducts.append(resp.json_get('all_products.%d.code' % i))

        #2.获取商品的可购买选项列表信息
        spu_code = mProducts[0]
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code)
        assert resp.status_code == 200

        #3.获取某个商品的实时用量信息
        resp = ProductApi.ConsoleProductService_ListRealtimeUsageByCodeGetApi(spu_code=spu_code)
        assert resp.status_code == 200

        #4.获取某个商品的用量信息
        date_request_start_at = str(datetime.date.today() - datetime.timedelta(days=7)) + "T00:00:00Z"
        date_request_end_at = str(datetime.date.today()-datetime.timedelta(days=1)) + "T00:00:00Z"
        resp = ProductApi.ConsoleProductService_ListUsageByCodeGetApi(spu_code=spu_code,
                                                                      date_request_start_at=date_request_start_at,
                                                                      date_request_end_at=date_request_end_at)
        assert resp.status_code == 200


