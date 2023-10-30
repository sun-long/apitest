#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.checkin
class TestVideomanagerCheckIn(object):
    """ videoManager Api测试"""

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

    def test_api_VideoManagerCenter_CreateTask(self, config_obj, VideomanagerApi):
        """  创建task"""
        device_id = "1234"
        ingress_ids = None
        resp = VideomanagerApi.VideoManagerCenter_CreateTaskPostApi(device_id=device_id, ingress_ids=ingress_ids)
        assert resp.status_code == 404
        assert resp.json_get("error.message") == "device not found"

    def test_api_VideoManagerCenter_DeleteTask(self, config_obj, VideomanagerApi):
        """  删除task"""
        task_id = "1234"
        resp = VideomanagerApi.VideoManagerCenter_DeleteTaskPostApi(task_id=task_id)
        assert resp.status_code == 404
        assert resp.json_get("error.details.0.message") == "task not found"
        assert resp.json_get("error.details.0.reason") == 11501001

    def test_api_VideoManagerCenter_GeneratePlayAddress(self, config_obj, VideomanagerApi):
        """  生成播放地址 """
        task_id = None
        protocol = None
        duration = None
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id, protocol=protocol, duration=duration)
        assert resp.status_code == 400
        assert resp.json_get("error.message") == "video task argument invalid"

    def test_api_VideoManagerCenter_GetTasks(self, config_obj, VideomanagerApi):
        """  获取task列表"""
        task_ids = None
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                 paging_offset=paging_offset,
                                                                 paging_limit=paging_limit,
                                                                 paging_total=paging_total)
        assert resp.status_code == 200
