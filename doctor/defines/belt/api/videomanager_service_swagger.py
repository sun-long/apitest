#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class VideomanagerSwaggerApi(BaseApi):
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

    def VideoManagerCenter_CancelRecordTaskPostApi(self, task_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  取消录播task
route: prefix=, internal_prefix=video, ac... """
        """  path: [post]/v1/CancelRecordTask API """
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
        intef = collections.interface("videoManager", "VideoManagerCenter_CancelRecordTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task_id", task_id)
        return intef.request() if sendRequest else intef

    def VideoManagerCenter_CreateRecordTaskPostApi(self, device_id=None, ingress_id=None, start_time=None, end_time=None, template=None, keep_days=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建录播task
route: prefix=, internal_prefix=video, ac... """
        """  path: [post]/v1/CreateRecordTask API """
        """  body: 
                {
                    "device_id": "",
                    "end_time": "",
                    "ingress_id": "",
                    "keep_days": 0,
                    "start_time": "",
                    "template": {
                        "audio_config": {
                            "config": {},
                            "use_origin": false
                        },
                        "format": "[RecordFileFormat_UNKNOWN]RecordFileFormat_UNKNOWN/MP4",
                        "video_config": {
                            "config": {},
                            "use_origin": false
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
                    "task": {
                        "created_at": "",
                        "device_id": "",
                        "end_time": "",
                        "id": "",
                        "ingress": {
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
                                "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                "webrtc": {
                                    "url": ""
                                }
                            },
                            "ingress_id": "",
                            "name": "",
                            "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVAILABLE"
                        },
                        "keep_days": 0,
                        "record_files": [
                            {
                                "created_at": "",
                                "object_key": "",
                                "status": "[FILE_UNKNOWN_STATUS]FILE_UNKNOWN_STATUS/FILE_RECORDING/FILE_RECORDED/FILE_UPLOADING/FILE_AVAILABLE/FILE_RETRYING/FILE_DELETED",
                                "updated_at": ""
                            }
                        ],
                        "start_time": "",
                        "status": "[UNKNOWN]UNKNOWN/NOT_START/INITING/RUNNING/CANCELED/FINISHED/FAILED/ERROR",
                        "template": {
                            "audio_config": {
                                "config": {},
                                "use_origin": false
                            },
                            "format": "[RecordFileFormat_UNKNOWN]RecordFileFormat_UNKNOWN/MP4",
                            "video_config": {
                                "config": {},
                                "use_origin": false
                            }
                        },
                        "updated_at": ""
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
        intef = collections.interface("videoManager", "VideoManagerCenter_CreateRecordTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("ingress_id", ingress_id)
        intef.update_body("start_time", start_time)
        intef.update_body("end_time", end_time)
        intef.update_body("template", template)
        intef.update_body("keep_days", keep_days)
        return intef.request() if sendRequest else intef

    def VideoManagerCenter_CreateTaskPostApi(self, device_id=None, ingress_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建task
route: prefix=, internal_prefix=video, acti... """
        """  path: [post]/v1/CreateTask API """
        """  body: 
                {
                    "device_id": "",
                    "ingress_ids": []
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
                    "task": {
                        "created_at": "",
                        "device_id": "",
                        "enable": false,
                        "id": "",
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
                                    "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                    "webrtc": {
                                        "url": ""
                                    }
                                },
                                "ingress_id": "",
                                "name": "",
                                "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVAILABLE"
                            }
                        ],
                        "metrics": {
                            "current_traffic": "",
                            "historical_traffic": "",
                            "reported_traffic": ""
                        },
                        "online_num": "",
                        "updated_at": ""
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
        intef = collections.interface("videoManager", "VideoManagerCenter_CreateTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("ingress_ids", ingress_ids)
        return intef.request() if sendRequest else intef

    def VideoManagerCenter_DeleteTaskPostApi(self, task_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除task
route: prefix=, internal_prefix=video, acti... """
        """  path: [post]/v1/DeleteTask API """
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
        intef = collections.interface("videoManager", "VideoManagerCenter_DeleteTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task_id", task_id)
        return intef.request() if sendRequest else intef

    def VideoManagerCenter_GeneratePlayAddressPostApi(self, task_id=None, protocol=None, duration=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  生成播放地址
route: prefix=, internal_prefix=video, acti... """
        """  path: [post]/v1/GeneratePlayAddress API """
        """  body: 
                {
                    "duration": "[TokenExpiration_UNSET]TokenExpiration_UNSET/HOURS_1/MINUTES_30/MINUTES_15/NO_EXPIRED",
                    "protocol": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
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
                    },
                    "url": ""
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
        intef = collections.interface("videoManager", "VideoManagerCenter_GeneratePlayAddress")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task_id", task_id)
        intef.update_body("protocol", protocol)
        intef.update_body("duration", duration)
        return intef.request() if sendRequest else intef

    def VideoManagerCenter_GetRecordTasksGetApi(self, task_ids=None, device_ids=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取录播task列表
route: prefix=, internal_prefix=video, ... """
        """  path: [get]/v1/GetRecordTasks API """
        """  params: 
                参数名称：task_ids　类型：array　描述：[可选] 按id搜索, 默认为空
                参数名称：device_ids　类型：array　描述：[可选] 按task对应的device_id搜索，默认为空,不对外暴露，仅rpc调用时可传
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
                            "created_at": "",
                            "device_id": "",
                            "end_time": "",
                            "id": "",
                            "ingress": {
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
                                    "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                    "webrtc": {
                                        "url": ""
                                    }
                                },
                                "ingress_id": "",
                                "name": "",
                                "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVAILABLE"
                            },
                            "keep_days": 0,
                            "record_files": [
                                {
                                    "created_at": "",
                                    "object_key": "",
                                    "status": "[FILE_UNKNOWN_STATUS]FILE_UNKNOWN_STATUS/FILE_RECORDING/FILE_RECORDED/FILE_UPLOADING/FILE_AVAILABLE/FILE_RETRYING/FILE_DELETED",
                                    "updated_at": ""
                                }
                            ],
                            "start_time": "",
                            "status": "[UNKNOWN]UNKNOWN/NOT_START/INITING/RUNNING/CANCELED/FINISHED/FAILED/ERROR",
                            "template": {
                                "audio_config": {
                                    "config": {},
                                    "use_origin": false
                                },
                                "format": "[RecordFileFormat_UNKNOWN]RecordFileFormat_UNKNOWN/MP4",
                                "video_config": {
                                    "config": {},
                                    "use_origin": false
                                }
                            },
                            "updated_at": ""
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
        intef = collections.interface("videoManager", "VideoManagerCenter_GetRecordTasks")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("task_ids", task_ids)
        intef.update_params("device_ids", device_ids)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def VideoManagerCenter_GetTasksGetApi(self, task_ids=None, device_ids=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取task列表
route: prefix=, internal_prefix=video, ac... """
        """  path: [get]/v1/GetTasks API """
        """  params: 
                参数名称：task_ids　类型：array　描述：[可选] 按id搜索, 默认为空
                参数名称：device_ids　类型：array　描述：[可选] 按task对应的device_id搜索，默认为空,不对外暴露，仅rpc调用时可传
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
                            "created_at": "",
                            "device_id": "",
                            "enable": false,
                            "id": "",
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
                                        "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                        "webrtc": {
                                            "url": ""
                                        }
                                    },
                                    "ingress_id": "",
                                    "name": "",
                                    "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVAILABLE"
                                }
                            ],
                            "metrics": {
                                "current_traffic": "",
                                "historical_traffic": "",
                                "reported_traffic": ""
                            },
                            "online_num": "",
                            "updated_at": ""
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
        intef = collections.interface("videoManager", "VideoManagerCenter_GetTasks")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("task_ids", task_ids)
        intef.update_params("device_ids", device_ids)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

