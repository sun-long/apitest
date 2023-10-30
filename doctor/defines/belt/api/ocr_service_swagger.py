#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class OcrSwaggerApi(BaseApi):
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

    def OCRService_H5OCRIDCardPostApi(self, front_image=None, back_image=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  检测识别图片中的身份证, 仅限H5调用[INTERNAL].
route prefix=ids in... """
        """  path: [post]/v1/h5/ocr/idcard API """
        """  body: 
                {
                    "back_image": "",
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "front_image": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "detailed_info": {
                        "detect_details": {
                            "additionalProp1": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp2": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp3": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            }
                        },
                        "has_invalid_field": false
                    },
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
                    "idcard": {
                        "address": "",
                        "authority": "",
                        "back_image": "",
                        "birth_date": "",
                        "expiry_date": "",
                        "front_image": "",
                        "idcard_source": "[ID_CARD_SOURCE_NONE]ID_CARD_SOURCE_NONE/ORIGIN/PHOTO_COPY/PS/REVERSION/TEMPORARY/ID_CARD_SOURCE_OTHER",
                        "image": "",
                        "issue_date": "",
                        "name": "",
                        "nation": "",
                        "number": "",
                        "sex": "",
                        "side": "[AUTO]AUTO/FRONT/BACK"
                    },
                    "quality_items": [
                        {
                            "quality_type": "[QUALITY_TYPE_NONE]QUALITY_TYPE_NONE/OCCLUSION/LIGHT_BRIGHT/LIGHT_DARK/BLUR/CROPPED/ID_CARD_QUALITY_OTHER",
                            "score": 0
                        }
                    ],
                    "quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/EXTREMELY_LOW/LOW/NORMAL/HIGH",
                    "roi": {
                        "vertices": [
                            {
                                "x": 0,
                                "y": 0
                            }
                        ]
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
        intef = collections.interface("ocr", "OCRService_H5OCRIDCard")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("front_image", front_image)
        intef.update_body("back_image", back_image)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def OCRService_OCRBankcardPostApi(self, image=None, encrypt_info=None, session_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  对图片中的文字进行模板检测识别.
route prefix=ids internal_prefix=... """
        """  path: [post]/v1/ocr/bankcard API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": "",
                    "session_id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "bankcard": {
                        "bank_id": "",
                        "bank_name": "",
                        "card_name": "",
                        "card_number": "",
                        "card_type": "",
                        "image": ""
                    },
                    "detailed_info": {
                        "detect_details": {
                            "additionalProp1": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp2": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp3": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            }
                        },
                        "has_invalid_field": false
                    },
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
        intef = collections.interface("ocr", "OCRService_OCRBankcard")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("encrypt_info", encrypt_info)
        intef.update_body("session_id", session_id)
        return intef.request() if sendRequest else intef

    def OCRService_OCRBusinessLicensePostApi(self, image=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  营业执照识别.
route prefix=ids internal_prefix=ids actio... """
        """  path: [post]/v1/ocr/business_license API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "business_license": {
                        "address": "",
                        "artificial_person": "",
                        "business_scope": "",
                        "capital": "",
                        "code": "",
                        "composition": "",
                        "name": "",
                        "operation_period": "",
                        "register_date": "",
                        "registration_authority_seal": "",
                        "serial_number": "",
                        "type": ""
                    },
                    "detailed_info": {
                        "detect_details": {
                            "additionalProp1": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp2": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp3": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            }
                        },
                        "has_invalid_field": false
                    },
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
        intef = collections.interface("ocr", "OCRService_OCRBusinessLicense")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def OCRService_OCRCarPlatePostApi(self, image=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  检测识别图片中的车牌号.
route prefix=ids internal_prefix=ids ... """
        """  path: [post]/v1/ocr/car_plate API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "car_plates": [
                        {
                            "color": "[COLOR_TYPE_NONE]COLOR_TYPE_NONE/BLACK/WHITE/BLUE/YELLOW/GREEN/YELLOW_GREEN",
                            "confidence": 0,
                            "is_valid": false,
                            "number": "",
                            "roi": {
                                "vertices": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ]
                            }
                        }
                    ],
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
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
        intef = collections.interface("ocr", "OCRService_OCRCarPlate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def OCRService_CreateSessionPostApi(self, session=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建一个检测会话.
route prefix=ids internal_prefix=ids act... """
        """  path: [post]/v1/ocr/create_session API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "session": {
                        "idcard_min_quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/EXTREMELY_LOW/LOW/NORMAL/HIGH",
                        "session_type": "[IDENTITY_VERIFICATION]IDENTITY_VERIFICATION/LIVENESS/H5_LIVENESS/IDCARD_SCAN/BANKCARD_SCAN",
                        "uuid": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "biz_token": "",
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "session_id": ""
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
        intef = collections.interface("ocr", "OCRService_CreateSession")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("session", session)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def OCRService_OCRDrivingLicensePostApi(self, image=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  驾驶证识别.
// route prefix=ids internal_prefix=ids act... """
        """  path: [post]/v1/ocr/driving_license API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "detailed_info": {
                        "detect_details": {
                            "additionalProp1": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp2": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp3": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            }
                        },
                        "has_invalid_field": false
                    },
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
                    "first_page": {
                        "address": "",
                        "birth_date": "",
                        "class": "",
                        "id": "",
                        "issue_date": "",
                        "name": "",
                        "nationality": "",
                        "sex": "",
                        "valid_from": "",
                        "valid_to": ""
                    },
                    "second_page": {
                        "barcode": "",
                        "file_no": "",
                        "id": "",
                        "name": "",
                        "record": ""
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
        intef = collections.interface("ocr", "OCRService_OCRDrivingLicense")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def OCRService_OCRHKMacauExitEntryPermitPostApi(self, image=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  港澳通行证识别.
route prefix=ids internal_prefix=ids acti... """
        """  path: [post]/v1/ocr/hk_macau_exit_entry_permit API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "detailed_info": {
                        "detect_details": {
                            "additionalProp1": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp2": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp3": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            }
                        },
                        "has_invalid_field": false
                    },
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
                    "hk_macau_exit_entry_permit": {
                        "birth_date": "",
                        "card_number": "",
                        "expiry_date": "",
                        "issue_address": "",
                        "name": "",
                        "name_pinyin": "",
                        "sex": ""
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
        intef = collections.interface("ocr", "OCRService_OCRHKMacauExitEntryPermit")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def OCRService_OCRIDCardPostApi(self, image=None, side=None, detect_quality=None, encrypt_info=None, session_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  检测识别图片中的身份证.
route prefix=ids internal_prefix=ids ... """
        """  path: [post]/v1/ocr/idcard API """
        """  body: 
                {
                    "detect_quality": false,
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": "",
                    "session_id": "",
                    "side": "[AUTO]AUTO/FRONT/BACK"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "detailed_info": {
                        "detect_details": {
                            "additionalProp1": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp2": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp3": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            }
                        },
                        "has_invalid_field": false
                    },
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
                    "idcard": {
                        "address": "",
                        "authority": "",
                        "back_image": "",
                        "birth_date": "",
                        "expiry_date": "",
                        "front_image": "",
                        "idcard_source": "[ID_CARD_SOURCE_NONE]ID_CARD_SOURCE_NONE/ORIGIN/PHOTO_COPY/PS/REVERSION/TEMPORARY/ID_CARD_SOURCE_OTHER",
                        "image": "",
                        "issue_date": "",
                        "name": "",
                        "nation": "",
                        "number": "",
                        "sex": "",
                        "side": "[AUTO]AUTO/FRONT/BACK"
                    },
                    "quality_items": [
                        {
                            "quality_type": "[QUALITY_TYPE_NONE]QUALITY_TYPE_NONE/OCCLUSION/LIGHT_BRIGHT/LIGHT_DARK/BLUR/CROPPED/ID_CARD_QUALITY_OTHER",
                            "score": 0
                        }
                    ],
                    "quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/EXTREMELY_LOW/LOW/NORMAL/HIGH",
                    "roi": {
                        "vertices": [
                            {
                                "x": 0,
                                "y": 0
                            }
                        ]
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
        intef = collections.interface("ocr", "OCRService_OCRIDCard")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("side", side)
        intef.update_body("detect_quality", detect_quality)
        intef.update_body("encrypt_info", encrypt_info)
        intef.update_body("session_id", session_id)
        return intef.request() if sendRequest else intef

    def OCRService_OCRPassportPostApi(self, image=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  护照识别.
route prefix=ids internal_prefix=ids action=... """
        """  path: [post]/v1/ocr/passport API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "detailed_info": {
                        "detect_details": {
                            "additionalProp1": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp2": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp3": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            }
                        },
                        "has_invalid_field": false
                    },
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
                    "passport": {
                        "authority": "",
                        "birth_date": "",
                        "birth_place": "",
                        "country_code": "",
                        "expiry_date": "",
                        "issue_date": "",
                        "issue_place": "",
                        "mrz_code_1": "",
                        "mrz_code_2": "",
                        "name": "",
                        "nationality": "",
                        "passport_no": "",
                        "sex": "",
                        "type": ""
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
        intef = collections.interface("ocr", "OCRService_OCRPassport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def OCRService_OCRTaiwanExitEntryPermitPostApi(self, image=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  台湾通行证识别.
route prefix=ids internal_prefix=ids acti... """
        """  path: [post]/v1/ocr/taiwan_exit_entry_permit API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "detailed_info": {
                        "detect_details": {
                            "additionalProp1": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp2": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp3": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            }
                        },
                        "has_invalid_field": false
                    },
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
                    "taiwan_exit_entry_permit": {
                        "birth_date": "",
                        "card_number": "",
                        "expiry_date": "",
                        "issue_address": "",
                        "name": "",
                        "name_pinyin": "",
                        "sex": ""
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
        intef = collections.interface("ocr", "OCRService_OCRTaiwanExitEntryPermit")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def OCRService_OCRVehicleLicensePostApi(self, image=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  行驶证识别.
route prefix=ids internal_prefix=ids action... """
        """  path: [post]/v1/ocr/vehicle_license API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "detailed_info": {
                        "detect_details": {
                            "additionalProp1": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp2": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            },
                            "additionalProp3": {
                                "confidence": 0,
                                "field_name": "",
                                "is_invalid": false
                            }
                        },
                        "has_invalid_field": false
                    },
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
                    "extra_page": {
                        "inspection_record": ""
                    },
                    "first_page": {
                        "address": "",
                        "engine_no": "",
                        "issue_date": "",
                        "model": "",
                        "owner": "",
                        "plate_no": "",
                        "register_date": "",
                        "use_character": "",
                        "vehicle_type": "",
                        "vin": ""
                    },
                    "second_page": {
                        "apc": "",
                        "approved_load": "",
                        "barcode": "",
                        "comment": "",
                        "file_no": "",
                        "gross_mass": "",
                        "inspection_record": "",
                        "overall_dimension": "",
                        "plate_no": "",
                        "traction_mass": "",
                        "unladen_mass": "",
                        "vehicle_type": ""
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
        intef = collections.interface("ocr", "OCRService_OCRVehicleLicense")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

