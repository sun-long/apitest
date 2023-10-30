#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestNotificationinternalScenario(object):
    """ Notificationinternal scenario test"""

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
    @pytest.mark.Skiponline
    def test_scenario_000_update_message_type_template(self, NotificationinternalApi, NotificationApi, UserApi):
        """ 修改消息类型，模板"""
        # 1. 创建消息类型
        msgTypeName = "场景测试消息类型1"
        resp = NotificationinternalApi.ConsoleNotificationInternalService_CreateMsgTypePostApi(name=msgTypeName)
        assert resp.status_code == 200
        type_id = resp.json_get("msg_type_info.msg_type_id")

        #1.1.查看消息类型详情
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetMsgTypeGetApi(msg_type_id=type_id)
        assert resp.json_get("msg_type_info.name") == msgTypeName

        # 2. 创建消息模板
        msgTemplateName = "场景测试消息模板1"
        msgTemplateContent = "场景测试消息模板内容：您订阅的{0}服务将于{1}天后到期。"
        sender = "0"
        resp = NotificationinternalApi.ConsoleNotificationInternalService_CreateTemplatePostApi(msg_type_id=type_id,
                                                                                                name=msgTemplateName,
                                                                                                content=msgTemplateContent,
                                                                                                sender=sender)
        assert resp.status_code == 200
        template_id = resp.json_get("template_info.template_id")

        #2.1.查看消息模板详情
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetTemplateGetApi(template_id=template_id)
        assert resp.json_get("template_info.name") == msgTemplateName

        # 3.修改消息类型
        updateMsgName = "修改场景测试消息类型1"
        resp = NotificationinternalApi.ConsoleNotificationInternalService_UpdateMsgTypePostApi(msg_type_id=type_id,
                                                                                               name=updateMsgName)
        assert resp.status_code == 200

        #3.1.查看消息类型详情
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetMsgTypeGetApi(msg_type_id=type_id)
        assert resp.json_get("msg_type_info.name") == updateMsgName

        # 4.修改消息模板
        updateMsgTemplateName = "修改场景测试消息模板1"
        updateMsgTemplateContent = "修改场景测试消息模板内容：您订阅的{0}服务将于{1}天后的{2}小时到期。"
        resp = NotificationinternalApi.ConsoleNotificationInternalService_UpdateTemplatePostApi(template_id=template_id,
                                                                                                msg_type_id=type_id,
                                                                                                name=updateMsgTemplateName,
                                                                                                content=updateMsgTemplateContent,
                                                                                                sender=sender)
        assert resp.status_code == 200

        #4.1.查看消息模板详情
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetTemplateGetApi(template_id=template_id)
        assert resp.json_get("template_info.name") == updateMsgTemplateName

        # 5. 发送消息
        resp = UserApi.ConsoleUserService_GetUserBaseInfoGetApi()
        user_id = resp.json_get("user_id")
        content = "场景测试，10，3"
        resp = NotificationinternalApi.ConsoleNotificationInternalService_SendNotificationPostApi(user_id=user_id,
                                                                                                  template_id=template_id,
                                                                                                  content=content)
        assert resp.status_code == 200
        # 6. 接收消息
        status = None
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = None
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=page_request_total)
        assert resp.status_code == 200
        receive_msg_id = resp.json_get("all_msgs.0.msg_id")

        # 7. 验证消息详情
        contentDetail = content.split(',')
        resp = NotificationApi.ConsoleNotificationService_GetOneMsgGetApi(msg_id=receive_msg_id)
        assert resp.json_get("msg_info.msg_type.name") == updateMsgName
        assert resp.json_get("msg_info.name") == updateMsgTemplateName
        for info in contentDetail:
            if info not in resp.json_get("msg_info.content"):
                assert False

        # 8. 批量删除消息
        all_msg_ids = [receive_msg_id]
        resp = NotificationApi.ConsoleNotificationService_DeleteBatchMsgPostApi(all_msg_ids=all_msg_ids)
        assert resp.status_code == 200

        # 9. 删除消息模板
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteTemplatePostApi(template_id=template_id)
        assert resp.status_code == 200

        # 10. 删除消息类型
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteMsgTypePostApi(msg_type_id=type_id)
        assert resp.status_code == 200

    @pytest.mark.skip("清理数据时可操作")
    def test_scenario_001_message_type_template_clear(self, NotificationinternalApi, NotificationApi, UserApi):
        """ 清理消息类型，模板"""
        # 1. 查找msgTypeId,msgTemplateId
        msgTypeName = "场景测试消息类型1"
        msgTemplateName = "场景测试消息模板1"
        type_id = None
        status = None
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = None
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=page_request_total)
        for n in range(len(resp.json["all_msgs"])):
            if resp.json_get("all_msgs.%d.msg_type.name" % n) == msgTypeName:
                mTypeId = resp.json_get("all_msgs.%d.msg_type.msg_type_id" % n)
                break

        page_request_offset = 0
        page_request_limit = 100
        page_request_total = None
        resp = NotificationinternalApi.ConsoleNotificationInternalService_GetAllTemplateGetApi(
            page_request_offset=page_request_offset, page_request_limit=page_request_limit,
            page_request_total=page_request_total)
        for n in range(len(resp.json["all_templates"])):
            if resp.json_get("all_templates.%d.msg_type.msg_type_id" % n) == mTypeId:
                mTemplateId = resp.json_get("all_templates.%d.template_id" % n)
                break

        # 2.删除消息
        resp = NotificationApi.ConsoleNotificationService_DeleteAllMsgPostApi(msg_type_id=mTypeId)
        assert resp.status_code == 200

        # 3.删除消息模板
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteTemplatePostApi(
            template_id=mTemplateId)
        assert resp.status_code == 200

        # 4.删除消息类型
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteMsgTypePostApi(
            msg_type_id=mTypeId)
        assert resp.status_code == 200
