#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestArgusipsApi(object):
    """ argusIps Api测试"""

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

    def test_api_CompareFeature(self, config_obj, ArgusipsApi):
        """   """
        one = None
        other = None
        feature_version = None
        resp = ArgusipsApi.CompareFeaturePostApi(one=one, other=other, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_CompareImage(self, config_obj, ArgusipsApi):
        """   """
        one = None
        other = None
        detect_mode = None
        feature_version = None
        resp = ArgusipsApi.CompareImagePostApi(one=one, other=other, detect_mode=detect_mode, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_FaceDetect(self, config_obj, ArgusipsApi):
        """   """
        image = None
        detect_mode = None
        feature_version = None
        resp = ArgusipsApi.FaceDetectPostApi(image=image, detect_mode=detect_mode, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_FaceDetectAndExtract(self, config_obj, ArgusipsApi):
        """   """
        image = None
        face_selection = None
        detect_mode = None
        feature_version = None
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, face_selection=face_selection, detect_mode=detect_mode, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_FaceDetectAndExtractAll(self, config_obj, ArgusipsApi):
        """   """
        image = None
        detect_mode = None
        feature_version = None
        resp = ArgusipsApi.FaceDetectAndExtractAllPostApi(image=image, detect_mode=detect_mode, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_FaceExtractWithBounding(self, config_obj, ArgusipsApi):
        """   """
        image = None
        bounding = None
        crop_image = None
        feature_version = None
        resp = ArgusipsApi.FaceExtractWithBoundingPostApi(image=image, bounding=bounding, crop_image=crop_image, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_FaceDetectAndExtractWithOverlap(self, config_obj, ArgusipsApi):
        """   """
        image = None
        bounding = None
        feature_version = None
        resp = ArgusipsApi.FaceDetectAndExtractWithOverlapPostApi(image=image, bounding=bounding, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_StructDetect(self, config_obj, ArgusipsApi):
        """   """
        image = None
        mode = None
        feature_version = None
        resp = ArgusipsApi.StructDetectPostApi(image=image, mode=mode, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_StructDetectAndExtract(self, config_obj, ArgusipsApi):
        """   """
        image = None
        mode = None
        feature_version = None
        resp = ArgusipsApi.StructDetectAndExtractPostApi(image=image, mode=mode, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_StructExtractWithBounding(self, config_obj, ArgusipsApi):
        """   """
        image = None
        bounding = None
        object_type = None
        crop_image = None
        feature_version = None
        resp = ArgusipsApi.StructExtractWithBoundingPostApi(image=image, bounding=bounding, object_type=object_type, crop_image=crop_image, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_OCRTemplate(self, config_obj, ArgusipsApi):
        """   """
        region_type = None
        type = None
        image = None
        resp = ArgusipsApi.OCRTemplatePostApi(region_type=region_type, type=type, image=image)
        assert resp.status_code == 200
