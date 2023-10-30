#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class IdentitySwaggerApi(BaseApi):
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

    def IdentityService_CheckHealthGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  内部接口, 上报健康信息给RAS [INTERNAL].
route prefix=ids inte... """
        """  path: [get]/health API """
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
        intef = collections.interface("identity", "IdentityService_CheckHealth")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def IdentityService_H5GetSessionConfigPostApi(self, session_id=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  H5 调用的内部接口, 获取H5全流程相关配置[INTERNAL].
route prefix=id... """
        """  path: [post]/v1/h5/identity/get_session_config API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "session_id": ""
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
                    "session": {
                        "action_number": 0,
                        "candidate_actions": [
                            "[ACTION_TYPE_NONE]ACTION_TYPE_NONE/BLINK_EYES/OPEN_MOUTH/SHAKE_HEAD/NOD_HEAD"
                        ],
                        "disable_color_liveness": false,
                        "extra_info": "",
                        "h5_config": {
                            "logo_url": "",
                            "page_title": "",
                            "redirect_url": "",
                            "template_id": ""
                        },
                        "id_verification": {
                            "certificate_type": "[CERTIFICATE_TYPE_NONE]CERTIFICATE_TYPE_NONE/IDCARD",
                            "certificate_types": [
                                "[CERTIFICATE_TYPE_NONE]CERTIFICATE_TYPE_NONE/IDCARD"
                            ],
                            "expiry_date": "",
                            "idcard_number": "",
                            "min_quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/EXTREMELY_LOW/LOW/NORMAL/HIGH",
                            "name": ""
                        },
                        "pick_images_by_quality_number": 0,
                        "pick_images_per_action_number": 0,
                        "save_process_video": false,
                        "session_type": "[IDENTITY_VERIFICATION]IDENTITY_VERIFICATION/LIVENESS/H5_LIVENESS/IDCARD_SCAN/BANKCARD_SCAN",
                        "uuid": ""
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
        intef = collections.interface("identity", "IdentityService_H5GetSessionConfig")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("session_id", session_id)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def IdentityService_H5UpdateIDCardPostApi(self, name=None, idcard_number=None, expiry_date=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  H5 三要素身份核验, 根据权威源校验身份证号和姓名是否匹配, 并比对请求中人脸图片和权威库图片[I... """
        """  path: [post]/v1/h5/identity/update_idcard API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "expiry_date": "",
                    "idcard_number": "",
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("identity", "IdentityService_H5UpdateIDCard")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("idcard_number", idcard_number)
        intef.update_body("expiry_date", expiry_date)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def IdentityService_CompareFaceIDCardPostApi(self, image=None, auto_rotate=None, min_quality_level=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  将手持身份证照中的被拍人的脸和身份证上的人脸进行比对，判断是否为同一人.
route prefix=... """
        """  path: [post]/v1/identity/compare_face_idcard API """
        """  body: 
                {
                    "auto_rotate": false,
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": "",
                    "min_quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/LOW/NORMAL/HIGH/EXTREMELY_HIGH"
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
        intef = collections.interface("identity", "IdentityService_CompareFaceIDCard")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("auto_rotate", auto_rotate)
        intef.update_body("min_quality_level", min_quality_level)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def IdentityService_CreateSessionPostApi(self, session=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建一个检测会话.
route prefix=ids internal_prefix=ids act... """
        """  path: [post]/v1/identity/create_session API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "session": {
                        "action_number": 0,
                        "candidate_actions": [
                            "[ACTION_TYPE_NONE]ACTION_TYPE_NONE/BLINK_EYES/OPEN_MOUTH/SHAKE_HEAD/NOD_HEAD"
                        ],
                        "disable_color_liveness": false,
                        "extra_info": "",
                        "h5_config": {
                            "logo_url": "",
                            "page_title": "",
                            "redirect_url": "",
                            "template_id": ""
                        },
                        "id_verification": {
                            "certificate_type": "[CERTIFICATE_TYPE_NONE]CERTIFICATE_TYPE_NONE/IDCARD",
                            "certificate_types": [
                                "[CERTIFICATE_TYPE_NONE]CERTIFICATE_TYPE_NONE/IDCARD"
                            ],
                            "expiry_date": "",
                            "idcard_number": "",
                            "min_quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/EXTREMELY_LOW/LOW/NORMAL/HIGH",
                            "name": ""
                        },
                        "pick_images_by_quality_number": 0,
                        "pick_images_per_action_number": 0,
                        "save_process_video": false,
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
                    "session_id": "",
                    "verification_url": ""
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
        intef = collections.interface("identity", "IdentityService_CreateSession")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("session", session)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def IdentityService_GetSessionLivenessResultPostApi(self, session_id=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取活体检测会话的最终结果.
route prefix=ids internal_prefix=id... """
        """  path: [post]/v1/identity/get_session_liveness_result API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "session_id": ""
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
                    "extra_info": "",
                    "session_result": {
                        "action_images": [
                            {
                                "action": "[ACTION_TYPE_NONE]ACTION_TYPE_NONE/BLINK_EYES/OPEN_MOUTH/SHAKE_HEAD/NOD_HEAD",
                                "image": ""
                            }
                        ],
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
                        "idcard_back_image": "",
                        "idcard_front_image": "",
                        "is_liveness": false,
                        "liveness_score": 0,
                        "process_video_url": "",
                        "quality_images": [
                            {
                                "image": "",
                                "quality": 0
                            }
                        ],
                        "user_updated_idcard": {
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
                        "verify_result": "[VERIFY_RESULT_UNKNOWN]VERIFY_RESULT_UNKNOWN/MATCH/INVALID_IDCARD_INFO/FACE_UNMATCH/MISMATCH"
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
        intef = collections.interface("identity", "IdentityService_GetSessionLivenessResult")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("session_id", session_id)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def IdentityService_GetSessionVerificationResultPostApi(self, session_id=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取身份核验检测会话的最终结果.
route prefix=ids internal_prefix=... """
        """  path: [post]/v1/identity/get_session_verification_result API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "session_id": ""
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
                    "extra_info": "",
                    "session_result": {
                        "action_images": [
                            {
                                "action": "[ACTION_TYPE_NONE]ACTION_TYPE_NONE/BLINK_EYES/OPEN_MOUTH/SHAKE_HEAD/NOD_HEAD",
                                "image": ""
                            }
                        ],
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
                        "idcard_back_image": "",
                        "idcard_front_image": "",
                        "is_liveness": false,
                        "liveness_score": 0,
                        "process_video_url": "",
                        "quality_images": [
                            {
                                "image": "",
                                "quality": 0
                            }
                        ],
                        "user_updated_idcard": {
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
                        "verify_result": "[VERIFY_RESULT_UNKNOWN]VERIFY_RESULT_UNKNOWN/MATCH/INVALID_IDCARD_INFO/FACE_UNMATCH/MISMATCH"
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
        intef = collections.interface("identity", "IdentityService_GetSessionVerificationResult")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("session_id", session_id)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def IdentityService_VerifyBankcardPostApi(self, verify_info=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  银行卡四要素核验.
route prefix=ids internal_prefix=ids act... """
        """  path: [post]/v1/identity/verify_bankcard API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "verify_info": {
                        "bankcard_number": "",
                        "idcard_number": "",
                        "mobile": "",
                        "name": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "description": "",
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "verify_result": "[VERIFY_RESULT_UNKNOWN]VERIFY_RESULT_UNKNOWN/MATCH/INVALID_IDCARD_INFO/FACE_UNMATCH/MISMATCH"
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
        intef = collections.interface("identity", "IdentityService_VerifyBankcard")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("verify_info", verify_info)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def IdentityService_VerifyEnterprisePostApi(self, verify_info=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  企业四要素核验.
route prefix=ids internal_prefix=ids acti... """
        """  path: [post]/v1/identity/verify_enterprise API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "verify_info": {
                        "artificial_person": "",
                        "enterprise_name": "",
                        "enterprise_no": "",
                        "idcard_number": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "description": "",
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "verify_result": "[VERIFY_RESULT_UNKNOWN]VERIFY_RESULT_UNKNOWN/MATCH/INVALID_IDCARD_INFO/FACE_UNMATCH/MISMATCH"
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
        intef = collections.interface("identity", "IdentityService_VerifyEnterprise")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("verify_info", verify_info)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def IdentityService_VerifyIDCardPostApi(self, name=None, idcard_number=None, expiry_date=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  身份证, 姓名二要素身份核验, 根据权威源校验身份证号和姓名是否匹配.
route prefix=i... """
        """  path: [post]/v1/identity/verify_idcard API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "expiry_date": "",
                    "idcard_number": "",
                    "name": ""
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
                    "verify_result": "[VERIFY_RESULT_UNKNOWN]VERIFY_RESULT_UNKNOWN/MATCH/INVALID_IDCARD_INFO/FACE_UNMATCH/MISMATCH"
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
        intef = collections.interface("identity", "IdentityService_VerifyIDCard")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("idcard_number", idcard_number)
        intef.update_body("expiry_date", expiry_date)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def IdentityService_VerifyIDCardFacePostApi(self, name=None, idcard_number=None, expiry_date=None, image=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  身份证, 姓名, 人脸图三要素身份核验, 根据权威源校验身份证号和姓名是否匹配, 并比对请求中人脸图... """
        """  path: [post]/v1/identity/verify_idcard_face API """
        """  body: 
                {
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "expiry_date": "",
                    "idcard_number": "",
                    "image": "",
                    "name": ""
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
                    "score": 0,
                    "verify_result": "[VERIFY_RESULT_UNKNOWN]VERIFY_RESULT_UNKNOWN/MATCH/INVALID_IDCARD_INFO/FACE_UNMATCH/MISMATCH"
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
        intef = collections.interface("identity", "IdentityService_VerifyIDCardFace")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("idcard_number", idcard_number)
        intef.update_body("expiry_date", expiry_date)
        intef.update_body("image", image)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

