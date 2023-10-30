#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.checkin
class TestOcrApi(object):
    """ ocr Api测试"""

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

    def test_api_OCRService_OCRBankcard(self, config_obj, OcrApi):
        """  对图片中的文字进行模板检测识别."""
        image_path = os.path.join(
            config.ids_image_path, "ocr/bankcard/debit_card.jpg")
        image = OcrApi.imageToBase64(image_path)       
        encrypt_info = None
        resp = OcrApi.OCRService_OCRBankcardPostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200

    def test_api_OCRService_OCRBusinessLicense(self, config_obj, OcrApi):
        """  营业执照识别."""
        image_path = os.path.join(
            config.ids_image_path, "ocr/business_license/business_01.jpg")
        image = OcrApi.imageToBase64(image_path)       
        encrypt_info = None
        resp = OcrApi.OCRService_OCRBusinessLicensePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200

    def test_api_OCRService_OCRDrivingLicense(self, config_obj, OcrApi):
        """  驾驶证识别."""
        image_path = os.path.join(
            config.ids_image_path, "ocr/driving_license/driver_full_01.jpg")
        image = OcrApi.imageToBase64(image_path)       
        encrypt_info = None
        resp = OcrApi.OCRService_OCRDrivingLicensePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200

    def test_api_OCRService_OCRHKMacauExitEntryPermit(self, config_obj, OcrApi):
        """  港澳通行证识别."""
        image_path = os.path.join(
            config.ids_image_path, "ocr/hk_macau_exit_entry_permit/hk_macau_exit_entry_permit_01.jpeg")
        image = OcrApi.imageToBase64(image_path)       
        encrypt_info = None
        resp = OcrApi.OCRService_OCRHKMacauExitEntryPermitPostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200

    def test_api_OCRService_OCRIDCard(self, config_obj, OcrApi):
        """  检测识别图片中的身份证."""
        image_path = os.path.join(
            config.ids_image_path, "ocr/idcard/normal/idcard_front_01.jpg")
        image = OcrApi.imageToBase64(image_path)       
        side = None
        detect_quality = None
        encrypt_info = None
        resp = OcrApi.OCRService_OCRIDCardPostApi(image=image, side=side, detect_quality=detect_quality, encrypt_info=encrypt_info)
        assert resp.status_code == 200

    def test_api_OCRService_OCRPassport(self, config_obj, OcrApi):
        """  护照识别."""
        image_path = os.path.join(
            config.ids_image_path, "ocr/passport/passport_02.jpeg")
        image = OcrApi.imageToBase64(image_path)       
        encrypt_info = None
        resp = OcrApi.OCRService_OCRPassportPostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200

    def test_api_OCRService_OCRTaiwanExitEntryPermit(self, config_obj, OcrApi):
        """  台湾通行证识别. """
        image_path = os.path.join(
            config.ids_image_path, "ocr/taiwan_exit_entry_permit/taiwan_exit_entry_permit_01.jpeg")
        image = OcrApi.imageToBase64(image_path)       
        encrypt_info = None
        resp = OcrApi.OCRService_OCRTaiwanExitEntryPermitPostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200

    def test_api_OCRService_OCRVehicleLicense(self, config_obj, OcrApi):
        """  行驶证识别."""
        image_path = os.path.join(
            config.ids_image_path, "ocr/vehicle_license/first.jpg")
        image = OcrApi.imageToBase64(image_path)       
        encrypt_info = None
        resp = OcrApi.OCRService_OCRVehicleLicensePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        
    def test_api_OCRService_OCRCarPlate(self, config_obj, OcrApi):
        """  车牌号识别 """
        imagepath = os.path.join(config.ids_image_path,"ocr/car_plate/normal_car_plate_blue.jpg")
        image = OcrApi.imageToBase64(imagepath)
        encrypt_info = None
        resp = OcrApi.OCRService_OCRCarPlatePostApi(image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200    
