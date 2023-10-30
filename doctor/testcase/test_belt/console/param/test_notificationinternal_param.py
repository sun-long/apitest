#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestNotificationinternalParam(object):
    """ notificationInternal Param测试"""

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
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('template_id', 'invalidtemplate_id'),
        ('template_id', ''),
        ('template_id', None),
        ('content', 'invalidcontent'),
        ('content', ''),
        ('content', None),
    ])
    def test_api_ConsoleNotificationInternalService_SendNotificationInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  发送系统消息
route: prefix=console-internal action=SendN... """
        user_id = None
        template_id = None
        content = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_SendNotificationPostApi(user_id=user_id, template_id=template_id, content=content, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
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
    def test_api_ConsoleNotificationInternalService_GetAllMsgTypeInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  拉取消息类型列表
route: prefix=console-internal action=Get... """
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_GetAllMsgTypeGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
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
    def test_api_ConsoleNotificationInternalService_GetAllTemplateInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  拉取消息模板列表
route: prefix=console-internal action=Get... """
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_GetAllTemplateGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('msg_type_id', 'invalidmsg_type_id'),
        ('msg_type_id', ''),
        ('msg_type_id', None),
    ])
    def test_api_ConsoleNotificationInternalService_DeleteMsgTypeInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  删除消息类型
route: prefix=console-internal action=Delet... """
        msg_type_id = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_DeleteMsgTypePostApi(msg_type_id=msg_type_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('template_id', 'invalidtemplate_id'),
        ('template_id', ''),
        ('template_id', None),
    ])
    def test_api_ConsoleNotificationInternalService_DeleteTemplateInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  删除消息模板
route: prefix=console-internal action=Delet... """
        template_id = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_DeleteTemplatePostApi(template_id=template_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('msg_type_id', 'invalidmsg_type_id'),
        ('msg_type_id', ''),
        ('msg_type_id', None),
    ])
    def test_api_ConsoleNotificationInternalService_GetMsgTypeInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  获取消息类型详情
route: prefix=console-internal action=Get... """
        msg_type_id = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_GetMsgTypeGetApi(msg_type_id=msg_type_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_ConsoleNotificationInternalService_CreateMsgTypeInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  添加消息类型
route: prefix=console-internal action=Creat... """
        name = None
        id = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_CreateMsgTypePostApi(name=name, id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('template_id', 'invalidtemplate_id'),
        ('template_id', ''),
        ('template_id', None),
    ])
    def test_api_ConsoleNotificationInternalService_GetTemplateInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  获取消息模板详情
route: prefix=console-internal action=Get... """
        template_id = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_GetTemplateGetApi(template_id=template_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('msg_type_id', 'invalidmsg_type_id'),
        ('msg_type_id', ''),
        ('msg_type_id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('content', 'invalidcontent'),
        ('content', ''),
        ('content', None),
        ('sender', 'invalidsender'),
        ('sender', ''),
        ('sender', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_ConsoleNotificationInternalService_CreateTemplateInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  创建消息模板
route: prefix=console-internal action=Creat... """
        msg_type_id = None
        name = None
        content = None
        sender = None
        id = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_CreateTemplatePostApi(msg_type_id=msg_type_id, name=name, content=content, sender=sender, id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('msg_type_id', 'invalidmsg_type_id'),
        ('msg_type_id', ''),
        ('msg_type_id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
    ])
    def test_api_ConsoleNotificationInternalService_UpdateMsgTypeInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  修改消息类型
route: prefix=console-internal action=Updat... """
        msg_type_id = None
        name = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_UpdateMsgTypePostApi(msg_type_id=msg_type_id, name=name, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('template_id', 'invalidtemplate_id'),
        ('template_id', ''),
        ('template_id', None),
        ('msg_type_id', 'invalidmsg_type_id'),
        ('msg_type_id', ''),
        ('msg_type_id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('content', 'invalidcontent'),
        ('content', ''),
        ('content', None),
        ('sender', 'invalidsender'),
        ('sender', ''),
        ('sender', None),
    ])
    def test_api_ConsoleNotificationInternalService_UpdateTemplateInvalidParam(self, invalidParam, config_obj, NotificationinternalApi):
        """  修改消息模板
route: prefix=console-internal action=Updat... """
        template_id = None
        msg_type_id = None
        name = None
        content = None
        sender = None
        intef = NotificationinternalApi.ConsoleNotificationInternalService_UpdateTemplatePostApi(template_id=template_id, msg_type_id=msg_type_id, name=name, content=content, sender=sender, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
