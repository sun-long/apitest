#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestNotificationParam(object):
    """ notification Param测试"""

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
        ('msg_type_id', 'invalidmsg_type_id'),
        ('msg_type_id', ''),
        ('msg_type_id', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
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
    def test_api_ConsoleNotificationService_GetAllMsgInvalidParam(self, invalidParam, config_obj, NotificationApi):
        """  拉取消息列表
route: prefix=console action=GetAllMsg vers... """
        msg_type_id = None
        status = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = NotificationApi.ConsoleNotificationService_GetAllMsgGetApi(msg_type_id=msg_type_id, status=status, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('msg_type_id', 'invalidmsg_type_id'),
        ('msg_type_id', ''),
        ('msg_type_id', None),
    ])
    def test_api_ConsoleNotificationService_DeleteAllMsgInvalidParam(self, invalidParam, config_obj, NotificationApi):
        """  删除全部消息
route: prefix=console action=DeleteAllMsg v... """
        msg_type_id = None
        intef = NotificationApi.ConsoleNotificationService_DeleteAllMsgPostApi(msg_type_id=msg_type_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('all_msg_ids', 'invalidall_msg_ids'),
        ('all_msg_ids', ''),
        ('all_msg_ids', None),
    ])
    def test_api_ConsoleNotificationService_DeleteBatchMsgInvalidParam(self, invalidParam, config_obj, NotificationApi):
        """  批量删除消息
route: prefix=console action=DeleteBatchMsg... """
        all_msg_ids = None
        intef = NotificationApi.ConsoleNotificationService_DeleteBatchMsgPostApi(all_msg_ids=all_msg_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('msg_id', 'invalidmsg_id'),
        ('msg_id', ''),
        ('msg_id', None),
    ])
    def test_api_ConsoleNotificationService_GetOneMsgInvalidParam(self, invalidParam, config_obj, NotificationApi):
        """  获取消息详情
route: prefix=console action=GetOneMsg vers... """
        msg_id = None
        intef = NotificationApi.ConsoleNotificationService_GetOneMsgGetApi(msg_id=msg_id, sendRequest=False)
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
    def test_api_ConsoleNotificationService_GetAllMsgTypeInvalidParam(self, invalidParam, config_obj, NotificationApi):
        """  拉取消息类型列表
route: prefix=console action=GetAllMsgTyp... """
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = NotificationApi.ConsoleNotificationService_GetAllMsgTypeGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ConsoleNotificationService_GetUnReadCountInvalidParam(self, invalidParam, config_obj, NotificationApi):
        """  获取未读消息数
route: prefix=console action=GetUnReadCoun... """
        intef = NotificationApi.ConsoleNotificationService_GetUnReadCountGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('msg_type_id', 'invalidmsg_type_id'),
        ('msg_type_id', ''),
        ('msg_type_id', None),
    ])
    def test_api_ConsoleNotificationService_ReadAllMsgInvalidParam(self, invalidParam, config_obj, NotificationApi):
        """  全部标记为已读
route: prefix=console action=ReadAllMsg ve... """
        msg_type_id = None
        intef = NotificationApi.ConsoleNotificationService_ReadAllMsgPostApi(msg_type_id=msg_type_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('all_msg_ids', 'invalidall_msg_ids'),
        ('all_msg_ids', ''),
        ('all_msg_ids', None),
    ])
    def test_api_ConsoleNotificationService_ReadBatchMsgInvalidParam(self, invalidParam, config_obj, NotificationApi):
        """  批量标记为已读
route: prefix=console action=ReadBatchMsg ... """
        all_msg_ids = None
        intef = NotificationApi.ConsoleNotificationService_ReadBatchMsgPostApi(all_msg_ids=all_msg_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
