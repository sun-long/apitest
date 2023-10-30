#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class IdsFaceServiceSwaggerSwaggerApi(BaseApi):
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

    def FaceService_CompareImagePostApi(self, image=None, base_image=None, auto_rotate=None, min_quality_level=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  人脸 1:1 比对接口, 输入两张图片, 进行特征比对.
route prefix=ids inte... """
        """  path: [post]/v1/face/compare_image API """
        """  body: 
                {
                    "auto_rotate": false,
                    "base_image": "",
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/RSA/SM2",
                        "data": "",
                        "encrypted_fields": [],
                        "iv": "",
                        "version": 0
                    },
                    "image": "",
                    "min_quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/LOW/NORMAL/HIGH"
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
                    "feature_version": 0,
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
        intef = collections.interface("ids-face-service.swagger", "FaceService_CompareImage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("base_image", base_image)
        intef.update_body("auto_rotate", auto_rotate)
        intef.update_body("min_quality_level", min_quality_level)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def FaceService_DetectLivenessPostApi(self, image=None, min_quality_level=None, disable_defake=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  提供图片静默活体检测.
route prefix=ids internal_prefix=ids a... """
        """  path: [post]/v1/face/detect_liveness API """
        """  body: 
                {
                    "disable_defake": false,
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/RSA/SM2",
                        "data": "",
                        "encrypted_fields": [],
                        "iv": "",
                        "version": 0
                    },
                    "image": "",
                    "min_quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/LOW/NORMAL/HIGH"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "defake_score": 0,
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "is_liveness": false,
                    "liveness_attack_type": "[LIVENESS_ATTACK_TYPE_NONE]LIVENESS_ATTACK_TYPE_NONE/PHOTO/SCREEN_SHOT/MASK_PAPER/MASK_3D/HEAD_MODEL_3D/FACE_REPLACE_AI/ADVERSARIAL_ATTACK",
                    "liveness_score": 0,
                    "quality_items": [
                        {
                            "quality_type": "[QUALITY_TYPE_NONE]QUALITY_TYPE_NONE/LIGHT_DARK/LIGHT_BRIGHT/BLUR/GRAY/OCCLUSION_FORHEAD/OCCLUSION_GLASSES/OCCLUSION_RESPIRATOR/OCCLUSION_OTHERS",
                            "score": 0
                        }
                    ],
                    "quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/LOW/NORMAL/HIGH"
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
        intef = collections.interface("ids-face-service.swagger", "FaceService_DetectLiveness")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("min_quality_level", min_quality_level)
        intef.update_body("disable_defake", disable_defake)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

