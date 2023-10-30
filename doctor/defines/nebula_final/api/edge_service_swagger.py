#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nebula_final")

TOKEN_NAME = "Authorization"
TOKEN_VALUE = "Bearer %s"  # token默认信息


class EdgeSwaggerApi(BaseApi):
    """ web接口"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        self.host = host
        self.ext_info = ext_info
        self.config_obj = config_obj
        self.token = token
        self.host_map = self.readHostMap(collections.name)
        collections.init(self, conf=config_obj, ext_info=ext_info)

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(TOKEN_NAME, TOKEN_VALUE % self.token)

    def genPostMan(self):
        """ 生成postman接口文件"""
        self.ext_info.isRequestOpened = True
        self.genPostManFromSwagger(collections)

    def AppletManagerSrv_ActivationCodeInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  ActivationCodeInfo 查看当前激活信息. """
        """  path: [get]/v1/activation_code API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "activationCodeInfo": {
                        "code_info": [
                            {
                                "auth_id": {
                                    "dongle_ids": [],
                                    "match_rules": [
                                        {
                                            "match_mode": "[MATCH_NAME_EXACTLY]MATCH_NAME_EXACTLY/MATCH_NAME_PREFIX",
                                            "pattern": ""
                                        }
                                    ],
                                    "user_algo_name": ""
                                },
                                "auth_item": {
                                    "expired_at": "",
                                    "group_id": "",
                                    "image_process_auth": {
                                        "qps": 0
                                    },
                                    "not_before": "",
                                    "video_process_auth": {
                                        "channels": 0,
                                        "resolution_channels": [
                                            {
                                                "quota": 0,
                                                "resolution": "[RESOLUTION_UNKNOWN]RESOLUTION_UNKNOWN/RESOLUTION_QCIF/RESOLUTION_CIF/RESOLUTION_4CIF/RESOLUTION_D1/RESOLUTION_720P/RESOLUTION_1080P/RESOLUTION_2K/RESOLUTION_4K"
                                            }
                                        ]
                                    },
                                    "worker_limit": 0
                                },
                                "version": 0
                            }
                        ],
                        "code_name": "",
                        "description": "",
                        "raw_code": "",
                        "source": "[unset]unset/cloud/edge",
                        "updated_at": ""
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AppletManagerSrv_ActivationCodeInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def AppletManagerSrv_ActivationCodeUpsertPostApi(self, code=None, loginToken=None, sendRequest=True, print_log=True):
        """  upsert activation code，导入或更新当前全量激活码. """
        """  path: [post]/v1/activation_code API """
        """  body: 
                {
                    "code": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AppletManagerSrv_ActivationCodeUpsert")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

    def AppletManagerSrv_ListAppletGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  list所有applet信息，包括算力、验签、激活信息. """
        """  path: [get]/v1/applets API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "applets": [
                        {
                            "applet_params": {
                                "activated_quota": {
                                    "additionalProp1": 0,
                                    "additionalProp2": 0,
                                    "additionalProp3": 0
                                },
                                "algo_config_path": "",
                                "applet_path": "",
                                "display_name": "",
                                "event_type": [
                                    {
                                        "description": "",
                                        "type": ""
                                    }
                                ],
                                "kestrel_version": "[KestrelVersionUnset]KestrelVersionUnset/KestrelVersionV1/KestrelVersionV2",
                                "name": "",
                                "power": {
                                    "default": {
                                        "additionalProp1": 0,
                                        "additionalProp2": 0,
                                        "additionalProp3": 0
                                    }
                                },
                                "render_config_path": "",
                                "type": [
                                    {
                                        "description": "",
                                        "type": ""
                                    }
                                ],
                                "verified": false,
                                "version": 0
                            },
                            "name": "",
                            "updated_at": 0,
                            "version": 0,
                            "version_str": ""
                        }
                    ],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AppletManagerSrv_ListApplet")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def AppletManagerSrv_AppletImportPostApi(self, content=None, path=None, resource_quota=None, kestrel_version=None, loginToken=None, sendRequest=True, print_log=True):
        """  导入一个applet，解析出其中的applet包中的meta信息，并进行验签工作，当有相关的任务存在... """
        """  path: [post]/v1/applets API """
        """  body: 
                {
                    "content": "",
                    "kestrel_version": "[KestrelVersionUnset]KestrelVersionUnset/KestrelVersionV1/KestrelVersionV2",
                    "path": "",
                    "resource_quota": {
                        "additionalProp1": 0,
                        "additionalProp2": 0,
                        "additionalProp3": 0
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "applet": {
                        "applet_params": {
                            "activated_quota": {
                                "additionalProp1": 0,
                                "additionalProp2": 0,
                                "additionalProp3": 0
                            },
                            "algo_config_path": "",
                            "applet_path": "",
                            "display_name": "",
                            "event_type": [
                                {
                                    "description": "",
                                    "type": ""
                                }
                            ],
                            "kestrel_version": "[KestrelVersionUnset]KestrelVersionUnset/KestrelVersionV1/KestrelVersionV2",
                            "name": "",
                            "power": {
                                "default": {
                                    "additionalProp1": 0,
                                    "additionalProp2": 0,
                                    "additionalProp3": 0
                                }
                            },
                            "render_config_path": "",
                            "type": [
                                {
                                    "description": "",
                                    "type": ""
                                }
                            ],
                            "verified": false,
                            "version": 0
                        },
                        "name": "",
                        "updated_at": 0,
                        "version": 0,
                        "version_str": ""
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AppletManagerSrv_AppletImport")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("content", content)
        intef.update_body("path", path)
        intef.update_body("resource_quota", resource_quota)
        intef.update_body("kestrel_version", kestrel_version)
        return intef.request() if sendRequest else intef

    def AppletManagerSrv_AppletGCPostApi(self, runningApplet=None, loginToken=None, sendRequest=True, print_log=True):
        """  [internal] gc applet，每个applet仅保留最新的3个版本. """
        """  path: [post]/v1/applets/gc API """
        """  body: 
                {
                    "runningApplet": [
                        {
                            "applet_params": {
                                "activated_quota": {
                                    "additionalProp1": 0,
                                    "additionalProp2": 0,
                                    "additionalProp3": 0
                                },
                                "algo_config_path": "",
                                "applet_path": "",
                                "display_name": "",
                                "event_type": [
                                    {
                                        "description": "",
                                        "type": ""
                                    }
                                ],
                                "kestrel_version": "[KestrelVersionUnset]KestrelVersionUnset/KestrelVersionV1/KestrelVersionV2",
                                "name": "",
                                "power": {
                                    "default": {
                                        "additionalProp1": 0,
                                        "additionalProp2": 0,
                                        "additionalProp3": 0
                                    }
                                },
                                "render_config_path": "",
                                "type": [
                                    {
                                        "description": "",
                                        "type": ""
                                    }
                                ],
                                "verified": false,
                                "version": 0
                            },
                            "name": "",
                            "updated_at": 0,
                            "version": 0,
                            "version_str": ""
                        }
                    ]
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "applets": [
                        {
                            "applet_params": {
                                "activated_quota": {
                                    "additionalProp1": 0,
                                    "additionalProp2": 0,
                                    "additionalProp3": 0
                                },
                                "algo_config_path": "",
                                "applet_path": "",
                                "display_name": "",
                                "event_type": [
                                    {
                                        "description": "",
                                        "type": ""
                                    }
                                ],
                                "kestrel_version": "[KestrelVersionUnset]KestrelVersionUnset/KestrelVersionV1/KestrelVersionV2",
                                "name": "",
                                "power": {
                                    "default": {
                                        "additionalProp1": 0,
                                        "additionalProp2": 0,
                                        "additionalProp3": 0
                                    }
                                },
                                "render_config_path": "",
                                "type": [
                                    {
                                        "description": "",
                                        "type": ""
                                    }
                                ],
                                "verified": false,
                                "version": 0
                            },
                            "name": "",
                            "updated_at": 0,
                            "version": 0,
                            "version_str": ""
                        }
                    ],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AppletManagerSrv_AppletGC")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("runningApplet", runningApplet)
        return intef.request() if sendRequest else intef

    def AppletManagerSrv_AppletDeleteDeleteApi(self, name, version, loginToken=None, sendRequest=True, print_log=True):
        """  删除一个applet，有worker正在运行的applet不能删除. """
        """  path: [delete]/v1/applets/{name}/{version} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AppletManagerSrv_AppletDelete")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("name", name)
        intef.set_path_param("version", version)
        return intef.request() if sendRequest else intef

    def AppletManagerSrv_AppletUpdatePutApi(self, name, version, resource_quota=None, kestrel_version=None, loginToken=None, sendRequest=True, print_log=True):
        """  更新applet meta信息，如quota, kestrel_version等，当有相关的任务存在... """
        """  path: [put]/v1/applets/{name}/{version} API """
        """  body: 
                {
                    "kestrel_version": "[KestrelVersionUnset]KestrelVersionUnset/KestrelVersionV1/KestrelVersionV2",
                    "name": "",
                    "resource_quota": {
                        "additionalProp1": 0,
                        "additionalProp2": 0,
                        "additionalProp3": 0
                    },
                    "version": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "applet": {
                        "applet_params": {
                            "activated_quota": {
                                "additionalProp1": 0,
                                "additionalProp2": 0,
                                "additionalProp3": 0
                            },
                            "algo_config_path": "",
                            "applet_path": "",
                            "display_name": "",
                            "event_type": [
                                {
                                    "description": "",
                                    "type": ""
                                }
                            ],
                            "kestrel_version": "[KestrelVersionUnset]KestrelVersionUnset/KestrelVersionV1/KestrelVersionV2",
                            "name": "",
                            "power": {
                                "default": {
                                    "additionalProp1": 0,
                                    "additionalProp2": 0,
                                    "additionalProp3": 0
                                }
                            },
                            "render_config_path": "",
                            "type": [
                                {
                                    "description": "",
                                    "type": ""
                                }
                            ],
                            "verified": false,
                            "version": 0
                        },
                        "name": "",
                        "updated_at": 0,
                        "version": 0,
                        "version_str": ""
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AppletManagerSrv_AppletUpdate")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("name", name)
        intef.set_path_param("version", version)
        intef.update_body("name", name)
        intef.update_body("version", version)
        intef.update_body("resource_quota", resource_quota)
        intef.update_body("kestrel_version", kestrel_version)
        return intef.request() if sendRequest else intef

    def BizAppManagerSrv_ListBizAppGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  list 所有通过bizapp-manager导入的BizApp """
        """  path: [get]/v1/bizapps API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "bizapps": [
                        {
                            "applets": "",
                            "name": "",
                            "state": 0,
                            "version": 0
                        }
                    ],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppManagerSrv_ListBizApp")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BizAppManagerSrv_BizAppDeleteDeleteApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  删除bizApp: 删除bizapp表数据, 删除applet_meta表数据, 删除bizapp-... """
        """  path: [delete]/v1/bizapps API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppManagerSrv_BizAppDelete")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BizAppManagerSrv_BizAppImportPostApi(self, content=None, path=None, loginToken=None, sendRequest=True, print_log=True):
        """  导入一个BizApp: 解析BizApp包中的meta信息并启动服务 """
        """  path: [post]/v1/bizapps API """
        """  body: 
                {
                    "content": "",
                    "path": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "bizapp": {
                        "applets": "",
                        "name": "",
                        "state": 0,
                        "version": 0
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppManagerSrv_BizAppImport")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("content", content)
        intef.update_body("path", path)
        return intef.request() if sendRequest else intef

    def BizAppManagerSrv_BizAppStartPostApi(self, name=None, version=None, loginToken=None, sendRequest=True, print_log=True):
        """  启动bizapp服务 """
        """  path: [post]/v1/bizapps/start API """
        """  body: 
                {
                    "name": "",
                    "version": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppManagerSrv_BizAppStart")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("version", version)
        return intef.request() if sendRequest else intef

    def BizAppManagerSrv_BizAppStopPostApi(self, name=None, version=None, loginToken=None, sendRequest=True, print_log=True):
        """  停止bizapp: 停止服务, 停止bizapp-task任务 """
        """  path: [post]/v1/bizapps/stop API """
        """  body: 
                {
                    "name": "",
                    "version": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppManagerSrv_BizAppStop")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("version", version)
        return intef.request() if sendRequest else intef

    def CallbackAgent_BatchPutObjectPostApi(self, object_requests=None, loginToken=None, sendRequest=True, print_log=True):
        """  图像推送接口 """
        """  path: [post]/v1/callback/batch_put_object API """
        """  body: 
                {
                    "object_requests": [
                        {
                            "header": {
                                "trace": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            },
                            "object_info": {
                                "camera_info": {
                                    "camera_id": "",
                                    "device_id": "",
                                    "device_type": "",
                                    "internal_id": {
                                        "camera_idx": 0,
                                        "region_id": 0
                                    },
                                    "place_code": "",
                                    "place_name": "",
                                    "platform_id": "",
                                    "source_id": "",
                                    "tollgate_id": "",
                                    "tollgate_name": "",
                                    "zone_id": ""
                                },
                                "captured_time": "",
                                "extra_info": "",
                                "feature": {
                                    "blob": "",
                                    "type": "",
                                    "version": 0
                                },
                                "ns_id": "",
                                "object": {
                                    "algo": {
                                        "app_name": "",
                                        "app_version": 0,
                                        "data": {
                                            "type_url": "",
                                            "value": ""
                                        },
                                        "object_type": "",
                                        "object_version": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        }
                                    },
                                    "associations": [
                                        {
                                            "object_id": "",
                                            "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                                        }
                                    ],
                                    "automobile": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "crowd": {
                                        "density_map": "",
                                        "density_size": {
                                            "height": 0,
                                            "width": 0
                                        },
                                        "incident": [
                                            {
                                                "id": "",
                                                "start_time": "",
                                                "status": "[INCIDENT_START]INCIDENT_START/INCIDENT_CONTINUE/INCIDENT_STOP",
                                                "stop_time": "",
                                                "type": "[INCIDENT_CROWD]INCIDENT_CROWD/INCIDENT_STRAND",
                                                "update_time": "",
                                                "uuid": ""
                                            }
                                        ],
                                        "quantity": "",
                                        "strand_map": {
                                            "cache_url": "",
                                            "data": "",
                                            "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                            "image_id": "",
                                            "url": ""
                                        }
                                    },
                                    "cyclist": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "event": {
                                        "event_id": "",
                                        "event_status": "[EVENT_START]EVENT_START/EVENT_CONTINUE",
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "rule": {
                                            "direction": {
                                                "x": 0,
                                                "y": 0
                                            },
                                            "duration": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "rule_id": "",
                                            "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                        }
                                    },
                                    "face": {
                                        "angle": {
                                            "pitch": 0,
                                            "roll": 0,
                                            "yaw": 0
                                        },
                                        "attributes": {
                                            "additionalProp1": "",
                                            "additionalProp2": "",
                                            "additionalProp3": ""
                                        },
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "face_score": 0,
                                        "landmarks": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ],
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "human_powered_vehicle": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "object_id": "",
                                    "pedestrian": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "portrait_image_location": {
                                        "panoramic_image_size": {
                                            "height": 0,
                                            "width": 0
                                        },
                                        "portrait_image_in_panoramic": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "portrait_in_panoramic": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        }
                                    },
                                    "scenario": {
                                        "objects": [
                                            {
                                                "attributes_with_score": {
                                                    "additionalProp1": {
                                                        "category": "",
                                                        "roi": {
                                                            "vertices": [
                                                                {
                                                                    "x": 0,
                                                                    "y": 0
                                                                }
                                                            ]
                                                        },
                                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                        "value": 0
                                                    },
                                                    "additionalProp2": {
                                                        "category": "",
                                                        "roi": {
                                                            "vertices": [
                                                                {
                                                                    "x": 0,
                                                                    "y": 0
                                                                }
                                                            ]
                                                        },
                                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                        "value": 0
                                                    },
                                                    "additionalProp3": {
                                                        "category": "",
                                                        "roi": {
                                                            "vertices": [
                                                                {
                                                                    "x": 0,
                                                                    "y": 0
                                                                }
                                                            ]
                                                        },
                                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                        "value": 0
                                                    }
                                                },
                                                "quality": 0,
                                                "rectangle": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                            }
                                        ]
                                    },
                                    "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                                },
                                "object_index_in_frame": 0,
                                "panoramic_image": {
                                    "cache_url": "",
                                    "data": "",
                                    "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                    "image_id": "",
                                    "url": ""
                                },
                                "portrait_image": {
                                    "cache_url": "",
                                    "data": "",
                                    "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                    "image_id": "",
                                    "url": ""
                                },
                                "received_time": "",
                                "relative_time": "",
                                "track_event": "[ONGOING]ONGOING/END/START"
                            },
                            "viid_id": ""
                        }
                    ]
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "object_put_responses": [
                        {
                            "PanoramicImageUri": "",
                            "PortraitImageUri": "",
                            "header": {
                                "timestamp": "",
                                "trace": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            }
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "CallbackAgent_BatchPutObject")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("object_requests", object_requests)
        return intef.request() if sendRequest else intef

    def CallbackAgent_ListCallbackConfigGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  查询callback配置列表. """
        """  path: [get]/v1/callback/configs API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "data": [
                        {
                            "create_at": "",
                            "id": "",
                            "provider": {
                                "address": "",
                                "name": "",
                                "type": "[UNSET]UNSET/HTTP"
                            },
                            "types": [
                                "[UNSET]UNSET/DEVICE_REGISTER/DEVICE_STATE/SUB_DEVICE_STATE/TASK_STATE/OPLOGS/SUB_DEVICE_DELETE/TASK_DELETE/RECORD_OUTPUT_RESULT/SUB_DEVICE_ADD/SUB_DEVICE_UPDATE/PORTRAIT_DB_ADD/PORTRAIT_DB_DELETE/PORTRAIT_DB_UPDATE/PORTRAIT_ADD/PORTRAIT_DELETE/PORTRAIT_UPDATE/VDD_TASK_STATE/ACTIVATION_CODE_UPSERT/APPLET_IMPORT/APPLET_DELETE/APPLET_UPDATE/SUB_DEVICE_ADD_FAILED/SUB_DEVICE_UPDATE_FAILED/SUB_DEVICE_DELETE_FAILED"
                            ],
                            "update_at": ""
                        }
                    ],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "CallbackAgent_ListCallbackConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def CallbackAgent_AddCallbackConfigPostApi(self, config=None, loginToken=None, sendRequest=True, print_log=True):
        """  增加callback配置项. """
        """  path: [post]/v1/callback/configs API """
        """  body: 
                {
                    "config": {
                        "create_at": "",
                        "id": "",
                        "provider": {
                            "address": "",
                            "name": "",
                            "type": "[UNSET]UNSET/HTTP"
                        },
                        "types": [
                            "[UNSET]UNSET/DEVICE_REGISTER/DEVICE_STATE/SUB_DEVICE_STATE/TASK_STATE/OPLOGS/SUB_DEVICE_DELETE/TASK_DELETE/RECORD_OUTPUT_RESULT/SUB_DEVICE_ADD/SUB_DEVICE_UPDATE/PORTRAIT_DB_ADD/PORTRAIT_DB_DELETE/PORTRAIT_DB_UPDATE/PORTRAIT_ADD/PORTRAIT_DELETE/PORTRAIT_UPDATE/VDD_TASK_STATE/ACTIVATION_CODE_UPSERT/APPLET_IMPORT/APPLET_DELETE/APPLET_UPDATE/SUB_DEVICE_ADD_FAILED/SUB_DEVICE_UPDATE_FAILED/SUB_DEVICE_DELETE_FAILED"
                        ],
                        "update_at": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "CallbackAgent_AddCallbackConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("config", config)
        return intef.request() if sendRequest else intef

    def CallbackAgent_UpdateCallbackConfigPutApi(self, config=None, loginToken=None, sendRequest=True, print_log=True):
        """  更新callback配置项. """
        """  path: [put]/v1/callback/configs API """
        """  body: 
                {
                    "config": {
                        "create_at": "",
                        "id": "",
                        "provider": {
                            "address": "",
                            "name": "",
                            "type": "[UNSET]UNSET/HTTP"
                        },
                        "types": [
                            "[UNSET]UNSET/DEVICE_REGISTER/DEVICE_STATE/SUB_DEVICE_STATE/TASK_STATE/OPLOGS/SUB_DEVICE_DELETE/TASK_DELETE/RECORD_OUTPUT_RESULT/SUB_DEVICE_ADD/SUB_DEVICE_UPDATE/PORTRAIT_DB_ADD/PORTRAIT_DB_DELETE/PORTRAIT_DB_UPDATE/PORTRAIT_ADD/PORTRAIT_DELETE/PORTRAIT_UPDATE/VDD_TASK_STATE/ACTIVATION_CODE_UPSERT/APPLET_IMPORT/APPLET_DELETE/APPLET_UPDATE/SUB_DEVICE_ADD_FAILED/SUB_DEVICE_UPDATE_FAILED/SUB_DEVICE_DELETE_FAILED"
                        ],
                        "update_at": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "CallbackAgent_UpdateCallbackConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("config", config)
        return intef.request() if sendRequest else intef

    def CallbackAgent_GetCallbackConfigGetApi(self, id, loginToken=None, sendRequest=True, print_log=True):
        """  查询callback的配置. """
        """  path: [get]/v1/callback/configs/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "config": {
                        "create_at": "",
                        "id": "",
                        "provider": {
                            "address": "",
                            "name": "",
                            "type": "[UNSET]UNSET/HTTP"
                        },
                        "types": [
                            "[UNSET]UNSET/DEVICE_REGISTER/DEVICE_STATE/SUB_DEVICE_STATE/TASK_STATE/OPLOGS/SUB_DEVICE_DELETE/TASK_DELETE/RECORD_OUTPUT_RESULT/SUB_DEVICE_ADD/SUB_DEVICE_UPDATE/PORTRAIT_DB_ADD/PORTRAIT_DB_DELETE/PORTRAIT_DB_UPDATE/PORTRAIT_ADD/PORTRAIT_DELETE/PORTRAIT_UPDATE/VDD_TASK_STATE/ACTIVATION_CODE_UPSERT/APPLET_IMPORT/APPLET_DELETE/APPLET_UPDATE/SUB_DEVICE_ADD_FAILED/SUB_DEVICE_UPDATE_FAILED/SUB_DEVICE_DELETE_FAILED"
                        ],
                        "update_at": ""
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "CallbackAgent_GetCallbackConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def CallbackAgent_DeleteCallbackConfigDeleteApi(self, id, loginToken=None, sendRequest=True, print_log=True):
        """  删除callback配置项. """
        """  path: [delete]/v1/callback/configs/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "CallbackAgent_DeleteCallbackConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def CallbackAgent_VIIDNewPostApi(self, viid_id=None, viid_param=None, extra_infos=None, loginToken=None, sendRequest=True, print_log=True):
        """  创建视图库 """
        """  path: [post]/v1/callback/viids API """
        """  body: 
                {
                    "extra_infos": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    },
                    "viid_id": "",
                    "viid_param": {
                        "client_id": "",
                        "host": "",
                        "password": "",
                        "port": 0,
                        "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                        "server_id": "",
                        "user": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "extra_infos": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "viid_id": "",
                    "viid_param": {
                        "client_id": "",
                        "host": "",
                        "password": "",
                        "port": 0,
                        "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                        "server_id": "",
                        "user": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "CallbackAgent_VIIDNew")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("viid_id", viid_id)
        intef.update_body("viid_param", viid_param)
        intef.update_body("extra_infos", extra_infos)
        return intef.request() if sendRequest else intef

    def CallbackAgent_VIIDInfoGetApi(self, viid_id, loginToken=None, sendRequest=True, print_log=True):
        """  查看视图库信息 """
        """  path: [get]/v1/callback/viids/{viid_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "viid_config": {
                        "extra_infos": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        },
                        "viid_id": "",
                        "viid_param": {
                            "client_id": "",
                            "host": "",
                            "password": "",
                            "port": 0,
                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                            "server_id": "",
                            "user": ""
                        }
                    },
                    "viid_status": {
                        "reason": "",
                        "status": "[UNKNOWN]UNKNOWN/CONNECTED/DISCONNECTED"
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "CallbackAgent_VIIDInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("viid_id", viid_id)
        return intef.request() if sendRequest else intef

    def CallbackAgent_VIIDDeleteDeleteApi(self, viid_id, loginToken=None, sendRequest=True, print_log=True):
        """  删除视图库 """
        """  path: [delete]/v1/callback/viids/{viid_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "CallbackAgent_VIIDDelete")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("viid_id", viid_id)
        return intef.request() if sendRequest else intef

    def NebulaDbSyncCallbackAgent_EventCallbackPostApi(self, content_type=None, portrait_db_add=None, portrait_db_delete=None, portrait_db_update=None, portrait_add=None, portrait_delete=None, portrait_update=None, loginToken=None, sendRequest=True, print_log=True):
        """  业务方实现，用来接收 nebula-db-sync-agent """
        """  path: [post]/nebula/v1/db-sync/callback API """
        """  body: 
                {
                    "content_type": "[UNSET]UNSET/PORTRAIT_DB_ADD/PORTRAIT_DB_UPDATE/PORTRAIT_DB_DELETE/PORTRAIT_ADD/PORTRAIT_UPDATE/PORTRAIT_DELETE/OPLOG",
                    "portrait_add": {
                        "cloud_portrait_db_id": "",
                        "device_id": "",
                        "device_sn": "",
                        "local_portrait_db_id": "",
                        "portraits": [
                            {
                                "cloud_portrait_db_id": "",
                                "cloud_portrait_id": "",
                                "local_portrait_db_id": "",
                                "local_portrait_id": "",
                                "result": {
                                    "code": 0,
                                    "message": ""
                                },
                                "seq_id": ""
                            }
                        ],
                        "result": {
                            "code": 0,
                            "message": ""
                        }
                    },
                    "portrait_db_add": {
                        "cloud_portrait_db_id": "",
                        "device_id": "",
                        "device_sn": "",
                        "local_portrait_db_id": "",
                        "result": {
                            "code": 0,
                            "message": ""
                        }
                    },
                    "portrait_db_delete": {
                        "cloud_portrait_db_id": "",
                        "device_id": "",
                        "device_sn": "",
                        "local_portrait_db_id": "",
                        "result": {
                            "code": 0,
                            "message": ""
                        }
                    },
                    "portrait_db_update": {
                        "cloud_portrait_db_id": "",
                        "device_id": "",
                        "device_sn": "",
                        "local_portrait_db_id": "",
                        "result": {
                            "code": 0,
                            "message": ""
                        }
                    },
                    "portrait_delete": {
                        "cloud_portrait_db_id": "",
                        "device_id": "",
                        "device_sn": "",
                        "local_portrait_db_id": "",
                        "portraits": [
                            {
                                "cloud_portrait_db_id": "",
                                "cloud_portrait_id": "",
                                "local_portrait_db_id": "",
                                "local_portrait_id": "",
                                "result": {
                                    "code": 0,
                                    "message": ""
                                },
                                "seq_id": ""
                            }
                        ],
                        "result": {
                            "code": 0,
                            "message": ""
                        }
                    },
                    "portrait_update": {
                        "cloud_portrait_db_id": "",
                        "device_id": "",
                        "device_sn": "",
                        "local_portrait_db_id": "",
                        "portraits": [
                            {
                                "cloud_portrait_db_id": "",
                                "cloud_portrait_id": "",
                                "local_portrait_db_id": "",
                                "local_portrait_id": "",
                                "result": {
                                    "code": 0,
                                    "message": ""
                                },
                                "seq_id": ""
                            }
                        ],
                        "result": {
                            "code": 0,
                            "message": ""
                        }
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaDbSyncCallbackAgent_EventCallback")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("content_type", content_type)
        intef.update_body("portrait_db_add", portrait_db_add)
        intef.update_body("portrait_db_delete", portrait_db_delete)
        intef.update_body("portrait_db_update", portrait_db_update)
        intef.update_body("portrait_add", portrait_add)
        intef.update_body("portrait_delete", portrait_delete)
        intef.update_body("portrait_update", portrait_update)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetRealTimeBGIMGGetApi(self, camera_id, loginToken=None, sendRequest=True, print_log=True):
        """  GetRealTimeBGIMG 获取实时背景大图... """
        """  path: [get]/v1/bg_img/{camera_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "bg_img": "",
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetRealTimeBGIMG")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("camera_id", camera_id)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetDefaultNicGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  获取默认网卡 """
        """  path: [get]/v1/device/default-nic API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "nic": {
                        "address": "",
                        "gateway": "",
                        "interface_name": "",
                        "mac_addr": "",
                        "netmask": "",
                        "state": "",
                        "type": "[IT_DHCP]IT_DHCP/IT_STATIC"
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetDefaultNic")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_SetDefaultNicByNamePostApi(self, name, loginToken=None, sendRequest=True, print_log=True):
        """  设置网卡为默认网卡 """
        """  path: [post]/v1/device/default-nic/{name} API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_SetDefaultNicByName")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("name", name)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetDeviceDisksInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetDeviceDisksInfo 获取设备磁盘信息 """
        """  path: [get]/v1/device/disks API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "disks": [
                        {
                            "avail": "",
                            "device": "",
                            "free": "",
                            "fstype": "",
                            "mountpoint": "",
                            "size": ""
                        }
                    ],
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetDeviceDisksInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetDNSConfigGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetDNSConfig 获取 DNS 配置信息 """
        """  path: [get]/v1/device/dns API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "dns": {
                        "primary": "",
                        "secondary": ""
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetDNSConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_SetDNSConfigPostApi(self, dns=None, loginToken=None, sendRequest=True, print_log=True):
        """  SetDNSConfig 设置 DNS """
        """  path: [post]/v1/device/dns API """
        """  body: 
                {
                    "dns": {
                        "primary": "",
                        "secondary": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_SetDNSConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("dns", dns)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetIPConfigGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetIPConfig 获取 IP 配置信息 """
        """  path: [get]/v1/device/ip API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "ip": {
                        "ips": [
                            {
                                "address": "",
                                "gateway": "",
                                "interface_name": "",
                                "mac_addr": "",
                                "netmask": "",
                                "state": "",
                                "type": "[IT_DHCP]IT_DHCP/IT_STATIC"
                            }
                        ]
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetIPConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_SetIPConfigPostApi(self, ip=None, loginToken=None, sendRequest=True, print_log=True):
        """  SetIPConfig 设置 IP (Pallas平台, 不支持interface alias配置) """
        """  path: [post]/v1/device/ip API """
        """  body: 
                {
                    "ip": {
                        "ips": [
                            {
                                "address": "",
                                "gateway": "",
                                "interface_name": "",
                                "mac_addr": "",
                                "netmask": "",
                                "state": "",
                                "type": "[IT_DHCP]IT_DHCP/IT_STATIC"
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_SetIPConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("ip", ip)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetModemAPNGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetModemAPN 获取4G插卡状态，运营商信息，IMSI,信号强度,APN名称，用户名，密码 """
        """  path: [get]/v1/device/modem-apn API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "apn_info": {
                        "apn": {
                            "apn": "",
                            "password": "",
                            "username": ""
                        },
                        "ccid": "",
                        "imsi": "",
                        "operator": "",
                        "status": "",
                        "strength": 0
                    },
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetModemAPN")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_CloseModemAPNDeleteApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  关闭4G功能 """
        """  path: [delete]/v1/device/modem-apn API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_CloseModemAPN")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_OpenModemAPNPostApi(self, apn=None, loginToken=None, sendRequest=True, print_log=True):
        """  开启4G功能，4G卡未插卡时，4G功能不可开启 """
        """  path: [post]/v1/device/modem-apn API """
        """  body: 
                {
                    "apn": {
                        "apn": "",
                        "password": "",
                        "username": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_OpenModemAPN")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("apn", apn)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetNTPConfigGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetNTPConfig 获取 NTP 配置信息 (Pallas平台, port参数设置为"123"... """
        """  path: [get]/v1/device/ntp API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "ntp": {
                        "enable": false,
                        "ntps": [
                            {
                                "port": "",
                                "url": ""
                            }
                        ],
                        "time_interval": 0
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetNTPConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_SetNTPConfigPostApi(self, ntp=None, loginToken=None, sendRequest=True, print_log=True):
        """  SetNTPConfig 设置 NTP (Pallas平台，port参数只能是"123"或者"") """
        """  path: [post]/v1/device/ntp API """
        """  body: 
                {
                    "ntp": {
                        "enable": false,
                        "ntps": [
                            {
                                "port": "",
                                "url": ""
                            }
                        ],
                        "time_interval": 0
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_SetNTPConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("ntp", ntp)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_PingPostApi(self, address=None, loginToken=None, sendRequest=True, print_log=True):
        """  Ping ping 指定地址，用于测试网络情况 """
        """  path: [post]/v1/device/ping API """
        """  body: 
                {
                    "address": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "ok": false
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_Ping")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("address", address)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetRegisterStateGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  获取设备注册信息 """
        """  path: [get]/v1/device/register_state API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "register_state": {
                        "latest_online": "",
                        "register_time": "",
                        "status": "[DS_UNACTIVED]DS_UNACTIVED/DS_ACTIVED/DS_ONLINE/DS_OFFLINE/DS_DISABLED"
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetRegisterState")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetROUTEConfigGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetROUTEConfig 获取 路由表 配置信息 """
        """  path: [get]/v1/device/route API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "route": {
                        "routes": [
                            {
                                "destination": "",
                                "flags": "",
                                "gateway": "",
                                "genmask": "",
                                "iface": "",
                                "metric": "",
                                "ref": "",
                                "use": ""
                            }
                        ]
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetROUTEConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_SetROUTEConfigPostApi(self, route=None, loginToken=None, sendRequest=True, print_log=True):
        """  SetROUTEConfig 设置 路由表 """
        """  path: [post]/v1/device/route API """
        """  body: 
                {
                    "route": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_SetROUTEConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("route", route)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetSerialNumberGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetSerialNumber 获取设备序列号 """
        """  path: [get]/v1/device/serial_number API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "serial_number": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetSerialNumber")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetTIMEConfigGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetTIMEConfig 获取 系统时间 """
        """  path: [get]/v1/device/time API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "time": {
                        "ntsc": "[N24]N24/N12",
                        "time_stamp": "",
                        "time_zone": "",
                        "type": "[YMD]YMD/MDY/DMY"
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetTIMEConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_SetTIMEConfigPostApi(self, time=None, loginToken=None, sendRequest=True, print_log=True):
        """  SetTIMEConfig 设置 系统时间 """
        """  path: [post]/v1/device/time API """
        """  body: 
                {
                    "time": {
                        "ntsc": "[N24]N24/N12",
                        "time_stamp": "",
                        "time_zone": "",
                        "type": "[YMD]YMD/MDY/DMY"
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_SetTIMEConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("time", time)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetRegisterUserMetaGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetRegisterUserMeta 获取用户自注册信息 """
        """  path: [get]/v1/device/user_meta API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "user_meta": {}
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetRegisterUserMeta")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_SetRegisterUserMetaPostApi(self, user_meta=None, loginToken=None, sendRequest=True, print_log=True):
        """  SetRegisterUserMeta 设置用户自注册信息 """
        """  path: [post]/v1/device/user_meta API """
        """  body: 
                {
                    "user_meta": {}
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_SetRegisterUserMeta")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("user_meta", user_meta)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetVersionInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetVersionInfo 获取序列号SN，Pallas固件版本ROM(t4不提供)，Viperl... """
        """  path: [get]/v1/device/version API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "version": {
                        "ROM": "",
                        "SN": "",
                        "nebula": "",
                        "viperlite": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetVersionInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetLicenseStateGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  GetLicenseState 获取 license 信息 """
        """  path: [get]/v1/license API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "license": {
                        "nebula_registry": "",
                        "registration": false,
                        "run_mode": "",
                        "symphony_addr": "",
                        "symphony_registry": "",
                        "symphony_registry_addr": ""
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetLicenseState")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_SetLicensePostApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  SetLicense 设置 license 信息(详情参考注释)
Use POST http met... """
        """  path: [post]/v1/license API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_SetLicense")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_UpsertSubDevicePostApi(self, subdevice=None, skip=None, loginToken=None, sendRequest=True, print_log=True):
        """  UpsertSubDevice 更新/添加子设备, device_id不存在时添加，存在时更新。
该... """
        """  path: [post]/v1/subdevices API """
        """  body: 
                {
                    "skip": false,
                    "subdevice": {
                        "brand": "[BR_UNSET]BR_UNSET/UNKNOWN/HIKVISION/DAHUA",
                        "created_at": "",
                        "description": "",
                        "device_config": {
                            "dns": {
                                "primary": "",
                                "secondary": ""
                            },
                            "ip": {
                                "ips": [
                                    {
                                        "address": "",
                                        "gateway": "",
                                        "gateway_type": "[GT_DEFAULT]GT_DEFAULT/GT_NORMAL",
                                        "interface_name": "",
                                        "netmask": "",
                                        "type": "[IT_DHCP]IT_DHCP/IT_STATIC"
                                    }
                                ]
                            },
                            "license_file": "",
                            "log": {
                                "level": "[S_LOG_DEBUG]S_LOG_DEBUG/S_LOG_INFO/S_LOG_WARNNING/S_LOG_ERROR/S_LOG_NONE",
                                "path": "",
                                "size": 0
                            },
                            "nat": {
                                "nats": [
                                    {
                                        "external_ip": "",
                                        "external_port": "",
                                        "internal_ip": "",
                                        "internal_port": "",
                                        "protocol": "",
                                        "status": "[SC_OK]SC_OK/SC_SC_CANCELLED/SC_UNKNOWN/SC_INVALID_ARGUMENT/SC_DEADLINE_EXCEEDED/SC_NOT_FOUND/SC_ALREADY_EXISTS/SC_PERMISSION_DENIED/SC_UNAUTHENTICATED/SC_RESOURCE_EXHAUSTED/SC_FAILED_PRECONDITION/SC_ABORTED/SC_OUT_OF_RANGE/SC_UNIMPLEMENTED/SC_INTERNAL/SC_UNAVAILABLE/SC_DATA_LOSS/SC_DEVICE_UNREACHABLE/SC_DEVICE_TIME_NOT_SYNC/SC_DEVICE_DELETED"
                                    }
                                ]
                            },
                            "ntp": {
                                "enable": false,
                                "ntps": [
                                    {
                                        "port": "",
                                        "url": ""
                                    }
                                ],
                                "time_interval": 0
                            },
                            "ssh": {
                                "ssh": {
                                    "enable": false,
                                    "port": ""
                                }
                            },
                            "time_zone": {
                                "time_zone": ""
                            },
                            "user_configs": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            }
                        },
                        "device_id": "",
                        "device_kind": "[SDK_UNSET]SDK_UNSET/CAMERA/NVR/PLATFORM",
                        "device_sn": "",
                        "disconnected_at": "",
                        "extra_config": {
                            "camera_config": {
                                "auth": {
                                    "password": "",
                                    "username": ""
                                },
                                "image_source_config": {
                                    "dahua_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "deepglint_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "dummy_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "ftp_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "gat1400_ape_face_camera_parameter": {
                                        "parameter": {
                                            "ape_id": "",
                                            "extra_info": "",
                                            "password": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hk_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hk_isapi_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "http_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hua_wei_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "keda_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "megvii_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sensetime_001_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sensetime_002_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sensetime_d_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "symphony_nebula_face_camera_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "task_id": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "symphony_pass_face_camera_parameter": {
                                        "parameter": {
                                            "device_id": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "tiandy_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "yuntian_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "yushi_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                },
                                "internal_id": {
                                    "camera_idx": 0,
                                    "region_id": 0
                                },
                                "manage_port": 0,
                                "streams": {
                                    "main": {
                                        "audio": {
                                            "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                        },
                                        "video": {
                                            "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                            "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                            "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                            "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                        }
                                    },
                                    "second": {
                                        "audio": {
                                            "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                        },
                                        "video": {
                                            "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                            "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                            "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                            "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                        }
                                    },
                                    "third": {
                                        "audio": {
                                            "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                        },
                                        "video": {
                                            "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                            "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                            "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                            "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                        }
                                    }
                                },
                                "video_source_config": {
                                    "hls_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "onvif_parameter": {
                                        "parameter": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtmp_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtsp_parameter": {
                                        "parameter": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                }
                            },
                            "nvr_config": {
                                "auth": {
                                    "password": "",
                                    "username": ""
                                },
                                "manage_port": 0,
                                "video_source_config": {
                                    "hls_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "onvif_parameter": {
                                        "parameter": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtmp_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtsp_parameter": {
                                        "parameter": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                }
                            },
                            "platform_config": {
                                "image_source_config": {
                                    "baidu_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "gat1400_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "security_first_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "security_third_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "tao_an_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "wang_li_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "xinghuo_parameter": {
                                        "face_camera_parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                },
                                "internal_id": {
                                    "camera_idx": 0,
                                    "region_id": 0
                                },
                                "video_source_config": {
                                    "dh_video_cloud_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "gb28181_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hls_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "huawei_vcn_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "nvr_parameter": {
                                        "parameter": {
                                            "downlink_host": "",
                                            "ipc": "",
                                            "password": "",
                                            "private": false,
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "onvif_parameter": {
                                        "parameter": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtmp_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtsp_parameter": {
                                        "parameter": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sjk_parameter": {
                                        "parameter": {
                                            "ipc": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "xinghuo_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                }
                            }
                        },
                        "extra_info": "",
                        "last_connected_at": "",
                        "name": "",
                        "product_name": "",
                        "status": "[DS_UNACTIVED]DS_UNACTIVED/DS_ACTIVED/DS_ONLINE/DS_OFFLINE/DS_DISABLED",
                        "type": "[TT_UNKNOWN]TT_UNKNOWN/TT_EDGE_GATEWAY/TT_EDGE_DEVICE/TT_END_SUBDEVICE",
                        "updated_at": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "subdevice": {
                        "brand": "[BR_UNSET]BR_UNSET/UNKNOWN/HIKVISION/DAHUA",
                        "created_at": "",
                        "description": "",
                        "device_config": {
                            "dns": {
                                "primary": "",
                                "secondary": ""
                            },
                            "ip": {
                                "ips": [
                                    {
                                        "address": "",
                                        "gateway": "",
                                        "gateway_type": "[GT_DEFAULT]GT_DEFAULT/GT_NORMAL",
                                        "interface_name": "",
                                        "netmask": "",
                                        "type": "[IT_DHCP]IT_DHCP/IT_STATIC"
                                    }
                                ]
                            },
                            "license_file": "",
                            "log": {
                                "level": "[S_LOG_DEBUG]S_LOG_DEBUG/S_LOG_INFO/S_LOG_WARNNING/S_LOG_ERROR/S_LOG_NONE",
                                "path": "",
                                "size": 0
                            },
                            "nat": {
                                "nats": [
                                    {
                                        "external_ip": "",
                                        "external_port": "",
                                        "internal_ip": "",
                                        "internal_port": "",
                                        "protocol": "",
                                        "status": "[SC_OK]SC_OK/SC_SC_CANCELLED/SC_UNKNOWN/SC_INVALID_ARGUMENT/SC_DEADLINE_EXCEEDED/SC_NOT_FOUND/SC_ALREADY_EXISTS/SC_PERMISSION_DENIED/SC_UNAUTHENTICATED/SC_RESOURCE_EXHAUSTED/SC_FAILED_PRECONDITION/SC_ABORTED/SC_OUT_OF_RANGE/SC_UNIMPLEMENTED/SC_INTERNAL/SC_UNAVAILABLE/SC_DATA_LOSS/SC_DEVICE_UNREACHABLE/SC_DEVICE_TIME_NOT_SYNC/SC_DEVICE_DELETED"
                                    }
                                ]
                            },
                            "ntp": {
                                "enable": false,
                                "ntps": [
                                    {
                                        "port": "",
                                        "url": ""
                                    }
                                ],
                                "time_interval": 0
                            },
                            "ssh": {
                                "ssh": {
                                    "enable": false,
                                    "port": ""
                                }
                            },
                            "time_zone": {
                                "time_zone": ""
                            },
                            "user_configs": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            }
                        },
                        "device_id": "",
                        "device_kind": "[SDK_UNSET]SDK_UNSET/CAMERA/NVR/PLATFORM",
                        "device_sn": "",
                        "disconnected_at": "",
                        "extra_config": {
                            "camera_config": {
                                "auth": {
                                    "password": "",
                                    "username": ""
                                },
                                "image_source_config": {
                                    "dahua_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "deepglint_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "dummy_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "ftp_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "gat1400_ape_face_camera_parameter": {
                                        "parameter": {
                                            "ape_id": "",
                                            "extra_info": "",
                                            "password": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hk_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hk_isapi_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "http_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hua_wei_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "keda_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "megvii_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sensetime_001_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sensetime_002_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sensetime_d_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "symphony_nebula_face_camera_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "task_id": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "symphony_pass_face_camera_parameter": {
                                        "parameter": {
                                            "device_id": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "tiandy_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "yuntian_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "yushi_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                },
                                "internal_id": {
                                    "camera_idx": 0,
                                    "region_id": 0
                                },
                                "manage_port": 0,
                                "streams": {
                                    "main": {
                                        "audio": {
                                            "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                        },
                                        "video": {
                                            "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                            "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                            "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                            "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                        }
                                    },
                                    "second": {
                                        "audio": {
                                            "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                        },
                                        "video": {
                                            "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                            "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                            "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                            "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                        }
                                    },
                                    "third": {
                                        "audio": {
                                            "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                        },
                                        "video": {
                                            "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                            "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                            "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                            "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                        }
                                    }
                                },
                                "video_source_config": {
                                    "hls_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "onvif_parameter": {
                                        "parameter": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtmp_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtsp_parameter": {
                                        "parameter": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                }
                            },
                            "nvr_config": {
                                "auth": {
                                    "password": "",
                                    "username": ""
                                },
                                "manage_port": 0,
                                "video_source_config": {
                                    "hls_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "onvif_parameter": {
                                        "parameter": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtmp_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtsp_parameter": {
                                        "parameter": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                }
                            },
                            "platform_config": {
                                "image_source_config": {
                                    "baidu_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "gat1400_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "security_first_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "security_third_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "tao_an_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "wang_li_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "xinghuo_parameter": {
                                        "face_camera_parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                },
                                "internal_id": {
                                    "camera_idx": 0,
                                    "region_id": 0
                                },
                                "video_source_config": {
                                    "dh_video_cloud_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "gb28181_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hls_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "huawei_vcn_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "nvr_parameter": {
                                        "parameter": {
                                            "downlink_host": "",
                                            "ipc": "",
                                            "password": "",
                                            "private": false,
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "onvif_parameter": {
                                        "parameter": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtmp_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtsp_parameter": {
                                        "parameter": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sjk_parameter": {
                                        "parameter": {
                                            "ipc": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "xinghuo_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                }
                            }
                        },
                        "extra_info": "",
                        "last_connected_at": "",
                        "name": "",
                        "product_name": "",
                        "status": "[DS_UNACTIVED]DS_UNACTIVED/DS_ACTIVED/DS_ONLINE/DS_OFFLINE/DS_DISABLED",
                        "type": "[TT_UNKNOWN]TT_UNKNOWN/TT_EDGE_GATEWAY/TT_EDGE_DEVICE/TT_END_SUBDEVICE",
                        "updated_at": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_UpsertSubDevice")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("subdevice", subdevice)
        intef.update_body("skip", skip)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_ListAllSubDevicesGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  ListAllSubDevices 获取所有子设备信息 """
        """  path: [get]/v1/subdevices/all API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "subdevices": [
                        {
                            "brand": "[BR_UNSET]BR_UNSET/UNKNOWN/HIKVISION/DAHUA",
                            "created_at": "",
                            "description": "",
                            "device_config": {
                                "dns": {
                                    "primary": "",
                                    "secondary": ""
                                },
                                "ip": {
                                    "ips": [
                                        {
                                            "address": "",
                                            "gateway": "",
                                            "gateway_type": "[GT_DEFAULT]GT_DEFAULT/GT_NORMAL",
                                            "interface_name": "",
                                            "netmask": "",
                                            "type": "[IT_DHCP]IT_DHCP/IT_STATIC"
                                        }
                                    ]
                                },
                                "license_file": "",
                                "log": {
                                    "level": "[S_LOG_DEBUG]S_LOG_DEBUG/S_LOG_INFO/S_LOG_WARNNING/S_LOG_ERROR/S_LOG_NONE",
                                    "path": "",
                                    "size": 0
                                },
                                "nat": {
                                    "nats": [
                                        {
                                            "external_ip": "",
                                            "external_port": "",
                                            "internal_ip": "",
                                            "internal_port": "",
                                            "protocol": "",
                                            "status": "[SC_OK]SC_OK/SC_SC_CANCELLED/SC_UNKNOWN/SC_INVALID_ARGUMENT/SC_DEADLINE_EXCEEDED/SC_NOT_FOUND/SC_ALREADY_EXISTS/SC_PERMISSION_DENIED/SC_UNAUTHENTICATED/SC_RESOURCE_EXHAUSTED/SC_FAILED_PRECONDITION/SC_ABORTED/SC_OUT_OF_RANGE/SC_UNIMPLEMENTED/SC_INTERNAL/SC_UNAVAILABLE/SC_DATA_LOSS/SC_DEVICE_UNREACHABLE/SC_DEVICE_TIME_NOT_SYNC/SC_DEVICE_DELETED"
                                        }
                                    ]
                                },
                                "ntp": {
                                    "enable": false,
                                    "ntps": [
                                        {
                                            "port": "",
                                            "url": ""
                                        }
                                    ],
                                    "time_interval": 0
                                },
                                "ssh": {
                                    "ssh": {
                                        "enable": false,
                                        "port": ""
                                    }
                                },
                                "time_zone": {
                                    "time_zone": ""
                                },
                                "user_configs": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            },
                            "device_id": "",
                            "device_kind": "[SDK_UNSET]SDK_UNSET/CAMERA/NVR/PLATFORM",
                            "device_sn": "",
                            "disconnected_at": "",
                            "extra_config": {
                                "camera_config": {
                                    "auth": {
                                        "password": "",
                                        "username": ""
                                    },
                                    "image_source_config": {
                                        "dahua_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "deepglint_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "dummy_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "ftp_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "gat1400_ape_face_camera_parameter": {
                                            "parameter": {
                                                "ape_id": "",
                                                "extra_info": "",
                                                "password": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "hk_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "hk_isapi_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "http_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "hua_wei_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "keda_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "megvii_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "sensetime_001_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "sensetime_002_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "sensetime_d_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "symphony_nebula_face_camera_parameter": {
                                            "parameter": {
                                                "device_id": "",
                                                "task_id": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "symphony_pass_face_camera_parameter": {
                                            "parameter": {
                                                "device_id": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "tiandy_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "yuntian_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "yushi_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        }
                                    },
                                    "internal_id": {
                                        "camera_idx": 0,
                                        "region_id": 0
                                    },
                                    "manage_port": 0,
                                    "streams": {
                                        "main": {
                                            "audio": {
                                                "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                            },
                                            "video": {
                                                "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                                "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                                "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                                "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                            }
                                        },
                                        "second": {
                                            "audio": {
                                                "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                            },
                                            "video": {
                                                "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                                "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                                "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                                "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                            }
                                        },
                                        "third": {
                                            "audio": {
                                                "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                            },
                                            "video": {
                                                "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                                "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                                "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                                "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                            }
                                        }
                                    },
                                    "video_source_config": {
                                        "hls_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "onvif_parameter": {
                                            "parameter": {
                                                "channel": 0,
                                                "host": "",
                                                "password": "",
                                                "port": 0,
                                                "profile_token": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "stream_type": "[Main]Main/Second/Third/Fourth",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtmp_parameter": {
                                            "parameter": {
                                                "device_id": "",
                                                "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                                "rtmp_url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtsp_parameter": {
                                            "parameter": {
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        }
                                    }
                                },
                                "nvr_config": {
                                    "auth": {
                                        "password": "",
                                        "username": ""
                                    },
                                    "manage_port": 0,
                                    "video_source_config": {
                                        "hls_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "onvif_parameter": {
                                            "parameter": {
                                                "channel": 0,
                                                "host": "",
                                                "password": "",
                                                "port": 0,
                                                "profile_token": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "stream_type": "[Main]Main/Second/Third/Fourth",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtmp_parameter": {
                                            "parameter": {
                                                "device_id": "",
                                                "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                                "rtmp_url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtsp_parameter": {
                                            "parameter": {
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        }
                                    }
                                },
                                "platform_config": {
                                    "image_source_config": {
                                        "baidu_platform_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "gat1400_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "security_first_platform_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "security_third_platform_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "tao_an_platform_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "wang_li_platform_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "xinghuo_parameter": {
                                            "face_camera_parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        }
                                    },
                                    "internal_id": {
                                        "camera_idx": 0,
                                        "region_id": 0
                                    },
                                    "video_source_config": {
                                        "dh_video_cloud_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "gb28181_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "downlink_host": "",
                                                "downlink_id": "",
                                                "gb28181_local_uuid": "",
                                                "ipc": "",
                                                "password": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "ratio_type": "[SD]SD/HD",
                                                "raw_config": {
                                                    "address": "",
                                                    "block": "",
                                                    "cert_num": "",
                                                    "certifiable": 0,
                                                    "civil_code": "",
                                                    "device_id": "",
                                                    "end_time": "",
                                                    "err_code": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "info": [
                                                        {
                                                            "business_group_id": "",
                                                            "direction_type": 0,
                                                            "download_speed": "",
                                                            "position_type": 0,
                                                            "ptz_type": 0,
                                                            "resolution": "",
                                                            "room_type": 0,
                                                            "supply_light_type": 0,
                                                            "svc_space_support_mode": 0,
                                                            "svc_time_support_mode": 0,
                                                            "use_type": 0
                                                        }
                                                    ],
                                                    "ip_address": "",
                                                    "manufacturer": "",
                                                    "model": "",
                                                    "name": "",
                                                    "owner": "",
                                                    "parent_id": "",
                                                    "parental": 0,
                                                    "password": "",
                                                    "port": 0,
                                                    "register_way": 0,
                                                    "safety_way": 0,
                                                    "secrecy": 0,
                                                    "status": "[ON]ON/OFF"
                                                },
                                                "speed": 0,
                                                "start_time": "",
                                                "stop_time": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "hls_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "huawei_vcn_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "downlink_host": "",
                                                "downlink_id": "",
                                                "gb28181_local_uuid": "",
                                                "ipc": "",
                                                "password": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "ratio_type": "[SD]SD/HD",
                                                "raw_config": {
                                                    "address": "",
                                                    "block": "",
                                                    "cert_num": "",
                                                    "certifiable": 0,
                                                    "civil_code": "",
                                                    "device_id": "",
                                                    "end_time": "",
                                                    "err_code": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "info": [
                                                        {
                                                            "business_group_id": "",
                                                            "direction_type": 0,
                                                            "download_speed": "",
                                                            "position_type": 0,
                                                            "ptz_type": 0,
                                                            "resolution": "",
                                                            "room_type": 0,
                                                            "supply_light_type": 0,
                                                            "svc_space_support_mode": 0,
                                                            "svc_time_support_mode": 0,
                                                            "use_type": 0
                                                        }
                                                    ],
                                                    "ip_address": "",
                                                    "manufacturer": "",
                                                    "model": "",
                                                    "name": "",
                                                    "owner": "",
                                                    "parent_id": "",
                                                    "parental": 0,
                                                    "password": "",
                                                    "port": 0,
                                                    "register_way": 0,
                                                    "safety_way": 0,
                                                    "secrecy": 0,
                                                    "status": "[ON]ON/OFF"
                                                },
                                                "speed": 0,
                                                "start_time": "",
                                                "stop_time": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "nvr_parameter": {
                                            "parameter": {
                                                "downlink_host": "",
                                                "ipc": "",
                                                "password": "",
                                                "private": false,
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "ratio_type": "[SD]SD/HD",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "onvif_parameter": {
                                            "parameter": {
                                                "channel": 0,
                                                "host": "",
                                                "password": "",
                                                "port": 0,
                                                "profile_token": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "stream_type": "[Main]Main/Second/Third/Fourth",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtmp_parameter": {
                                            "parameter": {
                                                "device_id": "",
                                                "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                                "rtmp_url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtsp_parameter": {
                                            "parameter": {
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "sjk_parameter": {
                                            "parameter": {
                                                "ipc": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "xinghuo_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "downlink_host": "",
                                                "downlink_id": "",
                                                "gb28181_local_uuid": "",
                                                "ipc": "",
                                                "password": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "ratio_type": "[SD]SD/HD",
                                                "raw_config": {
                                                    "address": "",
                                                    "block": "",
                                                    "cert_num": "",
                                                    "certifiable": 0,
                                                    "civil_code": "",
                                                    "device_id": "",
                                                    "end_time": "",
                                                    "err_code": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "info": [
                                                        {
                                                            "business_group_id": "",
                                                            "direction_type": 0,
                                                            "download_speed": "",
                                                            "position_type": 0,
                                                            "ptz_type": 0,
                                                            "resolution": "",
                                                            "room_type": 0,
                                                            "supply_light_type": 0,
                                                            "svc_space_support_mode": 0,
                                                            "svc_time_support_mode": 0,
                                                            "use_type": 0
                                                        }
                                                    ],
                                                    "ip_address": "",
                                                    "manufacturer": "",
                                                    "model": "",
                                                    "name": "",
                                                    "owner": "",
                                                    "parent_id": "",
                                                    "parental": 0,
                                                    "password": "",
                                                    "port": 0,
                                                    "register_way": 0,
                                                    "safety_way": 0,
                                                    "secrecy": 0,
                                                    "status": "[ON]ON/OFF"
                                                },
                                                "speed": 0,
                                                "start_time": "",
                                                "stop_time": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        }
                                    }
                                }
                            },
                            "extra_info": "",
                            "last_connected_at": "",
                            "name": "",
                            "product_name": "",
                            "status": "[DS_UNACTIVED]DS_UNACTIVED/DS_ACTIVED/DS_ONLINE/DS_OFFLINE/DS_DISABLED",
                            "type": "[TT_UNKNOWN]TT_UNKNOWN/TT_EDGE_GATEWAY/TT_EDGE_DEVICE/TT_END_SUBDEVICE",
                            "updated_at": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_ListAllSubDevices")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetSubDeviceByFilterGetApi(self, sub_filter_device_id=None, sub_filter_name=None, sub_filter_address=None, sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url=None, loginToken=None, sendRequest=True, print_log=True):
        """  GetSubDeviceByFilter 根据 ID, name, IP, rtsp_url 获取子... """
        """  path: [get]/v1/subdevices/filter API """
        """  params: 
                参数名称：sub_filter.device_id　类型：string　描述：null
                参数名称：sub_filter.name　类型：string　描述：null
                参数名称：sub_filter.address　类型：string　描述：null
                参数名称：sub_filter.extra_config.camera_config.video_source_config.rtsp_parameter.parameter.url　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "subdevices": [
                        {
                            "brand": "[BR_UNSET]BR_UNSET/UNKNOWN/HIKVISION/DAHUA",
                            "created_at": "",
                            "description": "",
                            "device_config": {
                                "dns": {
                                    "primary": "",
                                    "secondary": ""
                                },
                                "ip": {
                                    "ips": [
                                        {
                                            "address": "",
                                            "gateway": "",
                                            "gateway_type": "[GT_DEFAULT]GT_DEFAULT/GT_NORMAL",
                                            "interface_name": "",
                                            "netmask": "",
                                            "type": "[IT_DHCP]IT_DHCP/IT_STATIC"
                                        }
                                    ]
                                },
                                "license_file": "",
                                "log": {
                                    "level": "[S_LOG_DEBUG]S_LOG_DEBUG/S_LOG_INFO/S_LOG_WARNNING/S_LOG_ERROR/S_LOG_NONE",
                                    "path": "",
                                    "size": 0
                                },
                                "nat": {
                                    "nats": [
                                        {
                                            "external_ip": "",
                                            "external_port": "",
                                            "internal_ip": "",
                                            "internal_port": "",
                                            "protocol": "",
                                            "status": "[SC_OK]SC_OK/SC_SC_CANCELLED/SC_UNKNOWN/SC_INVALID_ARGUMENT/SC_DEADLINE_EXCEEDED/SC_NOT_FOUND/SC_ALREADY_EXISTS/SC_PERMISSION_DENIED/SC_UNAUTHENTICATED/SC_RESOURCE_EXHAUSTED/SC_FAILED_PRECONDITION/SC_ABORTED/SC_OUT_OF_RANGE/SC_UNIMPLEMENTED/SC_INTERNAL/SC_UNAVAILABLE/SC_DATA_LOSS/SC_DEVICE_UNREACHABLE/SC_DEVICE_TIME_NOT_SYNC/SC_DEVICE_DELETED"
                                        }
                                    ]
                                },
                                "ntp": {
                                    "enable": false,
                                    "ntps": [
                                        {
                                            "port": "",
                                            "url": ""
                                        }
                                    ],
                                    "time_interval": 0
                                },
                                "ssh": {
                                    "ssh": {
                                        "enable": false,
                                        "port": ""
                                    }
                                },
                                "time_zone": {
                                    "time_zone": ""
                                },
                                "user_configs": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            },
                            "device_id": "",
                            "device_kind": "[SDK_UNSET]SDK_UNSET/CAMERA/NVR/PLATFORM",
                            "device_sn": "",
                            "disconnected_at": "",
                            "extra_config": {
                                "camera_config": {
                                    "auth": {
                                        "password": "",
                                        "username": ""
                                    },
                                    "image_source_config": {
                                        "dahua_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "deepglint_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "dummy_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "ftp_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "gat1400_ape_face_camera_parameter": {
                                            "parameter": {
                                                "ape_id": "",
                                                "extra_info": "",
                                                "password": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "hk_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "hk_isapi_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "http_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "hua_wei_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "keda_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "megvii_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "sensetime_001_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "sensetime_002_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "sensetime_d_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "symphony_nebula_face_camera_parameter": {
                                            "parameter": {
                                                "device_id": "",
                                                "task_id": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "symphony_pass_face_camera_parameter": {
                                            "parameter": {
                                                "device_id": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "tiandy_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "yuntian_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "yushi_face_camera_parameter": {
                                            "parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        }
                                    },
                                    "internal_id": {
                                        "camera_idx": 0,
                                        "region_id": 0
                                    },
                                    "manage_port": 0,
                                    "streams": {
                                        "main": {
                                            "audio": {
                                                "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                            },
                                            "video": {
                                                "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                                "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                                "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                                "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                            }
                                        },
                                        "second": {
                                            "audio": {
                                                "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                            },
                                            "video": {
                                                "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                                "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                                "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                                "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                            }
                                        },
                                        "third": {
                                            "audio": {
                                                "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                            },
                                            "video": {
                                                "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                                "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                                "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                                "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                            }
                                        }
                                    },
                                    "video_source_config": {
                                        "hls_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "onvif_parameter": {
                                            "parameter": {
                                                "channel": 0,
                                                "host": "",
                                                "password": "",
                                                "port": 0,
                                                "profile_token": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "stream_type": "[Main]Main/Second/Third/Fourth",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtmp_parameter": {
                                            "parameter": {
                                                "device_id": "",
                                                "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                                "rtmp_url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtsp_parameter": {
                                            "parameter": {
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        }
                                    }
                                },
                                "nvr_config": {
                                    "auth": {
                                        "password": "",
                                        "username": ""
                                    },
                                    "manage_port": 0,
                                    "video_source_config": {
                                        "hls_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "onvif_parameter": {
                                            "parameter": {
                                                "channel": 0,
                                                "host": "",
                                                "password": "",
                                                "port": 0,
                                                "profile_token": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "stream_type": "[Main]Main/Second/Third/Fourth",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtmp_parameter": {
                                            "parameter": {
                                                "device_id": "",
                                                "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                                "rtmp_url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtsp_parameter": {
                                            "parameter": {
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        }
                                    }
                                },
                                "platform_config": {
                                    "image_source_config": {
                                        "baidu_platform_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "gat1400_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "security_first_platform_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "security_third_platform_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "tao_an_platform_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "wang_li_platform_parameter": {
                                            "face_camera_parameter": {
                                                "ape_id": "",
                                                "raw_config": {
                                                    "ape_id": "",
                                                    "cap_direction": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "ip_addr": "",
                                                    "ipv6_addr": "",
                                                    "is_online": "",
                                                    "model": "",
                                                    "monitor_area_desc": "",
                                                    "monitor_direction": "",
                                                    "name": "",
                                                    "org_code": "",
                                                    "owner_aps_id": "",
                                                    "password": "",
                                                    "place": "",
                                                    "place_code": "",
                                                    "port": 0,
                                                    "user_id": ""
                                                },
                                                "server_id": ""
                                            },
                                            "platform_parameter": {
                                                "client_id": "",
                                                "extra_info": "",
                                                "host": "",
                                                "password": "",
                                                "platform_id": "",
                                                "port": 0,
                                                "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                                "server_id": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "xinghuo_parameter": {
                                            "face_camera_parameter": {
                                                "dir": "",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "port": 0,
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        }
                                    },
                                    "internal_id": {
                                        "camera_idx": 0,
                                        "region_id": 0
                                    },
                                    "video_source_config": {
                                        "dh_video_cloud_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "host": "",
                                                "ipc": "",
                                                "password": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "gb28181_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "downlink_host": "",
                                                "downlink_id": "",
                                                "gb28181_local_uuid": "",
                                                "ipc": "",
                                                "password": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "ratio_type": "[SD]SD/HD",
                                                "raw_config": {
                                                    "address": "",
                                                    "block": "",
                                                    "cert_num": "",
                                                    "certifiable": 0,
                                                    "civil_code": "",
                                                    "device_id": "",
                                                    "end_time": "",
                                                    "err_code": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "info": [
                                                        {
                                                            "business_group_id": "",
                                                            "direction_type": 0,
                                                            "download_speed": "",
                                                            "position_type": 0,
                                                            "ptz_type": 0,
                                                            "resolution": "",
                                                            "room_type": 0,
                                                            "supply_light_type": 0,
                                                            "svc_space_support_mode": 0,
                                                            "svc_time_support_mode": 0,
                                                            "use_type": 0
                                                        }
                                                    ],
                                                    "ip_address": "",
                                                    "manufacturer": "",
                                                    "model": "",
                                                    "name": "",
                                                    "owner": "",
                                                    "parent_id": "",
                                                    "parental": 0,
                                                    "password": "",
                                                    "port": 0,
                                                    "register_way": 0,
                                                    "safety_way": 0,
                                                    "secrecy": 0,
                                                    "status": "[ON]ON/OFF"
                                                },
                                                "speed": 0,
                                                "start_time": "",
                                                "stop_time": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "hls_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "huawei_vcn_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "downlink_host": "",
                                                "downlink_id": "",
                                                "gb28181_local_uuid": "",
                                                "ipc": "",
                                                "password": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "ratio_type": "[SD]SD/HD",
                                                "raw_config": {
                                                    "address": "",
                                                    "block": "",
                                                    "cert_num": "",
                                                    "certifiable": 0,
                                                    "civil_code": "",
                                                    "device_id": "",
                                                    "end_time": "",
                                                    "err_code": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "info": [
                                                        {
                                                            "business_group_id": "",
                                                            "direction_type": 0,
                                                            "download_speed": "",
                                                            "position_type": 0,
                                                            "ptz_type": 0,
                                                            "resolution": "",
                                                            "room_type": 0,
                                                            "supply_light_type": 0,
                                                            "svc_space_support_mode": 0,
                                                            "svc_time_support_mode": 0,
                                                            "use_type": 0
                                                        }
                                                    ],
                                                    "ip_address": "",
                                                    "manufacturer": "",
                                                    "model": "",
                                                    "name": "",
                                                    "owner": "",
                                                    "parent_id": "",
                                                    "parental": 0,
                                                    "password": "",
                                                    "port": 0,
                                                    "register_way": 0,
                                                    "safety_way": 0,
                                                    "secrecy": 0,
                                                    "status": "[ON]ON/OFF"
                                                },
                                                "speed": 0,
                                                "start_time": "",
                                                "stop_time": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "nvr_parameter": {
                                            "parameter": {
                                                "downlink_host": "",
                                                "ipc": "",
                                                "password": "",
                                                "private": false,
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "ratio_type": "[SD]SD/HD",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "onvif_parameter": {
                                            "parameter": {
                                                "channel": 0,
                                                "host": "",
                                                "password": "",
                                                "port": 0,
                                                "profile_token": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "stream_type": "[Main]Main/Second/Third/Fourth",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtmp_parameter": {
                                            "parameter": {
                                                "device_id": "",
                                                "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                                "rtmp_url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "rtsp_parameter": {
                                            "parameter": {
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "url": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "sjk_parameter": {
                                            "parameter": {
                                                "ipc": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        },
                                        "xinghuo_parameter": {
                                            "parameter": {
                                                "command_type": "[Play]Play/Playback/Download",
                                                "downlink_host": "",
                                                "downlink_id": "",
                                                "gb28181_local_uuid": "",
                                                "ipc": "",
                                                "password": "",
                                                "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                                "ratio_type": "[SD]SD/HD",
                                                "raw_config": {
                                                    "address": "",
                                                    "block": "",
                                                    "cert_num": "",
                                                    "certifiable": 0,
                                                    "civil_code": "",
                                                    "device_id": "",
                                                    "end_time": "",
                                                    "err_code": 0,
                                                    "geo_point": {
                                                        "latitude": 0,
                                                        "longitude": 0
                                                    },
                                                    "info": [
                                                        {
                                                            "business_group_id": "",
                                                            "direction_type": 0,
                                                            "download_speed": "",
                                                            "position_type": 0,
                                                            "ptz_type": 0,
                                                            "resolution": "",
                                                            "room_type": 0,
                                                            "supply_light_type": 0,
                                                            "svc_space_support_mode": 0,
                                                            "svc_time_support_mode": 0,
                                                            "use_type": 0
                                                        }
                                                    ],
                                                    "ip_address": "",
                                                    "manufacturer": "",
                                                    "model": "",
                                                    "name": "",
                                                    "owner": "",
                                                    "parent_id": "",
                                                    "parental": 0,
                                                    "password": "",
                                                    "port": 0,
                                                    "register_way": 0,
                                                    "safety_way": 0,
                                                    "secrecy": 0,
                                                    "status": "[ON]ON/OFF"
                                                },
                                                "speed": 0,
                                                "start_time": "",
                                                "stop_time": "",
                                                "user": ""
                                            },
                                            "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                        }
                                    }
                                }
                            },
                            "extra_info": "",
                            "last_connected_at": "",
                            "name": "",
                            "product_name": "",
                            "status": "[DS_UNACTIVED]DS_UNACTIVED/DS_ACTIVED/DS_ONLINE/DS_OFFLINE/DS_DISABLED",
                            "type": "[TT_UNKNOWN]TT_UNKNOWN/TT_EDGE_GATEWAY/TT_EDGE_DEVICE/TT_END_SUBDEVICE",
                            "updated_at": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetSubDeviceByFilter")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("sub_filter.device_id", sub_filter_device_id)
        intef.update_params("sub_filter.name", sub_filter_name)
        intef.update_params("sub_filter.address", sub_filter_address)
        intef.update_params("sub_filter.extra_config.camera_config.video_source_config.rtsp_parameter.parameter.url", sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetSubDeviceStreamsByIDGetApi(self, id, loginToken=None, sendRequest=True, print_log=True):
        """   """
        """  path: [get]/v1/subdevices/streams/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "streams": {
                        "main": {
                            "audio": {
                                "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                            },
                            "video": {
                                "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                            }
                        },
                        "second": {
                            "audio": {
                                "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                            },
                            "video": {
                                "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                            }
                        },
                        "third": {
                            "audio": {
                                "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                            },
                            "video": {
                                "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                            }
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetSubDeviceStreamsByID")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_GetSubDeviceByIDGetApi(self, id, loginToken=None, sendRequest=True, print_log=True):
        """  GetSubDeviceByID 根据 ID 获取子设备信息 """
        """  path: [get]/v1/subdevices/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "subdevice": {
                        "brand": "[BR_UNSET]BR_UNSET/UNKNOWN/HIKVISION/DAHUA",
                        "created_at": "",
                        "description": "",
                        "device_config": {
                            "dns": {
                                "primary": "",
                                "secondary": ""
                            },
                            "ip": {
                                "ips": [
                                    {
                                        "address": "",
                                        "gateway": "",
                                        "gateway_type": "[GT_DEFAULT]GT_DEFAULT/GT_NORMAL",
                                        "interface_name": "",
                                        "netmask": "",
                                        "type": "[IT_DHCP]IT_DHCP/IT_STATIC"
                                    }
                                ]
                            },
                            "license_file": "",
                            "log": {
                                "level": "[S_LOG_DEBUG]S_LOG_DEBUG/S_LOG_INFO/S_LOG_WARNNING/S_LOG_ERROR/S_LOG_NONE",
                                "path": "",
                                "size": 0
                            },
                            "nat": {
                                "nats": [
                                    {
                                        "external_ip": "",
                                        "external_port": "",
                                        "internal_ip": "",
                                        "internal_port": "",
                                        "protocol": "",
                                        "status": "[SC_OK]SC_OK/SC_SC_CANCELLED/SC_UNKNOWN/SC_INVALID_ARGUMENT/SC_DEADLINE_EXCEEDED/SC_NOT_FOUND/SC_ALREADY_EXISTS/SC_PERMISSION_DENIED/SC_UNAUTHENTICATED/SC_RESOURCE_EXHAUSTED/SC_FAILED_PRECONDITION/SC_ABORTED/SC_OUT_OF_RANGE/SC_UNIMPLEMENTED/SC_INTERNAL/SC_UNAVAILABLE/SC_DATA_LOSS/SC_DEVICE_UNREACHABLE/SC_DEVICE_TIME_NOT_SYNC/SC_DEVICE_DELETED"
                                    }
                                ]
                            },
                            "ntp": {
                                "enable": false,
                                "ntps": [
                                    {
                                        "port": "",
                                        "url": ""
                                    }
                                ],
                                "time_interval": 0
                            },
                            "ssh": {
                                "ssh": {
                                    "enable": false,
                                    "port": ""
                                }
                            },
                            "time_zone": {
                                "time_zone": ""
                            },
                            "user_configs": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            }
                        },
                        "device_id": "",
                        "device_kind": "[SDK_UNSET]SDK_UNSET/CAMERA/NVR/PLATFORM",
                        "device_sn": "",
                        "disconnected_at": "",
                        "extra_config": {
                            "camera_config": {
                                "auth": {
                                    "password": "",
                                    "username": ""
                                },
                                "image_source_config": {
                                    "dahua_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "deepglint_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "dummy_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "ftp_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "gat1400_ape_face_camera_parameter": {
                                        "parameter": {
                                            "ape_id": "",
                                            "extra_info": "",
                                            "password": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hk_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hk_isapi_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "http_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hua_wei_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "keda_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "megvii_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sensetime_001_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sensetime_002_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sensetime_d_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "symphony_nebula_face_camera_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "task_id": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "symphony_pass_face_camera_parameter": {
                                        "parameter": {
                                            "device_id": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "tiandy_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "yuntian_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "yushi_face_camera_parameter": {
                                        "parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                },
                                "internal_id": {
                                    "camera_idx": 0,
                                    "region_id": 0
                                },
                                "manage_port": 0,
                                "streams": {
                                    "main": {
                                        "audio": {
                                            "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                        },
                                        "video": {
                                            "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                            "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                            "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                            "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                        }
                                    },
                                    "second": {
                                        "audio": {
                                            "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                        },
                                        "video": {
                                            "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                            "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                            "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                            "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                        }
                                    },
                                    "third": {
                                        "audio": {
                                            "Acodec": "[AcUnset]AcUnset/AcGv722v1/AcGv711ULAW/AcGv711ALAW/AcMP2L2/AcG_726/AcAAC/AcPCM",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF"
                                        },
                                        "video": {
                                            "BitRate": "[BRUnset]BRUnset/BR256/BR512/BR1024/BR2048/BR3072/BR4096/BR6144/BR8192/BR12288/BR16384",
                                            "Enable": "[SwUnset]SwUnset/SwON/SwOFF",
                                            "FrameRate": "[FRUnset]FRUnset/FR1/FR2/FR4/FR6/FR8/FR10/FR12/FR15/FR16/FR18/FR20/FR22/FR25/FR1v2/FR1v4/FR1v8/FR1v16",
                                            "Resolution": "[RUnset]RUnset/R640x480/R704x576/R1280x720/R1280x960/R1920x1080/R2560x1440/R2688x1520/R3840x2160/R4096x2160/R3072x1728",
                                            "Vcodec": "[VcUnset]VcUnset/Vch264/Vch265"
                                        }
                                    }
                                },
                                "video_source_config": {
                                    "hls_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "onvif_parameter": {
                                        "parameter": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtmp_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtsp_parameter": {
                                        "parameter": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                }
                            },
                            "nvr_config": {
                                "auth": {
                                    "password": "",
                                    "username": ""
                                },
                                "manage_port": 0,
                                "video_source_config": {
                                    "hls_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "onvif_parameter": {
                                        "parameter": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtmp_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtsp_parameter": {
                                        "parameter": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                }
                            },
                            "platform_config": {
                                "image_source_config": {
                                    "baidu_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "gat1400_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "security_first_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "security_third_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "tao_an_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "wang_li_platform_parameter": {
                                        "face_camera_parameter": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "platform_parameter": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "xinghuo_parameter": {
                                        "face_camera_parameter": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                },
                                "internal_id": {
                                    "camera_idx": 0,
                                    "region_id": 0
                                },
                                "video_source_config": {
                                    "dh_video_cloud_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "gb28181_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "hls_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "huawei_vcn_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "nvr_parameter": {
                                        "parameter": {
                                            "downlink_host": "",
                                            "ipc": "",
                                            "password": "",
                                            "private": false,
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "onvif_parameter": {
                                        "parameter": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtmp_parameter": {
                                        "parameter": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "rtsp_parameter": {
                                        "parameter": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "sjk_parameter": {
                                        "parameter": {
                                            "ipc": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    },
                                    "xinghuo_parameter": {
                                        "parameter": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "source_type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                    }
                                }
                            }
                        },
                        "extra_info": "",
                        "last_connected_at": "",
                        "name": "",
                        "product_name": "",
                        "status": "[DS_UNACTIVED]DS_UNACTIVED/DS_ACTIVED/DS_ONLINE/DS_OFFLINE/DS_DISABLED",
                        "type": "[TT_UNKNOWN]TT_UNKNOWN/TT_EDGE_GATEWAY/TT_EDGE_DEVICE/TT_END_SUBDEVICE",
                        "updated_at": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_GetSubDeviceByID")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def NebulaIOTAgentSrv_RemoveSubDeviceByIDDeleteApi(self, id, skip=None, loginToken=None, sendRequest=True, print_log=True):
        """  RemoveSubDeviceByID 根据 ID 删除子设备 """
        """  path: [delete]/v1/subdevices/{id} API """
        """  params: 
                参数名称：skip　类型：boolean　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaIOTAgentSrv_RemoveSubDeviceByID")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("skip", skip)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def NebulaKongGatewaySrv_ImportKongConfigByBizappPostApi(self, bizapp=None, config=None, loginToken=None, sendRequest=True, print_log=True):
        """  上传bizapp kong gateway配置文件 """
        """  path: [post]/v1/gateway/config API """
        """  body: 
                {
                    "bizapp": "",
                    "config": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaKongGatewaySrv_ImportKongConfigByBizapp")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("bizapp", bizapp)
        intef.update_body("config", config)
        return intef.request() if sendRequest else intef

    def NebulaKongGatewaySrv_GetPluginApiAuthWhiteUrlsGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  获取nebula-api-auth.white_urls """
        """  path: [get]/v1/gateway/plugin/api_auth/white_urls API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "urls": [
                        {
                            "method": "",
                            "path": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaKongGatewaySrv_GetPluginApiAuthWhiteUrls")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaKongGatewaySrv_DelPluginApiAuthWhiteUrlsDeleteApi(self, url_path=None, url_method=None, loginToken=None, sendRequest=True, print_log=True):
        """  删除nebula-api-auth.white_urls """
        """  path: [delete]/v1/gateway/plugin/api_auth/white_urls API """
        """  params: 
                参数名称：url.path　类型：string　描述：null
                参数名称：url.method　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaKongGatewaySrv_DelPluginApiAuthWhiteUrls")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("url.path", url_path)
        intef.update_params("url.method", url_method)
        return intef.request() if sendRequest else intef

    def NebulaKongGatewaySrv_AddPluginApiAuthWhiteUrlsPostApi(self, url=None, loginToken=None, sendRequest=True, print_log=True):
        """  增加nebula-api-auth.white_urls """
        """  path: [post]/v1/gateway/plugin/api_auth/white_urls API """
        """  body: 
                {
                    "url": {
                        "method": "",
                        "path": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaKongGatewaySrv_AddPluginApiAuthWhiteUrls")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("url", url)
        return intef.request() if sendRequest else intef

    def NebulaKongGatewaySrv_GetPluginJwtWhiteUrlsGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  获取nebula-jwt.white_urls """
        """  path: [get]/v1/gateway/plugin/jwt/white_urls API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "urls": [
                        {
                            "method": "",
                            "path": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaKongGatewaySrv_GetPluginJwtWhiteUrls")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NebulaKongGatewaySrv_DelPluginJwtWhiteUrlsDeleteApi(self, url_path=None, url_method=None, loginToken=None, sendRequest=True, print_log=True):
        """  删除nebula-jwt.white_urls """
        """  path: [delete]/v1/gateway/plugin/jwt/white_urls API """
        """  params: 
                参数名称：url.path　类型：string　描述：null
                参数名称：url.method　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaKongGatewaySrv_DelPluginJwtWhiteUrls")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("url.path", url_path)
        intef.update_params("url.method", url_method)
        return intef.request() if sendRequest else intef

    def NebulaKongGatewaySrv_AddPluginJwtWhiteUrlsPostApi(self, url=None, loginToken=None, sendRequest=True, print_log=True):
        """  增加nebula-jwt.white_urls """
        """  path: [post]/v1/gateway/plugin/jwt/white_urls API """
        """  body: 
                {
                    "url": {
                        "method": "",
                        "path": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaKongGatewaySrv_AddPluginJwtWhiteUrls")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("url", url)
        return intef.request() if sendRequest else intef

    def NebulaKongGatewaySrv_GetKongConfigByBizappGetApi(self, bizapp, loginToken=None, sendRequest=True, print_log=True):
        """  获取bizapp kong gateway配置文件 """
        """  path: [get]/v1/gateway/{bizapp}/config API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "bizapp": "",
                    "code": 0,
                    "config": "",
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaKongGatewaySrv_GetKongConfigByBizapp")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("bizapp", bizapp)
        return intef.request() if sendRequest else intef

    def NebulaKongGatewaySrv_RemoveKongConfigByBizappDeleteApi(self, bizapp, loginToken=None, sendRequest=True, print_log=True):
        """  删除bizapp kong gateway配置文件 """
        """  path: [delete]/v1/gateway/{bizapp}/config API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaKongGatewaySrv_RemoveKongConfigByBizapp")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("bizapp", bizapp)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_BatchCreateTaskPostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True):
        """  创建任务 """
        """  path: [post]/v1/bizapp/default/batch_task API """
        """  body: 
                {
                    "requests": [
                        {
                            "active": 0,
                            "dbs": "",
                            "desc": "",
                            "detect_type": "",
                            "extend_config": "",
                            "header": {
                                "trace": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            },
                            "identifier_id": "",
                            "name": "",
                            "not_support_merge": false,
                            "object_config": "",
                            "schedule": "",
                            "stream_type": 0,
                            "sub_device_ids": [],
                            "task_type": ""
                        }
                    ]
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_BatchCreateTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_DeleteRecordPostApi(self, ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  删除记录 """
        """  path: [post]/v1/bizapp/default/record/delete API """
        """  body: 
                {
                    "ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "affected": 0,
                    "code": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_DeleteRecord")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("ids", ids)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_ExportRecordPostApi(self, start_time=None, end_time=None, sub_device_name=None, sub_device_id=None, task_name=None, task_id=None, task_type=None, applet_record_type=None, lib_type=None, portrait_id=None, name=None, page=None, attributes=None, loginToken=None, sendRequest=True, print_log=True):
        """  导出记录 """
        """  path: [post]/v1/bizapp/default/record/export API """
        """  body: 
                {
                    "applet_record_type": [],
                    "attributes": [
                        {
                            "attr_name": "",
                            "attr_value": "",
                            "operator": ""
                        }
                    ],
                    "end_time": "",
                    "lib_type": 0,
                    "name": "",
                    "page": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    },
                    "portrait_id": "",
                    "start_time": "",
                    "sub_device_id": "",
                    "sub_device_name": "",
                    "task_id": "",
                    "task_name": "",
                    "task_type": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "data": {
                        "password": "",
                        "path": ""
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_ExportRecord")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("start_time", start_time)
        intef.update_body("end_time", end_time)
        intef.update_body("sub_device_name", sub_device_name)
        intef.update_body("sub_device_id", sub_device_id)
        intef.update_body("task_name", task_name)
        intef.update_body("task_id", task_id)
        intef.update_body("task_type", task_type)
        intef.update_body("applet_record_type", applet_record_type)
        intef.update_body("lib_type", lib_type)
        intef.update_body("portrait_id", portrait_id)
        intef.update_body("name", name)
        intef.update_body("page", page)
        intef.update_body("attributes", attributes)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_QueryRecordPostApi(self, start_time=None, end_time=None, sub_device_name=None, sub_device_id=None, task_name=None, task_id=None, task_type=None, applet_record_type=None, lib_type=None, portrait_id=None, name=None, page=None, attributes=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询记录 """
        """  path: [post]/v1/bizapp/default/record/query API """
        """  body: 
                {
                    "applet_record_type": [],
                    "attributes": [
                        {
                            "attr_name": "",
                            "attr_value": "",
                            "operator": ""
                        }
                    ],
                    "end_time": "",
                    "lib_type": 0,
                    "name": "",
                    "page": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    },
                    "portrait_id": "",
                    "start_time": "",
                    "sub_device_id": "",
                    "sub_device_name": "",
                    "task_id": "",
                    "task_name": "",
                    "task_type": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "data": [
                        {
                            "applet": "",
                            "applet_record_type": "",
                            "attrs": "",
                            "captured_time": "",
                            "create_time": "",
                            "detect_type": "",
                            "event_id": "",
                            "id": "",
                            "lib_info": "",
                            "object_id": "",
                            "panoramic_image_url": "",
                            "particular": "",
                            "portrait_image_location": "",
                            "portrait_image_url": "",
                            "push_interval": "",
                            "received_time": "",
                            "record_type": "",
                            "roi": "",
                            "stacked": "",
                            "sub_device_id": "",
                            "sub_device_name": "",
                            "task_extra_info": "",
                            "task_id": "",
                            "task_name": "",
                            "task_type": "",
                            "tms_id": ""
                        }
                    ],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "page": {
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_QueryRecord")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("start_time", start_time)
        intef.update_body("end_time", end_time)
        intef.update_body("sub_device_name", sub_device_name)
        intef.update_body("sub_device_id", sub_device_id)
        intef.update_body("task_name", task_name)
        intef.update_body("task_id", task_id)
        intef.update_body("task_type", task_type)
        intef.update_body("applet_record_type", applet_record_type)
        intef.update_body("lib_type", lib_type)
        intef.update_body("portrait_id", portrait_id)
        intef.update_body("name", name)
        intef.update_body("page", page)
        intef.update_body("attributes", attributes)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_UpdateRecordPostApi(self, field=None, ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  更新记录 """
        """  path: [post]/v1/bizapp/default/record/update API """
        """  body: 
                {
                    "field": "",
                    "ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "affected": 0,
                    "code": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_UpdateRecord")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("field", field)
        intef.update_body("ids", ids)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_DeleteTaskDeleteApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  删除任务 """
        """  path: [delete]/v1/bizapp/default/task API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_DeleteTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_CreateTaskPostApi(self, name=None, task_type=None, desc=None, detect_type=None, active=None, sub_device_ids=None, object_config=None, extend_config=None, schedule=None, identifier_id=None, stream_type=None, not_support_merge=None, dbs=None, loginToken=None, sendRequest=True, print_log=True):
        """  创建任务 """
        """  path: [post]/v1/bizapp/default/task API """
        """  body: 
                {
                    "active": 0,
                    "dbs": "",
                    "desc": "",
                    "detect_type": "",
                    "extend_config": "",
                    "identifier_id": "",
                    "name": "",
                    "not_support_merge": false,
                    "object_config": "",
                    "schedule": "",
                    "stream_type": 0,
                    "sub_device_ids": [],
                    "task_type": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_CreateTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("task_type", task_type)
        intef.update_body("desc", desc)
        intef.update_body("detect_type", detect_type)
        intef.update_body("active", active)
        intef.update_body("sub_device_ids", sub_device_ids)
        intef.update_body("object_config", object_config)
        intef.update_body("extend_config", extend_config)
        intef.update_body("schedule", schedule)
        intef.update_body("identifier_id", identifier_id)
        intef.update_body("stream_type", stream_type)
        intef.update_body("not_support_merge", not_support_merge)
        intef.update_body("dbs", dbs)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_UpdateTaskPutApi(self, task_ids=None, name=None, desc=None, object_config=None, extend_config=None, schedule=None, dbs=None, loginToken=None, sendRequest=True, print_log=True):
        """  修改任务 """
        """  path: [put]/v1/bizapp/default/task API """
        """  body: 
                {
                    "dbs": "",
                    "desc": "",
                    "extend_config": "",
                    "name": "",
                    "object_config": "",
                    "schedule": "",
                    "task_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_UpdateTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("task_ids", task_ids)
        intef.update_body("name", name)
        intef.update_body("desc", desc)
        intef.update_body("object_config", object_config)
        intef.update_body("extend_config", extend_config)
        intef.update_body("schedule", schedule)
        intef.update_body("dbs", dbs)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_QueryAllTaskPostApi(self, active=None, db_id=None, task_types=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询所有任务(无分页)，使用场景：任务的下拉框查询 """
        """  path: [post]/v1/bizapp/default/task/all API """
        """  body: 
                {
                    "active": 0,
                    "db_id": "",
                    "task_types": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "list": [
                        {
                            "active": 0,
                            "name": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_QueryAllTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("active", active)
        intef.update_body("db_id", db_id)
        intef.update_body("task_types", task_types)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_DisableTaskPutApi(self, task_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  禁用任务 """
        """  path: [put]/v1/bizapp/default/task/disable API """
        """  body: 
                {
                    "task_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_DisableTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("task_ids", task_ids)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_EnableTaskPutApi(self, task_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  启用任务 """
        """  path: [put]/v1/bizapp/default/task/enable API """
        """  body: 
                {
                    "task_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_EnableTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("task_ids", task_ids)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_QueryTaskPostApi(self, page_num=None, page_size=None, keyword=None, sub_device_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询任务(有分页)，正常的分页查询 """
        """  path: [post]/v1/bizapp/default/task/query API """
        """  body: 
                {
                    "keyword": "",
                    "page_num": 0,
                    "page_size": 0,
                    "sub_device_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "enabled_task_num": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "list": [
                        {
                            "active": 0,
                            "app_name": "",
                            "consumed_power": 0,
                            "dbs": "",
                            "decimal_consumed_power": "",
                            "desc": "",
                            "detect_type": "",
                            "extend_config": "",
                            "name": "",
                            "object_config": "",
                            "pu": 0,
                            "rtsp_address": "",
                            "schedule": "",
                            "state": 0,
                            "state_msg": "",
                            "stream_type": 0,
                            "sub_device_id": "",
                            "sub_device_name": "",
                            "support_merge": 0,
                            "task_id": "",
                            "task_type": "",
                            "tms_id": ""
                        }
                    ],
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_QueryTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("page_num", page_num)
        intef.update_body("page_size", page_size)
        intef.update_body("keyword", keyword)
        intef.update_body("sub_device_ids", sub_device_ids)
        return intef.request() if sendRequest else intef

    def BizAppTaskDefaultService_DetailTaskGetApi(self, task_id, loginToken=None, sendRequest=True, print_log=True):
        """  详情任务 """
        """  path: [get]/v1/bizapp/default/task/{task_id}/detail API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "active": 0,
                    "app_name": "",
                    "consumed_power": 0,
                    "dbs": "",
                    "decimal_consumed_power": "",
                    "desc": "",
                    "detect_type": "",
                    "extend_config": "",
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "name": "",
                    "object_config": "",
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "pu": 0,
                    "rtsp_address": "",
                    "schedule": "",
                    "state": 0,
                    "state_msg": "",
                    "stream_type": 0,
                    "sub_device_id": "",
                    "sub_device_name": "",
                    "support_merge": 0,
                    "task_id": "",
                    "task_type": "",
                    "tms_id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskDefaultService_DetailTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def BizAppTaskService_DeleteTaskDeleteApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  删除任务 """
        """  path: [delete]/v1/bizapptasks API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskService_DeleteTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BizAppTaskService_CreateTaskPostApi(self, name=None, task_type=None, desc=None, detect_type=None, active=None, sub_device_ids=None, object_config=None, extend_config=None, schedule=None, identifier_id=None, stream_type=None, not_support_merge=None, dbs=None, loginToken=None, sendRequest=True, print_log=True):
        """  创建任务, response里始终包括匹配个数的Result, bizapp-default依赖此约... """
        """  path: [post]/v1/bizapptasks API """
        """  body: 
                {
                    "active": 0,
                    "dbs": "",
                    "desc": "",
                    "detect_type": "",
                    "extend_config": "",
                    "identifier_id": "",
                    "name": "",
                    "not_support_merge": false,
                    "object_config": "",
                    "schedule": "",
                    "stream_type": 0,
                    "sub_device_ids": [],
                    "task_type": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskService_CreateTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("task_type", task_type)
        intef.update_body("desc", desc)
        intef.update_body("detect_type", detect_type)
        intef.update_body("active", active)
        intef.update_body("sub_device_ids", sub_device_ids)
        intef.update_body("object_config", object_config)
        intef.update_body("extend_config", extend_config)
        intef.update_body("schedule", schedule)
        intef.update_body("identifier_id", identifier_id)
        intef.update_body("stream_type", stream_type)
        intef.update_body("not_support_merge", not_support_merge)
        intef.update_body("dbs", dbs)
        return intef.request() if sendRequest else intef

    def BizAppTaskService_UpdateTaskPutApi(self, task_ids=None, name=None, desc=None, object_config=None, extend_config=None, schedule=None, dbs=None, loginToken=None, sendRequest=True, print_log=True):
        """  修改任务 """
        """  path: [put]/v1/bizapptasks API """
        """  body: 
                {
                    "dbs": "",
                    "desc": "",
                    "extend_config": "",
                    "name": "",
                    "object_config": "",
                    "schedule": "",
                    "task_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskService_UpdateTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("task_ids", task_ids)
        intef.update_body("name", name)
        intef.update_body("desc", desc)
        intef.update_body("object_config", object_config)
        intef.update_body("extend_config", extend_config)
        intef.update_body("schedule", schedule)
        intef.update_body("dbs", dbs)
        return intef.request() if sendRequest else intef

    def BizAppTaskService_QueryAllTaskPostApi(self, active=None, db_id=None, task_types=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询所有任务(无分页)，使用场景：任务的下拉框查询 """
        """  path: [post]/v1/bizapptasks/all API """
        """  body: 
                {
                    "active": 0,
                    "db_id": "",
                    "task_types": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "list": [
                        {
                            "active": 0,
                            "name": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskService_QueryAllTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("active", active)
        intef.update_body("db_id", db_id)
        intef.update_body("task_types", task_types)
        return intef.request() if sendRequest else intef

    def BizAppTaskService_DisableTaskPutApi(self, task_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  禁用任务 """
        """  path: [put]/v1/bizapptasks/disable API """
        """  body: 
                {
                    "task_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskService_DisableTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("task_ids", task_ids)
        return intef.request() if sendRequest else intef

    def BizAppTaskService_EnableTaskPutApi(self, task_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  启用任务 """
        """  path: [put]/v1/bizapptasks/enable API """
        """  body: 
                {
                    "task_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "failed": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "results": [
                        {
                            "code": 0,
                            "message": "",
                            "sub_device_id": "",
                            "task_id": ""
                        }
                    ],
                    "success": 0,
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskService_EnableTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("task_ids", task_ids)
        return intef.request() if sendRequest else intef

    def BizAppTaskService_LicenseStatisticsGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  License授权信息 """
        """  path: [get]/v1/bizapptasks/license_statis API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "business_quota": {
                        "additionalProp1": 0,
                        "additionalProp2": 0,
                        "additionalProp3": 0
                    },
                    "business_used_quota": {
                        "additionalProp1": 0,
                        "additionalProp2": 0,
                        "additionalProp3": 0
                    },
                    "code_info": [
                        {
                            "authid": {
                                "dongle_ids": [],
                                "user_algo_name": ""
                            },
                            "image_process_auth": {
                                "qps": 0
                            },
                            "video_process_auth": {
                                "ResolutionChannels": [
                                    {
                                        "quota": 0,
                                        "resolution": "[RESOLUTION_UNKNOWN]RESOLUTION_UNKNOWN/RESOLUTION_QCIF/RESOLUTION_CIF/RESOLUTION_4CIF/RESOLUTION_D1/RESOLUTION_720P/RESOLUTION_1080P/RESOLUTION_2K/RESOLUTION_4K"
                                    }
                                ],
                                "channels": 0
                            }
                        }
                    ],
                    "object_type_ratio": {
                        "additionalProp1": 0,
                        "additionalProp2": 0,
                        "additionalProp3": 0
                    },
                    "resolution_ratio": {
                        "additionalProp1": 0,
                        "additionalProp2": 0,
                        "additionalProp3": 0
                    },
                    "task_num": {
                        "additionalProp1": 0,
                        "additionalProp2": 0,
                        "additionalProp3": 0
                    },
                    "task_type_ratio": {
                        "additionalProp1": 0,
                        "additionalProp2": 0,
                        "additionalProp3": 0
                    },
                    "type_quota": {
                        "additionalProp1": 0,
                        "additionalProp2": 0,
                        "additionalProp3": 0
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskService_LicenseStatistics")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BizAppTaskService_PowerInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  获取算力信息 """
        """  path: [get]/v1/bizapptasks/power_info API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "info": {
                        "remained": {
                            "additionalProp1": {
                                "algo": 0,
                                "face": 0,
                                "ips": 0
                            },
                            "additionalProp2": {
                                "algo": 0,
                                "face": 0,
                                "ips": 0
                            },
                            "additionalProp3": {
                                "algo": 0,
                                "face": 0,
                                "ips": 0
                            }
                        },
                        "total": 0
                    },
                    "strategy": {
                        "arch": "",
                        "auto_start_ips": false,
                        "create_worker": "",
                        "face_quota": {
                            "additionalProp1": 0,
                            "additionalProp2": 0,
                            "additionalProp3": 0
                        },
                        "gpu_utils_rate_limit": 0,
                        "ips_quota": {
                            "additionalProp1": 0,
                            "additionalProp2": 0,
                            "additionalProp3": 0
                        },
                        "pre_start_ips": false,
                        "pu_type": "",
                        "select_worker": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskService_PowerInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def BizAppTaskService_QueryTaskPostApi(self, page_num=None, page_size=None, keyword=None, sub_device_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询任务(有分页)，正常的分页查询 """
        """  path: [post]/v1/bizapptasks/query API """
        """  body: 
                {
                    "keyword": "",
                    "page_num": 0,
                    "page_size": 0,
                    "sub_device_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "enabled_task_num": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "list": [
                        {
                            "active": 0,
                            "app_name": "",
                            "consumed_power": 0,
                            "dbs": "",
                            "decimal_consumed_power": "",
                            "desc": "",
                            "detect_type": "",
                            "extend_config": "",
                            "name": "",
                            "object_config": "",
                            "pu": 0,
                            "rtsp_address": "",
                            "schedule": "",
                            "state": 0,
                            "state_msg": "",
                            "stream_type": 0,
                            "sub_device_id": "",
                            "sub_device_name": "",
                            "support_merge": 0,
                            "task_id": "",
                            "task_type": "",
                            "tms_id": ""
                        }
                    ],
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "total": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskService_QueryTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("page_num", page_num)
        intef.update_body("page_size", page_size)
        intef.update_body("keyword", keyword)
        intef.update_body("sub_device_ids", sub_device_ids)
        return intef.request() if sendRequest else intef

    def BizAppTaskService_DetailTaskGetApi(self, task_id, loginToken=None, sendRequest=True, print_log=True):
        """  详情任务 """
        """  path: [get]/v1/bizapptasks/{task_id}/detail API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "active": 0,
                    "app_name": "",
                    "consumed_power": 0,
                    "dbs": "",
                    "decimal_consumed_power": "",
                    "desc": "",
                    "detect_type": "",
                    "extend_config": "",
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "name": "",
                    "object_config": "",
                    "op_sync_info": {
                        "op_version": ""
                    },
                    "pu": 0,
                    "rtsp_address": "",
                    "schedule": "",
                    "state": 0,
                    "state_msg": "",
                    "stream_type": 0,
                    "sub_device_id": "",
                    "sub_device_name": "",
                    "support_merge": 0,
                    "task_id": "",
                    "task_type": "",
                    "tms_id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "BizAppTaskService_DetailTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def ScheduleService_GetStorageInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  获取当前抓拍图片存储空间信息 """
        """  path: [get]/v1/schedule/image_storage_info API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "coverage_rate": "",
                    "keep_days": 0,
                    "message": "",
                    "remaining_days": 0,
                    "total_storage": "",
                    "used_storage": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "ScheduleService_GetStorageInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ScheduleService_ClearRecordDeleteApi(self, loginToken=None, sendRequest=True, print_log=True):
        """   """
        """  path: [delete]/v1/schedule/record API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "details": [],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "ScheduleService_ClearRecord")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ScheduleService_GetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  获取一些系统配置信息 """
        """  path: [get]/v1/schedule/sys_info API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "message": "",
                    "mq_type": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "ScheduleService_GetSystemInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ScheduleService_SetSystemInfoPostApi(self, save_days=None, loginToken=None, sendRequest=True, print_log=True):
        """  设置一些系统配置信息 """
        """  path: [post]/v1/schedule/sys_info API """
        """  body: 
                {
                    "save_days": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "ScheduleService_SetSystemInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("save_days", save_days)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_BatchGetTaskGetApi(self, task_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  批量获取任务 """
        """  path: [get]/v1/batch-tasks API """
        """  params: 
                参数名称：task_ids　类型：array　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "responses": [
                        {
                            "header": {
                                "timestamp": "",
                                "trace": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            },
                            "task": {
                                "camera_info": {
                                    "camera_id": "",
                                    "device_id": "",
                                    "device_type": "",
                                    "internal_id": {
                                        "camera_idx": 0,
                                        "region_id": 0
                                    },
                                    "place_code": "",
                                    "place_name": "",
                                    "platform_id": "",
                                    "source_id": "",
                                    "tollgate_id": "",
                                    "tollgate_name": "",
                                    "zone_id": ""
                                },
                                "consumed_power": 0,
                                "dbs": [
                                    {
                                        "db_id": "",
                                        "db_name": "",
                                        "min_score": 0,
                                        "top_k": 0
                                    }
                                ],
                                "decimal_consumed_power": "",
                                "desc": "",
                                "external_id": "",
                                "extra_info": "",
                                "merge": false,
                                "merge_id": "",
                                "name": "",
                                "object_config": {
                                    "algo_config": {
                                        "app_name": "",
                                        "app_version": 0,
                                        "data": {
                                            "type_url": "",
                                            "value": ""
                                        }
                                    },
                                    "crowd_config": {
                                        "crowd_thresh": 0,
                                        "enable_density_map": false,
                                        "enable_strand_analyze": false,
                                        "enable_strand_map": false,
                                        "labeled_person": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "panoramic_mode": "[OutputOnAlarm]OutputOnAlarm/OutputOff/OutputForever",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "scene_area": 0,
                                        "strand_roi": [
                                            {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            }
                                        ],
                                        "strand_thresh": 0
                                    },
                                    "decoder_config": {
                                        "set_skip_frame_num": false,
                                        "skip_frame_num": 0
                                    },
                                    "face_config": {
                                        "target_select_config": {
                                            "max_track_time": 0,
                                            "quick_response_time": 0,
                                            "set_max_track_time": false,
                                            "set_quick_response_time": false,
                                            "set_time_interval": false,
                                            "time_interval": 0
                                        }
                                    },
                                    "faceped_config": {
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "target_select_config": {
                                            "additionalProp1": {
                                                "max_track_time": 0,
                                                "quick_response_time": 0,
                                                "set_max_track_time": false,
                                                "set_quick_response_time": false,
                                                "set_time_interval": false,
                                                "time_interval": 0
                                            },
                                            "additionalProp2": {
                                                "max_track_time": 0,
                                                "quick_response_time": 0,
                                                "set_max_track_time": false,
                                                "set_quick_response_time": false,
                                                "set_time_interval": false,
                                                "time_interval": 0
                                            },
                                            "additionalProp3": {
                                                "max_track_time": 0,
                                                "quick_response_time": 0,
                                                "set_max_track_time": false,
                                                "set_quick_response_time": false,
                                                "set_time_interval": false,
                                                "time_interval": 0
                                            }
                                        }
                                    },
                                    "lite_faceped_config": {
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "select_frame_policy": "[ENTER]ENTER/OPTIMAL/PERIODIC"
                                    },
                                    "pach_config": {
                                        "target_select_config": {
                                            "max_track_time": 0,
                                            "quick_response_time": 0,
                                            "set_max_track_time": false,
                                            "set_quick_response_time": false,
                                            "set_time_interval": false,
                                            "time_interval": 0
                                        }
                                    },
                                    "rules": [
                                        {
                                            "direction": {
                                                "x": 0,
                                                "y": 0
                                            },
                                            "duration": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "rule_id": "",
                                            "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                        }
                                    ],
                                    "scenario_rules": [
                                        {
                                            "detect_thresh": 0,
                                            "roi": [
                                                {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                }
                                            ],
                                            "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                        }
                                    ]
                                },
                                "object_types": [
                                    "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                                ],
                                "pu": 0,
                                "schedule_config": {
                                    "end_date": "",
                                    "exec_times": [
                                        {
                                            "end_time": "",
                                            "start_time": ""
                                        }
                                    ],
                                    "start_date": "",
                                    "weekday": {
                                        "additionalProp1": false,
                                        "additionalProp2": false,
                                        "additionalProp3": false
                                    }
                                },
                                "source_addr": "",
                                "source_information": {
                                    "parameter": {
                                        "cvr": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "dh_video_cloud": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "user": ""
                                        },
                                        "face_camera": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "gat1400": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "gat1400_ape": {
                                            "ape_id": "",
                                            "extra_info": "",
                                            "password": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "user": ""
                                        },
                                        "gat1400_face_camera": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "hls": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "nvr": {
                                            "downlink_host": "",
                                            "ipc": "",
                                            "password": "",
                                            "private": false,
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "user": ""
                                        },
                                        "onvif": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "rtmp": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "rtsp": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "sjk": {
                                            "ipc": ""
                                        },
                                        "symphony_nebula": {
                                            "device_id": "",
                                            "task_id": ""
                                        },
                                        "symphony_pass": {
                                            "device_id": ""
                                        }
                                    },
                                    "type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                },
                                "source_protocol": "",
                                "status": "[TaskStatusUnset]TaskStatusUnset/TaskPending/TaskScheduleFailed/TaskRuning/TaskFinish/TaskInternalErr/TaskStopFailed/TaskSubmitted",
                                "storage_policy": {
                                    "binary_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {
                                            "enable": false
                                        },
                                        "osg": {
                                            "enable": false
                                        }
                                    },
                                    "panoramic_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {
                                            "enable": false
                                        },
                                        "osg": {
                                            "enable": false
                                        }
                                    },
                                    "portrait_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {
                                            "enable": false
                                        },
                                        "osg": {
                                            "enable": false
                                        }
                                    }
                                },
                                "sub_device_id": "",
                                "task_id": "",
                                "type": "[TaskTypeUnset]TaskTypeUnset/TaskTypeImage/TaskTypeVideo",
                                "video_parameter": {
                                    "bit_rate": 0,
                                    "bit_rate_type": "[BRT_UNKNOWN]BRT_UNKNOWN/CBR/VBR",
                                    "frame_rate": 0,
                                    "height": 0,
                                    "i_frame_interval": 0,
                                    "stream_type": "[Main]Main/Second/Third/Fourth",
                                    "video_format": "[VF_UNKNOWN]VF_UNKNOWN/VF_MPEG4/VF_H264/VF_SVAC/VF_3GP/VF_H265",
                                    "width": 0
                                }
                            }
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "details": [
                                {
                                    "type_url": "",
                                    "value": ""
                                }
                            ],
                            "message": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_BatchGetTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("task_ids", task_ids)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_BatchDeleteTaskDeleteApi(self, task_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  批量删除任务 """
        """  path: [delete]/v1/batch-tasks API """
        """  params: 
                参数名称：task_ids　类型：array　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "results": [
                        {
                            "code": 0,
                            "details": [
                                {
                                    "type_url": "",
                                    "value": ""
                                }
                            ],
                            "message": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_BatchDeleteTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("task_ids", task_ids)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_BatchCreateTaskPostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True):
        """  批量创建任务 """
        """  path: [post]/v1/batch-tasks API """
        """  body: 
                {
                    "requests": [
                        {
                            "header": {
                                "trace": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            },
                            "task": {
                                "camera_info": {
                                    "camera_id": "",
                                    "device_id": "",
                                    "device_type": "",
                                    "internal_id": {
                                        "camera_idx": 0,
                                        "region_id": 0
                                    },
                                    "place_code": "",
                                    "place_name": "",
                                    "platform_id": "",
                                    "source_id": "",
                                    "tollgate_id": "",
                                    "tollgate_name": "",
                                    "zone_id": ""
                                },
                                "consumed_power": 0,
                                "dbs": [
                                    {
                                        "db_id": "",
                                        "db_name": "",
                                        "min_score": 0,
                                        "top_k": 0
                                    }
                                ],
                                "decimal_consumed_power": "",
                                "desc": "",
                                "external_id": "",
                                "extra_info": "",
                                "merge": false,
                                "merge_id": "",
                                "name": "",
                                "object_config": {
                                    "algo_config": {
                                        "app_name": "",
                                        "app_version": 0,
                                        "data": {
                                            "type_url": "",
                                            "value": ""
                                        }
                                    },
                                    "crowd_config": {
                                        "crowd_thresh": 0,
                                        "enable_density_map": false,
                                        "enable_strand_analyze": false,
                                        "enable_strand_map": false,
                                        "labeled_person": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "panoramic_mode": "[OutputOnAlarm]OutputOnAlarm/OutputOff/OutputForever",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "scene_area": 0,
                                        "strand_roi": [
                                            {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            }
                                        ],
                                        "strand_thresh": 0
                                    },
                                    "decoder_config": {
                                        "set_skip_frame_num": false,
                                        "skip_frame_num": 0
                                    },
                                    "face_config": {
                                        "target_select_config": {
                                            "max_track_time": 0,
                                            "quick_response_time": 0,
                                            "set_max_track_time": false,
                                            "set_quick_response_time": false,
                                            "set_time_interval": false,
                                            "time_interval": 0
                                        }
                                    },
                                    "faceped_config": {
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "target_select_config": {
                                            "additionalProp1": {
                                                "max_track_time": 0,
                                                "quick_response_time": 0,
                                                "set_max_track_time": false,
                                                "set_quick_response_time": false,
                                                "set_time_interval": false,
                                                "time_interval": 0
                                            },
                                            "additionalProp2": {
                                                "max_track_time": 0,
                                                "quick_response_time": 0,
                                                "set_max_track_time": false,
                                                "set_quick_response_time": false,
                                                "set_time_interval": false,
                                                "time_interval": 0
                                            },
                                            "additionalProp3": {
                                                "max_track_time": 0,
                                                "quick_response_time": 0,
                                                "set_max_track_time": false,
                                                "set_quick_response_time": false,
                                                "set_time_interval": false,
                                                "time_interval": 0
                                            }
                                        }
                                    },
                                    "lite_faceped_config": {
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "select_frame_policy": "[ENTER]ENTER/OPTIMAL/PERIODIC"
                                    },
                                    "pach_config": {
                                        "target_select_config": {
                                            "max_track_time": 0,
                                            "quick_response_time": 0,
                                            "set_max_track_time": false,
                                            "set_quick_response_time": false,
                                            "set_time_interval": false,
                                            "time_interval": 0
                                        }
                                    },
                                    "rules": [
                                        {
                                            "direction": {
                                                "x": 0,
                                                "y": 0
                                            },
                                            "duration": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "rule_id": "",
                                            "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                        }
                                    ],
                                    "scenario_rules": [
                                        {
                                            "detect_thresh": 0,
                                            "roi": [
                                                {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                }
                                            ],
                                            "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                        }
                                    ]
                                },
                                "object_types": [
                                    "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                                ],
                                "pu": 0,
                                "schedule_config": {
                                    "end_date": "",
                                    "exec_times": [
                                        {
                                            "end_time": "",
                                            "start_time": ""
                                        }
                                    ],
                                    "start_date": "",
                                    "weekday": {
                                        "additionalProp1": false,
                                        "additionalProp2": false,
                                        "additionalProp3": false
                                    }
                                },
                                "source_addr": "",
                                "source_information": {
                                    "parameter": {
                                        "cvr": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "dh_video_cloud": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "user": ""
                                        },
                                        "face_camera": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "gat1400": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "gat1400_ape": {
                                            "ape_id": "",
                                            "extra_info": "",
                                            "password": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "user": ""
                                        },
                                        "gat1400_face_camera": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "hls": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "nvr": {
                                            "downlink_host": "",
                                            "ipc": "",
                                            "password": "",
                                            "private": false,
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "user": ""
                                        },
                                        "onvif": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "rtmp": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "rtsp": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "sjk": {
                                            "ipc": ""
                                        },
                                        "symphony_nebula": {
                                            "device_id": "",
                                            "task_id": ""
                                        },
                                        "symphony_pass": {
                                            "device_id": ""
                                        }
                                    },
                                    "type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                },
                                "source_protocol": "",
                                "status": "[TaskStatusUnset]TaskStatusUnset/TaskPending/TaskScheduleFailed/TaskRuning/TaskFinish/TaskInternalErr/TaskStopFailed/TaskSubmitted",
                                "storage_policy": {
                                    "binary_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {
                                            "enable": false
                                        },
                                        "osg": {
                                            "enable": false
                                        }
                                    },
                                    "panoramic_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {
                                            "enable": false
                                        },
                                        "osg": {
                                            "enable": false
                                        }
                                    },
                                    "portrait_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {
                                            "enable": false
                                        },
                                        "osg": {
                                            "enable": false
                                        }
                                    }
                                },
                                "sub_device_id": "",
                                "task_id": "",
                                "type": "[TaskTypeUnset]TaskTypeUnset/TaskTypeImage/TaskTypeVideo",
                                "video_parameter": {
                                    "bit_rate": 0,
                                    "bit_rate_type": "[BRT_UNKNOWN]BRT_UNKNOWN/CBR/VBR",
                                    "frame_rate": 0,
                                    "height": 0,
                                    "i_frame_interval": 0,
                                    "stream_type": "[Main]Main/Second/Third/Fourth",
                                    "video_format": "[VF_UNKNOWN]VF_UNKNOWN/VF_MPEG4/VF_H264/VF_SVAC/VF_3GP/VF_H265",
                                    "width": 0
                                }
                            }
                        }
                    ]
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "responses": [
                        {
                            "header": {
                                "timestamp": "",
                                "trace": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            },
                            "merge_id": "",
                            "success": false,
                            "task_id": ""
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "details": [
                                {
                                    "type_url": "",
                                    "value": ""
                                }
                            ],
                            "message": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_BatchCreateTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_BatchUpdateTaskPutApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True):
        """  批量更新任务 """
        """  path: [put]/v1/batch-tasks API """
        """  body: 
                {
                    "requests": [
                        {
                            "header": {
                                "trace": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            },
                            "task": {
                                "camera_info": {
                                    "camera_id": "",
                                    "device_id": "",
                                    "device_type": "",
                                    "internal_id": {
                                        "camera_idx": 0,
                                        "region_id": 0
                                    },
                                    "place_code": "",
                                    "place_name": "",
                                    "platform_id": "",
                                    "source_id": "",
                                    "tollgate_id": "",
                                    "tollgate_name": "",
                                    "zone_id": ""
                                },
                                "consumed_power": 0,
                                "dbs": [
                                    {
                                        "db_id": "",
                                        "db_name": "",
                                        "min_score": 0,
                                        "top_k": 0
                                    }
                                ],
                                "decimal_consumed_power": "",
                                "desc": "",
                                "external_id": "",
                                "extra_info": "",
                                "merge": false,
                                "merge_id": "",
                                "name": "",
                                "object_config": {
                                    "algo_config": {
                                        "app_name": "",
                                        "app_version": 0,
                                        "data": {
                                            "type_url": "",
                                            "value": ""
                                        }
                                    },
                                    "crowd_config": {
                                        "crowd_thresh": 0,
                                        "enable_density_map": false,
                                        "enable_strand_analyze": false,
                                        "enable_strand_map": false,
                                        "labeled_person": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "panoramic_mode": "[OutputOnAlarm]OutputOnAlarm/OutputOff/OutputForever",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "scene_area": 0,
                                        "strand_roi": [
                                            {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            }
                                        ],
                                        "strand_thresh": 0
                                    },
                                    "decoder_config": {
                                        "set_skip_frame_num": false,
                                        "skip_frame_num": 0
                                    },
                                    "face_config": {
                                        "target_select_config": {
                                            "max_track_time": 0,
                                            "quick_response_time": 0,
                                            "set_max_track_time": false,
                                            "set_quick_response_time": false,
                                            "set_time_interval": false,
                                            "time_interval": 0
                                        }
                                    },
                                    "faceped_config": {
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "target_select_config": {
                                            "additionalProp1": {
                                                "max_track_time": 0,
                                                "quick_response_time": 0,
                                                "set_max_track_time": false,
                                                "set_quick_response_time": false,
                                                "set_time_interval": false,
                                                "time_interval": 0
                                            },
                                            "additionalProp2": {
                                                "max_track_time": 0,
                                                "quick_response_time": 0,
                                                "set_max_track_time": false,
                                                "set_quick_response_time": false,
                                                "set_time_interval": false,
                                                "time_interval": 0
                                            },
                                            "additionalProp3": {
                                                "max_track_time": 0,
                                                "quick_response_time": 0,
                                                "set_max_track_time": false,
                                                "set_quick_response_time": false,
                                                "set_time_interval": false,
                                                "time_interval": 0
                                            }
                                        }
                                    },
                                    "lite_faceped_config": {
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "select_frame_policy": "[ENTER]ENTER/OPTIMAL/PERIODIC"
                                    },
                                    "pach_config": {
                                        "target_select_config": {
                                            "max_track_time": 0,
                                            "quick_response_time": 0,
                                            "set_max_track_time": false,
                                            "set_quick_response_time": false,
                                            "set_time_interval": false,
                                            "time_interval": 0
                                        }
                                    },
                                    "rules": [
                                        {
                                            "direction": {
                                                "x": 0,
                                                "y": 0
                                            },
                                            "duration": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "rule_id": "",
                                            "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                        }
                                    ],
                                    "scenario_rules": [
                                        {
                                            "detect_thresh": 0,
                                            "roi": [
                                                {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                }
                                            ],
                                            "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                        }
                                    ]
                                },
                                "object_types": [
                                    "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                                ],
                                "pu": 0,
                                "schedule_config": {
                                    "end_date": "",
                                    "exec_times": [
                                        {
                                            "end_time": "",
                                            "start_time": ""
                                        }
                                    ],
                                    "start_date": "",
                                    "weekday": {
                                        "additionalProp1": false,
                                        "additionalProp2": false,
                                        "additionalProp3": false
                                    }
                                },
                                "source_addr": "",
                                "source_information": {
                                    "parameter": {
                                        "cvr": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "downlink_host": "",
                                            "downlink_id": "",
                                            "gb28181_local_uuid": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "raw_config": {
                                                "address": "",
                                                "block": "",
                                                "cert_num": "",
                                                "certifiable": 0,
                                                "civil_code": "",
                                                "device_id": "",
                                                "end_time": "",
                                                "err_code": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "info": [
                                                    {
                                                        "business_group_id": "",
                                                        "direction_type": 0,
                                                        "download_speed": "",
                                                        "position_type": 0,
                                                        "ptz_type": 0,
                                                        "resolution": "",
                                                        "room_type": 0,
                                                        "supply_light_type": 0,
                                                        "svc_space_support_mode": 0,
                                                        "svc_time_support_mode": 0,
                                                        "use_type": 0
                                                    }
                                                ],
                                                "ip_address": "",
                                                "manufacturer": "",
                                                "model": "",
                                                "name": "",
                                                "owner": "",
                                                "parent_id": "",
                                                "parental": 0,
                                                "password": "",
                                                "port": 0,
                                                "register_way": 0,
                                                "safety_way": 0,
                                                "secrecy": 0,
                                                "status": "[ON]ON/OFF"
                                            },
                                            "speed": 0,
                                            "start_time": "",
                                            "stop_time": "",
                                            "user": ""
                                        },
                                        "dh_video_cloud": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "user": ""
                                        },
                                        "face_camera": {
                                            "dir": "",
                                            "host": "",
                                            "ipc": "",
                                            "password": "",
                                            "port": 0,
                                            "user": ""
                                        },
                                        "gat1400": {
                                            "client_id": "",
                                            "extra_info": "",
                                            "host": "",
                                            "password": "",
                                            "platform_id": "",
                                            "port": 0,
                                            "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                            "server_id": "",
                                            "user": ""
                                        },
                                        "gat1400_ape": {
                                            "ape_id": "",
                                            "extra_info": "",
                                            "password": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "user": ""
                                        },
                                        "gat1400_face_camera": {
                                            "ape_id": "",
                                            "raw_config": {
                                                "ape_id": "",
                                                "cap_direction": 0,
                                                "geo_point": {
                                                    "latitude": 0,
                                                    "longitude": 0
                                                },
                                                "ip_addr": "",
                                                "ipv6_addr": "",
                                                "is_online": "",
                                                "model": "",
                                                "monitor_area_desc": "",
                                                "monitor_direction": "",
                                                "name": "",
                                                "org_code": "",
                                                "owner_aps_id": "",
                                                "password": "",
                                                "place": "",
                                                "place_code": "",
                                                "port": 0,
                                                "user_id": ""
                                            },
                                            "server_id": ""
                                        },
                                        "hls": {
                                            "command_type": "[Play]Play/Playback/Download",
                                            "url": ""
                                        },
                                        "nvr": {
                                            "downlink_host": "",
                                            "ipc": "",
                                            "password": "",
                                            "private": false,
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "ratio_type": "[SD]SD/HD",
                                            "user": ""
                                        },
                                        "onvif": {
                                            "channel": 0,
                                            "host": "",
                                            "password": "",
                                            "port": 0,
                                            "profile_token": "",
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "stream_type": "[Main]Main/Second/Third/Fourth",
                                            "user": ""
                                        },
                                        "rtmp": {
                                            "device_id": "",
                                            "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                            "rtmp_url": ""
                                        },
                                        "rtsp": {
                                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                            "url": ""
                                        },
                                        "sjk": {
                                            "ipc": ""
                                        },
                                        "symphony_nebula": {
                                            "device_id": "",
                                            "task_id": ""
                                        },
                                        "symphony_pass": {
                                            "device_id": ""
                                        }
                                    },
                                    "type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                                },
                                "source_protocol": "",
                                "status": "[TaskStatusUnset]TaskStatusUnset/TaskPending/TaskScheduleFailed/TaskRuning/TaskFinish/TaskInternalErr/TaskStopFailed/TaskSubmitted",
                                "storage_policy": {
                                    "binary_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {
                                            "enable": false
                                        },
                                        "osg": {
                                            "enable": false
                                        }
                                    },
                                    "panoramic_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {
                                            "enable": false
                                        },
                                        "osg": {
                                            "enable": false
                                        }
                                    },
                                    "portrait_storage_config": {
                                        "gat1400": {
                                            "enable": false,
                                            "platform_id": ""
                                        },
                                        "kafka": {
                                            "enable": false
                                        },
                                        "osg": {
                                            "enable": false
                                        }
                                    }
                                },
                                "sub_device_id": "",
                                "task_id": "",
                                "type": "[TaskTypeUnset]TaskTypeUnset/TaskTypeImage/TaskTypeVideo",
                                "video_parameter": {
                                    "bit_rate": 0,
                                    "bit_rate_type": "[BRT_UNKNOWN]BRT_UNKNOWN/CBR/VBR",
                                    "frame_rate": 0,
                                    "height": 0,
                                    "i_frame_interval": 0,
                                    "stream_type": "[Main]Main/Second/Third/Fourth",
                                    "video_format": "[VF_UNKNOWN]VF_UNKNOWN/VF_MPEG4/VF_H264/VF_SVAC/VF_3GP/VF_H265",
                                    "width": 0
                                }
                            },
                            "task_id": ""
                        }
                    ]
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "responses": [
                        {
                            "header": {
                                "timestamp": "",
                                "trace": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            },
                            "merge_id": ""
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "details": [
                                {
                                    "type_url": "",
                                    "value": ""
                                }
                            ],
                            "message": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_BatchUpdateTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_HelloGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  Hello . """
        """  path: [get]/v1/hello API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_Hello")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_GetPowerInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  查询算力信息 """
        """  path: [get]/v1/power API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "info": {
                        "remained": {
                            "additionalProp1": {
                                "algo": 0,
                                "face": 0,
                                "ips": 0
                            },
                            "additionalProp2": {
                                "algo": 0,
                                "face": 0,
                                "ips": 0
                            },
                            "additionalProp3": {
                                "algo": 0,
                                "face": 0,
                                "ips": 0
                            }
                        },
                        "total": 0
                    },
                    "strategy": {
                        "arch": "",
                        "auto_start_ips": false,
                        "create_worker": "",
                        "face_quota": {
                            "additionalProp1": 0,
                            "additionalProp2": 0,
                            "additionalProp3": 0
                        },
                        "gpu_utils_rate_limit": 0,
                        "ips_quota": {
                            "additionalProp1": 0,
                            "additionalProp2": 0,
                            "additionalProp3": 0
                        },
                        "pre_start_ips": false,
                        "pu_type": "",
                        "select_worker": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_GetPowerInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_ListTaskGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  获取任务列表 """
        """  path: [get]/v1/tasks API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "tasks": [
                        {
                            "camera_info": {
                                "camera_id": "",
                                "device_id": "",
                                "device_type": "",
                                "internal_id": {
                                    "camera_idx": 0,
                                    "region_id": 0
                                },
                                "place_code": "",
                                "place_name": "",
                                "platform_id": "",
                                "source_id": "",
                                "tollgate_id": "",
                                "tollgate_name": "",
                                "zone_id": ""
                            },
                            "consumed_power": 0,
                            "dbs": [
                                {
                                    "db_id": "",
                                    "db_name": "",
                                    "min_score": 0,
                                    "top_k": 0
                                }
                            ],
                            "decimal_consumed_power": "",
                            "desc": "",
                            "external_id": "",
                            "extra_info": "",
                            "merge": false,
                            "merge_id": "",
                            "name": "",
                            "object_config": {
                                "algo_config": {
                                    "app_name": "",
                                    "app_version": 0,
                                    "data": {
                                        "type_url": "",
                                        "value": ""
                                    }
                                },
                                "crowd_config": {
                                    "crowd_thresh": 0,
                                    "enable_density_map": false,
                                    "enable_strand_analyze": false,
                                    "enable_strand_map": false,
                                    "labeled_person": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "panoramic_mode": "[OutputOnAlarm]OutputOnAlarm/OutputOff/OutputForever",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "scene_area": 0,
                                    "strand_roi": [
                                        {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        }
                                    ],
                                    "strand_thresh": 0
                                },
                                "decoder_config": {
                                    "set_skip_frame_num": false,
                                    "skip_frame_num": 0
                                },
                                "face_config": {
                                    "target_select_config": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    }
                                },
                                "faceped_config": {
                                    "roi": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "target_select_config": {
                                        "additionalProp1": {
                                            "max_track_time": 0,
                                            "quick_response_time": 0,
                                            "set_max_track_time": false,
                                            "set_quick_response_time": false,
                                            "set_time_interval": false,
                                            "time_interval": 0
                                        },
                                        "additionalProp2": {
                                            "max_track_time": 0,
                                            "quick_response_time": 0,
                                            "set_max_track_time": false,
                                            "set_quick_response_time": false,
                                            "set_time_interval": false,
                                            "time_interval": 0
                                        },
                                        "additionalProp3": {
                                            "max_track_time": 0,
                                            "quick_response_time": 0,
                                            "set_max_track_time": false,
                                            "set_quick_response_time": false,
                                            "set_time_interval": false,
                                            "time_interval": 0
                                        }
                                    }
                                },
                                "lite_faceped_config": {
                                    "roi": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "select_frame_policy": "[ENTER]ENTER/OPTIMAL/PERIODIC"
                                },
                                "pach_config": {
                                    "target_select_config": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    }
                                },
                                "rules": [
                                    {
                                        "direction": {
                                            "x": 0,
                                            "y": 0
                                        },
                                        "duration": "",
                                        "roi": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "rule_id": "",
                                        "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                    }
                                ],
                                "scenario_rules": [
                                    {
                                        "detect_thresh": 0,
                                        "roi": [
                                            {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            }
                                        ],
                                        "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                    }
                                ]
                            },
                            "object_types": [
                                "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                            ],
                            "pu": 0,
                            "schedule_config": {
                                "end_date": "",
                                "exec_times": [
                                    {
                                        "end_time": "",
                                        "start_time": ""
                                    }
                                ],
                                "start_date": "",
                                "weekday": {
                                    "additionalProp1": false,
                                    "additionalProp2": false,
                                    "additionalProp3": false
                                }
                            },
                            "source_addr": "",
                            "source_information": {
                                "parameter": {
                                    "cvr": {
                                        "command_type": "[Play]Play/Playback/Download",
                                        "downlink_host": "",
                                        "downlink_id": "",
                                        "gb28181_local_uuid": "",
                                        "ipc": "",
                                        "password": "",
                                        "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                        "ratio_type": "[SD]SD/HD",
                                        "raw_config": {
                                            "address": "",
                                            "block": "",
                                            "cert_num": "",
                                            "certifiable": 0,
                                            "civil_code": "",
                                            "device_id": "",
                                            "end_time": "",
                                            "err_code": 0,
                                            "geo_point": {
                                                "latitude": 0,
                                                "longitude": 0
                                            },
                                            "info": [
                                                {
                                                    "business_group_id": "",
                                                    "direction_type": 0,
                                                    "download_speed": "",
                                                    "position_type": 0,
                                                    "ptz_type": 0,
                                                    "resolution": "",
                                                    "room_type": 0,
                                                    "supply_light_type": 0,
                                                    "svc_space_support_mode": 0,
                                                    "svc_time_support_mode": 0,
                                                    "use_type": 0
                                                }
                                            ],
                                            "ip_address": "",
                                            "manufacturer": "",
                                            "model": "",
                                            "name": "",
                                            "owner": "",
                                            "parent_id": "",
                                            "parental": 0,
                                            "password": "",
                                            "port": 0,
                                            "register_way": 0,
                                            "safety_way": 0,
                                            "secrecy": 0,
                                            "status": "[ON]ON/OFF"
                                        },
                                        "speed": 0,
                                        "start_time": "",
                                        "stop_time": "",
                                        "user": ""
                                    },
                                    "dh_video_cloud": {
                                        "command_type": "[Play]Play/Playback/Download",
                                        "host": "",
                                        "ipc": "",
                                        "password": "",
                                        "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                        "user": ""
                                    },
                                    "face_camera": {
                                        "dir": "",
                                        "host": "",
                                        "ipc": "",
                                        "password": "",
                                        "port": 0,
                                        "user": ""
                                    },
                                    "gat1400": {
                                        "client_id": "",
                                        "extra_info": "",
                                        "host": "",
                                        "password": "",
                                        "platform_id": "",
                                        "port": 0,
                                        "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                        "server_id": "",
                                        "user": ""
                                    },
                                    "gat1400_ape": {
                                        "ape_id": "",
                                        "extra_info": "",
                                        "password": "",
                                        "raw_config": {
                                            "ape_id": "",
                                            "cap_direction": 0,
                                            "geo_point": {
                                                "latitude": 0,
                                                "longitude": 0
                                            },
                                            "ip_addr": "",
                                            "ipv6_addr": "",
                                            "is_online": "",
                                            "model": "",
                                            "monitor_area_desc": "",
                                            "monitor_direction": "",
                                            "name": "",
                                            "org_code": "",
                                            "owner_aps_id": "",
                                            "password": "",
                                            "place": "",
                                            "place_code": "",
                                            "port": 0,
                                            "user_id": ""
                                        },
                                        "user": ""
                                    },
                                    "gat1400_face_camera": {
                                        "ape_id": "",
                                        "raw_config": {
                                            "ape_id": "",
                                            "cap_direction": 0,
                                            "geo_point": {
                                                "latitude": 0,
                                                "longitude": 0
                                            },
                                            "ip_addr": "",
                                            "ipv6_addr": "",
                                            "is_online": "",
                                            "model": "",
                                            "monitor_area_desc": "",
                                            "monitor_direction": "",
                                            "name": "",
                                            "org_code": "",
                                            "owner_aps_id": "",
                                            "password": "",
                                            "place": "",
                                            "place_code": "",
                                            "port": 0,
                                            "user_id": ""
                                        },
                                        "server_id": ""
                                    },
                                    "hls": {
                                        "command_type": "[Play]Play/Playback/Download",
                                        "url": ""
                                    },
                                    "nvr": {
                                        "downlink_host": "",
                                        "ipc": "",
                                        "password": "",
                                        "private": false,
                                        "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                        "ratio_type": "[SD]SD/HD",
                                        "user": ""
                                    },
                                    "onvif": {
                                        "channel": 0,
                                        "host": "",
                                        "password": "",
                                        "port": 0,
                                        "profile_token": "",
                                        "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                        "stream_type": "[Main]Main/Second/Third/Fourth",
                                        "user": ""
                                    },
                                    "rtmp": {
                                        "device_id": "",
                                        "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                        "rtmp_url": ""
                                    },
                                    "rtsp": {
                                        "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                        "url": ""
                                    },
                                    "sjk": {
                                        "ipc": ""
                                    },
                                    "symphony_nebula": {
                                        "device_id": "",
                                        "task_id": ""
                                    },
                                    "symphony_pass": {
                                        "device_id": ""
                                    }
                                },
                                "type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                            },
                            "source_protocol": "",
                            "status": "[TaskStatusUnset]TaskStatusUnset/TaskPending/TaskScheduleFailed/TaskRuning/TaskFinish/TaskInternalErr/TaskStopFailed/TaskSubmitted",
                            "storage_policy": {
                                "binary_storage_config": {
                                    "gat1400": {
                                        "enable": false,
                                        "platform_id": ""
                                    },
                                    "kafka": {
                                        "enable": false
                                    },
                                    "osg": {
                                        "enable": false
                                    }
                                },
                                "panoramic_storage_config": {
                                    "gat1400": {
                                        "enable": false,
                                        "platform_id": ""
                                    },
                                    "kafka": {
                                        "enable": false
                                    },
                                    "osg": {
                                        "enable": false
                                    }
                                },
                                "portrait_storage_config": {
                                    "gat1400": {
                                        "enable": false,
                                        "platform_id": ""
                                    },
                                    "kafka": {
                                        "enable": false
                                    },
                                    "osg": {
                                        "enable": false
                                    }
                                }
                            },
                            "sub_device_id": "",
                            "task_id": "",
                            "type": "[TaskTypeUnset]TaskTypeUnset/TaskTypeImage/TaskTypeVideo",
                            "video_parameter": {
                                "bit_rate": 0,
                                "bit_rate_type": "[BRT_UNKNOWN]BRT_UNKNOWN/CBR/VBR",
                                "frame_rate": 0,
                                "height": 0,
                                "i_frame_interval": 0,
                                "stream_type": "[Main]Main/Second/Third/Fourth",
                                "video_format": "[VF_UNKNOWN]VF_UNKNOWN/VF_MPEG4/VF_H264/VF_SVAC/VF_3GP/VF_H265",
                                "width": 0
                            }
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_ListTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_CreateTaskPostApi(self, task=None, loginToken=None, sendRequest=True, print_log=True):
        """  创建任务 """
        """  path: [post]/v1/tasks API """
        """  body: 
                {
                    "task": {
                        "camera_info": {
                            "camera_id": "",
                            "device_id": "",
                            "device_type": "",
                            "internal_id": {
                                "camera_idx": 0,
                                "region_id": 0
                            },
                            "place_code": "",
                            "place_name": "",
                            "platform_id": "",
                            "source_id": "",
                            "tollgate_id": "",
                            "tollgate_name": "",
                            "zone_id": ""
                        },
                        "consumed_power": 0,
                        "dbs": [
                            {
                                "db_id": "",
                                "db_name": "",
                                "min_score": 0,
                                "top_k": 0
                            }
                        ],
                        "decimal_consumed_power": "",
                        "desc": "",
                        "external_id": "",
                        "extra_info": "",
                        "merge": false,
                        "merge_id": "",
                        "name": "",
                        "object_config": {
                            "algo_config": {
                                "app_name": "",
                                "app_version": 0,
                                "data": {
                                    "type_url": "",
                                    "value": ""
                                }
                            },
                            "crowd_config": {
                                "crowd_thresh": 0,
                                "enable_density_map": false,
                                "enable_strand_analyze": false,
                                "enable_strand_map": false,
                                "labeled_person": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "panoramic_mode": "[OutputOnAlarm]OutputOnAlarm/OutputOff/OutputForever",
                                "roi": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "scene_area": 0,
                                "strand_roi": [
                                    {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    }
                                ],
                                "strand_thresh": 0
                            },
                            "decoder_config": {
                                "set_skip_frame_num": false,
                                "skip_frame_num": 0
                            },
                            "face_config": {
                                "target_select_config": {
                                    "max_track_time": 0,
                                    "quick_response_time": 0,
                                    "set_max_track_time": false,
                                    "set_quick_response_time": false,
                                    "set_time_interval": false,
                                    "time_interval": 0
                                }
                            },
                            "faceped_config": {
                                "roi": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "target_select_config": {
                                    "additionalProp1": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    },
                                    "additionalProp2": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    },
                                    "additionalProp3": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    }
                                }
                            },
                            "lite_faceped_config": {
                                "roi": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "select_frame_policy": "[ENTER]ENTER/OPTIMAL/PERIODIC"
                            },
                            "pach_config": {
                                "target_select_config": {
                                    "max_track_time": 0,
                                    "quick_response_time": 0,
                                    "set_max_track_time": false,
                                    "set_quick_response_time": false,
                                    "set_time_interval": false,
                                    "time_interval": 0
                                }
                            },
                            "rules": [
                                {
                                    "direction": {
                                        "x": 0,
                                        "y": 0
                                    },
                                    "duration": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rule_id": "",
                                    "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                }
                            ],
                            "scenario_rules": [
                                {
                                    "detect_thresh": 0,
                                    "roi": [
                                        {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        }
                                    ],
                                    "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                }
                            ]
                        },
                        "object_types": [
                            "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                        ],
                        "pu": 0,
                        "schedule_config": {
                            "end_date": "",
                            "exec_times": [
                                {
                                    "end_time": "",
                                    "start_time": ""
                                }
                            ],
                            "start_date": "",
                            "weekday": {
                                "additionalProp1": false,
                                "additionalProp2": false,
                                "additionalProp3": false
                            }
                        },
                        "source_addr": "",
                        "source_information": {
                            "parameter": {
                                "cvr": {
                                    "command_type": "[Play]Play/Playback/Download",
                                    "downlink_host": "",
                                    "downlink_id": "",
                                    "gb28181_local_uuid": "",
                                    "ipc": "",
                                    "password": "",
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "ratio_type": "[SD]SD/HD",
                                    "raw_config": {
                                        "address": "",
                                        "block": "",
                                        "cert_num": "",
                                        "certifiable": 0,
                                        "civil_code": "",
                                        "device_id": "",
                                        "end_time": "",
                                        "err_code": 0,
                                        "geo_point": {
                                            "latitude": 0,
                                            "longitude": 0
                                        },
                                        "info": [
                                            {
                                                "business_group_id": "",
                                                "direction_type": 0,
                                                "download_speed": "",
                                                "position_type": 0,
                                                "ptz_type": 0,
                                                "resolution": "",
                                                "room_type": 0,
                                                "supply_light_type": 0,
                                                "svc_space_support_mode": 0,
                                                "svc_time_support_mode": 0,
                                                "use_type": 0
                                            }
                                        ],
                                        "ip_address": "",
                                        "manufacturer": "",
                                        "model": "",
                                        "name": "",
                                        "owner": "",
                                        "parent_id": "",
                                        "parental": 0,
                                        "password": "",
                                        "port": 0,
                                        "register_way": 0,
                                        "safety_way": 0,
                                        "secrecy": 0,
                                        "status": "[ON]ON/OFF"
                                    },
                                    "speed": 0,
                                    "start_time": "",
                                    "stop_time": "",
                                    "user": ""
                                },
                                "dh_video_cloud": {
                                    "command_type": "[Play]Play/Playback/Download",
                                    "host": "",
                                    "ipc": "",
                                    "password": "",
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "user": ""
                                },
                                "face_camera": {
                                    "dir": "",
                                    "host": "",
                                    "ipc": "",
                                    "password": "",
                                    "port": 0,
                                    "user": ""
                                },
                                "gat1400": {
                                    "client_id": "",
                                    "extra_info": "",
                                    "host": "",
                                    "password": "",
                                    "platform_id": "",
                                    "port": 0,
                                    "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                    "server_id": "",
                                    "user": ""
                                },
                                "gat1400_ape": {
                                    "ape_id": "",
                                    "extra_info": "",
                                    "password": "",
                                    "raw_config": {
                                        "ape_id": "",
                                        "cap_direction": 0,
                                        "geo_point": {
                                            "latitude": 0,
                                            "longitude": 0
                                        },
                                        "ip_addr": "",
                                        "ipv6_addr": "",
                                        "is_online": "",
                                        "model": "",
                                        "monitor_area_desc": "",
                                        "monitor_direction": "",
                                        "name": "",
                                        "org_code": "",
                                        "owner_aps_id": "",
                                        "password": "",
                                        "place": "",
                                        "place_code": "",
                                        "port": 0,
                                        "user_id": ""
                                    },
                                    "user": ""
                                },
                                "gat1400_face_camera": {
                                    "ape_id": "",
                                    "raw_config": {
                                        "ape_id": "",
                                        "cap_direction": 0,
                                        "geo_point": {
                                            "latitude": 0,
                                            "longitude": 0
                                        },
                                        "ip_addr": "",
                                        "ipv6_addr": "",
                                        "is_online": "",
                                        "model": "",
                                        "monitor_area_desc": "",
                                        "monitor_direction": "",
                                        "name": "",
                                        "org_code": "",
                                        "owner_aps_id": "",
                                        "password": "",
                                        "place": "",
                                        "place_code": "",
                                        "port": 0,
                                        "user_id": ""
                                    },
                                    "server_id": ""
                                },
                                "hls": {
                                    "command_type": "[Play]Play/Playback/Download",
                                    "url": ""
                                },
                                "nvr": {
                                    "downlink_host": "",
                                    "ipc": "",
                                    "password": "",
                                    "private": false,
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "ratio_type": "[SD]SD/HD",
                                    "user": ""
                                },
                                "onvif": {
                                    "channel": 0,
                                    "host": "",
                                    "password": "",
                                    "port": 0,
                                    "profile_token": "",
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "stream_type": "[Main]Main/Second/Third/Fourth",
                                    "user": ""
                                },
                                "rtmp": {
                                    "device_id": "",
                                    "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                    "rtmp_url": ""
                                },
                                "rtsp": {
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "url": ""
                                },
                                "sjk": {
                                    "ipc": ""
                                },
                                "symphony_nebula": {
                                    "device_id": "",
                                    "task_id": ""
                                },
                                "symphony_pass": {
                                    "device_id": ""
                                }
                            },
                            "type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                        },
                        "source_protocol": "",
                        "status": "[TaskStatusUnset]TaskStatusUnset/TaskPending/TaskScheduleFailed/TaskRuning/TaskFinish/TaskInternalErr/TaskStopFailed/TaskSubmitted",
                        "storage_policy": {
                            "binary_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {
                                    "enable": false
                                },
                                "osg": {
                                    "enable": false
                                }
                            },
                            "panoramic_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {
                                    "enable": false
                                },
                                "osg": {
                                    "enable": false
                                }
                            },
                            "portrait_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {
                                    "enable": false
                                },
                                "osg": {
                                    "enable": false
                                }
                            }
                        },
                        "sub_device_id": "",
                        "task_id": "",
                        "type": "[TaskTypeUnset]TaskTypeUnset/TaskTypeImage/TaskTypeVideo",
                        "video_parameter": {
                            "bit_rate": 0,
                            "bit_rate_type": "[BRT_UNKNOWN]BRT_UNKNOWN/CBR/VBR",
                            "frame_rate": 0,
                            "height": 0,
                            "i_frame_interval": 0,
                            "stream_type": "[Main]Main/Second/Third/Fourth",
                            "video_format": "[VF_UNKNOWN]VF_UNKNOWN/VF_MPEG4/VF_H264/VF_SVAC/VF_3GP/VF_H265",
                            "width": 0
                        }
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "merge_id": "",
                    "success": false,
                    "task_id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_CreateTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("task", task)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_GetTaskGetApi(self, task_id, loginToken=None, sendRequest=True, print_log=True):
        """  根据task_id获取任务 """
        """  path: [get]/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "task": {
                        "camera_info": {
                            "camera_id": "",
                            "device_id": "",
                            "device_type": "",
                            "internal_id": {
                                "camera_idx": 0,
                                "region_id": 0
                            },
                            "place_code": "",
                            "place_name": "",
                            "platform_id": "",
                            "source_id": "",
                            "tollgate_id": "",
                            "tollgate_name": "",
                            "zone_id": ""
                        },
                        "consumed_power": 0,
                        "dbs": [
                            {
                                "db_id": "",
                                "db_name": "",
                                "min_score": 0,
                                "top_k": 0
                            }
                        ],
                        "decimal_consumed_power": "",
                        "desc": "",
                        "external_id": "",
                        "extra_info": "",
                        "merge": false,
                        "merge_id": "",
                        "name": "",
                        "object_config": {
                            "algo_config": {
                                "app_name": "",
                                "app_version": 0,
                                "data": {
                                    "type_url": "",
                                    "value": ""
                                }
                            },
                            "crowd_config": {
                                "crowd_thresh": 0,
                                "enable_density_map": false,
                                "enable_strand_analyze": false,
                                "enable_strand_map": false,
                                "labeled_person": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "panoramic_mode": "[OutputOnAlarm]OutputOnAlarm/OutputOff/OutputForever",
                                "roi": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "scene_area": 0,
                                "strand_roi": [
                                    {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    }
                                ],
                                "strand_thresh": 0
                            },
                            "decoder_config": {
                                "set_skip_frame_num": false,
                                "skip_frame_num": 0
                            },
                            "face_config": {
                                "target_select_config": {
                                    "max_track_time": 0,
                                    "quick_response_time": 0,
                                    "set_max_track_time": false,
                                    "set_quick_response_time": false,
                                    "set_time_interval": false,
                                    "time_interval": 0
                                }
                            },
                            "faceped_config": {
                                "roi": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "target_select_config": {
                                    "additionalProp1": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    },
                                    "additionalProp2": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    },
                                    "additionalProp3": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    }
                                }
                            },
                            "lite_faceped_config": {
                                "roi": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "select_frame_policy": "[ENTER]ENTER/OPTIMAL/PERIODIC"
                            },
                            "pach_config": {
                                "target_select_config": {
                                    "max_track_time": 0,
                                    "quick_response_time": 0,
                                    "set_max_track_time": false,
                                    "set_quick_response_time": false,
                                    "set_time_interval": false,
                                    "time_interval": 0
                                }
                            },
                            "rules": [
                                {
                                    "direction": {
                                        "x": 0,
                                        "y": 0
                                    },
                                    "duration": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rule_id": "",
                                    "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                }
                            ],
                            "scenario_rules": [
                                {
                                    "detect_thresh": 0,
                                    "roi": [
                                        {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        }
                                    ],
                                    "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                }
                            ]
                        },
                        "object_types": [
                            "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                        ],
                        "pu": 0,
                        "schedule_config": {
                            "end_date": "",
                            "exec_times": [
                                {
                                    "end_time": "",
                                    "start_time": ""
                                }
                            ],
                            "start_date": "",
                            "weekday": {
                                "additionalProp1": false,
                                "additionalProp2": false,
                                "additionalProp3": false
                            }
                        },
                        "source_addr": "",
                        "source_information": {
                            "parameter": {
                                "cvr": {
                                    "command_type": "[Play]Play/Playback/Download",
                                    "downlink_host": "",
                                    "downlink_id": "",
                                    "gb28181_local_uuid": "",
                                    "ipc": "",
                                    "password": "",
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "ratio_type": "[SD]SD/HD",
                                    "raw_config": {
                                        "address": "",
                                        "block": "",
                                        "cert_num": "",
                                        "certifiable": 0,
                                        "civil_code": "",
                                        "device_id": "",
                                        "end_time": "",
                                        "err_code": 0,
                                        "geo_point": {
                                            "latitude": 0,
                                            "longitude": 0
                                        },
                                        "info": [
                                            {
                                                "business_group_id": "",
                                                "direction_type": 0,
                                                "download_speed": "",
                                                "position_type": 0,
                                                "ptz_type": 0,
                                                "resolution": "",
                                                "room_type": 0,
                                                "supply_light_type": 0,
                                                "svc_space_support_mode": 0,
                                                "svc_time_support_mode": 0,
                                                "use_type": 0
                                            }
                                        ],
                                        "ip_address": "",
                                        "manufacturer": "",
                                        "model": "",
                                        "name": "",
                                        "owner": "",
                                        "parent_id": "",
                                        "parental": 0,
                                        "password": "",
                                        "port": 0,
                                        "register_way": 0,
                                        "safety_way": 0,
                                        "secrecy": 0,
                                        "status": "[ON]ON/OFF"
                                    },
                                    "speed": 0,
                                    "start_time": "",
                                    "stop_time": "",
                                    "user": ""
                                },
                                "dh_video_cloud": {
                                    "command_type": "[Play]Play/Playback/Download",
                                    "host": "",
                                    "ipc": "",
                                    "password": "",
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "user": ""
                                },
                                "face_camera": {
                                    "dir": "",
                                    "host": "",
                                    "ipc": "",
                                    "password": "",
                                    "port": 0,
                                    "user": ""
                                },
                                "gat1400": {
                                    "client_id": "",
                                    "extra_info": "",
                                    "host": "",
                                    "password": "",
                                    "platform_id": "",
                                    "port": 0,
                                    "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                    "server_id": "",
                                    "user": ""
                                },
                                "gat1400_ape": {
                                    "ape_id": "",
                                    "extra_info": "",
                                    "password": "",
                                    "raw_config": {
                                        "ape_id": "",
                                        "cap_direction": 0,
                                        "geo_point": {
                                            "latitude": 0,
                                            "longitude": 0
                                        },
                                        "ip_addr": "",
                                        "ipv6_addr": "",
                                        "is_online": "",
                                        "model": "",
                                        "monitor_area_desc": "",
                                        "monitor_direction": "",
                                        "name": "",
                                        "org_code": "",
                                        "owner_aps_id": "",
                                        "password": "",
                                        "place": "",
                                        "place_code": "",
                                        "port": 0,
                                        "user_id": ""
                                    },
                                    "user": ""
                                },
                                "gat1400_face_camera": {
                                    "ape_id": "",
                                    "raw_config": {
                                        "ape_id": "",
                                        "cap_direction": 0,
                                        "geo_point": {
                                            "latitude": 0,
                                            "longitude": 0
                                        },
                                        "ip_addr": "",
                                        "ipv6_addr": "",
                                        "is_online": "",
                                        "model": "",
                                        "monitor_area_desc": "",
                                        "monitor_direction": "",
                                        "name": "",
                                        "org_code": "",
                                        "owner_aps_id": "",
                                        "password": "",
                                        "place": "",
                                        "place_code": "",
                                        "port": 0,
                                        "user_id": ""
                                    },
                                    "server_id": ""
                                },
                                "hls": {
                                    "command_type": "[Play]Play/Playback/Download",
                                    "url": ""
                                },
                                "nvr": {
                                    "downlink_host": "",
                                    "ipc": "",
                                    "password": "",
                                    "private": false,
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "ratio_type": "[SD]SD/HD",
                                    "user": ""
                                },
                                "onvif": {
                                    "channel": 0,
                                    "host": "",
                                    "password": "",
                                    "port": 0,
                                    "profile_token": "",
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "stream_type": "[Main]Main/Second/Third/Fourth",
                                    "user": ""
                                },
                                "rtmp": {
                                    "device_id": "",
                                    "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                    "rtmp_url": ""
                                },
                                "rtsp": {
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "url": ""
                                },
                                "sjk": {
                                    "ipc": ""
                                },
                                "symphony_nebula": {
                                    "device_id": "",
                                    "task_id": ""
                                },
                                "symphony_pass": {
                                    "device_id": ""
                                }
                            },
                            "type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                        },
                        "source_protocol": "",
                        "status": "[TaskStatusUnset]TaskStatusUnset/TaskPending/TaskScheduleFailed/TaskRuning/TaskFinish/TaskInternalErr/TaskStopFailed/TaskSubmitted",
                        "storage_policy": {
                            "binary_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {
                                    "enable": false
                                },
                                "osg": {
                                    "enable": false
                                }
                            },
                            "panoramic_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {
                                    "enable": false
                                },
                                "osg": {
                                    "enable": false
                                }
                            },
                            "portrait_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {
                                    "enable": false
                                },
                                "osg": {
                                    "enable": false
                                }
                            }
                        },
                        "sub_device_id": "",
                        "task_id": "",
                        "type": "[TaskTypeUnset]TaskTypeUnset/TaskTypeImage/TaskTypeVideo",
                        "video_parameter": {
                            "bit_rate": 0,
                            "bit_rate_type": "[BRT_UNKNOWN]BRT_UNKNOWN/CBR/VBR",
                            "frame_rate": 0,
                            "height": 0,
                            "i_frame_interval": 0,
                            "stream_type": "[Main]Main/Second/Third/Fourth",
                            "video_format": "[VF_UNKNOWN]VF_UNKNOWN/VF_MPEG4/VF_H264/VF_SVAC/VF_3GP/VF_H265",
                            "width": 0
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_GetTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_DeleteTaskDeleteApi(self, task_id, loginToken=None, sendRequest=True, print_log=True):
        """  根据task_id删除任务 """
        """  path: [delete]/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_DeleteTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_UpdateTaskPutApi(self, task_id, task=None, loginToken=None, sendRequest=True, print_log=True):
        """  更新任务 """
        """  path: [put]/v1/tasks/{task_id} API """
        """  body: 
                {
                    "task": {
                        "camera_info": {
                            "camera_id": "",
                            "device_id": "",
                            "device_type": "",
                            "internal_id": {
                                "camera_idx": 0,
                                "region_id": 0
                            },
                            "place_code": "",
                            "place_name": "",
                            "platform_id": "",
                            "source_id": "",
                            "tollgate_id": "",
                            "tollgate_name": "",
                            "zone_id": ""
                        },
                        "consumed_power": 0,
                        "dbs": [
                            {
                                "db_id": "",
                                "db_name": "",
                                "min_score": 0,
                                "top_k": 0
                            }
                        ],
                        "decimal_consumed_power": "",
                        "desc": "",
                        "external_id": "",
                        "extra_info": "",
                        "merge": false,
                        "merge_id": "",
                        "name": "",
                        "object_config": {
                            "algo_config": {
                                "app_name": "",
                                "app_version": 0,
                                "data": {
                                    "type_url": "",
                                    "value": ""
                                }
                            },
                            "crowd_config": {
                                "crowd_thresh": 0,
                                "enable_density_map": false,
                                "enable_strand_analyze": false,
                                "enable_strand_map": false,
                                "labeled_person": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "panoramic_mode": "[OutputOnAlarm]OutputOnAlarm/OutputOff/OutputForever",
                                "roi": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "scene_area": 0,
                                "strand_roi": [
                                    {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    }
                                ],
                                "strand_thresh": 0
                            },
                            "decoder_config": {
                                "set_skip_frame_num": false,
                                "skip_frame_num": 0
                            },
                            "face_config": {
                                "target_select_config": {
                                    "max_track_time": 0,
                                    "quick_response_time": 0,
                                    "set_max_track_time": false,
                                    "set_quick_response_time": false,
                                    "set_time_interval": false,
                                    "time_interval": 0
                                }
                            },
                            "faceped_config": {
                                "roi": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "target_select_config": {
                                    "additionalProp1": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    },
                                    "additionalProp2": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    },
                                    "additionalProp3": {
                                        "max_track_time": 0,
                                        "quick_response_time": 0,
                                        "set_max_track_time": false,
                                        "set_quick_response_time": false,
                                        "set_time_interval": false,
                                        "time_interval": 0
                                    }
                                }
                            },
                            "lite_faceped_config": {
                                "roi": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "select_frame_policy": "[ENTER]ENTER/OPTIMAL/PERIODIC"
                            },
                            "pach_config": {
                                "target_select_config": {
                                    "max_track_time": 0,
                                    "quick_response_time": 0,
                                    "set_max_track_time": false,
                                    "set_quick_response_time": false,
                                    "set_time_interval": false,
                                    "time_interval": 0
                                }
                            },
                            "rules": [
                                {
                                    "direction": {
                                        "x": 0,
                                        "y": 0
                                    },
                                    "duration": "",
                                    "roi": {
                                        "vertices": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rule_id": "",
                                    "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                }
                            ],
                            "scenario_rules": [
                                {
                                    "detect_thresh": 0,
                                    "roi": [
                                        {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        }
                                    ],
                                    "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                }
                            ]
                        },
                        "object_types": [
                            "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                        ],
                        "pu": 0,
                        "schedule_config": {
                            "end_date": "",
                            "exec_times": [
                                {
                                    "end_time": "",
                                    "start_time": ""
                                }
                            ],
                            "start_date": "",
                            "weekday": {
                                "additionalProp1": false,
                                "additionalProp2": false,
                                "additionalProp3": false
                            }
                        },
                        "source_addr": "",
                        "source_information": {
                            "parameter": {
                                "cvr": {
                                    "command_type": "[Play]Play/Playback/Download",
                                    "downlink_host": "",
                                    "downlink_id": "",
                                    "gb28181_local_uuid": "",
                                    "ipc": "",
                                    "password": "",
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "ratio_type": "[SD]SD/HD",
                                    "raw_config": {
                                        "address": "",
                                        "block": "",
                                        "cert_num": "",
                                        "certifiable": 0,
                                        "civil_code": "",
                                        "device_id": "",
                                        "end_time": "",
                                        "err_code": 0,
                                        "geo_point": {
                                            "latitude": 0,
                                            "longitude": 0
                                        },
                                        "info": [
                                            {
                                                "business_group_id": "",
                                                "direction_type": 0,
                                                "download_speed": "",
                                                "position_type": 0,
                                                "ptz_type": 0,
                                                "resolution": "",
                                                "room_type": 0,
                                                "supply_light_type": 0,
                                                "svc_space_support_mode": 0,
                                                "svc_time_support_mode": 0,
                                                "use_type": 0
                                            }
                                        ],
                                        "ip_address": "",
                                        "manufacturer": "",
                                        "model": "",
                                        "name": "",
                                        "owner": "",
                                        "parent_id": "",
                                        "parental": 0,
                                        "password": "",
                                        "port": 0,
                                        "register_way": 0,
                                        "safety_way": 0,
                                        "secrecy": 0,
                                        "status": "[ON]ON/OFF"
                                    },
                                    "speed": 0,
                                    "start_time": "",
                                    "stop_time": "",
                                    "user": ""
                                },
                                "dh_video_cloud": {
                                    "command_type": "[Play]Play/Playback/Download",
                                    "host": "",
                                    "ipc": "",
                                    "password": "",
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "user": ""
                                },
                                "face_camera": {
                                    "dir": "",
                                    "host": "",
                                    "ipc": "",
                                    "password": "",
                                    "port": 0,
                                    "user": ""
                                },
                                "gat1400": {
                                    "client_id": "",
                                    "extra_info": "",
                                    "host": "",
                                    "password": "",
                                    "platform_id": "",
                                    "port": 0,
                                    "relative_role": "[VIAS]VIAS/UPPER_VIID/LOWER_VIID/APS",
                                    "server_id": "",
                                    "user": ""
                                },
                                "gat1400_ape": {
                                    "ape_id": "",
                                    "extra_info": "",
                                    "password": "",
                                    "raw_config": {
                                        "ape_id": "",
                                        "cap_direction": 0,
                                        "geo_point": {
                                            "latitude": 0,
                                            "longitude": 0
                                        },
                                        "ip_addr": "",
                                        "ipv6_addr": "",
                                        "is_online": "",
                                        "model": "",
                                        "monitor_area_desc": "",
                                        "monitor_direction": "",
                                        "name": "",
                                        "org_code": "",
                                        "owner_aps_id": "",
                                        "password": "",
                                        "place": "",
                                        "place_code": "",
                                        "port": 0,
                                        "user_id": ""
                                    },
                                    "user": ""
                                },
                                "gat1400_face_camera": {
                                    "ape_id": "",
                                    "raw_config": {
                                        "ape_id": "",
                                        "cap_direction": 0,
                                        "geo_point": {
                                            "latitude": 0,
                                            "longitude": 0
                                        },
                                        "ip_addr": "",
                                        "ipv6_addr": "",
                                        "is_online": "",
                                        "model": "",
                                        "monitor_area_desc": "",
                                        "monitor_direction": "",
                                        "name": "",
                                        "org_code": "",
                                        "owner_aps_id": "",
                                        "password": "",
                                        "place": "",
                                        "place_code": "",
                                        "port": 0,
                                        "user_id": ""
                                    },
                                    "server_id": ""
                                },
                                "hls": {
                                    "command_type": "[Play]Play/Playback/Download",
                                    "url": ""
                                },
                                "nvr": {
                                    "downlink_host": "",
                                    "ipc": "",
                                    "password": "",
                                    "private": false,
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "ratio_type": "[SD]SD/HD",
                                    "user": ""
                                },
                                "onvif": {
                                    "channel": 0,
                                    "host": "",
                                    "password": "",
                                    "port": 0,
                                    "profile_token": "",
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "stream_type": "[Main]Main/Second/Third/Fourth",
                                    "user": ""
                                },
                                "rtmp": {
                                    "device_id": "",
                                    "rtmp_mode": "[RTMP_MODE_PUBLISH]RTMP_MODE_PUBLISH/RTMP_MODE_PLAY",
                                    "rtmp_url": ""
                                },
                                "rtsp": {
                                    "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                                    "url": ""
                                },
                                "sjk": {
                                    "ipc": ""
                                },
                                "symphony_nebula": {
                                    "device_id": "",
                                    "task_id": ""
                                },
                                "symphony_pass": {
                                    "device_id": ""
                                }
                            },
                            "type": "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                        },
                        "source_protocol": "",
                        "status": "[TaskStatusUnset]TaskStatusUnset/TaskPending/TaskScheduleFailed/TaskRuning/TaskFinish/TaskInternalErr/TaskStopFailed/TaskSubmitted",
                        "storage_policy": {
                            "binary_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {
                                    "enable": false
                                },
                                "osg": {
                                    "enable": false
                                }
                            },
                            "panoramic_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {
                                    "enable": false
                                },
                                "osg": {
                                    "enable": false
                                }
                            },
                            "portrait_storage_config": {
                                "gat1400": {
                                    "enable": false,
                                    "platform_id": ""
                                },
                                "kafka": {
                                    "enable": false
                                },
                                "osg": {
                                    "enable": false
                                }
                            }
                        },
                        "sub_device_id": "",
                        "task_id": "",
                        "type": "[TaskTypeUnset]TaskTypeUnset/TaskTypeImage/TaskTypeVideo",
                        "video_parameter": {
                            "bit_rate": 0,
                            "bit_rate_type": "[BRT_UNKNOWN]BRT_UNKNOWN/CBR/VBR",
                            "frame_rate": 0,
                            "height": 0,
                            "i_frame_interval": 0,
                            "stream_type": "[Main]Main/Second/Third/Fourth",
                            "video_format": "[VF_UNKNOWN]VF_UNKNOWN/VF_MPEG4/VF_H264/VF_SVAC/VF_3GP/VF_H265",
                            "width": 0
                        }
                    },
                    "task_id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "merge_id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_UpdateTask")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        intef.update_body("task_id", task_id)
        intef.update_body("task", task)
        return intef.request() if sendRequest else intef

    def TaskManagerSrv_GetWorkerInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  查询worker信息 """
        """  path: [get]/v1/worker API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "workers": [
                        {
                            "app_name": "",
                            "app_version": 0,
                            "pu": 0,
                            "running": false,
                            "type": "[WorkerTypeUnset]WorkerTypeUnset/WorkerTypeIps/WorkerTypeFace/WorkerTypeAlgo"
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "TaskManagerSrv_GetWorkerInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def OTAEngineService_FirmwareListGetApi(self, list_applet_only=None, loginToken=None, sendRequest=True, print_log=True):
        """  固件列表 """
        """  path: [get]/v1/firmwares API """
        """  params: 
                参数名称：list_applet_only　类型：boolean　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "firmwares": [
                        {
                            "module_config": {
                                "last_updated_at": "",
                                "method": "[UPGRADE_METHOD_UNKNOWN]UPGRADE_METHOD_UNKNOWN/NOTIFY/SILENT/FORCE",
                                "version": {
                                    "content": "",
                                    "delta_version": {
                                        "from": "",
                                        "to": ""
                                    },
                                    "ext_data": {
                                        "additionalProp1": "",
                                        "additionalProp2": "",
                                        "additionalProp3": ""
                                    },
                                    "module": "",
                                    "package_type": "[PACKAGE_TYPE_UNKNOWN]PACKAGE_TYPE_UNKNOWN/FULL/DELTA",
                                    "sign": "",
                                    "sign_method": "[SIGN_METHOD_UNKNOWN]SIGN_METHOD_UNKNOWN/SHA256/MD5",
                                    "size": "",
                                    "uri": {
                                        "kind": "[HTTP]HTTP/DOCKER_REGISTRY/FTP",
                                        "uri": ""
                                    },
                                    "version": ""
                                }
                            },
                            "module_state": {
                                "current_version": "",
                                "ext_data": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                },
                                "last_updated_at": "",
                                "module": "",
                                "phase": "[UPGRADE_PHASE_UNKNOWN]UPGRADE_PHASE_UNKNOWN/PENDING/DOWNLOADING/DOWNLOADED/WAIT_FOR_INSTALL/INSTALLING/SUCCESSED/FAILED/DISABLED",
                                "reason": "",
                                "upgrade_version": ""
                            },
                            "upgrade_status": {
                                "download_status": {
                                    "download_retry_count": 0,
                                    "percent": 0
                                },
                                "last_transition_at": "",
                                "message": "",
                                "phase": "[UPGRADE_PHASE_UNKNOWN]UPGRADE_PHASE_UNKNOWN/PENDING/DOWNLOADING/DOWNLOADED/WAIT_FOR_INSTALL/INSTALLING/SUCCESSED/FAILED/DISABLED",
                                "reason": "",
                                "started_at": "",
                                "updated_at": ""
                            }
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "OTAEngineService_FirmwareList")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("list_applet_only", list_applet_only)
        return intef.request() if sendRequest else intef

    def OTAEngineService_FirmwareUnregisterDeleteApi(self, name=None, current_version=None, loginToken=None, sendRequest=True, print_log=True):
        """  固件卸载 """
        """  path: [delete]/v1/firmwares API """
        """  params: 
                参数名称：name　类型：string　描述：null
                参数名称：current_version　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "OTAEngineService_FirmwareUnregister")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("name", name)
        intef.update_params("current_version", current_version)
        return intef.request() if sendRequest else intef

    def OTAEngineService_FirmwareRegisterPostApi(self, name=None, current_version=None, ext_data=None, loginToken=None, sendRequest=True, print_log=True):
        """  固件注册 """
        """  path: [post]/v1/firmwares API """
        """  body: 
                {
                    "current_version": "",
                    "ext_data": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    },
                    "name": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "OTAEngineService_FirmwareRegister")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("current_version", current_version)
        intef.update_body("ext_data", ext_data)
        return intef.request() if sendRequest else intef

    def OTAEngineService_FirmwareUpgradePostApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  固件上传并执行安装，不负责升级的原子性，一但由于比如机器重启被打断之后不能恢复。
支持request... """
        """  path: [post]/v1/firmwares/upgrade API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "OTAEngineService_FirmwareUpgrade")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def Portraits_CreatePortraitsPostApi(self, db_id=None, portrait_infos=None, quality_threshold=None, loginToken=None, sendRequest=True, print_log=True):
        """  创建人像 """
        """  path: [post]/v1/portraits API """
        """  body: 
                {
                    "db_id": "",
                    "portrait_infos": [
                        {
                            "activation_time": "",
                            "age": 0,
                            "company": "",
                            "department": "",
                            "expire_time": "",
                            "extra_info": "",
                            "gender": 0,
                            "ic_number": "",
                            "id_number": "",
                            "image": {
                                "data": "",
                                "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                "url": ""
                            },
                            "job_number": "",
                            "name": "",
                            "phone": "",
                            "portrait_id": "",
                            "remark": ""
                        }
                    ],
                    "quality_threshold": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "details": [],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "results": [
                        {
                            "code": 0,
                            "details": [],
                            "image": {
                                "data": "",
                                "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                "url": ""
                            },
                            "message": "",
                            "portrait_id": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_CreatePortraits")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("portrait_infos", portrait_infos)
        intef.update_body("quality_threshold", quality_threshold)
        return intef.request() if sendRequest else intef

    def Portraits_UpdatePortraitsPutApi(self, db_id=None, portrait_infos=None, quality_threshold=None, loginToken=None, sendRequest=True, print_log=True):
        """  更新人像 """
        """  path: [put]/v1/portraits API """
        """  body: 
                {
                    "db_id": "",
                    "portrait_infos": [
                        {
                            "activation_time": "",
                            "age": 0,
                            "company": "",
                            "department": "",
                            "expire_time": "",
                            "extra_info": "",
                            "gender": 0,
                            "ic_number": "",
                            "id_number": "",
                            "image": {
                                "data": "",
                                "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                "url": ""
                            },
                            "job_number": "",
                            "name": "",
                            "phone": "",
                            "portrait_id": "",
                            "remark": ""
                        }
                    ],
                    "quality_threshold": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "details": [],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "results": [
                        {
                            "code": 0,
                            "details": [],
                            "image": {
                                "data": "",
                                "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                "url": ""
                            },
                            "message": "",
                            "portrait_id": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_UpdatePortraits")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("portrait_infos", portrait_infos)
        intef.update_body("quality_threshold", quality_threshold)
        return intef.request() if sendRequest else intef

    def Portraits_CompareImageInDBPostApi(self, db_id=None, portrait_id=None, image=None, loginToken=None, sendRequest=True, print_log=True):
        """  单张图片跟库中指定人像进行1:1比对 """
        """  path: [post]/v1/portraits/compare_image_in_db API """
        """  body: 
                {
                    "db_id": "",
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    },
                    "portrait_id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "details": [],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "quality": 0,
                    "score": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_CompareImageInDB")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("portrait_id", portrait_id)
        intef.update_body("image", image)
        return intef.request() if sendRequest else intef

    def Portraits_CompareOneToOnePostApi(self, image_1=None, image_2=None, feature_version=None, loginToken=None, sendRequest=True, print_log=True):
        """  图片1:1比对 """
        """  path: [post]/v1/portraits/compare_one_to_one API """
        """  body: 
                {
                    "feature_version": 0,
                    "image_1": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    },
                    "image_2": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "details": [],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "quality_1": 0,
                    "quality_2": 0,
                    "score": 0
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_CompareOneToOne")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("image_1", image_1)
        intef.update_body("image_2", image_2)
        intef.update_body("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def Portraits_GetPortraitsConfigGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  获取全局配置信息 """
        """  path: [get]/v1/portraits/config API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "data": {
                        "default_feature_version": 0,
                        "global_db_capacity": 0,
                        "image_encrypt": false,
                        "max_db_num": 0,
                        "portrait_config": {
                            "max_dbs_per_query": 0,
                            "secret_sections": {
                                "additionalProp1": false,
                                "additionalProp2": false,
                                "additionalProp3": false
                            }
                        },
                        "save_images": false,
                        "support_feature_version_list": []
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_GetPortraitsConfig")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def Portraits_ListPortraitDbsGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询人像库列表 """
        """  path: [get]/v1/portraits/dbs API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
[EN] Optional, start position, value: > = 0, 0 is the first line; the default value is 0.
In response, actual offset of the first returned record is returned
(generally equals to the offset in request).
                参数名称：page.limit　类型：integer　描述：可选, 长度, 取值范围[0,100], 如果超出范围, 则返回失败;
若取值为0或不填写, limit取缺省值值. 人像库查询无缺省值, 即返回所有人像库;人像查询缺省limit值为50.
[EN] Length, value range [0,100], if it is out of the range, error will be returned;
If the value is 0 or not filled in, limit takes the default value. There is no default value for portraits/dbs query, it will return all portrait databases; the default limit value for portraits query is 50.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
[EN] Optional, this parameter is not required for request, but will be
filled in response
        """
        """  resp:
                200(A successful response.):
                {
                    "data": {
                        "dbs": [
                            {
                                "created_timestamp": "",
                                "created_user_code": 0,
                                "db_capacity": 0,
                                "db_id": "",
                                "db_name": "",
                                "db_size": 0,
                                "db_state": 0,
                                "db_type": 0,
                                "description": "",
                                "feature_db_id": "",
                                "feature_version": 0,
                                "import_type": 0,
                                "updated_timestamp": "",
                                "updated_user_code": 0
                            }
                        ],
                        "page": {
                            "limit": 0,
                            "offset": 0,
                            "total": 0
                        }
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_ListPortraitDbs")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def Portraits_CreatePortraitDbPostApi(self, db_name=None, db_type=None, db_capacity=None, operator=None, feature_version=None, description=None, loginToken=None, sendRequest=True, print_log=True):
        """  创建人像库 """
        """  path: [post]/v1/portraits/dbs API """
        """  body: 
                {
                    "db_capacity": 0,
                    "db_name": "",
                    "db_type": 0,
                    "description": "",
                    "feature_version": 0,
                    "operator": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "data": {
                        "created_timestamp": "",
                        "created_user_code": 0,
                        "db_capacity": 0,
                        "db_id": "",
                        "db_name": "",
                        "db_size": 0,
                        "db_state": 0,
                        "db_type": 0,
                        "description": "",
                        "feature_db_id": "",
                        "feature_version": 0,
                        "import_type": 0,
                        "updated_timestamp": "",
                        "updated_user_code": 0
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_CreatePortraitDb")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("db_name", db_name)
        intef.update_body("db_type", db_type)
        intef.update_body("db_capacity", db_capacity)
        intef.update_body("operator", operator)
        intef.update_body("feature_version", feature_version)
        intef.update_body("description", description)
        return intef.request() if sendRequest else intef

    def Portraits_DeletePortraitDbPostApi(self, db_id=None, unsafe_mode=None, operator=None, loginToken=None, sendRequest=True, print_log=True):
        """  删除人像库 """
        """  path: [post]/v1/portraits/dbs/delete API """
        """  body: 
                {
                    "db_id": "",
                    "operator": 0,
                    "unsafe_mode": false
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "data": [
                        {
                            "task_id": "",
                            "task_name": ""
                        }
                    ],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_DeletePortraitDb")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("unsafe_mode", unsafe_mode)
        intef.update_body("operator", operator)
        return intef.request() if sendRequest else intef

    def Portraits_QueryPortraitDbsPostApi(self, db_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询人像库集合信息 """
        """  path: [post]/v1/portraits/dbs/query API """
        """  body: 
                {
                    "db_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "data": [
                        {
                            "created_timestamp": "",
                            "created_user_code": 0,
                            "db_capacity": 0,
                            "db_id": "",
                            "db_name": "",
                            "db_size": 0,
                            "db_state": 0,
                            "db_type": 0,
                            "description": "",
                            "feature_db_id": "",
                            "feature_version": 0,
                            "import_type": 0,
                            "updated_timestamp": "",
                            "updated_user_code": 0
                        }
                    ],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_QueryPortraitDbs")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("db_ids", db_ids)
        return intef.request() if sendRequest else intef

    def Portraits_UpdatePortraitDbPutApi(self, db_id, db_name=None, db_type=None, description=None, operator=None, loginToken=None, sendRequest=True, print_log=True):
        """  更新人像库 """
        """  path: [put]/v1/portraits/dbs/{db_id} API """
        """  body: 
                {
                    "db_id": "",
                    "db_name": "",
                    "db_type": 0,
                    "description": "",
                    "operator": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "data": {
                        "created_timestamp": "",
                        "created_user_code": 0,
                        "db_capacity": 0,
                        "db_id": "",
                        "db_name": "",
                        "db_size": 0,
                        "db_state": 0,
                        "db_type": 0,
                        "description": "",
                        "feature_db_id": "",
                        "feature_version": 0,
                        "import_type": 0,
                        "updated_timestamp": "",
                        "updated_user_code": 0
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_UpdatePortraitDb")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("db_id", db_id)
        intef.update_body("db_id", db_id)
        intef.update_body("db_name", db_name)
        intef.update_body("db_type", db_type)
        intef.update_body("description", description)
        intef.update_body("operator", operator)
        return intef.request() if sendRequest else intef

    def Portraits_DecryptTextsPutApi(self, texts=None, loginToken=None, sendRequest=True, print_log=True):
        """  文本解密 """
        """  path: [put]/v1/portraits/decrypt API """
        """  body: 
                {
                    "texts": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "decrypt_results": [
                        {
                            "code": 0,
                            "decrypt_text": "",
                            "message": "",
                            "text": ""
                        }
                    ],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_DecryptTexts")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("texts", texts)
        return intef.request() if sendRequest else intef

    def Portraits_DeletePortraitsPostApi(self, db_id=None, portrait_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  删除人像 """
        """  path: [post]/v1/portraits/delete API """
        """  body: 
                {
                    "db_id": "",
                    "portrait_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "details": [],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "results": [
                        {
                            "code": 0,
                            "details": [],
                            "message": "",
                            "portrait_id": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_DeletePortraits")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("portrait_ids", portrait_ids)
        return intef.request() if sendRequest else intef

    def Portraits_ExportPortraitsPostApi(self, portraits_ids=None, db_id=None, loginToken=None, sendRequest=True, print_log=True):
        """  导出人像 """
        """  path: [post]/v1/portraits/export API """
        """  body: 
                {
                    "db_id": "",
                    "portraits_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "data": {
                        "affected_rows": 0,
                        "password": "",
                        "path": ""
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_ExportPortraits")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("portraits_ids", portraits_ids)
        intef.update_body("db_id", db_id)
        return intef.request() if sendRequest else intef

    def Portraits_ListPortraitsGetApi(self, db_id=None, encrypted=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询人像列表 """
        """  path: [get]/v1/portraits/list API """
        """  params: 
                参数名称：db_id　类型：string　描述：人像库id, 长度范围[1,64].
                参数名称：encrypted　类型：boolean　描述：加密标识.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
[EN] Optional, start position, value: > = 0, 0 is the first line; the default value is 0.
In response, actual offset of the first returned record is returned
(generally equals to the offset in request).
                参数名称：page.limit　类型：integer　描述：可选, 长度, 取值范围[0,100], 如果超出范围, 则返回失败;
若取值为0或不填写, limit取缺省值值. 人像库查询无缺省值, 即返回所有人像库;人像查询缺省limit值为50.
[EN] Length, value range [0,100], if it is out of the range, error will be returned;
If the value is 0 or not filled in, limit takes the default value. There is no default value for portraits/dbs query, it will return all portrait databases; the default limit value for portraits query is 50.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
[EN] Optional, this parameter is not required for request, but will be
filled in response
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "details": [],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "page": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    },
                    "portraits": [
                        {
                            "create_time": "",
                            "portrait_info": {
                                "activation_time": "",
                                "age": 0,
                                "company": "",
                                "department": "",
                                "expire_time": "",
                                "extra_info": "",
                                "gender": 0,
                                "ic_number": "",
                                "id_number": "",
                                "image": {
                                    "data": "",
                                    "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                    "url": ""
                                },
                                "job_number": "",
                                "name": "",
                                "phone": "",
                                "portrait_id": "",
                                "remark": ""
                            },
                            "status": 0,
                            "update_time": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_ListPortraits")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("db_id", db_id)
        intef.update_params("encrypted", encrypted)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def Portraits_QueryPortraitsPostApi(self, db_id=None, encrypted=None, portrait_ids=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询人像 """
        """  path: [post]/v1/portraits/query API """
        """  body: 
                {
                    "db_id": "",
                    "encrypted": false,
                    "portrait_ids": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "details": [],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "results": [
                        {
                            "code": 0,
                            "details": [],
                            "message": "",
                            "portrait": {
                                "create_time": "",
                                "portrait_info": {
                                    "activation_time": "",
                                    "age": 0,
                                    "company": "",
                                    "department": "",
                                    "expire_time": "",
                                    "extra_info": "",
                                    "gender": 0,
                                    "ic_number": "",
                                    "id_number": "",
                                    "image": {
                                        "data": "",
                                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                        "url": ""
                                    },
                                    "job_number": "",
                                    "name": "",
                                    "phone": "",
                                    "portrait_id": "",
                                    "remark": ""
                                },
                                "status": 0,
                                "update_time": ""
                            }
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_QueryPortraits")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("encrypted", encrypted)
        intef.update_body("portrait_ids", portrait_ids)
        return intef.request() if sendRequest else intef

    def Portraits_SearchPortraitsPostApi(self, db_ids=None, encrypted=None, page=None, name=None, job_number=None, ic_number=None, id_number=None, start_activation_time=None, end_activation_time=None, start_expire_time=None, end_expire_time=None, status=None, loginToken=None, sendRequest=True, print_log=True):
        """  搜索人像 """
        """  path: [post]/v1/portraits/search API """
        """  body: 
                {
                    "db_ids": [],
                    "encrypted": false,
                    "end_activation_time": "",
                    "end_expire_time": "",
                    "ic_number": "",
                    "id_number": "",
                    "job_number": "",
                    "name": "",
                    "page": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    },
                    "start_activation_time": "",
                    "start_expire_time": "",
                    "status": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "details": [],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "page": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    },
                    "results": [
                        {
                            "create_time": "",
                            "portrait_info": {
                                "activation_time": "",
                                "age": 0,
                                "company": "",
                                "department": "",
                                "expire_time": "",
                                "extra_info": "",
                                "gender": 0,
                                "ic_number": "",
                                "id_number": "",
                                "image": {
                                    "data": "",
                                    "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                    "url": ""
                                },
                                "job_number": "",
                                "name": "",
                                "phone": "",
                                "portrait_id": "",
                                "remark": ""
                            },
                            "status": 0,
                            "update_time": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_SearchPortraits")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("db_ids", db_ids)
        intef.update_body("encrypted", encrypted)
        intef.update_body("page", page)
        intef.update_body("name", name)
        intef.update_body("job_number", job_number)
        intef.update_body("ic_number", ic_number)
        intef.update_body("id_number", id_number)
        intef.update_body("start_activation_time", start_activation_time)
        intef.update_body("end_activation_time", end_activation_time)
        intef.update_body("start_expire_time", start_expire_time)
        intef.update_body("end_expire_time", end_expire_time)
        intef.update_body("status", status)
        return intef.request() if sendRequest else intef

    def Portraits_SearchImageInDBsPostApi(self, dbs=None, image=None, loginToken=None, sendRequest=True, print_log=True):
        """  在多个人像库进行图片1:N比对 """
        """  path: [post]/v1/portraits/search/image API """
        """  body: 
                {
                    "dbs": [
                        {
                            "db_id": "",
                            "min_score": 0,
                            "top_k": 0
                        }
                    ],
                    "image": {
                        "data": "",
                        "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                        "url": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "details": [],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "results": [
                        {
                            "code": 0,
                            "db_id": "",
                            "details": [],
                            "message": "",
                            "similar_results": [
                                {
                                    "portrait_id": "",
                                    "score": 0
                                }
                            ]
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "Portraits_SearchImageInDBs")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("dbs", dbs)
        intef.update_body("image", image)
        return intef.request() if sendRequest else intef

    def RecordProcess_DeleteBizAppInfoPostApi(self, bizapp_name=None, bizapp_version=None, loginToken=None, sendRequest=True, print_log=True):
        """  【内部接口】删除bizapp，用于删除用户自定义bizapp的topic等信息，则记录将不会转发给设... """
        """  path: [post]/v1/appinfo/delete API """
        """  body: 
                {
                    "bizapp_name": "",
                    "bizapp_version": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "RecordProcess_DeleteBizAppInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("bizapp_name", bizapp_name)
        intef.update_body("bizapp_version", bizapp_version)
        return intef.request() if sendRequest else intef

    def RecordProcess_GetBizAppInfoGetApi(self, biz_app_name, loginToken=None, sendRequest=True, print_log=True):
        """  【内部接口】查询具体bizapp的推送topic """
        """  path: [get]/v1/appinfo/query/{biz_app_name} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "bizapp_info": {
                        "applets": [
                            {
                                "app_name": "",
                                "app_table_name": "",
                                "app_topic": "",
                                "app_url": "",
                                "app_version": "",
                                "fields": [
                                    {
                                        "field": "",
                                        "source": "",
                                        "type": ""
                                    }
                                ],
                                "target_types": [
                                    {
                                        "detect_type": "",
                                        "detect_type_topic": "",
                                        "push_topic_switch": "",
                                        "st_event_type": ""
                                    }
                                ]
                            }
                        ],
                        "bizapp_name": "",
                        "bizapp_version": ""
                    },
                    "code": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "RecordProcess_GetBizAppInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("biz_app_name", biz_app_name)
        return intef.request() if sendRequest else intef

    def RecordProcess_SetBizAppInfoPostApi(self, bizapp_info=None, loginToken=None, sendRequest=True, print_log=True):
        """  设置具体bizapp的推送topic，用于设置用户自定义bizapp的topic等信息，则记录会转发... """
        """  path: [post]/v1/appinfo/setting API """
        """  body: 
                {
                    "bizapp_info": {
                        "applets": [
                            {
                                "app_name": "",
                                "app_table_name": "",
                                "app_topic": "",
                                "app_url": "",
                                "app_version": "",
                                "fields": [
                                    {
                                        "field": "",
                                        "source": "",
                                        "type": ""
                                    }
                                ],
                                "target_types": [
                                    {
                                        "detect_type": "",
                                        "detect_type_topic": "",
                                        "push_topic_switch": "",
                                        "st_event_type": ""
                                    }
                                ]
                            }
                        ],
                        "bizapp_name": "",
                        "bizapp_version": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "RecordProcess_SetBizAppInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("bizapp_info", bizapp_info)
        return intef.request() if sendRequest else intef

    def RecordProcess_GetStorageSwitchGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  【内部接口】查询storage使用的是es还是pg """
        """  path: [get]/v1/storageswitch/query API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "storage_switch": "[pg]pg/es"
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "RecordProcess_GetStorageSwitch")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def RecordProcess_GetTracelessSwitchGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  查询当前无痕模式 """
        """  path: [get]/v1/tracelessswitch API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": "",
                    "storage_mode": "[STORAGE_MODE_RECORD_ONLY]STORAGE_MODE_RECORD_ONLY/STORAGE_MODE_NORMAL/STORAGE_MODE_TRACELESS"
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "RecordProcess_GetTracelessSwitch")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def RecordProcess_SetTracelessSwitchPostApi(self, storage_mode=None, loginToken=None, sendRequest=True, print_log=True):
        """  设置当前无痕模式
无痕模式设置开启时:会清除所有已经产生的记录，图片不清除，且后续记录将存记录，不... """
        """  path: [post]/v1/tracelessswitch API """
        """  body: 
                {
                    "storage_mode": "[STORAGE_MODE_RECORD_ONLY]STORAGE_MODE_RECORD_ONLY/STORAGE_MODE_NORMAL/STORAGE_MODE_TRACELESS"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "code": 0,
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "message": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "RecordProcess_SetTracelessSwitch")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("storage_mode", storage_mode)
        return intef.request() if sendRequest else intef

    def AgentUserService_ListAPIInfoGetApi(self, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True):
        """  API信息列表. """
        """  path: [get]/v1/apis API """
        """  params: 
                参数名称：paging.offset　类型：integer　描述：参数 偏移量 0开始.
                参数名称：paging.limit　类型：integer　描述：参数 限制条数.
                参数名称：paging.total　类型：integer　描述：总数,返回时有值
        """
        """  resp:
                200(A successful response.):
                {
                    "apis": [
                        {
                            "create_at": "",
                            "id": "",
                            "method": "",
                            "name": "",
                            "remark": "",
                            "service_name": "",
                            "update_at": "",
                            "uri": ""
                        }
                    ],
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_ListAPIInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def AgentUserService_AddAPIInfoPostApi(self, api=None, loginToken=None, sendRequest=True, print_log=True):
        """  增加API信息. """
        """  path: [post]/v1/apis API """
        """  body: 
                {
                    "api": {
                        "create_at": "",
                        "id": "",
                        "method": "",
                        "name": "",
                        "remark": "",
                        "service_name": "",
                        "update_at": "",
                        "uri": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_AddAPIInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("api", api)
        return intef.request() if sendRequest else intef

    def AgentUserService_UpdateAPIInfoPutApi(self, api=None, loginToken=None, sendRequest=True, print_log=True):
        """  更新API信息. """
        """  path: [put]/v1/apis API """
        """  body: 
                {
                    "api": {
                        "create_at": "",
                        "id": "",
                        "method": "",
                        "name": "",
                        "remark": "",
                        "service_name": "",
                        "update_at": "",
                        "uri": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_UpdateAPIInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("api", api)
        return intef.request() if sendRequest else intef

    def AgentUserService_GetAPIInfoGetApi(self, id, loginToken=None, sendRequest=True, print_log=True):
        """  查询API信息. """
        """  path: [get]/v1/apis/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "api": {
                        "create_at": "",
                        "id": "",
                        "method": "",
                        "name": "",
                        "remark": "",
                        "service_name": "",
                        "update_at": "",
                        "uri": ""
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_GetAPIInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def AgentUserService_DeleteAPIInfoDeleteApi(self, id, loginToken=None, sendRequest=True, print_log=True):
        """  删除API信息. """
        """  path: [delete]/v1/apis/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_DeleteAPIInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def AgentUserService_CaptchaGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  图形验证码. """
        """  path: [get]/v1/captcha API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "key": "",
                    "pic": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_Captcha")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def AgentUserService_ListRoleGetApi(self, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True):
        """  角色列表. """
        """  path: [get]/v1/roles API """
        """  params: 
                参数名称：paging.offset　类型：integer　描述：参数 偏移量 0开始.
                参数名称：paging.limit　类型：integer　描述：参数 限制条数.
                参数名称：paging.total　类型：integer　描述：总数,返回时有值
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    },
                    "roles": [
                        {
                            "create_at": "",
                            "id": "",
                            "name": "",
                            "update_at": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_ListRole")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def AgentUserService_AddRolePostApi(self, role=None, loginToken=None, sendRequest=True, print_log=True):
        """  创建角色. """
        """  path: [post]/v1/roles API """
        """  body: 
                {
                    "role": {
                        "apis": [],
                        "create_at": "",
                        "id": "",
                        "name": "",
                        "update_at": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_AddRole")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("role", role)
        return intef.request() if sendRequest else intef

    def AgentUserService_UpdateRolePutApi(self, role=None, loginToken=None, sendRequest=True, print_log=True):
        """  修改角色. """
        """  path: [put]/v1/roles API """
        """  body: 
                {
                    "role": {
                        "apis": [],
                        "create_at": "",
                        "id": "",
                        "name": "",
                        "update_at": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_UpdateRole")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("role", role)
        return intef.request() if sendRequest else intef

    def AgentUserService_GetRoleGetApi(self, id, loginToken=None, sendRequest=True, print_log=True):
        """  查询角色详情 """
        """  path: [get]/v1/roles/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "role": {
                        "apis": [],
                        "create_at": "",
                        "id": "",
                        "name": "",
                        "update_at": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_GetRole")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def AgentUserService_DeleteRoleDeleteApi(self, id, loginToken=None, sendRequest=True, print_log=True):
        """  删除角色. """
        """  path: [delete]/v1/roles/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_DeleteRole")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def AgentUserService_ListUserGetApi(self, paging_offset=None, paging_limit=None, paging_total=None, decrypt=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询用户列表. """
        """  path: [get]/v1/users API """
        """  params: 
                参数名称：paging.offset　类型：integer　描述：参数 偏移量 0开始.
                参数名称：paging.limit　类型：integer　描述：参数 限制条数.
                参数名称：paging.total　类型：integer　描述：总数,返回时有值.
                参数名称：decrypt　类型：boolean　描述：敏感字段是否解密
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    },
                    "users": [
                        {
                            "address": "",
                            "api_secret": "",
                            "company": "",
                            "create_at": "",
                            "department": "",
                            "id_card": "",
                            "password": "",
                            "phone": "",
                            "real_name": "",
                            "role_id": "",
                            "sex": "",
                            "state": "[USER_STATE_UNSET]USER_STATE_UNSET/USER_STATE_ENABLED/USER_STATE_DISABLED",
                            "update_at": "",
                            "user_id": "",
                            "user_name": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_ListUser")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        intef.update_params("decrypt", decrypt)
        return intef.request() if sendRequest else intef

    def AgentUserService_AddUserPostApi(self, user=None, loginToken=None, sendRequest=True, print_log=True):
        """  增加用户. """
        """  path: [post]/v1/users API """
        """  body: 
                {
                    "user": {
                        "address": "",
                        "api_secret": "",
                        "company": "",
                        "create_at": "",
                        "department": "",
                        "id_card": "",
                        "password": "",
                        "phone": "",
                        "real_name": "",
                        "role_id": "",
                        "sex": "",
                        "state": "[USER_STATE_UNSET]USER_STATE_UNSET/USER_STATE_ENABLED/USER_STATE_DISABLED",
                        "update_at": "",
                        "user_id": "",
                        "user_name": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_AddUser")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("user", user)
        return intef.request() if sendRequest else intef

    def AgentUserService_UpdateUserPutApi(self, user=None, loginToken=None, sendRequest=True, print_log=True):
        """  更新用户. """
        """  path: [put]/v1/users API """
        """  body: 
                {
                    "user": {
                        "address": "",
                        "api_secret": "",
                        "company": "",
                        "create_at": "",
                        "department": "",
                        "id_card": "",
                        "password": "",
                        "phone": "",
                        "real_name": "",
                        "role_id": "",
                        "sex": "",
                        "state": "[USER_STATE_UNSET]USER_STATE_UNSET/USER_STATE_ENABLED/USER_STATE_DISABLED",
                        "update_at": "",
                        "user_id": "",
                        "user_name": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_UpdateUser")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("user", user)
        return intef.request() if sendRequest else intef

    def AgentUserService_IsInitializedGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  用户是否初始化(admin账户是否首次登录). """
        """  path: [get]/v1/users/initialization API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "initialization": false
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_IsInitialized")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def AgentUserService_UserLoginPostApi(self, user_name=None, password=None, key=None, captcha=None, loginToken=None, sendRequest=True, print_log=True):
        """  用户登录, 当返回错误码为11时, 表示需要下次登录需要验证码. """
        """  path: [post]/v1/users/login API """
        """  body: 
                {
                    "captcha": "",
                    "key": "",
                    "password": "",
                    "user_name": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "token": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_UserLogin")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("user_name", user_name)
        intef.update_body("password", password)
        intef.update_body("key", key)
        intef.update_body("captcha", captcha)
        return intef.request() if sendRequest else intef

    def AgentUserService_UserLogoutPostApi(self, token=None, loginToken=None, sendRequest=True, print_log=True):
        """  用户注销. """
        """  path: [post]/v1/users/logout API """
        """  body: 
                {
                    "token": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_UserLogout")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("token", token)
        return intef.request() if sendRequest else intef

    def AgentUserService_GetUserGetApi(self, id, decrypt=None, loginToken=None, sendRequest=True, print_log=True):
        """  查询用户信息 """
        """  path: [get]/v1/users/{id} API """
        """  params: 
                参数名称：decrypt　类型：boolean　描述：敏感字段是否解密
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "user": {
                        "address": "",
                        "api_secret": "",
                        "company": "",
                        "create_at": "",
                        "department": "",
                        "id_card": "",
                        "password": "",
                        "phone": "",
                        "real_name": "",
                        "role_id": "",
                        "sex": "",
                        "state": "[USER_STATE_UNSET]USER_STATE_UNSET/USER_STATE_ENABLED/USER_STATE_DISABLED",
                        "update_at": "",
                        "user_id": "",
                        "user_name": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_GetUser")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_params("decrypt", decrypt)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def AgentUserService_DeleteUserDeleteApi(self, id, loginToken=None, sendRequest=True, print_log=True):
        """  删除用户. """
        """  path: [delete]/v1/users/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_DeleteUser")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def AgentUserService_UpdateUserApiSecretPostApi(self, id, loginToken=None, sendRequest=True, print_log=True):
        """  重新生成用户ApiSecret """
        """  path: [post]/v1/users/{id}/reset-api-secret API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                {
                    "api_secret": "",
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "AgentUserService_UpdateUserApiSecret")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def NebulaVDDAgentSrv_DownloadLiveShotPostApi(self, RTSP=None, loginToken=None, sendRequest=True, print_log=True):
        """  获取实时背景大图. """
        """  path: [post]/v1/live/shot/download API """
        """  body: 
                {
                    "RTSP": {
                        "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                        "url": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "image": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaVDDAgentSrv_DownloadLiveShot")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("RTSP", RTSP)
        return intef.request() if sendRequest else intef

    def NebulaVDDAgentSrv_DownloadReplayShotPostApi(self, source_type=None, source=None, timestamp=None, loginToken=None, sendRequest=True, print_log=True):
        """  批量下载回放图片. """
        """  path: [post]/v1/replay/shot/download API """
        """  body: 
                {
                    "source": {
                        "RTSP": {
                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                            "url": ""
                        },
                        "network_video_recorder": {
                            "brand": "[BR_UNSET]BR_UNSET/UNKNOWN/HIKVISION/DAHUA",
                            "object_sub_device_ip": "",
                            "password": "",
                            "port": 0,
                            "sub_device_ip": "",
                            "user_name": ""
                        },
                        "source_type": "[Unset]Unset/SourceNetworkVideoRecorder/RTSP"
                    },
                    "source_type": "[Unset]Unset/SourceNetworkVideoRecorder/RTSP",
                    "timestamp": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaVDDAgentSrv_DownloadReplayShot")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("source_type", source_type)
        intef.update_body("source", source)
        intef.update_body("timestamp", timestamp)
        return intef.request() if sendRequest else intef

    def NebulaVDDAgentSrv_DownloadReplayVideoPostApi(self, source_type=None, source=None, timestamp=None, before=None, after=None, loginToken=None, sendRequest=True, print_log=True):
        """  批量下载回放短视频. """
        """  path: [post]/v1/replay/video/download API """
        """  body: 
                {
                    "after": 0,
                    "before": 0,
                    "source": {
                        "RTSP": {
                            "protocol_type": "[TCP]TCP/UDP/TCP_SERVER_MODE",
                            "url": ""
                        },
                        "network_video_recorder": {
                            "brand": "[BR_UNSET]BR_UNSET/UNKNOWN/HIKVISION/DAHUA",
                            "object_sub_device_ip": "",
                            "password": "",
                            "port": 0,
                            "sub_device_ip": "",
                            "user_name": ""
                        },
                        "source_type": "[Unset]Unset/SourceNetworkVideoRecorder/RTSP"
                    },
                    "source_type": "[Unset]Unset/SourceNetworkVideoRecorder/RTSP",
                    "timestamp": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("edge", "NebulaVDDAgentSrv_DownloadReplayVideo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("source_type", source_type)
        intef.update_body("source", source)
        intef.update_body("timestamp", timestamp)
        intef.update_body("before", before)
        intef.update_body("after", after)
        return intef.request() if sendRequest else intef

    def BatchCompareFeaturePostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True):
        """  人脸特征1:1比对 [SINCE v3.1.0].
[EN] One to one Identity... """
        """  path: [post]/engine/image-process/face-extract/v1/batch_compare_feature API """
        """  body: 
                {
                    "requests": [
                        {
                            "one": {
                                "blob": "",
                                "type": "",
                                "version": 0
                            },
                            "other": {
                                "blob": "",
                                "type": "",
                                "version": 0
                            }
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "score": 0
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                        }
                    ]
                }

        """
        intef = collections.interface("edge", "BatchCompareFeature")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def BatchDetectPostApi(self, requests=None, detect_mode=None, face_type=None, loginToken=None, sendRequest=True, print_log=True):
        """  对批量的图片中的人脸进行检测(只输出检测框和关键点坐标, 不输出特征和属性).
[EN] Detec... """
        """  path: [post]/engine/image-process/face-extract/v1/batch_detect API """
        """  body: 
                {
                    "detect_mode": "[Default]Default/Slow",
                    "face_type": "[Large]Large/Small",
                    "requests": [
                        {
                            "image": {
                                "cache_url": "",
                                "data": "",
                                "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                "image_id": "",
                                "url": ""
                            }
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "face_info": [
                                {
                                    "algo": {
                                        "app_name": "",
                                        "app_version": 0,
                                        "data": {
                                            "type_url": "",
                                            "value": ""
                                        },
                                        "object_type": "",
                                        "object_version": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        }
                                    },
                                    "associations": [
                                        {
                                            "object_id": "",
                                            "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                                        }
                                    ],
                                    "automobile": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "crowd": {
                                        "density_map": "",
                                        "density_size": {
                                            "height": 0,
                                            "width": 0
                                        },
                                        "incident": [
                                            {
                                                "id": "",
                                                "start_time": "",
                                                "status": "[INCIDENT_START]INCIDENT_START/INCIDENT_CONTINUE/INCIDENT_STOP",
                                                "stop_time": "",
                                                "type": "[INCIDENT_CROWD]INCIDENT_CROWD/INCIDENT_STRAND",
                                                "update_time": "",
                                                "uuid": ""
                                            }
                                        ],
                                        "quantity": "",
                                        "strand_map": {
                                            "cache_url": "",
                                            "data": "",
                                            "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                            "image_id": "",
                                            "url": ""
                                        }
                                    },
                                    "cyclist": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "event": {
                                        "event_id": "",
                                        "event_status": "[EVENT_START]EVENT_START/EVENT_CONTINUE",
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "rule": {
                                            "direction": {
                                                "x": 0,
                                                "y": 0
                                            },
                                            "duration": "",
                                            "roi": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "rule_id": "",
                                            "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                        }
                                    },
                                    "face": {
                                        "angle": {
                                            "pitch": 0,
                                            "roll": 0,
                                            "yaw": 0
                                        },
                                        "attributes": {
                                            "additionalProp1": "",
                                            "additionalProp2": "",
                                            "additionalProp3": ""
                                        },
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "face_score": 0,
                                        "landmarks": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ],
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "human_powered_vehicle": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "object_id": "",
                                    "pedestrian": {
                                        "attributes_with_score": {
                                            "additionalProp1": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp2": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            },
                                            "additionalProp3": {
                                                "category": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                "value": 0
                                            }
                                        },
                                        "quality": 0,
                                        "rectangle": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "track_id": ""
                                    },
                                    "portrait_image_location": {
                                        "panoramic_image_size": {
                                            "height": 0,
                                            "width": 0
                                        },
                                        "portrait_image_in_panoramic": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "portrait_in_panoramic": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        }
                                    },
                                    "scenario": {
                                        "objects": [
                                            {
                                                "attributes_with_score": {
                                                    "additionalProp1": {
                                                        "category": "",
                                                        "roi": {
                                                            "vertices": [
                                                                {
                                                                    "x": 0,
                                                                    "y": 0
                                                                }
                                                            ]
                                                        },
                                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                        "value": 0
                                                    },
                                                    "additionalProp2": {
                                                        "category": "",
                                                        "roi": {
                                                            "vertices": [
                                                                {
                                                                    "x": 0,
                                                                    "y": 0
                                                                }
                                                            ]
                                                        },
                                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                        "value": 0
                                                    },
                                                    "additionalProp3": {
                                                        "category": "",
                                                        "roi": {
                                                            "vertices": [
                                                                {
                                                                    "x": 0,
                                                                    "y": 0
                                                                }
                                                            ]
                                                        },
                                                        "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                        "value": 0
                                                    }
                                                },
                                                "quality": 0,
                                                "rectangle": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                            }
                                        ]
                                    },
                                    "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                        }
                    ]
                }

        """
        intef = collections.interface("edge", "BatchDetect")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("face_type", face_type)
        return intef.request() if sendRequest else intef

    def BatchDetectAndExtractAll2PostApi(self, requests=None, detect_mode=None, face_type=None, loginToken=None, sendRequest=True, print_log=True):
        """  对批量的图片中的所有人脸进行检测、提特征、提属性. v2.1.0之后用于替代BatchDetectA... """
        """  path: [post]/engine/image-process/face-extract/v1/batch_detect_and_extract_all_2 API """
        """  body: 
                {
                    "detect_mode": "[Default]Default/Slow",
                    "face_type": "[Large]Large/Small",
                    "requests": [
                        {
                            "auto_rotation_thresh": 0,
                            "face_selection": "[LargestFace]LargestFace",
                            "image": {
                                "cache_url": "",
                                "data": "",
                                "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                "image_id": "",
                                "url": ""
                            }
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "responses": [
                                {
                                    "face_info": {
                                        "algo": {
                                            "app_name": "",
                                            "app_version": 0,
                                            "data": {
                                                "type_url": "",
                                                "value": ""
                                            },
                                            "object_type": "",
                                            "object_version": 0,
                                            "rectangle": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            }
                                        },
                                        "associations": [
                                            {
                                                "object_id": "",
                                                "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                                            }
                                        ],
                                        "automobile": {
                                            "attributes_with_score": {
                                                "additionalProp1": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp2": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp3": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                }
                                            },
                                            "quality": 0,
                                            "rectangle": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "track_id": ""
                                        },
                                        "crowd": {
                                            "density_map": "",
                                            "density_size": {
                                                "height": 0,
                                                "width": 0
                                            },
                                            "incident": [
                                                {
                                                    "id": "",
                                                    "start_time": "",
                                                    "status": "[INCIDENT_START]INCIDENT_START/INCIDENT_CONTINUE/INCIDENT_STOP",
                                                    "stop_time": "",
                                                    "type": "[INCIDENT_CROWD]INCIDENT_CROWD/INCIDENT_STRAND",
                                                    "update_time": "",
                                                    "uuid": ""
                                                }
                                            ],
                                            "quantity": "",
                                            "strand_map": {
                                                "cache_url": "",
                                                "data": "",
                                                "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                                "image_id": "",
                                                "url": ""
                                            }
                                        },
                                        "cyclist": {
                                            "attributes_with_score": {
                                                "additionalProp1": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp2": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp3": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                }
                                            },
                                            "quality": 0,
                                            "rectangle": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "track_id": ""
                                        },
                                        "event": {
                                            "event_id": "",
                                            "event_status": "[EVENT_START]EVENT_START/EVENT_CONTINUE",
                                            "rectangle": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "rule": {
                                                "direction": {
                                                    "x": 0,
                                                    "y": 0
                                                },
                                                "duration": "",
                                                "roi": {
                                                    "vertices": [
                                                        {
                                                            "x": 0,
                                                            "y": 0
                                                        }
                                                    ]
                                                },
                                                "rule_id": "",
                                                "type": "[EVENT_UNKNOWN]EVENT_UNKNOWN/EVENT_PEDESTRIAN_STAY/EVENT_PEDESTRIAN_HOVER/EVENT_PEDESTRIAN_CROSS_LINE/EVENT_PEDESTRIAN_INVADE/EVENT_VEHICLE_PARK"
                                            }
                                        },
                                        "face": {
                                            "angle": {
                                                "pitch": 0,
                                                "roll": 0,
                                                "yaw": 0
                                            },
                                            "attributes": {
                                                "additionalProp1": "",
                                                "additionalProp2": "",
                                                "additionalProp3": ""
                                            },
                                            "attributes_with_score": {
                                                "additionalProp1": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp2": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp3": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                }
                                            },
                                            "face_score": 0,
                                            "landmarks": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ],
                                            "quality": 0,
                                            "rectangle": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "track_id": ""
                                        },
                                        "human_powered_vehicle": {
                                            "attributes_with_score": {
                                                "additionalProp1": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp2": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp3": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                }
                                            },
                                            "quality": 0,
                                            "rectangle": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "track_id": ""
                                        },
                                        "object_id": "",
                                        "pedestrian": {
                                            "attributes_with_score": {
                                                "additionalProp1": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp2": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                },
                                                "additionalProp3": {
                                                    "category": "",
                                                    "roi": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                    "value": 0
                                                }
                                            },
                                            "quality": 0,
                                            "rectangle": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "track_id": ""
                                        },
                                        "portrait_image_location": {
                                            "panoramic_image_size": {
                                                "height": 0,
                                                "width": 0
                                            },
                                            "portrait_image_in_panoramic": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            },
                                            "portrait_in_panoramic": {
                                                "vertices": [
                                                    {
                                                        "x": 0,
                                                        "y": 0
                                                    }
                                                ]
                                            }
                                        },
                                        "scenario": {
                                            "objects": [
                                                {
                                                    "attributes_with_score": {
                                                        "additionalProp1": {
                                                            "category": "",
                                                            "roi": {
                                                                "vertices": [
                                                                    {
                                                                        "x": 0,
                                                                        "y": 0
                                                                    }
                                                                ]
                                                            },
                                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                            "value": 0
                                                        },
                                                        "additionalProp2": {
                                                            "category": "",
                                                            "roi": {
                                                                "vertices": [
                                                                    {
                                                                        "x": 0,
                                                                        "y": 0
                                                                    }
                                                                ]
                                                            },
                                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                            "value": 0
                                                        },
                                                        "additionalProp3": {
                                                            "category": "",
                                                            "roi": {
                                                                "vertices": [
                                                                    {
                                                                        "x": 0,
                                                                        "y": 0
                                                                    }
                                                                ]
                                                            },
                                                            "type": "[DISCRIMINATION]DISCRIMINATION/REGRESSION/CLASSIFICATION",
                                                            "value": 0
                                                        }
                                                    },
                                                    "quality": 0,
                                                    "rectangle": {
                                                        "vertices": [
                                                            {
                                                                "x": 0,
                                                                "y": 0
                                                            }
                                                        ]
                                                    },
                                                    "scenario_type": "[ST_UNKNOWN]ST_UNKNOWN/ST_STALL/ST_FIRE/ST_SLOGAN/ST_LANDSCAPE_LAMP/ST_CLUTTER/ST_ROAD_CLEAN/ST_SOIL/ST_GARBAGE/ST_SHARED_BICYCLE/ST_SHARED_BICYCLE_MISORDER/ST_INDOOR/ST_SMOKING"
                                                }
                                            ]
                                        },
                                        "type": "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                                    },
                                    "feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "images_orientation": "[ClockWiseUnknown]ClockWiseUnknown/ClockWise0/ClockWise90/ClockWise180/ClockWise270"
                                }
                            ],
                            "results": {
                                "code": 0,
                                "error": "",
                                "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                            }
                        }
                    ]
                }

        """
        intef = collections.interface("edge", "BatchDetectAndExtractAll2")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("face_type", face_type)
        return intef.request() if sendRequest else intef

    def BatchExtractWithBoundingPostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True):
        """  对批量的图片中指定区域的人脸提特征.
[EN] Extract features of Identi... """
        """  path: [post]/engine/image-process/face-extract/v1/batch_extract_with_bounding API """
        """  body: 
                {
                    "requests": [
                        {
                            "bounding": {
                                "vertices": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ]
                            },
                            "crop_image": false,
                            "image": {
                                "cache_url": "",
                                "data": "",
                                "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                "image_id": "",
                                "url": ""
                            }
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "align_score": 0,
                            "face_score": 0,
                            "feature": {
                                "blob": "",
                                "type": "",
                                "version": 0
                            }
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": "[OK]OK/SYSTEM_UNKNOWN_ERROR/SYSTEM_NETWORK_ERROR/SYSTEM_STORAGE_ERROR/SYSTEM_LICENSE_ERROR/DB_NOT_FOUND/DB_KEY_NOT_FOUND/DB_ALREADY_EXISTS/DB_KEY_ALREADY_EXISTS/FACE_NOT_FOUND_FIRST/FACE_NOT_FOUND_SECOND/FACE_NOT_FOUND/FACE_BAD_QUALITY/IMAGE_UNKNOWN_FILE_FORMAT/IMAGE_UNKNOWN_PIXEL_FORMAT/IMAGE_SIZE_TOO_SMALL/IMAGE_SIZE_TOO_LARGE/OBJECT_NOT_FOUND/OBJECT_BAD_QUALITY"
                        }
                    ]
                }

        """
        intef = collections.interface("edge", "BatchExtractWithBounding")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def CompareFeaturePostApi(self, one=None, other=None, loginToken=None, sendRequest=True, print_log=True):
        """  特征1：1比对.
[EN] One to one feature comparison. """
        """  path: [post]/engine/image-process/face-extract/v1/compare_feature API """
        """  body: 
                {
                    "one": {
                        "blob": "",
                        "type": "",
                        "version": 0
                    },
                    "other": {
                        "blob": "",
                        "type": "",
                        "version": 0
                    }
                }
        """
        """  resp:
                200():
                {
                    "score": 0
                }

        """
        intef = collections.interface("edge", "CompareFeature")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        intef.update_body("one", one)
        intef.update_body("other", other)
        return intef.request() if sendRequest else intef

    def GetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True):
        """  获取系统信息 [SINCE v2.2.0].
[EN] Get system info which ... """
        """  path: [get]/engine/image-process/face-extract/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "models_info": {
                        "additionalProp1": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": ""
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp2": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": ""
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp3": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": ""
                                }
                            ],
                            "status": ""
                        }
                    }
                }

        """
        intef = collections.interface("edge", "GetSystemInfo")
        intef.set_print_log(print_log)
        if loginToken:
            intef.set_headers(TOKEN_NAME, TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

