#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.botmanager_service_swagger import BotmanagerSwaggerApi


"""
使用说明：


"""

TOKEN_NAME = "Authorization"
TOKEN_VALUE = "Bearer %s"  # token默认信息


class BotmanagerSwaggerBusiness(BotmanagerSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(BotmanagerSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Token"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        inte_obj.set_headers('X-Belt-Action', inte_obj.path_action)
        inte_obj.set_headers('X-Belt-Version', inte_obj.path_version)

    def createEasyBot(self, bot_name='easy-bot', bot_version='v1.0.0', support_device_kind=None):
        """ 创建easy-bot"""
        service = self.config_obj.Ras.botManager.serviceName
        name = bot_name
        version = bot_version
        desc = "test_demo"
        if not support_device_kind:
            support_device_kind = ["demo_device"]
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
        # bot_instances = [
        #     {
        #         "cluster": {
        #             "id": cluster_id
        #         }
        #     }
        # ]
        resp = self.RasBotManager_UpsertBotPostApi(name=name, version=version, desc=desc,
                                                   support_device_kind=support_device_kind,
                                                   bot_applets=bot_applets, implements=implements,
                                                   policy=policy, policy_group=policy_group,
                                                   product_spus=product_spus,
                                                   product_spu_groups=product_spu_groups,
                                                   bot_modules=bot_modules)
        assert resp.status_code == 200
        return self.getBotsByName(bot_name, drop_fields=[], print_log=False)

    def getBotsByName(self, bot_name, cluster_id=None, status=None, drop_fields=None, print_log=True):
        """ 根据bot名字查询bot信息"""
        paging_offset = 0
        paging_limit = 100
        if drop_fields is None:
            drop_fields = ['policy',
                           'bot_modules',
                           'policy_group',
                           'product_spu_groups', 'product_spus']
        # drop_fields =None
        resp = self.RasBotManager_ListBotGetApi(bot_name=bot_name, cluster_id=cluster_id,
                                                status=status, paging_offset=paging_offset,
                                                paging_limit=paging_limit, paging_total=None,
                                                drop_fields=drop_fields, print_log=print_log)
        return resp