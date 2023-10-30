#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib.log_utils import log
from commonlib.api_lib.base_api import BaseApi
from commonlib.config import ids_image_path

class TestIdentityParam(object):
    """ identity Param测试"""

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

    invalidencrypt_info={
        "algorithm": "",
        "version": 0,
        "iv": "string",
        "encrypted_fields": [
        "string"
        ],
        "data": "string"
    }    
    invalidimage_7M=os.path.join(ids_image_path,"ocr/beyond_size_7M.jpg")
    invalidimage_7M=str(BaseApi.imageToBase64(invalidimage_7M))

    @pytest.mark.parametrize("invalidParam", [
        ('name', '345'),
        ('name', ''),
        ('name', None),
        ('idcard_number', "sfdfgfg"),
        ('idcard_number', 123456),
        ('idcard_number', ''),
        ('idcard_number', None),
        ('expiry_date', '2030-01-00'),
        ('expiry_date', '2030-00-31'),
        ('expiry_date', '2030-01-32'),
        ('expiry_date', '2030-13-32'),
        ('expiry_date', '1888-01-30'),
        ('expiry_date', '2000-00-00'),
        ('expiry_date', '00-00-00'),
        ('expiry_date', '20211-023-220'),
        ('expiry_date', '011-023-0'),
        ('expiry_date', '011-0-0'),
        ('expiry_date', '011-0'),
        ('expiry_date', '2022-02-23-26'),
        ('expiry_date', '00'),
        ('expiry_date', '000'),
        ('expiry_date', '00000'),
        # ('expiry_date', ''),
        # ('expiry_date', None),
        ('encrypt_info', invalidencrypt_info),
        ('encrypt_info', ''),
        # ('encrypt_info', None),
    ])
    def test_api_VerifyIDCardInvalidParam(self, invalidParam, config_obj,testVerifyIDCard_official, IdentityApi):
        """验证二要素身份核验单接口_name非法_id非法_有效期非法_加密参数非法_反例"""
        name = testVerifyIDCard_official.name
        id_card_number = testVerifyIDCard_official.id_card_number
        expiry_date = "2030-02-23"
        encrypt_info={
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "encrypted_fields": [
            "string"
            ],
            "data": "string"
        }

        intef = IdentityApi.IdentityService_VerifyIDCardPostApi(name=name, idcard_number=id_card_number, expiry_date=expiry_date, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.status_code!=500
        assert resp.status_code!=401
        
     
    @pytest.mark.parametrize("invalidParam", [
        ('name', '345'),
        ('name', ''),
        ('name', None),
        ('idcard_number', "sfdfgfg"),
        ('idcard_number', 123456),
        ('idcard_number', ''),
        ('idcard_number', None),
        ('expiry_date', '2030-01-00'),
        ('expiry_date', '2030-00-31'),
        ('expiry_date', '2030-01-32'),
        ('expiry_date', '2030-13-32'),
        ('expiry_date', '1888-01-30'),
        ('expiry_date', '2000-00-00'),
        ('expiry_date', '00-00-00'),
        ('expiry_date', '20211-023-220'),
        ('expiry_date', '011-023-0'),
        ('expiry_date', '011-0-0'),
        ('expiry_date', '011-0'),
        ('expiry_date', '00'),
        ('expiry_date', '000'),
        ('expiry_date', '00000'),
        ('expiry_date', '2022-02-23-26'),
        # ('expiry_date', ''),
        # ('expiry_date', None),
        ('encrypt_info', invalidencrypt_info),
        ('encrypt_info', ''),
        # ('encrypt_info', None),
        ('image', invalidimage_7M),
        ('image', ''),
        ('image', None),
    ])

    def test_api_VerifyIDCardFaceInvalidParam(self, invalidParam, config_obj, testVerifyIDCardFace_common,IdentityApi):
        """验证三要素身份核验单接口_name非法_id非法_有效期非法_加密参数非法_图片非法_反例"""
        expiry_date = "2030-02-23"
        name = testVerifyIDCardFace_common.name
        id_card_number = testVerifyIDCardFace_common.id_card_number
        base64_image=str(BaseApi.imageToBase64(os.path.join(ids_image_path,testVerifyIDCardFace_common.image)))
        encrypt_info={
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "encrypted_fields": [
            "string"
            ],
            "data": "string"
        }
        intef = IdentityApi.IdentityService_VerifyIDCardFacePostApi(name=name, idcard_number=id_card_number, image=base64_image, encrypt_info=encrypt_info, expiry_date=expiry_date,sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.status_code!=500
        assert resp.status_code!=401

if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])