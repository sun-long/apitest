#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
@pytest.mark.Skiponline
@pytest.mark.ConsoleRegression
class TestOplogScenario(object):
    """ Oplog scenario test"""

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

    def test_scenario_000_getLog(self, config_obj, AuthinternalauthApi, OplogApi):
        """ 开启，关闭后付费，分配商务"""
        # 开启，关闭后付费模式
        account_id = config_obj.Console.User.testConsoleMainUser.accountIdForDisable
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountPostApi(account_id=account_id, update_mode="1", account_used_status=None, payment_type="ACCOUNT_PAYMENT_POSTPAID")
        assert resp.status_code == 200
        time.sleep(30)
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountPostApi(account_id=account_id, update_mode="1", account_used_status=None, payment_type="ACCOUNT_PAYMENT_UNPOSTPAID")
        assert resp.status_code == 200

        # 检查日志
        resp = OplogApi.ConsoleOplogService_GetOplogsGetApi(account_id=account_id, page_request_offset=0, page_request_limit=20, page_request_total=None)
        assert resp.status_code == 200
        assert resp.json_get("all_logs.0.action") == "关闭后付费"
        assert resp.json_get("all_logs.1.action") == "开启后付费"

        # 商务分配

        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminBusinessAssignmentPostApi(account_id=account_id,
                                                                                             business_department="zhaodl department",
                                                                                             business_name="zhaodl",
                                                                                             business_code="123456")
        assert resp.status_code == 200
        resp = OplogApi.ConsoleOplogService_GetOplogsGetApi(account_id=account_id, page_request_offset=0,
                                                            page_request_limit=20, page_request_total=None)
        assert resp.status_code == 200
        assert resp.json_get("all_logs.0.action") == "分配"


