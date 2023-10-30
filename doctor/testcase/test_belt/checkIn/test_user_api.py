#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import string
import random

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


@pytest.mark.checkin
class TestUserApi(object):
    """ user Api测试"""

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

    def test_api_ConsoleUserService_OCRIDCard(self, config_obj, UserApiMainUser):
        """  身份张照片识别
route: prefix=console action=OCRIDCard ver... """
        id_card_image = None
        resp = UserApiMainUser.ConsoleUserService_OCRIDCardPostApi(id_card_image=id_card_image)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_ListPolicyGroup(self, config_obj, UserApiMainUser):
        """  策略组列表
route: prefix=console action=ListPolicyGroup... """
        nick_name = None
        description = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = UserApiMainUser.ConsoleUserService_ListPolicyGroupGetApi(nick_name=nick_name, description=description, order=order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_GetPolicyGroupAssociatedInfoByID(self, config_obj, UserApiMainUser):
        """  策略组详情
route: prefix=console action=GetPolicyGroupA... """
        group_id = config_obj.Console.User.testConsoleMainUser.policyGroupId
        resp = UserApiMainUser.ConsoleUserService_GetPolicyGroupAssociatedInfoByIDGetApi(group_id=group_id)
        assert resp.status_code == 200

    @pytest.mark.skip("前端未使用此接口")
    def test_api_ConsoleUserService_GetAllPolicyGroupsByUserID(self, config_obj, UserApiMainUser):
            """  根据user_id获取策略组列表
    route: prefix=console action=GetA... """
            user_id = config_obj.Console.User.testConsoleMainUser.subUserId
            order = "LIST_ORDER_UNSPECIFIED"
            resp = UserApiMainUser.ConsoleUserService_GetAllPolicyGroupsByUserIDGetApi(user_id=user_id, order=order)
            assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleUserService_CreateUserWithAccount(self, config_obj, UserApiMainUser):
        """  portal主用户注册
route: prefix=console action=CreateUse... """
        mode = None
        password = None
        email = None
        phone = None
        code = None
        email_code = None
        resp = UserApiMainUser.ConsoleUserService_CreateUserWithAccountPostApi(mode=mode, password=password, email=email, phone=phone, code=code, email_code=email_code)
        assert resp.status_code == 200

    @pytest.mark.skip("此场景手动测试")
    def test_api_ConsoleUserService_UserLoginForgotPassword(self, config_obj, UserApiMainUser):
        """  portal主用户忘记密码时 用手机号码或者邮箱重置密码操作
route: prefix=conso... """
        mode = None
        password = None
        value = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_UserLoginForgotPasswordPostApi(mode=mode, password=password, value=value, code=code)
        assert resp.status_code == 200

    @pytest.mark.skip("此场景手动测试")
    def test_api_ConsoleUserService_VerifyUserRegisterInfo(self, config_obj, UserApiMainUser):
        """  portal验证邮箱账号、手机号、手机验证码信息
route: prefix=console act... """
        mode = None
        password = None
        value = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_VerifyUserRegisterInfoPostApi(mode=mode, password=password, value=value, code=code)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_GetUserList(self, config_obj, UserApiMainUser):
        """  获取子用户列表
route: prefix=console action=GetUserList v... """
        nick_name = None
        description = None
        blocked = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = UserApiMainUser.ConsoleUserService_GetUserListGetApi(nick_name=nick_name, description=description, blocked=blocked, order=order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleUserService_CreateUser(self, config_obj, UserApiMainUser):
        """  创建子用户
route: prefix=console action=CreateUser vers... """
        nick_name = None
        access_mode = None
        password = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_CreateUserPostApi(nick_name=nick_name, access_mode=access_mode, password=password, code=code)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_UpdateUserAccessMode(self, config_obj, UserApiMainUser):
        """  子用户编辑 包括用户访问方式（编程访问、控制台访问）
route: prefix=console a... """
        user_id = config_obj.Console.User.testConsoleMainUser.subUserId
        access_mode = 3
        code = None
        resp = UserApiMainUser.ConsoleUserService_UpdateUserAccessModePostApi(user_id=user_id, access_mode=access_mode, code=code)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_GetUserAssociatedInfoByID(self, config_obj, UserApiMainUser):
        """  子用户详情包括用户基本信息、所属权限组（用户所拥有的权限组列表）、安全设置（用户所拥有的access... """
        user_id = config_obj.Console.User.testConsoleMainUser.subUserId
        resp = UserApiMainUser.ConsoleUserService_GetUserAssociatedInfoByIDGetApi(user_id=user_id)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_GetUserBaseInfo(self, config_obj, UserApiMainUser):
        """  获取用户基本信息
route: prefix=console action=GetUserBaseI... """
        resp = UserApiMainUser.ConsoleUserService_GetUserBaseInfoGetApi()
        assert resp.status_code == 200

    def test_api_ConsoleUserService_UpdateUserBaseInfo(self, config_obj, UserApiMainUser):
        """  更新用户基本信息 包括昵称
route: prefix=console action=UpdateU... """
        randNum = ''.join(random.sample(string.digits, 5))
        nick_name = "user_4415505853978%s" % randNum
        resp = UserApiMainUser.ConsoleUserService_UpdateUserBaseInfoPostApi(nick_name=nick_name)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_SendSmsCode(self, config_obj, UserApiMainUser):
        """  申请验证码需要填写手机号或者邮箱账号
route: prefix=console action=Se... """
        mode = 1
        value = None
        resp = UserApiMainUser.ConsoleUserService_SendSmsCodeGetApi(mode=mode, value=value)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_VerifySmsCode(self, config_obj, UserApiMainUser):
        """  验证验证码需要填写手机号或者邮箱账号
route: prefix=console action=Ve... """
        mode = 1
        value = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_VerifySmsCodeGetApi(mode=mode, value=value, code=code)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_SendCurrentUserSmsCode(self, config_obj, UserApiMainUser):
        """  申请验证码用当前用户user_id的手机号或者邮箱账号
route: prefix=console ... """
        mode = 1

        resp = UserApiMainUser.ConsoleUserService_SendCurrentUserSmsCodeGetApi(mode=mode)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_VerifyCurrentUserSmsCode(self, config_obj, UserApiMainUser):
        """  验证验证码用当前用户user_id的手机号或者邮箱账号
route: prefix=console ... """
        mode = 1
        code = None
        resp = UserApiMainUser.ConsoleUserService_VerifyCurrentUserSmsCodeGetApi(mode=mode, code=code)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleUserService_UsePhoneOrUserIDDeleteUser(self, config_obj, UserApiMainUser):
        """  用手机号码或者userID删除主用户 """
        user_id = None
        phone = None
        resp = UserApiMainUser.ConsoleUserService_UsePhoneOrUserIDDeleteUserPostApi(user_id=user_id, phone=phone)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_UpdateUserDescInfo(self, config_obj, UserApiMainUser):
        """  子用户编辑 包括用户名称、状态、描述
route: prefix=console action=Up... """
        user_id = config_obj.Console.User.testConsoleMainUser.subUserId
        nick_name = config_obj.Console.User.testConsoleMainUser.subUserName
        description = config_obj.Console.User.testConsoleMainUser.subUserName
        blocked = None
        resp = UserApiMainUser.ConsoleUserService_UpdateUserDescInfoPostApi(user_id=user_id, nick_name=nick_name, description=description, blocked=blocked)
        assert resp.status_code == 200

    @pytest.mark.skip("此场景手动测试")
    def test_api_ConsoleUserService_SecuritySetUpdateUserCellphone(self, config_obj, UserApiMainUser):
        """  安全设置 手机号码修改
route: prefix=console action=SecurityS... """
        phone_code = None
        phone = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_SecuritySetUpdateUserCellphonePostApi(phone_code=phone_code, phone=phone, code=code)
        assert resp.status_code == 200

    @pytest.mark.skip("此场景手动测试")
    def test_api_ConsoleUserService_SecuritySetUpdateUserEmail(self, config_obj, UserApiMainUser):
        """  安全设置 绑定邮箱
route: prefix=console action=SecuritySet... """
        email = "11123@160.com"
        code = None
        resp = UserApiMainUser.ConsoleUserService_SecuritySetUpdateUserEmailPostApi(email=email, code=code)
        assert resp.status_code == 200

    @pytest.mark.skip("此场景手动测试")
    def test_api_ConsoleUserService_SecuritySetUpdateUserPassword(self, config_obj, UserApiMainUser):
        """  安全设置 修改登录密码
route: prefix=console action=SecurityS... """
        mode = None
        password = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_SecuritySetUpdateUserPasswordPostApi(mode=mode, password=password, code=code)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_UpdateSubUserPassword(self, config_obj, UserApiMainUser):
        """  子用户编辑 更新子用户密码
route: prefix=console action=UpdateS... """
        user_id = config_obj.Console.User.testConsoleMainUser.subUserId
        password = "123456qw"
        resp = UserApiMainUser.ConsoleUserService_UpdateSubUserPasswordPostApi(user_id=user_id, password=password)
        assert resp.status_code == 200

    @pytest.mark.skip("前端未使用此接口")
    def test_api_ConsoleUserService_GetUserUnRedactedInfo(self, config_obj, UserApiMainUser):
        """  获取用户未脱敏的基本信息(电话或者邮箱)
route: prefix=console action=... """
        mode = None
        user_id = None
        resp = UserApiMainUser.ConsoleUserService_GetUserUnRedactedInfoGetApi(mode=mode, user_id=user_id)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleUserService_DeleteUser(self, config_obj, UserApiMainUser):
        """  子用户删除
route: prefix=console action=DeleteUser vers... """
        user_id = None
        code = None
        force = None
        resp = UserApiMainUser.ConsoleUserService_DeleteUserPostApi(user_id=user_id, code=code, force=force)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleUserService_CreateUserAKSK(self, config_obj, UserApiMainUser):
        """  子用户新增访问密钥
route: prefix=console action=CreateUserA... """
        user_id = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_CreateUserAKSKPostApi(user_id=user_id, code=code)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleUserService_DeleteAccessKey(self, config_obj, UserApiMainUser):
        """  子用户移除访问密钥
route: prefix=console action=DeleteAcces... """
        user_id = None
        access_key_id = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_DeleteAccessKeyPostApi(user_id=user_id, access_key_id=access_key_id, code=code)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleUserService_ExportUserAKSKExcel(self, config_obj, UserApiMainUser):
        """  将aksk信息导出为excel文件
route: prefix=console action=Exp... """
        user_id = None
        access_key_id = None
        resp = UserApiMainUser.ConsoleUserService_ExportUserAKSKExcelPostApi(user_id=user_id, access_key_id=access_key_id)
        assert resp.status_code == 200

    @pytest.mark.skip("post接口，暂时先跳过，会写在scenario")
    def test_api_ConsoleUserService_SetAccessKeyStatus(self, config_obj, UserApiMainUser):
        """  设置子用户aksk状态
route: prefix=console action=SetAccess... """
        user_id = None
        access_key_id = None
        blocked = None
        resp = UserApiMainUser.ConsoleUserService_SetAccessKeyStatusPostApi(user_id=user_id, access_key_id=access_key_id, blocked=blocked)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_BatchAddPolicyGroupToUser(self, config_obj, UserApiMainUser):
        """  批量授权子用户权限组
route: prefix=console action=BatchAddPo... """
        user_id = config_obj.Console.User.testConsoleMainUser.subUserId
        group_id_list = [config_obj.Console.User.testConsoleMainUser.policyGroupId]
        resp = UserApiMainUser.ConsoleUserService_BatchAddPolicyGroupToUserPostApi(user_id=user_id, group_id_list=group_id_list)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_RemovePolicyGroupFromUser(self, config_obj, UserApiMainUser):
        """  用户移除授权权限组
route: prefix=console action=RemovePolic... """
        group_id = config_obj.Console.User.testConsoleMainUser.policyGroupId
        user_id = config_obj.Console.User.testConsoleMainUser.subUserId
        code = None
        resp = UserApiMainUser.ConsoleUserService_RemovePolicyGroupFromUserPostApi(group_id=group_id, user_id=user_id, code=code)
        assert resp.status_code == 200

    def test_api_ConsoleUserService_UserNameExistInAccount(self, config_obj, UserApiMainUser):
        """  查询创建的新子用户名称是否已经存在
route: prefix=console action=Use... """
        user_name = config_obj.Console.User.testConsoleMainUser.subUserName
        resp = UserApiMainUser.ConsoleUserService_UserNameExistInAccountPostApi(user_name=user_name)
        assert resp.status_code == 200