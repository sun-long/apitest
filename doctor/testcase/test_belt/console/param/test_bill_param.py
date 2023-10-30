#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestBillParam(object):
    """ bill Param测试"""

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
        ('date_request_start_at', 'invaliddate_request_start_at'),
        ('date_request_start_at', ''),
        ('date_request_start_at', None),
        ('date_request_end_at', 'invaliddate_request_end_at'),
        ('date_request_end_at', ''),
        ('date_request_end_at', None),
    ])
    def test_api_ConsoleBillService_GetAllBillGroupInvalidParam(self, invalidParam, config_obj, BillApi):
        """  获取所有账期账单
route: prefix=console action=GetAllBillGr... """
        date_request_start_at = None
        date_request_end_at = None
        intef = BillApi.ConsoleBillService_GetAllBillGroupGetApi(date_request_start_at=date_request_start_at, date_request_end_at=date_request_end_at, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('create_at', 'invalidcreate_at'),
        ('create_at', ''),
        ('create_at', None),
    ])
    def test_api_ConsoleBillService_GetOneBillGroupInvalidParam(self, invalidParam, config_obj, BillApi):
        """  获取单个账期账单详情
route: prefix=console action=GetOneBill... """
        create_at = None
        intef = BillApi.ConsoleBillService_GetOneBillGroupGetApi(create_at=create_at, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ConsoleBillService_GetBillNumInvalidParam(self, invalidParam, config_obj, BillApi):
        """  按状态获取账单数
route: prefix=console action=GetBillNum v... """
        intef = BillApi.ConsoleBillService_GetBillNumGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('create_at', 'invalidcreate_at'),
        ('create_at', ''),
        ('create_at', None),
        ('account_status', 'invalidaccount_status'),
        ('account_status', ''),
        ('account_status', None),
    ])
    def test_api_ConsoleBillService_UpdateBillStatusInvalidParam(self, invalidParam, config_obj, BillApi):
        """  更新账期账单状态
route: prefix=console action=UpdateBillSt... """
        create_at = None
        account_status = None
        intef = BillApi.ConsoleBillService_UpdateBillStatusPostApi(create_at=create_at, account_status=account_status, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
