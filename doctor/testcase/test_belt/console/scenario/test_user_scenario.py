#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import base64
import os
import time
from datetime import datetime, date, timedelta
from io import BytesIO
import pandas as pd

import pytest

from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
from commonlib.sign_utils import encode_jwt_token
from defines.belt.authiam_service_business import AuthiamSwaggerBusiness

"""
覆盖接口：
1.

"""


# class DeleteSubUser():
#     def deleteUser(self, UserApiMainUser):
#         UserApiMainUser.ConsoleUserService_DeleteUserPostApi(user_id=self.user_id, code=None, force=None)
#


@pytest.mark.ConsoleRegression
class TestUserScenario(object):
    """ User scenario test"""

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

    def test_scenario_001_UpdateNickName(self, UserApiMainUser):
        """ 账号中心修改昵称"""
        """
            1.查询信息
            2.修改nick_name
            3.再次查询信息，验证nick_name修改成功
        """
        resp = UserApiMainUser.ConsoleUserService_GetUserBaseInfoGetApi()
        assert resp.status_code == 200
        old_nick_name = resp.json_get("nick_name")

        new_nick_name = "new_nick_name_%s" % sign_utils.getUuid(5)
        resp = UserApiMainUser.ConsoleUserService_UpdateUserBaseInfoPostApi(nick_name=new_nick_name)
        assert resp.status_code == 200

        resp = UserApiMainUser.ConsoleUserService_GetUserBaseInfoGetApi()
        assert resp.status_code == 200
        assert resp.json_get("nick_name") == new_nick_name, "更新nick_name失败."

        resp = UserApiMainUser.ConsoleUserService_UpdateUserBaseInfoPostApi(nick_name=old_nick_name)
        assert resp.status_code == 200

        resp = UserApiMainUser.ConsoleUserService_GetUserBaseInfoGetApi()
        assert resp.status_code == 200
        assert resp.json_get("nick_name") == old_nick_name, "恢复nick_name失败."

    def test_scenarioo_002_modifySubUserType(self, UserApiMainUser):
        """ 修改子账号，校验子账户类型以及子账户和aksk状态"""
        # 创建编程访问子账号
        nick_name = "autoTestSubUser1"
        # access_mode （1编程访问，2控制台访问，3编程+控制台，0子账失效）
        access_mode = 1
        password = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_CreateUserPostApi(nick_name=nick_name, access_mode=access_mode,
                                                                    password=password, code=code)
        user_id = resp.json["user_id"]
        print('user_id {}'.format(user_id))
        assert resp.status_code == 200

        # 查询子账号
        resp = UserApiMainUser.ConsoleUserService_GetUserListGetApi(nick_name=nick_name)
        assert resp.status_code == 200
        assert len(resp.json["list"]) == 1

        # 修改子账号描述
        description = "autoTestSubUser"
        resp = UserApiMainUser.ConsoleUserService_UpdateUserDescInfoPostApi(user_id=user_id, nick_name=nick_name,
                                                                            description=description)
        assert resp.status_code == 200

        # 修改子账号类型
        # 编程访问改成控制台访问
        access_mode = 2
        resp = UserApiMainUser.ConsoleUserService_UpdateUserAccessModePostApi(user_id=user_id, access_mode=access_mode,
                                                                              code=code)
        assert resp.status_code == 200
        # 检查密钥失效
        resp = UserApiMainUser.ConsoleUserService_GetUserAssociatedInfoByIDGetApi(user_id=user_id)
        print('access_key_list {}'.format(resp.json))
        assert resp.json_get("access_key_list.0.blocked") is True
        assert resp.json_get("blocked") is False

        # 改为编程访问+控制台访问
        access_mode = 3
        resp = UserApiMainUser.ConsoleUserService_UpdateUserAccessModePostApi(user_id=user_id, access_mode=access_mode,
                                                                              code=code)
        assert resp.status_code == 200
        # 检查密钥应该为启用
        resp = UserApiMainUser.ConsoleUserService_GetUserAssociatedInfoByIDGetApi(user_id=user_id)
        assert resp.json_get("access_key_list.0.blocked") is False
        assert resp.json_get("blocked") is False

        # 改为子账无效
        access_mode = 0
        resp = UserApiMainUser.ConsoleUserService_UpdateUserAccessModePostApi(user_id=user_id, access_mode=access_mode,
                                                                              code=code)
        assert resp.status_code == 200
        # 检查密钥失效，用户状态失效
        resp = UserApiMainUser.ConsoleUserService_GetUserAssociatedInfoByIDGetApi(user_id=user_id)
        print('access_key_list {}'.format(resp.json_get("access_key_list.0.blocked")))

        assert resp.json_get("access_key_list.0.blocked") is True
        assert resp.json_get("blocked") is True

        # 删除子账号
        resp = UserApiMainUser.ConsoleUserService_DeleteUserPostApi(user_id=user_id, code=code, force=None)
        assert resp.status_code == 200

    def test_scenarioo_003_modifyProgrammeSubUser(self, config_obj, UserApiMainUser, OcrApi):
        """ 校验编程子账户密钥以及权限相关"""
        # 创建子账号
        nick_name = "autoTestSubUser2"
        access_mode = 1
        password = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_CreateUserPostApi(nick_name=nick_name, access_mode=access_mode,
                                                                    password=password, code=code)
        user_id = resp.json["user_id"]
        print('user_id {}'.format(user_id))
        assert resp.status_code == 200

        # 修改子账号描述
        description = "autoTestSubUser"
        resp = UserApiMainUser.ConsoleUserService_UpdateUserDescInfoPostApi(user_id=user_id, nick_name=nick_name,
                                                                            description=description)
        assert resp.status_code == 200

        # 获取权限组
        resp = UserApiMainUser.ConsoleUserService_ListPolicyGroupGetApi()
        assert resp.status_code == 200
        assert len(resp.json["list"]) >= 1

        # 权限组详情
        group_id = config_obj.Console.User.testConsoleMainUser.policyGroupId
        resp = UserApiMainUser.ConsoleUserService_GetPolicyGroupAssociatedInfoByIDGetApi(group_id=group_id)
        assert resp.status_code == 200

        # 增加密钥
        resp = UserApiMainUser.ConsoleUserService_CreateUserAKSKPostApi(user_id=user_id, code=code)
        assert resp.status_code == 200
        access_key_id = resp.json["access_key_id"]
        secret_access_key = resp.json["secret_access_key"]

        # 下载密钥
        resp = UserApiMainUser.ConsoleUserService_ExportUserAKSKExcelPostApi(user_id=user_id,
                                                                             access_key_id=access_key_id)
        assert resp.status_code == 200

        # 检查下载密钥内容
        base64_str = resp.json["file"]
        excel_data = base64.b64decode(base64_str)
        excel_file = BytesIO(excel_data)
        print(' excel_file is {}'.format(excel_file))

        df = pd.read_excel(excel_file)
        excel_dict = df.to_dict()
        print(' excel_dict is {}'.format(excel_dict))
        secret_access_key_from_file = excel_dict['secret_access_key'][0]
        access_key_id_from_file = excel_dict['access_key_id'][0]
        print('secret_access_key_from_file is {}'.format(secret_access_key_from_file))
        print('access_key_id_from_file is {}'.format(access_key_id_from_file))
        assert secret_access_key_from_file == secret_access_key
        assert access_key_id_from_file == access_key_id

        # 给子账号赋权营业执照
        resp = UserApiMainUser.ConsoleUserService_BatchAddPolicyGroupToUserPostApi(user_id=user_id,
                                                                                   group_id_list=[group_id])
        assert resp.status_code == 200
        """  营业执照识别"""
        ak = access_key_id
        sk = secret_access_key
        resp = OcrApi.OCRBusinessLicenseBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 200

        # 移除子账号权限
        resp = UserApiMainUser.ConsoleUserService_RemovePolicyGroupFromUserPostApi(group_id=group_id, user_id=user_id,
                                                                                   code=code)
        assert resp.status_code == 200
        time.sleep(30)

        # 营业执照识别失败
        resp = OcrApi.OCRBusinessLicenseBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 403

        # 删除密钥
        resp = UserApiMainUser.ConsoleUserService_DeleteAccessKeyPostApi(user_id=user_id, access_key_id=access_key_id,
                                                                         code=code)
        assert resp.status_code == 200

        # 删除子账号
        resp = UserApiMainUser.ConsoleUserService_DeleteUserPostApi(user_id=user_id, code=code, force=None)
        assert resp.status_code == 200
        
    @pytest.mark.Skiponline
    def test_scenarioo_004_modifyConsleSubUser(self, config_obj, UserApiMainUser, AuthiamApi, ProductApi):
        """ 校验控制台类型子账户以及权限相关，修改密码以及登录"""

        # 创建控制台子账号
        nick_name = "autoTestSubUser3"
        access_mode = 2
        password = "123456qw"
        pwd = sign_utils.getMd5(password)
        code = None
        resp = UserApiMainUser.ConsoleUserService_CreateUserPostApi(nick_name=nick_name, access_mode=access_mode,
                                                                    password=pwd, code=code)
        user_id = resp.json["user_id"]
        username = resp.json["user_name"]
        print('user_id {}'.format(user_id))
        assert resp.status_code == 200

        # 修改子账户描述
        description = "autoTestSubUser"
        resp = UserApiMainUser.ConsoleUserService_UpdateUserDescInfoPostApi(user_id=user_id, nick_name=nick_name,
                                                                            description=description)
        assert resp.status_code == 200

        # 子账号登录
        digits = "620836"
        captcha_id = "tiLFNNMPvzkGX9ysYSZ0"
        resp = AuthiamApi.login_with_user(username=username, password=password, captcha_id=captcha_id, digits=digits)

        assert resp.status_code == 200
        subUserLoginToken = resp.json_get("access_token")
        # 子账户未赋权的情况下，查看服务详情报403
        spu_code = config_obj.Console.User.testConsoleMainUser.spuCode
        resp = ProductApi.ConsoleProductService_ListRealtimeUsageByCodeGetApi(spu_code=spu_code,
                                                                              loginToken=subUserLoginToken)
        assert resp.status_code == 403

        # 给子账户赋权
        group_id = config_obj.Console.User.testConsoleMainUser.policyGroupId
        resp = UserApiMainUser.ConsoleUserService_BatchAddPolicyGroupToUserPostApi(user_id=user_id,
                                                                                   group_id_list=[group_id])
        assert resp.status_code == 200

        # 子账户查看服务详情
        time.sleep(5)
        resp = ProductApi.ConsoleProductService_ListRealtimeUsageByCodeGetApi(spu_code=spu_code,
                                                                              loginToken=subUserLoginToken)
        assert resp.status_code == 200

        # 去掉子账户权限
        resp = UserApiMainUser.ConsoleUserService_RemovePolicyGroupFromUserPostApi(group_id=group_id, user_id=user_id,
                                                                                   code=code)
        assert resp.status_code == 200
        time.sleep(5)

        # 子账户查看服务详情报无权限
        resp = ProductApi.ConsoleProductService_ListRealtimeUsageByCodeGetApi(spu_code=spu_code,
                                                                              loginToken=subUserLoginToken)
        assert resp.status_code == 403

        # 子账号修改密码
        passwordUpdate = sign_utils.getMd5('12345qwe')
        resp = UserApiMainUser.ConsoleUserService_UpdateSubUserPasswordPostApi(user_id=user_id, password=passwordUpdate)
        assert resp.status_code == 200

        # 子账户登录失败
        resp = AuthiamApi.login_with_user(username=username, password=password, captcha_id=captcha_id, digits=digits)
        assert resp.status_code == 400

        # 删除子账号
        resp = UserApiMainUser.ConsoleUserService_DeleteUserPostApi(user_id=user_id, code=code, force=None)
        assert resp.status_code == 200
    @pytest.mark.Skiponline
    # @pytest.mark.skip("测试环境有问题先暂时跳过")
    def test_scenario_005_UnsubscribeOrder(self, config_obj, OcrApi, OrderinternalApi, AuthiamApi, UserApiMainUser,
                                           OrderApi,
                                           ProductApi):
        """ openConsole订单退订权限组检查 """
        # 创建编程子账号
        nick_name = "autoTestSubUser4"
        access_mode = 1
        password = None
        code = None
        resp = UserApiMainUser.ConsoleUserService_CreateUserPostApi(nick_name=nick_name, access_mode=access_mode,
                                                                    password=password, code=code)
        user_id = resp.json["user_id"]
        print('user_id {}'.format(user_id))
        assert resp.status_code == 200

        # 修改子账户描述
        description = "autoTestSubUser"
        resp = UserApiMainUser.ConsoleUserService_UpdateUserDescInfoPostApi(user_id=user_id, nick_name=nick_name,
                                                                            description=description)
        assert resp.status_code == 200

        # 创建后付费订单
        digits = "620836"
        captcha_id = "tiLFNNMPvzkGX9ysYSZ0"
        phone = config_obj.Console.User.testConsoleMainUser.username
        password = config_obj.Console.User.testConsoleMainUser.password
        resp = AuthiamApi.login_with_phone(phone=phone, password=password, captcha_id=captcha_id, digits=digits)
        assert resp.status_code == 200

        loginToken = resp.json_get("access_token")
        spu_code = config_obj.Console.User.testConsoleMainUser.spuCodeForOrder
        resp = OrderApi.CreatePostPayOrder(spu_code, ProductApi, loginToken)
        order_id = resp.json_get("order_info.order_id")
        assert resp.status_code == 200

        # 审核订单
        operate = "OP_AGREE"
        resp = OrderinternalApi.ConsoleOrderInternalService_AuditOrderPostApi(order_id=order_id, operate=operate,
                                                                              reason=None)
        assert resp.status_code == 200

        # 给子账户赋予订单权限组
        group_id = config_obj.Console.User.testConsoleMainUser.policyGroupIdForOrder
        resp = UserApiMainUser.ConsoleUserService_BatchAddPolicyGroupToUserPostApi(user_id=user_id,
                                                                                   group_id_list=[group_id])
        assert resp.status_code == 200

        # 增加密钥
        resp = UserApiMainUser.ConsoleUserService_CreateUserAKSKPostApi(user_id=user_id, code=code)
        assert resp.status_code == 200
        access_key_id = resp.json["access_key_id"]
        secret_access_key = resp.json["secret_access_key"]
        ak = access_key_id
        sk = secret_access_key
        time.sleep(30)
        # 账户服务使用正常
        resp = OcrApi.OCRBankcardBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 200

        # 账户订单退订
        time.sleep(180)
        resp = OrderApi.ConsoleOrderService_UnsubscribeOrderPostApi(order_id=order_id, loginToken=loginToken)
        assert resp.status_code == 200

        # 检查订单状态为退订
        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=order_id, loginToken=loginToken)
        assert resp.json_get("order_info.status") == "UNSUBSCRIBED"

        # 检查权限组下线
        time.sleep(120)
        nick_name = config_obj.Console.User.testConsoleMainUser.policyGroupName
        resp = UserApiMainUser.ConsoleUserService_ListPolicyGroupGetApi(nick_name=nick_name)
        assert len(resp.json["list"]) == 0

        # 子账户与权限组解绑
        resp = OcrApi.OCRBankcardBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 403

        # 删除子账号
        resp = UserApiMainUser.ConsoleUserService_DeleteUserPostApi(user_id=user_id, code=code, force=None)
        assert resp.status_code == 200

    def test_scenarioo_006_modifySubUserAkSk(self, UserApiMainUser):
        # 创建编程控制台子账号
        nick_name = "autoTestSubUser5"
        access_mode = 3
        password = "f5e05a41724115d076bfb1fd2bd9613e"
        code = None
        resp = UserApiMainUser.ConsoleUserService_CreateUserPostApi(nick_name=nick_name, access_mode=access_mode,
                                                                    password=password, code=code)
        user_id = resp.json["user_id"]
        assert resp.status_code == 200

        # 修改子账户描述
        description = "autoTestSubUser"
        resp = UserApiMainUser.ConsoleUserService_UpdateUserDescInfoPostApi(user_id=user_id, nick_name=nick_name,
                                                                            description=description)
        assert resp.status_code == 200

        # 增加密钥
        resp = UserApiMainUser.ConsoleUserService_CreateUserAKSKPostApi(user_id=user_id, code=code)
        assert resp.status_code == 200

        # 子账号变更为失效
        access_mode = 0
        resp = UserApiMainUser.ConsoleUserService_UpdateUserAccessModePostApi(user_id=user_id, access_mode=access_mode,
                                                                              code=code)
        assert resp.status_code == 200

        # check aksk and pwd's status should be invalid
        resp = UserApiMainUser.ConsoleUserService_GetUserAssociatedInfoByIDGetApi(user_id=user_id)
        assert resp.status_code == 200
        assert resp.json["blocked"] is True
        for ak in resp.json["access_key_list"]:
            assert ak["blocked"] is True

        """ 删除子账号 """
        resp = UserApiMainUser.ConsoleUserService_DeleteUserPostApi(user_id=user_id, code=code, force=None)
        assert resp.status_code == 200

    @pytest.mark.skip("测试环境有问题先暂时跳过")
    def test_scenarioo_007_DisableAccount(self, config_obj, AuthinternalauthApi, OcrApi, UserApiMainUser, AuthiamApi,
                                          OrderApi, ProductApi, OrderinternalApi):
        """ 账户禁用检查权限组 """
        # 主账户登录
        digits = "620836"
        captcha_id = "tiLFNNMPvzkGX9ysYSZ0"
        username = config_obj.Console.User.testConsoleMainUser.userNameForDisable
        password = "123456qw"
        resp = AuthiamApi.login_with_user(username=username, password=password, captcha_id=captcha_id, digits=digits)
        assert resp.status_code == 200
        mainUserLoginToken = resp.json_get("access_token")

        # 创建后付费订单
        spu_code = config_obj.Console.User.testConsoleMainUser.spuCodeForOrder
        resp = OrderApi.CreatePostPayOrder(spu_code, ProductApi, mainUserLoginToken)
        assert resp.status_code == 200
        postPayOrderId = resp.json_get("order_info.order_id")

        # 创建预付费订单
        prePayOrderId = config_obj.Console.User.testConsoleMainUser.prePayOrderId

        # 运营后台审核
        operate = "OP_AGREE"
        resp = OrderinternalApi.ConsoleOrderInternalService_AuditOrderPostApi(order_id=postPayOrderId, operate=operate,
                                                                              reason=None)
        assert resp.status_code == 200

        # 子账户
        subUserIdForDisable = config_obj.Console.User.testConsoleMainUser.subUserIdForDisable
        ak = config_obj.Console.User.testConsoleMainUser.akForDisable
        sk = config_obj.Console.User.testConsoleMainUser.skForDisable

        # 获取权限组列表
        resp = UserApiMainUser.ConsoleUserService_ListPolicyGroupGetApi(nick_name=None, description=None, order=None,
                                                                        page_request_offset=None,
                                                                        page_request_limit=None,
                                                                        page_request_total=None,
                                                                        loginToken=mainUserLoginToken)
        assert resp.status_code == 200
        num = int(len(resp.json_get("list")))
        # 给子账户赋予订单权限组
        group_id_list = []
        for i in range(num):
            print('range {}'.format(range(num)))
            group_id = resp.json["list"][i]["group_id"]
            group_id_list.append(group_id)

        resp = UserApiMainUser.ConsoleUserService_BatchAddPolicyGroupToUserPostApi(user_id=subUserIdForDisable,
                                                                                   group_id_list=group_id_list,
                                                                                   loginToken=mainUserLoginToken)
        assert resp.status_code == 200

        # 验证后付费服务
        time.sleep(30)
        resp = OcrApi.OCRBankcardBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 200
        # 验证预付费服务
        resp = OcrApi.OCRBusinessLicenseBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 200

        # 账户禁用
        time.sleep(90)
        account_id = config_obj.Console.User.testConsoleMainUser.accountIdForDisable
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountPostApi(account_id=account_id,
                                                                                        update_mode=0,
                                                                                        account_used_status="ACCOUNT_USED_STATUS_BLOCKED",
                                                                                        payment_type=None)
        assert resp.status_code == 200
        # 权限组下线
        time.sleep(240)
        resp = UserApiMainUser.ConsoleUserService_ListPolicyGroupGetApi(nick_name=None, loginToken=mainUserLoginToken)
        assert len(resp.json["list"]) == 0

        # 子账户与权限组解绑
        # 验证后付费服务
        resp = OcrApi.OCRBankcardBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 403
        # 验证预付费服务
        resp = OcrApi.OCRBusinessLicenseBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 403
        # 检查订单状态为禁用
        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=postPayOrderId, loginToken=mainUserLoginToken)
        assert resp.json_get("order_info.status") == "FREEZED"

        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=prePayOrderId, loginToken=mainUserLoginToken)
        assert resp.json_get("order_info.status") == "PAID"

        # 禁用消息检查
        # 启用账户
        resp = AuthinternalauthApi.ConsoleInternalAuthService_AdminUpdateAccountPostApi(account_id=account_id,
                                                                                        update_mode=0,
                                                                                        account_used_status="ACCOUNT_USED_STATUS_UNBLOCKED",
                                                                                        payment_type=None)
        assert resp.status_code == 200
        time.sleep(180)
        # 后付费订单状态为禁用
        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=postPayOrderId, loginToken=mainUserLoginToken)
        assert resp.json_get("order_info.status") == "FREEZED"
        # 预付费订单状态为启用
        resp = OrderApi.ConsoleOrderService_GetOneOrderGetApi(order_id=prePayOrderId, loginToken=mainUserLoginToken)
        assert resp.json_get("order_info.status") == "PAID"

        # 预付费订单启用
        resp = OcrApi.OCRBusinessLicenseBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 403

        # 验证后付费服务
        resp = OcrApi.OCRBankcardBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 403

        # 预付费权限组启用
        nick_name = config_obj.Console.User.testConsoleMainUser.policyGroupNameForPrePaid
        resp = UserApiMainUser.ConsoleUserService_ListPolicyGroupGetApi(nick_name=nick_name, loginToken=mainUserLoginToken)
        assert len(resp.json["list"]) == 1

        # 启用消息检查

    @pytest.mark.skip("测试环境有问题先暂时跳过")
    def test_scenarioo_008_UnsubscribeOrderFromInternalConsole(self, config_obj, AuthinternalauthApi, OcrApi,
                                                               UserApiMainUser,
                                                               AuthiamApi, OrderApi, ProductApi, OrderinternalApi):
        """ 运营后台订单退订 """
        # 主账户登录
        digits = "620836"
        captcha_id = "tiLFNNMPvzkGX9ysYSZ0"
        username = config_obj.Console.User.testConsoleMainUser.userNameForDisable
        password = "123456qw"
        resp = AuthiamApi.login_with_user(username=username, password=password, captcha_id=captcha_id, digits=digits)
        assert resp.status_code == 200
        mainUserLoginToken = resp.json_get("access_token")

        # 创建后付费订单
        spu_code = config_obj.Console.User.testConsoleMainUser.spuCodeForOrder
        resp = OrderApi.CreatePostPayOrder(spu_code, ProductApi, mainUserLoginToken)
        assert resp.status_code == 200
        postPayOrderId = resp.json_get("order_info.order_id")

        # 运营后台审核
        operate = "OP_AGREE"
        resp = OrderinternalApi.ConsoleOrderInternalService_AuditOrderPostApi(order_id=postPayOrderId, operate=operate,
                                                                              reason=None)
        assert resp.status_code == 200
        # 子账户
        subUserIdForDisable = config_obj.Console.User.testConsoleMainUser.subUserIdForDisable
        ak = config_obj.Console.User.testConsoleMainUser.akForDisable
        sk = config_obj.Console.User.testConsoleMainUser.skForDisable

        # 获取权限组列表
        resp = UserApiMainUser.ConsoleUserService_ListPolicyGroupGetApi(nick_name=None, description=None,
                                                                        order=None, page_request_offset=None,
                                                                        page_request_limit=None,
                                                                        page_request_total=None,
                                                                        loginToken=mainUserLoginToken)
        assert resp.status_code == 200
        num = int(len(resp.json_get("list")))
        # 给子账户赋予权限组
        group_id_list = []
        for i in range(num):
            print('range {}'.format(range(num)))
            group_id = resp.json["list"][i]["group_id"]
            group_id_list.append(group_id)

        resp = UserApiMainUser.ConsoleUserService_BatchAddPolicyGroupToUserPostApi(user_id=subUserIdForDisable,
                                                                                   group_id_list=group_id_list,
                                                                                   loginToken=mainUserLoginToken)
        assert resp.status_code == 200
        time.sleep(60)
        # 验证后付费服务
        resp = OcrApi.OCRBankcardBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 200
        # 验证预付费服务
        resp = OcrApi.OCRBusinessLicenseBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 200

        # 运营后台订单退订
        time.sleep(180)
        resp = OrderinternalApi.ConsoleOrderInternalService_UnsubscribeOrderPostApi(order_id=postPayOrderId)
        assert resp.status_code == 200

        # 权限组下线
        time.sleep(120)

        # 子账户与权限组解绑
        # 验证后付费服务
        resp = OcrApi.OCRBankcardBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 403
        # 验证预付费服务
        resp = OcrApi.OCRBusinessLicenseBySubUser(ak=ak, sk=sk)
        assert resp.status_code == 200

        # 检查后付费订单状态为退订
        resp = OrderinternalApi.ConsoleOrderInternalService_GetAuditOneOrderGetApi(order_id=postPayOrderId)
        assert resp.json_get("order_info.order_info.status") == "UNSUBSCRIBED"

    def test_009_realtimeAndHistoryUsage(self, config_obj, MainUserTokenForSpuop, UserApiMainUser, ProductApi):
        """  查看实时调用量以及历史用量 """
        # 查看实时用量
        spu_code = config_obj.Console.User.testConsoleMainUser.spuCode
        resp = ProductApi.ConsoleProductService_ListRealtimeUsageByCodeGetApi(spu_code=spu_code,
                                                                              loginToken=MainUserTokenForSpuop)
        assert int(resp.json_get("total_count")) >= 1
        print('total_count {}'.format(int(resp.json_get("total_count"))))

        # 获取历史用量
        yesterday = str(date.today() - timedelta(days=2))
        print('yesterday {}'.format(yesterday))
        date_request_start_at = yesterday + "T16:00:00Z"
        date_request_end_at = yesterday + "T16:00:00Z"
        resp = ProductApi.ConsoleProductService_ListUsageByCodeGetApi(spu_code=spu_code,
                                                                      date_request_start_at=date_request_start_at,
                                                                      date_request_end_at=date_request_end_at,
                                                                      loginToken=MainUserTokenForSpuop)
        assert int(resp.json_get("all_usages.0.total_count")) >= 1

    def test_cleanAutoTestSubUser(self, UserApiMainUser):
        """ 清除自动化测试子账号 """
        description = "autoTestSubUser"
        resp = UserApiMainUser.getSubUser(description=description)
        num = int(len(resp.json_get("list")))
        if num >= 1:
            for i in range(num):
                print('range {}'.format(range(num)))
                user_id = resp.json["list"][i]["user_id"]
                UserApiMainUser.deleteSubUser(user_id=user_id)
        else:
            log().info("没有需要清除的自动化测试子账号")

    # def test_getPreOrderId(self, config_obj, UserApiMainUser, OrderApi, ProductApi, MainUserTokenForSpuop):
    #     # 获取预付费订单id
    #     resp = OrderApi.ConsoleOrderService_GetAllOrderGetApi(status=None, date_request_start_at=None,
    #                                                           date_request_end_at=None, page_request_offset=100,
    #                                                           page_request_limit=100, page_request_total=0,
    #                                                           created_sort_type=None, loginToken=MainUserTokenForSpuop)
    #     num = len(resp.json_get("all_orders"))
    #     print('num123 {}'.format(num))
    #     preOrderId = None
    #     for i in range(num):
    #         print('bill_mode123 {}'.format(resp.json["all_orders"][i]["bill_mode"]))
    #         if resp.json["all_orders"][i]["bill_mode"] == "PAY_TYPE_PRE" and \
    #                 resp.json["all_orders"][i]["product_info"]["all_spus"][0]["all_skus"][0]["status"] == "VALID":
    #             print('bill_mode456 {}'.format(resp.json["all_orders"][i]["bill_mode"]))
    #             preOrderId = resp.json["all_orders"][i]["order_id"]
    #             break
    #
    #     if preOrderId == None:
    #         # 创建预付费订单
    #         print('preOrderIdIF {}'.format(preOrderId))
    #         # spu_code = config_obj.Console.User.testConsoleMainUser.spuCode
    #         # resp = OrderApi.CreatePrePayOrder(spu_code, ProductApi, MainUserTokenForSpuop)
    #         # preOrderId = resp.json_get("order_info.order_id")
    #
    #     print('preOrderId123 {}'.format(preOrderId))
