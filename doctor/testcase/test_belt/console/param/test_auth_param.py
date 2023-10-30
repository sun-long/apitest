#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestAuthParam(object):
    """ auth Param测试"""

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
    ])
    def test_api_ConsoleAuthService_GetAccountInfoInvalidParam(self, invalidParam, config_obj, AuthApi):
        """  获取当前账户的信息 包含账户是否被禁用 是否开启后付费
route: prefix=console ... """
        intef = AuthApi.ConsoleAuthService_GetAccountInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ConsoleAuthService_GetAccountStatusInvalidParam(self, invalidParam, config_obj, AuthApi):
        """  账号中心实名认证 获取认证结果
route: prefix=console action=GetAc... """
        intef = AuthApi.ConsoleAuthService_GetAccountStatusGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ConsoleAuthService_GetEnterpriseAccountInvalidParam(self, invalidParam, config_obj, AuthApi):
        """  账号中心实名认证 查看企业认证数据
route: prefix=console action=Get... """
        intef = AuthApi.ConsoleAuthService_GetEnterpriseAccountGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('enterprise_account', 'invalidenterprise_account'),
        ('enterprise_account', ''),
        ('enterprise_account', None),
        ('phone_code', 'invalidphone_code'),
        ('phone_code', ''),
        ('phone_code', None),
    ])
    def test_api_ConsoleAuthService_SubmitEnterpriseAccountInvalidParam(self, invalidParam, config_obj, AuthApi):
        """  账号中心实名认证 企业提交认证
route: prefix=console action=Submi... """
        enterprise_account = None
        phone_code = None
        intef = AuthApi.ConsoleAuthService_SubmitEnterpriseAccountPostApi(enterprise_account=enterprise_account, phone_code=phone_code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('enterprise_account', 'invalidenterprise_account'),
        ('enterprise_account', ''),
        ('enterprise_account', None),
        ('phone_code', 'invalidphone_code'),
        ('phone_code', ''),
        ('phone_code', None),
    ])
    def test_api_ConsoleAuthService_UpdateEnterpriseAccountInvalidParam(self, invalidParam, config_obj, AuthApi):
        """  账号中心实名认证 企业变更认证
route: prefix=console action=Updat... """
        enterprise_account = None
        phone_code = None
        intef = AuthApi.ConsoleAuthService_UpdateEnterpriseAccountPostApi(enterprise_account=enterprise_account, phone_code=phone_code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ConsoleAuthService_GetIndustryInfoInvalidParam(self, invalidParam, config_obj, AuthApi):
        """  账号中心实名认证 获取行业信息
route: prefix=console action=GetIn... """
        intef = AuthApi.ConsoleAuthService_GetIndustryInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ConsoleAuthService_GetPersonAccountInvalidParam(self, invalidParam, config_obj, AuthApi):
        """  账号中心实名认证 查看个人认证数据
route: prefix=console action=Get... """
        intef = AuthApi.ConsoleAuthService_GetPersonAccountGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('person_account', 'invalidperson_account'),
        ('person_account', ''),
        ('person_account', None),
        ('phone_code', 'invalidphone_code'),
        ('phone_code', ''),
        ('phone_code', None),
    ])
    def test_api_ConsoleAuthService_SubmitPersonAccountInvalidParam(self, invalidParam, config_obj, AuthApi):
        """  账号中心实名认证 个人提交认证
route: prefix=console action=Submi... """
        person_account = None
        phone_code = None
        intef = AuthApi.ConsoleAuthService_SubmitPersonAccountPostApi(person_account=person_account, phone_code=phone_code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('person_account', 'invalidperson_account'),
        ('person_account', ''),
        ('person_account', None),
        ('phone_code', 'invalidphone_code'),
        ('phone_code', ''),
        ('phone_code', None),
    ])
    def test_api_ConsoleAuthService_UpdatePersonAccountInvalidParam(self, invalidParam, config_obj, AuthApi):
        """  账号中心实名认证 个人变更认证
route: prefix=console action=Updat... """
        person_account = None
        phone_code = None
        intef = AuthApi.ConsoleAuthService_UpdatePersonAccountPostApi(person_account=person_account, phone_code=phone_code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
