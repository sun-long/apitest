#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


@pytest.mark.skip("内部接口")
class TestBotmanagerScenario(object):
    """ Botmanager scenario test"""

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

    @pytest.mark.skip("手工测试用例")
    def test_scenario_000_botRegisterAndDeploy(self, BotmanagerApi):
        """ bot注册及部署流程	"""
        # 1.创建bot
        name = 'easy-bot-1'
        version = 'v1.0.0'
        resp = BotmanagerApi.createEasyBot(bot_name=name, bot_version=version)
        # 2.创建bot实例
        cluster_id = "2"
        module_name = resp.json_get("bots.0.bot_modules.0.name")
        resp = BotmanagerApi.RasBotManager_CreateBotInstancePostApi(name=name, version=version, module_name=module_name,
                                                                    cluster_id=cluster_id)
        assert resp.status_code == 200
        # 查询bot, 状态pending
        resp = BotmanagerApi.getBotsByName(name, cluster_id=cluster_id)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Pending"
        # 部署该bot(人工helm命令)
        i = 1
        # 查询bot, 状态running
        resp = BotmanagerApi.getBotsByName(name, cluster_id=cluster_id)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Running"
        # 卸载bot(人工helm命令)
        i = 1
        # 查询bot
        resp = BotmanagerApi.getBotsByName(name, cluster_id=cluster_id)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Pending"
        # 删除实例
        resp = BotmanagerApi.RasBotManager_DeleteBotInstanceGetApi(name=name, version=version, module_name=module_name, cluster_id=cluster_id)
        assert resp.status_code == 200
        # 删除bot
        resp = BotmanagerApi.RasBotManager_DeleteBotGetApi(name=name, version=version)
        assert resp.status_code == 200

    def test_scenario_001_botUpdate(self, BotmanagerApi, config_obj):
        """ bot更新(bot_modules修改无效)"""
        # 1.创建bot
        name = 'easy-bot-2'
        version = 'v1.0.0'
        resp = BotmanagerApi.createEasyBot(bot_name=name, bot_version=version)
        module_name = resp.json_get("bots.0.bot_modules.0.name")
        # 2.查询bot
        resp = BotmanagerApi.getBotsByName(name)
        assert resp.status_code == 200
        # 3.更新bot
        #     support_deviceKindType
        #     desc
        #     policy
        #     policy_group
        #     product_spu_groups
        #     product_spus
        #     bot_modules
        service = config_obj.Ras.botManager.serviceName
        desc = "updateDesc"  # 修改
        support_device_kind = [
            "updateDevice1",
            "updateDevice2",
            "updateDevice3",
        ] # 修改
        bot_applets = None
        implements = None
        policy = {
            "specs": [
                {
                    "name": "belt1:%s:%s:CreateDevice" % (name, version)  # 修改
                }
            ]
        }
        policy_group = [
            {
                "spec": {
                    "name": "demo_bot_create_assignment1",  # 修改
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
                    "name": "IDS0201update",  # 修改
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
                    "display_name": "身份验证全流程服务Update", # 修改
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
                "name": "easy_bot_main_new", # 修改
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
        resp = BotmanagerApi.RasBotManager_UpsertBotPostApi(name=name, version=version, desc=desc,
                                                            support_device_kind=support_device_kind,
                                                            bot_applets=bot_applets, implements=implements,
                                                            policy=policy, policy_group=policy_group,
                                                            product_spus=product_spus,
                                                            product_spu_groups=product_spu_groups,
                                                            bot_modules=bot_modules)
        assert resp.status_code == 200
        # 4.查询bot
        resp = BotmanagerApi.getBotsByName(name, drop_fields=[])
        assert resp.status_code == 200
        assert resp.json_get("bots.0.desc") == desc
        assert resp.json_get("bots.0.support_device_kind") == support_device_kind
        assert resp.json_get("bots.0.policy.specs.0.name") == policy["specs"][0]["name"]
        assert resp.json_get("bots.0.policy_group.0.spec.name") == policy_group[0]["spec"]["name"]
        assert resp.json_get("bots.0.product_spus.0.spec.name") == product_spus[0]["spec"]["name"]
        assert resp.json_get("bots.0.product_spu_groups.0.spec.display_name") == product_spu_groups[0]["spec"]["display_name"]
        assert resp.json_get("bots.0.bot_modules.0.name") == module_name, "预期不能修改"  # 不允许修改

        # 5.删除bot
        resp = BotmanagerApi.RasBotManager_DeleteBotGetApi(name=name, version=version)
        assert resp.status_code == 200

    @pytest.mark.skip("手工测试用例")
    def test_scenario_002_botInstanceDeleteFailed(self, BotmanagerApi):
        """ bot实例状态为running, 不允许删除该bot实例	"""
        # 1.创建bot
        name = 'easy-bot-1'
        version = 'v1.0.0'
        resp = BotmanagerApi.createEasyBot(bot_name=name, bot_version=version)
        # 2.创建bot实例
        cluster_id = "2"
        module_name = resp.json_get("bots.0.bot_modules.0.name")
        resp = BotmanagerApi.RasBotManager_CreateBotInstancePostApi(name=name, version=version, module_name=module_name,
                                                                    cluster_id=cluster_id)
        assert resp.status_code == 200
        # 3.查询bot, 状态pending
        resp = BotmanagerApi.getBotsByName(name, cluster_id=cluster_id)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Pending"
        # 4.部署该bot(人工helm命令)
        i = 1
        # 5.查询bot, 状态running
        resp = BotmanagerApi.getBotsByName(name, cluster_id=cluster_id)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Running"
        # 6.删除实例
        resp = BotmanagerApi.RasBotManager_DeleteBotInstanceGetApi(name=name, version=version, module_name=module_name,
                                                                   cluster_id=cluster_id)
        assert resp.status_code != 200
        # 7.卸载bot(人工helm命令)
        i = 1
        # 8.查询bot
        resp = BotmanagerApi.getBotsByName(name, cluster_id=cluster_id)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Pending"
        # 删除实例
        resp = BotmanagerApi.RasBotManager_DeleteBotInstanceGetApi(name=name, version=version, module_name=module_name,
                                                                   cluster_id=cluster_id)
        assert resp.status_code == 200
        # 删除bot
        resp = BotmanagerApi.RasBotManager_DeleteBotGetApi(name=name, version=version)
        assert resp.status_code == 200

    def test_scenario_003_botDeleteFailed(self, BotmanagerApi):
        """ bot中创建bot实例后, 不允许删除bot	"""
        # 1.创建bot
        name = 'easy-bot-1'
        version = 'v1.0.0'
        resp = BotmanagerApi.createEasyBot(bot_name=name, bot_version=version)
        # 2.创建bot实例
        cluster_id = "2"
        module_name = resp.json_get("bots.0.bot_modules.0.name")
        resp = BotmanagerApi.RasBotManager_CreateBotInstancePostApi(name=name, version=version, module_name=module_name,
                                                                    cluster_id=cluster_id)
        assert resp.status_code == 200
        # 3.删除bot
        resp = BotmanagerApi.RasBotManager_DeleteBotGetApi(name=name, version=version)
        assert resp.status_code != 200

        # 4.删除实例
        resp = BotmanagerApi.RasBotManager_DeleteBotInstanceGetApi(name=name, version=version, module_name=module_name,
                                                                   cluster_id=cluster_id)
        assert resp.status_code == 200
        # 5.删除bot
        resp = BotmanagerApi.RasBotManager_DeleteBotGetApi(name=name, version=version)
        assert resp.status_code == 200

    @pytest.mark.skip("手工测试用例")
    def test_scenario_004_botRegisterMutilCluster(self, BotmanagerApi):
        """ bot注册及部署2个cluster"""
        # 1.创建bot
        name = 'easy-bot-1'
        version = 'v1.0.0'
        resp = BotmanagerApi.createEasyBot(bot_name=name, bot_version=version)
        module_name = resp.json_get("bots.0.bot_modules.0.name")
        # 2.创建bot实例1
        cluster_id = "2"
        resp = BotmanagerApi.RasBotManager_CreateBotInstancePostApi(name=name, version=version, module_name=module_name,
                                                                    cluster_id=cluster_id)
        assert resp.status_code == 200
        # 3.创建bot实例2
        cluster_id_2 = "3"
        resp = BotmanagerApi.RasBotManager_CreateBotInstancePostApi(name=name, version=version, module_name=module_name,
                                                                    cluster_id=cluster_id_2)
        assert resp.status_code == 200
        # 4.查询bot, 状态pending
        resp = BotmanagerApi.getBotsByName(name)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Pending"
        assert resp.json_get("bots.0.bot_instances.1.status") == "Pending"
        # 部署该bot(人工helm命令)
        i = 1
        # 查询bot, 状态running
        resp = BotmanagerApi.getBotsByName(name)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Running"
        assert resp.json_get("bots.0.bot_instances.1.status") == "Running"
        # 卸载bot(人工helm命令)
        i = 1
        # 查询bot
        resp = BotmanagerApi.getBotsByName(name)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Pending"
        assert resp.json_get("bots.0.bot_instances.1.status") == "Pending"
        # 删除实例
        resp = BotmanagerApi.RasBotManager_DeleteBotInstanceGetApi(name=name, version=version, module_name=module_name,
                                                                   cluster_id=cluster_id)
        assert resp.status_code == 200
        resp = BotmanagerApi.RasBotManager_DeleteBotInstanceGetApi(name=name, version=version, module_name=module_name,
                                                                   cluster_id=cluster_id_2)
        assert resp.status_code == 200
        # 删除bot
        resp = BotmanagerApi.RasBotManager_DeleteBotGetApi(name=name, version=version)
        assert resp.status_code == 200

    @pytest.mark.skip("手工测试用例")
    def test_scenario_005_botMutilVersion(self, BotmanagerApi):
        """ bot注册及部署2个version"""
        # 1.创建bot1
        name = 'easy-bot-1'
        version = 'v1.0.0'
        resp = BotmanagerApi.createEasyBot(bot_name=name, bot_version=version)
        module_name = resp.json_get("bots.0.bot_modules.0.name")

        # 2.创建bot2
        name = 'easy-bot-1'
        version_2 = 'v2.0.0'
        resp = BotmanagerApi.createEasyBot(bot_name=name, bot_version=version_2)

        # 3.创建bot实例 For v1.0.0
        cluster_id = "2"
        resp = BotmanagerApi.RasBotManager_CreateBotInstancePostApi(name=name, version=version, module_name=module_name,
                                                                    cluster_id=cluster_id)
        assert resp.status_code == 200

        # 4.创建bot实例 For v2.0.0
        resp = BotmanagerApi.RasBotManager_CreateBotInstancePostApi(name=name, version=version_2, module_name=module_name,
                                                                    cluster_id=cluster_id)
        assert resp.status_code == 200
        # 5.查询bot, 状态pending
        resp = BotmanagerApi.getBotsByName(name, cluster_id=cluster_id)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Pending"
        assert resp.json_get("bots.1.bot_instances.0.status") == "Pending"
        # 部署该bot(人工helm命令)
        i = 1
        # 查询bot, 状态running
        resp = BotmanagerApi.getBotsByName(name, cluster_id=cluster_id)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Running"
        assert resp.json_get("bots.1.bot_instances.0.status") == "Running"
        # 卸载bot(人工helm命令)
        i = 1
        # 查询bot
        resp = BotmanagerApi.getBotsByName(name, cluster_id=cluster_id)
        assert resp.status_code == 200
        assert resp.json_get("bots.0.bot_instances.0.status") == "Pending"
        assert resp.json_get("bots.1.bot_instances.0.status") == "Pending"
        # 删除实例
        resp = BotmanagerApi.RasBotManager_DeleteBotInstanceGetApi(name=name, version=version, module_name=module_name,
                                                                   cluster_id=cluster_id)
        assert resp.status_code == 200
        resp = BotmanagerApi.RasBotManager_DeleteBotInstanceGetApi(name=name, version=version_2, module_name=module_name,
                                                                   cluster_id=cluster_id)
        assert resp.status_code == 200

        # 删除bot
        resp = BotmanagerApi.RasBotManager_DeleteBotGetApi(name=name, version=version)
        assert resp.status_code == 200
        resp = BotmanagerApi.RasBotManager_DeleteBotGetApi(name=name, version=version_2)
        assert resp.status_code == 200

    def test_scenario_006_ListBotByBotName(self, BotmanagerApi, config_obj):
        """ 根据bot名称查询列表"""
        bot_name = config_obj.Bot.aide.name
        cluster_id = None
        status = None  # Running / Pending
        paging_offset = None
        paging_limit = None
        drop_fields = ['policy',
                       'bot_modules',
                       'policy_group',
                       'product_spu_groups', 'product_spus']
        # drop_fields =None
        resp = BotmanagerApi.RasBotManager_ListBotGetApi(bot_name=bot_name, cluster_id=cluster_id,
                                                         status=status, paging_offset=paging_offset,
                                                         paging_limit=paging_limit, paging_total=None,
                                                         drop_fields=drop_fields)
        assert resp.status_code == 200
        assert resp.json_get("bots")
        assert len(resp.json_get("bots")) == 1
        assert resp.json_get("bots.0.name") == bot_name

    def test_scenario_005_ListBotByClusterId(self, BotmanagerApi, config_obj):
        """ 根据bot的cluster查询列表"""
        bot_name = None
        cluster_id = config_obj.Bot.aide.cluster_id
        status = None  # Running / Pending
        paging_offset = None
        paging_limit = None
        drop_fields = ['policy',
                       'bot_modules',
                       'policy_group',
                       'product_spu_groups', 'product_spus']
        # drop_fields =None
        resp = BotmanagerApi.RasBotManager_ListBotGetApi(bot_name=bot_name, cluster_id=cluster_id,
                                                         status=status, paging_offset=paging_offset,
                                                         paging_limit=paging_limit, paging_total=None,
                                                         drop_fields=drop_fields)
        assert resp.status_code == 200
        assert resp.json_get("bots")
        assert len(resp.json_get("bots")) > 0
        for bot in resp.json_get("bots"):
            for instance in bot["bot_instances"]:
                assert instance["cluster"]["id"] == cluster_id

    @pytest.mark.parametrize("status", ["Running", "Pending"])
    def test_scenario_005_ListBotByStatus(self, BotmanagerApi, status):
        """ 根据bot的status查询列表"""
        bot_name = None
        cluster_id = None
        paging_offset = None
        paging_limit = None
        drop_fields = ['policy',
                       'bot_modules',
                       'policy_group',
                       'product_spu_groups', 'product_spus']
        # drop_fields =None
        resp = BotmanagerApi.RasBotManager_ListBotGetApi(bot_name=bot_name, cluster_id=cluster_id,
                                                         status=status, paging_offset=paging_offset,
                                                         paging_limit=paging_limit, paging_total=None,
                                                         drop_fields=drop_fields)
        assert resp.status_code == 200
        assert resp.json_get("bots")
        assert len(resp.json_get("bots")) > 0
        for bot in resp.json_get("bots"):
            for instance in bot["bot_instances"]:
                assert instance["status"] == status

    def test_scenario_005_ListBotByPaging(self, BotmanagerApi):
        """ 根据bot的cluster查询列表"""
        bot_name = None
        cluster_id = None
        status = None  # Running / Pending
        paging_offset = 1
        paging_limit = 1
        drop_fields = ['policy',
                       'bot_modules',
                       'policy_group',
                       'product_spu_groups', 'product_spus']
        # drop_fields =None
        resp = BotmanagerApi.RasBotManager_ListBotGetApi(bot_name=bot_name, cluster_id=cluster_id,
                                                         status=status, paging_offset=paging_offset,
                                                         paging_limit=paging_limit, paging_total=None,
                                                         drop_fields=drop_fields)
        assert resp.status_code == 200
        assert resp.json_get("bots")
        assert len(resp.json_get("bots")) == 1
        assert resp.json_get("paging.limit") == 1
        assert resp.json_get("paging.offset") == 1

    # @pytest.mark.skip("内部接口")
    def test_scenario_006_GetBot(self, BotmanagerApi):
        """ getBot接口查询"""
        bot_name = None
        cluster_id = None
        status = None
        paging_offset = None
        paging_limit = None
        drop_fields = ['policy',
                       'policy_group',
                       'product_spu_groups', 'product_spus']
        # drop_fields =None
        resp = BotmanagerApi.RasBotManager_ListBotGetApi(bot_name=bot_name, cluster_id=cluster_id,
                                                         status=status, paging_offset=paging_offset,
                                                         paging_limit=paging_limit, paging_total=None,
                                                         drop_fields=drop_fields)
        assert resp.status_code == 200
        assert resp.json_get("bots")
        action = resp.json_get("bots.0.bot_modules.0.routes.0.action")
        prefix = resp.json_get("bots.0.bot_modules.0.routes.0.prefix")
        version = resp.json_get("bots.0.bot_modules.0.routes.0.version")

        resp = BotmanagerApi.RasBotManager_GetBotGetApi(action=action, version=version, prefix=prefix)
        assert resp.status_code == 200
        assert len(resp.json_get("bots")) > 0
        log().info("bots num:%s" % len(resp.json_get("bots")))