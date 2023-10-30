#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib.log_utils import log
from commonlib.api_lib.base_api import BaseApi
from commonlib.config import ids_image_path
@pytest.mark.P1
@pytest.mark.Regression

class TestCompareFaceHandholdIDCardParam(object):
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

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('auto_rotate', 'invalidauto_rotate'),
        ('auto_rotate', ''),
        ('min_quality_level', 'invalidmin_quality_level'),
        ('min_quality_level', ''),
        ('encrypt_info', 'invalidencrypt_info'),
        ('encrypt_info', ''),
    ])
    def test_api_IdentityService_CompareFaceIDCardInvalidParam(self, invalidParam, config_obj, IdentityApi,test_hold_idcard_common):
        """验证手持身份证单接口_非法入参"""
        image = IdentityApi.idsImageToBase64(test_hold_idcard_common)
        auto_rotate = True
        min_quality_level = True
        encrypt_info = None
        intef = IdentityApi.IdentityService_CompareFaceIDCardPostApi(image=image, auto_rotate=auto_rotate, min_quality_level=min_quality_level, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200


if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])