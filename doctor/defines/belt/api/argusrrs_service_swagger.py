#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class ArgusrrsSwaggerApi(BaseApi):
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

    def Tenant_AddRGroupPostApi(self, rgroup=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/add-r-group API """
        """  body: 
                {
                    "rgroup": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_AddRGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("rgroup", rgroup)
        return intef.request() if sendRequest else intef

    def Tenant_AddRGroupAkRelationPostApi(self, rgroup=None, ak=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/add-r-group-ak-relation API """
        """  body: 
                {
                    "ak": "",
                    "rgroup": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_AddRGroupAkRelation")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("rgroup", rgroup)
        intef.update_body("ak", ak)
        return intef.request() if sendRequest else intef

    def Tenant_AddResourcePostApi(self, unit=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/add-resource API """
        """  body: 
                {
                    "unit": {
                        "created_at": "",
                        "host": "",
                        "name": "",
                        "prom_name": "",
                        "resource_id": "",
                        "rgroup": "",
                        "rstype": "[SFD]SFD/GPU/MONGO",
                        "tags": [
                            {
                                "create_at": "",
                                "name": "",
                                "score": 0,
                                "type": "[STATIC]STATIC/DYNAMIC",
                                "update_at": "",
                                "value": ""
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_AddResource")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("unit", unit)
        return intef.request() if sendRequest else intef

    def Tenant_AddTagPostApi(self, tag=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/add-tag API """
        """  body: 
                {
                    "tag": {
                        "create_at": "",
                        "name": "",
                        "score": 0,
                        "type": "[STATIC]STATIC/DYNAMIC",
                        "update_at": "",
                        "value": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_AddTag")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("tag", tag)
        return intef.request() if sendRequest else intef

    def Tenant_DeleteRGroupPostApi(self, rgroup=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/delete-r-group API """
        """  body: 
                {
                    "rgroup": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_DeleteRGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("rgroup", rgroup)
        return intef.request() if sendRequest else intef

    def Tenant_DeleteResourcePostApi(self, resource_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/delete-resource API """
        """  body: 
                {
                    "resource_id": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "deleted_count": 0,
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_DeleteResource")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("resource_id", resource_id)
        return intef.request() if sendRequest else intef

    def Tenant_DeleteTagPostApi(self, tag=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/delete-tag API """
        """  body: 
                {
                    "tag": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_DeleteTag")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("tag", tag)
        return intef.request() if sendRequest else intef

    def Tenant_GetRgroupByAkGetApi(self, header_request_id=None, ak=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/sensego/v1/tenant/get-rgroup-by-ak API """
        """  params: 
                参数名称：header.request_id　类型：string　描述：null
                参数名称：ak　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "header": {
                        "request_id": ""
                    },
                    "rgroup": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_GetRgroupByAk")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("header.request_id", header_request_id)
        intef.update_params("ak", ak)
        return intef.request() if sendRequest else intef

    def Tenant_ListAllocateGroupGetApi(self, header_request_id=None, rstype=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/sensego/v1/tenant/list-allocate-group API """
        """  params: 
                参数名称：header.request_id　类型：string　描述：null
                参数名称：rstype　类型：string　描述： - SFD: 0 = SFD
 - GPU: 1 = GPU
 - MONGO: 2 = MONG
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": "",
                    "units": [
                        {
                            "host": "",
                            "key": ""
                        }
                    ]
                }

        """
        intef = collections.interface("argusRrs", "Tenant_ListAllocateGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("header.request_id", header_request_id)
        intef.update_params("rstype", rstype)
        return intef.request() if sendRequest else intef

    def Tenant_ListRGroupGetApi(self, header_request_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/sensego/v1/tenant/list-r-group API """
        """  params: 
                参数名称：header.request_id　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": "",
                    "rgroups": [
                        {
                            "create_at": "",
                            "rgroup": ""
                        }
                    ]
                }

        """
        intef = collections.interface("argusRrs", "Tenant_ListRGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("header.request_id", header_request_id)
        return intef.request() if sendRequest else intef

    def Tenant_ListRGroupAkRelationGetApi(self, header_request_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/sensego/v1/tenant/list-r-group-ak-relation API """
        """  params: 
                参数名称：header.request_id　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "bind": [
                        {
                            "ak": "",
                            "create_at": "",
                            "rgroup": ""
                        }
                    ],
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_ListRGroupAkRelation")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("header.request_id", header_request_id)
        return intef.request() if sendRequest else intef

    def Tenant_ListResourceGetApi(self, header_request_id=None, rgroup=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/sensego/v1/tenant/list-resource API """
        """  params: 
                参数名称：header.request_id　类型：string　描述：null
                参数名称：rgroup　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": "",
                    "units": [
                        {
                            "created_at": "",
                            "host": "",
                            "name": "",
                            "prom_name": "",
                            "resource_id": "",
                            "rgroup": "",
                            "rstype": "[SFD]SFD/GPU/MONGO",
                            "tags": [
                                {
                                    "create_at": "",
                                    "name": "",
                                    "score": 0,
                                    "type": "[STATIC]STATIC/DYNAMIC",
                                    "update_at": "",
                                    "value": ""
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("argusRrs", "Tenant_ListResource")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("header.request_id", header_request_id)
        intef.update_params("rgroup", rgroup)
        return intef.request() if sendRequest else intef

    def Tenant_ListResourceByRsTypeGetApi(self, header_request_id=None, rstype=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/sensego/v1/tenant/list-resource-by-rstype API """
        """  params: 
                参数名称：header.request_id　类型：string　描述：null
                参数名称：rstype　类型：string　描述： - SFD: 0 = SFD
 - GPU: 1 = GPU
 - MONGO: 2 = MONG
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": "",
                    "units": [
                        {
                            "created_at": "",
                            "host": "",
                            "name": "",
                            "prom_name": "",
                            "resource_id": "",
                            "rgroup": "",
                            "rstype": "[SFD]SFD/GPU/MONGO",
                            "tags": [
                                {
                                    "create_at": "",
                                    "name": "",
                                    "score": 0,
                                    "type": "[STATIC]STATIC/DYNAMIC",
                                    "update_at": "",
                                    "value": ""
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("argusRrs", "Tenant_ListResourceByRsType")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("header.request_id", header_request_id)
        intef.update_params("rstype", rstype)
        return intef.request() if sendRequest else intef

    def Tenant_ListTagGetApi(self, header_request_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/sensego/v1/tenant/list-tag API """
        """  params: 
                参数名称：header.request_id　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": "",
                    "tags": [
                        {
                            "create_at": "",
                            "name": "",
                            "score": 0,
                            "type": "[STATIC]STATIC/DYNAMIC",
                            "update_at": "",
                            "value": ""
                        }
                    ]
                }

        """
        intef = collections.interface("argusRrs", "Tenant_ListTag")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("header.request_id", header_request_id)
        return intef.request() if sendRequest else intef

    def Tenant_LookupPostApi(self, ak=None, tags=None, rsType=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/lookup API """
        """  body: 
                {
                    "ak": "",
                    "rsType": "[SFD]SFD/GPU/MONGO",
                    "tags": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "host": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_Lookup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("ak", ak)
        intef.update_body("tags", tags)
        intef.update_body("rsType", rsType)
        return intef.request() if sendRequest else intef

    def Tenant_UpdateRGroupPostApi(self, rgroup=None, new_rgroup=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/update-r-group API """
        """  body: 
                {
                    "new_rgroup": "",
                    "rgroup": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_UpdateRGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("rgroup", rgroup)
        intef.update_body("new_rgroup", new_rgroup)
        return intef.request() if sendRequest else intef

    def Tenant_UpdateResourcePostApi(self, unit=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/update-resource API """
        """  body: 
                {
                    "unit": {
                        "created_at": "",
                        "host": "",
                        "name": "",
                        "prom_name": "",
                        "resource_id": "",
                        "rgroup": "",
                        "rstype": "[SFD]SFD/GPU/MONGO",
                        "tags": [
                            {
                                "create_at": "",
                                "name": "",
                                "score": 0,
                                "type": "[STATIC]STATIC/DYNAMIC",
                                "update_at": "",
                                "value": ""
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_UpdateResource")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("unit", unit)
        return intef.request() if sendRequest else intef

    def Tenant_UpdateTagPostApi(self, tag=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/sensego/v1/tenant/update-tag API """
        """  body: 
                {
                    "tag": {
                        "create_at": "",
                        "name": "",
                        "score": 0,
                        "type": "[STATIC]STATIC/DYNAMIC",
                        "update_at": "",
                        "value": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "request_id": ""
                }

        """
        intef = collections.interface("argusRrs", "Tenant_UpdateTag")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("tag", tag)
        return intef.request() if sendRequest else intef

