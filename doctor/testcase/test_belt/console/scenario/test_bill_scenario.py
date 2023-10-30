#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import datetime
import json
import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestBillScenario(object):
    """ Bill scenario test"""

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
    def test_scenario_000_billProcess(self, BillEnterpriseApi):
        """账单查看"""
        date_request_start_at = str(datetime.date.today()-datetime.timedelta(days=100))+"T00:00:00Z"
        date_request_end_at = str(datetime.date.today()-datetime.timedelta(days=1))+"T00:00:00Z"
        resp = BillEnterpriseApi.ConsoleBillService_GetAllBillGroupGetApi(date_request_start_at=date_request_start_at,
                                                                date_request_end_at=date_request_end_at)
        assert resp.status_code == 200
        if len(resp.json_get('all_bill_groups')) == 0:
            pass
        else:
            assert resp.json_get("all_bill_groups.0.status") == "SEND"
            mCreateAt = resp.json_get("all_bill_groups.0.create_at")

            #获取单个账单详情
            resp = BillEnterpriseApi.ConsoleBillService_GetOneBillGroupGetApi(create_at=mCreateAt)
            assert resp.status_code == 200

            #检查账单明细
            resp = BillEnterpriseApi.ConsoleBillService_DownloadBillDetailPostApi(create_at=mCreateAt)
            assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_scenario_001_updateBill(self, BillEnterpriseApi):
        """更新账单状态"""
        date_request_start_at = str(datetime.date.today() - datetime.timedelta(days=100)) + "T00:00:00Z"
        date_request_end_at = str(datetime.date.today()-datetime.timedelta(days=1)) + "T00:00:00Z"
        resp = BillEnterpriseApi.ConsoleBillService_GetAllBillGroupGetApi(date_request_start_at=date_request_start_at,
                                                                          date_request_end_at=date_request_end_at)
        assert resp.status_code == 200
        if len(resp.json_get('all_bill_groups')) == 0:
            pass
        else:
            assert resp.json_get("all_bill_groups.0.status") == "SEND"
            for n in range(len(resp.json_get('all_bill_groups'))):
                if resp.json_get('all_bill_groups.%d.account_status'%n) == "STATUS_UNCONFIRMED":
                    mmCreateAt = resp.json_get('all_bill_groups.%d.create_at'%n)
                    mmAccountStatus = "STATUS_DOUBT"
                    resp = BillEnterpriseApi.ConsoleBillService_UpdateBillStatusPostApi(create_at=mmCreateAt,
                                                                              account_status=mmAccountStatus)
                    assert resp.status_code == 200
                elif resp.json_get('all_bill_groups.%d.account_status'%n) == "STATUS_CONFIRMED":
                    pass
                elif resp.json_get('all_bill_groups.%d.account_status'%n) == "STATUS_DOUBT":
                    mmCreateAt = resp.json_get('all_bill_groups.%d.create_at'%n)
                    mmAccountStatus = "STATUS_DOUBT_CONFIRMED"
                    resp = BillEnterpriseApi.ConsoleBillService_UpdateBillStatusPostApi(create_at=mmCreateAt,
                                                                              account_status=mmAccountStatus)
                    assert resp.status_code == 200









