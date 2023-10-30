#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils, utils
from commonlib.log_utils import log
from PIL import Image

class TestAuthiamApi(object):
    """ authIam Api测试"""

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

    def test_api_login_user(self, config_obj, AuthiamApi):
        """  登录 """
        captcha = {
            "digits": "956742",
            "id": "jTPXZ6bVHoJZMxvNMYwv"
        }
        client_id = None
        expires_after = None
        email = None
        phone = None
        verification_code = None
        username = "443022786655455183"
        password = sign_utils.getMd5("123456qw")
        resp = AuthiamApi.loginPostApi(captcha=captcha, client_id=client_id, expires_after=expires_after, email=email,
                                       phone=phone, verification_code=verification_code,
                                       username=username, password=password)
        assert resp.status_code == 200

    def test_api_login_phone(self, config_obj, AuthiamApi):
        """  登录 """
        captcha = {
            "digits": "620836",
            "id": "tiLFNNMPvzkGX9ysYSZ0"
        }
        client_id = None
        expires_after = 86399
        email = None
        phone = "15011263631"
        verification_code = None
        username = None
        password = sign_utils.getMd5("wangan1234")
        resp = AuthiamApi.loginPostApi(captcha=captcha, client_id=client_id, expires_after=expires_after, email=email,
                                       phone=phone, verification_code=verification_code,
                                       username=username, password=password)
        assert resp.status_code == 200

    def test_api_captcha(self, config_obj, AuthiamApi):
        """ 获取验证码"""
        resp = AuthiamApi.captchaGetApi(width=300, height=300, print_log=True)
        assert resp.status_code == 200
        captcha_id = resp.json_get("id")
        data = resp.json_get("data")
        data = data.split("data:image/png;base64,")[-1]
        img_path = os.path.join(config.temp_path,"captcha.png")
        utils.base64ToFile(img_path, data)
        img = Image.open(img_path)
        img.show()
        log().info("captcha_id: %s" % captcha_id)

    def test_api_logout(self, config_obj, AuthiamApi):
        """  登出 """
        redirect_uri = None
        resp = AuthiamApi.logoutGetApi(redirect_uri=redirect_uri)
        assert resp.status_code == 200