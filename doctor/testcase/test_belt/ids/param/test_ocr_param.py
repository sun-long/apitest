#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib.log_utils import log
from commonlib.api_lib.base_api import BaseApi
from commonlib.config import ids_image_path


invalidimage_15M=os.path.join(ids_image_path,"ocr/beyond_size_15M.png")
invalidimage_7M=os.path.join(ids_image_path,"ocr/beyond_size_7M.jpg")
image_ok=os.path.join(ids_image_path,"ocr/image_ok.jpg")

invalidimage_15M=str(BaseApi.imageToBase64(invalidimage_15M))
invalidimage_7M=str(BaseApi.imageToBase64(invalidimage_7M))
image_ok=str(BaseApi.imageToBase64(image_ok))

invalidencrypt_info={
    "algorithm": "",
    "version": 0,
    "iv": "string",
    "encrypted_fields": [
    "string"
    ],
    "data": "string"
}
class TestOcrParam(object):
    """ ocr Param测试"""

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
        ('image', invalidimage_7M),
        ('image', invalidimage_15M),
        ('image', ''),
        ('image', None),
        ('encrypt_info', invalidencrypt_info),
        ('encrypt_info', ''),
        # ('encrypt_info', None),
    ])
    def test_api_OCRBankcardInvalidParam(self, invalidParam, config_obj, OcrApi):
        """验证银行卡单接口_图片超过大小_图片为none_加密参数为none_反例 """
         
        encrypt_info={
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
            "string"
            ],
            "data": "string"
        }
        intef = OcrApi.OCRService_OCRBankcardPostApi(image=image_ok, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.status_code!=500
        assert resp.status_code!=401

    @pytest.mark.parametrize("invalidParam", [
        ('image', invalidimage_7M),
        ('image', invalidimage_15M),
        ('image', ''),
        ('image', None),
        ('encrypt_info', invalidencrypt_info),
        ('encrypt_info', ''),
        # ('encrypt_info', None),
    ])
    def test_api_OCRBusinessLicenseInvalidParam(self, invalidParam, config_obj, OcrApi):
        """验证营业执照单接口_图片超过大小_图片为none_加密参数为none_反例 """
         
        encrypt_info={
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
            "string"
            ],
            "data": "string"
        }
        intef = OcrApi.OCRService_OCRBusinessLicensePostApi(image=image_ok, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.status_code!=500
        assert resp.status_code!=401

    @pytest.mark.parametrize("invalidParam", [
        ('image', invalidimage_7M),
        ('image', invalidimage_15M),
        ('image', ''),
        ('image', None),
        ('encrypt_info', invalidencrypt_info),
        ('encrypt_info', ''),
        # ('encrypt_info', None),#返回正常，结果不加密
    ])
    def test_api_OCRDrivingLicenseInvalidParam(self, invalidParam, config_obj, OcrApi):
        """验证驾驶证单接口_图片超过大小_图片为none_加密参数为none_反例 """
         
        encrypt_info={
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
            "string"
            ],
            "data": "string"
        }
        intef = OcrApi.OCRService_OCRDrivingLicensePostApi(image=image_ok, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.status_code!=500
        assert resp.status_code!=401

    @pytest.mark.parametrize("invalidParam", [
        ('image', invalidimage_7M),
        ('image', invalidimage_15M),
        ('image', ''),
        ('image', None),
        ('encrypt_info', invalidencrypt_info),
        ('encrypt_info', ''),
        # ('encrypt_info', None),
    ])
    def test_api_OCRHKMacauExitEntryPermitInvalidParam(self, invalidParam, config_obj, OcrApi):
        """验证港澳通行证单接口_图片超过大小_图片为none_加密参数为none_反例 """
         
        encrypt_info={
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
            "string"
            ],
            "data": "string"
        }
        intef = OcrApi.OCRService_OCRHKMacauExitEntryPermitPostApi(image=image_ok, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.status_code!=500
        assert resp.status_code!=401

    @pytest.mark.parametrize("invalidParam", [
        ('image', invalidimage_7M),
        ('image', invalidimage_15M),
        ('image', ''),
        ('image', None),
        # ('side', 'invalidside'),
        ('side', ''),
        # ('side', None),
        # ('detect_quality', 'invaliddetect_quality'),
        ('detect_quality', ''),
        # ('detect_quality', None),
        ('encrypt_info', invalidencrypt_info),
        ('encrypt_info', ''),
        # ('encrypt_info', None),
    ])
    def test_api_OCRIDCardInvalidParam(self, invalidParam, config_obj, OcrApi):
        """验证身份证单接口_图片超过大小_图片为none_加密参数为none_反例 """
         
        side = "FRONT"
        detect_quality = False
        encrypt_info={
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
            "string"
            ],
            "data": "string"
        }
        intef = OcrApi.OCRService_OCRIDCardPostApi(image=image_ok, side=side, detect_quality=detect_quality, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.status_code!=500
        assert resp.status_code!=401

    @pytest.mark.parametrize("invalidParam", [
        ('image', invalidimage_7M),
        ('image', invalidimage_15M),
        ('image', ''),
        ('image', None),
        ('encrypt_info', invalidencrypt_info),
        ('encrypt_info', ''),
        # ('encrypt_info', None),
    ])
    def test_api_OCRPassportInvalidParam(self, invalidParam, config_obj, OcrApi):
        """验证护照单接口_图片超过大小_图片为none_加密参数为none_反例 """
         
        encrypt_info={
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
            "string"
            ],
            "data": "string"
        }
        intef = OcrApi.OCRService_OCRPassportPostApi(image=image_ok, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.status_code!=500
        assert resp.status_code!=401
        

    @pytest.mark.parametrize("invalidParam", [
        ('image', invalidimage_7M),
        ('image', invalidimage_15M),
        ('image', ''),
        ('image', None),
        ('encrypt_info', invalidencrypt_info),
        ('encrypt_info', ''),
        # ('encrypt_info', None),
    ])
    def test_api_OCRTaiwanExitEntryPermitInvalidParam(self, invalidParam, config_obj, OcrApi):
        """验证台湾通行证单接口_图片超过大小_图片为none_加密参数为none_反例 """
         
        encrypt_info={
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
            "string"
            ],
            "data": "string"
        }
        intef = OcrApi.OCRService_OCRTaiwanExitEntryPermitPostApi(image=image_ok, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.status_code!=500
        assert resp.status_code!=401

    @pytest.mark.parametrize("invalidParam", [
        ('image', invalidimage_7M),
        ('image', invalidimage_15M),
        ('image', ''),
        ('image', None),
        ('encrypt_info', invalidencrypt_info),
        ('encrypt_info', ''),
        # ('encrypt_info', None),
    ])
    def test_api_OCRVehicleLicenseInvalidParam(self, invalidParam, config_obj, OcrApi):
        """验证行驶证单接口_图片超过大小_图片为none_加密参数为none_反例 """
         
        encrypt_info={
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
            "string"
            ],
            "data": "string"
        }
        intef = OcrApi.OCRService_OCRVehicleLicensePostApi(image=image_ok, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.status_code!=500
        assert resp.status_code!=401
        
    @pytest.mark.parametrize("invalidParam", [
        ('session', 'invalidsession'),
        ('session', ''),
        ('session', None),
        ('encrypt_info', 'invalidencrypt_info'),
        ('encrypt_info', ''),
    ])
    def test_api_OCRService_CreateSessionInvalidParam(self, invalidParam, config_obj, OcrApi):
        """  创建一个检测会话参数校验"""
        session = None
        encrypt_info = None
        intef = OcrApi.OCRService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200    
if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])