#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger
import multiprocessing
lock = multiprocessing.Lock()
"""
使用说明：


"""


collections = load_swagger("nova")


class FileSwaggerApi(BaseApi):
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

    def FileService_ListFilesGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取文件列表 """
        """  path: [get]/v1/files API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "files": [
                        {
                            "created_at": "",
                            "description": "",
                            "file_name": "",
                            "id": "",
                            "scheme": "[FILESCHEME_UNKNOWN]FILESCHEME_UNKNOWN/FINE_TUNE_1/FINE_TUNE_IMGEN_1/KNOWLEDGE_BASE_1",
                            "status": "[FILESTATUS_UNKNOWN]FILESTATUS_UNKNOWN/NOTUPLOADED/UPLOADED/INVALID/VALID",
                            "updated_at": "",
                            "validate_result": ""
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
        intef = collections.interface("File", "FileService_ListFiles")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def uploadPostApi(self, file_path, description=None, scheme=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  上传文件 """
        """  path: [post]/v1/files API """
        """  body: 
                {
                    "description": "",
                    "scheme": ""
                }
        """
        """  resp:
               {
                  "created_at": "2023-07-26T07:11:55.577Z",
                  "description": "string",
                  "id": "string",
                  "scheme": "FILESCHEME_UNKNOWN",
                  "status": "FILESTATUS_UNKNOWN",
                  "updated_at": "2023-07-26T07:11:55.577Z"
                }

        """
        intef = collections.interface("File", "upload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("description", description)
        intef.update_body("scheme", scheme)
        intef.files["file"] = file_path
        with lock:
            return intef.request() if sendRequest else intef

    def FileService_ListFilesByFilterInternalPostApi(self, filter=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取文件列(Internal) """
        """  path: [post]/v1/files/internal API """
        """  body: 
                {
                    "filter": {
                        "account_id": "",
                        "ids": []
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "files": [
                        {
                            "ExternalDownloadURL": "",
                            "InternalDownloadURL": "",
                            "URI": "",
                            "created_at": "",
                            "description": "",
                            "id": "",
                            "scheme": "[FILESCHEME_UNKNOWN]FILESCHEME_UNKNOWN/FINE_TUNE_1/KNOWLEDGE_BASE_1",
                            "status": "[FILESTATUS_UNKNOWN]FILESTATUS_UNKNOWN/NOTUPLOADED/UPLOADED/INVALID/VALID",
                            "updated_at": "",
                            "validate_result": ""
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
        intef = collections.interface("File", "FileService_ListFilesByFilterInternal")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("filter", filter)
        return intef.request() if sendRequest else intef

    def FileService_GetFileGetApi(self, file_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取文件 """
        """  path: [get]/v1/files/{file_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "file": {
                        "created_at": "",
                        "description": "",
                        "file_name": "",
                        "id": "",
                        "scheme": "[FILESCHEME_UNKNOWN]FILESCHEME_UNKNOWN/FINE_TUNE_1/KNOWLEDGE_BASE_1",
                        "status": "[FILESTATUS_UNKNOWN]FILESTATUS_UNKNOWN/NOTUPLOADED/UPLOADED/INVALID/VALID",
                        "updated_at": "",
                        "validate_result": ""
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
        intef = collections.interface("File", "FileService_GetFile")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("file_id", file_id)
        with lock:
            return intef.request() if sendRequest else intef

    def FileService_DeleteFileDeleteApi(self, file_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除文件 """
        """  path: [delete]/v1/files/{file_id} API """
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
        intef = collections.interface("File", "FileService_DeleteFile")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("file_id", file_id)
        return intef.request() if sendRequest else intef

    def downloadGetApi(self, file_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  下载文件 """
        """  path: [get]/v1/files/{file_id}/content API """
        """  params: 

        """
        """  resp:
                302():
                ""
                default():
                ""

        """
        intef = collections.interface("File", "download")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("file_id", file_id)
        return intef.request() if sendRequest else intef

    def FileService_DecreaseFileUseCountPostApi(self, file_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  减少文件计数, only for internal temperary test """
        """  path: [post]/v1/files/{file_id}/decrease-use-count API """
        """  body: 
                {}
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
        intef = collections.interface("File", "FileService_DecreaseFileUseCount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("file_id", file_id)
        return intef.request() if sendRequest else intef

    def FileService_IncreaseFileUseCountPostApi(self, file_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  增加文件计数, only for internal temperary test """
        """  path: [post]/v1/files/{file_id}/increase-use-count API """
        """  body: 
                {}
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
        intef = collections.interface("File", "FileService_IncreaseFileUseCount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("file_id", file_id)
        return intef.request() if sendRequest else intef

    def FileService_ListFilesByFilterInternalPostApi(self, filter=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取文件列(Internal) """
        """  path: [post]/v1/internal-files API """
        """  body: 
                {
                    "filter": {
                        "account_id": "",
                        "ids": []
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "files": [
                        {
                            "URI": "",
                            "created_at": "",
                            "description": "",
                            "external_downloadURL": "",
                            "file_name": "",
                            "file_size": "",
                            "id": "",
                            "internal_downloadURL": "",
                            "scheme": "[FILESCHEME_UNKNOWN]FILESCHEME_UNKNOWN/FINE_TUNE_1/KNOWLEDGE_BASE_1",
                            "status": "[FILESTATUS_UNKNOWN]FILESTATUS_UNKNOWN/NOTUPLOADED/UPLOADED/INVALID/VALID",
                            "updated_at": "",
                            "validate_result": ""
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
        intef = collections.interface("File", "FileService_ListFilesByFilterInternal")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("filter", filter)
        return intef.request() if sendRequest else intef

