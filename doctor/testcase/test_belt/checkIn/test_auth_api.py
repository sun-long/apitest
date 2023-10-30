#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import base64
import os
import random
import string
import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.checkin
class TestAuthApi(object):
    """ auth Api测试"""

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

    def test_api_ConsoleAuthService_GetAccountInfo(self, config_obj, AuthDoubleApi):
        """  获取当前账户的信息 包含账户是否被禁用 是否开启后付费 """
        resp = AuthDoubleApi.ConsoleAuthService_GetAccountInfoGetApi()
        assert resp.status_code == 200

    def test_api_ConsoleAuthService_GetAccountStatus(self, config_obj, AuthDoubleApi):
        """  账号中心实名认证 获取认证结果 """
        resp = AuthDoubleApi.ConsoleAuthService_GetAccountStatusGetApi()
        assert resp.status_code == 200

    def test_api_ConsoleAuthService_GetEnterpriseAccount(self, config_obj, AuthEnterpriseApi):
        """  账号中心实名认证 查看企业认证数据 """
        resp = AuthEnterpriseApi.ConsoleAuthService_GetEnterpriseAccountGetApi()
        assert resp.status_code == 200

    def test_api_ConsoleAuthService_GetIndustryInfo(self, config_obj, AuthDoubleApi):
        """  账号中心实名认证 获取行业信息 """
        resp = AuthDoubleApi.ConsoleAuthService_GetIndustryInfoGetApi()
        assert resp.status_code == 200

    def test_api_ConsoleAuthService_GetPersonAccount(self, config_obj, AuthPersonApi):
        """  账号中心实名认证 查看个人认证数据 """
        resp = AuthPersonApi.ConsoleAuthService_GetPersonAccountGetApi()
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        print(ran_str)
        assert resp.status_code == 200

    def test_api_ConsoleAuthService_GetPersonAccountUnRedactedInfo(self, config_obj, AuthPersonApi):
        """  账号中心实名认证 查看个人认证未脱敏数据(姓名或者手机号或者身份证号码) """
        resp = AuthPersonApi.ConsoleAuthService_GetPersonAccountUnRedactedInfoGetApi()
        assert resp.status_code == 200