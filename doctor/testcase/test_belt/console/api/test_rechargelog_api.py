#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestRechargelogApi(object):
    """ rechargeLog Api测试"""

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

    def test_api_ConsoleRechargelogService_GetCurRechargeLog(self, config_obj, RechargelogApi):
        """  后台获取当前待二次确认的充值记录详情
route: prefix=console-internal ... """
        account_id = config_obj.Console.User.internalTestUser.account_id
        resp = RechargelogApi.ConsoleRechargelogService_GetCurRechargeLogGetApi(account_id=account_id)
        assert resp.status_code == 404

    @pytest.mark.skip("前端未用到此接口")
    def test_api_ConsoleRechargelogService_GetLastThreeMonthBillAmountsByAccountIDList(self, config_obj, RechargelogApi):
        """  根据多个accountID查找对应的最近三月账单金额
route: prefix=console-i... """
        account_ids = config_obj.Console.User.internalTestUser.account_id
        resp = RechargelogApi.ConsoleRechargelogService_GetLastThreeMonthBillAmountsByAccountIDListGetApi(account_ids=account_ids)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleRechargelogService_Recharge(self, config_obj, RechargelogApi):
        """  后台充值
route: prefix=console-internal action=Recharg... """
        id = None
        money = None
        remark = None
        resp = RechargelogApi.ConsoleRechargelogService_RechargePostApi(id=id, money=money, remark=remark)
        assert resp.status_code == 400

    def test_api_ConsoleRechargelogService_UpdateAccountAmountInfo(self, config_obj, RechargelogApi):
        """  后台更新账户等级 最近三月金额 账户余额低于阈值
route: prefix=console-int... """
        account_id = config_obj.Console.User.internalTestUser.account_id
        account_level = "ACCOUNT_LEVEL_N"
        the_last_three_months_bill_amount = "1200000"
        empty_status = 0
        account_amount_less_than = "1200000"
        resp = RechargelogApi.ConsoleRechargelogService_UpdateAccountAmountInfoPostApi(account_id=account_id, account_level=account_level, the_last_three_months_bill_amount=the_last_three_months_bill_amount, empty_status=empty_status, account_amount_less_than=account_amount_less_than)
        assert resp.status_code == 200

    def test_api_ConsoleRechargelogService_GetAccountAmountInfo(self, config_obj, RechargelogApi):
        """  后台获取账户余额的账户信息
route: prefix=console-internal actio... """
        account_id = config_obj.Console.User.internalTestUser.account_id
        resp = RechargelogApi.ConsoleRechargelogService_GetAccountAmountInfoGetApi(account_id=account_id)
        assert resp.status_code == 200

    @pytest.mark.skip("废弃接口")
    def test_api_ConsoleRechargelogService_CountSecondConfirmRechargeLogByAccountIDs(self, config_obj, RechargelogApi):
        """  获取多个accountID对应的待更新充值申请记录(也就是待二次确认的充值申请记录)数目
route... """
        account_ids = config_obj.Console.User.internalTestUser.account_id
        resp = RechargelogApi.ConsoleRechargelogService_CountSecondConfirmRechargeLogByAccountIDsGetApi(account_ids=account_ids)
        assert resp.status_code == 200

    @pytest.mark.skip("废弃接口")
    def test_api_ConsoleRechargelogService_CountUnprocessedRechargelogByAccountIDs(self, config_obj, RechargelogApi):
        """  获取多个accountID对应的未处理充值申请记录数目
route: prefix=console-... """
        account_ids = config_obj.Console.User.internalTestUser.account_id
        resp = RechargelogApi.ConsoleRechargelogService_CountUnprocessedRechargelogByAccountIDsGetApi(account_ids=account_ids)
        assert resp.status_code == 200

    def test_api_ConsoleRechargelogService_GetAllRechargeLog(self, config_obj, RechargelogApi):
        """  后台获取所有充值记录
route: prefix=console-internal action=G... """
        account_id = config_obj.Console.User.internalTestUser.account_id
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = None
        resp = RechargelogApi.ConsoleRechargelogService_GetAllRechargeLogGetApi(account_id=account_id, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    def test_api_ConsoleRechargelogService_GetInternalAmount(self, config_obj, RechargelogApi):
        """  后台获取用户账户余额
route: prefix=console-internal action=G... """
        account_id = config_obj.Console.User.internalTestUser.account_id
        resp = RechargelogApi.ConsoleRechargelogService_GetInternalAmountGetApi(account_id=account_id)
        assert resp.status_code == 200
        assert resp.json_get('amount') is not None


    def test_api_ConsoleRechargelogService_GetBalancelogs(self, config_obj, RechargelogApi):
        """  获取余额变更记录列表 GetBalancelogs
route: prefix=console-in... """
        account_id = config_obj.Console.User.internalTestUser.account_id
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = None
        resp = RechargelogApi.ConsoleRechargelogService_GetBalancelogsGetApi(account_id=account_id, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleRechargelogService_CancelRecharge(self, config_obj, RechargelogApi):
        """  后台取消充值
route: prefix=console-internal action=Cance... """
        id = None
        resp = RechargelogApi.ConsoleRechargelogService_CancelRechargePostApi(id=id)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleRechargelogService_CreateRecharge(self, config_obj, RechargelogApi):
        """  后台直接充值
route: prefix=console-internal action=Creat... """
        account_id = None
        money = None
        remark = None
        resp = RechargelogApi.ConsoleRechargelogService_CreateRechargePostApi(account_id=account_id, money=money, remark=remark)
        assert resp.status_code == 200

    @pytest.mark.skip("废弃接口")
    def test_api_ConsoleRechargelogService_GetLatestRechargelogsByAccountIDList(self, config_obj, RechargelogApi):
        """  根据多个accountID查找最新的充值申请记录
route: prefix=console-int... """
        account_ids = None
        resp = RechargelogApi.ConsoleRechargelogService_GetLatestRechargelogsByAccountIDListGetApi(account_ids=account_ids)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleRechargelogService_UpdateOwedAmount(self, config_obj, RechargelogApi):
        """  后台确认修改欠款金额
route: prefix=console-internal action=U... """
        bill_id = None
        account_id = None
        resp = RechargelogApi.ConsoleRechargelogService_UpdateOwedAmountPostApi(bill_id=bill_id, account_id=account_id)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleRechargelogService_RejectRecharge(self, config_obj, RechargelogApi):
        """  后台驳回充值
route: prefix=console-internal action=Rejec... """
        id = None
        resp = RechargelogApi.ConsoleRechargelogService_RejectRechargePostApi(id=id)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleRechargelogService_SecondConfirmationRecharge(self, config_obj, RechargelogApi):
        """  后台二次确认充值
route: prefix=console-internal action=Sec... """
        id = None
        account_id = None
        resp = RechargelogApi.ConsoleRechargelogService_SecondConfirmationRechargePostApi(id=id, account_id=account_id)
        assert resp.status_code == 200

    @pytest.mark.skip("废弃接口")
    def test_api_ConsoleRechargelogService_GetSecondConfirmationRechargelogList(self, config_obj, RechargelogApi):
        """  后台获取待二次确认状态下的所有充值记录
route: prefix=console-internal... """
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = None
        resp = RechargelogApi.ConsoleRechargelogService_GetSecondConfirmationRechargelogListGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    @pytest.mark.skip("废弃接口")
    def test_api_ConsoleRechargelogService_GetUnprocessedRechargelogList(self, config_obj, RechargelogApi):
        """  后台获取有未处理充值申请记录的账户 未处理完成包括的状态有：待处理、待二次确认、驳回
route: ... """
        recharge_at_list_order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = RechargelogApi.ConsoleRechargelogService_GetUnprocessedRechargelogListGetApi(recharge_at_list_order=recharge_at_list_order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    def test_api_ConsoleRechargelogService_GetAmount(self, config_obj, RechargelogApiOpen):
        """  获取账户余额
route: prefix=console action=GetAmount vers... """
        resp = RechargelogApiOpen.ConsoleRechargelogService_GetAmountGetApi()
        assert resp.status_code == 200


    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleRechargelogService_ApplyRecharge(self, config_obj, RechargelogApiOpen):
        """  申请充值
route: prefix=console action=ApplyRecharge ve... """
        money = "1000"
        resp = RechargelogApiOpen.ConsoleRechargelogService_ApplyRechargePostApi(money=money)
        assert resp.status_code == 200
