#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class DeviceiotcenterSwaggerApi(BaseApi):
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

    def DeviceIotCenter_OtaUpgradeBasePostApi(self, device_id=None, cmd=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ota基础升级
route: prefix=, internal_prefix=device, ac... """
        """  path: [post]/v1/OtaUpgradeBase API """
        """  body: 
                {
                    "cmd": "",
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
        intef = collections.interface("deviceIotCenter", "DeviceIotCenter_OtaUpgradeBase")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("cmd", cmd)
        return intef.request() if sendRequest else intef

    def DeviceIotCenter_PushRtcLivePostApi(self, device_id=None, ingress_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  摄像头Rtc推流
route: prefix=, internal_prefix=device, a... """
        """  path: [post]/v1/PushRtcLive API """
        """  body: 
                {
                    "device_id": "",
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
        intef = collections.interface("deviceIotCenter", "DeviceIotCenter_PushRtcLive")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("ingress_id", ingress_id)
        return intef.request() if sendRequest else intef

    def DeviceIotCenter_PushRTMPLivePostApi(self, device_id=None, url=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  摄像头Rtpm推流
route: prefix=, internal_prefix=device, ... """
        """  path: [post]/v1/PushRTMPLive API """
        """  body: 
                {
                    "device_id": "",
                    "url": ""
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
        intef = collections.interface("deviceIotCenter", "DeviceIotCenter_PushRTMPLive")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("url", url)
        return intef.request() if sendRequest else intef

    def DeviceIotCenter_SetIpcConfigPostApi(self, device_id=None, config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ipc配置下发
route: prefix=, internal_prefix=device, ac... """
        """  path: [post]/v1/SetIpcConfig API """
        """  body: 
                {
                    "config": "",
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
        intef = collections.interface("deviceIotCenter", "DeviceIotCenter_SetIpcConfig")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("config", config)
        return intef.request() if sendRequest else intef

    def DeviceIotCenter_StartCameraPTZPostApi(self, device_id=None, id=None, PTZ=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  摄像头开始PTZ
route: prefix=, internal_prefix=device, a... """
        """  path: [post]/v1/StartCameraPTZ API """
        """  body: 
                {
                    "PTZ": {
                        "Pan": 0,
                        "Tilt": 0,
                        "Zoom": 0
                    },
                    "device_id": "",
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
        intef = collections.interface("deviceIotCenter", "DeviceIotCenter_StartCameraPTZ")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("id", id)
        intef.update_body("PTZ", PTZ)
        return intef.request() if sendRequest else intef

    def DeviceIotCenter_StartRtcAudioPostApi(self, device_id=None, url=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  摄像头启动Rtc音频
route: prefix=, internal_prefix=device,... """
        """  path: [post]/v1/StartRtcAudio API """
        """  body: 
                {
                    "device_id": "",
                    "url": ""
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
        intef = collections.interface("deviceIotCenter", "DeviceIotCenter_StartRtcAudio")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("url", url)
        return intef.request() if sendRequest else intef

    def DeviceIotCenter_StopCameraPTZPostApi(self, device_id=None, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  摄像头停止PTZ
route: prefix=, internal_prefix=device, a... """
        """  path: [post]/v1/StopCameraPTZ API """
        """  body: 
                {
                    "device_id": "",
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
        intef = collections.interface("deviceIotCenter", "DeviceIotCenter_StopCameraPTZ")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def DeviceIotCenter_StopRtcAudioPostApi(self, device_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  摄像头停止Rtc音频
route: prefix=, internal_prefix=device,... """
        """  path: [post]/v1/StopRtcAudio API """
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
        intef = collections.interface("deviceIotCenter", "DeviceIotCenter_StopRtcAudio")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        return intef.request() if sendRequest else intef

    def DeviceIotCenter_StopRtcLivePostApi(self, device_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  摄像头停止Rtc推流
route: prefix=, internal_prefix=device,... """
        """  path: [post]/v1/StopRtcLive API """
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
        intef = collections.interface("deviceIotCenter", "DeviceIotCenter_StopRtcLive")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        return intef.request() if sendRequest else intef

    def DeviceIotCenter_StopRTMPLivePostApi(self, device_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  摄像头停止Rtmp推流
route: prefix=, internal_prefix=device... """
        """  path: [post]/v1/StopRTMPLive API """
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
        intef = collections.interface("deviceIotCenter", "DeviceIotCenter_StopRTMPLive")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        return intef.request() if sendRequest else intef

