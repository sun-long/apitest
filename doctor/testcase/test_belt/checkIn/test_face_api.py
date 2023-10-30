#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.checkin
@pytest.mark.ids
class TestFaceApi(object):
    """ face Api测试"""

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

    

    def test_api_FaceService_CompareImage(self, config_obj, FaceApi):
        """  人脸 1:1 比对接口, 输入两张图片, 进行特征比对."""
        image = None
        base_image = None
        auto_rotate = None
        min_quality_level = None
        encrypt_info = None
        resp = FaceApi.FaceService_CompareImagePostApi(image=image, base_image=base_image, auto_rotate=auto_rotate, min_quality_level=min_quality_level, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.message") == "E12003006: image data is empty"


    def test_api_FaceService_DetectLiveness(self, config_obj, FaceApi):
        """  提供图片静默活体检测."""
        image = None
        min_quality_level = None
        disable_defake = None
        encrypt_info = None
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level, disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.message") == "E12003006: image data is empty"

   