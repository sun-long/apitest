#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

import pytest
from pytest_check import check
from commonlib import config, time_utils, sign_utils, utils
from commonlib.log_utils import log
# from commonlib.ocr_demo import rtsp_check


@pytest.mark.P0
@pytest.mark.Regression
class TestVideomanagerScenario(object):
    """ Videomanager scenario test"""

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

    def test_scenario_000_taskCrdWithRtsp(self, RasmanagerAideApi, VideomanagerApi, config_obj, DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 视频直播crd,设备中只有1个ingress"""
        is_delete = True
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info=camera_info, cluster_info=cluster_info, is_delete=is_delete)
        # 2.创建视频任务
        resp = VideomanagerApi.createTask(device_id=device_id, is_delete=is_delete)
        task_id = resp.json_get("task.id")

        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        driver_id = resp.json_get("device_detail.device.driver.driver_id")
        ingress_id = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")

        # 3. 查询任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id])
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.id") == task_id
        assert resp.json_get("tasks.0.device_id") == device_id
        assert resp.json_get("tasks.0.ingresses.0.ingress_id") == ingress_id
        assert resp.json_get("tasks.0.ingresses.0.status") == "AVAILABLE"

        # 4.生成播放地址
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id,protocol="RTMP",duration="NO_EXPIRED")
        assert resp.status_code == 200
        assert resp.json_get("url")

        # url = resp.json_get("url")
        # save_path = os.path.join(config.temp_path, "test.jpg")
        # if os.path.exists(save_path):
        #     os.remove(save_path)
        # try:
        #     rtsp_check.get_img_from_camera_net_1(url, save_path)
        # except Exception as e:
        #     assert None, "解析生成播放地址失败"
        # assert os.path.exists(save_path), "%s 未生成视频图片" % save_path

        # 5. 删除任务
        resp = VideomanagerApi.VideoManagerCenter_DeleteTaskPostApi(task_id=task_id)
        assert resp.status_code == 200

        # 6.查询任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id])
        assert resp.status_code == 200
        assert not resp.json_get("tasks"), "任务未删除成功"
        # save_path = os.path.join(config.temp_path, "test_1.jpg")
        # if os.path.exists(save_path):
        #     os.remove(save_path)
        # try:
        #     rtsp_check.get_img_from_camera_net(url, save_path)
        # except Exception as e:
        #     pass
        # assert not os.path.exists(save_path), "%s 视频仍然能播放" % save_path

    def test_scenario_001_taskCrdWithRtsp_2(self, VideomanagerApi, RasmanagerAideApi,config_obj, DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 视频直播crd, 设备中存在多个ingress"""
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        driver = {
            "enable": True,
            "ingresses": [
                {
                    "information": {
                        "rtsp": {
                            "source_url": camera_info["rtsp"]
                        },
                        "type": camera_info["type"]
                    },
                    "name": "ingress_1_%s" % time_utils.get_str_by_timestamp(formate="%Y%m%d%H%M%S"),
                    "description": ""
                },
                {
                    "information": {
                        "rtsp": {
                            "source_url": camera_info["rtsp"]
                        },
                        "type": camera_info["type"]
                    },
                    "name": "ingress_2_%s" % time_utils.get_str_by_timestamp(formate="%Y%m%d%H%M%S"),
                    "description": ""
                }
            ],
        }
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, driver=driver, camera_info=camera_info, cluster_info=cluster_info)
        # 2.查询ingress_id
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        ingress_id_1 = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")
        ingress_id_2 = resp.json_get("device_detail.device.driver.ingresses.1.ingress_id")
        # 2.创建视频任务1
        resp = VideomanagerApi.createTask(device_id=device_id, ingress_ids=[ingress_id_1])
        task_id = resp.json_get("task.id")

        # 2.创建视频任务2
        resp = VideomanagerApi.createTask(device_id=device_id, ingress_ids=[ingress_id_2])
        task_id2 = resp.json_get("task.id")

        # 3. 查询任务1
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id])
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.id") == task_id
        # 3. 查询任务2
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id2])
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.id") == task_id2

        # 根据deviceid查询 应能查出2个任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi(device_ids=[device_id])
        assert resp.status_code == 200
        assert len(resp.json_get("tasks")) == 2

        # 4.生成播放地址1
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id,protocol="RTMP",duration="NO_EXPIRED")
        assert resp.status_code == 200

        # url = resp.json_get("url")
        # save_path = os.path.join(config.temp_path, "test.jpg")
        # if os.path.exists(save_path):
        #     os.remove(save_path)
        # try:
        #     rtsp_check.get_img_from_camera_net_1(url, save_path)
        # except Exception as e:
        #     assert None, "解析生成播放地址失败"
        # assert os.path.exists(save_path), "%s 未生成视频图片" % save_path

        # 4.生成播放地址2
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id2, protocol="RTMP",
                                                                             duration="NO_EXPIRED")
        assert resp.status_code == 200

        # url = resp.json_get("url")
        # save_path = os.path.join(config.temp_path, "test.jpg")
        # if os.path.exists(save_path):
        #     os.remove(save_path)
        # try:
        #     rtsp_check.get_img_from_camera_net_1(url, save_path)
        # except Exception as e:
        #     assert None, "解析生成播放地址失败"
        # assert os.path.exists(save_path), "%s 未生成视频图片" % save_path


        # 5. 删除任务1
        resp = VideomanagerApi.VideoManagerCenter_DeleteTaskPostApi(task_id=task_id)
        assert resp.status_code == 200

        # 根据deviceid查询 应能查出1个任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi(device_ids=[device_id])
        assert resp.status_code == 200
        assert len(resp.json_get("tasks")) == 1

        # 5. 删除任务2
        resp = VideomanagerApi.VideoManagerCenter_DeleteTaskPostApi(task_id=task_id2)
        assert resp.status_code == 200

        # 6.查询任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id])
        assert resp.status_code == 200
        assert not resp.json_get("tasks"), "任务未删除成功"
        # save_path = os.path.join(config.temp_path, "test_1.jpg")
        # if os.path.exists(save_path):
        #     os.remove(save_path)
        # try:
        #     rtsp_check.get_img_from_camera_net(url, save_path)
        # except Exception as e:
        #     pass
        # assert not os.path.exists(save_path), "%s 视频仍然能播放" % save_path
        # 6.查询任务2
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id2])
        assert resp.status_code == 200
        assert not resp.json_get("tasks"), "任务未删除成功"
        # save_path = os.path.join(config.temp_path, "test_1.jpg")
        # if os.path.exists(save_path):
        #     os.remove(save_path)
        # try:
        #     rtsp_check.get_img_from_camera_net(url, save_path)
        # except Exception as e:
        #     pass
        # assert not os.path.exists(save_path), "%s 视频仍然能播放" % save_path

    def test_scenario_002_createTaskWithMutilIngressIdsFail(self, VideomanagerApi, RasmanagerAideApi,config_obj, DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 创建任务，ingressIds中id的个数大于1个,填写多个ingressid 预期会失败"""
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        driver = {
            "enable": True,
            "ingresses": [
                {
                    "information": {
                        "rtsp": {
                            "source_url": camera_info["rtsp"]
                        },
                        "type": camera_info["type"]
                    },
                    "name": "ingress_1_%s" % time_utils.get_str_by_timestamp(formate="%Y%m%d%H%M%S"),
                    "description": ""
                },
                {
                    "information": {
                        "rtsp": {
                            "source_url": camera_info["rtsp"]
                        },
                        "type": camera_info["type"]
                    },
                    "name": "ingress_2_%s" % time_utils.get_str_by_timestamp(formate="%Y%m%d%H%M%S"),
                    "description": ""
                }
            ],
        }
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, driver=driver, camera_info=camera_info, cluster_info=cluster_info)
        # 2.查询ingress_id
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        ingress_id_1 = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")
        ingress_id_2 = resp.json_get("device_detail.device.driver.ingresses.1.ingress_id")
        # 2.创建视频任务
        resp = VideomanagerApi.VideoManagerCenter_CreateTaskPostApi(device_id=device_id, ingress_ids=[ingress_id_1, ingress_id_2])
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.reason") == 11503002

    def test_scenario_003_createTaskWithMutilIngressIdsFail2(self, VideomanagerApi, RasmanagerAideApi, config_obj,
                                                            DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 创建任务，当ingressIds中id的个数大于1个,不填写ingressIs 预期失败"""
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        driver = {
            "enable": True,
            "ingresses": [
                {
                    "information": {
                        "rtsp": {
                            "source_url": camera_info["rtsp"]
                        },
                        "type": camera_info["type"]
                    },
                    "name": "ingress_1_%s" % time_utils.get_str_by_timestamp(formate="%Y%m%d%H%M%S"),
                    "description": ""
                },
                {
                    "information": {
                        "rtsp": {
                            "source_url": camera_info["rtsp"]
                        },
                        "type": camera_info["type"]
                    },
                    "name": "ingress_2_%s" % time_utils.get_str_by_timestamp(formate="%Y%m%d%H%M%S"),
                    "description": ""
                }
            ],
        }
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, driver=driver, camera_info=camera_info,
                                                   cluster_info=cluster_info)
        # 2.查询ingress_id
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        ingress_id_1 = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")
        ingress_id_2 = resp.json_get("device_detail.device.driver.ingresses.1.ingress_id")
        # 2.创建视频任务
        resp = VideomanagerApi.VideoManagerCenter_CreateTaskPostApi(device_id=device_id,
                                                                    ingress_ids=None)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.reason") == 11503002

    def test_scenario_004_deleteDeviceWithHavingTaskFail(self, AideBotInfo, DeviceApi, VideomanagerApi, camera_info, cluster_info, RasmanagerAideApi):
        """ 删除设备时，校验是否存在直播任务，如有则不允许删除"""
        is_delete = True
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info=camera_info, cluster_info=cluster_info,
                                                   is_delete=is_delete)
        # 2.创建视频任务
        resp = VideomanagerApi.createTask(device_id=device_id, is_delete=is_delete)
        task_id = resp.json_get("task.id")

        # 3. 查询任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id])
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.id") == task_id
        # 4.生成播放地址
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id, protocol="RTMP",
                                                                             duration="NO_EXPIRED")
        assert resp.status_code == 200

        # 删除设备，预期失败
        resp = RasmanagerAideApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code == 403
        assert resp.json_get("error.message") == "device has video tasks"

    def test_scenario_005_updateDeviceWithHavingTaskFail(self, AideBotInfo, DeviceApi, VideomanagerApi, camera_info,
                                                         cluster_info, RasmanagerAideApi):
        """ 更新设备时，校验是否存在直播任务，如有则不允许更新"""
        is_delete = True
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info=camera_info, cluster_info=cluster_info,
                                                   is_delete=is_delete)
        # 2.创建视频任务
        resp = VideomanagerApi.createTask(device_id=device_id, is_delete=is_delete)
        task_id = resp.json_get("task.id")

        # 3. 查询任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id])
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.id") == task_id
        # 4.生成播放地址
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id, protocol="RTMP",
                                                                             duration="NO_EXPIRED")
        assert resp.status_code == 200

        # 5.查询设备device0
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        driver_id = resp.json_get("device_detail.device.driver.driver_id")
        ingress_id = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")
        # 更新设备device0
        device_name = "waDevice_%s_Update" % time_utils.get_time_str()
        device_desc = "Update"
        driver = {
            "driver_id": driver_id,
            "enable": True,
            "ingresses": [
                {
                    "information": {
                        "rtsp": {
                            "source_url": 'rtsp://admin:SenseNebula2021@10.151.116.116:554'
                        },
                        "type": camera_info["type"]
                    },
                    "name": device_name,
                    "description": "xxxxxx",
                    "ingress_id": ingress_id
                }
            ],
        }
        extra_info = None
        resp = RasmanagerAideApi.RasManager_UpdateDevicePostApi(device_id=device_id, name=device_name,
                                                            desc=device_desc, driver=driver,
                                                            extra_info=extra_info)
        assert resp.status_code == 403
        assert resp.json_get("error.message") == "device has video tasks"

    def test_scenario_006_taskCrdWithRtspAgainFail(self, VideomanagerApi, RasmanagerAideApi,config_obj, DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 视频直播crd, 相同deviceId ingressid 创建2次任务，预期失败"""
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        driver = {
            "enable": True,
            "ingresses": [
                {
                    "information": {
                        "rtsp": {
                            "source_url": camera_info["rtsp"]
                        },
                        "type": camera_info["type"]
                    },
                    "name": "ingress_1_%s" % time_utils.get_str_by_timestamp(formate="%Y%m%d%H%M%S"),
                    "description": ""
                },
                {
                    "information": {
                        "rtsp": {
                            "source_url": camera_info["rtsp"]
                        },
                        "type": camera_info["type"]
                    },
                    "name": "ingress_2_%s" % time_utils.get_str_by_timestamp(formate="%Y%m%d%H%M%S"),
                    "description": ""
                }
            ],
        }
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, driver=driver, camera_info=camera_info, cluster_info=cluster_info)
        # 2.查询ingress_id
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        ingress_id_1 = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")
        # 2.创建视频任务
        resp = VideomanagerApi.createTask(device_id=device_id, ingress_ids=[ingress_id_1])
        assert resp.status_code == 200
        task_id = resp.json_get("task.id")

        # 2.创建视频任务
        resp = VideomanagerApi.VideoManagerCenter_CreateTaskPostApi(device_id=device_id, ingress_ids=[ingress_id_1])
        assert resp.status_code == 409

    def test_scenario_007_GeneratePlayAddressAgain(self, VideomanagerApi, config_obj, DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 连续生成2次播放地址"""
        is_delete = True
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info=camera_info, cluster_info=cluster_info, is_delete=is_delete)
        # 2.创建视频任务
        resp = VideomanagerApi.createTask(device_id=device_id, is_delete=is_delete)
        task_id = resp.json_get("task.id")

        # 3. 查询任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id])
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.id") == task_id
        # 4.生成播放地址
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id,protocol="RTMP", duration="NO_EXPIRED")
        assert resp.status_code == 200
        assert resp.json_get("url")

        # 5.生成播放地址2
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id, protocol="RTMP", duration="NO_EXPIRED")
        assert resp.status_code == 200
        assert resp.json_get("url")

    def test_scenario_008_getTasks(self, config_obj, VideomanagerApi, AideBotInfo, DeviceApi, camera_info, cluster_info):
        """  查询所有任务"""
        tasks = []
        devices = []
        is_delete = True
        deviceKindName = AideBotInfo.deviceKindName
        for x in range(2):
            name = "waDevice_%s_%s" % (x, time_utils.get_time_str())
            # 1.创建设备
            device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, name=name, camera_info=camera_info, cluster_info=cluster_info, is_delete=is_delete)
            # 2.创建视频任务
            resp = VideomanagerApi.createTask(device_id=device_id, is_delete=is_delete)
            task_id = resp.json_get("task.id")
            tasks.append(task_id)
            devices.append(device_id)

        # 1. 查询全部
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
        assert len(resp.json_get("tasks")) >= 2

        # 2.指定deviceid
        task_ids = None
        device_ids = devices
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                 paging_offset=paging_offset,
                                                                 paging_limit=paging_limit,
                                                                 paging_total=paging_total)
        assert resp.status_code == 200
        assert len(resp.json_get("tasks")) == 2

        # 3.指定task_ids
        task_ids = tasks
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                 paging_offset=paging_offset,
                                                                 paging_limit=paging_limit,
                                                                 paging_total=paging_total)
        assert resp.status_code == 200
        assert len(resp.json_get("tasks")) == 2

    def test_scenario_009_getTasksWithNoTaskDevice(self, config_obj, VideomanagerApi, AideBotInfo, DeviceApi, camera_info, cluster_info):
        """  查询未绑定直播任务的id"""
        is_delete = True
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info=camera_info, cluster_info=cluster_info, is_delete=is_delete)

        task_ids = None
        device_ids = [device_id]
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                 paging_offset=paging_offset,
                                                                 paging_limit=paging_limit,
                                                                 paging_total=paging_total)
        assert resp.status_code == 200
        assert len(resp.json_get("tasks")) == 0

    def test_scenario_010_CreateRecordTask_CRC(self, config_obj, VideomanagerApi, recordTaskCamera_info, cluster_info, AideBotInfo,
                                           RasmanagerAideApi, DeviceApi):
        """  创建,查询,取消录播task"""
        """
        1. 创建录播任务
        2. 查询录播任务
        """
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(AideBotInfo.deviceKindName, camera_info=recordTaskCamera_info, cluster_info=cluster_info, is_delete=False)
        # device_id = recordTaskCamera_info.device_id
        # device_id = "ba0d280a1e824157a5e66aa477cd2c98" # rtmp
        # device_id = "b0dfee6cea1d453f8b058fbd47383ad4" # rtc
        # device_id = "22e20022c1af4c5bab44c2ea05f933c8"
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id)
        ingress_id = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")
        start_time = time_utils.get_str_by_timestamp(offset=10*60+10, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=1 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config":{
                "use_origin": True
            },
            "audio_config":{
                "use_origin": True
            },
            "format":"MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code == 200
        assert resp.json_get("task.device_id") == device_id
        assert resp.json_get("task.status") == "NOT_START"
        assert resp.json_get("task.start_time") == start_time
        assert resp.json_get("task.end_time") == end_time
        assert resp.json_get("task.id")
        assert resp.json_get("task.ingress.ingress_id") == ingress_id
        if keep_days:
            assert resp.json_get("task.keep_days") == keep_days
        else:
            assert resp.json_get("task.keep_days") == 7
        assert len(resp.json_get("task.record_files")) == 0
        task_id = resp.json_get("task.id")

        # 查询任务
        task_ids = [task_id]
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                       paging_offset=paging_offset,
                                                                       paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.device_id") == device_id
        assert resp.json_get("tasks.0.status") == "NOT_START"
        assert resp.json_get("tasks.0.start_time") == start_time
        assert resp.json_get("tasks.0.end_time") == end_time
        assert resp.json_get("tasks.0.id")
        assert resp.json_get("tasks.0.ingress.ingress_id") == ingress_id
        if keep_days:
            assert resp.json_get("tasks.0.keep_days") == keep_days
        else:
            assert resp.json_get("tasks.0.keep_days") == 7
        assert len(resp.json_get("tasks.0.record_files")) == 0

        # # 取消任务
        # resp = VideomanagerApi.VideoManagerCenter_CancelRecordTaskPostApi(task_id=task_id)
        # assert resp.status_code == 200
        #
        # # 查询任务
        # task_ids = [task_id]
        # device_ids = None
        # paging_offset = None
        # paging_limit = None
        # paging_total = None
        # resp = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids,
        #                                                                paging_offset=paging_offset,
        #                                                                paging_limit=paging_limit,
        #                                                                paging_total=paging_total)
        # assert resp.status_code == 200
        # assert resp.json_get("tasks.0.device_id") == device_id
        # assert resp.json_get("tasks.0.status") == "CANCELED"

    def test_scenario_011_CreateRecordTask_NoIngressIdWithMutilIngressFailed(self, config_obj, VideomanagerApi,
                                                                             recordTaskCamera_info, cluster_info, AideBotInfo,
                                                                             RasmanagerAideApi, DeviceApi):
        """  多个ingress情况下，创建录播不填写ingressid，报错"""
        """
        1. 创建录播任务
        2. 查询录播任务
        """
        # 1.创建设备
        driver = {
            "enable": True,
            "ingresses": [
                {
                    "information": {
                        "rtsp": {
                            "source_url": recordTaskCamera_info["rtsp"]
                        },
                        "type": recordTaskCamera_info["type"]
                    },
                    "name": "test11",
                    "description": ""
                },
                {
                    "information": {
                        "rtsp": {
                            "source_url": recordTaskCamera_info["rtsp"]
                        },
                        "type": recordTaskCamera_info["type"]
                    },
                    "name": "test22",
                    "description": ""
                }
            ],
        }
        device_id = DeviceApi.createDeviceWithRTSP(AideBotInfo.deviceKindName, camera_info=recordTaskCamera_info, cluster_info=cluster_info, is_delete=False, driver=driver)
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id)
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
        keep_days = None
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code != 200
        assert resp.json_get("error.message") == "video task argument invalid"

    def test_scenario_012_getTasks(self, config_obj, VideomanagerApi, recordTaskCamera_info, cluster_info, AideBotInfo,
                                           RasmanagerAideApi,DeviceApi):
        """  创建,查询,取消录播task"""
        """
        1. 创建录播任务
        2. 查询录播任务
        """
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(AideBotInfo.deviceKindName, camera_info=recordTaskCamera_info, cluster_info=cluster_info, is_delete=False)
        device_id2 = DeviceApi.createDeviceWithRTSP(AideBotInfo.deviceKindName, camera_info=recordTaskCamera_info, cluster_info=cluster_info, is_delete=False)

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
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=None,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=None)
        assert resp.status_code == 200
        assert resp.json_get("task.device_id") == device_id
        task_id = resp.json_get("task.id")
        time_utils.sleep(1)
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
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id2,
                                                                          ingress_id=None,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=None)
        assert resp.status_code == 200
        assert resp.json_get("task.device_id") == device_id2
        task_id2 = resp.json_get("task.id")

        # 取消任务
        resp = VideomanagerApi.VideoManagerCenter_CancelRecordTaskPostApi(task_id=task_id)
        assert resp.status_code == 200
        resp = VideomanagerApi.VideoManagerCenter_CancelRecordTaskPostApi(task_id=task_id2)
        assert resp.status_code == 200

        # 通过taskid查询任务
        task_ids = [task_id, task_id2]
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                       paging_offset=paging_offset,
                                                                       paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.device_id") in [device_id, device_id2]
        assert resp.json_get("tasks.0.id") in [task_id, task_id2]
        assert resp.json_get("tasks.1.device_id") in [device_id, device_id2]
        assert resp.json_get("tasks.1.id") in [task_id, task_id2]

        # 通过deviceid查询任务
        task_ids = None
        device_ids = [device_id, device_id2]
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                       paging_offset=paging_offset,
                                                                       paging_limit=paging_limit,
                                                                       paging_total=paging_total)
        assert resp.status_code == 200
        assert len(resp.json_get("tasks")) >= 2
        for task in resp.json_get("tasks"):
            assert task["device_id"] in [device_id, device_id2]

        # 查询所有任务
        task_ids = None
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                       paging_offset=paging_offset,
                                                                       paging_limit=paging_limit,
                                                                       paging_total=paging_total)
        assert resp.status_code == 200
        assert len(resp.json_get("tasks")) >= 2
        taskid_02 = resp.json_get("tasks.1.id")
        # 分页查询所有任务
        task_ids = None
        device_ids = None
        paging_offset = 1
        paging_limit = 1
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                       paging_offset=paging_offset,
                                                                       paging_limit=paging_limit,
                                                                       paging_total=paging_total)
        assert resp.status_code == 200
        assert len(resp.json_get("tasks")) == 1
        with check: assert resp.json_get("tasks.0.id") == taskid_02

        # 分页查询所有任务
        task_ids = [task_id, "invalid"]
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                       paging_offset=paging_offset,
                                                                       paging_limit=paging_limit,
                                                                       paging_total=paging_total)
        assert resp.status_code == 200
        assert len(resp.json_get("tasks")) == 1
        assert resp.json_get("tasks.0.id") == task_id

    def test_scenario_013_CreateRecordTask_failed(self, config_obj, VideomanagerApi, recordTaskCamera_info, cluster_info, AideBotInfo,
                                           RasmanagerAideApi, DeviceApi):
        """  同一个ingress上在一个时间段内只能创建一个录播任务"""
        """
        1. 创建录播任务
        2. 查询录播任务
        """
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(AideBotInfo.deviceKindName, camera_info=recordTaskCamera_info, cluster_info=cluster_info, is_delete=False)
        # device_id = recordTaskCamera_info.device_id
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id)
        ingress_id = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")

        #  2. 调用录制任务创建接口（1小时-3小时）
        start_time = time_utils.get_str_by_timestamp(offset=60*60, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=2 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config":{
                "use_origin": True
            },
            "audio_config":{
                "use_origin": True
            },
            "format":"MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code == 200
        assert resp.json_get("task.device_id") == device_id
        assert resp.json_get("task.status") == "NOT_START"
        assert resp.json_get("task.start_time") == start_time
        assert resp.json_get("task.end_time") == end_time
        assert resp.json_get("task.id")
        assert resp.json_get("task.ingress.ingress_id") == ingress_id
        if keep_days:
            assert resp.json_get("task.keep_days") == keep_days
        else:
            assert resp.json_get("task.keep_days") == 7
        assert len(resp.json_get("task.record_files")) == 0
        task_id = resp.json_get("task.id")

        # 3. 调用录制任务创建接口（10分钟- 1.5小时）
        start_time = time_utils.get_str_by_timestamp(offset=10 * 60+ 10, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=1.5 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config": {
                "use_origin": True
            },
            "audio_config": {
                "use_origin": True
            },
            "format": "MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code != 200

        # 4. 调用录制任务创建接口（1.5小时- 4小时）
        start_time = time_utils.get_str_by_timestamp(offset=1.5 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=4 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config": {
                "use_origin": True
            },
            "audio_config": {
                "use_origin": True
            },
            "format": "MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code != 200

        # 5. 调用录制任务创建接口（1.5小时-2.5小时）
        start_time = time_utils.get_str_by_timestamp(offset=1.5 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config": {
                "use_origin": True
            },
            "audio_config": {
                "use_origin": True
            },
            "format": "MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code != 200

        # 6. 调用录制任务创建接口（当前-5小时）
        start_time = time_utils.get_str_by_timestamp(offset= 10 * 60+ 10, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=5*60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config": {
                "use_origin": True
            },
            "audio_config": {
                "use_origin": True
            },
            "format": "MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code != 200

        # 取消任务
        resp = VideomanagerApi.VideoManagerCenter_CancelRecordTaskPostApi(task_id=task_id)
        assert resp.status_code == 200

        # 查询任务
        task_ids = [task_id]
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                       paging_offset=paging_offset,
                                                                       paging_limit=paging_limit,
                                                                       paging_total=paging_total)
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.device_id") == device_id
        assert resp.json_get("tasks.0.status") == "CANCELED"

    def test_scenario_014_CreateRecordTask_cancel_create_success(self, config_obj, VideomanagerApi, recordTaskCamera_info,
                                                  cluster_info, AideBotInfo,
                                                  RasmanagerAideApi, DeviceApi):
        """  同一个ingress上在一个时间段内只能创建一个录播任务， 取消后再创建即可成功"""
        """
        1. 创建录播任务
        2. 查询录播任务
        """
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(AideBotInfo.deviceKindName, camera_info=recordTaskCamera_info,
                                                   cluster_info=cluster_info, is_delete=False)
        # device_id = recordTaskCamera_info.device_id
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id)
        ingress_id = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")

        #  2. 调用录制任务创建接口（1小时-3小时）
        start_time = time_utils.get_str_by_timestamp(offset=60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=2 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config": {
                "use_origin": True
            },
            "audio_config": {
                "use_origin": True
            },
            "format": "MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code == 200
        assert resp.json_get("task.device_id") == device_id
        assert resp.json_get("task.status") == "NOT_START"
        assert resp.json_get("task.start_time") == start_time
        assert resp.json_get("task.end_time") == end_time
        assert resp.json_get("task.id")
        assert resp.json_get("task.ingress.ingress_id") == ingress_id
        if keep_days:
            assert resp.json_get("task.keep_days") == keep_days
        else:
            assert resp.json_get("task.keep_days") == 7
        assert len(resp.json_get("task.record_files")) == 0
        task_id = resp.json_get("task.id")


        # 2. 取消任务
        resp = VideomanagerApi.VideoManagerCenter_CancelRecordTaskPostApi(task_id=task_id)
        assert resp.status_code == 200

        # 3. 调用录制任务创建接口（10分钟- 1.5小时）
        start_time = time_utils.get_str_by_timestamp(offset=10 * 60 + 10, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=1.5 * 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config": {
                "use_origin": True
            },
            "audio_config": {
                "use_origin": True
            },
            "format": "MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code == 200
        task_id = resp.json_get("task.id")

        # 取消任务
        resp = VideomanagerApi.VideoManagerCenter_CancelRecordTaskPostApi(task_id=task_id)
        assert resp.status_code == 200

        # 查询任务
        task_ids = [task_id]
        device_ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = VideomanagerApi.VideoManagerCenter_GetRecordTasksGetApi(task_ids=task_ids, device_ids=device_ids,
                                                                       paging_offset=paging_offset,
                                                                       paging_limit=paging_limit,
                                                                       paging_total=paging_total)
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.device_id") == device_id
        assert resp.json_get("tasks.0.status") == "CANCELED"

    def test_scenario_014_CreateRecordTask_Mutiltask(self, config_obj, VideomanagerApi, recordTaskCamera_info,
                                                  cluster_info, AideBotInfo,
                                                  RasmanagerAideApi, DeviceApi):
        """  同一个ingress，创建多个时段任务"""
        """
        1. 创建录播任务
        2. 查询录播任务
        """
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(AideBotInfo.deviceKindName, camera_info=recordTaskCamera_info,
                                                   cluster_info=cluster_info, is_delete=False)
        # device_id = recordTaskCamera_info.device_id
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id)
        ingress_id = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")

        #  2. 调用录制任务创建接口（1小时-3小时）
        start_time = time_utils.get_str_by_timestamp(offset=60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset= 60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config": {
                "use_origin": True
            },
            "audio_config": {
                "use_origin": True
            },
            "format": "MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code == 200
        assert resp.json_get("task.device_id") == device_id
        assert resp.json_get("task.status") == "NOT_START"
        assert resp.json_get("task.start_time") == start_time
        assert resp.json_get("task.end_time") == end_time
        assert resp.json_get("task.id")
        assert resp.json_get("task.ingress.ingress_id") == ingress_id
        if keep_days:
            assert resp.json_get("task.keep_days") == keep_days
        else:
            assert resp.json_get("task.keep_days") == 7
        assert len(resp.json_get("task.record_files")) == 0
        task_id1 = resp.json_get("task.id")

        # 3. 调用录制任务创建接口（2小时- 3小时）
        start_time = time_utils.get_str_by_timestamp(offset=2*60 * 60 + 60, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config": {
                "use_origin": True
            },
            "audio_config": {
                "use_origin": True
            },
            "format": "MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code == 200
        task_id2 = resp.json_get("task.id")


        # 3. 调用录制任务创建接口（3小时- 4小时）
        start_time = time_utils.get_str_by_timestamp(offset=3*60 * 60 + 60, formate="%Y-%m-%dT%H:%M:%SZ")
        end_time = time_utils.get_str_by_timestamp(ts=start_time, offset=60 * 60, formate="%Y-%m-%dT%H:%M:%SZ")
        template = {
            "video_config": {
                "use_origin": True
            },
            "audio_config": {
                "use_origin": True
            },
            "format": "MP4"
        }
        keep_days = 30
        resp = VideomanagerApi.VideoManagerCenter_CreateRecordTaskPostApi(device_id=device_id,
                                                                          ingress_id=ingress_id,
                                                                          start_time=start_time, end_time=end_time,
                                                                          template=template, keep_days=keep_days)
        assert resp.status_code == 200
        task_id3 = resp.json_get("task.id")

        log().info("task1:%s" % task_id1)
        log().info("task2:%s" % task_id2)
        log().info("task3:%s" % task_id3)