#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


@pytest.mark.checkin
class TestAuthinternalauthApi(object):
    """ authInternalAuth Api测试"""

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

    def test_api_ConsoleInternalAuthService_AdminGetPhoneOrEmailByAccountID(self, config_obj, AuthinternalauthApi):
        """  超级管理员获取单个账户的真实手机号码或者邮箱账号
route: prefix=console-int... """
        account_id = config_obj.Console.User.internalTestUser.testAccountId
        mode = 0
        code = '1212'
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetPhoneOrEmailByAccountIDGetApi(account_id=account_id, mode=mode, code=code)
        assert resp.status_code == 200
        assert resp.json_get("email") is not None

    def test_api_ConsoleInternalAuthService_AdminGetAccountList(self, config_obj, AuthinternalauthApi):
        """  超级管理员获取账户列表
route: prefix=console-internal action=... """
        account_name = None
        account_type = None
        status = None
        business_status = None
        account_id = None
        user_id = None
        user_name = None
        enterprise_name = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetAccountListGetApi(account_name=account_name, account_type=account_type, status=status, business_status=business_status, account_id=account_id, user_id=user_id, user_name=user_name, enterprise_name=enterprise_name, order=order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200
        assert len(resp.json_get("account_info")) > 1

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleInternalAuthService_AdminUpdateAccount(self, config_obj, AuthinternalauthApi):
        """  超级管理员更新付费模式、账户的启用和禁用状态
route: prefix=console-inter... """
        account_id = None
        update_mode = None
        account_used_status = None
        payment_type = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountPostApi(account_id=account_id, update_mode=update_mode, account_used_status=account_used_status, payment_type=payment_type)
        assert resp.status_code == 200

    def test_api_ConsoleInternalAuthService_AdminGetEnterpriseAccount(self, config_obj, AuthinternalauthApi):
        """  超级管理员获取单账号审核认证数据
route: prefix=console-internal ac... """
        account_id = config_obj.Console.User.internalTestUser.testAccountId
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetEnterpriseAccountGetApi(account_id=account_id)
        assert resp.status_code == 200

    @pytest.mark.skip("前端未使用此接口")
    def test_api_ConsoleInternalAuthService_AdminGetEnterpriseAccountUnRedactedInfo(self, config_obj, AuthinternalauthApi):
        """  超级管理员获取单账号审核认证未脱敏数据(姓名或者手机号)
route: prefix=console... """
        mode = None
        account_id = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetEnterpriseAccountUnRedactedInfoGetApi(mode=mode, account_id=account_id)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleInternalAuthService_AdminUpdateAccountStatus(self, config_obj, AuthinternalauthApi):
        """  超级管理员认证审核
route: prefix=console-internal action=Ad... """
        account_id = None
        audit_at = None
        status = None
        audit_desc = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountStatusPostApi(account_id=account_id, audit_at=audit_at, status=status, audit_desc=audit_desc)
        assert resp.status_code == 200

    def test_api_ConsoleInternalAuthService_AdminBusinessAssignment(self, config_obj, AuthinternalauthApi):
        """  超级管理员分配商务
route: prefix=console-internal action=Ad... """
        account_id = config_obj.Console.User.internalTestUser.testAccountId
        business_department = 'zhaodl department'
        business_name = 'zhaodl'
        business_code = '21212'
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminBusinessAssignmentPostApi(account_id=account_id, business_department=business_department, business_name=business_name, business_code=business_code)
        assert resp.status_code == 200

    def test_api_ConsoleInternalAuthService_AdminGetIndustryInfo(self, config_obj, AuthinternalauthApi):
        """  超级管理员获取行业信息
route: prefix=console action=AdminGetI... """
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetIndustryInfoGetApi()
        assert resp.status_code == 200

    def test_api_ConsoleInternalAuthService_AdminGetAccountUserList(self, config_obj, AuthinternalauthApi):
        """  系统工具 超级管理员用户管理
route: prefix=console-internal acti... """
        user_id = None
        user_name = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetAccountUserListGetApi(user_id=user_id, user_name=user_name, order=order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

        assert len(resp.json_get("account_user_info")) > 1

    def test_api_ConsoleInternalAuthService_AdminGetCostManagementAccountList(self, config_obj, AuthinternalauthApi):
        """  超级管理员获取费用管理账户列表
route: prefix=console-internal act... """
        account_type = None
        account_id = None
        user_id = None
        user_name = None
        enterprise_name = None
        account_level = None
        only_view_unprocessed_records_accounts = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetCostManagementAccountListGetApi(account_type=account_type, account_id=account_id, user_id=user_id, user_name=user_name, enterprise_name=enterprise_name, account_level=account_level, only_view_unprocessed_records_accounts=only_view_unprocessed_records_accounts, order=order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    def test_api_ConsoleInternalAuthService_AdminGetInquiryAccountList(self, config_obj, AuthinternalauthApi):
        """  超级管理员获取账户查询列表
route: prefix=console-internal actio... """
        account_type = None
        account_id = None
        user_id = None
        user_name = None
        enterprise_name = None
        only_view_pending_change_accounts = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetInquiryAccountListGetApi(account_type=account_type, account_id=account_id, user_id=user_id, user_name=user_name, enterprise_name=enterprise_name, only_view_pending_change_accounts=only_view_pending_change_accounts, order=order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    def test_api_ConsoleInternalAuthService_AdminListPolicyGroup(self, config_obj, AuthinternalauthApi):
        """  系统工具 超级管理员策略组列表
route: prefix=console-internal act... """
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminListPolicyGroupGetApi()
        assert resp.status_code == 200

    def test_api_ConsoleInternalAuthService_AdminGetAllPolicyGroupsByUserID(self, config_obj, AuthinternalauthApi):
        """  系统工具 超级管理员根据user_id获取策略组列表
route: prefix=console-i... """
        user_id = config_obj.Console.User.internalTestUser.testUserId
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetAllPolicyGroupsByUserIDGetApi(user_id=user_id)
        assert resp.status_code == 200

    @pytest.mark.skip("前端未用到此接口")
    def test_api_ConsoleInternalAuthService_CreateInternalUserWithAccount(self, config_obj, AuthinternalauthApi):
        """  运营后台主用户注册
route: prefix=console action=CreateInter... """
        email = None
        phone = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_CreateInternalUserWithAccountPostApi(email=email, phone=phone)
        assert resp.status_code == 200

    def test_api_ConsoleInternalAuthService_AdminGetUserBaseInfo(self, config_obj, AuthinternalauthApi):
        """  超级管理员获取用户基本信息
route: prefix=console-internal actio... """
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminGetUserBaseInfoGetApi()
        assert resp.status_code == 200
        assert resp.json_get("user_name") is not None


    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleInternalAuthService_ConsoleInternalUpdateUserCellphone(self, config_obj, AuthinternalauthApi):
        """  运营后台手机号码修改
route: prefix=console action=ConsoleInt... """
        phone = '13693108787'
        code = 1
        resp = AuthinternalauthApi.ConsoleInternalAuthService_ConsoleInternalUpdateUserCellphonePostApi(phone=phone, code=code)
        assert resp.status_code == 200

    @pytest.mark.skip("post 接口写在场景用例中")
    def test_api_ConsoleInternalAuthService_AdminSendSmsCode(self, config_obj, AuthinternalauthApi):
        """  运营后台申请验证码需要填写手机号或者邮箱账号
route: prefix=console actio... """
        mode = None
        value = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminSendSmsCodeGetApi(mode=mode, value=value)
        assert resp.status_code == 200

    @pytest.mark.skip("post 接口写在场景用例中")
    def test_api_ConsoleInternalAuthService_AdminVerifySmsCode(self, config_obj, AuthinternalauthApi):
        """  运营后台验证验证码需要填写手机号或者邮箱账号
route: prefix=console actio... """
        mode = None
        value = None
        code = None
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminVerifySmsCodeGetApi(mode=mode, value=value, code=code)
        assert resp.status_code == 200

    def test_api_ConsoleInternalAuthService_SendCurrentAdminUserSmsCode(self, config_obj, AuthinternalauthApi):
        """  申请验证码用当前超级管理员用户user_id的手机号或者邮箱账号
route: prefix=con... """
        mode = 1
        resp = AuthinternalauthApi.ConsoleInternalAuthService_SendCurrentAdminUserSmsCodeGetApi(mode=mode)
        assert resp.status_code == 200

    def test_api_ConsoleInternalAuthService_VerifyCurrentAdminUserSmsCode(self, config_obj, AuthinternalauthApi):
        """  运营后台验证验证码用当前用户user_id的手机号或者邮箱账号
route: prefix=cons... """
        mode = 1
        code = 1212
        resp = AuthinternalauthApi.ConsoleInternalAuthService_VerifyCurrentAdminUserSmsCodeGetApi(mode=mode, code=code)
        assert resp.status_code == 200

    #@pytest.mark.skip("post接口在场景用例中实现")
    def test_api_ConsoleInternalAuthService_AdminBatchAddPolicyGroupToUser(self, config_obj, AuthinternalauthApi):
        """  系统工具 超级管理员批量授权子用户权限组
route: prefix=console-interna... """
        user_id = config_obj.Console.User.internalTestUser.testUserId
        group_id_list = config_obj.Console.User.internalTestUser.group_id_list
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminBatchAddPolicyGroupToUserPostApi(user_id=user_id, group_id_list=group_id_list)
        assert resp.status_code == 200

