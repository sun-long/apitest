#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
from pytest_check import check


class TestLotteryScenario(object):
    """ Lottery scenario test"""

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

    @pytest.mark.parametrize("image_name", [
        "20221212_114827.bmp",
        "20221212_114827.jpg",
        "20221212_114827.png",
    ])
    @pytest.mark.Regression
    @pytest.mark.P0
    def test_scenario_000_imageFormat(self, config_obj, LotteryApi, image_name):
        """  ocr接口支持不同图片类型：bmp,jpg,png"""
        image_path = os.path.join(config.image_path, "go_image/belt/lottery/%s" % image_name)
        image = LotteryApi.imageToBase64(image_path)
        resp = LotteryApi.BotLotteryService_LotteryOcrPostApi(image=image)
        assert resp.status_code == 200
        assert resp.json_get("scratch_ticket.security_code")
        assert resp.json_get("scratch_ticket.ticket_code")

    @pytest.mark.Regression
    @pytest.mark.P0
    def test_scenario_001_imageSizeGt4M(self, config_obj, LotteryApi):
        """  图片大小不支持大于4M"""
        image_path = os.path.join(config.image_path, "go_image/belt/lottery/20221212_111637_gt4M.png")
        image = LotteryApi.imageToBase64(image_path)
        resp = LotteryApi.BotLotteryService_LotteryOcrPostApi(image=image)
        assert resp.status_code == 400
        assert resp.json_get("error.message") == "image data over size"

    @pytest.mark.Regression
    @pytest.mark.P0
    def test_scenario_002_noContent(self, config_obj, LotteryApi):
        """  图片中无彩票识别的内容，能够正常返回，返回内容为乱码或无内容"""
        image_path = os.path.join(config.image_path, "go_image/belt/lottery/noticket.jpg")
        image = LotteryApi.imageToBase64(image_path)
        resp = LotteryApi.BotLotteryService_LotteryOcrPostApi(image=image)
        assert resp.status_code == 200

    @pytest.mark.parametrize("image_name", [
        "ticket_1M.jpg",
        "ticket_4M.png",
        "ticket_105K.jpg",
    ])
    @pytest.mark.Regression
    @pytest.mark.P0
    @pytest.mark.xfail(reason="耗时目前达不到300ms")
    def test_scenario_003_delayLt300ms(self, config_obj, LotteryApi, image_name):
        """  接口耗时小于300ms"""
        exec_time = 10
        exec_result = []
        image_path = os.path.join(config.image_path, "go_image/belt/lottery/%s" % image_name)
        image = LotteryApi.imageToBase64(image_path)
        for x in range(exec_time):
            resp = LotteryApi.BotLotteryService_LotteryOcrPostApi(image=image)
            exec_result.append(resp.time)
            with check: assert resp.status_code == 200
            with check: assert resp.time <= 0.3, "接口调用耗时%s大于300ms，" % resp.time
        _str = "\n%s\nmax:%ss,min:%ss,avg:%ss\n" % (image_name, max(exec_result), min(exec_result), round(sum(exec_result)/len(exec_result)*1.0,2))
        for idx, x in enumerate(exec_result):
            _str += "[%s]%ss\n" % (idx, x)
        log().info(_str)