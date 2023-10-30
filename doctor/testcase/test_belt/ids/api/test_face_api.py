#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import pytest
from commonlib.api_lib.AES_new import AESCipher
from commonlib.log_utils import log
import os
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
@pytest.mark.P0
@pytest.mark.Regression
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

    def test_api_Compare_001(self, config_obj, testImages_multiple_faces, FaceApi):
        """验证face1:1单接口_验证图片内存在多张人脸_正例"""
        resp = FaceApi.compareImage(testImages_multiple_faces.base_image, testImages_multiple_faces.image)
        assert resp.status_code == 200
        assert resp.schema_validator(["score", "feature_version"], response_type="200"), "Json_schema验证失败"



    def test_api_Compare_01(self, config_obj, testImages_format, FaceApi):
        """验证face1:1单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_正例"""
        resp = FaceApi.compareImage(testImages_format.base_image, testImages_format.image)
        assert resp.status_code == 200
        assert resp.schema_validator(["score", "feature_version"], response_type="200"), "Json_schema验证失败"

    def test_api_Compare_02(self, config_obj, testImages_same, FaceApi):
        """验证face1:1单接口_验证对比功能_设置两张一样的图片_预期分数接近/等于1"""
        resp = FaceApi.compareImage(testImages_same.base_image, testImages_same.image)
        assert resp.status_code == 200
        assert resp.resp_json["score"] >= 0.99
        assert resp.schema_validator(["score", "feature_version"], response_type="200"), "Json_schema验证失败"

    def test_api_Compare_03(self, config_obj, testImages_similar, FaceApi):
        """验证face1:1单接口_验证对比功能_设置同一人的不同图片_预期分数大于0.5"""
        resp = FaceApi.compareImage(testImages_similar.base_image, testImages_similar.image)
        assert resp.status_code == 200
        assert resp.resp_json["score"] >= 0.5
        assert resp.schema_validator(["score", "feature_version"], response_type="200"), "Json_schema验证失败"

    def test_api_Compare_04(self, config_obj, testImages_different, FaceApi):
        """验证face1:1单接口_验证对比功能_设置不同人的不同图片_预期分数小于0.5"""
        resp = FaceApi.compareImage(testImages_different.base_image, testImages_different.image)
        assert resp.status_code == 200
        assert resp.schema_validator(["score", "feature_version"], response_type="200"), "Json_schema验证失败"
        assert resp.resp_json["score"] <= 0.5
        assert resp.schema_validator(["score", "feature_version"], response_type="200"), "Json_schema验证失败"

    def test_api_Compare_05(self, config_obj, testImage_rotate, FaceApi):
        """验证face1:1单接口_验证自动旋转检测功能_设置两张一样的图片_其中一张带旋转_角度为90_180_270_预期分数等于/接近1"""
        resp = FaceApi.compareImage(testImage_rotate.base_image, testImage_rotate.image, auto_rotate=True)
        assert resp.status_code == 200
        assert resp.resp_json["score"] >= 0.98
        assert resp.schema_validator(["score", "feature_version"], response_type="200"), "Json_schema验证失败"

    def test_api_Compare_06(self, config_obj, testImages_badQuality, FaceApi):
        """验证face1:1单接口_验证质量过滤功能_设置质量等级较高_使用质量较差图片_预期返回"""
        resp = FaceApi.compareImage(testImages_badQuality.base_image, testImages_badQuality.image, min_quality_level="HIGH")
        assert resp.status_code != 200

    def test_api_Compare_07(self, config_obj, testImages_same, FaceApi, user_info):
        """验证face1:1单接口_验证加密功能_request设置图片加密"""
        cryptor = AESCipher(user_info.sk)
        jstr = {
            "base_image": FaceApi.idsImageToBase64(testImages_same.base_image),
            "image": FaceApi.idsImageToBase64(testImages_same.image),
        }
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher = cryptor.decrypt(cypher)
        feilds = ["base_image", "image"]
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = FaceApi.compareImage(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.resp_json["score"] >= 0.98
        assert resp.schema_validator(["score", "feature_version"], response_type="200"), "Json_schema验证失败"

    def test_api_Compare_08(self, config_obj, testImages_same, FaceApi, user_info):
        """验证face1:1单接口_验证加密GCM功能_request设置图片加密"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {
            "base_image": FaceApi.idsImageToBase64(testImages_same.base_image),
            "image": FaceApi.idsImageToBase64(testImages_same.image),
        }
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher = cryptor.decrypt(cypher)
        feilds = ["base_image", "image"]
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = FaceApi.compareImage(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.resp_json["score"] >= 0.98
        assert resp.schema_validator(["score", "feature_version"], response_type="200"), "Json_schema验证失败"

if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])