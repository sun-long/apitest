#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestDeviceiotcenterParam(object):
    """ deviceIotCenter Param测试"""

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

    # pass 5.5
    @pytest.mark.parametrize("invalidParam", [
        ('cmd', 'invalidcmd', "sh: 1: invalidcmd: not found\n"),
        ('cmd', '', "invalid OtaUpgradeBaseReq.Cmd: value length must be at least 1 runes"),
        ('cmd', None, "invalid OtaUpgradeBaseReq.Cmd: value length must be at least 1 runes"),
    ])
    def test_api_DeviceIotCenter_OtaUpgradeBaseInvalidParam(self, invalidParam, config_obj, DeviceiotcenterApi):
        """  ota基础升级
route: prefix=, internal_prefix=device, ac... """
        device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        cmd = None
        intef = DeviceiotcenterApi.DeviceIotCenter_OtaUpgradeBasePostApi(device_id=device_id, cmd=cmd,
                                                                         sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == invalidParam[2]

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('ingress_id', 'invalidingress_id'),
        ('ingress_id', ''),
        ('ingress_id', None),
    ])
    def test_api_DeviceIotCenter_PushRtcLiveInvalidParam(self, invalidParam, config_obj, DeviceiotcenterApi):
        """  摄像头Rtc推流
route: prefix=, internal_prefix=device, a... """
        device_id = None
        ingress_id = None
        intef = DeviceiotcenterApi.DeviceIotCenter_PushRtcLivePostApi(device_id=device_id, ingress_id=ingress_id,
                                                                      sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('url', 'invalidurl'),
        ('url', ''),
        ('url', None),
    ])
    def test_api_DeviceIotCenter_PushRTMPLiveInvalidParam(self, invalidParam, config_obj, DeviceiotcenterApi):
        """  摄像头Rtpm推流
route: prefix=, internal_prefix=device, ... """
        device_id = None
        url = None
        intef = DeviceiotcenterApi.DeviceIotCenter_PushRTMPLivePostApi(device_id=device_id, url=url, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    # pass 5.5
    @pytest.mark.parametrize("invalidParam", [
        ('config', None, "device iot argument invalid"),
        ('config', 123, "proto: (line 1:61): invalid value for string type: 123"),
        ('config', [], "proto: (line 1:61): invalid value for string type: ["),
    ])
    def test_api_DeviceIotCenter_SetIpcConfigInvalidParam(self, invalidParam, config_obj, DeviceiotcenterApi):
        """  ipc配置下发
route: prefix=, internal_prefix=device, ac... """
        device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        config = None
        intef = DeviceiotcenterApi.DeviceIotCenter_SetIpcConfigPostApi(device_id=device_id, config=config,
                                                                       sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.json_get("error.message") == invalidParam[2]

    # PASS 5.5
    @pytest.mark.parametrize("invalidParam", [
        ('PTZ', {"Pan": "2", "Tilt": "1", "Zoom": "1"}, "Pan should be in [-1, 1]"),
        ('PTZ', {"Pan": "1", "Tilt": "2", "Zoom": "1"}, "Tilt should be in [-1, 1]"),
        ('PTZ', {"Pan": "1", "Tilt": "1", "Zoom": "2"}, "Zoom should be in [0, 1]"),
    ])
    def test_api_DeviceIotCenter_StartCameraPTZInvalidParam(self, invalidParam, config_obj, DeviceiotcenterApi):
        """  摄像头开始PTZ
route: prefix=, internal_prefix=device, a... """
        device_id = config_obj.Clients.SubDevice.IotRtmp.device_id
        id = None
        PTZ = None
        intef = DeviceiotcenterApi.DeviceIotCenter_StartCameraPTZPostApi(device_id=device_id, id=id, PTZ=PTZ,
                                                                         sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == invalidParam[2]

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('url', 'invalidurl'),
        ('url', ''),
        ('url', None),
    ])
    def test_api_DeviceIotCenter_StartRtcAudioInvalidParam(self, invalidParam, config_obj, DeviceiotcenterApi):
        """  摄像头启动Rtc音频
route: prefix=, internal_prefix=device,... """
        device_id = None
        url = None
        intef = DeviceiotcenterApi.DeviceIotCenter_StartRtcAudioPostApi(device_id=device_id, url=url, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_DeviceIotCenter_StopCameraPTZInvalidParam(self, invalidParam, config_obj, DeviceiotcenterApi):
        """  摄像头停止PTZ
route: prefix=, internal_prefix=device, a... """
        device_id = None
        id = None
        intef = DeviceiotcenterApi.DeviceIotCenter_StopCameraPTZPostApi(device_id=device_id, id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
    ])
    def test_api_DeviceIotCenter_StopRtcAudioInvalidParam(self, invalidParam, config_obj, DeviceiotcenterApi):
        """  摄像头停止Rtc音频
route: prefix=, internal_prefix=device,... """
        device_id = None
        intef = DeviceiotcenterApi.DeviceIotCenter_StopRtcAudioPostApi(device_id=device_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
    ])
    def test_api_DeviceIotCenter_StopRtcLiveInvalidParam(self, invalidParam, config_obj, DeviceiotcenterApi):
        """  摄像头停止Rtc推流
route: prefix=, internal_prefix=device,... """
        device_id = None
        intef = DeviceiotcenterApi.DeviceIotCenter_StopRtcLivePostApi(device_id=device_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
    ])
    def test_api_DeviceIotCenter_StopRTMPLiveInvalidParam(self, invalidParam, config_obj, DeviceiotcenterApi):
        """  摄像头停止Rtmp推流
route: prefix=, internal_prefix=device... """
        device_id = None
        intef = DeviceiotcenterApi.DeviceIotCenter_StopRTMPLivePostApi(device_id=device_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
