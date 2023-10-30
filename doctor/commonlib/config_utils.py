#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   conftest_utils.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/11/17 下午3:02   wangan      1.0         configObj for pytest
'''
import pytest

from commonlib import cmd_utils
from commonlib.log_utils import log

# 子设备支持列表
SUBDEVICE_SUPPORT_TYPE = {
    'NVR': {
        'productType': 'NVR',
        'typeName': 'NVR',
        'aiotKind': 'NVR',
    },
    'Camera': {
        'productType': 'Camera',
        'typeName': 'Camera',
        'aiotKind': 'CAMERA',
    },
    'Snap': {
        'productType': 'Camera',
        'typeName': 'Snap',  # 细分类型,　比如摄像头包含摄像头Camera和抓拍机Snap,给测试人员看的
        'aiotKind': 'CAMERA',  # 接口需要传递的类型 ,给接口看的
    }
}


def configObj_Clients_Aiot(configObjKey, config_obj):
    """ 读取端信息"""
    if configObjKey in config_obj.Clients.Aiot:
        client_info = config_obj["Clients"]["Aiot"][configObjKey]
        if not cmd_utils.ping_ip(client_info['ip']):
            log().warning('Client=%s Ip:%s, ping不通' % (configObjKey, client_info['ip']))
        log().info("Test Client Info: %s" % client_info)
        client_info["name"] = configObjKey
        return client_info
    else:
        pytest.skip(msg='config文件中未配置该Client=%s, 跳过执行这条case' % configObjKey)


def configObj_Clients_SubDevice(configObjKey, config_obj):
    """　读取子设备信息"""
    if configObjKey in config_obj.Clients.SubDevice:
        subDevice = config_obj["Clients"]["SubDevice"][configObjKey]
        if not cmd_utils.ping_ip(subDevice['ip']):
            log().warning('SubDevice=%s Ip:%s, ping不通' % (configObjKey, subDevice['ip']))
        log().info("subDevice_info: %s" % subDevice)
        for key, value in SUBDEVICE_SUPPORT_TYPE.items():
            if configObjKey.startswith(key):
                subDevice['productType'] = value['productType']
                subDevice['aiotKind'] = value['aiotKind']
                subDevice['name'] = value['configObjKey']
                break
        else:
            pytest.skip(msg='不支持的子设备类型,请修改toml文件中的Clients.SubDevice.xxx.目前支持类型如下：' % SUBDEVICE_SUPPORT_TYPE)
        return subDevice
    else:
        pytest.skip(msg='config文件中未配置该SubDevice=%s, 跳过执行这条case' % configObjKey)


def configInfoByKey(config_obj, key):
    """ configObj中获取key对应的信息"""
    info = config_obj.get(key)
    log().info("[Config]%s Info: %s" % (key, info))
    info["key"] = key  # 添加键名
    return info
