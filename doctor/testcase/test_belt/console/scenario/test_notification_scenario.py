#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.Skiponline
class TestNotificationScenario(object):
    """ Notification scenario test"""

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

    def test_demo(self, demoClass, demoFunction):
        """ demo setup teardown"""
        log().info("cases......")

    # def test_demo_login(self, NotificationApi, UserApi):
    #     """ 切换用户/token 伪代码"""
    #     resp = UserApi.login(username="11", password="222")
    #     token = resp.json_get("token")
    #     # 用新token调用接口
    #     resp = NotificationApi.ConsoleNotificationService_GetUnReadCountGetApi(loginToken=token)

    @pytest.mark.ConsoleRegression
    def test_scenario_000_send_receive_message(self, NotificationinternalApi, NotificationApi, UserApi):
        """ 收发消息"""
        # 1. 创建消息类型
        msgTypeName = "场景测试消息类型1"
        resp = NotificationinternalApi.ConsoleNotificationInternalService_CreateMsgTypePostApi(name=msgTypeName)
        assert resp.status_code == 200
        type_id = resp.json_get("msg_type_info.msg_type_id")

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

        # 3. 发送消息
        resp = UserApi.ConsoleUserService_GetUserBaseInfoGetApi()
        user_id = resp.json_get("user_id")
        content = "场景测试，10"
        resp = NotificationinternalApi.ConsoleNotificationInternalService_SendNotificationPostApi(user_id=user_id,
                                                                                                  template_id=template_id,
                                                                                                  content=content)
        assert resp.status_code == 200
        # 4. 接收消息
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

        # 5. 验证消息详情
        contentDetail = content.split(',')
        resp = NotificationApi.ConsoleNotificationService_GetOneMsgGetApi(msg_id=receive_msg_id)
        for info in contentDetail:
            if info not in resp.json_get("msg_info.content"):
                assert False

        # 6. 批量删除消息
        all_msg_ids = [receive_msg_id]
        resp = NotificationApi.ConsoleNotificationService_DeleteBatchMsgPostApi(all_msg_ids=all_msg_ids)
        assert resp.status_code == 200

        # 7. 删除消息模板
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteTemplatePostApi(template_id=template_id)
        assert resp.status_code == 200

        # 8. 删除消息类型
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteMsgTypePostApi(msg_type_id=type_id)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_scenario_001_markRead_message(self, NotificationinternalApi, NotificationApi, UserApi):
        """ 消息批量标记已读"""
        # 1. 创建消息类型
        msgTypeName = "场景测试消息类型1"
        resp = NotificationinternalApi.ConsoleNotificationInternalService_CreateMsgTypePostApi(name=msgTypeName)
        assert resp.status_code == 200
        type_id = resp.json_get("msg_type_info.msg_type_id")

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

        # 3. 发送消息
        resp = UserApi.ConsoleUserService_GetUserBaseInfoGetApi()
        user_id = resp.json_get("user_id")
        content = "场景测试，10"
        resp = NotificationinternalApi.ConsoleNotificationInternalService_SendNotificationPostApi(user_id=user_id,
                                                                                                  template_id=template_id,
                                                                                                  content=content)
        assert resp.status_code == 200
        # 4. 获取消息id
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
        all_msg_ids = [receive_msg_id]

        # 5.获取未读消息数
        resp = NotificationApi.ConsoleNotificationService_GetUnReadCountGetApi()
        assert resp.status_code == 200
        preUnReadNum = resp.json_get("count")

        # 6.标记消息为已读
        resp = NotificationApi.ConsoleNotificationService_ReadBatchMsgPostApi(all_msg_ids=all_msg_ids)
        assert resp.status_code == 200

        # 7. 验证消息已读
        resp = NotificationApi.ConsoleNotificationService_GetOneMsgGetApi(msg_id=receive_msg_id)
        assert resp.json_get("msg_info.status") == "STATUS_READ"

        # 8.获取未读消息数
        resp = NotificationApi.ConsoleNotificationService_GetUnReadCountGetApi()
        assert resp.status_code == 200
        postUnReadNum = resp.json_get("count")

        assert int(postUnReadNum) == int(preUnReadNum) - 1

        # 9. 批量删除消息
        resp = NotificationApi.ConsoleNotificationService_DeleteBatchMsgPostApi(all_msg_ids=all_msg_ids)
        assert resp.status_code == 200

        # 10. 删除消息模板
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteTemplatePostApi(template_id=template_id)
        assert resp.status_code == 200

        # 11. 删除消息类型
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteMsgTypePostApi(msg_type_id=type_id)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_scenario_002_markAllRead_message(self, NotificationinternalApi, NotificationApi, UserApi):
        """ 消息全部标记已读，全部删除"""
        # 1. 创建消息类型
        msgTypeName = "场景测试消息类型1"
        resp = NotificationinternalApi.ConsoleNotificationInternalService_CreateMsgTypePostApi(name=msgTypeName)
        assert resp.status_code == 200
        type_id = resp.json_get("msg_type_info.msg_type_id")

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

        # 3. 发送消息
        resp = UserApi.ConsoleUserService_GetUserBaseInfoGetApi()
        user_id = resp.json_get("user_id")
        content = "场景测试，10"
        num = 3
        for index in range(num):
            resp = NotificationinternalApi.ConsoleNotificationInternalService_SendNotificationPostApi(user_id=user_id,
                                                                                                      template_id=template_id,
                                                                                                      content=content)

        assert resp.status_code == 200

        # 4.获取未读消息数
        resp = NotificationApi.ConsoleNotificationService_GetUnReadCountGetApi()
        assert resp.status_code == 200
        preUnReadNum = resp.json_get("count")

        # 5. 消息标记已读
        status = None
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = None
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=page_request_total)
        assert resp.status_code == 200
        receive_msg_id_l = []
        for i in range(len(resp.json["all_msgs"])):
            receive_msg_id_l.append(resp.json_get("all_msgs.%d.msg_id" % i))

        resp = NotificationApi.ConsoleNotificationService_ReadAllMsgPostApi(msg_type_id=type_id)
        assert resp.status_code == 200

        # 6. 验证消息已读
        for m in range(len(receive_msg_id_l)):
            resp = NotificationApi.ConsoleNotificationService_GetOneMsgGetApi(msg_id=receive_msg_id_l[m])
            assert resp.json_get("msg_info.status") == "STATUS_READ"

        # 7.获取未读消息数
        resp = NotificationApi.ConsoleNotificationService_GetUnReadCountGetApi()
        assert resp.status_code == 200
        postUnReadNum = resp.json_get("count")
        assert int(postUnReadNum) == int(preUnReadNum) - num

        # 8. 删除全部消息
        resp = NotificationApi.ConsoleNotificationService_DeleteAllMsgPostApi(msg_type_id=type_id)
        assert resp.status_code == 200

        # 9. 删除消息模板
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteTemplatePostApi(template_id=template_id)
        assert resp.status_code == 200

        # 10. 删除消息类型
        resp = NotificationinternalApi.ConsoleNotificationInternalService_DeleteMsgTypePostApi(msg_type_id=type_id)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_scenario_003_message_page(self, NotificationinternalApi, NotificationApi, UserApi):
        """ 消息分页"""
        type_id = None
        status = None
        page_request_offset = 0
        page_request_limit = 1
        page_request_total = None
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=page_request_total)
        assert resp.status_code == 200
        assert len(resp.json["all_msgs"]) == 1

    @pytest.mark.ConsoleRegression
    def test_scenario_004_message_page(self, NotificationinternalApi, NotificationApi, UserApi):
        """ 消息分页第二页"""
        type_id = None
        status = None
        page_request_offset = 1
        page_request_limit = 1
        page_request_total = None
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=page_request_total)
        assert resp.status_code == 200
        one_msg_id = resp.json_get("all_msgs.0.msg_id")
        page_request_offset = 0
        page_request_limit = 2
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=page_request_total)
        two_msg_id = resp.json_get("all_msgs.1.msg_id")
        assert one_msg_id == two_msg_id

    @pytest.mark.ConsoleRegression
    def test_scenario_005_message_search(self, NotificationinternalApi, NotificationApi, UserApi):
        """ 消息查看_已读"""
        type_id = None
        status = "STATUS_READ"
        page_request_offset = 0
        page_request_limit = 1
        page_request_total = None
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=page_request_total)
        assert resp.status_code == 200
        for i in range(page_request_limit):
            assert resp.json_get("all_msgs.%d.status" % i) == status

    @pytest.mark.ConsoleRegression
    def test_scenario_006_message_search(self, NotificationinternalApi, NotificationApi, UserApi):
        """ 消息查看_未读"""
        type_id = None
        status = "STATUS_UNREAD"
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = None
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=type_id, status=status,
                                                                          page_request_offset=page_request_offset,
                                                                          page_request_limit=page_request_limit,
                                                                          page_request_total=page_request_total)
        assert resp.status_code == 200
        for m in range(len("all_msgs")):
            assert resp.json_get("all_msgs.%d.status" % m) == status
