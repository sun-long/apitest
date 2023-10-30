#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.ids
@pytest.mark.checkin
class TestIdentityApi(object):
    """ identity Api测试"""

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

    def test_api_IdentityService_VerifyIDCard(self, config_obj, IdentityApi,):
        """  身份证, 姓名二要素身份核验, 根据权威源校验身份证号和姓名是否匹配."""
        name = "阮志华"
        idcard_number = "445224200107155710"
        expiry_date = None
        encrypt_info = None
        resp = IdentityApi.IdentityService_VerifyIDCardPostApi(name=name, idcard_number=idcard_number, expiry_date=expiry_date, encrypt_info=encrypt_info)
        assert resp.status_code == 200

    def test_api_IdentityService_VerifyIDCardFace(self, config_obj, IdentityApi):
        """  身份证, 姓名, 人脸图三要素身份核验, 根据权威源校验身份证号和姓名是否匹配, 并比对请求中人脸图... """
        name = "阮志华"
        idcard_number = "445224200107155710"
        expiry_date = None
        image_path = os.path.join(
            config.ids_image_path, "identify/阮志华.png")
        image = IdentityApi.imageToBase64(image_path)       
        encrypt_info = None
        resp = IdentityApi.IdentityService_VerifyIDCardFacePostApi(name=name, idcard_number=idcard_number, expiry_date=expiry_date, image=image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
