#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


@pytest.mark.checkin
@pytest.mark.device
class TestDeviceApi(object):
    """ device Api测试"""

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

    def test_api_DeviceManagerCenter_BatchCreateDevice(self, config_obj, DeviceApi, camera_info, cluster_info, AideBotInfo):
        """  批量创建Device """
        request_header = None
        devices = []
        devicekind_name = AideBotInfo.deviceKindName
        for x in range(2):
            devices.append({
              "cluster": {
                "id": cluster_info["id"]
              },
              "desc": "test",
              "devicekind_name": devicekind_name,
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
              # "name": "device_%s_%s" % (x, sign_utils.getUuid(5))
            })
        resp = DeviceApi.DeviceManagerCenter_BatchCreateDeviceByKindNamePostApi(request_header=request_header, devices=devices)
        assert resp.status_code == 200
        assert resp.json_get("devices.0.error.message") == "invalid BatchDevice.Name: value length must be between 1 and 64 runes, inclusive"
        assert resp.json_get("devices.1.error.message") == "invalid BatchDevice.Name: value length must be between 1 and 64 runes, inclusive"


    def test_api_DeviceManagerCenter_CreateDevice(self, config_obj, deviceKindAide, DeviceApi, camera_info, AideBotInfo,
                                                  cluster_info):
        """  创建Device, 设备鉴权信息创建时不用指定，会在创建设备时自动创建鉴权信息并返回，不能修改 """
        request_header = None
        devicekind_name = AideBotInfo.deviceKindName
        # name = "device_%s" % sign_utils.getUuid(5)
        name = None
        desc = "test"
        cluster = {"id": cluster_info["id"]}
        extra_info = None
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
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(request_header=request_header,
                                                                 devicekind_name=devicekind_name, name=name, desc=desc,
                                                                 cluster=cluster, extra_info=extra_info, driver=driver)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "invalid CreateDeviceByKindNameReq.Name: value length must be between 1 and 64 runes, inclusive"

    def test_api_DeviceManagerCenter_GenRTMPAddress(self, config_obj, DeviceApi):
        """  生成RTMP推流地址, 生成的地址过期时间为1小时, 超时后需要重新生成."""
        device_id = "1234"
        ingress_id = None
        duration = None
        resp = DeviceApi.DeviceManagerCenter_GenRTMPAddressPostApi(device_id=device_id, ingress_id=ingress_id,
                                                                   duration=duration)
        assert resp.status_code == 404
        assert resp.json_get("error.message") == "device not found"
