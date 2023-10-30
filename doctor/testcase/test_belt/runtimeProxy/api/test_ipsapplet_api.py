#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestIpsappletApi(object):
    """ ipsApplet Api测试"""

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

    def test_api_BatchProcess(self, config_obj, IpsappletApi):
        """  批量图像处理 [EXPERIMENTAL].
[EN] Batch image processing... """
        image1 = os.path.join(config.image_path, "go_image/face/wsh/shihan1.jpg")
        image2 = os.path.join(config.image_path, "go_image/face/wsh/shihan2.jpg")
        config_field = {
            "value": "{\"stages\":[\"headpose\",\"eyestate\",\"liveness\",\"feature\",\"defake\"]}"
        }
        requests = [
            {
                "images": [
                    {"data": IpsappletApi.imageToBase64(image1), },
                    {"data": IpsappletApi.imageToBase64(image2), },
                ],
                "config": config_field
            },
            {
                "images": [
                    {"data": IpsappletApi.imageToBase64(image1), },
                    {"data": IpsappletApi.imageToBase64(image2), },
                ],
                "config": config_field
            },
        ]
        resp = IpsappletApi.BatchProcessPostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_GetSystemInfo(self, config_obj, IpsappletApi):
        """  获取系统信息 [EXPERIMENTAL].
[EN] Get system info [EXPER... """
        resp = IpsappletApi.GetSystemInfoGetApi()
        assert resp.status_code == 200
