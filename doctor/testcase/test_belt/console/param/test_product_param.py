#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestProductParam(object):
    """ product Param测试"""

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
        ('spu_code', 'invalidspu_code'),
        ('spu_code', ''),
        ('spu_code', None),
    ])
    def test_api_ConsoleProductService_ListProductByCodeInvalidParam(self, invalidParam, config_obj, ProductApi):
        """  获取商品的可购买选项列表信息
route: prefix=console action=ListPr... """
        spu_code = None
        intef = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ConsoleProductService_ListOrderedProductInvalidParam(self, invalidParam, config_obj, ProductApi):
        """  获取所有订阅商品信息
route: prefix=console action=ListOrdere... """
        intef = ProductApi.ConsoleProductService_ListOrderedProductGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('spu_code', 'invalidspu_code'),
        ('spu_code', ''),
        ('spu_code', None),
        ('date_request_start_at', 'invaliddate_request_start_at'),
        ('date_request_start_at', ''),
        ('date_request_start_at', None),
        ('date_request_end_at', 'invaliddate_request_end_at'),
        ('date_request_end_at', ''),
        ('date_request_end_at', None),
    ])
    def test_api_ConsoleProductService_ListUsageByCodeInvalidParam(self, invalidParam, config_obj, ProductApi):
        """  获取某个商品的用量信息
route: prefix=console action=ListUsage... """
        spu_code = None
        date_request_start_at = None
        date_request_end_at = None
        intef = ProductApi.ConsoleProductService_ListUsageByCodeGetApi(spu_code=spu_code, date_request_start_at=date_request_start_at, date_request_end_at=date_request_end_at, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200
