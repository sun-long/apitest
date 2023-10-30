#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestAuthinternalauthParam(object):
    """ authInternalAuth Param测试"""

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
        ('account_name', 'invalidaccount_name'),
        ('account_name', ''),
        ('account_name', None),
        ('account_type', 'invalidaccount_type'),
        ('account_type', ''),
        ('account_type', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('enterprise_name', 'invalidenterprise_name'),
        ('enterprise_name', ''),
        ('enterprise_name', None),
        ('order', 'invalidorder'),
        ('order', ''),
        ('order', None),
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
    def test_api_ConsoleInternalAuthService_AdminGetAccountListInvalidParam(self, invalidParam, config_obj, AuthinternamlauthApi):
        """  超级管理员获取账户列表
route: prefix=console-internal action=... """
        account_name = None
        account_type = None
        status = None
        account_id = None
        user_id = None
        enterprise_name = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = AuthinternamlauthApi.ConsoleInternalAuthService_AdminGetAccountListGetApi(account_name=account_name, account_type=account_type, status=status, account_id=account_id, user_id=user_id, enterprise_name=enterprise_name, order=order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
        ('update_mode', 'invalidupdate_mode'),
        ('update_mode', ''),
        ('update_mode', None),
        ('account_used_status', 'invalidaccount_used_status'),
        ('account_used_status', ''),
        ('account_used_status', None),
        ('payment_type', 'invalidpayment_type'),
        ('payment_type', ''),
        ('payment_type', None),
    ])
    def test_api_ConsoleInternalAuthService_AdminUpdateAccountInvalidParam(self, invalidParam, config_obj, AuthinternamlauthApi):
        """  超级管理员更新付费模式、账户的启用和禁用状态
route: prefix=console-inter... """
        account_id = None
        update_mode = None
        account_used_status = None
        payment_type = None
        intef = AuthinternamlauthApi.ConsoleInternalAuthService_AdminUpdateAccountPostApi(account_id=account_id, update_mode=update_mode, account_used_status=account_used_status, payment_type=payment_type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
    ])
    def test_api_ConsoleInternalAuthService_AdminGetEnterpriseAccountInvalidParam(self, invalidParam, config_obj, AuthinternamlauthApi):
        """  超级管理员获取单账号审核认证数据
route: prefix=console-internal ac... """
        account_id = None
        intef = AuthinternamlauthApi.ConsoleInternalAuthService_AdminGetEnterpriseAccountGetApi(account_id=account_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
        ('audit_at', 'invalidaudit_at'),
        ('audit_at', ''),
        ('audit_at', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
        ('audit_desc', 'invalidaudit_desc'),
        ('audit_desc', ''),
        ('audit_desc', None),
    ])
    def test_api_ConsoleInternalAuthService_AdminUpdateAccountStatusInvalidParam(self, invalidParam, config_obj, AuthinternamlauthApi):
        """  超级管理员认证审核
route: prefix=console-internal action=Ad... """
        account_id = None
        audit_at = None
        status = None
        audit_desc = None
        intef = AuthinternamlauthApi.ConsoleInternalAuthService_AdminUpdateAccountStatusPostApi(account_id=account_id, audit_at=audit_at, status=status, audit_desc=audit_desc, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
        ('business_department', 'invalidbusiness_department'),
        ('business_department', ''),
        ('business_department', None),
        ('business_name', 'invalidbusiness_name'),
        ('business_name', ''),
        ('business_name', None),
        ('business_code', 'invalidbusiness_code'),
        ('business_code', ''),
        ('business_code', None),
    ])
    def test_api_ConsoleInternalAuthService_AdminBusinessAssignmentInvalidParam(self, invalidParam, config_obj, AuthinternamlauthApi):
        """  超级管理员分配商务
route: prefix=console-internal action=Ad... """
        account_id = None
        business_department = None
        business_name = None
        business_code = None
        intef = AuthinternamlauthApi.ConsoleInternalAuthService_AdminBusinessAssignmentPostApi(account_id=account_id, business_department=business_department, business_name=business_name, business_code=business_code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
