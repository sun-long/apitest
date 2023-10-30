#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestOplogParam(object):
    """ oplog Param测试"""

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
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
        ('page_request_offset', 'invalidpage_request_offset'),
        ('page_request_offset', ''),
        ('page_request_offset', None),
        ('page_request_limit', 'invalidpage_request_limit'),
        ('page_request_limit', ''),
        ('page_request_limit', None),
        ('page_request_total', 'invalidpage_request_total'),
        ('page_request_total', ''),
        ('page_request_total', None),
    ])
    def test_api_ConsoleOplogService_GetOplogsInvalidParam(self, invalidParam, config_obj, OplogApi):
        """  获取操作记录列表
route: prefix=console-internal action=Get... """
        account_id = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = OplogApi.ConsoleOplogService_GetOplogsGetApi(account_id=account_id, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
        ('service', 'invalidservice'),
        ('service', ''),
        ('service', None),
        ('action', 'invalidaction'),
        ('action', ''),
        ('action', None),
        ('op_user', 'invalidop_user'),
        ('op_user', ''),
        ('op_user', None),
    ])
    def test_api_ConsoleOplogService_CreateOplogInvalidParam(self, invalidParam, config_obj, OplogApi):
        """  增加操作记录
route: prefix=console-internal action=Creat... """
        account_id = None
        service = None
        action = None
        op_user = None
        intef = OplogApi.ConsoleOplogService_CreateOplogPostApi(account_id=account_id, service=service, action=action, op_user=op_user, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
