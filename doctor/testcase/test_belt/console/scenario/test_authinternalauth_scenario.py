#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.Skiponline
class TestAuthinternalauthScenario(object):
    """ Authinternalauth scenario test"""

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
    def test_scenario_000_AdminUpdateAccount_PaymentType(self, config_obj, AuthEnterpriseApi, AuthinternalauthApi):
        """ 超级管理员更新付费模式"""
        # 1、查看账户信息
        account_name = None
        account_type = None
        status = None
        business_status = None
        account_id = config_obj.Console.User.testEnterprise.account_id
        user_id = None
        user_name = None
        enterprise_name = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetAccountListGetApi(account_name=account_name,
                                                                                        account_type=account_type,
                                                                                        status=status,
                                                                                        business_status=business_status,
                                                                                        account_id=account_id,
                                                                                        user_id=user_id,
                                                                                        user_name=user_name,
                                                                                        enterprise_name=enterprise_name,
                                                                                        order=order,
                                                                                        page_request_offset=page_request_offset,
                                                                                        page_request_limit=page_request_limit,
                                                                                        page_request_total=page_request_total)
        assert resp.status_code == 200
        mAccountId = resp.json_get("account_info.0.account_id")
        mAccountLevel = resp.json_get("account_info.0.account_level")
        mAccountUsedStatus = resp.json_get("account_info.0.account_used_status")
        mPaymentType = resp.json_get("account_info.0.payment_type")

        # 2、修改该企业账户付费模式
        update_mode = 1  # 0:更新账户启用状态，1:更新付费类型
        account_used_status = None  # ACCOUNT_USED_STATUS_UNSPECIFIED: 未指定 - ACCOUNT_USED_STATUS_UNBLOCKED: 启用 - ACCOUNT_USED_STATUS_BLOCKED: 停用
        payment_type = "ACCOUNT_PAYMENT_POSTPAID"  # ACCOUNT_PAYMENT_UNSPECIFIED: 未指定 - ACCOUNT_PAYMENT_POSTPAID: 允许后付费 - ACCOUNT_PAYMENT_UNPOSTPAID: 不允许后付费，未指定状态不可恢复（历史账号问题）
        resp1 = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountPostApi(account_id=account_id,
                                                                                         update_mode=update_mode,
                                                                                         account_used_status=account_used_status,
                                                                                         payment_type=payment_type)
        # 3、查看修改是否成功
        resp2 = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetAccountListGetApi(account_name=account_name,
                                                                                         account_type=account_type,
                                                                                         status=status,
                                                                                         business_status=business_status,
                                                                                         account_id=account_id,
                                                                                         user_id=user_id,
                                                                                         user_name=user_name,
                                                                                         enterprise_name=enterprise_name,
                                                                                         order=order,
                                                                                         page_request_offset=page_request_offset,
                                                                                         page_request_limit=page_request_limit,
                                                                                         page_request_total=page_request_total)
        assert resp2.json_get("account_info.0.payment_type") == payment_type

        # 4、恢复现场
        update_mode = 1  # 0:更新账户启用状态，1:更新付费类型
        account_used_status = None  # ACCOUNT_USED_STATUS_UNSPECIFIED: 未指定 - ACCOUNT_USED_STATUS_UNBLOCKED: 启用 - ACCOUNT_USED_STATUS_BLOCKED: 停用
        payment_type = "ACCOUNT_PAYMENT_UNPOSTPAID"  # ACCOUNT_PAYMENT_UNSPECIFIED: 未指定 - ACCOUNT_PAYMENT_POSTPAID: 允许后付费 - ACCOUNT_PAYMENT_UNPOSTPAID: 不允许后付费
        resp3 = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountPostApi(account_id=account_id,
                                                                                         update_mode=update_mode,
                                                                                         account_used_status=account_used_status,
                                                                                         payment_type=payment_type)

        resp4 = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetAccountListGetApi(account_name=account_name,
                                                                                         account_type=account_type,
                                                                                         status=status,
                                                                                         business_status=business_status,
                                                                                         account_id=account_id,
                                                                                         user_id=user_id,
                                                                                         user_name=user_name,
                                                                                         enterprise_name=enterprise_name,
                                                                                         order=order,
                                                                                         page_request_offset=page_request_offset,
                                                                                         page_request_limit=page_request_limit,
                                                                                         page_request_total=page_request_total)
        assert resp4.json_get("account_info.0.payment_type") == payment_type

    @pytest.mark.ConsoleRegression
    def test_scenario_001_AdminUpdateAccount_AccountUsedStatus(self, config_obj, AuthEnterpriseApi,
                                                               AuthinternalauthApi):
        """ 超级管理员更新账户的启用和禁用状态"""
        # 1、查看账户信息
        account_name = None
        account_type = None
        status = None
        business_status = None
        account_id = config_obj.Console.User.testEnterprise.account_id
        user_id = None
        user_name = None
        enterprise_name = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetAccountListGetApi(account_name=account_name,
                                                                                        account_type=account_type,
                                                                                        status=status,
                                                                                        business_status=business_status,
                                                                                        account_id=account_id,
                                                                                        user_id=user_id,
                                                                                        user_name=user_name,
                                                                                        enterprise_name=enterprise_name,
                                                                                        order=order,
                                                                                        page_request_offset=page_request_offset,
                                                                                        page_request_limit=page_request_limit,
                                                                                        page_request_total=page_request_total)
        assert resp.status_code == 200
        mAccountId = resp.json_get("account_info.0.account_id")
        mAccountLevel = resp.json_get("account_info.0.account_level")
        mAccountUsedStatus = resp.json_get("account_info.0.account_used_status")
        mPaymentType = resp.json_get("account_info.0.payment_type")

        # 2、修改该企业账户启用禁用状态
        update_mode = 0  # 0:更新账户启用状态，1:更新付费类型
        account_used_status = "ACCOUNT_USED_STATUS_UNBLOCKED"  # ACCOUNT_USED_STATUS_UNSPECIFIED: 未指定 - ACCOUNT_USED_STATUS_UNBLOCKED: 启用 - ACCOUNT_USED_STATUS_BLOCKED: 停用
        payment_type = None  # ACCOUNT_PAYMENT_UNSPECIFIED: 未指定 - ACCOUNT_PAYMENT_POSTPAID: 允许后付费 - ACCOUNT_PAYMENT_UNPOSTPAID: 不允许后付费
        resp1 = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountPostApi(account_id=account_id,
                                                                                         update_mode=update_mode,
                                                                                         account_used_status=account_used_status,
                                                                                         payment_type=payment_type)
        # 3、查看修改是否成功
        resp2 = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetAccountListGetApi(account_name=account_name,
                                                                                         account_type=account_type,
                                                                                         status=status,
                                                                                         business_status=business_status,
                                                                                         account_id=account_id,
                                                                                         user_id=user_id,
                                                                                         user_name=user_name,
                                                                                         enterprise_name=enterprise_name,
                                                                                         order=order,
                                                                                         page_request_offset=page_request_offset,
                                                                                         page_request_limit=page_request_limit,
                                                                                         page_request_total=page_request_total)
        assert resp2.json_get("account_info.0.account_used_status") == account_used_status

        # 4、恢复现场
        update_mode = 0  # 0:更新账户启用状态，1:更新付费类型
        account_used_status = mAccountUsedStatus  # ACCOUNT_USED_STATUS_UNSPECIFIED: 未指定 - ACCOUNT_USED_STATUS_UNBLOCKED: 启用 - ACCOUNT_USED_STATUS_BLOCKED: 停用，未指定状态不可恢复（历史账号问题）
        payment_type = None  # ACCOUNT_PAYMENT_UNSPECIFIED: 未指定 - ACCOUNT_PAYMENT_POSTPAID: 允许后付费 - ACCOUNT_PAYMENT_UNPOSTPAID: 不允许后付费
        resp3 = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountPostApi(account_id=account_id,
                                                                                         update_mode=update_mode,
                                                                                         account_used_status=account_used_status,
                                                                                         payment_type=payment_type)

        resp4 = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetAccountListGetApi(account_name=account_name,
                                                                                         account_type=account_type,
                                                                                         status=status,
                                                                                         business_status=business_status,
                                                                                         account_id=account_id,
                                                                                         user_id=user_id,
                                                                                         user_name=user_name,
                                                                                         enterprise_name=enterprise_name,
                                                                                         order=order,
                                                                                         page_request_offset=page_request_offset,
                                                                                         page_request_limit=page_request_limit,
                                                                                         page_request_total=page_request_total)
        assert resp4.json_get("account_info.0.account_used_status") == account_used_status

    @pytest.mark.ConsoleRegression
    def test_scenario_002_ConsoleInternalUpdateUserCellphone(self, config_obj, AuthEnterpriseApi, AuthinternalauthApi):
        phone = "13312341235"  # 此号码为重复号码
        code = "1"
        resp = AuthinternalauthApi.ConsoleInternalAuthService_ConsoleInternalUpdateUserCellphonePostApi(phone=phone,
                                                                                                        code=code)
        assert resp.json_get("code") == 3
        assert resp.json_get("details.0.reason") == 20103014

    #@pytest.mark.ConsoleRegression
    @pytest.mark.skip("会增加用户的数量暂时不配置在定时任务中")
    def test_scenario_003_whiteAccount(self, config_obj, AuthinternalauthApi, AuthiamApi):
        # 添加白名单
        resp = AuthinternalauthApi.ConsoleInternalAuthService_CreateWhitelistAccountPostApi()
        password = resp.json["password"]
        userName = resp.json["user_name"]

        # 验证白名单login
        digits = "620836"
        captcha_id = "tiLFNNMPvzkGX9ysYSZ0"
        resp = AuthiamApi.login_with_user(username=userName, password=password, captcha_id=captcha_id, digits=digits)
        assert resp.status_code == 200

        # 查询白名单
        page_request_offset = 0
        page_request_limit = 10
        page_request_total = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_GetWhitelistAccountsGetApi(
            page_request_offset=page_request_offset, page_request_limit=page_request_limit,
            page_request_total=page_request_total)
        assert resp.status_code == 200
        num = len(resp.json["list"])
        userId = None
        for i in range(num):
            if resp.json["list"][i]["user_name"] == userName:
                userId = resp.json["list"][i]["user_id"]
                break

        # 删除白名单
        resp = AuthinternalauthApi.ConsoleInternalAuthService_DeleteWhitelistAccountPostApi(user_id=userId)
        assert resp.status_code == 200
