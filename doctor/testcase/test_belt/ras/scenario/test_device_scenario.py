#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
from defines.belt.device_service_business import RASINGRESS_STATUS_AVAILABLE


@pytest.mark.skip("内部接口，device创建相关放到rasManager中验证")
class TestDeviceScenario(object):
    """ Device scenario test"""

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

    @pytest.mark.skip("手工测试用例")
    def test_scenario_000_registration(self, DeviceApi):
        """ 边缘云设备服务注册信息查询"""
        # 1.edge的device服务通过注册的形式被中心发现
        # 2.调用注册信息查询接口（内部接口），查看返回值，观察如下信息是否正确
        resp = DeviceApi.DeviceManagerCenter_ListRegistrationGetApi()
        assert resp.status_code == 200
        # TODO 查看注册信息是否完全

    @pytest.mark.skip("手工测试用例")
    def test_scenario_001_EdgeDeviceServiceHealthCheck(self, DeviceApi):
        """ 健康检查"""
        # 1. 边缘云device服务注册成功
        # 2. 调用注册信息查询接口（内部接口），查看返回值，观察健康检查信息
        resp = DeviceApi.DeviceManagerCenter_ListRegistrationGetApi()
        assert resp.status_code == 200
        # TODO 预期状态为在线
        # kill掉边缘云device服务
        # 调用注册信息查询接口（内部接口），查看返回值，观察健康检查信息
        resp = DeviceApi.DeviceManagerCenter_ListRegistrationGetApi()
        assert resp.status_code == 200
        # TODO 预期状态为离线

    @pytest.mark.skip("手工测试用例")
    def test_scenario_002_dataRecovery(self, DeviceApi, deviceKindAide, cluster_info, camera_info):
        """ 数据恢复"""
        # 1.边缘云服务注册成功
        # 2.调用接口创建一个rtsp流的设备
        name = "test_device"
        device_kind_id = deviceKindAide.id
        cluster = {"id": cluster_info.id}
        driver = {
            "enable": True,
            "ingresses": [
                {
                    "information": {
                        "rtsp": {
                            "source_url": camera_info.rtsp
                        },
                        "type": camera_info.type
                    },
                    "name": "new_driver",
                    "description": "new_driver"
                }
            ],
        }
        resp = DeviceApi.DeviceManagerCenter_CreateDevicePostApi(device_kind_id=device_kind_id, name=name,
                                                                 cluster=cluster, driver=driver)
        assert resp.status_code == 200
        device_id = resp.json_get("device.id")

        # 3.调用接口查询该设备信息，rtsp流地址，读取rtsp流数据
        resp = DeviceApi.getDeviceByIDUntilAvailable(device_id)
        assert resp.status_code == 200
        device_rtsp_url = resp.json_get("device.driver.ingresses.0.information.rtsp.url")  # 只有上报后才有
        log().info("deviceId:%s,url:%s" % (device_id, device_rtsp_url))
        # 4.kill掉边缘云设备服务，等待5分钟
        # 5.启动边缘云设备服务
        # 6.调用接口查询该设备，rtsp流地址
        resp = DeviceApi.DeviceManagerCenter_GetDeviceGetApi(device_id)
        assert resp.status_code == 200
        device_rtsp_url = resp.json_get("device.driver.ingresses.0.information.rtsp.url")  # 只有上报后才有
        log().info("deviceId:%s,url:%s" % (device_id, device_rtsp_url))
        assert resp.json_get("device.driver.ingresses.0.status") == RASINGRESS_STATUS_AVAILABLE
        # 播放rtsp流,检查是否正常

    def test_scenario_003_deviceKindCRUDForRTSP(self, DeviceApi, deviceKindAide, cluster_info, camera_info):
        """ rtsp 设备类型crud"""
        # RTSP设备类型的CRUD
        # 1.创建设备类型
        name = "test_deviceKind_%s" % time_utils.get_time_str()
        desc = "desc"
        ingress_types = ["RTSP"]
        verify_method = "USER"
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceKindPostApi(name=name, desc=desc, ingress_types=ingress_types,
                                                                     verify_method=verify_method)
        assert resp.status_code == 200
        devicekind_id = resp.json_get("devicekind.id")
        log().info("devicekind_id=%s" % devicekind_id)
        assert resp.json_get("devicekind.desc") == desc
        assert resp.json_get("devicekind.ingress_types") == ingress_types
        assert resp.json_get("devicekind.name") == name
        assert resp.json_get("devicekind.verify_method") == verify_method
        assert resp.json_get("devicekind.created_at")
        assert resp.json_get("devicekind.updated_at")
        # 2.查询设备类型
        resp = DeviceApi.DeviceManagerCenter_GetDeviceKindGetApi(devicekind_id)
        assert resp.status_code == 200
        assert resp.json_get("devicekind.desc") == desc
        assert resp.json_get("devicekind.ingress_types") == ingress_types
        assert resp.json_get("devicekind.name") == name
        assert resp.json_get("devicekind.verify_method") == verify_method
        assert resp.json_get("devicekind.created_at")
        assert resp.json_get("devicekind.updated_at")
        # 3.更新设备类型:名称,描述
        update_name = "new_deviceKind"
        update_desc = "new_desc"
        resp = DeviceApi.DeviceManagerCenter_UpdateDeviceKindPostApi(devicekind_id, name=update_name, desc=update_desc)
        assert resp.status_code == 200
        assert resp.json_get("devicekind.desc") == update_desc
        assert resp.json_get("devicekind.name") == update_name

        # 4.查询设备类型
        resp = DeviceApi.DeviceManagerCenter_GetDeviceKindGetApi(devicekind_id)
        assert resp.status_code == 200
        assert resp.json_get("devicekind.desc") == update_desc
        assert resp.json_get("devicekind.name") == update_name

        # 删除设备类型
        resp = DeviceApi.DeviceManagerCenter_DeleteDeviceKindPostApi(devicekind_id)
        assert resp.status_code == 200
        # 查询设备类型
        resp = DeviceApi.DeviceManagerCenter_GetDeviceKindGetApi(devicekind_id)
        assert resp.status_code == 404

    def test_scenario_003_deviceKindDeleteFailed(self, DeviceApi, deviceKindAide, cluster_info, camera_info):
        """ 关联设备的设备类型不允许删除，删除关联设备后，允许删除"""
        # 1.创建设备类型 写在business封装
        deviceKind_id = DeviceApi.createDeviceKindWithRTSP()
        # 2.创建设备，指定该设备类型
        device_id = DeviceApi.createDeviceWithRTSP(deviceKind_id, camera_info, cluster_info)
        # 3.删除设备类型
        resp = DeviceApi.DeviceManagerCenter_DeleteDeviceKindPostApi(deviceKind_id)
        assert resp.status_code != 200
        # 4.删除设备
        DeviceApi.deleteDeviceById(device_id)
        # 5.删除设备类型
        resp = DeviceApi.DeviceManagerCenter_DeleteDeviceKindPostApi(deviceKind_id)
        assert resp.status_code == 200
        # 6.查询设备类型,预期返回404
        resp = DeviceApi.DeviceManagerCenter_GetDeviceKindGetApi(deviceKind_id)
        assert resp.status_code == 404

    def test_scenario_004_deviceKindUpdateFailed(self, DeviceApi, deviceKindAide, cluster_info, camera_info):
        """ 关联设备的设备类型不允许更新，删除关联设备后，允许更新"""
        # 1.创建设备类型
        deviceKind_id = DeviceApi.createDeviceKindWithRTSP()
        # 2.创建设备，指定该设备类型
        device_id = DeviceApi.createDeviceWithRTSP(deviceKind_id, camera_info, cluster_info)
        # 3.更改设备类型
        name = "new_name"
        desc = "new_desc"
        resp = DeviceApi.DeviceManagerCenter_UpdateDeviceKindPostApi(deviceKind_id, name=name, desc=desc)
        assert resp.status_code != 200
        # 4.删除设备
        DeviceApi.deleteDeviceById(device_id)
        # 5.删除设备类型
        resp = DeviceApi.DeviceManagerCenter_DeleteDeviceKindPostApi(deviceKind_id)
        assert resp.status_code == 200
        # 6.查询设备类型,预期返回404
        resp = DeviceApi.DeviceManagerCenter_GetDeviceKindGetApi(deviceKind_id)
        assert resp.status_code == 404

    def test_scenario_005_deviceKindForMutilDevice(self, DeviceApi, deviceKindAide, cluster_info, camera_info):
        """ 一个设备类型关联多个设备	"""
        # 1.创建设备类型
        deviceKind_id = DeviceApi.createDeviceKindWithRTSP()
        # 2.创建设备1，指定该设备类型
        device_id = DeviceApi.createDeviceWithRTSP(deviceKind_id, camera_info, cluster_info)
        # 3.创建设备2，指定该设备类型
        device_id2 = DeviceApi.createDeviceWithRTSP(deviceKind_id, camera_info, cluster_info)
        # 查询设备信息,返回的设备类型id
        resp = DeviceApi.DeviceManagerCenter_GetDeviceGetApi(device_id)
        assert resp.json_get("device.devicekind_id") == deviceKind_id
        resp = DeviceApi.DeviceManagerCenter_GetDeviceGetApi(device_id2)
        assert resp.json_get("device.devicekind_id") == deviceKind_id

    def test_scenario_006_deviceKindList(self, DeviceApi, deviceKindAide, cluster_info, camera_info):
        """ 设备类型列表查询接口分页"""
        # 验证list, ids = None, 查询全部
        resp = DeviceApi.DeviceManagerCenter_GetDeviceKindsGetApi()
        assert resp.status_code == 200
        # assert resp.json_get("paging")
        i = 1
        # 分页的默认值 limit 10 offset 0
        # TODO

    def test_scenario_007_batchCreateDeviceLt50Failed(self, DeviceApi, deviceKindAide, cluster_info, camera_info):
        """ 批量创建任务，单次最多创建50个"""
        request_header = None
        devices = []
        devicekind_id = deviceKindAide.id
        for x in range(51):
            devices.append({
              "cluster": {
                "id": cluster_info["id"]
              },
              "desc": "test",
              "devicekind_id": devicekind_id,
              "driver": {
                "enable": True,
                "ingresses": [
                  {
                    "information": {
                      "rtsp": {
                         "source_url": camera_info["rtsp"]
                      },
                      "type":  camera_info["type"]
                    },
                    "name": "driver_name_%s" % x
                  }
                ]
              },
              "name": "device_%s_%s" % (x, sign_utils.getUuid(5))
            })
        resp = DeviceApi.DeviceManagerCenter_BatchCreateDevicePostApi(request_header=request_header, devices=devices)
        assert resp.status_code != 200

    def test_scenario_008_batchCreateDeviceEq50Success(self, DeviceApi, deviceKindAide, cluster_info, camera_info):
        """ 批量创建任务，单次最多创建50个"""
        request_header = None
        devices = []
        devicekind_id = deviceKindAide.id
        for x in range(50):
            devices.append({
                "cluster": {
                    "id": cluster_info["id"]
                },
                "desc": "test",
                "devicekind_id": devicekind_id,
                "driver": {
                    "enable": True,
                    "ingresses": [
                        {
                            "information": {
                                "rtsp": {
                                    "source_url": camera_info["rtsp"]
                                },
                                "type": camera_info["type"]
                            },
                            "name": "driver_name_%s" % x
                        }
                    ]
                },
                "name": "device_%s_%s" % (x, sign_utils.getUuid(5))
            })
        resp = DeviceApi.DeviceManagerCenter_BatchCreateDevicePostApi(request_header=request_header, devices=devices)
        assert resp.status_code == 200
        devices = resp.json_get("devices")
        success = []
        failed = []
        for d in devices:
            if d["error"]:
                failed.append(d)
            else:
                success.append(d)
        log().info("success:%s, failed:%s" % (len(success), len(failed)))
        i = 1
        for d in success:
            DeviceApi.getDeviceByIDUntilAvailable(d["device"]["id"])

        for d in success:
            DeviceApi.DeviceManagerCenter_DeleteDevicePostApi(id=d["device"]["id"])





