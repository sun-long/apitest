#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestDeviceiotcenterApi(object):
    """ deviceIotCenter Api测试"""

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

    #pass
    def test_api_DeviceIotCenter_OtaUpgradeBase_rtmp(self, config_obj, DeviceiotcenterApi):
        """  ota基础升级
route: prefix=, internal_prefix=device, ac... """
        device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        cmd = "echo 'it is demo hahahah'>abc111.txt"
        resp = DeviceiotcenterApi.DeviceIotCenter_OtaUpgradeBasePostApi(device_id=device_id, cmd=cmd)
        assert resp.status_code == 200
        cmd = "rm abc111.txt"
        resp = DeviceiotcenterApi.DeviceIotCenter_OtaUpgradeBasePostApi(device_id=device_id, cmd=cmd)
        assert resp.status_code == 200

    #pass 5.4
    def test_api_DeviceIotCenter_OtaUpgradeBase_rtc(self, config_obj, DeviceiotcenterApi):
        """  ota基础升级
route: prefix=, internal_prefix=device, ac... """
        device_id = config_obj.Clients.SubDevice.IotRtc.device_id
        cmd = "echo 'it is demo hahahah'>abc111.txt"
        resp = DeviceiotcenterApi.DeviceIotCenter_OtaUpgradeBasePostApi(device_id=device_id, cmd=cmd)
        assert resp.status_code == 200
        cmd = "rm abc111.txt"
        resp = DeviceiotcenterApi.DeviceIotCenter_OtaUpgradeBasePostApi(device_id=device_id, cmd=cmd)
        assert resp.status_code == 200

    #nopass bug
    def test_api_DeviceIotCenter_PushRtcLive(self, config_obj, DeviceiotcenterApi):
        """  摄像头Rtc推流
route: prefix=, internal_prefix=device, a... """
        device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        resp = DeviceiotcenterApi.DeviceIotCenter_PushRtcLivePostApi(device_id=device_id, ingress_id=None)
        assert resp.status_code == 200

    def test_api_DeviceIotCenter_PushRTMPLive(self, config_obj, DeviceiotcenterApi):
        """  摄像头Rtpm推流
route: prefix=, internal_prefix=device, ... """
        device_id = "a114be1412fe4e9cb60b4232dc3effd8"
        url = "rtmp://nlb-dcc-1-eg-cn-shanghai-1.test.sensebelt.net:31935/live/00002010?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbmdyZXNzX2lkIjoiMjg4YzI5ZTQtOWU0Mi00ZjkwLWI5M2YtYjE2ZDk1NWRmYzM1LTAwMDAyMDEwIiwiZXhwIjo5MjIzMzcyMDM2fQ.M73KAXiSZY_kmzM5BPQbGHSI7Ig0EQE_T2s7puRPtO8"
        resp = DeviceiotcenterApi.DeviceIotCenter_PushRTMPLivePostApi(device_id=device_id, url=url)
        assert resp.status_code == 200

    #pass
    def test_api_DeviceIotCenter_SetIpcConfig(self, config_obj, DeviceiotcenterApi):
        """  ipc配置下发
route: prefix=, internal_prefix=device, ac... """
        device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        config = "this is test config"
        resp = DeviceiotcenterApi.DeviceIotCenter_SetIpcConfigPostApi(device_id=device_id, config=config)
        assert resp.status_code == 200

    #nopass
    def test_api_DeviceIotCenter_StartCameraPTZ(self, config_obj, DeviceiotcenterApi):
        """  摄像头开始PTZ
route: prefix=, internal_prefix=device, a... """
        device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        id = sign_utils.getUuid()
        PTZ =  {
            "Pan": "1",
            "Tilt": "1",
            "Zoom": "0"
          }
        resp = DeviceiotcenterApi.DeviceIotCenter_StartCameraPTZPostApi(device_id=device_id, id=id, PTZ=PTZ)
        assert resp.status_code == 200

#     def test_api_DeviceIotCenter_StartRtcAudio(self, config_obj, DeviceiotcenterApi):
#         """  摄像头启动Rtc音频
# route: prefix=, internal_prefix=device,... """
#         device_id = None
#         url = None
#         resp = DeviceiotcenterApi.DeviceIotCenter_StartRtcAudioPostApi(device_id=device_id, url=url)
#         assert resp.status_code == 200

    #pass
    def test_api_DeviceIotCenter_StopCameraPTZ(self, config_obj, DeviceiotcenterApi):
        """  摄像头停止PTZ
route: prefix=, internal_prefix=device, a... """
        device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        id = sign_utils.getUuid()
        resp = DeviceiotcenterApi.DeviceIotCenter_StopCameraPTZPostApi(device_id=device_id, id=id)
        assert resp.status_code == 200

#     def test_api_DeviceIotCenter_StopRtcAudio(self, config_obj, DeviceiotcenterApi):
#         """  摄像头停止Rtc音频
# route: prefix=, internal_prefix=device,... """
#         device_id = None
#         resp = DeviceiotcenterApi.DeviceIotCenter_StopRtcAudioPostApi(device_id=device_id)
#         assert resp.status_code == 200

    #pass
    def test_api_DeviceIotCenter_StopRtcLive(self, config_obj, DeviceiotcenterApi,camera_info):
        """  摄像头停止Rtc推流
route: prefix=, internal_prefix=device,... """
        device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        resp = DeviceiotcenterApi.DeviceIotCenter_StopRtcLivePostApi(device_id=device_id)
        assert resp.status_code == 200

    def test_api_DeviceIotCenter_StopRTMPLive(self, config_obj, DeviceiotcenterApi):
        """  摄像头停止Rtmp推流
route: prefix=, internal_prefix=device... """
        device_id = None
        resp = DeviceiotcenterApi.DeviceIotCenter_StopRTMPLivePostApi(device_id=device_id)
        assert resp.status_code == 200
