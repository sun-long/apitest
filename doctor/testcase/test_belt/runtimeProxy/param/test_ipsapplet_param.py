#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestIpsappletParam(object):
    """ ipsApplet Param测试"""

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
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests.0.config', None),
        ('requests.0.config', ""),
        ('requests.0.config.value', ""),
        ('requests.0.images', "invalid"),
        ('requests.0.images', ""),
        ('requests.0.images', None),
        ('requests.0.images', []),
        ('requests.0.images.0.data', ""),
        ('requests.0.images.0.data', "abcde"),
    ])
    def test_api_BatchProcessInvalidParam(self, invalidParam, config_obj, IpsappletApi):
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
        intef = IpsappletApi.BatchProcessPostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_GetSystemInfoInvalidParam(self, invalidParam, config_obj, IpsappletApi):
        """  获取系统信息 [EXPERIMENTAL].
[EN] Get system info [EXPER... """
        intef = IpsappletApi.GetSystemInfoGetApi(sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('X-Resource-Type', ''),
        ('X-Resource-Type', 'invalid'),
        ('X-Resource-Type', 'ocr'),
        ('X-Resource-Type', None),
        ('X-Object-Type', ''),
        ('X-Object-Type', 'invalid'),
        ('X-Object-Type', None),
        ('X-Object-Version', ''),
        ('X-Object-Version', 'invalid'),
        ('X-Object-Version', None),
        # ('X-Bot-Name', ''),  # 本期Bot-Name不做限制
        # ('X-Bot-Name', 'invalid'),
        # ('X-Bot-Name', None),
    ])
    def test_api_GetSystemInfoInvalidHeaderParam(self, invalidParam, config_obj, IpsappletApi):
        """  获取系统信息 [EXPERIMENTAL].
[EN] Get system info [EXPER... """
        intef = IpsappletApi.GetSystemInfoGetApi(sendRequest=False)
        intef.set_headers(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
