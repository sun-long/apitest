#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.Skiponline
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

    @pytest.mark.skip("场景测试中添加")
    def test_api_ConsoleNotificationInternalService_SendNotification(self, config_obj, NotificationinternalApi):
        """  发送系统消息
route: prefix=console-internal action=SendN... """
        user_id = None
        template_id = None
        content = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_SendNotificationPostApi(user_id=user_id, template_id=template_id, content=content)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_api_ConsoleNotificationInternalService_GetAllMsgType(self, config_obj, NotificationinternalApi):
        """  拉取消息类型列表
route: prefix=console-internal action=Get... """
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetAllMsgTypeGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_api_ConsoleNotificationInternalService_GetAllTemplate(self, config_obj, NotificationinternalApi):
        """  拉取消息模板列表
route: prefix=console-internal action=Get... """
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetAllTemplateGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    @pytest.mark.skip("不可逆操作，会在场景测试中考虑添加")
    def test_api_ConsoleNotificationInternalService_DeleteMsgType(self, config_obj, NotificationinternalApi):
        """  删除消息类型
route: prefix=console-internal action=Delet... """
        msg_type_id = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteMsgTypePostApi(msg_type_id=msg_type_id)
        assert resp.status_code == 200

    @pytest.mark.skip("不可逆操作，会在场景测试中考虑添加")
    def test_api_ConsoleNotificationInternalService_DeleteTemplate(self, config_obj, NotificationinternalApi):
        """  删除消息模板
route: prefix=console-internal action=Delet... """
        template_id = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteTemplatePostApi(template_id=template_id)
        assert resp.status_code == 200

    @pytest.mark.skip("场景测试中添加")
    def test_api_ConsoleNotificationInternalService_GetMsgType(self, config_obj, NotificationinternalApi):
        """  获取消息类型详情
route: prefix=console-internal action=Get... """
        msg_type_id = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetMsgTypeGetApi(msg_type_id=msg_type_id)
        assert resp.status_code == 200

    @pytest.mark.skip("场景测试中添加")
    def test_api_ConsoleNotificationInternalService_CreateMsgType(self, config_obj, NotificationinternalApi):
        """  添加消息类型
route: prefix=console-internal action=Creat... """
        name = None
        id = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_CreateMsgTypePostApi(name=name, id=id)
        assert resp.status_code == 200

    @pytest.mark.skip("场景测试中添加")
    def test_api_ConsoleNotificationInternalService_GetTemplate(self, config_obj, NotificationinternalApi):
        """  获取消息模板详情
route: prefix=console-internal action=Get... """
        template_id = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetTemplateGetApi(template_id=template_id)
        assert resp.status_code == 200

    @pytest.mark.skip("场景测试中添加")
    def test_api_ConsoleNotificationInternalService_CreateTemplate(self, config_obj, NotificationinternalApi):
        """  创建消息模板
route: prefix=console-internal action=Creat... """
        msg_type_id = None
        name = None
        content = None
        sender = None
        id = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_CreateTemplatePostApi(msg_type_id=msg_type_id, name=name, content=content, sender=sender, id=id)
        assert resp.status_code == 200

    @pytest.mark.skip("场景测试中添加")
    def test_api_ConsoleNotificationInternalService_UpdateMsgType(self, config_obj, NotificationinternalApi):
        """  修改消息类型
route: prefix=console-internal action=Updat... """
        msg_type_id = None
        name = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_UpdateMsgTypePostApi(msg_type_id=msg_type_id, name=name)
        assert resp.status_code == 200

    @pytest.mark.skip("场景测试中添加")
    def test_api_ConsoleNotificationInternalService_UpdateTemplate(self, config_obj, NotificationinternalApi):
        """  修改消息模板
route: prefix=console-internal action=Updat... """
        template_id = None
        msg_type_id = None
        name = None
        content = None
        sender = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_UpdateTemplatePostApi(template_id=template_id, msg_type_id=msg_type_id, name=name, content=content, sender=sender)
        assert resp.status_code == 200
