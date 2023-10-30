#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class FaceSwaggerApi(BaseApi):
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

    def FaceService_AddPersonPostApi(self, db_id=None, person_id=None, images=None, extra_info=None, auto_rotate=None, min_quality_level=None, tag_ids=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  添加人员信息到指定人员库.
route prefix=ids internal_prefix=ids... """
        """  path: [post]/v1/face/add_person API """
        """  body: 
                {
                    "auto_rotate": false,
                    "db_id": "",
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "extra_info": "",
                    "images": [],
                    "min_quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/LOW/NORMAL/HIGH/EXTREMELY_HIGH",
                    "person_id": "",
                    "tag_ids": []
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
                            "error": {
                                "code": 0,
                                "details": [
                                    {
                                        "@type": ""
                                    }
                                ],
                                "message": ""
                            },
                            "face_id": ""
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
        intef = collections.interface("face", "FaceService_AddPerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("person_id", person_id)
        intef.update_body("images", images)
        intef.update_body("extra_info", extra_info)
        intef.update_body("auto_rotate", auto_rotate)
        intef.update_body("min_quality_level", min_quality_level)
        intef.update_body("tag_ids", tag_ids)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def FaceService_AddPersonFacePostApi(self, db_id=None, person_id=None, image=None, auto_rotate=None, min_quality_level=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  增加人员的人脸图.
route prefix=ids internal_prefix=ids act... """
        """  path: [post]/v1/face/add_person_face API """
        """  body: 
                {
                    "auto_rotate": false,
                    "db_id": "",
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": "",
                    "min_quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/LOW/NORMAL/HIGH/EXTREMELY_HIGH",
                    "person_id": ""
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
                    "face_id": ""
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
        intef = collections.interface("face", "FaceService_AddPersonFace")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("person_id", person_id)
        intef.update_body("image", image)
        intef.update_body("auto_rotate", auto_rotate)
        intef.update_body("min_quality_level", min_quality_level)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def FaceService_CompareImagePostApi(self, image=None, base_image=None, auto_rotate=None, min_quality_level=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  人脸 1:1 比对接口, 输入两张图片, 进行特征比对.
route prefix=ids inte... """
        """  path: [post]/v1/face/compare_image API """
        """  body: 
                {
                    "auto_rotate": false,
                    "base_image": "",
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
        intef = collections.interface("face", "FaceService_CompareImage")
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

    def FaceService_CreatePersonDBPostApi(self, name=None, description=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建人员库.
route prefix=ids internal_prefix=ids action... """
        """  path: [post]/v1/face/create_person_db API """
        """  body: 
                {
                    "description": "",
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
                    "id": ""
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
        intef = collections.interface("face", "FaceService_CreatePersonDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("description", description)
        return intef.request() if sendRequest else intef

    def FaceService_CreateTagPostApi(self, db_id=None, name=None, description=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建人员在库中的业务标签.
route prefix=ids internal_prefix=ids... """
        """  path: [post]/v1/face/create_tag API """
        """  body: 
                {
                    "db_id": "",
                    "description": "",
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
                    "tag_id": ""
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
        intef = collections.interface("face", "FaceService_CreateTag")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("name", name)
        intef.update_body("description", description)
        return intef.request() if sendRequest else intef

    def FaceService_DeletePersonPostApi(self, db_id=None, person_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取人员详细信息.
route prefix=ids internal_prefix=ids act... """
        """  path: [post]/v1/face/delete_person API """
        """  body: 
                {
                    "db_id": "",
                    "person_id": ""
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
        intef = collections.interface("face", "FaceService_DeletePerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("person_id", person_id)
        return intef.request() if sendRequest else intef

    def FaceService_DeletePersonDBPostApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除指定人员库.
route prefix=ids internal_prefix=ids acti... """
        """  path: [post]/v1/face/delete_person_db API """
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
        intef = collections.interface("face", "FaceService_DeletePersonDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def FaceService_DeletePersonFacePostApi(self, db_id=None, person_id=None, face_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除人员的人脸特征.
route prefix=ids internal_prefix=ids ac... """
        """  path: [post]/v1/face/delete_person_face API """
        """  body: 
                {
                    "db_id": "",
                    "face_id": "",
                    "person_id": ""
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
        intef = collections.interface("face", "FaceService_DeletePersonFace")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("person_id", person_id)
        intef.update_body("face_id", face_id)
        return intef.request() if sendRequest else intef

    def FaceService_DeleteTagPostApi(self, db_id=None, tag_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除人员标签.
route prefix=ids internal_prefix=ids actio... """
        """  path: [post]/v1/face/delete_tag API """
        """  body: 
                {
                    "db_id": "",
                    "tag_id": ""
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
        intef = collections.interface("face", "FaceService_DeleteTag")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("tag_id", tag_id)
        return intef.request() if sendRequest else intef

    def FaceService_DetectLivenessPostApi(self, image=None, min_quality_level=None, disable_defake=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  提供图片静默活体检测.
route prefix=ids internal_prefix=ids a... """
        """  path: [post]/v1/face/detect_liveness API """
        """  body: 
                {
                    "disable_defake": false,
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
                            "quality_type": "[QUALITY_TYPE_NONE]QUALITY_TYPE_NONE/PUPIL_DISTANCE/CLARITY/LIGHT_DARK/LIGHT_BRIGHT/INTEGRITY_EYEBROW/INTEGRITY_NOSE/INTEGRITY_MOUTH/INTEGRITY_CHEEK/HEAD_YAW/HEAD_PITCH/HEAD_ROLL/MOUTH_CLOSED/EYES_OPEN",
                            "value": 0
                        }
                    ],
                    "quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/LOW/NORMAL/HIGH/EXTREMELY_HIGH"
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
        intef = collections.interface("face", "FaceService_DetectLiveness")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("min_quality_level", min_quality_level)
        intef.update_body("disable_defake", disable_defake)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def FaceService_GetPersonGetApi(self, db_id=None, person_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取人员详细信息.
route prefix=ids internal_prefix=ids act... """
        """  path: [get]/v1/face/get_person API """
        """  params: 
                参数名称：db_id　类型：string　描述：人员库标识.
                参数名称：person_id　类型：string　描述：根据业务填入的人员标识获取人员详情
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
                    "face_infos": [
                        {
                            "created_at": "",
                            "face_id": "",
                            "image_url": ""
                        }
                    ],
                    "person": {
                        "created_at": "",
                        "extra_info": "",
                        "person_id": "",
                        "updated_at": ""
                    },
                    "tags": [
                        {
                            "id": "",
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
        intef = collections.interface("face", "FaceService_GetPerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("db_id", db_id)
        intef.update_params("person_id", person_id)
        return intef.request() if sendRequest else intef

    def FaceService_ListPersonGetApi(self, db_id=None, filter_person_id=None, page_offset=None, page_limit=None, page_total=None, page_marker=None, page_backward=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  列举人员.
route prefix=ids internal_prefix=ids action=... """
        """  path: [get]/v1/face/list_person API """
        """  params: 
                参数名称：db_id　类型：string　描述：人员库标识.
                参数名称：filter.person_id　类型：string　描述：根据人员标识过滤.
[EN] Filter with person id.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
[EN] Optional, start position, value: > = 0, 0 is the first line; the default value is 0.
In response, actual offset of the first returned record is returned
(generally equals to the offset in request).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 默认为10, 如果超出范围, 则返回失败.
[EN] Length, default value range [1,100], if it is out of the range, error will be returned.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
[EN] Optional, this parameter is not required for request, but will be filled in response.
                参数名称：page.marker　类型：string　描述：可选, 分页书签信息, 适用于大数据量深分页, 响应更快. 第一页列举传空, 后续列举需回传应答结果中对应字段值, 当传递该字段时,优先使用（此时忽略offset）.
[EN], Page bookmark.
                参数名称：page.backward　类型：boolean　描述：当使用marker分页时生效， true: 往上一页翻页, false: 往下一页翻页.
[EN] valid when paging with marker, true: turn the page backward, false: turn the page forward
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
                    "page": {
                        "backward": false,
                        "limit": 0,
                        "marker": "",
                        "offset": 0,
                        "total": 0
                    },
                    "persons": [
                        {
                            "created_at": "",
                            "extra_info": "",
                            "person_id": "",
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
        intef = collections.interface("face", "FaceService_ListPerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("db_id", db_id)
        intef.update_params("filter.person_id", filter_person_id)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.update_params("page.marker", page_marker)
        intef.update_params("page.backward", page_backward)
        return intef.request() if sendRequest else intef

    def FaceService_ListPersonDBGetApi(self, page_offset=None, page_limit=None, page_total=None, page_marker=None, page_backward=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  列举人员库.
route prefix=ids internal_prefix=ids action... """
        """  path: [get]/v1/face/list_person_db API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
[EN] Optional, start position, value: > = 0, 0 is the first line; the default value is 0.
In response, actual offset of the first returned record is returned
(generally equals to the offset in request).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 默认为10, 如果超出范围, 则返回失败.
[EN] Length, default value range [1,100], if it is out of the range, error will be returned.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
[EN] Optional, this parameter is not required for request, but will be filled in response.
                参数名称：page.marker　类型：string　描述：可选, 分页书签信息, 适用于大数据量深分页, 响应更快. 第一页列举传空, 后续列举需回传应答结果中对应字段值, 当传递该字段时,优先使用（此时忽略offset）.
[EN], Page bookmark.
                参数名称：page.backward　类型：boolean　描述：当使用marker分页时生效， true: 往上一页翻页, false: 往下一页翻页.
[EN] valid when paging with marker, true: turn the page backward, false: turn the page forward
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
                    "page": {
                        "backward": false,
                        "limit": 0,
                        "marker": "",
                        "offset": 0,
                        "total": 0
                    },
                    "person_dbs": [
                        {
                            "created_at": "",
                            "description": "",
                            "id": "",
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
        intef = collections.interface("face", "FaceService_ListPersonDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.update_params("page.marker", page_marker)
        intef.update_params("page.backward", page_backward)
        return intef.request() if sendRequest else intef

    def FaceService_ListTagGetApi(self, db_id=None, page_offset=None, page_limit=None, page_total=None, page_marker=None, page_backward=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  列举人员标签.
route prefix=ids internal_prefix=ids actio... """
        """  path: [get]/v1/face/list_tag API """
        """  params: 
                参数名称：db_id　类型：string　描述：列举指定库支持的人员标签.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
[EN] Optional, start position, value: > = 0, 0 is the first line; the default value is 0.
In response, actual offset of the first returned record is returned
(generally equals to the offset in request).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 默认为10, 如果超出范围, 则返回失败.
[EN] Length, default value range [1,100], if it is out of the range, error will be returned.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
[EN] Optional, this parameter is not required for request, but will be filled in response.
                参数名称：page.marker　类型：string　描述：可选, 分页书签信息, 适用于大数据量深分页, 响应更快. 第一页列举传空, 后续列举需回传应答结果中对应字段值, 当传递该字段时,优先使用（此时忽略offset）.
[EN], Page bookmark.
                参数名称：page.backward　类型：boolean　描述：当使用marker分页时生效， true: 往上一页翻页, false: 往下一页翻页.
[EN] valid when paging with marker, true: turn the page backward, false: turn the page forward
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
                    "page": {
                        "backward": false,
                        "limit": 0,
                        "marker": "",
                        "offset": 0,
                        "total": 0
                    },
                    "tags": [
                        {
                            "id": "",
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
        intef = collections.interface("face", "FaceService_ListTag")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("db_id", db_id)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.update_params("page.marker", page_marker)
        intef.update_params("page.backward", page_backward)
        return intef.request() if sendRequest else intef

    def FaceService_SearchPersonPostApi(self, db_id=None, image=None, top_k=None, min_score=None, auto_rotate=None, min_quality_level=None, detect_liveness=None, tag_ids=None, with_detail=None, encrypt_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  提供人员库特征检索.
route prefix=ids internal_prefix=ids ac... """
        """  path: [post]/v1/face/search_person API """
        """  body: 
                {
                    "auto_rotate": false,
                    "db_id": "",
                    "detect_liveness": false,
                    "encrypt_info": {
                        "algorithm": "[ENCRPT_ALGORITHM_NONE]ENCRPT_ALGORITHM_NONE/AES_256_CBC/AES_256_GCM",
                        "data": "",
                        "encrypted_fields": [],
                        "version": 0
                    },
                    "image": "",
                    "min_quality_level": "[QUALITY_LEVEL_NONE]QUALITY_LEVEL_NONE/LOW/NORMAL/HIGH/EXTREMELY_HIGH",
                    "min_score": 0,
                    "tag_ids": [],
                    "top_k": 0,
                    "with_detail": false
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
                            "face_id": "",
                            "person": {
                                "created_at": "",
                                "extra_info": "",
                                "person_id": "",
                                "updated_at": ""
                            },
                            "score": 0,
                            "tag_ids": []
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
        intef = collections.interface("face", "FaceService_SearchPerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("image", image)
        intef.update_body("top_k", top_k)
        intef.update_body("min_score", min_score)
        intef.update_body("auto_rotate", auto_rotate)
        intef.update_body("min_quality_level", min_quality_level)
        intef.update_body("detect_liveness", detect_liveness)
        intef.update_body("tag_ids", tag_ids)
        intef.update_body("with_detail", with_detail)
        intef.update_body("encrypt_info", encrypt_info)
        return intef.request() if sendRequest else intef

    def FaceService_UpdatePersonPostApi(self, db_id=None, person_id=None, extra_info=None, tag_list=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  修改人员信息，包括人员备注信息、标签，更新会覆盖原信息.
route prefix=ids inte... """
        """  path: [post]/v1/face/update_person API """
        """  body: 
                {
                    "db_id": "",
                    "extra_info": "",
                    "person_id": "",
                    "tag_list": {
                        "ids": []
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
        intef = collections.interface("face", "FaceService_UpdatePerson")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("person_id", person_id)
        intef.update_body("extra_info", extra_info)
        intef.update_body("tag_list", tag_list)
        return intef.request() if sendRequest else intef

    def FaceService_UpdatePersonDBPostApi(self, id=None, name=None, description=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新指定人员库信息, 包括库名和特征版本.
route prefix=ids internal_pr... """
        """  path: [post]/v1/face/update_person_db API """
        """  body: 
                {
                    "description": "",
                    "id": "",
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
        intef = collections.interface("face", "FaceService_UpdatePersonDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("name", name)
        intef.update_body("description", description)
        return intef.request() if sendRequest else intef

