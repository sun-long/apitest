#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import base64
import json
import os
import random
import string
import time

import pytest
from commonlib import config, time_utils, sign_utils, utils
from commonlib.log_utils import log
from PIL import Image


class TestRasTool(object):
    """ Ras工具代码"""

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

    @pytest.mark.skip("工具,默认跳过")
    def test_tool_CreateUser(self, config_obj, UserApi):
        """  创建手机用户"""
        phone = "15011263628"
        password = "wangan1234"
        resp = UserApi.createPhoneUser(phone, password)
        assert resp.status_code == 200

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_Captcha(self, config_obj, AuthiamApi):
        """ 登录获取token"""
        captcha_id = AuthiamApi.get_captcha()
        digits = str(input("请输入验证码："))
        log().info("captcha_id: %s" % captcha_id)
        log().info("code: %s" % digits)

    def test_tool_Login1(self, config_obj, AuthiamApi):
        # username = "443022786655455183"
        # password = "123456qw"
        phone = "15011263680"
        password = "wangan1234"
        captcha_id = "1"
        digits = "1234"
        source = None #"console"
        # source = "console-internal"
        resp = AuthiamApi.login_with_phone(phone, password, captcha_id, digits, source=source)
        token = resp.json_get("access_token")
        expires_in = resp.json_get("expires_in")
        log().info("token:%s" % token)
        log().info("expires_in:%s" % time_utils.get_str_by_timestamp(expires_in))
        i = 1

    def test_tool_LoginSkipCode(self, config_obj, AuthiamApi):
        """ 测试环境跳过验证码"""
        # username = "443022786655455183"
        # password = "123456qw"
        phone = "15011263680"
        password = "wangan1234"
        captcha_id = AuthiamApi.get_captcha()
        digits = "123456"
        log().info("captcha_id: %s" % captcha_id)
        log().info("code: %s" % digits)
        resp = AuthiamApi.login_with_phone(phone, password, captcha_id, digits)
        token = resp.json_get("access_token")
        expires_in = resp.json_get("expires_in")
        log().info("token:%s" % token)
        log().info("expires_in:%s" % time_utils.get_str_by_timestamp(expires_in))

    def test_tool_CreateAutoTestUser(self, config_obj, UserApi, AuthApi, AuthiamApi):

        # 注册账号
        mode = "1"
        password = "123456qw"
        passwordMd5 = sign_utils.getMd5(password)
        randNum = ''.join(random.sample(string.digits, 3))
        email = "18%s@160.com" % randNum
        log().info("newEmail: %s" % email)
        phone = "13693109%s" % randNum
        code = None
        email_code = "12121"
        resp = UserApi.ConsoleUserService_CreateUserWithAccountPostApi(mode=mode, password=passwordMd5, email=email,
                                                                       phone=phone, code=code, email_code=email_code)
        assert resp.status_code == 200

        # 登录(线上环境手动登录获取token)
        captcha_id = AuthiamApi.get_captcha()
        resp = AuthiamApi.login_with_phone(phone, password, captcha_id, "123456")
        loginToken = resp.json_get("access_token")
        log().info("loginToken: %s" % loginToken)

        # 提交审核
        image_path = os.path.join(config.console_image_path, "mucun.jpeg")
        enterprise_photo = AuthApi.imageToBase64(image_path)
        randNam = ''.join(random.sample(string.ascii_letters + string.digits, 3))
        randNum = ''.join(random.sample(string.digits, 3))
        enterprise_account = {
            "enterprise_name": "enterprise_%s" % randNam,
            "enterprise_number": "91350100M%s100Y10" % randNum,
            "enterprise_card_name": "Miss zhao",
            "position": "ceo",
            "industry": "INDUSTRY_TYPE_OTHERS",
            "scenario": "1212",
            "end_user": "toC",
            "business_inviter": None,
            "enterprise_photo": enterprise_photo,
            "area_name": "中国大陆_吉林省_白城市"
        }
        log().info("enterprise_account: %s" % enterprise_account)
        phone_code = "12345"
        resp = AuthApi.ConsoleAuthService_SubmitEnterpriseAccountPostApi(enterprise_account=enterprise_account,
                                                                         phone_code=phone_code, loginToken=loginToken)
        assert resp.status_code == 200
        # 认证审核
        # 认证审核
        # 开启后付费
        # 下单
        # 创建aksk

    def test_tool_createAllPostPayOrders(self, config_obj, OrderApi, OrderinternalApi, ProductApi):
        """ 批量创建后付费订单"""
        spuIdsCodeList = config_obj.SpuCode.ids.ids_spuCode
        spuRasCodeList = config_obj.SpuCode.ras.ras_spuCode
        spuCodeList = spuIdsCodeList + spuRasCodeList
        print('spuCodeList :{}'.format(spuCodeList))
        for spuCode in spuCodeList:
            try:
                # 获取商品的sku_id
                spu_code = spuCode
                resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code)
                assert resp.status_code == 200

                # 创建后付费订单
                sku_id = resp.json_get("all_spus.0.all_skus.0.all_prices.0.sku_id")
                all_items = [{"sku_id": sku_id, "count": "1", "site_id": config_obj.EnvInfo.BeltEdge.hangzhou.site_id}]
                resp = OrderApi.ConsoleOrderService_CreateOrderPostApi(all_items=all_items)
                assert resp.status_code == 200
                order_id = resp.json["order_info"]["order_id"]
                operate = "OP_AGREE"
                resp = OrderinternalApi.ConsoleOrderInternalService_AuditOrderPostApi(order_id=order_id, operate=operate,
                                                                                      reason=None)
                assert resp.status_code == 200
            except IndexError:
                pass

    def test_tool_listPostpayBufferTime(self, config_obj, OrderApi, OrderinternalApi, ProductApi, UserApi):
        """  计算权限下线时间"""
        # spuIdsCodeList = config_obj.SpuCode.ids.ids_spuCode
        # spuRasCodeList = config_obj.SpuCode.ras.ras_spuCode
        spuCodeList = ["FallDetection"]
        print('spuCodeList :{}'.format(spuCodeList))
        bufferTime = 0
        runTime = 90
        timeInternal = 90
        nick_name = "FallDetection_default_pg"
        for spuCode in spuCodeList:
            try:
                # 获取商品的sku_id
                spu_code = spuCode
                resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code)
                assert resp.status_code == 200

                # 创建后付费订单
                sku_id = resp.json_get("all_spus.0.all_skus.0.all_prices.0.sku_id")
                all_items = [{"sku_id": sku_id, "count": "1", "site_id": config_obj.EnvInfo.BeltEdge.hangzhou.site_id}]
                resp = OrderApi.ConsoleOrderService_CreateOrderPostApi(all_items=all_items)
                assert resp.status_code == 200
                order_id = resp.json["order_info"]["order_id"]
                operate = "OP_AGREE"
                resp = OrderinternalApi.ConsoleOrderInternalService_AuditOrderPostApi(order_id=order_id,
                                                                                      operate=operate,
                                                                                      reason=None)
                assert resp.status_code == 200
                #退订
                time.sleep(timeInternal)
                resp = OrderApi.ConsoleOrderService_UnsubscribeOrderPostApi(order_id=order_id)
                startTime = time.time()
                assert resp.status_code == 200

                #获取权限列表
                while len(UserApi.ConsoleUserService_ListPolicyGroupGetApi(nick_name=nick_name).json["list"]) == 1 and bufferTime < runTime:
                    time.sleep(1)
                    endTime = time.time()
                    bufferTime = endTime - startTime

                count = len(UserApi.ConsoleUserService_ListPolicyGroupGetApi(nick_name=nick_name).json["list"])
                if bufferTime > runTime and count == 1:
                    log().info("spuCode： %s, 超过 %ss 依然没有下线, 用时时间: %s " % (spuCodeList, runTime, bufferTime))
                elif count == 0:
                    log().info("spuCode： %s, 权限下线时间: %s " % (spuCode, bufferTime))

            except IndexError:
                pass

    def test_tool_ListPolicyGroup(self, config_obj, UserApi):
        """  查询权限组id"""
        nick_name = None
        description = None
        order = None
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = UserApi.ConsoleUserService_ListPolicyGroupGetApi(nick_name=nick_name, description=description, order=order, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200
        group_list = resp.json_get("list")
        out = "\n权限组列表\n"
        for group_info in group_list:
            out += "%s,%s\n" % (group_info["group_name"], group_info["group_id"])
        log().info(out)
