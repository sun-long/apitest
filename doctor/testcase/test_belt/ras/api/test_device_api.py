#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


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

    def test_api_DeviceManagerCenter_BatchCreateDevice(self, config_obj, DeviceApi, camera_info, cluster_info):
        """  批量创建Device """
        request_header = None
        devices = []
        devicekind_id = "c78a66b8734a4c3b92e4c62ee43595b2"
        for x in range(2):
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
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_GetAccountId(self, config_obj, DeviceApi):
        """  根据请求自带的Context获取account_id,
route: prefix=, intern... """
        resp = DeviceApi.DeviceManagerCenter_GetAccountIdGetApi()
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_GetIotIngresses(self, config_obj, DeviceApi):
        """  获取Iot接入配置
route: prefix=, internal_prefix=device, ... """
        resp = DeviceApi.DeviceManagerCenter_GetIotIngressesGetApi()
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_SDPPublish(self, config_obj, DeviceApi):
        """  生成SDP服务端描述信息, 生成的SDP描述信息过期时间为30秒, 超时后需要重新生成.
rout... """
        device_id = None
        ingress_id = None
        sdp = None
        type = None
        resp = DeviceApi.DeviceManagerCenter_SDPPublishPostApi(device_id=device_id, ingress_id=ingress_id, sdp=sdp,
                                                               type=type)
        assert resp.status_code == 200



    def test_api_DeviceManagerCenter_BatchCreateDeviceByKindName(self, config_obj, DeviceApi):
        """  批量创建Device, devicekind仅提供devicekind_name, 上限50
rou... """
        request_header = None
        devices = None
        resp = DeviceApi.DeviceManagerCenter_BatchCreateDeviceByKindNamePostApi(request_header=request_header, devices=devices)
        assert resp.status_code == 200

    # TODO action可能错误，等待成修更新接口文档
    def test_api_DeviceManagerCenter_BindDevicePolicyGroup(self, config_obj, DeviceApi):
        """  添加设备和policy group的绑定 """
        request_header = None
        device_id = "9faac3f76d5d42c1903e4630dba683fe"
        group_id = "1"
        resp = DeviceApi.DeviceManagerCenter_BindDevicePolicyGroupPostApi(request_header=request_header, device_id=device_id, group_id=group_id)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_CreateDevice(self, config_obj, deviceKindAide, DeviceApi, camera_info,
                                                  cluster_info):
        """  创建Device, 设备鉴权信息创建时不用指定，会在创建设备时自动创建鉴权信息并返回，不能修改 """
        request_header = None
        # devicekind_id = "70e97d3b1ac542c3b9ccc10d444d4ef0"
        devicekind_id = deviceKindAide.id
        # devicekind_id = "a4b2a709bb544c74b85580503a480145"
        name = "device_%s" % sign_utils.getUuid(5)
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
        resp = DeviceApi.DeviceManagerCenter_CreateDevicePostApi(request_header=request_header,
                                                                 devicekind_id=devicekind_id, name=name, desc=desc,
                                                                 cluster=cluster, extra_info=extra_info, driver=driver)
        assert resp.status_code == 200
        log().info("deviceID:%s" % resp.json_get("device.id"))

    def test_api_DeviceManagerCenter_CreateDeviceByKindName(self, config_obj, DeviceApi):
        """  创建Device, 设备鉴权信息创建时不用指定，会在创建设备时自动创建鉴权信息并返回，并且之后不能修... """
        request_header = None
        devicekind_name = None
        name = None
        desc = None
        cluster = None
        extra_info = None
        driver = None
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(request_header=request_header,
                                                                           devicekind_name=devicekind_name, name=name,
                                                                           desc=desc, cluster=cluster,
                                                                           extra_info=extra_info, driver=driver)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_CreateDeviceKind(self, config_obj, DeviceApi):
        """  创建Devicekind """
        name = "test3"
        desc = "测试用，支持rtsp"
        verify_method = "USER"
        # ingress_types = ["RTSP"]
        # ingress_types = ["RTMP"]
        ingress_types = ["RTSP"]
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceKindPostApi(name=name, desc=desc, verify_method=verify_method,
                                                                     ingress_types=ingress_types)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_DeleteDevice(self, config_obj, DeviceApi):
        """  删除Device """
        request_header = None
        id = "9faac3f76d5d42c1903e4630dba683fe"
        resp = DeviceApi.DeviceManagerCenter_DeleteDevicePostApi(request_header=request_header, id=id)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_DeleteDeviceKind(self, config_obj, DeviceApi):
        """  删除Devicekind, device_kind下有device时，禁止删除 """
        id = "e0ac2e20c2684de2b42961af602bf345"
        resp = DeviceApi.DeviceManagerCenter_DeleteDeviceKindPostApi(id=id)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_GenRTMPAddress(self, config_obj, DeviceApi):
        """  生成RTMP推流地址, 生成的地址过期时间为1小时, 超时后需要重新生成.
route: pref... """
        device_id = None
        ingress_id = None
        duration = None
        resp = DeviceApi.DeviceManagerCenter_GenRTMPAddressPostApi(device_id=device_id, ingress_id=ingress_id, duration=duration)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_GetAllDevices(self, config_obj, DeviceApi):
        """  获取所有account_id下的Device列表及总数，支持按device id, name批量分页... """
        ids = None
        names = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = DeviceApi.DeviceManagerCenter_GetAllDevicesGetApi(ids=ids, names=names, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_GetDevice(self, config_obj, DeviceApi):
        """  根据device_id获取Device """
        id = '939e8fff127146a1b73876dcc4a24bfe'
        resp = DeviceApi.DeviceManagerCenter_GetDeviceGetApi(id=id)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_GetDeviceKind(self, config_obj, DeviceApi):
        """  根据device_kind_id获取DeviceKind """
        id = "c78a66b8734a4c3b92e4c62ee43595b2"
        resp = DeviceApi.DeviceManagerCenter_GetDeviceKindGetApi(id=id)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_GetDeviceKinds(self, config_obj, DeviceApi):
        """  获取Devicekind列表 """
        ids = [
            # "70e97d3b1ac542c3b9ccc10d444d4ef0",
        ]
        paging_offset = None
        paging_limit = 100
        paging_total = None
        resp = DeviceApi.DeviceManagerCenter_GetDeviceKindsGetApi(ids=ids, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_GetDevices(self, config_obj, DeviceApi):
        """  获取Device列表及总数，支持分页查询 """
        ids = None
        names = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = DeviceApi.DeviceManagerCenter_GetDevicesGetApi(ids=ids, names=names, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_DeleteAllDevices(self, config_obj, DeviceApi):
        """  获取Device列表及总数，支持分页查询 """
        ids = None
        names = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = DeviceApi.DeviceManagerCenter_GetDevicesGetApi(ids=ids, names=names, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200
        i = 1
        for device in resp.json_get("devices"):
            request_header = None
            id = device["id"]
            if id in ["243e775e8d4e4ad4a4af7fb90c38238a"]:
                continue
            resp = DeviceApi.DeviceManagerCenter_DeleteDevicePostApi(request_header=request_header, id=id)
            assert resp.status_code == 200

    @pytest.mark.skip("内部接口")
    def test_api_DeviceManagerCenter_Register(self, config_obj, DeviceApi):
        """  [internal] 边缘向中心注册接口 """
        info = None
        resp = DeviceApi.DeviceManagerCenter_RegisterPostApi(info=info)
        assert resp.status_code == 200

    @pytest.mark.skip("内部接口")
    def test_api_DeviceManagerCenter_ListRegistration(self, config_obj, DeviceApi):
        """  [internal] 获取边缘注册信息 """
        resp = DeviceApi.DeviceManagerCenter_ListRegistrationGetApi()
        assert resp.status_code == 200

    # TODO action可能错误，等待成修更新接口文档
    def test_api_DeviceManagerCenter_UnbindDevicePolicyGroup(self, config_obj, DeviceApi):
        """  解绑设备和policy group的绑定 """
        request_header = None
        device_id = "e074d4726c38468ea186760546b614fe"
        group_id = "1"
        resp = DeviceApi.DeviceManagerCenter_UnbindDevicePolicyGroupPostApi(request_header=request_header, device_id=device_id, group_id=group_id)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_UpdateDevice(self, config_obj, DeviceApi,camera_info, cluster_info):
        """  更新Device，鉴权信息不可修改 """
        request_header = None
        id = "ad095130d79b438b862bd1733c65102d"
        name = "deviceUpdate_%s" % sign_utils.getUuid(5)
        desc = "testUpdate"
        cluster = {"id": cluster_info["id"]}
        extra_info = None
        driver = {
            "driver_id": "778af8ab-7b2c-4e54-96a8-c3c298aee0ec", # TODO 必须嘛？不填报错
            "enable": True,
            "ingresses": [
                {
                    "information": {
                        "rtsp": {
                            "source_url": 'rtsp://admin:SenseNebula2021@10.151.116.116:554'
                        },
                        "type": camera_info["type"]
                    },
                    "name": name,
                    "description": "xxxxxx",
                    "ingress_id": "388ab744-d17c-42c7-90c8-0d3fa686144c-00001001", # TODO 必须嘛？不填报错
                }
            ],
        }
        resp = DeviceApi.DeviceManagerCenter_UpdateDevicePostApi(request_header=request_header, id=id, name=name, desc=desc, extra_info=extra_info, driver=driver)
        assert resp.status_code == 200

    def test_api_DeviceManagerCenter_UpdateDeviceKind(self, config_obj, DeviceApi):
        """  更新Devicekind, device_kind下有device时，禁止更新 """
        id = "c78a66b8734a4c3b92e4c62ee43595b2"
        name = "new_kind1"
        desc = "new_desc"
        verify_method = "USER"
        ingress_types = ["RTSP"]
        resp = DeviceApi.DeviceManagerCenter_UpdateDeviceKindPostApi(id=id, name=name, desc=desc, verify_method=verify_method, ingress_types=ingress_types)
        assert resp.status_code == 200
