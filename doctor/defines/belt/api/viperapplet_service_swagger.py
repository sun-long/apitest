#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class ViperappletSwaggerApi(BaseApi):
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

    def BatchProcessPostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  批量图像处理 [EXPERIMENTAL].
[EN] Batch image processing... """
        """  path: [post]/v1/batch_process API """
        """  body: 
                {
                    "requests": [
                        {
                            "config": {
                                "type_url": "",
                                "value": ""
                            },
                            "images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                                    "image_id": "",
                                    "url": ""
                                }
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "response": {
                                "type_url": "",
                                "value": ""
                            },
                            "response_items": [
                                {
                                    "type_url": "",
                                    "value": ""
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
        intef = collections.interface("viperApplet", "BatchProcess")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def GetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取系统信息 [EXPERIMENTAL].
[EN] Get system info [EXPER... """
        """  path: [get]/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "app_name": "",
                    "app_version": 0,
                    "load": {
                        "decode_rate": "",
                        "failed_count": "",
                        "max_decode_rate": "",
                        "success_count": ""
                    },
                    "models_info": {
                        "additionalProp1": {
                            "err_msg": "",
                            "name": "",
                            "oid": "",
                            "path": ""
                        },
                        "additionalProp2": {
                            "err_msg": "",
                            "name": "",
                            "oid": "",
                            "path": ""
                        },
                        "additionalProp3": {
                            "err_msg": "",
                            "name": "",
                            "oid": "",
                            "path": ""
                        }
                    }
                }

        """
        intef = collections.interface("viperApplet", "GetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

