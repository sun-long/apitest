#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pytest
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
import time
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
import os
@pytest.mark.ids
@pytest.mark.checkin
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


    def test_api_IdentityService_CompareFaceIDCard_01(self, config_obj, IdentityApi):
        """验证手持身份证单接口_验证支持图片格式功能_输入三种图片格式_JPG_PNG_BMP"""
        auto_rotate = None
        min_quality_level = None
        encrypt_info = None
        image="hold_idcard/hold_idcard_5.jpg"
        resp = IdentityApi.CompareFaceIDCard(image=image, auto_rotate=auto_rotate, min_quality_level=min_quality_level, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")



if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])