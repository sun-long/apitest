#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
import warnings
import os
from datetime import date, timedelta, datetime

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.Skiponline
@pytest.mark.ConsoleRegression
class TestOrderinternalScenario(object):
    """ Orderinternal scenario test"""

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

    def test_scenario_000_modifyOrder(self, config_obj, OrderinternalApi, OrderApi, MainUserTokenForSpuop, ProductApi):
        """ 修改订单,获取修改记录，联合查询"""
        # 创建订单
        spu_code = "OCRDrivingLicense"
        resp = OrderApi.CreatePostPayOrder(spu_code, ProductApi, MainUserTokenForSpuop)
        assert resp.status_code == 200
        order_id = resp.json["order_info"]["order_id"]
        created_sort_type = "DESC"
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = 1

        # 查询订单
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditAllOrderGetApi(order_id=order_id,
                                                                                   created_sort_type=created_sort_type,
                                                                                   page_request_offset=page_request_offset,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_total=page_request_total)
        assert resp.status_code == 200
        spu_id = resp.json["all_orders"][0]["order_info"]["product_info"]["all_spus"][0]["info"]["id"]

        # 检查订单状态为待审核
        assert resp.json["all_orders"][0]["order_info"]["status"] == "AUDITING"

        # 修改订单
        all_modify_records = [
            {"order_id": order_id, "spu_id": spu_id, "new_prices": [10],
             "oa_number": "xiugai", "remark": ""}]
        resp = OrderinternalApi.ConsoleOrderInternalService_ModifyOrderPostApi(all_modify_records=all_modify_records)
        assert resp.status_code == 200

        # 获取修改记录
        resp = OrderinternalApi.ConsoleOrderInternalService_GetOrderModifyRecordGetApi(order_id=order_id)
        assert resp.status_code == 200
        assert resp.json_get("all_modify_records.0.new_prices") == ['10']

        # 订单驳回
        time.sleep(180)
        operate = "OP_REJECT"
        reason = None
        resp = OrderinternalApi.ConsoleOrderInternalService_AuditOrderPostApi(order_id=order_id, operate=operate,
                                                                              reason=reason)
        assert resp.status_code == 200

        # 检查订单状态为审核不通过
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditAllOrderGetApi(order_id=order_id,
                                                                                   created_sort_type=created_sort_type,
                                                                                   page_request_offset=page_request_offset,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_total=page_request_total)
        assert resp.json["all_orders"][0]["order_info"]["status"] == "AUDIT_REJECTED"

        # 联合查询
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditAllOrderGetApi(status="AUDIT_REJECTED",
                                                                                   account_id=config_obj.Console.User.testConsoleMainUser.accountIdForDisable,
                                                                                   user_id=None,
                                                                                   user_name=config_obj.Console.User.testConsoleMainUser.userNameForDisable,
                                                                                   order_id=order_id,
                                                                                   category1=None,
                                                                                   category2=None,
                                                                                   bill_mode="PAY_TYPE_POST",
                                                                                   created_sort_type="DESC",
                                                                                   page_request_offset=0,
                                                                                   page_request_limit=20,
                                                                                   page_request_total=None)
        assert len(resp.json_get("all_orders")) == 1

        # 检查openConsole的订单状态
        # 检查订单状态为审核不通过
        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=order_id, loginToken=MainUserTokenForSpuop)
        assert resp.json_get("order_info.status") == "AUDIT_REJECTED"

    def test_scenario_001_modifyOrderAndOrderAgain(self, config_obj, OrderinternalApi, OrderApi, MainUserTokenForSpuop,
                                                   ProductApi):
        """ 修改订单价格，审核通过以后，展示修改后的价格，退订再次订阅展示的sku的定价"""

        # 创建后付费订单
        spu_code = config_obj.Console.User.testConsoleMainUser.spuCodeForOrderAgain
        resp = OrderApi.CreatePostPayOrder(spu_code, ProductApi, MainUserTokenForSpuop)
        assert resp.status_code == 200
        order_id = resp.json_get("order_info.order_id")

        # 查询订单
        created_sort_type = "DESC"
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = 1
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditAllOrderGetApi(order_id=order_id,
                                                                                   created_sort_type=created_sort_type,
                                                                                   page_request_offset=page_request_offset,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_total=page_request_total)

        assert resp.status_code == 200
        spu_id = resp.json["all_orders"][0]["order_info"]["product_info"]["all_spus"][0]["info"]["id"]
        # 修改订单
        all_modify_records = [
            {"order_id": order_id, "spu_id": spu_id, "new_prices": [12000],
             "oa_number": "xiugai", "remark": ""}]
        resp = OrderinternalApi.ConsoleOrderInternalService_ModifyOrderPostApi(all_modify_records=all_modify_records)
        assert resp.status_code == 200

        # 订单审核
        operate = "OP_AGREE"
        reason = None
        resp = OrderinternalApi.ConsoleOrderInternalService_AuditOrderPostApi(order_id=order_id, operate=operate,
                                                                              reason=reason)
        assert resp.status_code == 200
        time.sleep(10)

        # 获取订单详情的价格为修改后的价格
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditOneOrderGetApi(order_id=order_id)
        assert resp.json["order_info"]["all_modify_records"][0]["new_prices"][0] == "12000"

        # 运营后台订单退订
        time.sleep(180)
        resp = OrderinternalApi.ConsoleOrderInternalService_UnsubscribeOrderPostApi(order_id=order_id)
        assert resp.status_code == 200

        # 重新订阅
        time.sleep(180)
        resp = OrderApi.CreatePostPayOrder(spu_code, ProductApi, MainUserTokenForSpuop)
        assert resp.status_code == 200
        secondOrderId = resp.json_get("order_info.order_id")

        # 审核通过
        operate = "OP_AGREE"
        reason = None
        resp = OrderinternalApi.ConsoleOrderInternalService_AuditOrderPostApi(order_id=secondOrderId, operate=operate,
                                                                              reason=reason)
        assert resp.status_code == 200

        # 获取订单详情的价格
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditOneOrderGetApi(order_id=secondOrderId)
        assert \
            resp.json["order_info"]["order_info"]["product_info"]["all_spus"][0]["all_skus"][0]["all_prices"][0][
                "rules"][
                0]["unit_price"] == "15000"

        # 退订
        time.sleep(180)
        resp = OrderinternalApi.ConsoleOrderInternalService_UnsubscribeOrderPostApi(order_id=secondOrderId)
        assert resp.status_code == 200
        time.sleep(180)

    @pytest.mark.parametrize("bill_mode", ["PAY_TYPE_PRE",
                                           "PAY_TYPE_POST"])
    def test_scenario_002_getOrderInternalByOrderId(self, OrderinternalApi, bill_mode):
        """ 通过订单编码可查询订单"""
        """
        订单类型列表【订单管理，订单修改】
        包括:后付费订单和预付费订单
            通过订单编码可查询, check检查结果
        """
        created_sort_type = "DESC"
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = 1
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditAllOrderGetApi(bill_mode=bill_mode,
                                                                                   created_sort_type=created_sort_type,
                                                                                   page_request_offset=page_request_offset,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_total=page_request_total)
        assert resp.status_code == 200
        order_id = resp.json_get("all_orders.0.order_info.order_id")
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditAllOrderGetApi(order_id=order_id,
                                                                                   created_sort_type=created_sort_type,
                                                                                   page_request_offset=page_request_offset,
                                                                                   page_request_limit=page_request_limit,
                                                                                   page_request_total=page_request_total)
        assert resp.status_code == 200
        assert len(resp.json_get("all_orders")) == 1
        assert resp.json_get("all_orders.0.order_info.order_id") == order_id


