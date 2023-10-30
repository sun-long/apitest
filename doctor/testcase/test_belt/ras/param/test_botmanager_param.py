#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestBotmanagerParam(object):
    """ botManager Param测试"""

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
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('version', 'invalidversion'),
        ('version', ''),
        ('version', None),
        ('module_name', 'invalidmodule_name'),
        ('module_name', ''),
        ('module_name', None),
        ('cluster_id', 'invalidcluster_id'),
        ('cluster_id', ''),
        ('cluster_id', None),
    ])
    def test_api_RasBotManager_CreateBotInstanceInvalidParam(self, invalidParam, config_obj, BotmanagerApi):
        """  创建bot instance
一个instance 是一个bot module的部署实例
route... """
        name = None
        version = None
        module_name = None
        cluster_id = None
        intef = BotmanagerApi.RasBotManager_CreateBotInstancePostApi(name=name, version=version, module_name=module_name, cluster_id=cluster_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('version', 'invalidversion'),
        ('version', ''),
        ('version', None),
    ])
    def test_api_RasBotManager_DeleteBotInvalidParam(self, invalidParam, config_obj, BotmanagerApi):
        """  删除bot
route prefix= internal_prefix=ras action=Del... """
        name = None
        version = None
        intef = BotmanagerApi.RasBotManager_DeleteBotGetApi(name=name, version=version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('version', 'invalidversion'),
        ('version', ''),
        ('version', None),
        ('module_name', 'invalidmodule_name'),
        ('module_name', ''),
        ('module_name', None),
        ('cluster_id', 'invalidcluster_id'),
        ('cluster_id', ''),
        ('cluster_id', None),
    ])
    def test_api_RasBotManager_DeleteBotInstanceInvalidParam(self, invalidParam, config_obj, BotmanagerApi):
        """  删除bot instance
route prefix= internal_prefix=ras a... """
        name = None
        version = None
        module_name = None
        cluster_id = None
        intef = BotmanagerApi.RasBotManager_DeleteBotInstanceGetApi(name=name, version=version, module_name=module_name, cluster_id=cluster_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('edge_bot_status', 'invalidedge_bot_status'),
        ('edge_bot_status', ''),
        ('edge_bot_status', None),
        ('cluster_id', 'invalidcluster_id'),
        ('cluster_id', ''),
        ('cluster_id', None),
    ])
    def test_api_RasBotManager_EdgeReportBotStateInvalidParam(self, invalidParam, config_obj, BotmanagerApi):
        """  边manager 上报bot状态，包括探活、pipeline等信息
route prefix= in... """
        edge_bot_status = None
        cluster_id = None
        intef = BotmanagerApi.RasBotManager_EdgeReportBotStatePostApi(edge_bot_status=edge_bot_status, cluster_id=cluster_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('action', 'invalidaction'),
        ('action', ''),
        ('action', None),
        ('version', 'invalidversion'),
        ('version', ''),
        ('version', None),
        ('prefix', 'invalidprefix'),
        ('prefix', ''),
        ('prefix', None),
    ])
    def test_api_RasBotManager_GetBotInvalidParam(self, invalidParam, config_obj, BotmanagerApi):
        """  action + version + prefix 查询bot
route prefix= inte... """
        action = None
        version = None
        prefix = None
        intef = BotmanagerApi.RasBotManager_GetBotGetApi(action=action, version=version, prefix=prefix, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bot_name', 'invalidbot_name'),
        ('bot_name', ''),
        ('bot_name', None),
        ('cluster_id', 'invalidcluster_id'),
        ('cluster_id', ''),
        ('cluster_id', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
        ('drop_fields', 'invaliddrop_fields'),
        ('drop_fields', ''),
        ('drop_fields', None),
    ])
    def test_api_RasBotManager_ListBotInvalidParam(self, invalidParam, config_obj, BotmanagerApi):
        """  中心manager bot查询，center manager拥有所有bot信息
route pref... """
        bot_name = None
        cluster_id = None
        status = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        drop_fields = None
        intef = BotmanagerApi.RasBotManager_ListBotGetApi(bot_name=bot_name, cluster_id=cluster_id, status=status, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, drop_fields=drop_fields, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('version', 'invalidversion'),
        ('version', ''),
        ('version', None),
        ('desc', 'invaliddesc'),
        ('desc', ''),
        ('desc', None),
        ('support_device_kind', 'invalidsupport_device_kind'),
        ('support_device_kind', ''),
        ('support_device_kind', None),
        ('bot_applets', 'invalidbot_applets'),
        ('bot_applets', ''),
        ('bot_applets', None),
        ('implements', 'invalidimplements'),
        ('implements', ''),
        ('implements', None),
        ('policy', 'invalidpolicy'),
        ('policy', ''),
        ('policy', None),
        ('policy_group', 'invalidpolicy_group'),
        ('policy_group', ''),
        ('policy_group', None),
        ('product_spus', 'invalidproduct_spus'),
        ('product_spus', ''),
        ('product_spus', None),
        ('product_spu_groups', 'invalidproduct_spu_groups'),
        ('product_spu_groups', ''),
        ('product_spu_groups', None),
        ('bot_modules', 'invalidbot_modules'),
        ('bot_modules', ''),
        ('bot_modules', None),
    ])
    def test_api_RasBotManager_UpsertBotInvalidParam(self, invalidParam, config_obj, BotmanagerApi):
        """  创建或者更新bot
route prefix= internal_prefix=ras action... """
        name = None
        version = None
        desc = None
        support_device_kind = None
        bot_applets = None
        implements = None
        policy = None
        policy_group = None
        product_spus = None
        product_spu_groups = None
        bot_modules = None
        intef = BotmanagerApi.RasBotManager_UpsertBotPostApi(name=name, version=version, desc=desc, support_device_kind=support_device_kind, bot_applets=bot_applets, implements=implements, policy=policy, policy_group=policy_group, product_spus=product_spus, product_spu_groups=product_spu_groups, bot_modules=bot_modules, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
