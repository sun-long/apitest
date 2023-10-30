#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestVideomanagerParam(object):
    """ videoManager Param测试"""

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
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
    ])
    def test_api_VideoManagerCenter_CancelRecordTaskInvalidParam(self, invalidParam, config_obj, VideomanagerApi):
        """  取消录播task
route: prefix=, internal_prefix=video, ac... """
        task_id = None
        intef = VideomanagerApi.VideoManagerCenter_CancelRecordTaskPostApi(task_id=task_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('ingress_id', 'invalidingress_id'),
        ('start_time', 'invalidstart_time'),
        ('start_time', ''),
        ('start_time', None),
        ('start_time', -1),
        ['start_time', "当前时间+9分59秒"],
        ['start_time', "当前时间-5分钟"],
        ('end_time', 'invalidend_time'),
        ('end_time', ''),
        ('end_time', -1),
        ('end_time', None),
        ['end_time', "start_time+59分59秒"],
        ['end_time', "start_time+24小时00分1秒"],
        ['end_time', "当前时间-5分钟"],
        ['keep_days', 'invalidkeep_days'],
        # ('keep_days', 0),
        ('keep_days', -1),
        ('keep_days', 31),
    ])
    def test_api_VideoManagerCenter_CreateRecordTaskInvalidParam(self, invalidParam, config_obj, VideomanagerApi,
                                                                 recordTaskCamera_info):
        """  创建录播task
route: prefix=, internal_prefix=video, ac... """
        device_id = recordTaskCamera_info.device_id
        ingress_id = None
        start_time = time_utils.get_str_by_timestamp(offset=10 * 60 + 10, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=1 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config": {
                "use_origin": True
            },
            "audio_config": {
                "use_origin": True
            },
            "format": "MP4"
        }
        keep_days = 7
        intef = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id, ingress_id=ingress_id, start_time=start_time, end_time=end_time, template=template, keep_days=keep_days, sendRequest=False)
        if invalidParam[0] == "start_time" and invalidParam[1] == "当前时间+9分59秒":
            invalidParam[1] = time_utils.get_str_by_timestamp(offset=9*60 + 59, formate="%Y-%m-%dT%H:%M:%SZ")
            end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=1 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        elif invalidParam[0] == "start_time" and invalidParam[1] == "当前时间-5分钟":
            invalidParam[1] = time_utils.get_str_by_timestamp(offset=-5 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
            end_time = time_utils.get_str_by_timestamp(offset=1 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        elif invalidParam[0] == "end_time" and invalidParam[1] == "start_time+59分59秒":
            start_time = time_utils.get_str_by_timestamp(offset=10 * 60 + 10, formate="%Y-%m-%dT%H:%M:%SZ")
            invalidParam[1] = time_utils.get_str_by_timestamp(ts=start_time, offset=59 * 60 +59, formate="%Y-%m-%dT%H:%M:%SZ")
        elif invalidParam[0] == "end_time" and invalidParam[1] == "start_time+24小时00分1秒":
            start_time = time_utils.get_str_by_timestamp(offset=10 * 60 + 10, formate="%Y-%m-%dT%H:%M:%SZ")
            invalidParam[1] = time_utils.get_str_by_timestamp(ts=start_time, offset=24 * 60 * 60 + 60, formate="%Y-%m-%dT%H:%M:%SZ")
        elif invalidParam[0] == "end_time" and invalidParam[1] == "当前时间-5分钟":
            start_time = time_utils.get_str_by_timestamp(offset=10 * 60 + 10, formate="%Y-%m-%dT%H:%M:%SZ")
            invalidParam[1] = time_utils.get_str_by_timestamp(offset=-5 * 60, formate="%Y-%m-%dT%H:%M:%SZ")

        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('ingress_ids', ['invalidingress_ids']),
    ])
    def test_api_VideoManagerCenter_CreateTaskInvalidParam(self, invalidParam, config_obj,DeviceApi, VideomanagerApi,
                                                           AideBotInfo, camera_info, cluster_info):
        """  创建task
route: prefix=, internal_prefix=video, acti... """
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info=camera_info, cluster_info=cluster_info)
        ingress_ids = None
        intef = VideomanagerApi.VideoManagerCenter_CreateTaskPostApi(device_id=device_id, ingress_ids=ingress_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
    ])
    def test_api_VideoManagerCenter_DeleteTaskInvalidParam(self, invalidParam, config_obj, VideomanagerApi):
        """  删除task
route: prefix=, internal_prefix=video, acti... """
        task_id = None
        intef = VideomanagerApi.VideoManagerCenter_DeleteTaskPostApi(task_id=task_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
        ('protocol', 'invalidprotocol'),
        ('protocol', 'Rtmp'),
        ('protocol', 'rtmp'),
        ('protocol', 'rtsp'),
        ('protocol', ''),
        ('protocol', None),
        ('duration', 'invalidduration'),
        ('duration', ''),
        ('duration', None),
    ])
    def test_api_VideoManagerCenter_GeneratePlayAddressInvalidParam(self, invalidParam, config_obj, VideomanagerApi,
                                                                    AideBotInfo, DeviceApi, camera_info,cluster_info):
        """  生成播放地址
route: prefix=, internal_prefix=video, acti... """
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info=camera_info, cluster_info=cluster_info)
        # 2.创建视频任务
        resp = VideomanagerApi.createTask(device_id=device_id)
        task_id = resp.json_get("task.id")
        # 3. 查询任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id])
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.id") == task_id

        protocol = None
        duration = None
        intef = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id, protocol=protocol, duration=duration, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
        ('device_ids', 'invaliddevice_ids'),
        ('device_ids', ''),
        ('device_ids', None),
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
    ])
    def test_api_VideoManagerCenter_GetRecordTasksInvalidParam(self, invalidParam, config_obj, VideomanagerApi):
        """  获取录播task列表
route: prefix=, internal_prefix=video, ... """
        task_ids = None
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                        paging_offset=paging_offset,
                                                                        paging_limit=paging_limit,
                                                                        paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', ['invalidtask_ids']),
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('device_ids', ['invaliddevice_ids']),
        ('device_ids', 'invaliddevice_ids'),
        ('device_ids', ''),
    ])
    def test_api_VideoManagerCenter_GetTasksInvalidParam(self, invalidParam, config_obj, VideomanagerApi):
        """  获取task列表
route: prefix=, internal_prefix=video, ac... """
        task_ids = None
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = VideomanagerApi.VideoManagerCenter_GetTasksGetApi(task_ids=task_ids, device_ids=device_ids, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code == 200
        assert not resp.json_get("tasks")
