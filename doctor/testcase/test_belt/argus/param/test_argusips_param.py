#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestArgusipsParam(object):
    """ argusIps Param测试"""

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
        ('one', 'invalidone'),
        ('one', ''),
        ('one', None),
        ('other', 'invalidother'),
        ('other', ''),
        ('other', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_CompareFeatureInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        one = None
        other = None
        feature_version = None
        intef = ArgusipsApi.CompareFeaturePostApi(one=one, other=other, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('one', 'invalidone'),
        ('one', ''),
        ('one', None),
        ('other', 'invalidother'),
        ('other', ''),
        ('other', None),
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_CompareImageInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        one = None
        other = None
        detect_mode = None
        feature_version = None
        intef = ArgusipsApi.CompareImagePostApi(one=one, other=other, detect_mode=detect_mode, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_FaceDetectInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        image = None
        detect_mode = None
        feature_version = None
        intef = ArgusipsApi.FaceDetectPostApi(image=image, detect_mode=detect_mode, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('face_selection', 'invalidface_selection'),
        ('face_selection', ''),
        ('face_selection', None),
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_FaceDetectAndExtractInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        image = None
        face_selection = None
        detect_mode = None
        feature_version = None
        intef = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, face_selection=face_selection, detect_mode=detect_mode, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_FaceDetectAndExtractAllInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        image = None
        detect_mode = None
        feature_version = None
        intef = ArgusipsApi.FaceDetectAndExtractAllPostApi(image=image, detect_mode=detect_mode, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('bounding', 'invalidbounding'),
        ('bounding', ''),
        ('bounding', None),
        ('crop_image', 'invalidcrop_image'),
        ('crop_image', ''),
        ('crop_image', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_FaceExtractWithBoundingInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        image = None
        bounding = None
        crop_image = None
        feature_version = None
        intef = ArgusipsApi.FaceExtractWithBoundingPostApi(image=image, bounding=bounding, crop_image=crop_image, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('bounding', 'invalidbounding'),
        ('bounding', ''),
        ('bounding', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_FaceDetectAndExtractWithOverlapInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        image = None
        bounding = None
        feature_version = None
        intef = ArgusipsApi.FaceDetectAndExtractWithOverlapPostApi(image=image, bounding=bounding, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_StructDetectInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        image = None
        mode = None
        feature_version = None
        intef = ArgusipsApi.StructDetectPostApi(image=image, mode=mode, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_StructDetectAndExtractInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        image = None
        mode = None
        feature_version = None
        intef = ArgusipsApi.StructDetectAndExtractPostApi(image=image, mode=mode, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('bounding', 'invalidbounding'),
        ('bounding', ''),
        ('bounding', None),
        ('object_type', 'invalidobject_type'),
        ('object_type', ''),
        ('object_type', None),
        ('crop_image', 'invalidcrop_image'),
        ('crop_image', ''),
        ('crop_image', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_StructExtractWithBoundingInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        image = None
        bounding = None
        object_type = None
        crop_image = None
        feature_version = None
        intef = ArgusipsApi.StructExtractWithBoundingPostApi(image=image, bounding=bounding, object_type=object_type, crop_image=crop_image, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('region_type', 'invalidregion_type'),
        ('region_type', ''),
        ('region_type', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
    ])
    def test_api_OCRTemplateInvalidParam(self, invalidParam, config_obj, ArgusipsApi):
        """   """
        region_type = None
        type = None
        image = None
        intef = ArgusipsApi.OCRTemplatePostApi(region_type=region_type, type=type, image=image, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
