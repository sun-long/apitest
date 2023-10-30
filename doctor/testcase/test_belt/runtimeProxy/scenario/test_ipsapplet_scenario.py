#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from pytest_check import check

from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestIpsappletScenario(object):
    """ Ipsapplet scenario test"""

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

    def test_scenario_000_batchProcessCheck(self, config_obj, IpsappletApi, ViperappletApi, appletConfigStr):
        """ 检查batchProcess接口,proxy和viper一致"""
        # 准备测试数据
        image1 = os.path.join(config.image_path, "go_image/face/wsh/shihan1.jpg")
        image2 = os.path.join(config.image_path, "go_image/face/wsh/shihan2.jpg")
        requests_proxy = [
            {
                "images": [
                    {"data": IpsappletApi.imageToBase64(image1), },
                    {"data": IpsappletApi.imageToBase64(image2), },
                ],
                "config": {
                    "value": "{\"stages\":[\"headpose\",\"eyestate\",\"liveness\",\"feature\",\"defake\"]}"
                }
            },
        ]
        requests_viper = [
            {
                "images": [
                    {"data": IpsappletApi.imageToBase64(image1), },
                    {"data": IpsappletApi.imageToBase64(image2), },
                ],
                "config": {
                    "stages": ["headpose", "eyestate", "liveness", "feature", "defake"]
                }
            },
        ]
        # 1. 调用proxy接口
        resp_proxy = IpsappletApi.BatchProcessPostApi(requests=requests_proxy)

        # 2. 调用viper接口
        resp_viper = ViperappletApi.BatchProcessPostApi(requests_viper)

        # 3. 对比返回结果
        check_list = [
            "responses.0.response",
            "responses.0.response_items",
            "results.0.code",
            "results.0.error",
            "results.0.status",
        ]
        for item in check_list:
            proxy_value = resp_proxy.json_get(item)
            viper_value = resp_viper.json_get(item)
            with check: assert proxy_value == viper_value, "%s字段返回结果不一致,%s=%s" % (
                item, proxy_value, viper_value)

    def test_scenario_001_GetSystemInfoCheck(self, config_obj, IpsappletApi, ViperappletApi):
        """ 检查GetSystemInfo接口,proxy和viper一致"""
        # 准备测试数据
        # 1. 调用proxy接口
        resp_proxy = IpsappletApi.GetSystemInfoGetApi()
        assert resp_proxy.status_code == 200
        # 2. 调用viper接口
        resp_viper = ViperappletApi.GetSystemInfoGetApi()
        assert resp_viper.status_code == 200

        # 3. 对比返回结果
        check_list = ["app_name",
                      "app_version",
                      "load.decode_rate",
                      "load.failed_count",
                      "load.max_decode_rate",
                      "load.success_count",
                      "models_info",
                      ]
        for item in check_list:
            proxy_value = resp_proxy.json_get(item)
            viper_value = resp_viper.json_get(item)
            with check: assert proxy_value == viper_value, "%s字段返回结果不一致,%s=%s" % (
                item, proxy_value, viper_value)