#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class WatermarkSwaggerApi(BaseApi):
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

    def DataSecurityService_SignImagePostApi(self, image=None, watermark=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  图片数字水印签名.
route prefix=ids internal_prefix=ids act... """
        """  path: [post]/v1/watermark/sign_image API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": "",
                    "watermark": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
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
                    "image": ""
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
        intef = collections.interface("watermark", "DataSecurityService_SignImage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("watermark", watermark)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def DataSecurityService_VerifyImagePostApi(self, image=None, watermark=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  图片数字水印验签.
route prefix=ids internal_prefix=ids act... """
        """  path: [post]/v1/watermark/verify_image API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": "",
                    "watermark": ""
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
                    "is_matched": false,
                    "score": 0
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
        intef = collections.interface("watermark", "DataSecurityService_VerifyImage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("watermark", watermark)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

