#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.skip(msg="内部接口，不对外")
class TestDeviceParam(object):
    """ device Param测试"""

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
        ('request_header', 'invalidrequest_header'),
        ('request_header', ''),
        ('request_header', None),
        ('devices', 'invaliddevices'),
        ('devices', ''),
        ('devices', None),
    ])
    def test_api_DeviceManagerCenter_BatchCreateDeviceInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  批量创建Device, devicekind仅提供devicekind_id, 上限50
route... """
        request_header = None
        devices = None
        intef = DeviceApi.DeviceManagerCenter_BatchCreateDevicePostApi(request_header=request_header, devices=devices, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('request_header', 'invalidrequest_header'),
        ('request_header', ''),
        ('request_header', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
    ])
    def test_api_DeviceManagerCenter_BindDevicePolicyGroupInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  添加设备和policy group的绑定 """
        request_header = None
        device_id = None
        group_id = None
        intef = DeviceApi.DeviceManagerCenter_BindDevicePolicyGroupPostApi(request_header=request_header, device_id=device_id, group_id=group_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('request_header', 'invalidrequest_header'),
        ('request_header', ''),
        ('request_header', None),
        ('devicekind_id', 'invaliddevicekind_id'),
        ('devicekind_id', ''),
        ('devicekind_id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('desc', 'invaliddesc'),
        ('desc', ''),
        ('desc', None),
        ('cluster', 'invalidcluster'),
        ('cluster', ''),
        ('cluster', None),
        ('extra_info', 'invalidextra_info'),
        ('extra_info', ''),
        ('extra_info', None),
        ('driver', 'invaliddriver'),
        ('driver', ''),
        ('driver', None),
    ])
    def test_api_DeviceManagerCenter_CreateDeviceInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  创建Device, 设备鉴权信息创建时不用指定，会在创建设备时自动创建鉴权信息并返回，不能修改 """
        request_header = None
        devicekind_id = None
        name = None
        desc = None
        cluster = None
        extra_info = None
        driver = None
        intef = DeviceApi.DeviceManagerCenter_CreateDevicePostApi(request_header=request_header, devicekind_id=devicekind_id, name=name, desc=desc, cluster=cluster, extra_info=extra_info, driver=driver, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('desc', 'invaliddesc'),
        ('desc', ''),
        ('desc', None),
        ('verify_method', 'invalidverify_method'),
        ('verify_method', ''),
        ('verify_method', None),
        ('ingress_types', 'invalidingress_types'),
        ('ingress_types', ''),
        ('ingress_types', None),
    ])
    def test_api_DeviceManagerCenter_CreateDeviceKindInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  创建Devicekind """
        name = None
        desc = None
        verify_method = None
        ingress_types = None
        intef = DeviceApi.DeviceManagerCenter_CreateDeviceKindPostApi(name=name, desc=desc, verify_method=verify_method, ingress_types=ingress_types, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('request_header', 'invalidrequest_header'),
        ('request_header', ''),
        ('request_header', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_DeviceManagerCenter_DeleteDeviceInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  删除Device """
        request_header = None
        id = None
        intef = DeviceApi.DeviceManagerCenter_DeleteDevicePostApi(request_header=request_header, id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_DeviceManagerCenter_DeleteDeviceKindInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  删除Devicekind, device_kind下有device时，禁止删除 """
        id = None
        intef = DeviceApi.DeviceManagerCenter_DeleteDeviceKindPostApi(id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_DeviceManagerCenter_GetAccountIdInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  根据请求自带的Context获取account_id,
route: prefix=, intern... """
        intef = DeviceApi.DeviceManagerCenter_GetAccountIdGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_DeviceManagerCenter_GetDeviceInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  根据device_id获取Device """
        id = None
        intef = DeviceApi.DeviceManagerCenter_GetDeviceGetApi(id=id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_DeviceManagerCenter_GetDeviceKindInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  根据device_kind_id获取DeviceKind """
        id = None
        intef = DeviceApi.DeviceManagerCenter_GetDeviceKindGetApi(id=id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ids', 'invalidids'),
        ('ids', ''),
        ('ids', None),
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
    def test_api_DeviceManagerCenter_GetDeviceKindsInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  获取Devicekind列表 """
        ids = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = DeviceApi.DeviceManagerCenter_GetDeviceKindsGetApi(ids=ids, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ids', 'invalidids'),
        ('ids', ''),
        ('ids', None),
        ('names', 'invalidnames'),
        ('names', ''),
        ('names', None),
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
    def test_api_DeviceManagerCenter_GetDevicesInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  获取Device列表及总数，支持分页查询 """
        ids = None
        names = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = DeviceApi.DeviceManagerCenter_GetDevicesGetApi(ids=ids, names=names, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_DeviceManagerCenter_GetIotIngressesInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  获取Iot接入配置
route: prefix=, internal_prefix=device, ... """
        intef = DeviceApi.DeviceManagerCenter_GetIotIngressesGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('info', 'invalidinfo'),
        ('info', ''),
        ('info', None),
    ])
    def test_api_DeviceManagerCenter_RegisterInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  [internal] 边缘向中心注册接口 """
        info = None
        intef = DeviceApi.DeviceManagerCenter_RegisterPostApi(info=info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_DeviceManagerCenter_ListRegistrationInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  [internal] 获取边缘注册信息 """
        intef = DeviceApi.DeviceManagerCenter_ListRegistrationGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

        @pytest.mark.parametrize("invalidParam", [
            ('device_id', 'invaliddevice_id'),
            ('device_id', ''),
            ('device_id', None),
            ('ingress_id', 'invalidingress_id'),
            ('ingress_id', ''),
            ('ingress_id', None),
            ('sdp', 'invalidsdp'),
            ('sdp', ''),
            ('sdp', None),
            ('type', 'invalidtype'),
            ('type', ''),
            ('type', None),
        ])
        def test_api_DeviceManagerCenter_SDPPublishInvalidParam(self, invalidParam, config_obj, DeviceApi):
            """  生成SDP服务端描述信息, 生成的SDP描述信息过期时间为30秒, 超时后需要重新生成.
    rout... """
            device_id = None
            ingress_id = None
            sdp = None
            type = None
            intef = DeviceApi.DeviceManagerCenter_SDPPublishPostApi(device_id=device_id, ingress_id=ingress_id, sdp=sdp,
                                                                    type=type, sendRequest=False)
            intef.update_body(invalidParam[0], invalidParam[1])
            resp = intef.request()
            assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('request_header', 'invalidrequest_header'),
        ('request_header', ''),
        ('request_header', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
    ])
    def test_api_DeviceManagerCenter_UnbindDevicePolicyGroupInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  解绑设备和policy group的绑定 """
        request_header = None
        device_id = None
        group_id = None
        intef = DeviceApi.DeviceManagerCenter_UnbindDevicePolicyGroupPostApi(request_header=request_header, device_id=device_id, group_id=group_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('request_header', 'invalidrequest_header'),
        ('request_header', ''),
        ('request_header', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('desc', 'invaliddesc'),
        ('desc', ''),
        ('desc', None),
        ('extra_info', 'invalidextra_info'),
        ('extra_info', ''),
        ('extra_info', None),
        ('driver', 'invaliddriver'),
        ('driver', ''),
        ('driver', None),
    ])
    def test_api_DeviceManagerCenter_UpdateDeviceInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  更新Device，鉴权信息不可修改 """
        request_header = None
        id = None
        name = None
        desc = None
        extra_info = None
        driver = None
        intef = DeviceApi.DeviceManagerCenter_UpdateDevicePostApi(request_header=request_header, id=id, name=name, desc=desc, extra_info=extra_info, driver=driver, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('desc', 'invaliddesc'),
        ('desc', ''),
        ('desc', None),
        ('verify_method', 'invalidverify_method'),
        ('verify_method', ''),
        ('verify_method', None),
        ('ingress_types', 'invalidingress_types'),
        ('ingress_types', ''),
        ('ingress_types', None),
    ])
    def test_api_DeviceManagerCenter_UpdateDeviceKindInvalidParam(self, invalidParam, config_obj, DeviceApi):
        """  更新Devicekind, device_kind下有device时，禁止更新 """
        id = None
        name = None
        desc = None
        verify_method = None
        ingress_types = None
        intef = DeviceApi.DeviceManagerCenter_UpdateDeviceKindPostApi(id=id, name=name, desc=desc, verify_method=verify_method, ingress_types=ingress_types, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
