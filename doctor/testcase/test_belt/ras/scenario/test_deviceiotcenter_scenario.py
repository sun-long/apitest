#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestDeviceiotcenterScenario(object):
    """ Deviceiotcenter scenario test"""

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

    def test_scenario_000_demo(self):
        """ func test"""
        pass

    @pytest.mark.P0
    @pytest.mark.Regression
    #5.19 生产pass
    #5.19 stage pass
    #5.19 test pass
    def test_scenario_001_Iot_push_and_stop_RTMPlive(self, config_obj, RasmanagerAideApi,DeviceiotcenterApi):
        """  验证openAPI的rtmp推流与关闭功能"""
        # # 1、开始rtmp推流
        device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        url = config_obj.Clients.SubDevice.IotRtmp.url

        # 关闭rtmp推流
        resp = DeviceiotcenterApi.DeviceIotCenter_StopRTMPLivePostApi(device_id=device_id)
        time_utils.sleep(5)

        # TODO 自动生成url
        # 2、注意要绑定任务,case运行完删除任务
        RasmanagerApi = RasmanagerAideApi
        resp = DeviceiotcenterApi.DeviceIotCenter_PushRTMPLivePostApi(device_id=device_id, url=url)
        assert resp.status_code==200
        time.sleep(3)
        resp = RasmanagerApi.createAssignment(device_id, is_delete=True)
        assert resp.status_code == 200
        # 3.此步骤保证任务是running
        RasmanagerAideApi.getAssignmentsUntilRunning(device_id=device_id)
        #time.sleep(30)
        # 4、关闭rtmp推流
        resp = DeviceiotcenterApi.DeviceIotCenter_StopRTMPLivePostApi(device_id=device_id)
        assert resp.status_code == 200

    # 5.19 生产通过
    # 5.19 stage pass
    # 5.19 test pass
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_002_Iot_push_and_stop_Rtclive(self, config_obj, DeviceiotcenterApi,RasmanagerAideApi):
        """  验证openAPI的rtc推流与关闭功能"""
        # 1、开始rtc推流，用预先注册好的rtc设备
        device_id = config_obj.Clients.SubDevice.IotRtc.device_id
        #device_id="27d0b660028f47d5a70a2bccf461f03c"
        #ingress_id = config_obj.Clients.SubDevice.IotRtc.ingress_id

        resp = DeviceiotcenterApi.DeviceIotCenter_StopRtcLivePostApi(device_id=device_id)
        time_utils.sleep(5)
        # 2、注意要绑定任务,case运行完删除任务
        RasmanagerApi = RasmanagerAideApi
        resp = RasmanagerApi.createAssignment(device_id, is_delete=True)
        # 3、设备只有一个ingress，且为webrtc类型时可不填
        resp = DeviceiotcenterApi.DeviceIotCenter_PushRtcLivePostApi(device_id=device_id, ingress_id=None)
        assert resp.status_code == 200
        # 4.此步骤保证任务是running
        RasmanagerAideApi.getAssignmentsUntilRunning(device_id=device_id)
        #time.sleep(600)
        # 5、关闭rtc推流
        resp = DeviceiotcenterApi.DeviceIotCenter_StopRtcLivePostApi(device_id=device_id)
        assert resp.status_code == 200

    # 5.19生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_003_Iot_start_and_stop_CameraPTZ(self, config_obj, DeviceiotcenterApi):
        """  验证云台控制摄像头旋转功能，调通接口即可，无需在端上验证"""
        # 1、设置参数，开始旋转云台摄像头
        device_id = config_obj.Clients.SubDevice.IotRtc.device_id
        #device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        id = sign_utils.getUuid()
        PTZ = {
            "Pan": 1,
            "Tilt": 1,
            "Zoom": 0
        }
        resp = DeviceiotcenterApi.DeviceIotCenter_StartCameraPTZPostApi(device_id=device_id, id=id, PTZ=PTZ)
        assert resp.status_code == 200
        # 2、停止摄像头旋转
        resp = DeviceiotcenterApi.DeviceIotCenter_StopCameraPTZPostApi(device_id=device_id, id=id)
        assert resp.status_code == 200

    # 5.19生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_004_Iot_SetIpcConfig(self, config_obj, DeviceiotcenterApi):
        """  验证ipc配置下发功能"""
        device_id = config_obj.Clients.SubDevice.IotRtc.device_id
        #device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        config = "this is test config111112233"
        resp = DeviceiotcenterApi.DeviceIotCenter_SetIpcConfigPostApi(device_id=device_id, config=config)
        assert resp.status_code == 200

    # 5.19 生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_005_Iot_OtaUpgradeBase(self, config_obj, DeviceiotcenterApi):
        """  验证ota基础升级功能"""
        device_id = config_obj.Clients.SubDevice.IotRtc.device_id
        #device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        # 将一段文字写入某个文件
        cmd = "echo 'it is demo'>abc111.txt"
        resp = DeviceiotcenterApi.DeviceIotCenter_OtaUpgradeBasePostApi(device_id=device_id, cmd=cmd)
        assert resp.status_code == 200
        #删除这个文件
        cmd = "rm abc111.txt"
        resp = DeviceiotcenterApi.DeviceIotCenter_OtaUpgradeBasePostApi(device_id=device_id, cmd=cmd)
        assert resp.status_code == 200

    # 5.19 生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_006_IOT_device_create_success_UnRegister(self, DeviceApi, config_obj, RasmanagerAideApi, cluster_info):

        """  成功创建一个rtmp_iot的设备，不注册,查询，最后删除 """
        # 未注册成功的iot结构体应该如下,各个接口返回结果通用
        iot_information={
                            "type": "SYMPHONY",
                            "symphony": {
                                "registry_id": "",
                                "extra_info": ""
                            }
                        }

        # 创建设备并且验证返回结果
        resp = DeviceApi.createIOTDeviceWithRTMP(config_obj, cluster_info)
        device_id = resp.json_get("device.id")

        # 查询设备
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.json_get("device_detail.device.id") == device_id
        assert resp.json_get("device_detail.device.driver.iot.name") == "symphony-1"
        assert resp.json_get("device_detail.device.driver.iot.iot_id") == ""
        assert resp.json_get("device_detail.device.driver.iot.device_sn") == ""
        assert resp.json_get("device_detail.device.driver.iot.information") == iot_information
        assert resp.json_get("device_detail.device.driver.iot.status") == "IOT_STATUS_UNKNOWN"
        assert resp.json_get("device_detail.device.driver.iot.register_status") == "IOT_NOT_REGISTERED"

        """  成功创建一个rtc_iot的设备，不注册,查询,最后删除 """
        # 创建设备并且验证返回结果
        resp = DeviceApi.createIOTDeviceWithRTC(config_obj, cluster_info)

        # 查询设备，此时是未注册状态
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.json_get("device_detail.device.id") == device_id
        assert resp.json_get("device_detail.device.driver.iot.name") == "symphony-1"
        assert resp.json_get("device_detail.device.driver.iot.iot_id") == ""
        assert resp.json_get("device_detail.device.driver.iot.device_sn") == ""
        assert resp.json_get("device_detail.device.driver.iot.information") == iot_information
        assert resp.json_get("device_detail.device.driver.iot.status") == "IOT_STATUS_UNKNOWN"
        assert resp.json_get("device_detail.device.driver.iot.register_status") == "IOT_NOT_REGISTERED"

    # 5.19 生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_007_IOT_device_already_Register(self, DeviceApi, config_obj, RasmanagerAideApi):
        """  查询一个已经注册的iot设备的相关信息 """
        # 成功创建一个IOT_rtc的设备
        device_id = config_obj.Clients.SubDevice.IotRtc.device_id
        #device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.json_get("device_detail.device.id") == device_id
        assert resp.json_get("device_detail.device.driver.iot.name") == "symphony-1"
        assert resp.json_get("device_detail.device.driver.iot.iot_id") != ""
        assert resp.json_get("device_detail.device.driver.iot.device_sn") != ""
        assert resp.json_get("device_detail.device.driver.iot.information.type") == "SYMPHONY"
        assert resp.json_get("device_detail.device.driver.iot.information.symphony.registry_id") == "belt"
        assert resp.json_get("device_detail.device.driver.iot.status") == "IOT_STATUS_ONLINE"
        assert resp.json_get("device_detail.device.driver.iot.register_status") == "IOT_REGISTERED"

    # 5.19 生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_008_IOT_device_creata_failed_invalid_iotname(self, DeviceApi, config_obj, RasmanagerApi,
                                                                   cluster_info):
        """  IOT的name字段不合法，导致设备创建不成功 """
        devicekind_name = config_obj.Clients.devicekind.name
        name = "IOT_rtsp_Device_%s_%s" % (sign_utils.getUuid(4), time_utils.get_time_str())
        cluster = {"id": cluster_info["id"]}
        driver = {
            "ingresses": [
                {
                    "name": "ingress_rtmp_test",
                    "description": "for rtmp test",
                    "information": {
                        "type": "RTMP",
                        "rtmp": {
                            "verification": {
                                "method": "TOKEN"
                            }
                        }
                    }
                }
            ],
            "iot": {
                "name": "invalid_iot_name",
                "information": {
                    "type": "SYMPHONY"
                }
            },
            "enable": True
        }
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=devicekind_name,
                                                                           cluster=cluster, name=name, driver=driver,
                                                                           desc=None)

        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.message") == "device argument invalid"
        assert resp.json_get("error.details.0.reason") == 11403002
        assert resp.json_get("error.details.0.message") == "iot instance not found"

        # 创建设备失败，返回iot not found

    # 5.19 生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_009_IOT_device_creata_failed_invalid_iot_type(self, DeviceApi, config_obj, RasmanagerApi,
                                                                    cluster_info):
        """  IOT的name字段不填，导致设备创建不成功 """
        devicekind_name = config_obj.Clients.devicekind.name
        name = "IOT_rtsp_Device_%s_%s" % (sign_utils.getUuid(4), time_utils.get_time_str())
        cluster = {"id": cluster_info["id"]}
        driver = {
            "ingresses": [
                {
                    "name": "ingress_rtmp_test",
                    "description": "for rtmp test",
                    "information": {
                        "type": "RTMP",
                        "rtmp": {
                            "verification": {
                                "method": "TOKEN"
                            }
                        }
                    }
                }
            ],
            "iot": {
                "name": "symphony-1",
                "information": {
                    "type": "IOT_TYPE_UNKNOWN"
                }
            },
            "enable": True
        }
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=devicekind_name,
                                                                           cluster=cluster, name=name,
                                                                           driver=driver, desc=None)

        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.message") == "device argument invalid"
        assert resp.json_get("error.details.0.reason") == 11403002
        assert resp.json_get(
            "error.details.0.message") == "device iot type(IOT_TYPE_UNKNOWN) not match devicekind iot type(SYMPHONY)"

    # 5.19 生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_010_IOT_device_creata_failed_iot_name_is_null(self, DeviceApi, config_obj, RasmanagerApi,
                                                                    cluster_info):
        """  IOT的iot_name不填，导致设备创建不成功 """
        devicekind_name = config_obj.Clients.devicekind.name
        name = "IOT_rtsp_Device_%s_%s" % (sign_utils.getUuid(4), time_utils.get_time_str())
        cluster = {"id": cluster_info["id"]}
        driver = {
            "ingresses": [
                {
                    "name": "ingress_rtmp_test",
                    "description": "for rtmp test",
                    "information": {
                        "type": "RTMP",
                        "rtmp": {
                            "verification": {
                                "method": "TOKEN"
                            }
                        }
                    }
                }
            ],
            "iot": {
                "information": {
                    "type": "SYMPHONY"
                }
            },
            "enable": True
        }
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=devicekind_name,
                                                                           cluster=cluster, name=name,
                                                                           driver=driver, desc=None)

        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.message") == "device argument invalid"
        assert resp.json_get("error.details.0.reason") == 11403002
        assert resp.json_get("error.details.0.message") == "iot instance not found"


    # 5.19 生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_011_IOT_device_creata_failed_iot_type_is_null(self, DeviceApi, config_obj, RasmanagerApi,
                                                                    cluster_info):
        """  IOT的type字段填空，导致设备创建不成功 """
        devicekind_name = config_obj.Clients.devicekind.name
        name = "IOT_rtsp_Device_%s_%s" % (sign_utils.getUuid(4), time_utils.get_time_str())
        cluster = {"id": cluster_info["id"]}
        driver = {
            "ingresses": [
                {
                    "name": "ingress_rtmp_test",
                    "description": "for rtmp test",
                    "information": {
                        "type": "RTMP",
                        "rtmp": {
                            "verification": {
                                "method": "TOKEN"
                            }
                        }
                    }
                }
            ],
            "iot": {
                "name": "symphony-1",
                "information": {
                    "type": ""
                }
            },
            "enable": True
        }
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=devicekind_name,
                                                                           cluster=cluster, name=name,
                                                                           driver=driver, desc=None)

        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert "invalid value for enum type" in resp.json_get("error.message")

    # 5.19 生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_012_IOT_RegisterRtRtcDevice_not_allow(self, DeviceApi, config_obj, RasmanagerApi, cluster_info):
        """  已经成功创建的iot-Rtc设备,不允许更新iot信息 """
        # 如果设备绑定Bot，需要先解绑，否则报错信息不是iot update not support
        # device_id = config_obj.Clients.SubDevice.IotRtc.device_id
        resp = DeviceApi.createIOTDeviceWithRTMP(config_obj, cluster_info)
        device_id = resp.json_get("device.id")
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        driver_id = resp.json_get("device_detail.device.driver.driver_id")
        update_name = resp.json_get("device_detail.device.name") + "update"
        driver = {
            "driver_id": driver_id,
            "iot": {
                "name": "symphony-1",
                "information": {
                    "type": "SYMPHONY"
                }
            },
            "enable": True
        }
        resp = RasmanagerApi.RasManager_UpdateDevicePostApi(device_id=device_id, name=update_name, desc=None,
                                                            driver=driver, extra_info=None)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.message") == "iot update not support"
        assert resp.json_get("error.details.0.reason") == 11403025
        assert resp.json_get("error.details.0.message") == "iot update not support"

    # 5.19 生产通过
    # 5.19 stage pass
    # 5.19 test通过
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_013_IOT_RtmpDevice_allow_update(self, DeviceApi, config_obj, RasmanagerApi, cluster_info):
        """  已经成功创建的iot-Rtc设备,允许更新非iot信息,回归之前case """
        resp = DeviceApi.createIOTDeviceWithRTMP(config_obj, cluster_info)
        device_id = resp.json_get("device.id")
        resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        # driver_id = resp.json_get("device_detail.device.driver.driver_id")
        # 允许更新设备和描述信息
        update_name = resp.json_get("device_detail.device.name") + "update"
        desc = str(sign_utils.getTime())
        resp = RasmanagerApi.RasManager_UpdateDevicePostApi(device_id=device_id, name=update_name, desc=desc,
                                                            driver=None, extra_info=None)

        assert resp.json_get("device_detail.device.name") == update_name
        assert resp.json_get("device_detail.device.desc") == desc
        assert resp.status_code == 200

        # assert resp.json_get("error.code") == 3
        # assert resp.json_get("error.message") == "iot update not support"
        # assert resp.json_get("error.details.0.reason") == 11403025
        # assert resp.json_get("error.details.0.message") == "iot update not support"

    # pass5.4
    # 5.16 stage通过
    @pytest.mark.skip(msg="需要手动停止服务，才能执行这个case")
    def test_scenario_014_IOT_RegisterRtRtcDevice_stop_edge_server(self, DeviceApi, config_obj, RasmanagerAideApi, cluster_info):
        """  成功注册的设备，手动将端服务停掉，此设备的状态会由IOT_STATUS_ONLINE变成IOT_STATUS_OFFLINE """
        device_id = config_obj.Clients.SubDevice.IotRtc.device_id
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.json_get("device_detail.device.driver.iot.status") == "IOT_STATUS_OFFLINE"

