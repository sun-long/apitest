#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class DatasetSwaggerApi(BaseApi):
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

    def NovaFinetunesDatasetService_ListImgenFinetuneDatasetsGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取 imgen 类型的 dateset 列表 """
        """  path: [get]/v1/imgen/internal/datasets API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "datasets": [
                        {
                            "created_at": "",
                            "description": "",
                            "files": [
                                {
                                    "description": "",
                                    "id": "",
                                    "status": "[NOTUPLOADED]NOTUPLOADED/UPLOADED/INVALID/VALID"
                                }
                            ],
                            "id": "",
                            "status": "[READY]READY/NOTREADY",
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_ListImgenFinetuneDatasets")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_CreateImgenFinetuneDatasetPostApi(self, description=None, files=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建 imgen 类型的 dataset """
        """  path: [post]/v1/imgen/internal/datasets API """
        """  body: 
                {
                    "description": "",
                    "files": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "dataset": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[NOTUPLOADED]NOTUPLOADED/UPLOADED/INVALID/VALID"
                            }
                        ],
                        "id": "",
                        "status": "[READY]READY/NOTREADY",
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_CreateImgenFinetuneDataset")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("description", description)
        intef.update_body("files", files)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_GetImgenFinetuneDatasetGetApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取 imgen 类型的 dataset 信息 """
        """  path: [get]/v1/imgen/internal/datasets/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "dataset": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[NOTUPLOADED]NOTUPLOADED/UPLOADED/INVALID/VALID"
                            }
                        ],
                        "id": "",
                        "status": "[READY]READY/NOTREADY",
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_GetImgenFinetuneDataset")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_DeleteImgenFinetuneDatasetDeleteApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除 imgen 类型的 dataset """
        """  path: [delete]/v1/imgen/internal/datasets/{id} API """
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_DeleteImgenFinetuneDataset")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_UpdateImgenFinetuneDatasetPostApi(self, id, description=None, files=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新 imgen 类型的 dataset 信息 """
        """  path: [post]/v1/imgen/internal/datasets/{id} API """
        """  body: 
                {
                    "description": "",
                    "files": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "dataset": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[NOTUPLOADED]NOTUPLOADED/UPLOADED/INVALID/VALID"
                            }
                        ],
                        "id": "",
                        "status": "[READY]READY/NOTREADY",
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_UpdateImgenFinetuneDataset")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        intef.update_body("description", description)
        intef.update_body("files", files)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_ListNovaFinetunesDatasetsGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  list datasets by accountid """
        """  path: [get]/v1/llm/fine-tune/datasets API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "datasets": [
                        {
                            "created_at": "",
                            "description": "",
                            "files": [
                                {
                                    "description": "",
                                    "id": "",
                                    "status": "[NOTUPLOADED]NOTUPLOADED/UPLOADED/INVALID/VALID"
                                }
                            ],
                            "id": "",
                            "status": "[READY]READY/NOTREADY",
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_ListNovaFinetunesDatasets")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_CreateNovaFinetunesDatasetPostApi(self, description=None, files=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  create dataset by accountid """
        """  path: [post]/v1/llm/fine-tune/datasets API """
        """  body: 
                {
                    "description": "",
                    "files": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "dataset": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[NOTUPLOADED]NOTUPLOADED/UPLOADED/INVALID/VALID"
                            }
                        ],
                        "id": "",
                        "status": "[READY]READY/NOTREADY",
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_CreateNovaFinetunesDataset")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("description", description)
        intef.update_body("files", files)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_GetNovaFinetunesDatasetGetApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  get dataset by accountid and datasetid """
        """  path: [get]/v1/llm/fine-tune/datasets/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "dataset": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[NOTUPLOADED]NOTUPLOADED/UPLOADED/INVALID/VALID"
                            }
                        ],
                        "id": "",
                        "status": "[READY]READY/NOTREADY",
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_GetNovaFinetunesDataset")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_DeleteNovaFinetunesDatasetDeleteApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  delete dataset by accountid and datasetid """
        """  path: [delete]/v1/llm/fine-tune/datasets/{id} API """
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_DeleteNovaFinetunesDataset")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_UpdateNovaFinetunesDatasetPutApi(self, id, description=None, files=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [put]/v1/llm/fine-tune/datasets/{id} API """
        """  body: 
                {
                    "description": "",
                    "files": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "dataset": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[NOTUPLOADED]NOTUPLOADED/UPLOADED/INVALID/VALID"
                            }
                        ],
                        "id": "",
                        "status": "[READY]READY/NOTREADY",
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_UpdateNovaFinetunesDataset")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        intef.update_body("description", description)
        intef.update_body("files", files)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_AddFileToNovaFinetunesDatasetPostApi(self, id, description=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  add file to dataset by accountid and datasetid """
        """  path: [post]/v1/llm/fine-tune/datasets/{id}/files API """
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_AddFileToNovaFinetunesDataset")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        intef.update_body("description", description)
        return intef.request() if sendRequest else intef

    def NovaFinetunesDatasetService_GetNoveFinetunesDatasetInternalGetApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/v1/llm/fine-tune/datasets/{id}/internal API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "dataset": {
                        "created_at": "",
                        "description": "",
                        "files": [
                            {
                                "description": "",
                                "id": "",
                                "status": "[NOTUPLOADED]NOTUPLOADED/UPLOADED/INVALID/VALID",
                                "uri": ""
                            }
                        ],
                        "id": "",
                        "status": "[READY]READY/NOTREADY"
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
        intef = collections.interface("Dataset", "NovaFinetunesDatasetService_GetNoveFinetunesDatasetInternal")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

