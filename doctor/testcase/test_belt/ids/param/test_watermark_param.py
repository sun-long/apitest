#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.P1
class TestWatermarkParam(object):
    """ watermark Param测试"""

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
        ('watermark', '6K6p56eR5oqA5byV6aKG5Lq657G76L+b5q2l5ZWG5rGk56eR5oqA'),#让科技引领人类进步商汤科技
        ('watermark', '6K6p56eR5oqA5byV6aKG5Lq657G76L+b5q2l5ZWG5rGk56eR5oqA5ZWK5ZWK5ZWK5ZWK5ZWK5ZWK5ZWK5ZWK'),#让科技引领人类进步商汤科技啊啊啊啊啊啊啊啊
        # ('watermark', '6K6p'),#让
        # ('watermark', "c2Vuc2V0aW1l"),#sensetime
    ])
    def test_api_DataSecurityService_SignImageInvalidParam(self, invalidParam, config_obj, WatermarkApi):
        """  图片数字水印签名.
route prefix=ids internal_prefix=ids act... """
        image =WatermarkApi.idsImageToBase64("watermark/paper.jpg")
        watermark="5ZWG5rGk56eR5oqA"#sensetime
        encrypt_info = None
        intef = WatermarkApi.DataSecurityService_SignImagePostApi(image=image, watermark=watermark, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

