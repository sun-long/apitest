#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class ViperocrSwaggerApi(BaseApi):
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

    def BatchCustomTemplatePostApi(self, type=None, images=None, template_data=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  对批量的图片中的文字进行用户自定义模板检测识别.  [INTERNAL] [EXPERIMENTAL... """
        """  path: [post]/v1/batch_custom_template_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "template_data": "",
                    "type": "[UNKNOWN_CUSTOM_TEMPLATE_TYPE]UNKNOWN_CUSTOM_TEMPLATE_TYPE/OCR_CUSTOM_TEMPLATE/OCR_CUSTOM_TABLE/OCR_CUSTOM_LAYOUT/OCR_TABLE_MATCH/OCR_TEMPLATE_EXTRACTION/OCR_TEMPLATE_ADAPTIVE/OCR_SELF_TRAINING"
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {
                                        "columns": 0,
                                        "data": [],
                                        "order": "[ROW_MAJOR]ROW_MAJOR/COLUMN_MAJOR",
                                        "rows": 0
                                    },
                                    "textline": {
                                        "cell_position": {
                                            "bottom_right_col": 0,
                                            "bottom_right_row": 0,
                                            "top_left_col": 0,
                                            "top_left_row": 0
                                        },
                                        "chars": [
                                            {
                                                "pos": 0,
                                                "score": 0
                                            }
                                        ],
                                        "childs": [
                                            "killMe"
                                        ],
                                        "content": "",
                                        "multiline": false,
                                        "name": "",
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ],
                                        "score": 0,
                                        "valid": false
                                    },
                                    "type": ""
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
        intef = collections.interface("viperOcr", "BatchCustomTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("type", type)
        intef.update_body("images", images)
        intef.update_body("template_data", template_data)
        return intef.request() if sendRequest else intef

    def BatchPlainTextPostApi(self, type=None, region_type=None, images=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  对批量的图片中的纯文本进行检测识别.  [SINCE v3.0.0].
[EN] Detection... """
        """  path: [post]/v1/batch_plaintext_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "region_type": "[UNKNOWN_REGION]UNKNOWN_REGION/CHINA/UK/HK/MACAO/JP/KR/ES/RUS",
                    "type": "[UNKNOWN_PLAIN_TEXT_TYPE]UNKNOWN_PLAIN_TEXT_TYPE/OCR_GENERAL_SCENE/OCR_GENERAL_HAND_WRITING/OCR_GENERAL_PRINT/OCR_PRE_IDENTIFY_GENERAL/OCR_GENERAL_TABLE/OCR_GENERAL_TABLE_WITHOUT_FORMLINE"
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {
                                        "columns": 0,
                                        "data": [],
                                        "order": "[ROW_MAJOR]ROW_MAJOR/COLUMN_MAJOR",
                                        "rows": 0
                                    },
                                    "textline": {
                                        "cell_position": {
                                            "bottom_right_col": 0,
                                            "bottom_right_row": 0,
                                            "top_left_col": 0,
                                            "top_left_row": 0
                                        },
                                        "chars": [
                                            {
                                                "pos": 0,
                                                "score": 0
                                            }
                                        ],
                                        "childs": [
                                            "killMe"
                                        ],
                                        "content": "",
                                        "multiline": false,
                                        "name": "",
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ],
                                        "score": 0,
                                        "valid": false
                                    },
                                    "type": ""
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
        intef = collections.interface("viperOcr", "BatchPlainText")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("type", type)
        intef.update_body("region_type", region_type)
        intef.update_body("images", images)
        return intef.request() if sendRequest else intef

    def BatchSpecialTemplatePostApi(self, type=None, images=None, template_db_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  对批量的图片进行模板检测识别, 适用于特殊模板类型.  [SINCE v3.0.0].
[EN] O... """
        """  path: [post]/v1/batch_special_template_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "template_db_ids": [],
                    "type": "[UNKNOWN_SPECIAL_TEMPLATE_TYPE]UNKNOWN_SPECIAL_TEMPLATE_TYPE/OCR_DOC_RETRIEVE/OCR_PRE_IDENTIFY_TABLE/OCR_OBJECT_DETECTION/OCR_MIXED_TEMPLATE"
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {
                                        "columns": 0,
                                        "data": [],
                                        "order": "[ROW_MAJOR]ROW_MAJOR/COLUMN_MAJOR",
                                        "rows": 0
                                    },
                                    "textline": {
                                        "cell_position": {
                                            "bottom_right_col": 0,
                                            "bottom_right_row": 0,
                                            "top_left_col": 0,
                                            "top_left_row": 0
                                        },
                                        "chars": [
                                            {
                                                "pos": 0,
                                                "score": 0
                                            }
                                        ],
                                        "childs": [
                                            "killMe"
                                        ],
                                        "content": "",
                                        "multiline": false,
                                        "name": "",
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ],
                                        "score": 0,
                                        "valid": false
                                    },
                                    "type": ""
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
        intef = collections.interface("viperOcr", "BatchSpecialTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("type", type)
        intef.update_body("images", images)
        intef.update_body("template_db_ids", template_db_ids)
        return intef.request() if sendRequest else intef

    def BatchTemplatePostApi(self, region_type=None, type=None, images=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  对批量的图片中的文字进行模板检测识别, 需要指定模板的区域信息.  [SINCE v3.0.0].
... """
        """  path: [post]/v1/batch_template_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": "[IMAGE_UNKNOWN]IMAGE_UNKNOWN/IMAGE_JPEG/IMAGE_PNG/IMAGE_BMP/IMAGE_TIFF/IMAGE_GIF",
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "region_type": "[UNKNOWN_REGION]UNKNOWN_REGION/CHINA/UK/HK/MACAO/JP/KR/ES/RUS",
                    "type": ""
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {
                                        "columns": 0,
                                        "data": [],
                                        "order": "[ROW_MAJOR]ROW_MAJOR/COLUMN_MAJOR",
                                        "rows": 0
                                    },
                                    "textline": {
                                        "cell_position": {
                                            "bottom_right_col": 0,
                                            "bottom_right_row": 0,
                                            "top_left_col": 0,
                                            "top_left_row": 0
                                        },
                                        "chars": [
                                            {
                                                "pos": 0,
                                                "score": 0
                                            }
                                        ],
                                        "childs": [
                                            "killMe"
                                        ],
                                        "content": "",
                                        "multiline": false,
                                        "name": "",
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ],
                                        "score": 0,
                                        "valid": false
                                    },
                                    "type": ""
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
        intef = collections.interface("viperOcr", "BatchTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("region_type", region_type)
        intef.update_body("type", type)
        intef.update_body("images", images)
        return intef.request() if sendRequest else intef

    def GetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取系统信息. [SINCE v3.0.0].
[EN] Get system info which... """
        """  path: [get]/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "custom_template": [],
                    "models_info": {
                        "additionalProp1": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
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
                                    "path": "",
                                    "type": "",
                                    "version": 0
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
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        }
                    },
                    "region_info": {
                        "additionalProp1": {
                            "plain_text": [],
                            "template": []
                        },
                        "additionalProp2": {
                            "plain_text": [],
                            "template": []
                        },
                        "additionalProp3": {
                            "plain_text": [],
                            "template": []
                        }
                    },
                    "special_template": []
                }

        """
        intef = collections.interface("viperOcr", "GetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

