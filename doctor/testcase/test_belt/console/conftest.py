#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   conftest.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/10 下午2:58   wangan      1.0         None
'''
import sys

import pytest
from commonlib.log_utils import log


@pytest.fixture(scope='function')
def MsgType1(config_obj):
    return config_obj.Console.type1.name

@pytest.fixture(scope='function')
def MsgType2(config_obj):
    return config_obj.Console.type2.name

@pytest.fixture(scope='function')
def MsgTemplate1(config_obj):
    return config_obj.Console.template1.name

@pytest.fixture(scope='function')
def MsgTemplate2(config_obj):
    return config_obj.Console.template2.name

@pytest.fixture(scope='function')
def MsgTemplateConent1(config_obj):
    return config_obj.Console.tempContent1.name

@pytest.fixture(scope='function')
def MsgConent1(config_obj):
    return config_obj.Console.msgContent1.name

@pytest.fixture(scope="class")
def demoClass():
    # setup
    log().info("class setup......")
    yield
    log().info("class teardown......")
    # teardown


@pytest.fixture(scope="function")
def demoFunction():
    # setup
    log().info("function setup......")
    yield
    log().info("function teardown......")
    # teardown
    
@pytest.fixture(scope='class', autouse=False)
def MsgClear(config_obj, NotificationApi, NotificationinternalApi, MsgType1, MsgTemplate1):
    NotificationApi.prepareNotification(MsgType1)
    NotificationinternalApi.prepareInternalNotification(MsgType1, MsgTemplate1)

# learn_4 测试准备数据
@pytest.fixture(scope='function')
def msgTypeId1(config_obj, cache_obj, MsgType1, NotificationinternalApi):
    """ 创建msgType,获取ID"""
    key = '%s_%s' % (sys._getframe().f_code.co_name, MsgType1)

    def cache_func():
        NotificationinternalApi.perpareInternalNotification(MsgType1, MsgTemplate1)
        resp = NotificationinternalApi.ConsoleNotificationInternalService_CreateMsgTypePostApi(name=MsgType1)
        type_id = resp.json_get("msg_type_info.msg_type_id")

        def clear_func():
            NotificationinternalApi.ConsoleNotificationInternalService_DeleteMsgTypeDeleteApi(type_id)
        return type_id, clear_func

    yield cache_obj.get_value(key, func=cache_func)

