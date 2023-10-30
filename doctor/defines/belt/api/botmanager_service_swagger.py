#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class BotmanagerSwaggerApi(BaseApi):
    """ web接口"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        self.host = host
        self.ext_info = ext_info
        self.config_obj = config_obj
        self.token = token
        self.host_map = self.readHostMap(collections.name)
        self.TOKEN_NAME = ""
        self.TOKEN_VALUE = "%s"  # token默认信息
        collections.init(self, conf=config_obj, ext_info=ext_info)

    def genPostMan(self):
        """ 生成postman接口文件"""
        self.ext_info.isRequestOpened = True
        self.genPostManFromSwagger(collections)

    def RasBotManager_CreateBotInstancePostApi(self, name=None, version=None, module_name=None, cluster_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建bot instance
一个instance 是一个bot module的部署实例
route... """
        """  path: [post]/v1/CreateBotInstance API """
        """  body: 
                {
                    "cluster_id": "",
                    "module_name": "",
                    "name": "",
                    "version": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("botManager", "RasBotManager_CreateBotInstance")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("version", version)
        intef.update_body("module_name", module_name)
        intef.update_body("cluster_id", cluster_id)
        return intef.request() if sendRequest else intef

    def RasBotManager_DeleteBotPostApi(self, name=None, version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除bot
route prefix= internal_prefix=ras action=Del... """
        """  path: [post]/v1/DeleteBot API """
        """  body: 
                {
                    "name": "",
                    "version": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("botManager", "RasBotManager_DeleteBot")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("version", version)
        return intef.request() if sendRequest else intef

    def RasBotManager_DeleteBotInstancePostApi(self, name=None, version=None, module_name=None, cluster_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除bot instance
route prefix= internal_prefix=ras a... """
        """  path: [post]/v1/DeleteBotInstance API """
        """  body: 
                {
                    "cluster_id": "",
                    "module_name": "",
                    "name": "",
                    "version": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("botManager", "RasBotManager_DeleteBotInstance")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("version", version)
        intef.update_body("module_name", module_name)
        intef.update_body("cluster_id", cluster_id)
        return intef.request() if sendRequest else intef

    def RasBotManager_EdgeReportBotStatePostApi(self, edge_bot_status=None, cluster_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  边manager 上报bot状态，包括探活、pipeline等信息
route prefix= in... """
        """  path: [post]/v1/EdgeReportBotState API """
        """  body: 
                {
                    "cluster_id": "",
                    "edge_bot_status": [
                        {
                            "bot_id": "",
                            "status": "[BotStatus_Unknown]BotStatus_Unknown/Pending/Running"
                        }
                    ]
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("botManager", "RasBotManager_EdgeReportBotState")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("edge_bot_status", edge_bot_status)
        intef.update_body("cluster_id", cluster_id)
        return intef.request() if sendRequest else intef

    def RasBotManager_GetBotGetApi(self, action=None, version=None, prefix=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  action + version + prefix 查询bot
route prefix= inte... """
        """  path: [get]/v1/GetBot API """
        """  params: 
                参数名称：action　类型：string　描述：null
                参数名称：version　类型：string　描述：null
                参数名称：prefix　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "bots": [
                        {
                            "bot_applets": [
                                {
                                    "desc": "",
                                    "name": "",
                                    "version": ""
                                }
                            ],
                            "bot_instances": [
                                {
                                    "cluster": {
                                        "id": "",
                                        "infra_cluster_id": "",
                                        "name": "",
                                        "private_ingress": "",
                                        "public_ingress": "",
                                        "site_id": "",
                                        "type": "[CT_UNKNOWN]CT_UNKNOWN/CT_CENTER/CT_EDGE"
                                    },
                                    "created_at": "",
                                    "module_name": "",
                                    "status": "[BotStatus_Unknown]BotStatus_Unknown/Pending/Running",
                                    "updated_at": ""
                                }
                            ],
                            "bot_modules": [
                                {
                                    "hostname": "",
                                    "liveness": {
                                        "interval": 0,
                                        "liveness_type": "[LivenessType_Unknown]LivenessType_Unknown/TCP/HTTP",
                                        "path": "",
                                        "port": 0,
                                        "ready_delay": 0
                                    },
                                    "name": "",
                                    "resources": {
                                        "ars": [
                                            {
                                                "version": ""
                                            }
                                        ],
                                        "ips": [
                                            {
                                                "feature_version": "",
                                                "object_type": "",
                                                "version": ""
                                            }
                                        ],
                                        "sfd": [
                                            {
                                                "feature_version": "",
                                                "version": ""
                                            }
                                        ],
                                        "vps": [
                                            {
                                                "version": ""
                                            }
                                        ]
                                    },
                                    "routes": [
                                        {
                                            "route_type": "[RouteType_Unknown]RouteType_Unknown/Public/Private/Local",
                                            "spec": {
                                                "services": [
                                                    {
                                                        "connect_timeout": "",
                                                        "name": "",
                                                        "read_timeout": "",
                                                        "routes": [
                                                            {
                                                                "headers": {
                                                                    "additionalProp1": [],
                                                                    "additionalProp2": [],
                                                                    "additionalProp3": []
                                                                },
                                                                "methods": [],
                                                                "name": "",
                                                                "paths": [],
                                                                "strip_path": false
                                                            }
                                                        ],
                                                        "url": "",
                                                        "write_timeout": ""
                                                    }
                                                ]
                                            },
                                            "version": ""
                                        }
                                    ],
                                    "singleton": false,
                                    "version": ""
                                }
                            ],
                            "desc": "",
                            "implements": {
                                "assignment_interface": {
                                    "port": 0,
                                    "service": ""
                                },
                                "data_collecting_interface": {
                                    "port": 0,
                                    "service": ""
                                }
                            },
                            "name": "",
                            "policy": {
                                "specs": [
                                    {
                                        "desc": "",
                                        "name": ""
                                    }
                                ]
                            },
                            "policy_group": [
                                {
                                    "spec": {
                                        "name": "",
                                        "policies": [],
                                        "type": ""
                                    }
                                }
                            ],
                            "product_spu_groups": [
                                {
                                    "spec": {
                                        "category": "",
                                        "description": "",
                                        "display_name": "",
                                        "name": "",
                                        "notice": "",
                                        "sku": [],
                                        "sku_group": [
                                            {
                                                "sku_sub_group": []
                                            }
                                        ]
                                    },
                                    "version": ""
                                }
                            ],
                            "product_spus": [
                                {
                                    "spec": {
                                        "category": "",
                                        "description": "",
                                        "display_name": "",
                                        "name": "",
                                        "notice": "",
                                        "policy_group": [],
                                        "sku": [
                                            {
                                                "metric": "",
                                                "name": "",
                                                "pay_type": "",
                                                "price": [
                                                    {
                                                        "rule": [
                                                            {
                                                                "display_name": "",
                                                                "end": "",
                                                                "start": "",
                                                                "type": 0,
                                                                "unit_price": 0
                                                            }
                                                        ],
                                                        "site_id": "",
                                                        "unit": {
                                                            "factor": 0,
                                                            "name": ""
                                                        }
                                                    }
                                                ],
                                                "spec": [
                                                    {
                                                        "key": "",
                                                        "value": ""
                                                    }
                                                ]
                                            }
                                        ],
                                        "value_points": []
                                    },
                                    "version": ""
                                }
                            ],
                            "support_device_kind": [],
                            "version": ""
                        }
                    ],
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("botManager", "RasBotManager_GetBot")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("action", action)
        intef.update_params("version", version)
        intef.update_params("prefix", prefix)
        return intef.request() if sendRequest else intef

    def RasBotManager_ListBotGetApi(self, bot_name=None, cluster_id=None, status=None, paging_offset=None, paging_limit=None, paging_total=None, drop_fields=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  中心manager bot查询，center manager拥有所有bot信息
route pref... """
        """  path: [get]/v1/ListBot API """
        """  params: 
                参数名称：bot_name　类型：string　描述：按name过滤
                参数名称：cluster_id　类型：string　描述：按cluster_id过滤
                参数名称：status　类型：string　描述：按status过滤
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：null
                参数名称：drop_fields　类型：array　描述：bot 字段很多 不用的字段可以设置drop_fields 减小请
        """
        """  resp:
                200(A successful response.):
                {
                    "bots": [
                        {
                            "bot_applets": [
                                {
                                    "desc": "",
                                    "name": "",
                                    "version": ""
                                }
                            ],
                            "bot_instances": [
                                {
                                    "cluster": {
                                        "id": "",
                                        "infra_cluster_id": "",
                                        "name": "",
                                        "private_ingress": "",
                                        "public_ingress": "",
                                        "site_id": "",
                                        "type": "[CT_UNKNOWN]CT_UNKNOWN/CT_CENTER/CT_EDGE"
                                    },
                                    "created_at": "",
                                    "module_name": "",
                                    "status": "[BotStatus_Unknown]BotStatus_Unknown/Pending/Running",
                                    "updated_at": ""
                                }
                            ],
                            "bot_modules": [
                                {
                                    "hostname": "",
                                    "liveness": {
                                        "interval": 0,
                                        "liveness_type": "[LivenessType_Unknown]LivenessType_Unknown/TCP/HTTP",
                                        "path": "",
                                        "port": 0,
                                        "ready_delay": 0
                                    },
                                    "name": "",
                                    "resources": {
                                        "ars": [
                                            {
                                                "version": ""
                                            }
                                        ],
                                        "ips": [
                                            {
                                                "feature_version": "",
                                                "object_type": "",
                                                "version": ""
                                            }
                                        ],
                                        "sfd": [
                                            {
                                                "feature_version": "",
                                                "version": ""
                                            }
                                        ],
                                        "vps": [
                                            {
                                                "version": ""
                                            }
                                        ]
                                    },
                                    "routes": [
                                        {
                                            "route_type": "[RouteType_Unknown]RouteType_Unknown/Public/Private/Local",
                                            "spec": {
                                                "services": [
                                                    {
                                                        "connect_timeout": "",
                                                        "name": "",
                                                        "read_timeout": "",
                                                        "routes": [
                                                            {
                                                                "headers": {
                                                                    "additionalProp1": [],
                                                                    "additionalProp2": [],
                                                                    "additionalProp3": []
                                                                },
                                                                "methods": [],
                                                                "name": "",
                                                                "paths": [],
                                                                "strip_path": false
                                                            }
                                                        ],
                                                        "url": "",
                                                        "write_timeout": ""
                                                    }
                                                ]
                                            },
                                            "version": ""
                                        }
                                    ],
                                    "singleton": false,
                                    "version": ""
                                }
                            ],
                            "desc": "",
                            "implements": {
                                "assignment_interface": {
                                    "port": 0,
                                    "service": ""
                                },
                                "data_collecting_interface": {
                                    "port": 0,
                                    "service": ""
                                }
                            },
                            "name": "",
                            "policy": {
                                "specs": [
                                    {
                                        "desc": "",
                                        "name": ""
                                    }
                                ]
                            },
                            "policy_group": [
                                {
                                    "spec": {
                                        "name": "",
                                        "policies": [],
                                        "type": ""
                                    }
                                }
                            ],
                            "product_spu_groups": [
                                {
                                    "spec": {
                                        "category": "",
                                        "description": "",
                                        "display_name": "",
                                        "name": "",
                                        "notice": "",
                                        "sku": [],
                                        "sku_group": [
                                            {
                                                "sku_sub_group": []
                                            }
                                        ]
                                    },
                                    "version": ""
                                }
                            ],
                            "product_spus": [
                                {
                                    "spec": {
                                        "category": "",
                                        "description": "",
                                        "display_name": "",
                                        "name": "",
                                        "notice": "",
                                        "policy_group": [],
                                        "sku": [
                                            {
                                                "metric": "",
                                                "name": "",
                                                "pay_type": "",
                                                "price": [
                                                    {
                                                        "rule": [
                                                            {
                                                                "display_name": "",
                                                                "end": "",
                                                                "start": "",
                                                                "type": 0,
                                                                "unit_price": 0
                                                            }
                                                        ],
                                                        "site_id": "",
                                                        "unit": {
                                                            "factor": 0,
                                                            "name": ""
                                                        }
                                                    }
                                                ],
                                                "spec": [
                                                    {
                                                        "key": "",
                                                        "value": ""
                                                    }
                                                ]
                                            }
                                        ],
                                        "value_points": []
                                    },
                                    "version": ""
                                }
                            ],
                            "support_device_kind": [],
                            "version": ""
                        }
                    ],
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("botManager", "RasBotManager_ListBot")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("bot_name", bot_name)
        intef.update_params("cluster_id", cluster_id)
        intef.update_params("status", status)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        intef.update_params("drop_fields", drop_fields)
        return intef.request() if sendRequest else intef

    def RasBotManager_UpsertBotPostApi(self, name=None, version=None, desc=None, support_device_kind=None, bot_applets=None, implements=None, policy=None, policy_group=None, product_spus=None, product_spu_groups=None, bot_modules=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建或者更新bot
route prefix= internal_prefix=ras action... """
        """  path: [post]/v1/UpsertBot API """
        """  body: 
                {
                    "bot_applets": [
                        {
                            "desc": "",
                            "name": "",
                            "version": ""
                        }
                    ],
                    "bot_modules": [
                        {
                            "hostname": "",
                            "liveness": {
                                "interval": 0,
                                "liveness_type": "[LivenessType_Unknown]LivenessType_Unknown/TCP/HTTP",
                                "path": "",
                                "port": 0,
                                "ready_delay": 0
                            },
                            "name": "",
                            "resources": {
                                "ars": [
                                    {
                                        "version": ""
                                    }
                                ],
                                "ips": [
                                    {
                                        "feature_version": "",
                                        "object_type": "",
                                        "version": ""
                                    }
                                ],
                                "sfd": [
                                    {
                                        "feature_version": "",
                                        "version": ""
                                    }
                                ],
                                "vps": [
                                    {
                                        "version": ""
                                    }
                                ]
                            },
                            "routes": [
                                {
                                    "route_type": "[RouteType_Unknown]RouteType_Unknown/Public/Private/Local",
                                    "spec": {
                                        "services": [
                                            {
                                                "connect_timeout": "",
                                                "name": "",
                                                "read_timeout": "",
                                                "routes": [
                                                    {
                                                        "headers": {
                                                            "additionalProp1": [],
                                                            "additionalProp2": [],
                                                            "additionalProp3": []
                                                        },
                                                        "methods": [],
                                                        "name": "",
                                                        "paths": [],
                                                        "strip_path": false
                                                    }
                                                ],
                                                "url": "",
                                                "write_timeout": ""
                                            }
                                        ]
                                    },
                                    "version": ""
                                }
                            ],
                            "singleton": false,
                            "version": ""
                        }
                    ],
                    "desc": "",
                    "implements": {
                        "assignment_interface": {
                            "port": 0,
                            "service": ""
                        },
                        "data_collecting_interface": {
                            "port": 0,
                            "service": ""
                        }
                    },
                    "name": "",
                    "policy": {
                        "specs": [
                            {
                                "desc": "",
                                "name": ""
                            }
                        ]
                    },
                    "policy_group": [
                        {
                            "spec": {
                                "name": "",
                                "policies": [],
                                "type": ""
                            }
                        }
                    ],
                    "product_spu_groups": [
                        {
                            "spec": {
                                "category": "",
                                "description": "",
                                "display_name": "",
                                "name": "",
                                "notice": "",
                                "sku": [],
                                "sku_group": [
                                    {
                                        "sku_sub_group": []
                                    }
                                ]
                            },
                            "version": ""
                        }
                    ],
                    "product_spus": [
                        {
                            "spec": {
                                "category": "",
                                "description": "",
                                "display_name": "",
                                "name": "",
                                "notice": "",
                                "policy_group": [],
                                "sku": [
                                    {
                                        "metric": "",
                                        "name": "",
                                        "pay_type": "",
                                        "price": [
                                            {
                                                "rule": [
                                                    {
                                                        "display_name": "",
                                                        "end": "",
                                                        "start": "",
                                                        "type": 0,
                                                        "unit_price": 0
                                                    }
                                                ],
                                                "site_id": "",
                                                "unit": {
                                                    "factor": 0,
                                                    "name": ""
                                                }
                                            }
                                        ],
                                        "spec": [
                                            {
                                                "key": "",
                                                "value": ""
                                            }
                                        ]
                                    }
                                ],
                                "value_points": []
                            },
                            "version": ""
                        }
                    ],
                    "support_device_kind": [],
                    "version": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("botManager", "RasBotManager_UpsertBot")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("version", version)
        intef.update_body("desc", desc)
        intef.update_body("support_device_kind", support_device_kind)
        intef.update_body("bot_applets", bot_applets)
        intef.update_body("implements", implements)
        intef.update_body("policy", policy)
        intef.update_body("policy_group", policy_group)
        intef.update_body("product_spus", product_spus)
        intef.update_body("product_spu_groups", product_spu_groups)
        intef.update_body("bot_modules", bot_modules)
        return intef.request() if sendRequest else intef

