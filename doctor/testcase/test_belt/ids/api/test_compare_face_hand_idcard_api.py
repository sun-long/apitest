#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pytest
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
import time
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
import os
@pytest.mark.P0
@pytest.mark.Regression
class TestCompareFaceHandholdIDCardApi(object):
    """ CompareFaceHandholdIDCard Api测试"""

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


    def test_api_IdentityService_CompareFaceIDCard_01(self, config_obj, IdentityApi,test_hold_idcard_format):
        """验证手持身份证单接口_验证支持图片格式功能_输入三种图片格式_JPG_PNG_BMP"""
        auto_rotate = None
        min_quality_level = None
        encrypt_info = None
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_format, auto_rotate=auto_rotate, min_quality_level=min_quality_level, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")


    def test_api_IdentityService_CompareFaceIDCard_02(self, config_obj, IdentityApi,user_info,test_hold_idcard_common):
        """验证手持身份证单接口_验证支持AES_CBC加密_设置image为None"""
        cryptor = AESCipher(user_info.sk)
        jstr = {
            "image": IdentityApi.idsImageToBase64(test_hold_idcard_common),
        }
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher = cryptor.decrypt(cypher)
        feilds = ["image"]
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = IdentityApi.CompareFaceIDCard(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")>0.8

    def test_api_IdentityService_CompareFaceIDCard_03(self, config_obj, IdentityApi,user_info,test_hold_idcard_common):
        """验证手持身份证单接口_验证支持AES_CBC加密_设置image为非None,但是与加密中的图片不一致，预期解析的是加密图片"""
        image=f"H5_back.jpg"
        cryptor = AESCipher(user_info.sk)
        jstr = {
            "image": IdentityApi.idsImageToBase64(test_hold_idcard_common),
        }
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher = cryptor.decrypt(cypher)
        feilds = ["image"]
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = IdentityApi.CompareFaceIDCard(image=image,encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")>0.8

    def test_api_IdentityService_CompareFaceIDCard_04(self, config_obj, IdentityApi,user_info,test_hold_idcard_common):
        """验证手持身份证单接口_验证支持AES_GCM加密"""
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {
            "image": IdentityApi.idsImageToBase64(test_hold_idcard_common),
        }
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        de_cypher = cryptor.decrypt(cypher)
        feilds = ["image"]
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = IdentityApi.CompareFaceIDCard(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")>0.8

    def test_api_IdentityService_CompareFaceIDCard_05(self, config_obj, IdentityApi,test_hold_idcard_rotate):
        """验证手持身份证单接口_验证自动旋转的功能"""
        auto_rotate = True
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_rotate,auto_rotate=auto_rotate)
        assert resp.status_code == 200
        assert resp.json_get("score")>0.8        

    def test_api_IdentityService_CompareFaceIDCard_06(self, config_obj, IdentityApi,test_hold_idcard_outsize):
        """验证手持身份证单接口_错误码_图片超过大小限制"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_outsize)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "image size is exceeded"
        assert resp.json_get("error.details.0.reason") == 12003005

        
    def test_api_IdentityService_CompareFaceIDCard_07(self, config_obj, IdentityApi):
        """验证手持身份证单接口_错误码_图片为空"""
        resp = IdentityApi.CompareFaceIDCard(image=None)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "image data is empty"
        assert resp.json_get("error.details.0.reason") == 12003006
    def test_api_IdentityService_CompareFaceIDCard_08(self, config_obj, IdentityApi,test_hold_idcard_error_format):
        """验证手持身份证单接口_错误码_图片格式错误"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_error_format)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "invalid image"
        assert resp.json_get("error.details.0.reason") == 12003007
    def test_api_IdentityService_CompareFaceIDCard_09(self, config_obj, IdentityApi,test_hold_idcard_low_resolution):
        """验证手持身份证单接口_错误码_分辨率过低"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_low_resolution)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "low image resolution"
        assert resp.json_get("error.details.0.reason") == 12003009

    def test_api_IdentityService_CompareFaceIDCard_10(self, config_obj, IdentityApi,test_hold_idcard_fake):
        """验证手持身份证单接口_错误码_身份证非原件"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_fake)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "invalid id card source"
        assert resp.json_get("error.details.0.reason") == 12003012


    def test_api_IdentityService_CompareFaceIDCard_11(self, config_obj, IdentityApi,test_hold_idcard_no_idcard):
        """验证手持身份证单接口_错误码_未检测到人像面身份证"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_no_idcard)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "no front id card detected"
        assert resp.json_get("error.details.0.reason") == 12003100

    def test_api_IdentityService_CompareFaceIDCard_12(self, config_obj, IdentityApi,test_hold_idcard_cropped):
        """验证手持身份证单接口_错误码_人像面存在裁剪"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_cropped)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "front idcard cropped"
        assert resp.json_get("error.details.0.reason") == 12003986

    @pytest.mark.skip("无图片可构造出此错误码字，除非身份证人像面无法识别到人脸")
    def test_api_IdentityService_CompareFaceIDCard_13(self, config_obj, IdentityApi,test_hold_idcard_no_face):
        """验证手持身份证单接口_错误码_未检测到人脸"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_no_face)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "no face detected"
        assert resp.json_get("error.details.0.reason") == 12003020

    def test_api_IdentityService_CompareFaceIDCard_14(self, config_obj, IdentityApi,test_hold_idcard_one_face):
        """验证手持身份证单接口_错误码_仅检测到一个人脸"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_one_face)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "only one face detected"
        assert resp.json_get("error.details.0.reason") == 12003103

    def test_api_IdentityService_CompareFaceIDCard_15(self, config_obj, IdentityApi,test_hold_idcard_multiple_face):
        """验证手持身份证单接口_错误码_图片中检测到多个人脸"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_multiple_face)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "multiple faces detected"
        assert resp.json_get("error.details.0.reason") == 12003021

    @pytest.mark.skip("无图片可构造出此错误码字，除非身份证人像面无法识别到人脸")
    def test_api_IdentityService_CompareFaceIDCard_16(self, config_obj, IdentityApi,test_hold_idcard_no_face_in_idcard):
        """验证手持身份证单接口_错误码_身份证中未检测到人脸"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_no_face_in_idcard)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "no face detected on the id card"
        assert resp.json_get("error.details.0.reason") == 12003101


    def test_api_IdentityService_CompareFaceIDCard_17(self, config_obj, IdentityApi,test_hold_idcard):
        """验证手持身份证单接口_正常场景的手持身份证"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard)
        assert resp.status_code == 200
        assert resp.json_get("score")

    def test_api_IdentityService_CompareFaceIDCard_18(self, config_obj, IdentityApi,test_hold_idcard_1v1_not_suit):
        """验证手持身份证单接口_人脸对比功能_人脸不匹配_预期返回的分数低"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_1v1_not_suit)
        assert resp.status_code == 200
        assert resp.json_get("score")<0.3

    def test_api_IdentityService_CompareFaceIDCard_19(self, config_obj, IdentityApi,test_hold_idcard_1v1_suit):
        """验证手持身份证单接口_人脸对比功能_人脸匹配_预期返回的分数高"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_1v1_suit)
        assert resp.status_code == 200
        assert resp.json_get("score")>0.7

    def test_api_IdentityService_CompareFaceIDCard_20(self, config_obj, IdentityApi,test_hold_idcard_many_idcard):
        """验证手持身份证单接口_错误码_多张身份证"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_many_idcard)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "multiple id cards detected"
        assert resp.json_get("error.details.0.reason") == 12003105


    def test_api_IdentityService_CompareFaceIDCard_21(self, config_obj, IdentityApi,test_hold_idcard_small_face):
        """验证手持身份证单接口_错误码_持身份证人脸较小"""
        resp = IdentityApi.CompareFaceIDCard(image=test_hold_idcard_small_face)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "card holder's face is too small"
        assert resp.json_get("error.details.0.reason") == 12003104

        
        

if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])