#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestUserParam(object):
    """ user Param测试"""

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
        ('id_card_image', 'invalidid_card_image'),
        ('id_card_image', ''),
        ('id_card_image', None),
    ])
    def test_api_ConsoleUserService_OCRIDCardInvalidParam(self, invalidParam, config_obj, UserApi):
        """  身份张照片识别
route: prefix=console action=OCRIDCard ver... """
        id_card_image = None
        intef = UserApi.ConsoleUserService_OCRIDCardPostApi(id_card_image=id_card_image, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('nick_name', 'invalidnick_name'),
        ('nick_name', ''),
        ('nick_name', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('order', 'invalidorder'),
        ('order', ''),
        ('order', None),
        ('page_request_offset', 'invalidpage_request_offset'),
        ('page_request_offset', ''),
        ('page_request_offset', None),
        ('page_request_limit', 'invalidpage_request_limit'),
        ('page_request_limit', ''),
        ('page_request_limit', None),
        ('page_request_total', 'invalidpage_request_total'),
        ('page_request_total', ''),
        ('page_request_total', None),
    ])
    def test_api_ConsoleUserService_ListPolicyGroupInvalidParam(self, invalidParam, config_obj, UserApi):
        """  策略组列表
route: prefix=console action=ListPolicyGroup... """
        nick_name = None
        description = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = UserApi.ConsoleUserService_ListPolicyGroupGetApi(nick_name=nick_name, description=description, order=order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
    ])
    def test_api_ConsoleUserService_GetPolicyGroupAssociatedInfoByIDInvalidParam(self, invalidParam, config_obj, UserApi):
        """  策略组详情
route: prefix=console action=GetPolicyGroupA... """
        group_id = None
        intef = UserApi.ConsoleUserService_GetPolicyGroupAssociatedInfoByIDGetApi(group_id=group_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('password', 'invalidpassword'),
        ('password', ''),
        ('password', None),
        ('email', 'invalidemail'),
        ('email', ''),
        ('email', None),
        ('phone', 'invalidphone'),
        ('phone', ''),
        ('phone', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
        ('email_code', 'invalidemail_code'),
        ('email_code', ''),
        ('email_code', None),
    ])
    def test_api_ConsoleUserService_CreateUserWithAccountInvalidParam(self, invalidParam, config_obj, UserApi):
        """  portal主用户注册
route: prefix=console action=CreateUse... """
        mode = None
        password = None
        email = None
        phone = None
        code = None
        email_code = None
        intef = UserApi.ConsoleUserService_CreateUserWithAccountPostApi(mode=mode, password=password, email=email, phone=phone, code=code, email_code=email_code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('password', 'invalidpassword'),
        ('password', ''),
        ('password', None),
        ('value', 'invalidvalue'),
        ('value', ''),
        ('value', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_UserLoginForgotPasswordInvalidParam(self, invalidParam, config_obj, UserApi):
        """  portal主用户忘记密码时 用手机号码或者邮箱重置密码操作
route: prefix=conso... """
        mode = None
        password = None
        value = None
        code = None
        intef = UserApi.ConsoleUserService_UserLoginForgotPasswordPostApi(mode=mode, password=password, value=value, code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('password', 'invalidpassword'),
        ('password', ''),
        ('password', None),
        ('value', 'invalidvalue'),
        ('value', ''),
        ('value', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_VerifyUserRegisterInfoInvalidParam(self, invalidParam, config_obj, UserApi):
        """  portal验证邮箱账号、手机号、手机验证码信息
route: prefix=console act... """
        mode = None
        password = None
        value = None
        code = None
        intef = UserApi.ConsoleUserService_VerifyUserRegisterInfoPostApi(mode=mode, password=password, value=value, code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('nick_name', 'invalidnick_name'),
        ('nick_name', ''),
        ('nick_name', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('blocked', 'invalidblocked'),
        ('blocked', ''),
        ('blocked', None),
        ('order', 'invalidorder'),
        ('order', ''),
        ('order', None),
        ('page_request_offset', 'invalidpage_request_offset'),
        ('page_request_offset', ''),
        ('page_request_offset', None),
        ('page_request_limit', 'invalidpage_request_limit'),
        ('page_request_limit', ''),
        ('page_request_limit', None),
        ('page_request_total', 'invalidpage_request_total'),
        ('page_request_total', ''),
        ('page_request_total', None),
    ])
    def test_api_ConsoleUserService_GetUserListInvalidParam(self, invalidParam, config_obj, UserApi):
        """  获取子用户列表
route: prefix=console action=GetUserList v... """
        nick_name = None
        description = None
        blocked = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = UserApi.ConsoleUserService_GetUserListGetApi(nick_name=nick_name, description=description, blocked=blocked, order=order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('nick_name', 'invalidnick_name'),
        ('nick_name', ''),
        ('nick_name', None),
        ('access_mode', 'invalidaccess_mode'),
        ('access_mode', ''),
        ('access_mode', None),
        ('password', 'invalidpassword'),
        ('password', ''),
        ('password', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_CreateUserInvalidParam(self, invalidParam, config_obj, UserApi):
        """  创建子用户
route: prefix=console action=CreateUser vers... """
        nick_name = None
        access_mode = None
        password = None
        code = None
        intef = UserApi.ConsoleUserService_CreateUserPostApi(nick_name=nick_name, access_mode=access_mode, password=password, code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('access_mode', 'invalidaccess_mode'),
        ('access_mode', ''),
        ('access_mode', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_UpdateUserAccessModeInvalidParam(self, invalidParam, config_obj, UserApi):
        """  子用户编辑 包括用户访问方式（编程访问、控制台访问）
route: prefix=console a... """
        user_id = None
        access_mode = None
        code = None
        intef = UserApi.ConsoleUserService_UpdateUserAccessModePostApi(user_id=user_id, access_mode=access_mode, code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
    ])
    def test_api_ConsoleUserService_GetUserAssociatedInfoByIDInvalidParam(self, invalidParam, config_obj, UserApi):
        """  子用户详情包括用户基本信息、所属权限组（用户所拥有的权限组列表）、安全设置（用户所拥有的access... """
        user_id = None
        intef = UserApi.ConsoleUserService_GetUserAssociatedInfoByIDGetApi(user_id=user_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ConsoleUserService_GetUserBaseInfoInvalidParam(self, invalidParam, config_obj, UserApi):
        """  获取用户基本信息
route: prefix=console action=GetUserBaseI... """
        intef = UserApi.ConsoleUserService_GetUserBaseInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('nick_name', 'invalidnick_name'),
        ('nick_name', ''),
        ('nick_name', None),
    ])
    def test_api_ConsoleUserService_UpdateUserBaseInfoInvalidParam(self, invalidParam, config_obj, UserApi):
        """  更新用户基本信息 包括昵称
route: prefix=console action=UpdateU... """
        nick_name = None
        intef = UserApi.ConsoleUserService_UpdateUserBaseInfoPostApi(nick_name=nick_name, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('value', 'invalidvalue'),
        ('value', ''),
        ('value', None),
    ])
    def test_api_ConsoleUserService_SendSmsCodeInvalidParam(self, invalidParam, config_obj, UserApi):
        """  申请验证码需要填写手机号或者邮箱账号
route: prefix=console action=Se... """
        mode = None
        value = None
        intef = UserApi.ConsoleUserService_SendSmsCodeGetApi(mode=mode, value=value, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('value', 'invalidvalue'),
        ('value', ''),
        ('value', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_VerifySmsCodeInvalidParam(self, invalidParam, config_obj, UserApi):
        """  验证验证码需要填写手机号或者邮箱账号
route: prefix=console action=Ve... """
        mode = None
        value = None
        code = None
        intef = UserApi.ConsoleUserService_VerifySmsCodeGetApi(mode=mode, value=value, code=code, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
    ])
    def test_api_ConsoleUserService_SendCurrentUserSmsCodeInvalidParam(self, invalidParam, config_obj, UserApi):
        """  申请验证码用当前用户user_id的手机号或者邮箱账号
route: prefix=console ... """
        mode = None
        intef = UserApi.ConsoleUserService_SendCurrentUserSmsCodeGetApi(mode=mode, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_VerifyCurrentUserSmsCodeInvalidParam(self, invalidParam, config_obj, UserApi):
        """  验证验证码用当前用户user_id的手机号或者邮箱账号
route: prefix=console ... """
        mode = None
        code = None
        intef = UserApi.ConsoleUserService_VerifyCurrentUserSmsCodeGetApi(mode=mode, code=code, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('phone', 'invalidphone'),
        ('phone', ''),
        ('phone', None),
    ])
    def test_api_ConsoleUserService_UsePhoneOrUserIDDeleteUserInvalidParam(self, invalidParam, config_obj, UserApi):
        """  用手机号码或者userID删除主用户 """
        user_id = None
        phone = None
        intef = UserApi.ConsoleUserService_UsePhoneOrUserIDDeleteUserPostApi(user_id=user_id, phone=phone, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('nick_name', 'invalidnick_name'),
        ('nick_name', ''),
        ('nick_name', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('blocked', 'invalidblocked'),
        ('blocked', ''),
        ('blocked', None),
    ])
    def test_api_ConsoleUserService_UpdateUserDescInfoInvalidParam(self, invalidParam, config_obj, UserApi):
        """  子用户编辑 包括用户名称、状态、描述
route: prefix=console action=Up... """
        user_id = None
        nick_name = None
        description = None
        blocked = None
        intef = UserApi.ConsoleUserService_UpdateUserDescInfoPostApi(user_id=user_id, nick_name=nick_name, description=description, blocked=blocked, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('phone_code', 'invalidphone_code'),
        ('phone_code', ''),
        ('phone_code', None),
        ('phone', 'invalidphone'),
        ('phone', ''),
        ('phone', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_SecuritySetUpdateUserCellphoneInvalidParam(self, invalidParam, config_obj, UserApi):
        """  安全设置 手机号码修改
route: prefix=console action=SecurityS... """
        phone_code = None
        phone = None
        code = None
        intef = UserApi.ConsoleUserService_SecuritySetUpdateUserCellphonePostApi(phone_code=phone_code, phone=phone, code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('email', 'invalidemail'),
        ('email', ''),
        ('email', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_SecuritySetUpdateUserEmailInvalidParam(self, invalidParam, config_obj, UserApi):
        """  安全设置 绑定邮箱
route: prefix=console action=SecuritySet... """
        email = None
        code = None
        intef = UserApi.ConsoleUserService_SecuritySetUpdateUserEmailPostApi(email=email, code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('password', 'invalidpassword'),
        ('password', ''),
        ('password', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_SecuritySetUpdateUserPasswordInvalidParam(self, invalidParam, config_obj, UserApi):
        """  安全设置 修改登录密码
route: prefix=console action=SecurityS... """
        mode = None
        password = None
        code = None
        intef = UserApi.ConsoleUserService_SecuritySetUpdateUserPasswordPostApi(mode=mode, password=password, code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('password', 'invalidpassword'),
        ('password', ''),
        ('password', None),
    ])
    def test_api_ConsoleUserService_UpdateSubUserPasswordInvalidParam(self, invalidParam, config_obj, UserApi):
        """  子用户编辑 更新子用户密码
route: prefix=console action=UpdateS... """
        user_id = None
        password = None
        intef = UserApi.ConsoleUserService_UpdateSubUserPasswordPostApi(user_id=user_id, password=password, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
        ('force', 'invalidforce'),
        ('force', ''),
        ('force', None),
    ])
    def test_api_ConsoleUserService_DeleteUserInvalidParam(self, invalidParam, config_obj, UserApi):
        """  子用户删除
route: prefix=console action=DeleteUser vers... """
        user_id = None
        code = None
        force = None
        intef = UserApi.ConsoleUserService_DeleteUserPostApi(user_id=user_id, code=code, force=force, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_CreateUserAKSKInvalidParam(self, invalidParam, config_obj, UserApi):
        """  子用户新增访问密钥
route: prefix=console action=CreateUserA... """
        user_id = None
        code = None
        intef = UserApi.ConsoleUserService_CreateUserAKSKPostApi(user_id=user_id, code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('access_key_id', 'invalidaccess_key_id'),
        ('access_key_id', ''),
        ('access_key_id', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_DeleteAccessKeyInvalidParam(self, invalidParam, config_obj, UserApi):
        """  子用户移除访问密钥
route: prefix=console action=DeleteAcces... """
        user_id = None
        access_key_id = None
        code = None
        intef = UserApi.ConsoleUserService_DeleteAccessKeyPostApi(user_id=user_id, access_key_id=access_key_id, code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('group_id_list', 'invalidgroup_id_list'),
        ('group_id_list', ''),
        ('group_id_list', None),
    ])
    def test_api_ConsoleUserService_BatchAddPolicyGroupToUserInvalidParam(self, invalidParam, config_obj, UserApi):
        """  批量授权子用户权限组
route: prefix=console action=BatchAddPo... """
        user_id = None
        group_id_list = None
        intef = UserApi.ConsoleUserService_BatchAddPolicyGroupToUserPostApi(user_id=user_id, group_id_list=group_id_list, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('group_id', 'invalidgroup_id'),
        ('group_id', ''),
        ('group_id', None),
        ('user_id', 'invaliduser_id'),
        ('user_id', ''),
        ('user_id', None),
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_ConsoleUserService_RemovePolicyGroupFromUserInvalidParam(self, invalidParam, config_obj, UserApi):
        """  用户移除授权权限组
route: prefix=console action=RemovePolic... """
        group_id = None
        user_id = None
        code = None
        intef = UserApi.ConsoleUserService_RemovePolicyGroupFromUserPostApi(group_id=group_id, user_id=user_id, code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_name', 'invaliduser_name'),
        ('user_name', ''),
        ('user_name', None),
    ])
    def test_api_ConsoleUserService_UserNameExistInAccountInvalidParam(self, invalidParam, config_obj, UserApi):
        """  查询创建的新子用户名称是否已经存在
route: prefix=console action=Use... """
        user_name = None
        intef = UserApi.ConsoleUserService_UserNameExistInAccountPostApi(user_name=user_name, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
