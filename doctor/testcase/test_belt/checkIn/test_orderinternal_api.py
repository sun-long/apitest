#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


@pytest.mark.checkin
class TestOrderinternalApi(object):
    """ orderInternal Api测试"""

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

    def test_api_ConsoleOrderInternalService_GetAuditAllOrder(self, config_obj, OrderinternalApi):
        """  获取所有订单
route: prefix=console-internal action=GetAu... """
        status = None
        account_id = None
        user_id = None
        user_name = None
        order_id = None
        category1 = None
        category2 = None
        bill_mode = None
        created_sort_type = 'DESC'
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = None
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditAllOrderGetApi(status=status, account_id=account_id, user_id=user_id, user_name=user_name, order_id=order_id, category1=category1, category2=category2, bill_mode=bill_mode, created_sort_type=created_sort_type, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200
        assert len(resp.json_get('all_orders')) > 0

    def test_api_ConsoleOrderInternalService_GetAllCategory(self, config_obj, OrderinternalApi):
        """  获取所有类目信息（二期接口）
route: prefix=console-internal acti... """
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAllCategoryGetApi()
        assert resp.status_code == 200
        assert len(resp.json_get('all_categories')) > 0


    def test_api_ConsoleOrderInternalService_GetOrderModifyRecord(self, config_obj, OrderinternalApi):
        """  获取订单修改记录（beta1版本修改）
route: prefix=console-internal... """
        order_id = config_obj.Console.User.internalTestUser.orderIdByGetLog
        resp = OrderinternalApi.ConsoleOrderInternalService_GetOrderModifyRecordGetApi(order_id=order_id)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleOrderInternalService_ModifyOrder(self, config_obj, OrderinternalApi):
        """  修改订单（beta1版本修改）
route: prefix=console-internal act... """
        all_modify_records = None
        resp = OrderinternalApi.ConsoleOrderInternalService_ModifyOrderPostApi(all_modify_records=all_modify_records)
        assert resp.status_code == 200

    def test_api_ConsoleOrderInternalService_GetAuditOneOrder(self, config_obj, OrderinternalApi):
        """  按order_id获取订单详情
route: prefix=console-internal act... """
        order_id = config_obj.Console.User.internalTestUser.orderIdByGetLog
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditOneOrderGetApi(order_id=order_id)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleOrderInternalService_AuditOrder(self, config_obj, OrderinternalApi):
        """  审核订单
route: prefix=console-internal action=AuditOr... """
        order_id = None
        operate = None
        reason = None
        resp = OrderinternalApi.ConsoleOrderInternalService_AuditOrderPostApi(order_id=order_id, operate=operate, reason=reason)
        assert resp.status_code == 200
        
    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleOrderInternalService_UnsubscribeOrder(self, config_obj, OrderinternalApi):
        """  后付费订单退订（ga版本新增）
route: prefix=console-internal act... """
        order_id = None
        resp = OrderinternalApi.ConsoleOrderInternalService_UnsubscribeOrderPostApi(order_id=order_id)
        assert resp.status_code == 200

    def test_api_ConsoleOrderInternalService_GetAllCategory(self, config_obj, OrderinternalApi):
            """  获取所有类目信息（二期接口）
    route: prefix=console-internal acti... """
            resp = OrderinternalApi.ConsoleOrderInternalService_GetAllCategoryGetApi()
            assert resp.status_code == 200
