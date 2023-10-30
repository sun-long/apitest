#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestVideomanagerApi(object):
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

    def test_api_VideoManagerCenter_CancelRecordTask(self, config_obj, VideomanagerApi):
        """  取消录播task
route: prefix=, internal_prefix=video, ac... """
        task_id = "cb678d28ea35490cb5274726faa29eb3"
        resp = VideomanagerApi.VideoManagerCenter_CancelRecordTaskPostApi(task_id=task_id)
        assert resp.status_code == 200

    def test_api_VideoManagerCenter_CreateRecordTask(self, config_obj, VideomanagerApi):
        """  创建录播task
route: prefix=, internal_prefix=video, ac... """
        device_id = None
        ingress_id = None
        start_time = None
        end_time = None
        template = None
        keep_days = None
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id, ingress_id=ingress_id, start_time=start_time, end_time=end_time, template=template, keep_days=keep_days)
        assert resp.status_code == 200

    def test_api_VideoManagerCenter_CreateTask(self, config_obj, VideomanagerApi):
        """  创建task
route: prefix=, internal_prefix=video, acti... """
        device_id = None
        ingress_ids = None
        resp = VideomanagerApi.VideoManagerCenter_CreateTaskPostApi(device_id=device_id, ingress_ids=ingress_ids)
        assert resp.status_code == 200

    def test_api_VideoManagerCenter_DeleteTask(self, config_obj, VideomanagerApi):
        """  删除task
route: prefix=, internal_prefix=video, acti... """
        task_id = None
        resp = VideomanagerApi.VideoManagerCenter_DeleteTaskPostApi(task_id=task_id)
        assert resp.status_code == 200

    def test_api_VideoManagerCenter_GeneratePlayAddress(self, config_obj, VideomanagerApi):
        """  生成播放地址
route: prefix=, internal_prefix=video, acti... """
        task_id = None
        protocol = None
        duration = None
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id, protocol=protocol, duration=duration)
        assert resp.status_code == 200

    def test_api_VideoManagerCenter_GetRecordTasks(self, config_obj, VideomanagerApi):
        """  获取录播task列表
route: prefix=, internal_prefix=video, ... """
        # task_ids = ["faafd3a72bcb4cc2801735fd0ce67d38"]
        # task_ids = ["08236f3ea4bb4e24807a15c7634ad9f8", # 7天
        #             "69b9410026f147e0a5d5d9ec290e576f", # 7
        #             "93cb72f4ec5540e686d4105dc63b1cf0", #30
        #             "894e8f1fd59847a9b9869b41c17caf6c", # 1
        #             ]
        task_ids = [
            # "502dd977613c44ffa5ec00f95a10d06b", #7.11
            #         "e5b2b86908a640d886b2c154b67bb4e2", #live55
            # "19cefe744f7e4e9ebaecb7e29b017d75"
                    ]
        # task_ids = ["b207582ef1534a728f6495fd6de21dd6"]
        # task_ids = ["057b2f51349249d9b3b2b41140ead251", "7effb82cdd774e149af242d72bcd907f"]
        # task_ids = None
        device_ids = None
        paging_offset = None
        paging_limit = 51
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200
        res = ""
        log().info("count=%s" % len(resp.json_get("tasks")))
        for task in resp.json_get("tasks"):
            res += "\n%s:%s:%s:%s-%s:%s:%s" % (task["id"],
                                         task["status"],
                                         task["keep_days"],
                                         task["start_time"],
                                         task["end_time"],
                                        task["device_id"],
                                           len(task["record_files"]),

                                         )
        log().info(res)

        """
        public endpoint：https://s3-eg-cn-shanghai-1.test.sensebelt.net
        ak: vDETkb8Qg7waFjQH
        sk: 8mUJbGyeNgXUkDzR2S7HQJqRdmrn2apY
        bucket: video-manager
        """

    def test_api_VideoManagerCenter_GetTasks(self, config_obj, VideomanagerApi):
        """  获取task列表
route: prefix=, internal_prefix=video, ac... """
        task_ids = None
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi(task_ids=task_ids, device_ids=device_ids, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200
