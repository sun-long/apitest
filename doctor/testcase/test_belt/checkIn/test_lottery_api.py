#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestLotteryApi(object):
    """ lottery Api测试"""

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

    @pytest.mark.checkin
    def test_api_BotLotteryService_LotteryOcr(self, config_obj, LotteryApi):
        """  彩票识别. """
        image_path = os.path.join(config.image_path, "go_image/belt/lottery/20221212_114827.bmp")
        image = LotteryApi.imageToBase64(image_path)
        resp = LotteryApi.BotLotteryService_LotteryOcrPostApi(image=image)
        assert resp.status_code == 200
