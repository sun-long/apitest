#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class RasmanagerSwaggerApi(BaseApi):
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

    def RasManager_CallbackAssignmentStatePostApi(self, states=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  内部接口，用于边缘上报 bot_assignment 的状态
route: prefix=, int... """
        """  path: [post]/v1/CallbackAssignmentState API """
        """  body: 
                {
                    "states": [
                        {
                            "assignment_id": "",
                            "elements": [
                                {
                                    "code": 0,
                                    "message": "",
                                    "meta": {},
                                    "state": "[AS_UNKNOWN]AS_UNKNOWN/AS_EL_PENDING/AS_EL_RUNNING/AS_SUCCEED/AS_FAILED/EL_TERMINATED"
                                }
                            ],
                            "state": "[AS_UNKNOWN]AS_UNKNOWN/AS_EL_PENDING/AS_EL_RUNNING/AS_SUCCEED/AS_FAILED/EL_TERMINATED"
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
                    },
                    "results": [
                        {
                            "code": 0,
                            "details": [
                                {
                                    "@type": ""
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("rasManager", "RasManager_CallbackAssignmentState")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("states", states)
        return intef.request() if sendRequest else intef

    def RasManager_CallbackDataCollectingTaskStatusPostApi(self, cluster_id=None, task_id=None, status=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CallbackDataCollectingTaskStatus 设置回流作业状态.
route: ... """
        """  path: [post]/v1/CallbackDataCollectingTaskStatus API """
        """  body: 
                {
                    "cluster_id": "",
                    "status": {
                        "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                        "state_message": ""
                    },
                    "task_id": ""
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
        intef = collections.interface("rasManager", "RasManager_CallbackDataCollectingTaskStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("cluster_id", cluster_id)
        intef.update_body("task_id", task_id)
        intef.update_body("status", status)
        return intef.request() if sendRequest else intef

    def RasManager_CountDevicesGetApi(self, spu_names=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CountDevices 返回 account 下的 device 总数.
route: prefi... """
        """  path: [get]/v1/CountDevices API """
        """  params: 
                参数名称：spu_names　类型：array　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "subscribe_total": 0,
                    "total": 0
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
        intef = collections.interface("rasManager", "RasManager_CountDevices")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("spu_names", spu_names)
        return intef.request() if sendRequest else intef

    def RasManager_CreateAssignmentPostApi(self, device_id=None, assignment_config=None, rotate_config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CreateAssignment 为指定的 device 创建 bot_assignment(推理能... """
        """  path: [post]/v1/CreateAssignment API """
        """  body: 
                {
                    "assignment_config": {},
                    "device_id": "",
                    "rotate_config": {
                        "retention": {
                            "day": 0
                        }
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "assignment": {
                        "account_id": "",
                        "assignment_config": {},
                        "assignment_id": "",
                        "created_at": "",
                        "device_id": "",
                        "elements": [
                            {
                                "code": 0,
                                "message": "",
                                "meta": {},
                                "state": "[AS_UNKNOWN]AS_UNKNOWN/AS_EL_PENDING/AS_EL_RUNNING/AS_SUCCEED/AS_FAILED/EL_TERMINATED"
                            }
                        ],
                        "rotate_config": {
                            "retention": {
                                "day": 0
                            }
                        },
                        "spu_name": "",
                        "state": "[AS_UNKNOWN]AS_UNKNOWN/AS_EL_PENDING/AS_EL_RUNNING/AS_SUCCEED/AS_FAILED/EL_TERMINATED",
                        "updated_at": ""
                    },
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
        intef = collections.interface("rasManager", "RasManager_CreateAssignment")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("assignment_config", assignment_config)
        intef.update_body("rotate_config", rotate_config)
        return intef.request() if sendRequest else intef

    def RasManager_CreateDataCollectingTaskPostApi(self, task=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CreateDataCollectingTask 发起回流作业.
route: prefix=dat... """
        """  path: [post]/v1/CreateDataCollectingTask API """
        """  body: 
                {
                    "task": {
                        "acl": [
                            {
                                "ad": "",
                                "expire_time": "",
                                "name": ""
                            }
                        ],
                        "auth_id": "",
                        "callback_url": "",
                        "data_type": "[Video]Video/Structural",
                        "desc": "",
                        "devices": [],
                        "event_filter": {
                            "key": "",
                            "operator": "[EQ]EQ/GT/GTE/LT/LTE/NE/IN/NIN",
                            "value": {}
                        },
                        "name": "",
                        "result_detail": {
                            "additionalProp1": {
                                "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                                "state_message": ""
                            },
                            "additionalProp2": {
                                "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                                "state_message": ""
                            },
                            "additionalProp3": {
                                "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                                "state_message": ""
                            }
                        },
                        "siphon_job_id": "",
                        "spu_name": "",
                        "status": {
                            "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                            "state_message": ""
                        },
                        "target_config": {
                            "ceph_config": {
                                "access_key": "",
                                "bucket": "",
                                "prefix": "",
                                "protocol": "",
                                "secret_key": ""
                            },
                            "cluster_name": "",
                            "lustre_config": {
                                "path": ""
                            },
                            "target_type": "[Ceph]Ceph/Lustre"
                        },
                        "task_id": "",
                        "time_config": {
                            "end_date": "",
                            "start_date": "",
                            "windows": [
                                {
                                    "end_time": "",
                                    "start_time": ""
                                }
                            ]
                        }
                    }
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
                    },
                    "success": false,
                    "task_id": ""
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
        intef = collections.interface("rasManager", "RasManager_CreateDataCollectingTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task", task)
        return intef.request() if sendRequest else intef

    def RasManager_DeleteAssignmentPostApi(self, device_id=None, spu_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteAssignment 移除 bot_assignment
route: prefix=r... """
        """  path: [post]/v1/DeleteAssignment API """
        """  body: 
                {
                    "device_id": "",
                    "spu_name": ""
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
        intef = collections.interface("rasManager", "RasManager_DeleteAssignment")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("spu_name", spu_name)
        return intef.request() if sendRequest else intef

    def RasManager_DeleteDataCollectingTaskPostApi(self, task_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteDataCollectingTask 根据task_id删除回流作业
route: pr... """
        """  path: [post]/v1/DeleteDataCollectingTask API """
        """  body: 
                {
                    "task_id": ""
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
        intef = collections.interface("rasManager", "RasManager_DeleteDataCollectingTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task_id", task_id)
        return intef.request() if sendRequest else intef

    def RasManager_DeleteDevicePostApi(self, device_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteDevice 删除设备信息. 同时校验设备是否有使用 ras 的资源, 如果有资源绑定关... """
        """  path: [post]/v1/DeleteDevice API """
        """  body: 
                {
                    "device_id": ""
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
        intef = collections.interface("rasManager", "RasManager_DeleteDevice")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        return intef.request() if sendRequest else intef

    def RasManager_GetAssignmentGetApi(self, device_id=None, spu_name=None, verbose=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetAssignment 获取 bot_assignment 的信息
route: prefix=... """
        """  path: [get]/v1/GetAssignment API """
        """  params: 
                参数名称：device_id　类型：string　描述：bot_assignment 应用在 device 上.
                参数名称：spu_name　类型：string　描述：对外不暴露. 内部调用时需要指定 spu_name
                参数名称：verbose　类型：boolean　描述：optional, 是否输出详细结果，如 elements 信息等，默认 false
        """
        """  resp:
                200(A successful response.):
                {
                    "assignment": {
                        "account_id": "",
                        "assignment_config": {},
                        "assignment_id": "",
                        "created_at": "",
                        "device_id": "",
                        "elements": [
                            {
                                "code": 0,
                                "message": "",
                                "meta": {},
                                "state": "[AS_UNKNOWN]AS_UNKNOWN/AS_EL_PENDING/AS_EL_RUNNING/AS_SUCCEED/AS_FAILED/EL_TERMINATED"
                            }
                        ],
                        "rotate_config": {
                            "retention": {
                                "day": 0
                            }
                        },
                        "spu_name": "",
                        "state": "[AS_UNKNOWN]AS_UNKNOWN/AS_EL_PENDING/AS_EL_RUNNING/AS_SUCCEED/AS_FAILED/EL_TERMINATED",
                        "updated_at": ""
                    },
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
        intef = collections.interface("rasManager", "RasManager_GetAssignment")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("device_id", device_id)
        intef.update_params("spu_name", spu_name)
        intef.update_params("verbose", verbose)
        return intef.request() if sendRequest else intef

    def RasManager_GetDataCollectingTaskGetApi(self, task_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetDataCollectingTask 根据task_id获取回流作业
route: prefi... """
        """  path: [get]/v1/GetDataCollectingTask API """
        """  params: 
                参数名称：task_id　类型：string　描述：nul
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
                    },
                    "task": {
                        "acl": [
                            {
                                "ad": "",
                                "expire_time": "",
                                "name": ""
                            }
                        ],
                        "auth_id": "",
                        "callback_url": "",
                        "data_type": "[Video]Video/Structural",
                        "desc": "",
                        "devices": [],
                        "event_filter": {
                            "key": "",
                            "operator": "[EQ]EQ/GT/GTE/LT/LTE/NE/IN/NIN",
                            "value": {}
                        },
                        "name": "",
                        "result_detail": {
                            "additionalProp1": {
                                "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                                "state_message": ""
                            },
                            "additionalProp2": {
                                "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                                "state_message": ""
                            },
                            "additionalProp3": {
                                "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                                "state_message": ""
                            }
                        },
                        "siphon_job_id": "",
                        "spu_name": "",
                        "status": {
                            "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                            "state_message": ""
                        },
                        "target_config": {
                            "ceph_config": {
                                "access_key": "",
                                "bucket": "",
                                "prefix": "",
                                "protocol": "",
                                "secret_key": ""
                            },
                            "cluster_name": "",
                            "lustre_config": {
                                "path": ""
                            },
                            "target_type": "[Ceph]Ceph/Lustre"
                        },
                        "task_id": "",
                        "time_config": {
                            "end_date": "",
                            "start_date": "",
                            "windows": [
                                {
                                    "end_time": "",
                                    "start_time": ""
                                }
                            ]
                        }
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
        intef = collections.interface("rasManager", "RasManager_GetDataCollectingTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("task_id", task_id)
        return intef.request() if sendRequest else intef

    def RasManager_GetDeviceDetailGetApi(self, device_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetDeviceDetail 获取单个设备信息, 包含设备绑定的 ras 信息.
route: p... """
        """  path: [get]/v1/GetDeviceDetail API """
        """  params: 
                参数名称：device_id　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "device_detail": {
                        "device": {
                            "cluster": {
                                "id": "",
                                "infra_cluster_id": "",
                                "l4_ingress": "",
                                "name": "",
                                "private_ingress": "",
                                "public_ingress": "",
                                "site_id": "",
                                "type": "[CT_UNKNOWN]CT_UNKNOWN/CT_CENTER/CT_EDGE"
                            },
                            "created_at": "",
                            "desc": "",
                            "devicekind_id": "",
                            "driver": {
                                "driver_id": "",
                                "enable": false,
                                "ingresses": [
                                    {
                                        "description": "",
                                        "information": {
                                            "rtmp": {
                                                "publish_url": "",
                                                "url": "",
                                                "verification": {
                                                    "method": "[NONE]NONE/TOKEN"
                                                }
                                            },
                                            "rtsp": {
                                                "protocol_type": "[TCP]TCP/UDP",
                                                "source_url": "",
                                                "url": "",
                                                "verification": {
                                                    "method": "[NONE]NONE/TOKEN"
                                                }
                                            },
                                            "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP"
                                        },
                                        "ingress_id": "",
                                        "name": "",
                                        "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                    }
                                ]
                            },
                            "extra_info": "",
                            "id": "",
                            "name": "",
                            "updated_at": "",
                            "verify": {
                                "method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER",
                                "user_info": {
                                    "ak": "",
                                    "sk": "",
                                    "user_id": ""
                                }
                            }
                        },
                        "device_kind": {
                            "created_at": "",
                            "desc": "",
                            "id": "",
                            "ingress_types": [
                                "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP"
                            ],
                            "iot_types": [
                                "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN"
                            ],
                            "name": "",
                            "updated_at": "",
                            "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                        },
                        "spus": [
                            {
                                "display_name": "",
                                "name": ""
                            }
                        ]
                    },
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
        intef = collections.interface("rasManager", "RasManager_GetDeviceDetail")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("device_id", device_id)
        return intef.request() if sendRequest else intef

    def RasManager_ListAccountDeviceSpusGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListAccountDeviceSpus 获取 account 下所有 device 订阅的 sp... """
        """  path: [get]/v1/ListAccountDeviceSpus API """
        """  params: 

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
                    },
                    "spus": [
                        {
                            "display_name": "",
                            "name": ""
                        }
                    ]
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
        intef = collections.interface("rasManager", "RasManager_ListAccountDeviceSpus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def RasManager_ListAllDeviceDetailsGetApi(self, spu_names=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListAllDeviceDetails 获取所有 account 的设备列表, 包含设备绑定的 r... """
        """  path: [get]/v1/ListAllDeviceDetails API """
        """  params: 
                参数名称：spu_names　类型：array　描述：[required] 至少传入一个spu_name.
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "device_detail": [
                        {
                            "device": {
                                "cluster": {
                                    "id": "",
                                    "infra_cluster_id": "",
                                    "l4_ingress": "",
                                    "name": "",
                                    "private_ingress": "",
                                    "public_ingress": "",
                                    "site_id": "",
                                    "type": "[CT_UNKNOWN]CT_UNKNOWN/CT_CENTER/CT_EDGE"
                                },
                                "created_at": "",
                                "desc": "",
                                "devicekind_id": "",
                                "driver": {
                                    "driver_id": "",
                                    "enable": false,
                                    "ingresses": [
                                        {
                                            "description": "",
                                            "information": {
                                                "rtmp": {
                                                    "publish_url": "",
                                                    "url": "",
                                                    "verification": {
                                                        "method": "[NONE]NONE/TOKEN"
                                                    }
                                                },
                                                "rtsp": {
                                                    "protocol_type": "[TCP]TCP/UDP",
                                                    "source_url": "",
                                                    "url": "",
                                                    "verification": {
                                                        "method": "[NONE]NONE/TOKEN"
                                                    }
                                                },
                                                "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP"
                                            },
                                            "ingress_id": "",
                                            "name": "",
                                            "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                        }
                                    ]
                                },
                                "extra_info": "",
                                "id": "",
                                "name": "",
                                "updated_at": "",
                                "verify": {
                                    "method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER",
                                    "user_info": {
                                        "ak": "",
                                        "sk": "",
                                        "user_id": ""
                                    }
                                }
                            },
                            "device_kind": {
                                "created_at": "",
                                "desc": "",
                                "id": "",
                                "ingress_types": [
                                    "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP"
                                ],
                                "iot_types": [
                                    "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN"
                                ],
                                "name": "",
                                "updated_at": "",
                                "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                            },
                            "spus": [
                                {
                                    "display_name": "",
                                    "name": ""
                                }
                            ]
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
        intef = collections.interface("rasManager", "RasManager_ListAllDeviceDetails")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("spu_names", spu_names)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def RasManager_ListAssignmentsGetApi(self, device_id=None, verbose=None, paging_offset=None, paging_limit=None, paging_total=None, spu_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListAssignments 获取 bot_assignment 的列表，支持以 bot_name... """
        """  path: [get]/v1/ListAssignments API """
        """  params: 
                参数名称：device_id　类型：string　描述：null
                参数名称：verbose　类型：boolean　描述：optional, 是否输出详细结果，如 elements 信息等，默认 false.
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：null
                参数名称：spu_name　类型：string　描述：optional, 不对外暴露。仅 rpc 调用时可
        """
        """  resp:
                200(A successful response.):
                {
                    "assignments": [
                        {
                            "account_id": "",
                            "assignment_config": {},
                            "assignment_id": "",
                            "created_at": "",
                            "device_id": "",
                            "elements": [
                                {
                                    "code": 0,
                                    "message": "",
                                    "meta": {},
                                    "state": "[AS_UNKNOWN]AS_UNKNOWN/AS_EL_PENDING/AS_EL_RUNNING/AS_SUCCEED/AS_FAILED/EL_TERMINATED"
                                }
                            ],
                            "rotate_config": {
                                "retention": {
                                    "day": 0
                                }
                            },
                            "spu_name": "",
                            "state": "[AS_UNKNOWN]AS_UNKNOWN/AS_EL_PENDING/AS_EL_RUNNING/AS_SUCCEED/AS_FAILED/EL_TERMINATED",
                            "updated_at": ""
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
        intef = collections.interface("rasManager", "RasManager_ListAssignments")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("device_id", device_id)
        intef.update_params("verbose", verbose)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        intef.update_params("spu_name", spu_name)
        return intef.request() if sendRequest else intef

    def RasManager_ListDataCollectingTaskGetApi(self, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListDataCollectingTask 获取回流作业列表
route: prefix=data... """
        """  path: [get]/v1/ListDataCollectingTask API """
        """  params: 
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
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
                    },
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    },
                    "tasks": [
                        {
                            "acl": [
                                {
                                    "ad": "",
                                    "expire_time": "",
                                    "name": ""
                                }
                            ],
                            "auth_id": "",
                            "callback_url": "",
                            "data_type": "[Video]Video/Structural",
                            "desc": "",
                            "devices": [],
                            "event_filter": {
                                "key": "",
                                "operator": "[EQ]EQ/GT/GTE/LT/LTE/NE/IN/NIN",
                                "value": {}
                            },
                            "name": "",
                            "result_detail": {
                                "additionalProp1": {
                                    "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                                    "state_message": ""
                                },
                                "additionalProp2": {
                                    "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                                    "state_message": ""
                                },
                                "additionalProp3": {
                                    "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                                    "state_message": ""
                                }
                            },
                            "siphon_job_id": "",
                            "spu_name": "",
                            "status": {
                                "state": "[Unset]Unset/Created/InProcess/UploadFailed/Uploaded/Submited/SubmitFailed/SyncFailed/Completed",
                                "state_message": ""
                            },
                            "target_config": {
                                "ceph_config": {
                                    "access_key": "",
                                    "bucket": "",
                                    "prefix": "",
                                    "protocol": "",
                                    "secret_key": ""
                                },
                                "cluster_name": "",
                                "lustre_config": {
                                    "path": ""
                                },
                                "target_type": "[Ceph]Ceph/Lustre"
                            },
                            "task_id": "",
                            "time_config": {
                                "end_date": "",
                                "start_date": "",
                                "windows": [
                                    {
                                        "end_time": "",
                                        "start_time": ""
                                    }
                                ]
                            }
                        }
                    ]
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
        intef = collections.interface("rasManager", "RasManager_ListDataCollectingTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def RasManager_ListDeviceDetailsGetApi(self, spu_names=None, filter_with_spu=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListDeviceDetails 获取设备列表, 包含设备绑定的 ras 信息.
route: p... """
        """  path: [get]/v1/ListDeviceDetails API """
        """  params: 
                参数名称：spu_names　类型：array　描述：null
                参数名称：filter_with_spu　类型：boolean　描述：仅展示绑定了 spu 的设备列表. 默认为 false
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "device_detail": [
                        {
                            "device": {
                                "cluster": {
                                    "id": "",
                                    "infra_cluster_id": "",
                                    "l4_ingress": "",
                                    "name": "",
                                    "private_ingress": "",
                                    "public_ingress": "",
                                    "site_id": "",
                                    "type": "[CT_UNKNOWN]CT_UNKNOWN/CT_CENTER/CT_EDGE"
                                },
                                "created_at": "",
                                "desc": "",
                                "devicekind_id": "",
                                "driver": {
                                    "driver_id": "",
                                    "enable": false,
                                    "ingresses": [
                                        {
                                            "description": "",
                                            "information": {
                                                "rtmp": {
                                                    "publish_url": "",
                                                    "url": "",
                                                    "verification": {
                                                        "method": "[NONE]NONE/TOKEN"
                                                    }
                                                },
                                                "rtsp": {
                                                    "protocol_type": "[TCP]TCP/UDP",
                                                    "source_url": "",
                                                    "url": "",
                                                    "verification": {
                                                        "method": "[NONE]NONE/TOKEN"
                                                    }
                                                },
                                                "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP"
                                            },
                                            "ingress_id": "",
                                            "name": "",
                                            "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                        }
                                    ]
                                },
                                "extra_info": "",
                                "id": "",
                                "name": "",
                                "updated_at": "",
                                "verify": {
                                    "method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER",
                                    "user_info": {
                                        "ak": "",
                                        "sk": "",
                                        "user_id": ""
                                    }
                                }
                            },
                            "device_kind": {
                                "created_at": "",
                                "desc": "",
                                "id": "",
                                "ingress_types": [
                                    "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP"
                                ],
                                "iot_types": [
                                    "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN"
                                ],
                                "name": "",
                                "updated_at": "",
                                "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                            },
                            "spus": [
                                {
                                    "display_name": "",
                                    "name": ""
                                }
                            ]
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
        intef = collections.interface("rasManager", "RasManager_ListDeviceDetails")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("spu_names", spu_names)
        intef.update_params("filter_with_spu", filter_with_spu)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def RasManager_UpdateAssignmentPostApi(self, device_id=None, assignment_config=None, rotate_config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  UpdateAssignment 更新 bot_assignment 的配置
route: pref... """
        """  path: [post]/v1/UpdateAssignment API """
        """  body: 
                {
                    "assignment_config": {},
                    "device_id": "",
                    "rotate_config": {
                        "retention": {
                            "day": 0
                        }
                    }
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
        intef = collections.interface("rasManager", "RasManager_UpdateAssignment")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("assignment_config", assignment_config)
        intef.update_body("rotate_config", rotate_config)
        return intef.request() if sendRequest else intef

    def RasManager_UpdateDevicePostApi(self, device_id=None, name=None, desc=None, driver=None, extra_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  UpdateDevice 更新设备信息. 同时检查设备是否已经绑定 ras 资源，如果有资源绑定关系... """
        """  path: [post]/v1/UpdateDevice API """
        """  body: 
                {
                    "desc": "",
                    "device_id": "",
                    "driver": {
                        "driver_id": "",
                        "enable": false,
                        "ingresses": [
                            {
                                "description": "",
                                "information": {
                                    "rtmp": {
                                        "publish_url": "",
                                        "url": "",
                                        "verification": {
                                            "method": "[NONE]NONE/TOKEN"
                                        }
                                    },
                                    "rtsp": {
                                        "protocol_type": "[TCP]TCP/UDP",
                                        "source_url": "",
                                        "url": "",
                                        "verification": {
                                            "method": "[NONE]NONE/TOKEN"
                                        }
                                    },
                                    "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP"
                                },
                                "ingress_id": "",
                                "name": "",
                                "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                            }
                        ]
                    },
                    "extra_info": "",
                    "name": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "device_detail": {
                        "device": {
                            "cluster": {
                                "id": "",
                                "infra_cluster_id": "",
                                "l4_ingress": "",
                                "name": "",
                                "private_ingress": "",
                                "public_ingress": "",
                                "site_id": "",
                                "type": "[CT_UNKNOWN]CT_UNKNOWN/CT_CENTER/CT_EDGE"
                            },
                            "created_at": "",
                            "desc": "",
                            "devicekind_id": "",
                            "driver": {
                                "driver_id": "",
                                "enable": false,
                                "ingresses": [
                                    {
                                        "description": "",
                                        "information": {
                                            "rtmp": {
                                                "publish_url": "",
                                                "url": "",
                                                "verification": {
                                                    "method": "[NONE]NONE/TOKEN"
                                                }
                                            },
                                            "rtsp": {
                                                "protocol_type": "[TCP]TCP/UDP",
                                                "source_url": "",
                                                "url": "",
                                                "verification": {
                                                    "method": "[NONE]NONE/TOKEN"
                                                }
                                            },
                                            "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP"
                                        },
                                        "ingress_id": "",
                                        "name": "",
                                        "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                    }
                                ]
                            },
                            "extra_info": "",
                            "id": "",
                            "name": "",
                            "updated_at": "",
                            "verify": {
                                "method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER",
                                "user_info": {
                                    "ak": "",
                                    "sk": "",
                                    "user_id": ""
                                }
                            }
                        },
                        "device_kind": {
                            "created_at": "",
                            "desc": "",
                            "id": "",
                            "ingress_types": [
                                "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP"
                            ],
                            "iot_types": [
                                "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN"
                            ],
                            "name": "",
                            "updated_at": "",
                            "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                        },
                        "spus": [
                            {
                                "display_name": "",
                                "name": ""
                            }
                        ]
                    },
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
        intef = collections.interface("rasManager", "RasManager_UpdateDevice")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("name", name)
        intef.update_body("desc", desc)
        intef.update_body("driver", driver)
        intef.update_body("extra_info", extra_info)
        return intef.request() if sendRequest else intef

