#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
@pytest.mark.Skiponline
@pytest.mark.ConsoleRegression
class TestSpuopScenario(object):
    """ Spuop scenario test"""

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

    def test_scenario_000_allAccountInvisible(self, config_obj, ProductApi, PersonalTokenForSpuop, MainUserTokenForSpuop, SpuopApi):
        """ 设置所有账号不可见"""
        # 设置spu所有账号不可见
        name = config_obj.Console.User.internalTestUser.skuName
        filter_account_type = None
        all_account_ids = None
        resp = SpuopApi.ConsoleSPUopService_SetSKUFilterPostApi(name=name, filter_account_type=filter_account_type,
                                                                all_account_ids=all_account_ids)
        assert resp.status_code == 200

        # 校验企业账户不可见
        spu_code = config_obj.Console.User.internalTestUser.spuCode
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code, loginToken=MainUserTokenForSpuop)
        assert resp.status_code == 200
        num = int(len(resp.json_get("all_spus.0.all_skus")))

        for i in range(num):
            print('skuIdMain {}'.format(resp.json["all_spus"][0]["all_skus"][i]["id"]))
            assert resp.json["all_spus"][0]["all_skus"][i]["id"] != config_obj.Console.User.internalTestUser.skuId

        # 校验个人账户不可见
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code, loginToken=PersonalTokenForSpuop)
        assert resp.status_code == 200
        num = int(len(resp.json_get("all_spus.0.all_skus")))

        for i in range(num):
            print('skuId {}'.format(resp.json["all_spus"][0]["all_skus"][i]["id"]))
            assert resp.json["all_spus"][0]["all_skus"][i]["id"] != config_obj.Console.User.internalTestUser.skuId

    def test_scenario_001_allAccountVisible(self,  config_obj, ProductApi, PersonalTokenForSpuop, MainUserTokenForSpuop, SpuopApi):
        """ 设置所有账号可见"""
        # 设置spu所有账号可见
        name = config_obj.Console.User.internalTestUser.skuName
        filter_account_type = "ALL"
        all_account_ids = None
        resp = SpuopApi.ConsoleSPUopService_SetSKUFilterPostApi(name=name, filter_account_type=filter_account_type,
                                                                all_account_ids=all_account_ids)
        assert resp.status_code == 200

        # 校验企业账户可见
        spu_code = config_obj.Console.User.internalTestUser.spuCode
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code,loginToken=MainUserTokenForSpuop)
        assert resp.status_code == 200
        num = int(len(resp.json_get("all_spus.0.all_skus")))
        skuIdList = []
        for i in range(num):
            skuId = resp.json["all_spus"][0]["all_skus"][i]["id"]
            skuIdList.append(skuId)

        print('skuIdList {}'.format(skuIdList))
        assert skuIdList.__contains__(config_obj.Console.User.internalTestUser.skuId)

        # 校验个人账户可见
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code, loginToken=PersonalTokenForSpuop)
        assert resp.status_code == 200
        num = int(len(resp.json_get("all_spus.0.all_skus")))
        skuIdList1 = []
        for i in range(num):
            skuId = resp.json["all_spus"][0]["all_skus"][i]["id"]
            skuIdList1.append(skuId)

        print('skuIdList {}'.format(skuIdList1))
        assert skuIdList1.__contains__(config_obj.Console.User.internalTestUser.skuId)

    def test_scenario_002_allEnterpriseAccountVisible(self,  config_obj, ProductApi, PersonalTokenForSpuop, MainUserTokenForSpuop, SpuopApi):
        """ 设置所有企业账号可见"""
        # 设置所有企业账号可见
        name = config_obj.Console.User.internalTestUser.skuName
        filter_account_type = "ENTERPRISE"
        all_account_ids = None
        resp = SpuopApi.ConsoleSPUopService_SetSKUFilterPostApi(name=name, filter_account_type=filter_account_type,
                                                                all_account_ids=all_account_ids)
        assert resp.status_code == 200

        # 校验企业账户可见
        spu_code = config_obj.Console.User.internalTestUser.spuCode
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code,
                                                                        loginToken=MainUserTokenForSpuop)
        assert resp.status_code == 200
        num = int(len(resp.json_get("all_spus.0.all_skus")))
        skuIdList = []
        for i in range(num):
            skuId = resp.json["all_spus"][0]["all_skus"][i]["id"]
            skuIdList.append(skuId)

        print('skuIdList {}'.format(skuIdList))
        assert skuIdList.__contains__(config_obj.Console.User.internalTestUser.skuId)

        # 校验个人账户不可见
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code,
                                                                        loginToken=PersonalTokenForSpuop)
        assert resp.status_code == 200
        num = int(len(resp.json_get("all_spus.0.all_skus")))

        for i in range(num):
            print('skuId {}'.format(resp.json["all_spus"][0]["all_skus"][i]["id"]))
            assert resp.json["all_spus"][0]["all_skus"][i]["id"] != config_obj.Console.User.internalTestUser.skuId

    def test_scenario_003_allPersonalAccountVisible(self,  config_obj, ProductApi, PersonalTokenForSpuop, MainUserTokenForSpuop, SpuopApi):
        """ 设置所有个人账号可见"""
        # 设置所有个人账号可见
        name = config_obj.Console.User.internalTestUser.skuName
        filter_account_type = "PERSION"
        all_account_ids = None
        resp = SpuopApi.ConsoleSPUopService_SetSKUFilterPostApi(name=name, filter_account_type=filter_account_type,
                                                                all_account_ids=all_account_ids)
        assert resp.status_code == 200

        # 校验企业账户不可见
        spu_code = config_obj.Console.User.internalTestUser.spuCode
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code,
                                                                        loginToken=MainUserTokenForSpuop)
        assert resp.status_code == 200
        num = int(len(resp.json_get("all_spus.0.all_skus")))

        for i in range(num):
            print('skuIdMain {}'.format(resp.json["all_spus"][0]["all_skus"][i]["id"]))
            assert resp.json["all_spus"][0]["all_skus"][i]["id"] != config_obj.Console.User.internalTestUser.skuId

        # 校验个人账户可见
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code,
                                                                        loginToken=PersonalTokenForSpuop)
        assert resp.status_code == 200
        num = int(len(resp.json_get("all_spus.0.all_skus")))
        skuIdList1 = []
        for i in range(num):
            skuId = resp.json["all_spus"][0]["all_skus"][i]["id"]
            skuIdList1.append(skuId)

        print('skuIdList {}'.format(skuIdList1))
        assert skuIdList1.__contains__(config_obj.Console.User.internalTestUser.skuId)

    def test_scenario_004_setSeveralAccountVisible(self,  config_obj, ProductApi, PersonalTokenForSpuop, MainUserTokenForSpuop, SpuopApi):
        """ 设置部分企业账号账号可见"""
        # 设置spu部分账号可见
        name = config_obj.Console.User.internalTestUser.skuName
        filter_account_type = "NONE"
        all_account_ids = [config_obj.Console.User.internalTestUser.testAccountId]
        resp = SpuopApi.ConsoleSPUopService_SetSKUFilterPostApi(name=name, filter_account_type=filter_account_type,
                                                                all_account_ids=all_account_ids)
        assert resp.status_code == 200
        # 设置的该账号可见
        spu_code = config_obj.Console.User.internalTestUser.spuCode
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code,
                                                                        loginToken=MainUserTokenForSpuop)
        assert resp.status_code == 200
        num = int(len(resp.json_get("all_spus.0.all_skus")))
        skuIdList = []
        for i in range(num):
            skuId = resp.json["all_spus"][0]["all_skus"][i]["id"]
            skuIdList.append(skuId)

        print('skuIdList {}'.format(skuIdList))
        assert skuIdList.__contains__(config_obj.Console.User.internalTestUser.skuId)

        #其他账号不可见
        resp = ProductApi.ConsoleProductService_ListProductByCodeGetApi(spu_code=spu_code,
                                                                        loginToken=PersonalTokenForSpuop)
        assert resp.status_code == 200
        num = int(len(resp.json_get("all_spus.0.all_skus")))

        for i in range(num):
            print('skuId {}'.format(resp.json["all_spus"][0]["all_skus"][i]["id"]))
            assert resp.json["all_spus"][0]["all_skus"][i]["id"] != config_obj.Console.User.internalTestUser.skuId



    def test_setAllTestspuInvisiable(self, config_obj, ProductApi, PersonalTokenForSpuop, MainUserTokenForSpuop, SpuopApi):
        """ 设置所有账号不可见"""
        # 设置spu所有账号不可见
        name = config_obj.Console.User.internalTestUser.skuName
        filter_account_type = None
        all_account_ids = None
        resp = SpuopApi.ConsoleSPUopService_SetSKUFilterPostApi(name=name, filter_account_type=filter_account_type,
                                                                all_account_ids=all_account_ids)
        assert resp.status_code == 200



