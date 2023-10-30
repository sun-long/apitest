#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestBillinternalParam(object):
    """ billInternal Param测试"""

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
        ('create_at', 'invalidcreate_at'),
        ('create_at', ''),
        ('create_at', None),
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('user_name', 'invaliduser_name'),
        ('user_name', ''),
        ('user_name', None),
        ('enterprise_name', 'invalidenterprise_name'),
        ('enterprise_name', ''),
        ('enterprise_name', None),
        ('page_request_limit', 'invalidpage_request_limit'),
        ('page_request_limit', ''),
        ('page_request_limit', None),
        ('page_request_marker', 'invalidpage_request_marker'),
        ('page_request_marker', ''),
        ('page_request_marker', None),
    ])
    def test_api_ConsoleInternalBillService_GetInternalAllBillInvalidParam(self, invalidParam, config_obj, BillinternalApi):
        """  获取所有账单
route: prefix=console-internal action=GetIn... """
        create_at = None
        account_id = None
        user_id = None
        user_name = None
        enterprise_name = None
        page_request_limit = None
        page_request_marker = None
        intef = BillinternalApi.ConsoleInternalBillService_GetInternalAllBillGetApi(create_at=create_at, account_id=account_id, user_id=user_id, user_name=user_name, enterprise_name=enterprise_name, page_request_limit=page_request_limit, page_request_marker=page_request_marker, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('create_at', 'invalidcreate_at'),
        ('create_at', ''),
        ('create_at', None),
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
        ('op_user', 'invalidop_user'),
        ('op_user', ''),
        ('op_user', None),
    ])
    def test_api_ConsoleInternalBillService_GetInternalOneBillInvalidParam(self, invalidParam, config_obj, BillinternalApi):
        """  获取单个账单详情
route: prefix=console-internal action=Get... """
        create_at = None
        account_id = None
        op_user = None
        intef = BillinternalApi.ConsoleInternalBillService_GetInternalOneBillGetApi(create_at=create_at, account_id=account_id, op_user=op_user, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('create_at', 'invalidcreate_at'),
        ('create_at', ''),
        ('create_at', None),
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
        ('account_status', 'invalidaccount_status'),
        ('account_status', ''),
        ('account_status', None),
    ])
    def test_api_ConsoleInternalBillService_UpdateInternalBillStatusInvalidParam(self, invalidParam, config_obj, BillinternalApi):
        """  更新账单状态
route: prefix=console-internal action=Updat... """
        create_at = None
        account_id = None
        account_status = None
        intef = BillinternalApi.ConsoleInternalBillService_UpdateInternalBillStatusPostApi(create_at=create_at, account_id=account_id, account_status=account_status, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('create_at', 'invalidcreate_at'),
        ('create_at', ''),
        ('create_at', None),
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
    ])
    def test_api_ConsoleInternalBillService_DownloadBillDetailInvalidParam(self, invalidParam, config_obj, BillinternalApi):
        """  账单明细
route: prefix=console-internal action=Downloa... """
        create_at = None
        account_id = None
        intef = BillinternalApi.ConsoleInternalBillService_DownloadBillDetailPostApi(create_at=create_at, account_id=account_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('create_at', 'invalidcreate_at'),
        ('create_at', ''),
        ('create_at', None),
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
    ])
    def test_api_ConsoleInternalBillService_SendInternalBillInvalidParam(self, invalidParam, config_obj, BillinternalApi):
        """  发送账单
route: prefix=console-internal action=SendInt... """
        create_at = None
        account_id = None
        intef = BillinternalApi.ConsoleInternalBillService_SendInternalBillPostApi(create_at=create_at, account_id=account_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
