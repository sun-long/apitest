#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestSpuopApi(object):
    """ spuop Api测试"""

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

    def test_api_ConsoleSPUopService_GetAllSPU(self, config_obj, SpuopApi):
        """  获取所有SPU列表
route: prefix=console-internal action=Ge... """
        code = None
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = None
        resp = SpuopApi.ConsoleSPUopService_GetAllSPUGetApi(code=code, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    @pytest.mark.skip("console内部使用")
    def test_api_ConsoleSPUopService_CheckSKUValidForAccount(self, config_obj, SpuopApi):
        """  检查用户是否能订阅指定的SKU(console内部使用) """
        account_id = None
        sku_name = None
        resp = SpuopApi.ConsoleSPUopService_CheckSKUValidForAccountPostApi(account_id=account_id, sku_name=sku_name)
        assert resp.status_code == 200

    def test_api_ConsoleSPUopService_CheckAccountList(self, config_obj, SpuopApi):
        """  检查输入的白名单账号是否存在
route: prefix=console-internal acti... """
        all_account_ids = [config_obj.Console.User.internalTestUser.account_id]
        resp = SpuopApi.ConsoleSPUopService_CheckAccountListPostApi(all_account_ids=all_account_ids)
        assert resp.status_code == 200

    def test_api_ConsoleSPUopService_GetSKUFilter(self, config_obj, SpuopApi):
        """  获取单个SKU设置的白名单
route: prefix=console-internal actio... """
        name = config_obj.Console.User.internalTestUser.spuCode
        resp = SpuopApi.ConsoleSPUopService_GetSKUFilterGetApi(name=name)
        assert resp.status_code == 200

    @pytest.mark.skip("场景测试中实现")
    def test_api_ConsoleSPUopService_SetSKUFilter(self, config_obj, SpuopApi):
        """  设置单个SKU的白名单
route: prefix=console-internal action=... """
        name = None
        filter_account_type = None
        all_account_ids = None
        resp = SpuopApi.ConsoleSPUopService_SetSKUFilterPostApi(name=name, filter_account_type=filter_account_type, all_account_ids=all_account_ids)
        assert resp.status_code == 200

    @pytest.mark.skip("内部接口")
    def test_api_ConsoleSPUopService_GetSPUInfoByPoliceName(self, config_obj, SpuopApi):
        """  根据spu_id或者policy_name获取SPU数据(bot使用) """
        spu_id = None
        policy_name = None
        spu_code = None
        resp = SpuopApi.ConsoleSPUopService_GetSPUInfoByPoliceNameGetApi(spu_id=spu_id, policy_name=policy_name, spu_code=spu_code)
        assert resp.status_code == 200

    def test_api_ConsoleSPUopService_GetSPU(self, config_obj, SpuopApi):
        """  获取单个SPU详情
route: prefix=console-internal action=Ge... """
        id = config_obj.Console.User.internalTestUser.spuId
        page_request_offset = 0
        page_request_limit = 20
        page_request_total = None
        resp = SpuopApi.ConsoleSPUopService_GetSPUGetApi(id=id, page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200
