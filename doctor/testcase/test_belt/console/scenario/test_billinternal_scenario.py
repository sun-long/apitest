#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import base64
import datetime
import os
import time
from io import BytesIO
from time import localtime

import arrow as arrow
import pandas as pd
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
import arrow

@pytest.mark.Skiponline
class TestBillinternalScenario(object):
    """ Billinternal scenario test"""

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
    def test_scenario_000_billInternal(self, config_obj, BillinternalApi, UserApi):
        """账单查看"""
        # 1. 查询账单
        create_at = str(datetime.date.today() - datetime.timedelta(days=32)) + "T00:00:00Z"
        resp = UserApi.ConsoleUserService_GetUserBaseInfoGetApi()
        account_id = resp.json_get("account_id")
        user_id = None
        user_name = None
        enterprise_name = None
        page_request_limit = 20
        page_request_marker = None
        resp = BillinternalApi.ConsoleInternalBillService_GetInternalAllBillGetApi(create_at=create_at,
                                                                                   account_id=account_id,
                                                                                   user_id=user_id, user_name=user_name,
                                                                                   enterprise_name=enterprise_name,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_marker=page_request_marker)
        assert resp.status_code == 200
        mCreateAt = resp.json_get("all_bills.0.bill_group_info.create_at")
        mAccountStatus = resp.json_get("all_bills.0.bill_group_info.account_status")
        mSendStatus = resp.json_get("all_bills.0.bill_group_info.status")

        # 2. 获取账单详情
        resp = BillinternalApi.ConsoleInternalBillService_GetInternalOneBillGetApi(create_at=mCreateAt,
                                                                                   account_id=account_id,
                                                                                   op_user=None)
        assert resp.status_code == 200

        # 3.更新账单状态
        if mAccountStatus == "STATUS_UNCONFIRMED" or "STATUS_CONFIRMED":
            pass
        elif mAccountStatus == "STATUS_DOUBT":
            mmAccountStatus = "STATUS_DOUBT_CONFIRMED"
            resp = BillinternalApi.ConsoleInternalBillService_UpdateInternalBillStatusPostApi(create_at=mCreateAt,
                                                                                              account_id=account_id,
                                                                                              account_status=mmAccountStatus)
            assert resp.status_code == 200

        # 4. 下载账单
        resp = BillinternalApi.ConsoleInternalBillService_DownloadBillDetailPostApi(create_at=mCreateAt,
                                                                                    account_id=account_id)
        assert resp.status_code == 200
        assert resp.json_get("result.buffer") is not None

        # 5.发送账单
        if mSendStatus == "NOT_SEND":
            resp = BillinternalApi.ConsoleInternalBillService_SendInternalBillPostApi(create_at=mCreateAt,
                                                                                      account_id=account_id)
            assert resp.status_code == 200
        else:
            pass

    @pytest.mark.ConsoleRegression
    def test_scenario_001_billInternal_mult_search(self, config_obj, BillinternalApi, UserApi):
        """账单查看_账期"""
        # 1. 查询账单
        create_at = str(datetime.datetime.utcnow().isoformat(timespec='seconds')) + "Z"
        account_id = None
        user_id = None
        user_name = None
        enterprise_name = None
        page_request_limit = 20
        page_request_marker = None
        resp = BillinternalApi.ConsoleInternalBillService_GetInternalAllBillGetApi(create_at=create_at,
                                                                                   account_id=account_id,
                                                                                   user_id=user_id, user_name=user_name,
                                                                                   enterprise_name=enterprise_name,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_marker=page_request_marker)
        assert resp.status_code == 200
        for n in range(len(resp.json_get("all_bills"))):
            if resp.json_get("all_bills.%d.bill_group_info.create_at" % n)[0:7] == str(
                    datetime.date.today().replace(day=1) - datetime.timedelta(days=1))[0:7]:
                pass
            else:
                assert False

    @pytest.mark.ConsoleRegression
    def test_scenario_002_billInternal_mult_search(self, config_obj, BillinternalApi, UserApi):
        """账单查看_状态_NOT_PAY"""
        # 1. 查询账单
        create_at = str(datetime.datetime.utcnow().isoformat(timespec='seconds')) + "Z"
        account_id = None
        user_id = None
        user_name = None
        enterprise_name = None
        page_request_limit = 20
        page_request_marker = None
        pay_status = "NOT_PAY"
        resp = BillinternalApi.ConsoleInternalBillService_GetInternalAllBillGetApi(create_at=create_at,
                                                                                   account_id=account_id,
                                                                                   user_id=user_id, user_name=user_name,
                                                                                   enterprise_name=enterprise_name,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_marker=page_request_marker,
                                                                                   pay_status=pay_status)
        assert resp.status_code == 200
        for n in range(len(resp.json_get("all_bills"))):
            if resp.json_get("all_bills.%d.bill_group_info.pay_status" % n) == pay_status:
                pass
            else:
                assert False

    @pytest.mark.ConsoleRegression
    def test_scenario_003_billInternal_mult_search(self, config_obj, BillinternalApi, UserApi):
        """账单查看_状态_PAY"""
        # 1. 查询账单
        create_at = str(datetime.datetime.utcnow().isoformat(timespec='seconds')) + "Z"
        account_id = None
        user_id = None
        user_name = None
        enterprise_name = None
        page_request_limit = 20
        page_request_marker = None
        pay_status = "PAY"
        resp = BillinternalApi.ConsoleInternalBillService_GetInternalAllBillGetApi(create_at=create_at,
                                                                                   account_id=account_id,
                                                                                   user_id=user_id, user_name=user_name,
                                                                                   enterprise_name=enterprise_name,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_marker=page_request_marker,
                                                                                   pay_status=pay_status)
        assert resp.status_code == 200
        for n in range(len(resp.json_get("all_bills"))):
            if resp.json_get("all_bills.%d.bill_group_info.pay_status" % n) == pay_status:
                pass
            else:
                assert False

    @pytest.mark.ConsoleRegression
    def test_scenario_004_billInternal_mult_search(self, config_obj, BillinternalApi, UserApi):
        """账单查看_account_id"""
        # 1. 查询账单
        create_at = str(datetime.datetime.utcnow().isoformat(timespec='seconds')) + "Z"
        account_id = UserApi.ConsoleUserService_GetUserBaseInfoGetApi().json_get("account_id")
        user_id = None
        user_name = None
        enterprise_name = None
        page_request_limit = 20
        page_request_marker = None
        pay_status = None
        resp = BillinternalApi.ConsoleInternalBillService_GetInternalAllBillGetApi(create_at=create_at,
                                                                                   account_id=account_id,
                                                                                   user_id=user_id, user_name=user_name,
                                                                                   enterprise_name=enterprise_name,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_marker=page_request_marker,
                                                                                   pay_status=pay_status)
        assert resp.status_code == 200
        for n in range(len(resp.json_get("all_bills"))):
            if resp.json_get("all_bills.%d.account_info.account_id" % n) == account_id:
                pass
            else:
                assert False

    @pytest.mark.ConsoleRegression
    def test_scenario_005_billInternal_mult_search(self, config_obj, BillinternalApi, UserApi):
        """账单查看_user_id"""
        # 1. 查询账单
        create_at = str(datetime.datetime.utcnow().isoformat(timespec='seconds')) + "Z"
        account_id = None
        user_id = UserApi.ConsoleUserService_GetUserBaseInfoGetApi().json_get("user_id")
        user_name = None
        enterprise_name = None
        page_request_limit = 20
        page_request_marker = None
        pay_status = None
        resp = BillinternalApi.ConsoleInternalBillService_GetInternalAllBillGetApi(create_at=create_at,
                                                                                   account_id=account_id,
                                                                                   user_id=user_id, user_name=user_name,
                                                                                   enterprise_name=enterprise_name,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_marker=page_request_marker,
                                                                                   pay_status=pay_status)
        assert resp.status_code == 200
        for n in range(len(resp.json_get("all_bills"))):
            if resp.json_get("all_bills.%d.user_id" % n) == user_id:
                pass
            else:
                assert False

    @pytest.mark.ConsoleRegression
    def test_scenario_006_billInternal_mult_search(self, config_obj, BillinternalApi, UserApi):
        """账单查看_分页"""
        # 1. 查询账单
        create_at = str(datetime.date.today() - datetime.timedelta(days=32)) + "T00:00:00Z"
        account_id = None
        user_id = None
        user_name = None
        enterprise_name = None
        page_request_limit = 1
        page_request_marker = None
        pay_status = None
        resp = BillinternalApi.ConsoleInternalBillService_GetInternalAllBillGetApi(create_at=create_at,
                                                                                   account_id=account_id,
                                                                                   user_id=user_id, user_name=user_name,
                                                                                   enterprise_name=enterprise_name,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_marker=page_request_marker,
                                                                                   pay_status=pay_status)
        assert resp.status_code == 200
        assert len(resp.json_get("all_bills")) == page_request_limit

    @pytest.mark.ConsoleRegression
    def test_scenario_007_billInternal_mult_search(self, config_obj, BillinternalApi, AuthEnterpriseApi):
        """账单查看_认证主体"""
        # 1. 查询账单
        create_at = str(datetime.datetime.utcnow().isoformat(timespec='seconds')) + "Z"
        account_id = None
        user_id = None
        user_name = None
        enterprise_name = AuthEnterpriseApi.ConsoleAuthService_GetEnterpriseAccountGetApi().json_get(
            "enterprise_account.enterprise_name")
        page_request_limit = 1
        page_request_marker = None
        pay_status = None
        resp = BillinternalApi.ConsoleInternalBillService_GetInternalAllBillGetApi(create_at=create_at,
                                                                                   account_id=account_id,
                                                                                   user_id=user_id, user_name=user_name,
                                                                                   enterprise_name=enterprise_name,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_marker=page_request_marker,
                                                                                   pay_status=pay_status)
        assert resp.status_code == 200
        for n in range(len(resp.json_get("all_bills"))):
            if resp.json_get("all_bills.%d.account_info.enterprise_name" % n) == enterprise_name:
                pass
            else:
                assert False

    @pytest.mark.ConsoleRegression
    def test_scenario_008_billInternal_billCheck(self, config_obj, BillinternalApi, AuthEnterpriseApi):
        """校验上月账单是否生成"""
        now = datetime.datetime.now().replace(microsecond=0)  # 当前时间

        ago = now - datetime.timedelta(days=30)  # 当前时间往前推30天

        agoone = datetime.datetime.strftime(ago, "%Y-%m-%d %H:%M:%S")

        print("agoone:", agoone)

        last = datetime.date(datetime.date.today().year, datetime.date.today().month, 1) - datetime.timedelta(1)
        print("last:", last)
        lastOne = datetime.datetime.strftime(last, "%Y-%m-%d %H:%M:%S")
        print("lastOne:", lastOne)
        utctime = arrow.get(lastOne).to("UTC")
        utc_time_format = utctime.strftime("%Y-%m-%dT%H:%M:%SZ")
        print("转换后: ", str(utc_time_format))


        # localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # #ago = localtime - datetime.timedelta(days=30)  # 当前时间往前推30天
        # utctime = arrow.get(localtime).to("UTC")
        # utc_time_format = utctime.strftime("%Y-%m-%dT%H:%M:%SZ")
        # print("localtime:", localtime)
        # #print("ago:", ago)
        #
        # print("utc_date_time:", utc_time_format)
        # print("转换前: ", str(localtime))
        # print("转换后: ", str(utc_time_format))

        create_at = utc_time_format
        account_id = None
        user_id = None
        user_name = None
        enterprise_name = None
        page_request_limit = 20
        page_request_marker = None
        resp = BillinternalApi.ConsoleInternalBillService_GetInternalAllBillGetApi(create_at=create_at,
                                                                                   account_id=account_id,
                                                                                   user_id=user_id, user_name=user_name,
                                                                                   enterprise_name=enterprise_name,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_marker=page_request_marker)
        assert resp.status_code == 200
        assert len(resp.json["all_bills"]) > 0





