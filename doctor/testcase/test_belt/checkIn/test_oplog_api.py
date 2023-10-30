#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


@pytest.mark.checkin
class TestOplogApi(object):
    """ oplog Api测试"""

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

    def test_api_ConsoleOplogService_GetOplogs(self, config_obj, OplogApi):
        """  获取操作记录列表
route: prefix=console-internal action=Get... """
        account_id = config_obj.Console.User.internalTestUser.account_id
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = None
        resp = OplogApi.ConsoleOplogService_GetOplogsGetApi(account_id=account_id, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleOplogService_CreateOplog(self, config_obj, OplogApi):
        """  增加操作记录
route: prefix=console-internal action=Creat... """
        account_id = None
        service = None
        action = None
        op_user = None
        resp = OplogApi.ConsoleOplogService_CreateOplogPostApi(account_id=account_id, service=service, action=action, op_user=op_user)
        assert resp.status_code == 200
