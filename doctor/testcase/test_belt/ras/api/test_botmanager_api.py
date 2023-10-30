#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestBotmanagerApi(object):
    """ botManager Api测试"""

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

    def test_api_RasBotManager_CreateBotInstance(self, config_obj, BotmanagerApi):
        """  创建bot instance
一个instance 是一个bot module的部署实例
route... """
        name = "easy-bot-1"
        version = "v1.0.0"
        module_name = "easy_bot_main"
        cluster_id = "2"
        resp = BotmanagerApi.RasBotManager_CreateBotInstancePostApi(name=name, version=version, module_name=module_name, cluster_id=cluster_id)
        assert resp.status_code == 200

    def test_api_RasBotManager_DeleteBot(self, config_obj, BotmanagerApi):
        """  删除bot
route prefix= internal_prefix=ras action=Del... """
        name = "easy-bot-1"
        version = "v1.0.0"
        resp = BotmanagerApi.RasBotManager_DeleteBotGetApi(name=name, version=version)
        assert resp.status_code == 200

    def test_api_RasBotManager_DeleteBotInstance(self, config_obj, BotmanagerApi):
        """  删除bot instance
route prefix= internal_prefix=ras a... """
        name = "easy-bot-1"
        version = "v1.0.0"
        module_name = "easy_bot_main"
        cluster_id = "2"
        resp = BotmanagerApi.RasBotManager_DeleteBotInstanceGetApi(name=name, version=version, module_name=module_name, cluster_id=cluster_id)
        assert resp.status_code == 200

    def test_api_RasBotManager_EdgeReportBotState(self, config_obj, BotmanagerApi):
        """  边manager 上报bot状态，包括探活、pipeline等信息
route prefix= in... """
        edge_bot_status = None
        cluster_id = None
        resp = BotmanagerApi.RasBotManager_EdgeReportBotStatePostApi(edge_bot_status=edge_bot_status, cluster_id=cluster_id)
        assert resp.status_code == 200

    def test_api_RasBotManager_GetBot(self, config_obj, BotmanagerApi):
        """  action + version + prefix 查询bot
route prefix= inte... """
        action = 'CreateAssignment'
        version = 'v1'
        prefix = 'ras'
        resp = BotmanagerApi.RasBotManager_GetBotGetApi(action=action, version=version, prefix=prefix)
        assert resp.status_code == 200
        log().info("bots num:%s" % len(resp.json_get("bots")))

    def test_api_RasBotManager_ListBot(self, config_obj, BotmanagerApi):
        """  中心manager bot查询，center manager拥有所有bot信息
route pref... """
        # bot_name = "fell-detective"
        bot_name = None
        # bot_name = "easy-bot"
        cluster_id = None
        status = None  # Running / Pending
        paging_offset = 0
        paging_limit = 10
        drop_fields = [
            'policy',
                       'bot_modules',
                       'policy_group',
                       'product_spu_groups',
            'product_spus'
        ]
        # drop_fields =None
        resp = BotmanagerApi.RasBotManager_ListBotGetApi(bot_name=bot_name, cluster_id=cluster_id,
                                                         status=status, paging_offset=paging_offset,
                                                         paging_limit=paging_limit, paging_total=None,
                                                         drop_fields=drop_fields)
        assert resp.status_code == 200
        log().info("bots num:%s" % len(resp.json_get("bots")))
        # log().info("status:%s" % resp.json_get("bots.0.bot_instances.0.status"))

    def test_api_RasBotManager_UpsertBot(self, config_obj, BotmanagerApi):
        """  创建或者更新bot
route prefix= internal_prefix=ras action... """
        service = config_obj.Ras.botManager.serviceName
        name = "easy-bot-1"
        version = "v1.0.0"
        desc = "a test demoxxxx"
        support_device_kind = [
            "demo_device1",  # 设备管理中创建的设备类型名称
            "my_device"  # 设备管理中创建的设备类型名称
        ]
        bot_applets = None
        implements = None
        policy = {
            "specs": [
                {
                    "name": "belt:%s:%s:CreateDevice" % (name, version)  # 假的
                }
            ]
        }
        policy_group = [
            {
                "spec": {
                    "name": "demo_bot_create_assignment",
                    "type": "assignment",
                    "policies": [
                        "belt:%s:%s:Create" % (name, version)
                    ]
                }
            },
            {
                "spec": {
                    "name": "demo_bot_update_assignment",
                    "type": "assignment",
                    "policies": [
                        "belt:%s:%s:Update" % (name, version)
                    ]
                }
            },
            {
                "spec": {
                    "name": "demo_bot_get_assignment",
                    "type": "assignment",
                    "policies": [
                        "belt:%s:%s:Get" % (name, version)
                    ]
                }
            },
            {
                "spec": {
                    "name": "demo_bot_delete_assignment",
                    "type": "assignment",
                    "policies": [
                        "belt:%s:%s:delete" % (name, version)
                    ]
                }
            }
        ]
        product_spus = [
            {
                "version": "v1",
                "spec": {
                    "name": "IDS0201",
                    "category": "category001-3",
                    "display_name": "人脸1:1",
                    "description": "产品具体描述",
                    "notice": "购买须知",
                    "value_points": [
                        "xxxx"
                    ],
                    "policy_group": [
                        "$plocyGroupName"
                    ],
                    "sku": [
                        {
                            "name": "IDS0201-sku1",
                            "metric": "counter",
                            "pay_type": "stprering",
                            "spec": [
                                {
                                    "key": "计费模式",
                                    "value": "按量计费(大)"
                                }
                            ],
                            "price": {
                                "unit": {
                                    "name": "元/次",
                                    "factor": "1"
                                },
                                "site_id": "xx",
                                "rule": [
                                    {
                                        "end": "10000",
                                        "unit_price": "1",
                                        "type": 1,
                                        "display_name": "调用量1w以下"
                                    },
                                    {
                                        "unit_price": "1",
                                        "type": 1,
                                        "display_name": "调用量1w以下"
                                    }
                                ]
                            }
                        },
                        {
                            "name": " IDS0201-sku2",
                            "metric": "counter",
                            "pay_type": "pre",
                            "spec": [
                                {
                                    "key": "计费模式",
                                    "value": "按量计费(中)"
                                }
                            ]
                        }
                    ]
                }
            }
        ]
        product_spu_groups = [
            {
                "version": "v1",
                "spec": {
                    "name": "IDS0101",
                    "display_name": "身份验证全流程服务",
                    "category": "category001-3",
                    "description": "产品具体描述",
                    "notice": "购买须知",
                    "sku": [
                        "IDS0201",
                        "IDS0202",
                        "IDS0203"
                    ],
                    "sku_group": [
                        {
                            "sku_sub_group": [
                                "IDS0101-sku1",
                                "IDS0101-sku2"
                            ]
                        },
                        {
                            "sku_sub_group": [
                                "IDS0101-sku3",
                                "IDS0101-sku4"
                            ]
                        }
                    ]
                }
            }
        ]
        bot_modules = [
            {
                "name": "easy_bot_main",
                "hostname": "%s.%s" % (name, service),
                "version": "%s" % version,
                "singleton": True,
                "liveness": {
                    "liveness_type": "HTTP",
                    "port": 8080,
                    "path": "/bot/assignment"
                },
                "routes": [
                    {
                        "type": "assignment",
                        "upstream": {
                            "service_name": "%s.%s" % (name, service),
                            "port": 8081
                        },
                        "path": "/v1/CreateAssignment",
                        "method": "POST",
                        "action": "CreateAssignment",
                        "version": "v1",
                        # "prefix": "sku"
                        "prefix": "ras"
                    },
                    {
                        "type": "assignment",
                        "upstream": {
                            "service_name": "%s.%s" % (name, service),
                            "port": 8081
                        },
                        "path": "/v1/UpdateAssignment",
                        "method": "POST",
                        "action": "UpdateAssignment",
                        "version": "v1",
                        "prefix": "sku"
                    },
                    {
                        "type": "assignment",
                        "upstream": {
                            "service_name": "%s.%s" % (name, service),
                            "port": 8081
                        },
                        "path": "/v1/GetAssignment",
                        "method": "POST",
                        "action": "GetAssignment",
                        "version": "v1",
                        "prefix": "sku"
                    },
                    {
                        "type": "assignment",
                        "upstream": {
                            "service_name": "%s.%s" % (name, service),
                            "port": 8081
                        },
                        "path": "/v1/DeleteAssignment",
                        "method": "POST",
                        "action": "DeleteAssignment",
                        "version": "v1",
                        "prefix": "sku"
                    }
                ]
            }
        ]
        resp = BotmanagerApi.RasBotManager_UpsertBotPostApi(name=name, version=version, desc=desc, support_device_kind=support_device_kind, bot_applets=bot_applets, implements=implements, policy=policy, policy_group=policy_group, product_spus=product_spus, product_spu_groups=product_spu_groups, bot_modules=bot_modules)
        assert resp.status_code == 200
