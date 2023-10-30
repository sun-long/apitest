#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestProductApi(object):
    """ product Api测试"""

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
    def test_api_ConsoleProductService_ListProductByCode(self, config_obj, ProductApi):
        """  获取商品的可购买选项列表信息
route: prefix=console action=ListPr... """
        spu_code = "FallDetection"
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_api_ConsoleProductService_ListOrderedProduct(self, config_obj, ProductApi):
        """  获取所有订阅商品信息
route: prefix=console action=ListOrdere... """
        resp = ProductApi.ConsoleProductService_ListOrderedProductGetApi()
        assert resp.status_code == 200

    @pytest.mark.skip("post接口在场景用例中实现")
    def test_api_ConsoleProductService_ListRealtimeUsageByCode(self, config_obj, ProductApi):
        """  获取某个商品的实时用量信息
route: prefix=console action=ListRea... """
        spu_code = "FallDetection"
        resp = ProductApi.ConsoleProductService_ListRealtimeUsageByCodeGetApi(spu_code=spu_code)
        assert resp.status_code == 200

    @pytest.mark.skip("接口不对外")
    def test_api_ConsoleProductService_ListAllSite(self, config_obj, ProductApi):
        """  获取所有计算节点
route: prefix=console action=ListAllSite ... """
        resp = ProductApi.ConsoleProductService_ListAllSiteGetApi()
        assert resp.status_code == 200

    @pytest.mark.skip("post接口在场景用例中实现")
    def test_api_ConsoleProductService_ListUsageByCode(self, config_obj, ProductApi):
        """  获取某个商品的用量信息
route: prefix=console action=ListUsage... """
        spu_code = "FallDetection"
        date_request_start_at = "2023-02-13T16:00:00Z"
        date_request_end_at = "2023-02-19T16:00:00Z"
        resp = ProductApi.ConsoleProductService_ListUsageByCodeGetApi(spu_code=spu_code, date_request_start_at=date_request_start_at, date_request_end_at=date_request_end_at)
        assert resp.status_code == 200
