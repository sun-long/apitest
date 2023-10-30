#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestArguspedestrianApi(object):
    """ argusPedestrian Api测试"""

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

    def test_api_Pedestrain_Recognize(self, config_obj, ArguspedestrianApi):
        """  pedestrian API """
        associates = None
        bg_image_upload = None
        body = None
        device = None
        face = None
        faceTrack = None
        flag = None
        image = None
        location = None
        meta = None
        misc = None
        monitor = None
        relation = None
        timestamp = None
        resp = ArguspedestrianApi.Pedestrain_RecognizePostApi(associates=associates, bg_image_upload=bg_image_upload, body=body, device=device, face=face, faceTrack=faceTrack, flag=flag, image=image, location=location, meta=meta, misc=misc, monitor=monitor, relation=relation, timestamp=timestamp)
        assert resp.status_code == 200
