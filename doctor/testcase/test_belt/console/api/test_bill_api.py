#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import datetime

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestBillApi(object):
    """ bill Api测试"""

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
    def test_api_ConsoleBillService_GetAllBillGroup(self, config_obj, BillApi):
        """  获取所有账期账单 """
        date_request_start_at = str(datetime.date.today() - datetime.timedelta(days=31)) + "T00:00:00Z"
        date_request_end_at = str(datetime.date.today()-datetime.timedelta(days=1)) + "T00:00:00Z"
        resp = BillApi.ConsoleBillService_GetAllBillGroupGetApi(date_request_start_at=date_request_start_at, date_request_end_at=date_request_end_at)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口在场景用例中实现")
    def test_api_ConsoleBillService_GetOneBillGroup(self, config_obj, BillApi):
        """  获取单个账期账单详情 """
        create_at = None
        resp = BillApi.ConsoleBillService_GetOneBillGroupGetApi(create_at=create_at)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_api_ConsoleBillService_GetBillNum(self, config_obj, BillApi):
        """  按状态获取账单数 """
        resp = BillApi.ConsoleBillService_GetBillNumGetApi()
        assert resp.status_code == 200

    @pytest.mark.skip("post接口在场景用例中实现")
    def test_api_ConsoleBillService_DownloadBillDetail(self, config_obj, BillApi):
        """  账单明细（ga版本新增） """
        create_at = None
        resp = BillApi.ConsoleBillService_DownloadBillDetailPostApi(create_at=create_at)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口在场景用例中实现")
    def test_api_ConsoleBillService_UpdateBillStatus(self, config_obj, BillApi):
        """  更新账期账单状态 """
        create_at = None
        account_status = None
        resp = BillApi.ConsoleBillService_UpdateBillStatusPostApi(create_at=create_at, account_status=account_status)
        assert resp.status_code == 200
