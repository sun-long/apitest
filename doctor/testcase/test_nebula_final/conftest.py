#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys

import pytest

from commonlib import sign_utils
from commonlib.cache_dict import CacheDict
from commonlib.log_utils import log
from defines.nebula_final.cloud_service_business import CloudSwaggerBusiness
from defines.nebula_final.edge_service_business import EdgeSwaggerBusiness


@pytest.fixture(scope='function')
def CloudApi(config_obj, ext_info):
    """ CloudApi API """
    host = config_obj.EnvInfo.NebulaCloud.Service
    return CloudSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info)


@pytest.fixture(scope='function')
def EdgeApi(config_obj, ext_info, client_info):
    """ EdgeApi API """
    host = config_obj.EnvInfo.NebulaEdge.Service % client_info.ip
    return EdgeSwaggerBusiness(host, config_obj=config_obj,  ext_info=ext_info)


@pytest.fixture(scope='function')
def client_info(config_obj, request):
    """ yaml中client信息"""
    return config_obj.get(request.param)


@pytest.fixture(scope='function')
def camera_info(config_obj, request):
    """ yaml中摄像机信息"""
    return config_obj.get(request.param)

# learn_1 fixture使用
@pytest.fixture(scope='function', autouse=True)
def loginToken(config_obj, EdgeApi):
    EdgeApi.freshToken()


# 类级别缓存对象
@pytest.fixture(scope="class")
def cache_obj():
    obj = CacheDict()
    yield obj
    obj.clear_func_all()

# learn_4 测试准备数据
@pytest.fixture(scope='function')
def cameraNewId(config_obj, EdgeApi, client_info, camera_info, cache_obj):
    """ 创建子设备, 返回子设备ID"""
    key = '%s_%s_%s' % (sys._getframe().f_code.co_name, client_info['key'], camera_info['key'])

    def cache_func():
        device_id = sign_utils.getUuid(32)
        subdevice = {
            "brand": camera_info.brand,
            "device_config": {
                "ip": {
                    "ips": [
                        {
                            "address": camera_info.ip
                        }
                    ]
                }
            },
            "device_id": device_id,  # 存在=>更新, 不存在=>创建
            "extra_config": {
                "camera_config": {
                    "auth": {
                        "username": camera_info.username,
                        "password": camera_info.password,
                    },
                    "manage_port": camera_info.port,
                    "video_source_config": {
                        "rtsp_parameter": {
                            "parameter": {
                                "url": camera_info.rtsp
                            }
                        }
                    },
                }
            },
            "name": device_id,
            "device_kind": camera_info.kind
        }
        resp = EdgeApi.NebulaIOTAgentSrv_UpsertSubDevicePostApi(subdevice=subdevice, skip=None)
        if resp.status_code != 200:
            raise Exception("fixture:cameraId创建子设备失败.")

        def clear_func():
            EdgeApi.NebulaIOTAgentSrv_RemoveSubDeviceByIDDeleteApi(device_id)

        return device_id, clear_func

    yield cache_obj.get_value(key, func=cache_func)


# learn_4 测试准备数据
@pytest.fixture(scope='function')
def cameraNewGroupIds(config_obj, EdgeApi, client_info, camera_info, cache_obj):
    """ 创建一组子设备, 返回子设备ID"""
    key = '%s_%s_%s' % (sys._getframe().f_code.co_name, client_info['key'], camera_info['key'])

    def cache_func():
        device_num = 3
        device_ids = []
        for idx in range(device_num):
            device_id = sign_utils.getUuid(32)
            subdevice = {
                "brand": camera_info.brand,
                "device_config": {
                    "ip": {
                        "ips": [
                            {
                                "address": camera_info.ip
                            }
                        ]
                    }
                },
                "device_id": device_id,  # 存在=>更新, 不存在=>创建
                "extra_config": {
                    "camera_config": {
                        "auth": {
                            "username": camera_info.username,
                            "password": camera_info.password,
                        },
                        "manage_port": camera_info.port,
                        "video_source_config": {
                            "rtsp_parameter": {
                                "parameter": {
                                    "url": camera_info.rtsp
                                }
                            }
                        },
                    }
                },
                "name": device_id,
                "device_kind": camera_info.kind
            }
            resp = EdgeApi.NebulaIOTAgentSrv_UpsertSubDevicePostApi(subdevice=subdevice, skip=None)
            if resp.status_code != 200:
                raise Exception("fixture:cameraId_%s创建子设备失败." % idx)

        def clear_func():
            for device_id in device_ids:
                EdgeApi.NebulaIOTAgentSrv_RemoveSubDeviceByIDDeleteApi(device_id)

        return device_ids, clear_func
    yield cache_obj.get_value(key, func=cache_func)


@pytest.fixture(scope='function')
def deviceInfo(config_obj, EdgeApi, CloudApi, client_info, cache_obj):
    """ 根据client查询device信息"""
    key = '%s_%s' % (sys._getframe().f_code.co_name, client_info['key'])

    def cache_func():
        resp = EdgeApi.NebulaIOTAgentSrv_GetSerialNumberGetApi()
        serial_number = resp.json_get("serial_number")

        resp = EdgeApi.NebulaIOTAgentSrv_GetLicenseStateGetApi()
        nebula_registry = resp.json_get("license.nebula_registry")

        resp = CloudApi.NebulaIOTSrv_GetDeviceBySNGetApi(nebula_registry, serial_number)
        device_id = resp.json_get("device.device.metadata.device_id")

        log().info("ak:%s" % nebula_registry)
        log().info("sn:%s" % serial_number)
        log().info("device_id:%s" % device_id)
        res = {"ak": nebula_registry, "sn": serial_number, "device_id": device_id}
        return res, None

    yield cache_obj.get_value(key, func=cache_func)

@pytest.fixture(scope='function')
def edgeLogin(EdgeApi, request):
    """ 边登录 """
    user = request.param['user_name']
    pwd = request.param['password']
    yield EdgeApi.getToken(user_name=user, password=pwd)
    # logout


@pytest.fixture(scope='function')
def logName(request):
    """ 测试用, 无实际用途 """
    yield "logName:%s" % request.param
