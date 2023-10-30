#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestNotificationApi(object):
    """ notification Api测试"""

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
    def test_api_ConsoleNotificationService_GetAllMsg(self, config_obj, NotificationApi):
        """  拉取消息列表
route: prefix=console action=GetAllMsg vers... """
        msg_type_id = None
        status = None
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = None
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=msg_type_id, status=status, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    @pytest.mark.skip("不可逆操作，会在场景测试中考虑添加")
    def test_api_ConsoleNotificationService_DeleteAllMsg(self, config_obj, NotificationApi):
        """  删除全部消息
route: prefix=console action=DeleteAllMsg v... """
        msg_type_id = None
        resp = NotificationApi.ConsoleNotificationService_DeleteAllMsgPostApi(msg_type_id="456912671699139055")
        assert resp.status_code == 200

    @pytest.mark.skip("不可逆操作，会在场景测试中考虑添加")
    def test_api_ConsoleNotificationService_DeleteBatchMsg(self, config_obj, NotificationApi):
        """  批量删除消息
route: prefix=console action=DeleteBatchMsg... """
        all_msg_ids = None
        resp = NotificationApi.ConsoleNotificationService_DeleteBatchMsgPostApi(all_msg_ids=all_msg_ids)
        assert resp.status_code == 200

    @pytest.mark.skip("场景测试中添加")
    def test_api_ConsoleNotificationService_GetOneMsg(self, config_obj, NotificationApi):
        """  获取消息详情
route: prefix=console action=GetOneMsg vers... """
        msg_id = None
        resp = NotificationApi.ConsoleNotificationService_GetOneMsgGetApi(msg_id=msg_id)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_api_ConsoleNotificationService_GetAllMsgType(self, config_obj, NotificationApi):
        """  拉取消息类型列表
route: prefix=console action=GetAllMsgTyp... """
        page_request_offset = 0
        page_request_limit = 100
        page_request_total = None
        resp = NotificationApi.ConsoleNotificationService_GetAllMsgTypeGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_api_ConsoleNotificationService_GetUnReadCount(self, config_obj, NotificationApi):
        """  获取未读消息数
route: prefix=console action=GetUnReadCoun... """
        resp = NotificationApi.ConsoleNotificationService_GetUnReadCountGetApi()
        assert resp.status_code == 200

    @pytest.mark.skip("不可逆操作，会在场景测试中考虑添加")
    def test_api_ConsoleNotificationService_ReadAllMsg(self, config_obj, NotificationApi):
        """  全部标记为已读
route: prefix=console action=ReadAllMsg ve... """
        msg_type_id = None
        resp = NotificationApi.ConsoleNotificationService_ReadAllMsgPostApi(msg_type_id=msg_type_id)
        assert resp.status_code == 200

    @pytest.mark.skip("不可逆操作，会在场景测试中考虑添加")
    def test_api_ConsoleNotificationService_ReadBatchMsg(self, config_obj, NotificationApi):
        """  批量标记为已读
route: prefix=console action=ReadBatchMsg ... """
        all_msg_ids = None
        resp = NotificationApi.ConsoleNotificationService_ReadBatchMsgPostApi(all_msg_ids=all_msg_ids)
        assert resp.status_code == 200
