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

    @pytest.mark.ConsoleRegression
    @pytest.mark.Skiponline
    def test_api_ConsoleAuthService_GetAccountInfo(self, config_obj, AuthDoubleApi):
        """  获取当前账户的信息 包含账户是否被禁用 是否开启后付费
route: prefix=console ... """
        resp = AuthDoubleApi.ConsoleAuthService_GetAccountInfoGetApi()
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    @pytest.mark.Skiponline
    def test_api_ConsoleAuthService_GetAccountStatus(self, config_obj, AuthDoubleApi):
        """  账号中心实名认证 获取认证结果
route: prefix=console action=GetAc... """
        resp = AuthDoubleApi.ConsoleAuthService_GetAccountStatusGetApi()
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_api_ConsoleAuthService_GetEnterpriseAccount(self, config_obj, AuthEnterpriseApi):
        """  账号中心实名认证 查看企业认证数据
route: prefix=console action=Get... """
        resp = AuthEnterpriseApi.ConsoleAuthService_GetEnterpriseAccountGetApi()
        assert resp.status_code == 200

    @pytest.mark.skip("手动用例")
    def test_api_ConsoleAuthService_SubmitEnterpriseAccount(self, config_obj, AuthApi):
        """  账号中心实名认证 企业提交认证
route: prefix=console action=Submi... """
        with open(os.path.join(config.console_image_path, 'enterprise.png'), 'rb') as f:
            base64_data = base64.b64encode(f.read()).decode('ascii')
        randNam = ''.join(random.sample(string.ascii_letters + string.digits, 3))
        randNum = ''.join(random.sample(string.digits, 3))
        enterprise_account = {
            "enterprise_name": "enterprise_%s" % randNam,
            "enterprise_number": "91350100M%s100Y10" % randNum,
            "enterprise_photo": "%s" % base64_data,
            "enterprise_card_name": "联系人姓名",
            "position": "职位",
            "industry": "INDUSTRY_TYPE_OTHERS",
            "area_name": "中国大陆-北京市-东城区",
            "scenario": "业务场景",
            "end_user": "最终用户",
            "business_inviter": "string"
          }
        phone_code = "1"
        resp = AuthApi.ConsoleAuthService_SubmitEnterpriseAccountPostApi(enterprise_account=enterprise_account, phone_code=phone_code)
        assert resp.status_code == 200

    @pytest.mark.skip("场景用例")
    def test_api_ConsoleAuthService_UpdateEnterpriseAccount(self, config_obj, AuthApi):
        """  账号中心实名认证 企业变更认证
route: prefix=console action=Updat... """
        with open(os.path.join(config.console_image_path, 'enterprise.png'), 'rb') as f:
            base64_data = base64.b64encode(f.read()).decode('ascii')
        randNam = ''.join(random.sample(string.ascii_letters + string.digits, 3))
        randNum = ''.join(random.sample(string.digits, 3))
        enterprise_account = {
            "enterprise_name": "enterprise_%s" % randNam,
            "enterprise_number": "91350100M%s100Y10" % randNum,
            "enterprise_photo": "%s" % base64_data,
            "enterprise_card_name": "联系人姓名",
            "position": "职位",
            "industry": "INDUSTRY_TYPE_OTHERS",
            "area_name": "中国大陆-北京市-东城区",
            "scenario": "业务场景",
            "end_user": "最终用户",
            "business_inviter": "string"
        }
        phone_code = "1"
        resp = AuthApi.ConsoleAuthService_UpdateEnterpriseAccountPostApi(enterprise_account=enterprise_account, phone_code=phone_code)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_api_ConsoleAuthService_GetIndustryInfo(self, config_obj, AuthEnterpriseApi):
        """  账号中心实名认证 获取行业信息
route: prefix=console action=GetIn... """
        resp = AuthEnterpriseApi.ConsoleAuthService_GetIndustryInfoGetApi()
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_api_ConsoleAuthService_GetPersonAccount(self, config_obj, AuthPersonApi):
        """  账号中心实名认证 查看个人认证数据
route: prefix=console action=Get... """
        resp = AuthPersonApi.ConsoleAuthService_GetPersonAccountGetApi()
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        print(ran_str)
        assert resp.status_code == 200

    @pytest.mark.ConsoleRegression
    def test_api_ConsoleAuthService_GetPersonAccountUnRedactedInfo(self, config_obj, AuthPersonApi):
        """  账号中心实名认证 查看个人认证未脱敏数据(姓名或者手机号或者身份证号码)
route: prefix... """
        resp = AuthPersonApi.ConsoleAuthService_GetPersonAccountUnRedactedInfoGetApi()
        assert resp.status_code == 200

    @pytest.mark.skip("手动用例")
    def test_api_ConsoleAuthService_SubmitPersonAccount(self, config_obj, AuthApi):
        """  账号中心实名认证 个人提交认证
route: prefix=console action=Submi... """
        person_account = None
        phone_code = None
        resp = AuthApi.ConsoleAuthService_SubmitPersonAccountPostApi(person_account=person_account, phone_code=phone_code)
        assert resp.status_code == 200

    @pytest.mark.skip("场景用例")
    def test_api_ConsoleAuthService_UpdatePersonAccount(self, config_obj, AuthApi):
        """  账号中心实名认证 个人变更认证
route: prefix=console action=Updat... """
        person_account = None
        phone_code = None
        resp = AuthApi.ConsoleAuthService_UpdatePersonAccountPostApi(person_account=person_account, phone_code=phone_code)
        assert resp.status_code == 200

