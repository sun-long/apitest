#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
@pytest.mark.Skiponline
@pytest.mark.ConsoleRegression
class TestRechargelogScenario(object):
    """ Rechargelog scenario test"""

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


    def test_scenario_001_recharge(self, config_obj, RechargelogApiOpen, AuthiamApi, RechargelogApi, NotificationApi):
        """ 充值操作"""
        # 账户充值
        digits = "620836"
        captcha_id = "tiLFNNMPvzkGX9ysYSZ0"
        resp = AuthiamApi.login_with_user(username=config_obj.Console.User.testConsoleMainUser.userNameForDisable,
                                          password="123456qw", captcha_id=captcha_id, digits=digits)
        assert resp.status_code == 200
        userloginToken = resp.json_get("access_token")
        money = "10000"
        resp = RechargelogApiOpen.ConsoleRechargelogService_ApplyRechargePostApi(money=money, loginToken=userloginToken)
        assert resp.status_code == 200

        # 获取充值记录id
        account_id = config_obj.Console.User.testConsoleMainUser.accountIdForDisable
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = None
        resp = RechargelogApi.ConsoleRechargelogService_GetAllRechargeLogGetApi(account_id=account_id,
                                                                                page_request_offset=page_request_offset,
                                                                                page_request_limit=page_request_limit,
                                                                                page_request_total=page_request_total)
        assert resp.status_code == 200
        rechargeId = resp.json_get("all_infos.0.id")
        # 充值记录为待处理
        assert resp.json_get("all_infos.0.status") == "RECHARGE_LOG_STATUS_WAIT"

        # 审核前获取充值日志
        resp = RechargelogApi.ConsoleRechargelogService_GetBalancelogsGetApi(account_id=account_id, page_request_offset=0, page_request_limit=20, page_request_total=page_request_total)
        rechargeLogCount = resp.json_get("page_response.total")

        # 运营后台操作充值
        id = rechargeId
        money = '10000'
        resp = RechargelogApi.ConsoleRechargelogService_RechargePostApi(id=id, money=money, remark=None)
        assert resp.status_code == 200

        # 再次直接充值
        resp = RechargelogApi.ConsoleRechargelogService_CreateRechargePostApi(account_id=account_id, money=money,
                                                                              remark=None)
        assert resp.status_code == 409

        # 获取待审核的记录为二次待审核
        resp = RechargelogApi.ConsoleRechargelogService_GetCurRechargeLogGetApi(account_id=account_id)
        assert resp.json_get("info.status") == "RECHARGE_LOG_STATUS_WAITCONFIRM"
        id = resp.json_get("info.id")

        # 审核
        resp = RechargelogApi.ConsoleRechargelogService_SecondConfirmationRechargePostApi(id=id, account_id=account_id)
        assert resp.status_code == 200

        # 检查充值记录为审核通过
        resp = RechargelogApi.ConsoleRechargelogService_GetAllRechargeLogGetApi(account_id=account_id,
                                                                                page_request_offset=0,
                                                                                page_request_limit=20,
                                                                                page_request_total=None)

        assert resp.json_get("all_infos.0.status") == "RECHARGE_LOG_STATUS_CONFIRM"

        # 审核后获取充值日志新增一条充值日志
        resp = RechargelogApi.ConsoleRechargelogService_GetBalancelogsGetApi(account_id=account_id,
                                                                             page_request_offset=0,
                                                                             page_request_limit=20,
                                                                             page_request_total=None)
        rechargeLogCount1 = resp.json_get("page_response.total")
        assert rechargeLogCount1 == rechargeLogCount + 1

        # 运营后台账户余额与openConsole余额一致校验
        resp = RechargelogApi.ConsoleRechargelogService_GetAccountAmountInfoGetApi(account_id=account_id)
        accountAmountInternal = resp.json_get("account_amount")

        resp = RechargelogApiOpen.ConsoleRechargelogService_GetAmountGetApi(loginToken=userloginToken)
        accountAmountOpen = resp.json_get("amount")
        assert accountAmountInternal == accountAmountOpen

        # 获取财务类型充值消息
        msg_type_id = 4
        status = "STATUS_UNREAD"
        page_request_offset = 0
        page_request_limit = 100
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=msg_type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=None,
                                                                          loginToken=userloginToken)
        assert resp.status_code == 200
        receive_msg_id = resp.json_get("all_msgs.0.msg_id")

        # 获取充值消息详情
        resp = NotificationApi.ConsoleNotificationService_GetOneMsgGetApi(msg_id=receive_msg_id,
                                                                          loginToken=userloginToken)
        assert resp.json_get("msg_info.name") == "充值成功提醒"

        # 删除消息
        all_msg_ids = [receive_msg_id]
        resp = NotificationApi.ConsoleNotificationService_DeleteBatchMsgPostApi(all_msg_ids=all_msg_ids,
                                                                                loginToken=userloginToken)
        assert resp.status_code == 200

    def test_scenario_002_directRecharge(self, config_obj, AuthiamApi, RechargelogApiOpen, RechargelogApi, NotificationApi):
        """ 直接充值操作"""
        # 直接充值
        account_id = config_obj.Console.User.testConsoleMainUser.accountIdForDisable
        money = "10000"
        resp = RechargelogApi.ConsoleRechargelogService_CreateRechargePostApi(account_id=account_id, money=money,
                                                                              remark=None)
        assert resp.status_code == 200
        # 再次直接充值
        resp = RechargelogApi.ConsoleRechargelogService_CreateRechargePostApi(account_id=account_id, money=money,
                                                                              remark=None)
        assert resp.status_code == 409
        # 获取待审核的记录
        resp = RechargelogApi.ConsoleRechargelogService_GetCurRechargeLogGetApi(account_id=account_id)
        assert resp.json_get("info.status") == "RECHARGE_LOG_STATUS_WAITCONFIRM"
        id = resp.json_get("info.id")

        # 审核前获取充值日志
        resp = RechargelogApi.ConsoleRechargelogService_GetBalancelogsGetApi(account_id=account_id,
                                                                             page_request_offset=0,
                                                                             page_request_limit=20,
                                                                             page_request_total=None)
        rechargeLogCount = resp.json_get("page_response.total")

        # 审核
        resp = RechargelogApi.ConsoleRechargelogService_SecondConfirmationRechargePostApi(id=id, account_id=account_id)
        assert resp.status_code == 200

        # 审核后获取充值日志新增一条充值日志
        resp = RechargelogApi.ConsoleRechargelogService_GetBalancelogsGetApi(account_id=account_id,
                                                                             page_request_offset=0,
                                                                             page_request_limit=20,
                                                                             page_request_total=None)
        rechargeLogCount1 = resp.json_get("page_response.total")
        assert rechargeLogCount1 == rechargeLogCount + 1

        # 检查充值记录为审核通过
        resp = RechargelogApi.ConsoleRechargelogService_GetAllRechargeLogGetApi(account_id=account_id,
                                                                                page_request_offset=0,
                                                                                page_request_limit=20,
                                                                                page_request_total=None)

        assert resp.json_get("all_infos.0.status") == "RECHARGE_LOG_STATUS_CONFIRM"

        # 运营后台账户余额
        resp = RechargelogApi.ConsoleRechargelogService_GetAccountAmountInfoGetApi(account_id=account_id)
        accountAmountInternal = resp.json_get("account_amount")


        # 检查运营后台余额和openConsole余额是否一致
        digits = "620836"
        captcha_id = "tiLFNNMPvzkGX9ysYSZ0"
        resp = AuthiamApi.login_with_user(username=config_obj.Console.User.testConsoleMainUser.userNameForDisable, password="123456qw", captcha_id=captcha_id, digits=digits)
        assert resp.status_code == 200
        userloginToken = resp.json_get("access_token")
        resp = RechargelogApiOpen.ConsoleRechargelogService_GetAmountGetApi(loginToken=userloginToken)
        accountAmountOpen = resp.json_get("amount")
        assert accountAmountInternal == accountAmountOpen

        # 获取财务类型充值消息
        msg_type_id = 4
        status = "STATUS_UNREAD"
        page_request_offset = 0
        page_request_limit = 100
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=msg_type_id, status=status, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=None, loginToken=userloginToken)
        assert resp.status_code == 200
        receive_msg_id = resp.json_get("all_msgs.0.msg_id")

        # 获取充值消息详情
        resp = NotificationApi.ConsoleNotificationService_GetOneMsgGetApi(msg_id=receive_msg_id, loginToken=userloginToken)
        assert resp.json_get("msg_info.name") == "充值成功提醒"

        # 删除消息
        all_msg_ids = [receive_msg_id]
        resp = NotificationApi.ConsoleNotificationService_DeleteBatchMsgPostApi(all_msg_ids=all_msg_ids, loginToken=userloginToken)
        assert resp.status_code == 200



    def test_scenario_003_rechargeReject(self,config_obj, AuthiamApi, RechargelogApiOpen, RechargelogApi, NotificationApi):
        """ 充值且驳回，取消操作"""
        # 账户充值
        digits = "620836"
        captcha_id = "tiLFNNMPvzkGX9ysYSZ0"
        resp = AuthiamApi.login_with_user(username=config_obj.Console.User.testConsoleMainUser.userNameForDisable,
                                          password="123456qw", captcha_id=captcha_id, digits=digits)
        assert resp.status_code == 200
        userloginToken = resp.json_get("access_token")
        money = "10000"
        resp = RechargelogApiOpen.ConsoleRechargelogService_ApplyRechargePostApi(money=money, loginToken=userloginToken)
        assert resp.status_code == 200

        # 获取充值记录id
        account_id = config_obj.Console.User.testConsoleMainUser.accountIdForDisable
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = None
        resp = RechargelogApi.ConsoleRechargelogService_GetAllRechargeLogGetApi(account_id=account_id,
                                                                                page_request_offset=page_request_offset,
                                                                                page_request_limit=page_request_limit,
                                                                                page_request_total=page_request_total)
        assert resp.status_code == 200
        rechargeId = resp.json_get("all_infos.0.id")

        # 获取待审核记录为0
        resp = RechargelogApi.ConsoleRechargelogService_GetCurRechargeLogGetApi(account_id=account_id)
        assert resp.json_get("error") == "find rechargelog by status err record not found"

        # 操作充值
        id = rechargeId
        money = '10000'
        resp = RechargelogApi.ConsoleRechargelogService_RechargePostApi(id=id, money=money, remark=None)
        assert resp.status_code == 200

        # 获取待审核的记录
        resp = RechargelogApi.ConsoleRechargelogService_GetCurRechargeLogGetApi(account_id=account_id)
        assert resp.json_get("info.status") == "RECHARGE_LOG_STATUS_WAITCONFIRM"
        id = resp.json_get("info.id")

        # 驳回
        resp = RechargelogApi.ConsoleRechargelogService_RejectRechargePostApi(id=id)
        assert resp.status_code == 200

        # 无充值消息
        msg_type_id = 4
        status = "STATUS_UNREAD"
        page_request_offset = 0
        page_request_limit = 100
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=msg_type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=None,
                                                                          loginToken=userloginToken)
        assert resp.status_code == 200
        assert resp.json_get("all_msgs") == []

        # 检查充值记录为已驳回
        resp = RechargelogApi.ConsoleRechargelogService_GetAllRechargeLogGetApi(account_id=account_id,
                                                                                page_request_offset=page_request_offset,
                                                                                page_request_limit=page_request_limit,
                                                                                page_request_total=page_request_total)

        assert resp.json_get("all_infos.0.status") == "RECHARGE_LOG_STATUS_REJECT"

        # 取消操作
        resp = RechargelogApi.ConsoleRechargelogService_CancelRechargePostApi(id=rechargeId)
        assert resp.status_code == 200

        # 检查充值记录为已取消
        resp = RechargelogApi.ConsoleRechargelogService_GetAllRechargeLogGetApi(account_id=account_id,
                                                                                page_request_offset=page_request_offset,
                                                                                page_request_limit=page_request_limit,
                                                                                page_request_total=page_request_total)

        assert resp.json_get("all_infos.0.status") == "RECHARGE_LOG_STATUS_CANCEL"


    def test_scenario_004_directRechargeReject(self,config_obj, AuthiamApi, RechargelogApiOpen, RechargelogApi, NotificationApi):
        """ 直接充值且驳回，取消操作"""
        #直接充值
        digits = "620836"
        captcha_id = "tiLFNNMPvzkGX9ysYSZ0"
        resp = AuthiamApi.login_with_user(username=config_obj.Console.User.testConsoleMainUser.userNameForDisable,
                                          password="123456qw", captcha_id=captcha_id, digits=digits)
        assert resp.status_code == 200
        userloginToken = resp.json_get("access_token")
        account_id = config_obj.Console.User.testConsoleMainUser.accountIdForDisable
        money = "10000"
        resp = RechargelogApi.ConsoleRechargelogService_CreateRechargePostApi(account_id=account_id, money=money,
                                                                              remark=None)
        assert resp.status_code == 200

        # 获取充值记录id
        account_id = config_obj.Console.User.testConsoleMainUser.accountIdForDisable
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = None
        resp = RechargelogApi.ConsoleRechargelogService_GetAllRechargeLogGetApi(account_id=account_id,
                                                                                page_request_offset=page_request_offset,
                                                                                page_request_limit=page_request_limit,
                                                                                page_request_total=page_request_total)
        assert resp.status_code == 200
        rechargeId = resp.json_get("all_infos.0.id")

        # 获取待审核的记录
        resp = RechargelogApi.ConsoleRechargelogService_GetCurRechargeLogGetApi(account_id=account_id)
        assert resp.json_get("info.status") == "RECHARGE_LOG_STATUS_WAITCONFIRM"
        id = resp.json_get("info.id")

        # 驳回
        resp = RechargelogApi.ConsoleRechargelogService_RejectRechargePostApi(id=id)
        assert resp.status_code == 200

        # 无充值消息
        msg_type_id = 4
        status = "STATUS_UNREAD"
        page_request_offset = 0
        page_request_limit = 100
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=msg_type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=None,
                                                                          loginToken=userloginToken)
        assert resp.status_code == 200
        assert resp.json_get("all_msgs") == []

        # 检查充值记录为已驳回
        resp = RechargelogApi.ConsoleRechargelogService_GetAllRechargeLogGetApi(account_id=account_id,
                                                                                page_request_offset=page_request_offset,
                                                                                page_request_limit=page_request_limit,
                                                                                page_request_total=page_request_total)

        assert resp.json_get("all_infos.0.status") == "RECHARGE_LOG_STATUS_REJECT"

        # 取消操作
        resp = RechargelogApi.ConsoleRechargelogService_CancelRechargePostApi(id=rechargeId)
        assert resp.status_code == 200

        # 检查充值记录为已取消
        resp = RechargelogApi.ConsoleRechargelogService_GetAllRechargeLogGetApi(account_id=account_id,
                                                                                page_request_offset=page_request_offset,
                                                                                page_request_limit=page_request_limit,
                                                                                page_request_total=page_request_total)

        assert resp.json_get("all_infos.0.status") == "RECHARGE_LOG_STATUS_CANCEL"


    def test_scenario_005_personalRecharge(self,config_obj, AuthinternalauthApi, RechargelogApi):

        # 获取个人账户信息
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetCostManagementAccountListGetApi(account_type="ACCOUNT_TYPE_PERSON", account_id=None, user_id=None, user_name=None, enterprise_name=None, account_level=None, only_view_unprocessed_records_accounts=None, order=None, page_request_offset=None, page_request_limit=None, page_request_total=None)
        account_id = resp.json_get("account_info.0.account_id")
        # 个人充值
        money = "10000"
        resp = RechargelogApi.ConsoleRechargelogService_CreateRechargePostApi(account_id=account_id, money=money,
                                                                              remark=None)
        assert resp.status_code == 403


