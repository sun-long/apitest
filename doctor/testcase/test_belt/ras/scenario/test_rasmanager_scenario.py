#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
from commonlib.sign_utils import encode_jwt_token
from pytest_check import check


class TestRasmanagerScenario(object):
    """ Rasmanager scenario test"""

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

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_000_AideCountDevices(self, config_obj, RasmanagerApi, EasyBotInfo, AideBotInfo):
        """  海目：返回account下的设备数量"""
        """
            覆盖接口：
                /v1/CountDevices
        """
        # 1.查询CountDevice列表
        spu_names = [AideBotInfo.spu_name]
        resp = RasmanagerApi.RasManager_CountDevicesGetApi(spu_names=spu_names)
        assert resp.status_code == 200
        total, subscribe_total = resp.json_get("total"), resp.json_get("subscribe_total")
        # 2.查询设备列表
        allDevice_list = RasmanagerApi.getAllDeviceDetail(spu_names=None, print_log=True)
        assert len(allDevice_list) == total, "CountDevice:设备总数error"
        # 3.查询绑定设备列表
        bindAideDevice_list = RasmanagerApi.getAllDeviceDetail(spu_names=[AideBotInfo.spu_name], print_log=True)
        assert len(bindAideDevice_list) == subscribe_total, "CountDevice:绑定aide设备数量error"

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_001_AideDeviceCRUD(self, RasmanagerAideApi, DeviceApi, camera_info, cluster_info, AideBotInfo):
        """ aide assignment的crud流程"""
        """
            覆盖接口：
                device：
                    /v1/createDevice
                Ras：
                    /v1/UpdateDevice
                    /v1/ListDeviceDetails
                    /v1/GetDeviceDetail
                    /v1/DeleteDevice
        """
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备device = device1
        name = "waDevice_%s" % time_utils.get_time_str()
        cluster = {"id": cluster_info["id"]}
        desc = "test"
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
                    "name": name,
                    "description": desc
                }
            ],
        }
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=deviceKindName, name=name,
                                                                           cluster=cluster, driver=driver, desc=desc)
        assert resp.status_code == 200
        assert resp.json_get("device.cluster.id")  # TODO 集成测试补充验证
        assert resp.json_get("device.cluster.name")  # TODO 集成测试补充验证
        assert resp.json_get("device.cluster.type")  # TODO 集成测试补充验证
        assert resp.json_get("device.created_at")
        assert resp.json_get("device.updated_at")
        assert resp.json_get("device.name") == name
        assert resp.json_get("device.desc") == desc
        assert resp.json_get("device.id")
        assert resp.json_get("device.verify.method") == "USER"
        assert resp.json_get("device.verify.user_info.ak")
        assert resp.json_get("device.verify.user_info.sk")
        assert resp.json_get("device.verify.user_info.user_id")
        assert resp.json_get("device.devicekind.name") == deviceKindName
        assert resp.json_get("device.driver.driver_id")
        assert resp.json_get("device.driver.ingresses.0.description") == desc
        assert resp.json_get("device.driver.ingresses.0.ingress_id")
        assert resp.json_get("device.driver.ingresses.0.name") == name
        assert resp.json_get("device.driver.ingresses.0.information.rtsp.protocol_type") in ["TCP", "UDP"]
        assert resp.json_get("device.driver.ingresses.0.information.rtsp.source_url") == camera_info["rtsp"]
        assert resp.json_get("device.driver.ingresses.0.information.rtsp.url") == ""
        # assert resp.json_get("device.driver.ingresses.0.information.rtsp.verification")
        assert resp.json_get("device.driver.ingresses.0.information.type") == camera_info["type"]
        assert resp.json_get("device.driver.ingresses.0.status") in ["INGRESS_STATUS_UNKNOWN", "AVAILABLE",
                                                                     "UNAVAILABLE"]
        device_id = resp.json_get("device.id")
        user_info = resp.json_get("device.verify.user_info")
        driver_id = resp.json_get("device.driver.driver_id")
        ingress_id = resp.json_get("device.driver.ingresses.0.ingress_id")

        RasmanagerApi.getDeviceByIDUntilAvailable(device_id)
        # 2.查询设备 getDeviceDetail接口
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id)
        assert resp.status_code == 200
        assert resp.json_get("device_detail.device.cluster.id")  # TODO 集成测试补充验证
        assert resp.json_get("device_detail.device.cluster.name")  # TODO 集成测试补充验证
        assert resp.json_get("device_detail.device.cluster.type")  # TODO 集成测试补充验证
        assert resp.json_get("device_detail.device.created_at")
        assert resp.json_get("device_detail.device.updated_at")
        assert resp.json_get("device_detail.device.name") == name
        assert resp.json_get("device_detail.device.desc") == desc
        assert resp.json_get("device_detail.device.id")
        assert resp.json_get("device_detail.device.verify.method") == "USER"
        assert resp.json_get("device_detail.device.verify.user_info.ak") == "", "不显示鉴权信息"
        assert resp.json_get("device_detail.device.verify.user_info.sk") == "", "不显示鉴权信息"
        assert resp.json_get("device_detail.device.verify.user_info.user_id") == "0", "不显示鉴权信息"
        assert resp.json_get("device_detail.device_kind.name") == deviceKindName
        assert resp.json_get("device_detail.device.driver.driver_id")
        assert resp.json_get("device_detail.device.driver.ingresses.0.description") == desc
        assert resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")
        assert resp.json_get("device_detail.device.driver.ingresses.0.name") == name
        assert resp.json_get("device_detail.device.driver.ingresses.0.information.rtsp.protocol_type") in ["TCP", "UDP"]
        assert resp.json_get(
            "device_detail.device.driver.ingresses.0.information.rtsp.source_url") == "", "不显示source_url"
        assert resp.json_get("device_detail.device.driver.ingresses.0.information.rtsp.url") == "", "不显示source_url"
        # assert resp.json_get("device_detail.device.driver.ingresses.0.information.rtsp.verification")
        assert resp.json_get("device_detail.device.driver.ingresses.0.information.type") == camera_info["type"]
        assert resp.json_get("device_detail.device.driver.ingresses.0.status") in ["INGRESS_STATUS_UNKNOWN",
                                                                                   "AVAILABLE",
                                                                                   "UNAVAILABLE"]
        # 3.查询设备 ListDeviceDetail接口
        device_list = RasmanagerApi.getAllDeviceDetail()
        device_info = None
        for device in device_list:
            if device["device"]["id"] == device_id:
                device_info = device
                break
        assert device_info, "ListDeviceDetail中未查询到该设备%s" % device_id
        assert device_info["device"]["cluster"]["id"]  # TODO 集成测试补充验证
        assert device_info["device"]["cluster"]["name"]  # TODO 集成测试补充验证
        assert device_info["device"]["cluster"]["type"]  # TODO 集成测试补充验证
        assert device_info["device"]["created_at"]
        assert device_info["device"]["updated_at"]
        assert device_info["device"]["name"] == name
        assert device_info["device"]["desc"] == desc
        assert device_info["device"]["id"]
        assert device_info["device"]["verify"]["method"] == "USER"
        assert device_info["device"]["verify"]["user_info"]["ak"] == "", "不显示鉴权信息"
        assert device_info["device"]["verify"]["user_info"]["sk"] == "", "不显示鉴权信息"
        assert device_info["device"]["verify"]["user_info"]["user_id"] == "0", "不显示鉴权信息"
        assert device_info["device_kind"]["name"] == deviceKindName
        assert device_info["device"]["driver"]["driver_id"]
        assert device_info["device"]["driver"]["ingresses"][0]["description"] == desc
        assert device_info["device"]["driver"]["ingresses"][0]["ingress_id"]
        assert device_info["device"]["driver"]["ingresses"][0]["name"] == name
        assert device_info["device"]["driver"]["ingresses"][0]["information"]["rtsp"]["protocol_type"] in ["TCP", "UDP"]
        assert device_info["device"]["driver"]["ingresses"][0]["information"]["rtsp"][
                   "source_url"] == "", "不显示source_url"
        assert device_info["device"]["driver"]["ingresses"][0]["information"]["rtsp"]["url"] == "", "不显示source_url"
        # assert device_info["device"]["driver"]["ingresses"][0]["information"]["rtsp"]["verification"]
        assert device_info["device"]["driver"]["ingresses"][0]["information"]["type"] == camera_info["type"]
        assert device_info["device"]["driver"]["ingresses"][0]["status"] in ["INGRESS_STATUS_UNKNOWN",
                                                                             "AVAILABLE",
                                                                             "UNAVAILABLE"]
        # 4.更新设备
        nameUpdate = "update_%s" % name
        descUpdate = "update_%s" % desc
        rtspUpdate = 'rtsp://10.53.4.176:8554/invaild.264'
        driverUpdate = {
            "driver_id": driver_id,
            "enable": True,
            "ingresses": [
                {
                    "ingress_id": ingress_id,
                    "information": {
                        "rtsp": {
                            "source_url": rtspUpdate
                        },
                        "type": camera_info["type"]
                    },
                    "name": nameUpdate,
                    "description": descUpdate
                }
            ],
        }
        resp = RasmanagerApi.RasManager_UpdateDevicePostApi(device_id=device_id, name=nameUpdate,
                                                            driver=driverUpdate, desc=descUpdate)
        assert resp.status_code == 200
        assert resp.json_get("device_detail.device.cluster.id")  # TODO 集成测试补充验证
        assert resp.json_get("device_detail.device.cluster.name")  # TODO 集成测试补充验证
        assert resp.json_get("device_detail.device.cluster.type")  # TODO 集成测试补充验证
        assert resp.json_get("device_detail.device.created_at")
        assert resp.json_get("device_detail.device.updated_at")
        assert resp.json_get("device_detail.device.name") == nameUpdate
        assert resp.json_get("device_detail.device.desc") == descUpdate
        assert resp.json_get("device_detail.device.id")
        assert resp.json_get("device_detail.device.verify.method") == "USER"
        assert resp.json_get("device_detail.device.verify.user_info.ak") == "", "不显示鉴权信息"
        assert resp.json_get("device_detail.device.verify.user_info.sk") == "", "不显示鉴权信息"
        assert resp.json_get("device_detail.device.verify.user_info.user_id") == "0", "不显示鉴权信息"
        assert resp.json_get("device_detail.device_kind.name") == deviceKindName
        assert resp.json_get("device_detail.device.driver.driver_id")
        assert resp.json_get("device_detail.device.driver.ingresses.0.description") == descUpdate
        assert resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")
        assert resp.json_get("device_detail.device.driver.ingresses.0.name") == nameUpdate
        assert resp.json_get("device_detail.device.driver.ingresses.0.information.rtsp.protocol_type") in ["TCP", "UDP"]
        assert resp.json_get(
            "device_detail.device.driver.ingresses.0.information.rtsp.source_url") == "", "不显示source_url"
        assert resp.json_get("device_detail.device.driver.ingresses.0.information.rtsp.url") == "", "不显示source_url"
        # assert resp.json_get("device.driver.ingresses.0.information.rtsp.verification")
        assert resp.json_get("device_detail.device.driver.ingresses.0.information.type") == camera_info["type"]
        assert resp.json_get("device_detail.device.driver.ingresses.0.status") in ["INGRESS_STATUS_UNKNOWN",
                                                                                   "AVAILABLE",
                                                                                   "UNAVAILABLE"]
        # 5.更新后查询设备 getDeviceDetail接口
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id)
        assert resp.status_code == 200
        assert resp.json_get("device_detail.device.cluster.id")  # TODO 集成测试补充验证
        assert resp.json_get("device_detail.device.cluster.name")  # TODO 集成测试补充验证
        assert resp.json_get("device_detail.device.cluster.type")  # TODO 集成测试补充验证
        assert resp.json_get("device_detail.device.created_at")
        assert resp.json_get("device_detail.device.updated_at")
        assert resp.json_get("device_detail.device.name") == nameUpdate
        assert resp.json_get("device_detail.device.desc") == descUpdate
        assert resp.json_get("device_detail.device.id")
        assert resp.json_get("device_detail.device.verify.method") == "USER"
        assert resp.json_get("device_detail.device.verify.user_info.ak") == "", "不显示鉴权信息"
        assert resp.json_get("device_detail.device.verify.user_info.sk") == "", "不显示鉴权信息"
        assert resp.json_get("device_detail.device.verify.user_info.user_id") == "0", "不显示鉴权信息"
        assert resp.json_get("device_detail.device_kind.name") == deviceKindName
        assert resp.json_get("device_detail.device.driver.driver_id")
        assert resp.json_get("device_detail.device.driver.ingresses.0.description") == descUpdate
        assert resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")
        assert resp.json_get("device_detail.device.driver.ingresses.0.name") == nameUpdate
        assert resp.json_get("device_detail.device.driver.ingresses.0.information.rtsp.protocol_type") in ["TCP", "UDP"]
        assert resp.json_get(
            "device_detail.device.driver.ingresses.0.information.rtsp.source_url") == "", "不显示source_url"
        assert resp.json_get("device_detail.device.driver.ingresses.0.information.rtsp.url") == "", "不显示source_url"
        # assert resp.json_get("device_detail.device.driver.ingresses.0.information.rtsp.verification")
        assert resp.json_get("device_detail.device.driver.ingresses.0.information.type") == camera_info["type"]
        assert resp.json_get("device_detail.device.driver.ingresses.0.status") in ["INGRESS_STATUS_UNKNOWN",
                                                                                   "AVAILABLE",
                                                                                   "UNAVAILABLE"]
        # 6.删除设备
        resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code == 200
        RasmanagerApi.getDeviceByIDUntilNotFound(device_id)

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_002_AideBatchCreateDeviceEq50Success(self, RasmanagerAideApi, DeviceApi, camera_info,
                                                           cluster_info, AideBotInfo):
        """ 批量创建设备"""
        """
            覆盖接口：
                device:
                    /v1/batchCreateDevice
        """
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        request_header = None
        devices = []
        for x in range(50):
            devices.append({
                "cluster": {
                    "id": cluster_info["id"]
                },
                "desc": "test",
                "devicekind_name": deviceKindName,
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
        resp = DeviceApi.DeviceManagerCenter_BatchCreateDeviceByKindNamePostApi(request_header=request_header,
                                                                                devices=devices)
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
        for d in success:
            RasmanagerApi.getDeviceByIDUntilAvailable(d["device"]["id"])

        for d in success:
            resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=d["device"]["id"])
            assert resp.status_code == 200
            RasmanagerApi.getDeviceByIDUntilNotFound(d["device"]["id"])

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_003_AideBatchCreateDevicegt50Failed(self, RasmanagerAideApi, DeviceApi, camera_info, cluster_info,
                                                          AideBotInfo):
        """ 批量创建设备"""
        deviceKindName = AideBotInfo.deviceKindName
        request_header = None
        devices = []
        for x in range(51):
            devices.append({
                "cluster": {
                    "id": cluster_info["id"]
                },
                "desc": "test",
                "devicekind_name": deviceKindName,
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
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_004_AideDeviceCreateNameIsNullFailed(self, RasmanagerAideApi, DeviceApi, camera_info,
                                                           cluster_info, AideBotInfo):
        """ aide assignment的crud流程"""
        """
            覆盖接口：
                device：
                    /v1/createDevice
        """
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备device = device1
        name = ""
        cluster = {"id": cluster_info["id"]}
        desc = "test"
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
                    "name": name,
                    "description": desc
                }
            ],
        }
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=deviceKindName, name=name,
                                                                           cluster=cluster, driver=driver, desc=desc)
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_005_AideDeviceCreateNameDuplicateFailed(self, RasmanagerAideApi, DeviceApi, AideBotInfo,
                                                              camera_info,
                                                              cluster_info):
        """ 创建设备名称重复会失败"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备device = device1
        name = "waDevice_%s" % time_utils.get_time_str()
        cluster = {"id": cluster_info["id"]}
        desc = "test"
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
                    "name": name,
                    "description": desc
                }
            ],
        }
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=deviceKindName, name=name,
                                                                           cluster=cluster, driver=driver, desc=desc)
        assert resp.status_code == 200
        device_id = resp.json_get("device.id")
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=deviceKindName, name=name,
                                                                           cluster=cluster, driver=driver, desc=desc)
        assert resp.status_code != 200
        resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code == 200
        RasmanagerApi.getDeviceByIDUntilNotFound(device_id)


    def test_scenario_006_AideDeviceCreateNameDuplicateSuccessWithMutilAccount(self, RasmanagerAideApi, DeviceApi,
                                                                               AideBotInfo, camera_info,
                                                                               cluster_info, config_obj, user_info):
        """ 在多个acount下，创建同名设备可以成功"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备device = device1
        name = "waDevice_%s" % time_utils.get_time_str()
        cluster = {"id": cluster_info["id"]}
        desc = "test"
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
                    "name": name,
                    "description": desc
                }
            ],
        }
        testUser = user_info
        loginToken1 = encode_jwt_token(testUser.ak, testUser.sk)
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=deviceKindName, name=name,
                                                                           cluster=cluster, driver=driver, desc=desc,
                                                                           loginToken=loginToken1)
        assert resp.status_code == 200
        device_id1 = resp.json_get("device.id")

        testUser1 = config_obj.Console.User.testUser1
        loginToken2 = encode_jwt_token(testUser1.ak, testUser1.sk)
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=deviceKindName, name=name,
                                                                           cluster=cluster, driver=driver, desc=desc,
                                                                           loginToken=loginToken2)
        assert resp.status_code == 200
        device_id2 = resp.json_get("device.id")

        resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id1, loginToken=loginToken1)
        assert resp.status_code == 200
        RasmanagerApi.getDeviceByIDUntilNotFound(device_id1, loginToken=loginToken1)

        resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id2, loginToken=loginToken2)
        assert resp.status_code == 200
        RasmanagerApi.getDeviceByIDUntilNotFound(device_id2, loginToken=loginToken2)

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_007_AideUpdateDeviceNameIsNullFailed(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                                           cluster_info):
        """ 更新设备-name为null不允许更新"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 创建设备device0
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 查询设备device0
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        driver_id = resp.json_get("device_detail.device.driver.driver_id")
        ingress_id = resp.json_get("device_detail.device.driver.ingresses.0.ingress_id")
        # 更新设备device0
        device_name = ""
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
        resp = RasmanagerApi.RasManager_UpdateDevicePostApi(device_id=device_id, name=device_name,
                                                            desc=device_desc, driver=driver,
                                                            extra_info=extra_info)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "invalid UpdateDeviceReq.Name: value length must be between 1 and 64 runes, inclusive"
        assert resp.json_get("error.details.0.reason") == 11403002

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_008_AideAssignmentCRD(self, RasmanagerAideApi, DeviceApi, AideBotInfo, cluster_info,
                                            AideCallbackAddress1, config_obj, user_info):
        """ assignment的crd流程"""
        """
            覆盖接口：
                device：
                    /v1/createDevice
                Ras：
                    /v1/ListDeviceDetails
                    /v1/GetDeviceDetail
                    /v1/DeleteDevice
                    /v1/CreateAssignment
                    /v1/DeleteAssignment
                    /v1/GetAssignment
        """
        # camera_info = config_obj.Clients.SubDevice.aide1  # live555模拟流
        camera_info = config_obj.Clients.SubDevice.camera1  # 真实摄像头
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        spu_name = AideBotInfo.spu_name
        spu_display_name = AideBotInfo.spu_display_name
        # 1.创建设备device = device1
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        assignment_config = {
            "data": {
                "rules": [{
                    "roi": {
                        "vertices": [{
                            "x": 0,
                            "y": 0
                        },
                            {
                                "x": 1,
                                "y": 1
                            }
                        ]
                    },
                    "rule_id": "a",
                }]
            },
            "user_callback_url": AideCallbackAddress1
        }
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code == 200
        assignment_id = resp.json_get("assignment.assignment_id")
        assert resp.json_get("assignment.assignment_id")
        assert resp.json_get("assignment.spu_name") == spu_name
        assert resp.json_get("assignment.account_id") == user_info.account_id
        assert resp.json_get("assignment.device_id") == device_id
        assert resp.json_get("assignment.assignment_config") == assignment_config
        assert resp.json_get("assignment.rotate_config") == rotate_config
        assert resp.json_get("assignment.state")
        # 3.查询assignment
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        assert resp.status_code == 200
        assert resp.json_get("assignment.assignment_id")
        assert resp.json_get("assignment.spu_name") == spu_name
        assert resp.json_get("assignment.account_id") == user_info.account_id
        assert resp.json_get("assignment.device_id") == device_id
        assert resp.json_get("assignment.assignment_config") == assignment_config
        assert resp.json_get("assignment.rotate_config") == rotate_config
        assert resp.json_get("assignment.state")

        # 2.查询设备 getDeviceDetail接口
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id)
        assert resp.status_code == 200
        assert resp.json_get("device_detail.spus.0.display_name") == spu_display_name
        assert resp.json_get("device_detail.spus.0.name") == spu_name
        # 3.查询设备 ListDeviceDetail接口
        device_list = RasmanagerApi.getAllDeviceDetail()
        device_info = None
        for device in device_list:
            if device["device"]["id"] == device_id:
                device_info = device
                break
        assert device_info, "ListDeviceDetail中未查询到该设备%s" % device_id
        assert device_info["spus"][0]["display_name"] == spu_display_name
        assert device_info["spus"][0]["name"] == spu_name

        # 4.删除assignment
        resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
        assert resp.status_code == 200
        # 5.查询assignment
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        assert resp.status_code == 404
        # 6.删除设备

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_009_AideAssignmentUpdateAssignmentConfig(self, RasmanagerAideApi, DeviceApi, AideBotInfo,
                                                               cluster_info,
                                                               AideCallbackAddress1, config_obj, user_info):
        """ 更新assignment的AssignmentConfig"""
        """
            覆盖接口：
                device：
                    /v1/createDevice
                Ras：
                    /v1/ListDeviceDetails
                    /v1/GetDeviceDetail
                    /v1/DeleteDevice
                    /v1/UpdateAssignment
        """
        # camera_info = config_obj.Clients.SubDevice.aide1  # live555模拟流
        camera_info = config_obj.Clients.SubDevice.camera1  # 真实摄像头
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        spu_name = AideBotInfo.spu_name
        # 1.创建设备device = device1
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        assignment_config = {
            "data": {
                "rules": [{
                    "roi": {
                        "vertices": [{
                            "x": 0,
                            "y": 0
                        },
                            {
                                "x": 1,
                                "y": 1
                            }
                        ]
                    },
                    "rule_id": "a",
                }]
            },
            "user_callback_url": AideCallbackAddress1
        }
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        resp = RasmanagerApi.createAssignment(device_id=device_id,
                                              assignment_config=assignment_config,
                                              rotate_config=rotate_config)
        assert resp.status_code == 200
        assignment_id = resp.json_get("assignment.assignment_id")
        # 4.更新assignment
        assignment_config_update = {
            "data": {
                "rules": [{
                    "roi": {
                        "vertices": [
                            {
                                "x": 0.1,
                                "y": 0.1
                            },
                            {
                                "x": 0.5,
                                "y": 0.5
                            },
                            {
                                "x": 0.9,
                                "y": 0.9
                            }
                        ]
                    },
                    "rule_id": "b",
                }]
            },
            "user_callback_url": AideCallbackAddress1
        }
        resp = RasmanagerApi.RasManager_UpdateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config_update,
                                                                rotate_config=None)
        assert resp.status_code == 200
        # 5.查询assignment
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        assert resp.status_code == 200
        assert resp.json_get("assignment.assignment_id") == assignment_id
        assert resp.json_get("assignment.spu_name") == spu_name
        assert resp.json_get("assignment.account_id") == user_info.account_id
        assert resp.json_get("assignment.device_id") == device_id
        assert resp.json_get("assignment.assignment_config") == assignment_config_update
        assert resp.json_get("assignment.rotate_config") == rotate_config
        assert resp.json_get("assignment.state")

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_010_AideAssignmentUpdateRotateConfig(self, RasmanagerAideApi, DeviceApi, AideBotInfo,
                                                           cluster_info,
                                                           AideCallbackAddress1, config_obj, user_info):
        """ 更新assignment的rotateconfig"""
        """
            覆盖接口：
                device：
                    /v1/createDevice
                Ras：
                    /v1/ListDeviceDetails
                    /v1/GetDeviceDetail
                    /v1/DeleteDevice
                    /v1/UpdateAssignment
        """
        # camera_info = config_obj.Clients.SubDevice.aide1  # live555模拟流
        camera_info = config_obj.Clients.SubDevice.camera1  # 真实摄像头
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        spu_name = AideBotInfo.spu_name
        # 1.创建设备device = device1
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        assignment_config = {
            "data": {
                "rules": [{
                    "roi": {
                        "vertices": [{
                            "x": 0,
                            "y": 0
                        },
                            {
                                "x": 1,
                                "y": 1
                            }
                        ]
                    },
                    "rule_id": "a",
                }]
            },
            "user_callback_url": AideCallbackAddress1
        }
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        resp = RasmanagerApi.createAssignment(device_id=device_id,
                                              assignment_config=assignment_config,
                                              rotate_config=rotate_config)
        assert resp.status_code == 200
        assignment_id = resp.json_get("assignment.assignment_id")
        assert resp.json_get("assignment.assignment_id")
        assert resp.json_get("assignment.spu_name") == spu_name
        assert resp.json_get("assignment.account_id") == user_info.account_id
        assert resp.json_get("assignment.device_id") == device_id
        assert resp.json_get("assignment.assignment_config") == assignment_config
        assert resp.json_get("assignment.rotate_config") == rotate_config
        assert resp.json_get("assignment.state")
        # 3.查询assignment
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        assert resp.status_code == 200
        assert resp.json_get("assignment.assignment_id")
        assert resp.json_get("assignment.spu_name") == spu_name
        assert resp.json_get("assignment.account_id") == user_info.account_id
        assert resp.json_get("assignment.device_id") == device_id
        assert resp.json_get("assignment.assignment_config") == assignment_config
        assert resp.json_get("assignment.rotate_config") == rotate_config
        assert resp.json_get("assignment.state")
        # 4.更新assignment
        rotate_config_update = {
            "retention": {
                "day": 3
            }
        }
        resp = RasmanagerApi.RasManager_UpdateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=None,
                                                                rotate_config=rotate_config_update)
        assert resp.status_code == 200
        # 5.查询assignment
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        assert resp.status_code == 200
        assert resp.json_get("assignment.assignment_id") == assignment_id
        assert resp.json_get("assignment.spu_name") == spu_name
        assert resp.json_get("assignment.account_id") == user_info.account_id
        assert resp.json_get("assignment.device_id") == device_id
        assert resp.json_get("assignment.assignment_config") == assignment_config
        assert resp.json_get("assignment.rotate_config") == rotate_config_update
        assert resp.json_get("assignment.state")

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_011_AideAssignmentWithMutipDevice(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                                        cluster_info):
        """ 1个bot绑定多个设备	"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        # 创建设备device0， device1
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        time.sleep(1)
        device_id1 = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 绑定设备device0到demo bot上
        resp = RasmanagerApi.createAssignment(device_id)
        assert resp.status_code == 200
        resp = RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)
        # 查询bot及设备绑定关系
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        assert resp.status_code == 200
        assert resp.json_get("assignment.state") == 'AS_EL_RUNNING'
        assert resp.json_get("assignment.device_id") == device_id
        # 绑定设备device1到demo bot上
        resp = RasmanagerApi.createAssignment(device_id1)
        assert resp.status_code == 200
        resp = RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id1)
        # 查询bot及设备绑定关系
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id1, spu_name=None)
        assert resp.status_code == 200
        assert resp.json_get("assignment.state") == 'AS_EL_RUNNING'
        assert resp.json_get("assignment.device_id") == device_id1

    @pytest.mark.P0
    @pytest.mark.Regression
    @pytest.mark.skip("需要准备多个bot")
    def test_scenario_012_deviceWithMutipBot(self, RasmanagerEasyBotApi, RasmanagerAideApi, DeviceApi, EasyBotInfo,
                                             camera_info, cluster_info):
        """ 1个设备被绑定到多个bot"""
        deviceKindId = EasyBotInfo.deviceKindId
        # 1.创建设备device0
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindId, camera_info, cluster_info)

        # 4.绑定设备device0到demo bot2 上
        resp = RasmanagerAideApi.createAssignment(device_id)
        assert resp.status_code == 200
        resp = RasmanagerAideApi.getAssignmentsUntilRunning(device_id=device_id)
        # 5.查询bot2及设备绑定关系
        resp = RasmanagerAideApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        assert resp.status_code == 200
        assert resp.json_get("assignment.state") == 'AS_EL_RUNNING'
        assert resp.json_get("assignment.device_id") == device_id

        # 2.绑定设备device0到demo bot1 上
        resp = RasmanagerEasyBotApi.createAssignment(device_id)
        assert resp.status_code == 200
        resp = RasmanagerEasyBotApi.getAssignmentsUntilRunning(device_id=device_id)
        # 3.查询bot1及设备绑定关系
        resp = RasmanagerEasyBotApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        assert resp.status_code == 200
        assert resp.json_get("assignment.state") == 'AS_EL_RUNNING'
        assert resp.json_get("assignment.device_id") == device_id

        # 查询设备
        resp = RasmanagerEasyBotApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        assert resp.json_get("device_detail.spus")
        assert len(resp.json_get("device_detail.spus")) == 2

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_013_deviceWithBotAgainFailed(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                                   cluster_info):
        """ 1个bot只能绑定同一个设备1次"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 1.创建设备device0
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.绑定设备device0到demo bot上
        resp = RasmanagerApi.createAssignment(device_id)
        assert resp.status_code == 200
        resp = RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)
        # 3.查询bot1及设备绑定关系
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        assert resp.status_code == 200
        assert resp.json_get("assignment.state") == 'AS_EL_RUNNING'
        assert resp.json_get("assignment.device_id") == device_id
        # 4.再次绑定设备device0到demo bot上
        resp = RasmanagerApi.createAssignment(device_id)
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_014_ListAssignmentWithBot(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                                cluster_info):
        """ 查询bot下的所有assignment列表"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 创建设备device0, device1, device2, device3
        device_ids = []
        for x in range(3):
            device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
            device_ids.append(device_id)
            time.sleep(1)

        # bot绑定device.
        assignment_config = {
            "data": {
                "rules": [{
                    "roi": {
                        "vertices": [{
                            "x": 0,
                            "y": 0
                        },
                            {
                                "x": 1,
                                "y": 1
                            }
                        ]
                    },
                    "rule_id": "a",
                }]
            },
            "user_callback_url": "http://10.4.132.19:9999"
            # "user_callback_url": ""
        }
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        for device_id in device_ids:
            resp = RasmanagerApi.createAssignment(device_id, assignment_config=assignment_config,
                                                  rotate_config=rotate_config)
            assert resp.status_code == 200

        # 查询该bot下的device0的assignment list
        for device_id in device_ids:
            resp = RasmanagerApi.RasManager_ListAssignmentsGetApi(device_id=device_id)
            with check: assert resp.status_code == 200
            with check: assert len(resp.json_get("assignments")) == 1
            with check: assert resp.json_get("assignments.0.device_id") == device_id
            with check: assert resp.json_get("assignments.0.spu_name")
            with check: assert resp.json_get("assignments.0.assignment_config") == assignment_config
            with check: assert resp.json_get("assignments.0.rotate_config") == rotate_config

        # 查询该bot下的所有的assignment list
        assignments = RasmanagerApi.getAllAssignments()
        for assignment in assignments:
            if device_ids and assignment["device_id"] in device_ids:
                with check: assert assignment["spu_name"]
                with check: assert assignment["assignment_config"] == assignment_config
                with check: assert assignment["rotate_config"] == rotate_config
                device_ids.remove(assignment["device_id"])
        assert not device_ids

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_015_deleteDeviceSuccess(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                              cluster_info):
        """ 删除设备-未绑定删除成功"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 创建设备device0
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 删除设备device0
        resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code == 200
        # 查询设备
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 404

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_016_deleteDeviceWithAssignmentFailed(self, RasmanagerAideApi, DeviceApi, AideBotInfo,
                                                           camera_info, cluster_info):
        """ 删除设备-绑定删除失败"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 创建设备device0
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 创建assignment
        resp = RasmanagerApi.createAssignment(device_id)
        assert resp.status_code == 200
        # 删除设备
        resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code == 403
        # 删除assignment
        resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
        # 删除设备
        resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code == 200
        # 查询设备
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 404

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_017_updateDeviceSuccess(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                              cluster_info):
        """ 更新设备-未绑定允许更新"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 创建设备device0
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 查询设备device0
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
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
        resp = RasmanagerApi.RasManager_UpdateDevicePostApi(device_id=device_id, name=device_name,
                                                            desc=device_desc, driver=driver,
                                                            extra_info=extra_info)
        assert resp.status_code == 200
        time.sleep(30)
        # 查询设备
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        assert resp.json_get("device_detail.device.desc") == device_desc
        assert resp.json_get("device_detail.device.driver.ingresses.0.name") == device_name
        assert resp.json_get("device_detail.device.name") == device_name

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_018_updateDeviceWithAssignmentFailed(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                                           cluster_info):
        """ 更新设备-绑定不允许更新"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 创建设备device0
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 创建assignment
        resp = RasmanagerApi.createAssignment(device_id)
        assert resp.status_code == 200
        # 查询设备device0
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
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
        resp = RasmanagerApi.RasManager_UpdateDevicePostApi(device_id=device_id, name=device_name,
                                                            desc=device_desc, driver=driver,
                                                            extra_info=extra_info)
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_019_GetDeviceDetailWithUnBindDevice(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                                          cluster_info):
        """ 查询未绑定设备，没有spus信息"""
        # 创建设备device0,device1
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        name = "waDevice_%s" % time_utils.get_time_str()
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
                    "name": name,
                    "description": ""
                }
            ],
        }
        desc = "test"
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info, name=name,
                                                   driver=driver, desc=desc)
        # 获取单个设备信息device0
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        assert not resp.json_get("device_detail.spus")

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_020_GetDeviceDetailWithBindDevice(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                                        cluster_info):
        """ 获取单个设备信息"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        # 创建设备device0,device1
        name = "waDevice_%s" % time_utils.get_time_str()
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
                    "name": name,
                    "description": ""
                }
            ],
        }
        desc = "test"
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info, name=name, driver=driver,
                                                   desc=desc)
        # 创建assignment with device0
        resp = RasmanagerApi.createAssignment(device_id)
        assert resp.status_code == 200

        # 获取单个设备信息device0
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200
        assert len(resp.json_get("device_detail.spus")) == 1  # 仅绑定了1个spu
        assert resp.json_get("device_detail.spus.0.name") == AideBotInfo.spu_name
        assert resp.json_get("device_detail.spus.0.display_name") == AideBotInfo.spu_display_name

    def test_scenario_021_ListDeviceDetailWithPageTotal(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                                        cluster_info):
        """ 设备列表分页验证"""
        # 1.不传参数
        RasmanagerApi = RasmanagerAideApi
        resp = RasmanagerApi.RasManager_ListDeviceDetailsGetApi()
        assert resp.status_code == 200
        assert resp.json_get("paging.total") is not None
        assert resp.json_get("paging.limit") == 50
        assert resp.json_get("paging.offset") == 0
        deviceCountTotal = resp.json_get("paging.total")
        deviceCount = len(resp.json_get("device_detail"))

        resp = RasmanagerApi.RasManager_ListDeviceDetailsGetApi(spu_names=[AideBotInfo.spu_name])
        assert resp.status_code == 200
        AideDeviceCountTotal = resp.json_get("paging.total")
        AideDeviceCount = len(resp.json_get("device_detail"))

        resp = RasmanagerApi.RasManager_ListDeviceDetailsGetApi(spu_names=[AideBotInfo.spu_name], paging_limit=1)
        assert resp.status_code == 200
        AideDeviceCountLimit1Total = resp.json_get("paging.total")
        AideDeviceCountLimit1 = len(resp.json_get("device_detail"))

        resp = RasmanagerApi.RasManager_ListDeviceDetailsGetApi(filter_with_spu=True)
        assert resp.status_code == 200
        AideDeviceCountBindTotal = resp.json_get("paging.total")
        AideDeviceCountBind = len(resp.json_get("device_detail"))

        resp = RasmanagerApi.RasManager_ListDeviceDetailsGetApi(filter_with_spu=False)
        assert resp.status_code == 200
        AideDeviceCountUnBindTotal = resp.json_get("paging.total")
        AideDeviceCountUnBind = len(resp.json_get("device_detail"))
        log().info("deviceCount:%s/%s" % (deviceCount, deviceCountTotal))
        log().info("AideDeviceCount:%s/%s" % (AideDeviceCount, AideDeviceCountTotal))
        log().info("AideDeviceCountLimit1:%s/%s" % (AideDeviceCountLimit1, AideDeviceCountLimit1Total))
        log().info("AideDeviceCountBind:%s/%s" % (AideDeviceCountBind, AideDeviceCountBindTotal))
        log().info("AideDeviceCountUnBind:%s/%s" % (AideDeviceCountUnBind, AideDeviceCountUnBindTotal))

    @pytest.mark.skip("手工测试用例")
    def test_scenario_022_ListDeviceDetailAcc(self, RasmanagerEasyBotApi, RasmanagerAideApi, DeviceApi, EasyBotInfo,
                                              AideBotInfo, camera_info, cluster_info):
        """ 接口返回结果正确性测试"""
        offset = 0
        easyBotDevices = []
        AideBotDevices = []
        otherBotDevices = []
        UnBindDevice = []
        while True:
            resp = RasmanagerEasyBotApi.RasManager_ListDeviceDetailsGetApi(paging_offset=offset, paging_limit=50)
            assert resp.status_code == 200
            if len(resp.json_get("device_detail")) == 0:
                break
            for deviceInfo in resp.json_get("device_detail"):
                if deviceInfo['spus']:
                    for spu in deviceInfo['spus']:
                        if spu['name'] == EasyBotInfo.spu_name:
                            easyBotDevices.append(deviceInfo)
                        elif spu['name'] == AideBotInfo.spu_name:
                            AideBotDevices.append(deviceInfo)
                        else:
                            otherBotDevices.append(deviceInfo)
                else:
                    UnBindDevice.append(deviceInfo)
            offset += 50

        resp = RasmanagerEasyBotApi.RasManager_ListDeviceDetailsGetApi(spu_names=[EasyBotInfo.spu_name])
        with check:
            assert len(resp.json_get("device_detail")) == len(easyBotDevices), '查询easyBotDevices数量错误'

        resp = RasmanagerEasyBotApi.RasManager_ListDeviceDetailsGetApi(spu_names=[AideBotInfo.spu_name])
        with check:
            assert len(resp.json_get("device_detail")) == len(AideBotDevices), '查询AideBotDevices数量错误'

        resp = RasmanagerEasyBotApi.RasManager_ListDeviceDetailsGetApi(
            spu_names=[AideBotInfo.spu_name, EasyBotInfo.spu_name])
        with check:
            assert len(resp.json_get("device_detail")) == len(AideBotDevices) + len(easyBotDevices), \
                '查询AideBotDevices和EasyBot数量错误'

        resp = RasmanagerEasyBotApi.RasManager_ListDeviceDetailsGetApi(filter_with_spu=True)
        with check:
            assert len(resp.json_get("device_detail")) == len(easyBotDevices) + len(AideBotDevices) + len(
                otherBotDevices), '查询filter_with_spu=True数量错误'

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_023_ListDeviceDetailWithPageOffset(self, RasmanagerAideApi, DeviceApi, AideBotInfo, camera_info,
                                                         cluster_info):
        """ 获取单个设备信息"""
        resp = RasmanagerAideApi.RasManager_ListDeviceDetailsGetApi(paging_offset=1, paging_limit=1)
        assert resp.status_code == 200

    @pytest.mark.skip("手工测试用例")
    def test_scenario_024_CreateAssignmentWithUnSupportDeviceKindFailed(self, RasmanagerAideApi, DeviceApi,
                                                                        AideBotInfo, camera_info, cluster_info):
        """ 不支持的设备类型绑定bot"""
        device_id = DeviceApi.createDeviceWithRTSP(AideBotInfo.noSupportdeviceKindName, camera_info, cluster_info)
        resp = RasmanagerAideApi.createAssignment(device_id)
        assert resp.status_code == 400

    @pytest.mark.skip("手工测试用例")
    def test_scenario_030_scavenger(self, RasmanagerAideApi, DeviceApi, camera_info, AideBotInfo,
                                    cluster_info):
        """ 正常清理"""
        deviceKindName = AideBotInfo.deviceKindName

        # 1.创建设备device0
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)

        # 4.绑定设备device0到demo bot2 上
        rotate_config = {
            "retention": {
                "day": 3
            }
        }
        resp = RasmanagerAideApi.createAssignment(device_id, rotate_config=rotate_config)
        assert resp.status_code == 200
        resp = RasmanagerAideApi.getAssignmentsUntilRunning(device_id=device_id)
        i = 0
        # 更新assignment
        rotate_config_update = {
            "retention": {
                "day": 5
            }
        }
        resp = RasmanagerAideApi.RasManager_UpdateAssignmentPostApi(device_id=device_id,
                                                                    assignment_config=None,
                                                                    rotate_config=rotate_config_update)
        assert resp.status_code == 200

        i = 0

        # 更新assignment
        rotate_config_update = {
            "retention": {
                "day": 1
            }
        }
        resp = RasmanagerAideApi.RasManager_UpdateAssignmentPostApi(device_id=device_id,
                                                                    assignment_config=None,
                                                                    rotate_config=rotate_config_update)
        assert resp.status_code == 200

        i = 0
        # 更新assignment
        rotate_config_update = None
        resp = RasmanagerAideApi.RasManager_UpdateAssignmentPostApi(device_id=device_id,
                                                                    assignment_config=None,
                                                                    rotate_config=rotate_config_update)
        assert resp.status_code == 200

    @pytest.mark.skip("查看callback是否有数据")
    def test_scenario_031_AssignmentCallBackEasyBotReceivedMessage(self, RasmanagerEasyBotApi, DeviceApi, EasyBotInfo,
                                                                   camera_info, cluster_info):
        """ callback收到消息，半自动	"""
        RasmanagerApi = RasmanagerEasyBotApi
        deviceKindName = EasyBotInfo.deviceKindName

        # 创建设备device0， device1
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 绑定设备device0到demo bot上
        resp = RasmanagerApi.createAssignment(device_id)
        assert resp.status_code == 200
        resp = RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)
        # 查询bot及设备绑定关系
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        assert resp.status_code == 200
        assert resp.json_get("assignment.state") == 'AS_EL_RUNNING'
        assert resp.json_get("assignment.device_id") == device_id
        # 查看是否有callback消息
        i = 0

    @pytest.mark.skip("查看callback是否有数据")
    def test_scenario_032_AssignmentCallBackAideReceivedMessage(self, config_obj, RasmanagerAideApi, DeviceApi,
                                                                AideBotInfo, camera_info, cluster_info):
        """ callback收到消息，半自动	"""
        # camera_info = config_obj.Clients.SubDevice.camera1
        camera_info = config_obj.Clients.SubDevice.aide1
        # camera_info = config_obj.Clients.SubDevice.camera2
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 创建设备device0， device1
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info, is_delete=False)
        # 绑定设备device0到demo bot上
        resp = RasmanagerApi.createAssignment(device_id, is_delete=False)
        assert resp.status_code == 200
        resp = RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)
        # 查询bot及设备绑定关系
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=True)
        assert resp.status_code == 200
        assert resp.json_get("assignment.state") == 'AS_EL_RUNNING'
        assert resp.json_get("assignment.device_id") == device_id
        # 查看是否有callback消息
        i = 0

    @pytest.mark.skip("手工测试")
    def test_scenario_033_AssignmentDaDian(self, config_obj, RasmanagerAideApi, DeviceApi,
                                           AideBotInfo, camera_info, cluster_info):
        """ 打点，返回绑定，数量不增加"""
        camera_info = config_obj.Clients.SubDevice.camera1
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 创建设备device0， device1
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info, is_delete=False)
        # 绑定设备device0到demo bot上
        resp = RasmanagerApi.createAssignment(device_id, is_delete=False)
        assert resp.status_code == 200
        resp = RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)
        # 查询bot及设备绑定关系
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=True)
        assert resp.status_code == 200
        assert resp.json_get("assignment.state") == 'AS_EL_RUNNING'
        assert resp.json_get("assignment.device_id") == device_id
        # 查看是否有callback消息
        resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id)
        i = 0
        resp = RasmanagerApi.createAssignment(device_id, is_delete=False)
        i = 0
        resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id)
        i = 0
        resp = RasmanagerApi.createAssignment(device_id, is_delete=False)
        i = 0
        resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id)
        i = 0
        resp = RasmanagerApi.createAssignment(device_id, is_delete=False)

    @pytest.mark.skip("手工测试")
    def test_scenario_034_AssignmentFaildDaDian(self, config_obj, RasmanagerAideApi, DeviceApi,
                                                AideBotInfo, camera_info, cluster_info):
        """ 接口调用失败，打点，数量不增加"""
        camera_info = config_obj.Clients.SubDevice.camera1
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        # 创建设备device0， device1
        # device_id = DeviceApi.createDeviceWithRTSP(deviceKindId, camera_info, cluster_info, is_delete=True)
        device_id = "123456"
        # 绑定设备device0到demo bot上
        assignment_config = {
            "data": {
                "rules": [{
                    "roi": {
                        "vertices": [{
                            "x": 0,
                            "y": 0
                        },
                            {
                                "x": 1,
                                "y": 1
                            }
                        ]
                    },
                    "rule_id": "a",
                }]
            },
            "user_callback_url": "http://10.4.132.19:9999"
            # "user_callback_url": ""
        }
        resp = RasmanagerApi.createAssignment(device_id, assignment_config=assignment_config, is_delete=True)
        assert resp.status_code != 200

    #@pytest.mark.skip("rtmp流程")
    def test_scenario_035_rtmp(self, config_obj, RasmanagerAideApi, DeviceApi,
                               AideBotInfo, camera_info, cluster_info):
        """ rtmp流程，半自动	"""
        camera_info = config_obj.Clients.SubDevice.camera2  # 不需要
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 创建设备device0， device1
        resp = DeviceApi.createDeviceWithRTMP(deviceKindName, camera_info, cluster_info, is_delete=True, ret_response=True)

        time.sleep(5)
        device_id = resp.json_get("device.id")
        ak = resp.json_get("device.verify.user_info.ak")
        sk = resp.json_get("device.verify.user_info.sk")
        token = sign_utils.encode_jwt_token(ak, sk)

        resp = DeviceApi.DeviceManagerCenter_GenRTMPAddressPostApi(device_id=device_id, duration='NO_EXPIRED',
                                                                   loginToken=token)
        assert resp.status_code == 403
        assert resp.json_get("error.message") == 'Forbidden'

        # 绑定设备device0到demo bot上
        resp = RasmanagerApi.createAssignment(device_id, is_delete=True)
        assert resp.status_code == 200

        time.sleep(30)
        resp = DeviceApi.DeviceManagerCenter_GenRTMPAddressPostApi(device_id=device_id, duration='NO_EXPIRED',
                                                                   loginToken=token)
        assert resp.status_code == 200

        i = 0 # 推流 手动操作
        # resp = RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)

        # 查询bot及设备绑定关系
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=True)
        assert resp.status_code == 200
        # assert resp.json_get("assignment.state") == 'AS_EL_RUNNING'
        # assert resp.json_get("assignment.device_id") == device_id
        # 查看是否有callback消息

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_036_ListDeviceBySpu(self, config_obj, RasmanagerApi, AideBotInfo):
        """  查询账号下的设备,给管理台用的 """
        resp = RasmanagerApi.RasManager_ListAccountDeviceSpusGetApi()
        assert resp.status_code == 200
        assert resp.json_get("spus.0.display_name") == AideBotInfo.spu_display_name
        assert resp.json_get("spus.0.name") == AideBotInfo.spu_name

        spu_names = [resp.json_get("spus.0.name")]
        paging_offset =0
        paging_limit = 50
        paging_total = 100
        resp = RasmanagerApi.RasManager_ListAllDeviceDetailsGetApi(spu_names=spu_names, paging_offset=paging_offset,
                                                                   paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    # @pytest.mark.P0
    # @pytest.mark.Regression
    #@pytest.mark.skip("目前存在多任务无告警的bug")
    def test_scenario_037_DataCollectingTaskCRD(self, DeviceApi, config_obj, RasmanagerAideApi, AideBotInfo,
                                                cluster_info):
        """  数据回流任务增加，更新，删除 """

        # 1.准备设备
        # 获取当前时间
        today_time = time_utils.get_str_by_timestamp(formate="%Y-%m-%d")
        camera_info = config_obj.Clients.SubDevice.camera2  # 永久播放的流
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        assignment_config = {
            "data": {
                "rules": [{
                    "roi": {
                        "vertices": [
                            {
                                "x": 0,
                                "y": 0
                            },
                            {
                                "x": 1,
                                "y": 0
                            },
                            {
                                "x": 1,
                                "y": 1
                            },
                            {
                                "x": 0,
                                "y": 1
                            }
                        ]
                    },
                    "rule_id": "lcrules",
                }]
            },
            "user_callback_url": "http://10.4.132.35:9999"
        }
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code == 200
        # 3.此步骤保证任务是running
        RasmanagerAideApi.getAssignmentsUntilRunning(device_id=device_id)

        # 任务运行120秒，产生一定量的告警
        log().info("任务运行30秒，产生一定量的告警")
        time.sleep(30)
        resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
        assert resp.status_code == 200

        """  数据回流任务增查删 """
        # - EQ: 等于 - GT: 大于 - GTE: 大于等于 - LT: 小于 - LTE: 小于等于 - NE: 不等于 - IN: 包含于 - NIN: 不包含于
        # 1、新建数据回流任务
        devices = [
            device_id
        ]
        start_time = 0
        end_time = 86400
        value = 0.8
        operator = "GTE"

        start_date = today_time
        end_date = today_time
        # 从配置文件中拿到ceph_config
        access_key_id = config_obj.Clients.ceph.config.access_key_id
        access_key_secret = config_obj.Clients.ceph.config.access_key_secret

        resp = RasmanagerAideApi.CreateDataCollectingTask(devices=devices, start_time=start_time, end_time=end_time,
                                                          value=value, operator=operator, start_date=start_date,
                                                          end_date=end_date, access_key=access_key_id,
                                                          secret_key=access_key_secret)
        taskid = resp.json_get("task_id")
        assert resp.status_code == 200
        assert resp.json_get("success") == True

        # 2、根据task_id查询任务
        resp = RasmanagerAideApi.RasManager_GetDataCollectingTaskGetApi(task_id=taskid)
        siphon_job_id = resp.json_get("task.siphon_job_id")
        assert resp.status_code == 200
        assert resp.json_get("task.task_id") == taskid

        # 3.此步骤保证任务最终状态是Submited
        RasmanagerAideApi.getDataCollectingTaskUntilSubmited(task_id=taskid)

        # 3、list所有数据回流任务，看创建的任务是否在list里
        resp = RasmanagerAideApi.ListAllDataCollectingTask(paging_offset=0, paging_limit=100,
                                                           paging_total=100)
        assert taskid in resp

        #4、删除这个数据回流任务
        resp=RasmanagerAideApi.RasManager_DeleteDataCollectingTaskPostApi(task_id=taskid)
        assert resp.status_code == 200

        # 5、删除所有数据回流任务
        resp = RasmanagerAideApi.DeleteAllDataCollectingTask()
        # 清空后判断任务个数是不是0
        assert len(resp.json_get("tasks")) == 0

        # """  数据回流下载文件 """
        # access_key_id = config_obj.Clients.OSS.user1.access_key_id
        # access_key_secret = config_obj.Clients.OSS.user1.access_key_secret
        # endpoint = config_obj.Clients.OSS.user1.endpoint
        # bucket_name = config_obj.Clients.OSS.user1.bucket_name
        # res = RasmanagerAideApi.download_oss(access_key_id=access_key_id, access_key_secret=access_key_secret,
        #                                      endpoint=endpoint, bucket_name=bucket_name, num=siphon_job_id)
        # for i in res:
        #     assert i >= 0.8

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_038_verbose_function(self, DeviceApi, config_obj, RasmanagerAideApi, AideBotInfo,
                                           cluster_info):
        """  显示ars任务详细参数 """
        # 1.准备设备
        camera_info = config_obj.Clients.SubDevice.camera2  # 真实摄像头
        i = 1
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        assignment_config = {
            "data": {
                "rules": [{
                    "roi": {
                        "vertices": [
                            {
                                "x": 0,
                                "y": 0
                            },
                            {
                                "x": 1,
                                "y": 1
                            }
                        ]
                    },
                    "rule_id": "lcrules",
                }]
            },
            "user_callback_url": "http://10.4.132.35:9999"
        }
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code == 200

        resp = RasmanagerAideApi.getAssignmentsUntilRunning(device_id=device_id)

        # verbose传True
        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(verbose=True, device_id=device_id)
        assert resp.status_code == 200
        assert len(resp.json_get("assignment.elements")) == 1
        assert resp.json_get("assignment.elements.0.code") == 0

        resp = RasmanagerApi.RasManager_GetAssignmentGetApi(verbose=False, device_id=device_id)
        assert resp.status_code == 200
        assert len(resp.json_get("assignment.elements")) == 0

        resp = RasmanagerApi.RasManager_ListAssignmentsGetApi(verbose=True, device_id=device_id, paging_offset=0,
                                                              paging_limit=100, paging_total=100)
        assert resp.status_code == 200
        assert len(resp.json_get("assignments.0.elements")) == 1
        assert resp.json_get("assignments.0.elements.0.code") == 0

        resp = RasmanagerApi.RasManager_ListAssignmentsGetApi(verbose=False, device_id=device_id, paging_offset=0,
                                                              paging_limit=100, paging_total=100)
        assert resp.status_code == 200
        assert len(resp.json_get("assignments.0.elements")) == 0

        # 3.任务运行2分钟后删除，此时产生一定量的告警,30秒大概5条数据
        resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
        assert resp.status_code == 200

    @pytest.mark.skip
    def test_scenario_038_downloadOSS(self, DeviceApi, config_obj, RasmanagerAideApi, AideBotInfo,
                                      cluster_info):
        """  数据回流下载文件 """

        access_key_id = config_obj.Clients.OSS.user1.access_key_id
        access_key_secret = config_obj.Clients.OSS.user1.access_key_secret
        endpoint = config_obj.Clients.OSS.user1.endpoint
        bucket_name = config_obj.Clients.OSS.user1.bucket_name
        RasmanagerAideApi.download_oss(access_key_id=access_key_id, access_key_secret=access_key_secret,
                                       endpoint=endpoint, bucket_name=bucket_name, num=301)


    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_039_rtmp_interface_check(self, config_obj, RasmanagerAideApi, DeviceApi,
                               AideBotInfo, camera_info, cluster_info):
        """ 验证一个rtmp的设备类型，调用rtmp接口	"""
        camera_info = config_obj.Clients.SubDevice.camera2  # 不需要
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        # 创建设备device0， device1
        resp = DeviceApi.createDeviceWithRTMP(deviceKindName, camera_info, cluster_info, is_delete=True, ret_response=True)

        time.sleep(5)
        device_id = resp.json_get("device.id")
        #直接使用用户的aksk生成的token调，此处用户的aksk和设备的都能调，设备的aksk得绑定Bot才有权限
        resp = DeviceApi.DeviceManagerCenter_GenRTMPAddressPostApi(device_id=device_id, duration='NO_EXPIRED')
        assert resp.status_code == 200