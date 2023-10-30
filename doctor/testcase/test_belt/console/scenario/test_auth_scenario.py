#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import base64
import os
import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestAuthScenario(object):
    """ Auth scenario test"""

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
    def test_scenario_000_enterprise_update_success(self, config_obj, AuthEnterpriseApi, AuthinternalauthApi):
        """ 企业实名认证变更"""
        #1、查看企业认证数据
        resp = AuthEnterpriseApi.ConsoleAuthService_GetEnterpriseAccountGetApi()
        assert resp.status_code == 200

        #2、企业实名认证变更
        position = "position"
        enterprise_account = {
            "enterprise_card_name": "changeName",
            "position": position,
            "industry": "INDUSTRY_TYPE_OTHERS",
            "area_name": "中国大陆-北京市-东城区",
            "scenario": "业务场景",
            "end_user": "最终用户",
            "business_inviter": "string"
        }
        phone_code = "1"
        resp = AuthEnterpriseApi.ConsoleAuthService_UpdateEnterpriseAccountPostApi(enterprise_account=enterprise_account,
                                                                         phone_code=phone_code)
        assert resp.status_code == 200

        #3、运营后台审核通过
        account_id = config_obj.Console.User.testEnterprise.account_id
        audit_at = int(time.time())
        status = "ACCOUNT_STATUS_SUCCEEDED"
        audit_desc = "success"
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountStatusPostApi(account_id=account_id,
                                                                                              audit_at=audit_at,
                                                                                              status=status,
                                                                                              audit_desc=audit_desc)
        assert resp.status_code == 200
        #4、查看变更校验
        resp = AuthEnterpriseApi.ConsoleAuthService_GetEnterpriseAccountGetApi()
        assert resp.json_get("enterprise_account.position") == position

    @pytest.mark.ConsoleRegression
    @pytest.mark.Skiponline
    def test_scenario_001_person_update_success(self, config_obj, AuthPersonApi, AuthinternalauthApi):
        """ 个人实名认证变更"""
        #1、查看个人认证数据
        resp = AuthPersonApi.ConsoleAuthService_GetPersonAccountUnRedactedInfoGetApi()
        assert resp.status_code == 200

        #2、个人实名认证变更
        with open(os.path.join(config.console_image_path, 'idcardFront.jpg'), 'rb') as f:
            base64_data_front = base64.b64encode(f.read()).decode('ascii')
       # with open(os.path.join(config.console_image_path, 'enterprise.png'), 'rb') as f:
            base64_data_back = base64.b64encode(f.read()).decode('ascii')
        person_name = "仲大力"
        person_card_number = "142128196307028537"

        person_account = {
            "person_name": person_name,
            "person_card_type": "IDCREDENTIAL_TYPE_IDCARD",
            "person_card_number": person_card_number,
            "person_card_photo1": base64_data_front,
            #"person_card_photo2": base64_data_back,
        }
        phone_code = "1"
        resp = AuthPersonApi.ConsoleAuthService_UpdatePersonAccountPostApi(person_account=person_account,
                                                                     phone_code=phone_code)
        assert resp.status_code == 200

        #3、查看变更校验
        resp = AuthPersonApi.ConsoleAuthService_GetPersonAccountGetApi()
        assert resp.json_get("person_account.person_card_number")[0:3] == person_card_number[0:3]
        assert resp.json_get("person_account.person_card_number")[-1:-4] == person_card_number[-1:-4]
        assert resp.json_get("person_account.person_name")[-1] == person_name[-1]
