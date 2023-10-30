#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestOrderinternalParam(object):
    """ orderInternal Param测试"""

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
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
        ('account_id', 'invalidaccount_id'),
        ('account_id', ''),
        ('account_id', None),
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('user_name', 'invaliduser_name'),
        ('user_name', ''),
        ('user_name', None),
        ('order_id', 'invalidorder_id'),
        ('order_id', ''),
        ('order_id', None),
        ('category1', 'invalidcategory1'),
        ('category1', ''),
        ('category1', None),
        ('category2', 'invalidcategory2'),
        ('category2', ''),
        ('category2', None),
        ('bill_mode', 'invalidbill_mode'),
        ('bill_mode', ''),
        ('bill_mode', None),
        ('created_sort_type', 'invalidcreated_sort_type'),
        ('created_sort_type', ''),
        ('created_sort_type', None),
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
    def test_api_ConsoleOrderInternalService_GetAuditAllOrderInvalidParam(self, invalidParam, config_obj, OrderinternalApi):
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
        created_sort_type = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = OrderinternalApi.ConsoleOrderInternalService_GetAuditAllOrderGetApi(status=status, account_id=account_id, user_id=user_id, user_name=user_name, order_id=order_id, category1=category1, category2=category2, bill_mode=bill_mode, created_sort_type=created_sort_type, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ConsoleOrderInternalService_GetAllCategoryInvalidParam(self, invalidParam, config_obj, OrderinternalApi):
        """  获取所有类目信息（二期接口）
route: prefix=console-internal acti... """
        intef = OrderinternalApi.ConsoleOrderInternalService_GetAllCategoryGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('order_id', 'invalidorder_id'),
        ('order_id', ''),
        ('order_id', None),
    ])
    def test_api_ConsoleOrderInternalService_GetOrderModifyRecordInvalidParam(self, invalidParam, config_obj, OrderinternalApi):
        """  获取订单修改记录（beta1版本修改）
route: prefix=console-internal... """
        order_id = None
        intef = OrderinternalApi.ConsoleOrderInternalService_GetOrderModifyRecordGetApi(order_id=order_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('all_modify_records', 'invalidall_modify_records'),
        ('all_modify_records', ''),
        ('all_modify_records', None),
    ])
    def test_api_ConsoleOrderInternalService_ModifyOrderInvalidParam(self, invalidParam, config_obj, OrderinternalApi):
        """  修改订单（beta1版本修改）
route: prefix=console-internal act... """
        all_modify_records = None
        intef = OrderinternalApi.ConsoleOrderInternalService_ModifyOrderPostApi(all_modify_records=all_modify_records, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('order_id', 'invalidorder_id'),
        ('order_id', ''),
        ('order_id', None),
    ])
    def test_api_ConsoleOrderInternalService_GetAuditOneOrderInvalidParam(self, invalidParam, config_obj, OrderinternalApi):
        """  按order_id获取订单详情
route: prefix=console-internal act... """
        order_id = None
        intef = OrderinternalApi.ConsoleOrderInternalService_GetAuditOneOrderGetApi(order_id=order_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('order_id', 'invalidorder_id'),
        ('order_id', ''),
        ('order_id', None),
        ('operate', 'invalidoperate'),
        ('operate', ''),
        ('operate', None),
        ('reason', 'invalidreason'),
        ('reason', ''),
        ('reason', None),
    ])
    def test_api_ConsoleOrderInternalService_AuditOrderInvalidParam(self, invalidParam, config_obj, OrderinternalApi):
        """  审核订单
route: prefix=console-internal action=AuditOr... """
        order_id = None
        operate = None
        reason = None
        intef = OrderinternalApi.ConsoleOrderInternalService_AuditOrderPostApi(order_id=order_id, operate=operate, reason=reason, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('order_id', 'invalidorder_id'),
        ('order_id', ''),
        ('order_id', None),
    ])
    def test_api_ConsoleOrderInternalService_UnsubscribeOrderInvalidParam(self, invalidParam, config_obj, OrderinternalApi):
        """  后付费订单退订（ga版本新增）
route: prefix=console-internal act... """
        order_id = None
        intef = OrderinternalApi.ConsoleOrderInternalService_UnsubscribeOrderPostApi(order_id=order_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
