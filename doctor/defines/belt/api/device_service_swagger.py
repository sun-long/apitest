#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class DeviceSwaggerApi(BaseApi):
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

    def DeviceManagerCenter_BatchCreateDevicePostApi(self, request_header=None, devices=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  批量创建Device, devicekind仅提供devicekind_id, 上限50
route... """
        """  path: [post]/v1/BatchCreateDevices API """
        """  body: 
                {
                    "devices": [
                        {
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
                            "desc": "",
                            "devicekind_id": "",
                            "devicekind_name": "",
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
                                            "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                            "webrtc": {
                                                "url": ""
                                            }
                                        },
                                        "ingress_id": "",
                                        "name": "",
                                        "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                    }
                                ],
                                "iot": {
                                    "created_at": "",
                                    "device_sn": "",
                                    "information": {
                                        "symphony": {
                                            "extra_info": "",
                                            "registry_id": ""
                                        },
                                        "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                                    },
                                    "iot_id": "",
                                    "name": "",
                                    "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                                    "updated_at": ""
                                }
                            },
                            "extra_info": "",
                            "name": ""
                        }
                    ],
                    "request_header": {
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "devices": [
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
                                                "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                                "webrtc": {
                                                    "url": ""
                                                }
                                            },
                                            "ingress_id": "",
                                            "name": "",
                                            "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                        }
                                    ],
                                    "iot": {
                                        "created_at": "",
                                        "device_sn": "",
                                        "information": {
                                            "symphony": {
                                                "extra_info": "",
                                                "registry_id": ""
                                            },
                                            "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                                        },
                                        "iot_id": "",
                                        "name": "",
                                        "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                                        "updated_at": ""
                                    }
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
                            "error": {
                                "code": 0,
                                "details": [
                                    {
                                        "@type": ""
                                    }
                                ],
                                "message": ""
                            },
                            "response_header": {
                                "timestamp": "",
                                "trace": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            }
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
                    "failed": 0,
                    "passed": 0,
                    "response_header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
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
        intef = collections.interface("device", "DeviceManagerCenter_BatchCreateDevice")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("request_header", request_header)
        intef.update_body("devices", devices)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_BatchCreateDeviceByKindNamePostApi(self, request_header=None, devices=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  批量创建Device, devicekind仅提供devicekind_name, 上限50
rou... """
        """  path: [post]/v1/BatchCreateDevicesByKindName API """
        """  body: 
                {
                    "devices": [
                        {
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
                            "desc": "",
                            "devicekind_id": "",
                            "devicekind_name": "",
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
                                            "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                            "webrtc": {
                                                "url": ""
                                            }
                                        },
                                        "ingress_id": "",
                                        "name": "",
                                        "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                    }
                                ],
                                "iot": {
                                    "created_at": "",
                                    "device_sn": "",
                                    "information": {
                                        "symphony": {
                                            "extra_info": "",
                                            "registry_id": ""
                                        },
                                        "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                                    },
                                    "iot_id": "",
                                    "name": "",
                                    "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                                    "updated_at": ""
                                }
                            },
                            "extra_info": "",
                            "name": ""
                        }
                    ],
                    "request_header": {
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "devices": [
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
                                "devicekind": {
                                    "created_at": "",
                                    "desc": "",
                                    "id": "",
                                    "ingress_types": [
                                        "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC"
                                    ],
                                    "iot_type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY",
                                    "name": "",
                                    "updated_at": "",
                                    "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                                },
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
                                                "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                                "webrtc": {
                                                    "url": ""
                                                }
                                            },
                                            "ingress_id": "",
                                            "name": "",
                                            "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                        }
                                    ],
                                    "iot": {
                                        "created_at": "",
                                        "device_sn": "",
                                        "information": {
                                            "symphony": {
                                                "extra_info": "",
                                                "registry_id": ""
                                            },
                                            "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                                        },
                                        "iot_id": "",
                                        "name": "",
                                        "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                                        "updated_at": ""
                                    }
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
                            "error": {
                                "code": 0,
                                "details": [
                                    {
                                        "@type": ""
                                    }
                                ],
                                "message": ""
                            },
                            "response_header": {
                                "timestamp": "",
                                "trace": {
                                    "additionalProp1": "",
                                    "additionalProp2": "",
                                    "additionalProp3": ""
                                }
                            }
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
                    "failed": 0,
                    "passed": 0,
                    "response_header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
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
        intef = collections.interface("device", "DeviceManagerCenter_BatchCreateDeviceByKindName")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("request_header", request_header)
        intef.update_body("devices", devices)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_BindDevicePolicyGroupPostApi(self, request_header=None, device_id=None, group_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  添加设备和policy group的绑定,
route: prefix=, internal_pre... """
        """  path: [post]/v1/BindDevicePolicyGroup API """
        """  body: 
                {
                    "device_id": "",
                    "group_id": "",
                    "request_header": {
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
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
                    "response_header": {
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_BindDevicePolicyGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("request_header", request_header)
        intef.update_body("device_id", device_id)
        intef.update_body("group_id", group_id)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_CreateDevicePostApi(self, request_header=None, devicekind_id=None, name=None, desc=None, cluster=None, extra_info=None, driver=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建Device, 设备鉴权信息创建时不用指定，会在创建设备时自动创建鉴权信息并返回，并且之后不能修... """
        """  path: [post]/v1/CreateDevice API """
        """  body: 
                {
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
                                    "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                    "webrtc": {
                                        "url": ""
                                    }
                                },
                                "ingress_id": "",
                                "name": "",
                                "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                            }
                        ],
                        "iot": {
                            "created_at": "",
                            "device_sn": "",
                            "information": {
                                "symphony": {
                                    "extra_info": "",
                                    "registry_id": ""
                                },
                                "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                            },
                            "iot_id": "",
                            "name": "",
                            "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                            "updated_at": ""
                        }
                    },
                    "extra_info": "",
                    "name": "",
                    "request_header": {
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
        """
        """  resp:
                200(A successful response.):
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
                                        "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                        "webrtc": {
                                            "url": ""
                                        }
                                    },
                                    "ingress_id": "",
                                    "name": "",
                                    "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                }
                            ],
                            "iot": {
                                "created_at": "",
                                "device_sn": "",
                                "information": {
                                    "symphony": {
                                        "extra_info": "",
                                        "registry_id": ""
                                    },
                                    "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                                },
                                "iot_id": "",
                                "name": "",
                                "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                                "updated_at": ""
                            }
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
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "response_header": {
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_CreateDevice")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("request_header", request_header)
        intef.update_body("devicekind_id", devicekind_id)
        intef.update_body("name", name)
        intef.update_body("desc", desc)
        intef.update_body("cluster", cluster)
        intef.update_body("extra_info", extra_info)
        intef.update_body("driver", driver)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_CreateDeviceByKindNamePostApi(self, request_header=None, devicekind_name=None, name=None, desc=None, cluster=None, extra_info=None, driver=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建Device, 设备鉴权信息创建时不用指定，会在创建设备时自动创建鉴权信息并返回，并且之后不能修... """
        """  path: [post]/v1/CreateDeviceByKindName API """
        """  body: 
                {
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
                    "desc": "",
                    "devicekind_name": "",
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
                                    "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                    "webrtc": {
                                        "url": ""
                                    }
                                },
                                "ingress_id": "",
                                "name": "",
                                "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                            }
                        ],
                        "iot": {
                            "created_at": "",
                            "device_sn": "",
                            "information": {
                                "symphony": {
                                    "extra_info": "",
                                    "registry_id": ""
                                },
                                "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                            },
                            "iot_id": "",
                            "name": "",
                            "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                            "updated_at": ""
                        }
                    },
                    "extra_info": "",
                    "name": "",
                    "request_header": {
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
        """
        """  resp:
                200(A successful response.):
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
                        "devicekind": {
                            "created_at": "",
                            "desc": "",
                            "id": "",
                            "ingress_types": [
                                "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC"
                            ],
                            "iot_type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY",
                            "name": "",
                            "updated_at": "",
                            "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                        },
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
                                        "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                        "webrtc": {
                                            "url": ""
                                        }
                                    },
                                    "ingress_id": "",
                                    "name": "",
                                    "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                }
                            ],
                            "iot": {
                                "created_at": "",
                                "device_sn": "",
                                "information": {
                                    "symphony": {
                                        "extra_info": "",
                                        "registry_id": ""
                                    },
                                    "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                                },
                                "iot_id": "",
                                "name": "",
                                "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                                "updated_at": ""
                            }
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
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "response_header": {
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_CreateDeviceByKindName")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("request_header", request_header)
        intef.update_body("devicekind_name", devicekind_name)
        intef.update_body("name", name)
        intef.update_body("desc", desc)
        intef.update_body("cluster", cluster)
        intef.update_body("extra_info", extra_info)
        intef.update_body("driver", driver)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_CreateDeviceKindPostApi(self, name=None, desc=None, verify_method=None, ingress_types=None, iot_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建Devicekind,
route: prefix=, internal_prefix=devi... """
        """  path: [post]/v1/CreateDeviceKind API """
        """  body: 
                {
                    "desc": "",
                    "ingress_types": [
                        "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC"
                    ],
                    "iot_type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY",
                    "name": "",
                    "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "devicekind": {
                        "created_at": "",
                        "desc": "",
                        "id": "",
                        "ingress_types": [
                            "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC"
                        ],
                        "iot_type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY",
                        "name": "",
                        "updated_at": "",
                        "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                    },
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_CreateDeviceKind")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("desc", desc)
        intef.update_body("verify_method", verify_method)
        intef.update_body("ingress_types", ingress_types)
        intef.update_body("iot_type", iot_type)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_DeleteDevicePostApi(self, request_header=None, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除Device,
route: prefix=, internal_prefix=device, ... """
        """  path: [post]/v1/DeleteDevice API """
        """  body: 
                {
                    "id": "",
                    "request_header": {
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
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
                    "response_header": {
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_DeleteDevice")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("request_header", request_header)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_DeleteDeviceKindPostApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除Devicekind, device_kind下有device时，禁止删除,
route: p... """
        """  path: [post]/v1/DeleteDeviceKind API """
        """  body: 
                {
                    "id": ""
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_DeleteDeviceKind")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_GenRTMPAddressPostApi(self, device_id=None, ingress_id=None, duration=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  生成RTMP推流地址, 生成的地址过期时间为1小时, 超时后需要重新生成.
route: pref... """
        """  path: [post]/v1/GenRTMPAddress API """
        """  body: 
                {
                    "device_id": "",
                    "duration": "[TokenExpiration_UNSET]TokenExpiration_UNSET/HOURS_1/MINUTES_30/MINUTES_15/NO_EXPIRED",
                    "ingress_id": ""
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
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "publish_url": ""
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
        intef = collections.interface("device", "DeviceManagerCenter_GenRTMPAddress")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("ingress_id", ingress_id)
        intef.update_body("duration", duration)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_GetAccountIdGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据请求自带的Context获取account_id,
route: prefix=, intern... """
        """  path: [get]/v1/GetAccountId API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "account_id": "",
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
        intef = collections.interface("device", "DeviceManagerCenter_GetAccountId")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_GetAllDevicesGetApi(self, ids=None, names=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取所有account_id下的Device列表及总数，支持按device id, name批量分页... """
        """  path: [get]/v1/GetAllDevices API """
        """  params: 
                参数名称：ids　类型：array　描述：[可选]. 按id搜索，默认为空，获取全部, ids和names都存在时，按id搜索
                参数名称：names　类型：array　描述：[可选]. 按name搜索，默认为空，获取全部
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "devices": [
                        {
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
                                            "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                            "webrtc": {
                                                "url": ""
                                            }
                                        },
                                        "ingress_id": "",
                                        "name": "",
                                        "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                    }
                                ],
                                "iot": {
                                    "created_at": "",
                                    "device_sn": "",
                                    "information": {
                                        "symphony": {
                                            "extra_info": "",
                                            "registry_id": ""
                                        },
                                        "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                                    },
                                    "iot_id": "",
                                    "name": "",
                                    "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                                    "updated_at": ""
                                }
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
                    },
                    "response_header": {
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_GetAllDevices")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ids", ids)
        intef.update_params("names", names)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_GetDeviceGetApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据device_id获取Device,
route: prefix=, internal_pre... """
        """  path: [get]/v1/GetDevice API """
        """  params: 
                参数名称：id　类型：string　描述：[必须]. Device id, 长度范围[1, 64
        """
        """  resp:
                200(A successful response.):
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
                                        "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                        "webrtc": {
                                            "url": ""
                                        }
                                    },
                                    "ingress_id": "",
                                    "name": "",
                                    "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                }
                            ],
                            "iot": {
                                "created_at": "",
                                "device_sn": "",
                                "information": {
                                    "symphony": {
                                        "extra_info": "",
                                        "registry_id": ""
                                    },
                                    "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                                },
                                "iot_id": "",
                                "name": "",
                                "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                                "updated_at": ""
                            }
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
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "response_header": {
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_GetDevice")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_GetDeviceKindGetApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据device_kind_id获取DeviceKind,
route: prefix=, int... """
        """  path: [get]/v1/GetDeviceKind API """
        """  params: 
                参数名称：id　类型：string　描述：[必须]. Devicekind id, 长度范围[1, 64
        """
        """  resp:
                200(A successful response.):
                {
                    "devicekind": {
                        "created_at": "",
                        "desc": "",
                        "id": "",
                        "ingress_types": [
                            "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC"
                        ],
                        "iot_type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY",
                        "name": "",
                        "updated_at": "",
                        "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                    },
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_GetDeviceKind")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_GetDeviceKindsGetApi(self, ids=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取Devicekind列表,
route: prefix=, internal_prefix=d... """
        """  path: [get]/v1/GetDeviceKinds API """
        """  params: 
                参数名称：ids　类型：array　描述：[可选] 按id搜索, 默认为空，获取全部
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "devicekinds": [
                        {
                            "created_at": "",
                            "desc": "",
                            "id": "",
                            "ingress_types": [
                                "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC"
                            ],
                            "iot_type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY",
                            "name": "",
                            "updated_at": "",
                            "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_GetDeviceKinds")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ids", ids)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_GetDevicesGetApi(self, ids=None, names=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取Device列表及总数，支持按device id, name批量分页查询，默认分页设置: off... """
        """  path: [get]/v1/GetDevices API """
        """  params: 
                参数名称：ids　类型：array　描述：[可选]. 按id搜索，默认为空，获取全部, ids和names都存在时，按id搜索
                参数名称：names　类型：array　描述：[可选]. 按name搜索，默认为空，获取全部
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "devices": [
                        {
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
                                            "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                            "webrtc": {
                                                "url": ""
                                            }
                                        },
                                        "ingress_id": "",
                                        "name": "",
                                        "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                    }
                                ],
                                "iot": {
                                    "created_at": "",
                                    "device_sn": "",
                                    "information": {
                                        "symphony": {
                                            "extra_info": "",
                                            "registry_id": ""
                                        },
                                        "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                                    },
                                    "iot_id": "",
                                    "name": "",
                                    "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                                    "updated_at": ""
                                }
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
                    },
                    "response_header": {
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_GetDevices")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ids", ids)
        intef.update_params("names", names)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_GetIotIngressesGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取Iot接入配置
route: prefix=, internal_prefix=device, ... """
        """  path: [get]/v1/GetIotIngresses API """
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
                    "iot_ingress": [
                        {
                            "clients": [
                                {
                                    "grpc_client": {
                                        "address": "",
                                        "close_resolver": false,
                                        "metrics_disabled": false,
                                        "with_block": false
                                    },
                                    "http_client": {
                                        "ingress": "",
                                        "prefix": "",
                                        "schema": ""
                                    },
                                    "name": "",
                                    "register_callback_url": "",
                                    "status_callback_url": ""
                                }
                            ],
                            "name": "",
                            "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
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
        intef = collections.interface("device", "DeviceManagerCenter_GetIotIngresses")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_ListRegistrationGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  [internal] 获取边缘注册信息,
route: prefix=, internal_pre... """
        """  path: [get]/v1/ListRegistration API """
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
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "infos": [
                        {
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
                            "create_time": "",
                            "id": "",
                            "last_connected_time": "",
                            "online": false,
                            "version": ""
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
        intef = collections.interface("device", "DeviceManagerCenter_ListRegistration")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_RegisterPostApi(self, info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  [internal] 边缘向中心注册接口 """
        """  path: [post]/v1/Register API """
        """  body: 
                {
                    "info": {
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
                        "create_time": "",
                        "id": "",
                        "last_connected_time": "",
                        "online": false,
                        "version": ""
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_Register")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("info", info)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_SDPPublishPostApi(self, device_id=None, ingress_id=None, sdp=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  生成SDP服务端描述信息, 生成的SDP描述信息过期时间为30秒, 超时后需要重新生成.
rout... """
        """  path: [post]/v1/SDP/Publish API """
        """  body: 
                {
                    "device_id": "",
                    "ingress_id": "",
                    "sdp": "",
                    "type": "[OFFER]OFFER/ANSWER"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "device_id": "",
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "header": {
                        "timestamp": "",
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    },
                    "ingress_id": "",
                    "sdp": "",
                    "type": "[OFFER]OFFER/ANSWER"
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
        intef = collections.interface("device", "DeviceManagerCenter_SDPPublish")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("ingress_id", ingress_id)
        intef.update_body("sdp", sdp)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_UnbindDevicePolicyGroupPostApi(self, request_header=None, device_id=None, group_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  解绑设备和policy group的绑定,
route: prefix=, internal_pr... """
        """  path: [post]/v1/UnbindDevicePolicyGroup API """
        """  body: 
                {
                    "device_id": "",
                    "group_id": "",
                    "request_header": {
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
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
                    "response_header": {
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_UnbindDevicePolicyGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("request_header", request_header)
        intef.update_body("device_id", device_id)
        intef.update_body("group_id", group_id)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_UpdateDevicePostApi(self, request_header=None, id=None, name=None, desc=None, extra_info=None, driver=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新Device，鉴权信息, cluster信息不可修改,
route: prefix=, inte... """
        """  path: [post]/v1/UpdateDevice API """
        """  body: 
                {
                    "desc": "",
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
                                    "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                    "webrtc": {
                                        "url": ""
                                    }
                                },
                                "ingress_id": "",
                                "name": "",
                                "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                            }
                        ],
                        "iot": {
                            "created_at": "",
                            "device_sn": "",
                            "information": {
                                "symphony": {
                                    "extra_info": "",
                                    "registry_id": ""
                                },
                                "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                            },
                            "iot_id": "",
                            "name": "",
                            "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                            "updated_at": ""
                        }
                    },
                    "extra_info": "",
                    "id": "",
                    "name": "",
                    "request_header": {
                        "trace": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        }
                    }
                }
        """
        """  resp:
                200(A successful response.):
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
                                        "type": "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC",
                                        "webrtc": {
                                            "url": ""
                                        }
                                    },
                                    "ingress_id": "",
                                    "name": "",
                                    "status": "[INGRESS_STATUS_UNKNOWN]INGRESS_STATUS_UNKNOWN/AVAILABLE/UNAVALIABLE"
                                }
                            ],
                            "iot": {
                                "created_at": "",
                                "device_sn": "",
                                "information": {
                                    "symphony": {
                                        "extra_info": "",
                                        "registry_id": ""
                                    },
                                    "type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY"
                                },
                                "iot_id": "",
                                "name": "",
                                "status": "[IOT_STATUS_UNKNOWN]IOT_STATUS_UNKNOWN/IOT_STATUS_AVAILABLE/IOT_STATUS_UNAVAILABLE",
                                "updated_at": ""
                            }
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
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "response_header": {
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_UpdateDevice")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("request_header", request_header)
        intef.update_body("id", id)
        intef.update_body("name", name)
        intef.update_body("desc", desc)
        intef.update_body("extra_info", extra_info)
        intef.update_body("driver", driver)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_UpdateDeviceKindPostApi(self, id=None, name=None, desc=None, verify_method=None, ingress_types=None, iot_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新Devicekind, device_kind下有device时，禁止更新,
route: p... """
        """  path: [post]/v1/UpdateDeviceKind API """
        """  body: 
                {
                    "desc": "",
                    "id": "",
                    "ingress_types": [
                        "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC"
                    ],
                    "iot_type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY",
                    "name": "",
                    "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "devicekind": {
                        "created_at": "",
                        "desc": "",
                        "id": "",
                        "ingress_types": [
                            "[INGRESS_TYPE_UNKNOWN]INGRESS_TYPE_UNKNOWN/RTSP/RTMP/WEBRTC"
                        ],
                        "iot_type": "[IOT_TYPE_UNKNOWN]IOT_TYPE_UNKNOWN/SYMPHONY",
                        "name": "",
                        "updated_at": "",
                        "verify_method": "[UNKNOWN_METHOD]UNKNOWN_METHOD/USER"
                    },
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("device", "DeviceManagerCenter_UpdateDeviceKind")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("name", name)
        intef.update_body("desc", desc)
        intef.update_body("verify_method", verify_method)
        intef.update_body("ingress_types", ingress_types)
        intef.update_body("iot_type", iot_type)
        return intef.request() if sendRequest else intef

