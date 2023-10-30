#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest


sys.path.append('..')

from commonlib.subjectlib.devicemanager import devicemanager_service
from commonlib.log_utils import log

notExistDeviceID = "9999"
notExistAK = "thisisnotexistAK"


class TestDeviceManager(object):
    @pytest.fixture(scope="class", autouse=True)
    def init_func(self, env_obj):
        # 所有test运行前运行一次，接收外部参数env_obj，初始化测试环境
        log().info("==========%s测试开始，测试环境%s==========" % (self.__class__.__name__, env_obj.host))
        global env_config, deviceManager_obj, test_data  # 全局变量
        env_config = env_obj
        deviceManager_obj = devicemanager_service.DeviceManagerService(env_config)
        # 测试数据
        test_data = {
            "AK": env_config.ak,
            "deviceID": "2000"
        }
        deviceManager_obj.add_variable_batch(test_data)

    def teardown_class(self):
        # 所有test运行完后运行一次
        log().info("==========%s测试结束==========\n" % self.__name__)

    def setup_method(self, method):
        # 每个测试用例执行之前做操作
        log().info("用例%s开始" % method.__name__)

    def teardown_method(self, method):
        # 每个测试用例执行之后做操作
        log().info("用例%s结束" % method.__name__)

    @pytest.mark.Demo
    def test_GetDevice_000_demo(self):
        """测试RegisterDevices接口， device注册流程"""
        resp = deviceManager_obj.get_device()
        assert resp.status_code == 200
        assert resp.error_code == 0


if __name__ == '__main__':
    pass




