#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.checkin
class TestNotificationinternalApi(object):
    """ notificationInternal Api测试"""

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

    def test_api_ConsoleNotificationInternalService_GetAllMsgType(self, config_obj, NotificationinternalApi):
        """  拉取消息类型列表 """
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = 100
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetAllMsgTypeGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    def test_api_ConsoleNotificationInternalService_GetAllTemplate(self, config_obj, NotificationinternalApi):
        """  拉取消息模板列表 """
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = 100
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetAllTemplateGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    def test_api_ConsoleNotificationInternalService_GetMsgType(self, config_obj, NotificationinternalApi):
        """  获取消息类型详情 """
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = 100
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetAllMsgTypeGetApi(
            page_request_offset=page_request_offset, page_request_limit=page_request_limit,
            page_request_total=page_request_total)
        msg_type_id = resp.json_get("all_msg_types.0.msg_type_id")
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetMsgTypeGetApi(msg_type_id=msg_type_id)
        assert resp.status_code == 200

    def test_api_ConsoleNotificationInternalService_GetTemplate(self, config_obj, NotificationinternalApi):
        """  获取消息模板详情 """
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = 100
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetAllTemplateGetApi(
            page_request_offset=page_request_offset, page_request_limit=page_request_limit,
            page_request_total=page_request_total)
        template_id = resp.json_get("all_templates.0.template_id")
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetTemplateGetApi(template_id=template_id)
        assert resp.status_code == 200
