#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class KbsSwaggerApi(BaseApi):
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

    def KnowledgeBaseService_ListInternalKnowledgeBasesGetApi(self, types=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询默认知识库列表[internal] """
        """  path: [get]/v1/llm/internal/knowledge-bases API """
        """  params: 
                参数名称：types　类型：array　描述： - KBT_UNKNOWN: 未知类型.
 - KBT_BUSINESS: 用户知识库.
 - KBT_DEFAULT: 默认知识库.
 - KBT_PUBLIC: 开放知识库
        """
        """  resp:
                200(A successful response.):
                {
                    "knowledge_bases": [
                        {
                            "created_at": "",
                            "description": "",
                            "files": [
                                {
                                    "description": "",
                                    "id": "",
                                    "status": "[FILESTATUS_UNKNOWN]FILESTATUS_UNKNOWN/NOTUPLOADED/UPLOADED/INVALID/VALID"
                                }
                            ],
                            "id": "",
                            "region": "",
                            "status": "[STATUS_UNNKNOWN]STATUS_UNNKNOWN/PENDING/LOADING/AVAILABLE/UNAVAILABLE",
                            "type": "[KBT_UNKNOWN]KBT_UNKNOWN/KBT_BUSINESS/KBT_DEFAULT/KBT_PUBLIC",
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
        intef = collections.interface("Kbs", "KnowledgeBaseService_ListInternalKnowledgeBases")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("types", types)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_CreateInternalKnowledgeBasePostApi(self, description=None, region=None, files=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建默认知识库[internal] """
        """  path: [post]/v1/llm/internal/knowledge-bases API """
        """  body: 
                {
                    "description": "",
                    "files": [],
                    "region": "",
                    "type": "[KBT_UNKNOWN]KBT_UNKNOWN/KBT_BUSINESS/KBT_DEFAULT/KBT_PUBLIC"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "knowledge_base": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[FILESTATUS_UNKNOWN]FILESTATUS_UNKNOWN/NOTUPLOADED/UPLOADED/INVALID/VALID"
                            }
                        ],
                        "id": "",
                        "region": "",
                        "status": "[STATUS_UNNKNOWN]STATUS_UNNKNOWN/PENDING/LOADING/AVAILABLE/UNAVAILABLE",
                        "type": "[KBT_UNKNOWN]KBT_UNKNOWN/KBT_BUSINESS/KBT_DEFAULT/KBT_PUBLIC",
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
        intef = collections.interface("Kbs", "KnowledgeBaseService_CreateInternalKnowledgeBase")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("description", description)
        intef.update_body("region", region)
        intef.update_body("files", files)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_CreateInternalKnowledgeBaseFilesPostApi(self, knowledge_base_id, description=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建默认知识库文件，并生成文件上传地址[internal] """
        """  path: [post]/v1/llm/internal/knowledge-bases/{knowledge_base_id}/files API """
        """  body: 
                {
                    "description": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "description": "",
                    "id": "",
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
        intef = collections.interface("Kbs", "KnowledgeBaseService_CreateInternalKnowledgeBaseFiles")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("knowledge_base_id", knowledge_base_id)
        intef.update_body("description", description)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_GetKnowledgeBasesGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询知识库列表 """
        """  path: [get]/v1/llm/knowledge-bases API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "knowledge_bases": [
                        {
                            "created_at": "",
                            "description": "",
                            "files": [
                                {
                                    "description": "",
                                    "id": "",
                                    "status": "[FILESTATUS_UNKNOWN]FILESTATUS_UNKNOWN/NOTUPLOADED/UPLOADED/INVALID/VALID"
                                }
                            ],
                            "id": "",
                            "status": "[STATUS_UNNKNOWN]STATUS_UNNKNOWN/PENDING/LOADING/AVAILABLE/UNAVAILABLE",
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
        intef = collections.interface("Kbs", "KnowledgeBaseService_GetKnowledgeBases")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_CreateKnowledgeBasePostApi(self, description=None, files=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建知识库
1.此接口只创建逻辑数据集，不再支持上传文件，上传文件由后续独立接口完成；
2.为提升用... """
        """  path: [post]/v1/llm/knowledge-bases API """
        """  body: 
                {
                    "description": "",
                    "files": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "knowledge_base": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[FILESTATUS_UNKNOWN]FILESTATUS_UNKNOWN/NOTUPLOADED/UPLOADED/INVALID/VALID"
                            }
                        ],
                        "id": "",
                        "status": "[STATUS_UNNKNOWN]STATUS_UNNKNOWN/PENDING/LOADING/AVAILABLE/UNAVAILABLE",
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
        intef = collections.interface("Kbs", "KnowledgeBaseService_CreateKnowledgeBase")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("description", description)
        intef.update_body("files", files)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_ListConsumerGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询Consumer信息 """
        """  path: [get]/v1/llm/knowledge-bases-build-consumer API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "consumer_infos": [
                        {
                            "id": "",
                            "last_active": "",
                            "status": "[ConsumerStatus_Unknown]ConsumerStatus_Unknown/Enabled/Disabled",
                            "work_status": "[ConsumerWorkStatus_Unknown]ConsumerWorkStatus_Unknown/Idle/Building/Offline"
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
        intef = collections.interface("Kbs", "KnowledgeBaseService_ListConsumer")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_UpdateConsumerStatusPostApi(self, status=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  设置Consumer状态，Enable为正常，Disable为不再消费但不主动停止当前任务 """
        """  path: [post]/v1/llm/knowledge-bases-build-consumer API """
        """  body: 
                {
                    "status": "[ConsumerStatus_Unknown]ConsumerStatus_Unknown/Enabled/Disabled"
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
        intef = collections.interface("Kbs", "KnowledgeBaseService_UpdateConsumerStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("status", status)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_GetKnowledgeBaseByIDGetApi(self, knowledge_base_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询知识库详情 """
        """  path: [get]/v1/llm/knowledge-bases/{knowledge_base_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "knowledge_base": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[FILESTATUS_UNKNOWN]FILESTATUS_UNKNOWN/NOTUPLOADED/UPLOADED/INVALID/VALID"
                            }
                        ],
                        "id": "",
                        "status": "[STATUS_UNNKNOWN]STATUS_UNNKNOWN/PENDING/LOADING/AVAILABLE/UNAVAILABLE",
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
        intef = collections.interface("Kbs", "KnowledgeBaseService_GetKnowledgeBaseByID")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("knowledge_base_id", knowledge_base_id)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_DeleteKnowledgeBaseDeleteApi(self, knowledge_base_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除知识库 """
        """  path: [delete]/v1/llm/knowledge-bases/{knowledge_base_id} API """
        """  params: 

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
        intef = collections.interface("Kbs", "KnowledgeBaseService_DeleteKnowledgeBase")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("knowledge_base_id", knowledge_base_id)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_UpdateKnowledgeBasePutApi(self, knowledge_base_id, description=None, files=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新知识库 """
        """  path: [put]/v1/llm/knowledge-bases/{knowledge_base_id} API """
        """  body: 
                {
                    "description": "",
                    "files": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "knowledge_base": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[FILESTATUS_UNKNOWN]FILESTATUS_UNKNOWN/NOTUPLOADED/UPLOADED/INVALID/VALID"
                            }
                        ],
                        "id": "",
                        "status": "[STATUS_UNNKNOWN]STATUS_UNNKNOWN/PENDING/LOADING/AVAILABLE/UNAVAILABLE",
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
        intef = collections.interface("Kbs", "KnowledgeBaseService_UpdateKnowledgeBase")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("knowledge_base_id", knowledge_base_id)
        intef.update_body("description", description)
        intef.update_body("files", files)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_CreateKnowledgeBaseFilesPostApi(self, knowledge_base_id, description=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建知识库文件，并生成文件上传地址，
创建知识库时，files参数为空，需要通过该接口创建知识库文件... """
        """  path: [post]/v1/llm/knowledge-bases/{knowledge_base_id}/files API """
        """  body: 
                {
                    "description": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "description": "",
                    "id": "",
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
        intef = collections.interface("Kbs", "KnowledgeBaseService_CreateKnowledgeBaseFiles")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("knowledge_base_id", knowledge_base_id)
        intef.update_body("description", description)
        return intef.request() if sendRequest else intef

    def KnowledgeBaseService_DeleteKnowledgeBaseFileDeleteApi(self, knowledge_base_id, file_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除知识库文件.
通过gateway前缀区分原生http handler, 防止请求被拦截. """
        """  path: [delete]/v1/llm/knowledge-bases/{knowledge_base_id}/files/{file_id} API """
        """  params: 

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
        intef = collections.interface("Kbs", "KnowledgeBaseService_DeleteKnowledgeBaseFile")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("knowledge_base_id", knowledge_base_id)
        intef.set_path_param("file_id", file_id)
        return intef.request() if sendRequest else intef

