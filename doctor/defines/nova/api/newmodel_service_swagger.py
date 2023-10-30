#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class NewmodelSwaggerApi(BaseApi):
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

    def ModelService_ListInternalModelsGetApi(self, model_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListInternalModels 获取 internal model列表 """
        """  path: [get]/v1/llm/internal_models API """
        """  params: 
                参数名称：model_id　类型：string　描述：[optional] model id, 格式: [a-zA-Z0-9\-]
        """
        """  resp:
                200(A successful response.):
                {
                    "internal_models": [
                        {
                            "created_at": "",
                            "extra_info": {},
                            "id": "",
                            "inference_addresses": {},
                            "model_id": "",
                            "parent_internal_id": "",
                            "root_internal_id": "",
                            "updated_at": "",
                            "uri": ""
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
        intef = collections.interface("NewModel", "ModelService_ListInternalModels")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("model_id", model_id)
        return intef.request() if sendRequest else intef

    def ModelService_CreateInternalModelPostApi(self, id=None, model_id=None, root_internal_id=None, parent_internal_id=None, extra_info=None, uri=None, inference_address=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CreateInternalModel 创建 internal model """
        """  path: [post]/v1/llm/internal_models API """
        """  body: 
                {
                    "extra_info": {},
                    "id": "",
                    "inference_address": {},
                    "model_id": "",
                    "parent_internal_id": "",
                    "root_internal_id": "",
                    "uri": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "internal_model": {
                        "created_at": "",
                        "extra_info": {},
                        "id": "",
                        "inference_addresses": {},
                        "model_id": "",
                        "parent_internal_id": "",
                        "root_internal_id": "",
                        "updated_at": "",
                        "uri": ""
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
        intef = collections.interface("NewModel", "ModelService_CreateInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("model_id", model_id)
        intef.update_body("root_internal_id", root_internal_id)
        intef.update_body("parent_internal_id", parent_internal_id)
        intef.update_body("extra_info", extra_info)
        intef.update_body("uri", uri)
        intef.update_body("inference_address", inference_address)
        return intef.request() if sendRequest else intef

    def ModelService_GetInternalModelGetApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetInternalModel 获取 internal model by id """
        """  path: [get]/v1/llm/internal_models/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "internal_model": {
                        "created_at": "",
                        "extra_info": {},
                        "id": "",
                        "inference_addresses": {},
                        "model_id": "",
                        "parent_internal_id": "",
                        "root_internal_id": "",
                        "updated_at": "",
                        "uri": ""
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
        intef = collections.interface("NewModel", "ModelService_GetInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def ModelService_DeleteInternalModelDeleteApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteInternalModel 删除 internal model """
        """  path: [delete]/v1/llm/internal_models/{id} API """
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
        intef = collections.interface("NewModel", "ModelService_DeleteInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def ModelService_UpdateInternalModelPutApi(self, id, root_internal_id=None, parent_internal_id=None, extra_info=None, uri=None, inference_address=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  UpdateInternalModel 更新 internal model """
        """  path: [put]/v1/llm/internal_models/{id} API """
        """  body: 
                {
                    "extra_info": {},
                    "inference_address": {},
                    "parent_internal_id": "",
                    "root_internal_id": "",
                    "uri": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "internal_model": {
                        "created_at": "",
                        "extra_info": {},
                        "id": "",
                        "inference_addresses": {},
                        "model_id": "",
                        "parent_internal_id": "",
                        "root_internal_id": "",
                        "updated_at": "",
                        "uri": ""
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
        intef = collections.interface("NewModel", "ModelService_UpdateInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        intef.update_body("root_internal_id", root_internal_id)
        intef.update_body("parent_internal_id", parent_internal_id)
        intef.update_body("extra_info", extra_info)
        intef.update_body("uri", uri)
        intef.update_body("inference_address", inference_address)
        return intef.request() if sendRequest else intef

    def ModelService_ListModelRoutesGetApi(self, model_id=None, account_id=None, route_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListModelRoutes 获取model的路由策略 """
        """  path: [get]/v1/llm/model_routes API """
        """  params: 
                参数名称：model_id　类型：string　描述：[optional] model id, 格式: [a-zA-Z0-9\-]+
                参数名称：account_id　类型：string　描述：[optional] account id, 格式: [a-zA-Z0-9\-]+
                参数名称：route_type　类型：string　描述：[optional] route typ
        """
        """  resp:
                200(A successful response.):
                {
                    "model_routes": [
                        {
                            "account": "",
                            "created_at": "",
                            "id": "",
                            "model_id": "",
                            "model_internal_id": "",
                            "primary": false,
                            "type": "[ROUTE_TYPE_UNKNOWN]ROUTE_TYPE_UNKNOWN/ROUTE_TYPE_WEIGHT/ROUTE_TYPE_ACCOUNT",
                            "updated_at": "",
                            "weight": ""
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
        intef = collections.interface("NewModel", "ModelService_ListModelRoutes")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("model_id", model_id)
        intef.update_params("account_id", account_id)
        intef.update_params("route_type", route_type)
        return intef.request() if sendRequest else intef

    def ModelService_AddModelRoutePostApi(self, model_id=None, model_internal_id=None, type=None, account=None, weight=None, primary=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AddModelRoute 添加model的路由策略 """
        """  path: [post]/v1/llm/model_routes API """
        """  body: 
                {
                    "account": "",
                    "model_id": "",
                    "model_internal_id": "",
                    "primary": false,
                    "type": "[ROUTE_TYPE_UNKNOWN]ROUTE_TYPE_UNKNOWN/ROUTE_TYPE_WEIGHT/ROUTE_TYPE_ACCOUNT",
                    "weight": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "model_route": {
                        "account": "",
                        "created_at": "",
                        "id": "",
                        "model_id": "",
                        "model_internal_id": "",
                        "primary": false,
                        "type": "[ROUTE_TYPE_UNKNOWN]ROUTE_TYPE_UNKNOWN/ROUTE_TYPE_WEIGHT/ROUTE_TYPE_ACCOUNT",
                        "updated_at": "",
                        "weight": ""
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
        intef = collections.interface("NewModel", "ModelService_AddModelRoute")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model_id", model_id)
        intef.update_body("model_internal_id", model_internal_id)
        intef.update_body("type", type)
        intef.update_body("account", account)
        intef.update_body("weight", weight)
        intef.update_body("primary", primary)
        return intef.request() if sendRequest else intef

    def ModelService_DeleteModelRouteDeleteApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteModelRoute 删除model的路由策略 """
        """  path: [delete]/v1/llm/model_routes/{id} API """
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
        intef = collections.interface("NewModel", "ModelService_DeleteModelRoute")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def ModelService_UpdateModelRoutePutApi(self, id, account=None, weight=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  UpdateModelRoute 更新model的路由策略 """
        """  path: [put]/v1/llm/model_routes/{id} API """
        """  body: 
                {
                    "account": "",
                    "weight": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "model_route": {
                        "account": "",
                        "created_at": "",
                        "id": "",
                        "model_id": "",
                        "model_internal_id": "",
                        "primary": false,
                        "type": "[ROUTE_TYPE_UNKNOWN]ROUTE_TYPE_UNKNOWN/ROUTE_TYPE_WEIGHT/ROUTE_TYPE_ACCOUNT",
                        "updated_at": "",
                        "weight": ""
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
        intef = collections.interface("NewModel", "ModelService_UpdateModelRoute")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        intef.update_body("account", account)
        intef.update_body("weight", weight)
        return intef.request() if sendRequest else intef

    def ModelService_ListModelsV2GetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  [openapi] ListModels 获取 model 的列表 """
        """  path: [get]/v1/llm/models API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "data": [
                        {
                            "created_at": "",
                            "id": "",
                            "object": "[OBJECT_TYPE_UNKNOWN]OBJECT_TYPE_UNKNOWN/MODEL_PERMISSION/MODEL/LIST",
                            "owned_by": "",
                            "parent": "",
                            "permission": [],
                            "root": "",
                            "type": "[MODEL_TYPE_UNKNOWN]MODEL_TYPE_UNKNOWN/BASE_MODEL/FINE_TUNED_MODEL",
                            "updated_at": ""
                        }
                    ],
                    "object": "[OBJECT_TYPE_UNKNOWN]OBJECT_TYPE_UNKNOWN/MODEL_PERMISSION/MODEL/LIST"
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
        intef = collections.interface("NewModel", "ModelService_ListModelsV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ModelService_CreateModelV2PostApi(self, id=None, type=None, allow_fine_tuning=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CreateModel 创建 model """
        """  path: [post]/v1/llm/models API """
        """  body: 
                {
                    "allow_fine_tuning": false,
                    "id": "",
                    "type": "[MODEL_TYPE_UNKNOWN]MODEL_TYPE_UNKNOWN/BASE_MODEL/FINE_TUNED_MODEL"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "model": {
                        "created_at": "",
                        "id": "",
                        "object": "[OBJECT_TYPE_UNKNOWN]OBJECT_TYPE_UNKNOWN/MODEL_PERMISSION/MODEL/LIST",
                        "owned_by": "",
                        "parent": "",
                        "permission": [],
                        "root": "",
                        "type": "[MODEL_TYPE_UNKNOWN]MODEL_TYPE_UNKNOWN/BASE_MODEL/FINE_TUNED_MODEL",
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
        intef = collections.interface("NewModel", "ModelService_CreateModelV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("type", type)
        intef.update_body("allow_fine_tuning", allow_fine_tuning)
        return intef.request() if sendRequest else intef

    def ModelService_GetModelV2GetApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  [openapi] GetModel 获取 model 的信息 """
        """  path: [get]/v1/llm/models/{id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "data": {
                        "created_at": "",
                        "id": "",
                        "object": "[OBJECT_TYPE_UNKNOWN]OBJECT_TYPE_UNKNOWN/MODEL_PERMISSION/MODEL/LIST",
                        "owned_by": "",
                        "parent": "",
                        "permission": [],
                        "root": "",
                        "type": "[MODEL_TYPE_UNKNOWN]MODEL_TYPE_UNKNOWN/BASE_MODEL/FINE_TUNED_MODEL",
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
        intef = collections.interface("NewModel", "ModelService_GetModelV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def ModelService_DeleteModelV2DeleteApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteModel 移除 model,  移除access 和 route """
        """  path: [delete]/v1/llm/models/{id} API """
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
        intef = collections.interface("NewModel", "ModelService_DeleteModelV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def ModelService_UpdateModelV2PutApi(self, id, allow_fine_tuning=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  UpdateModel 更新 model """
        """  path: [put]/v1/llm/models/{id} API """
        """  body: 
                {
                    "allow_fine_tuning": false
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "data": {
                        "created_at": "",
                        "id": "",
                        "object": "[OBJECT_TYPE_UNKNOWN]OBJECT_TYPE_UNKNOWN/MODEL_PERMISSION/MODEL/LIST",
                        "owned_by": "",
                        "parent": "",
                        "permission": [],
                        "root": "",
                        "type": "[MODEL_TYPE_UNKNOWN]MODEL_TYPE_UNKNOWN/BASE_MODEL/FINE_TUNED_MODEL",
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
        intef = collections.interface("NewModel", "ModelService_UpdateModelV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        intef.update_body("allow_fine_tuning", allow_fine_tuning)
        return intef.request() if sendRequest else intef

    def ModelService_ListModelAccessGetApi(self, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListModelAccess 获取用户对Model的访问权限 """
        """  path: [get]/v1/llm/models/{id}/access API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "account_ids": [],
                    "id": "",
                    "public_access": false
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
        intef = collections.interface("NewModel", "ModelService_ListModelAccess")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def ModelService_DeleteModelAccessDeleteApi(self, id, account_ids=None, access_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteModelAccess 删除用户对Model的访问权限 """
        """  path: [delete]/v1/llm/models/{id}/access API """
        """  params: 
                参数名称：account_ids　类型：array　描述：[optional] account id, only valid when access_type is ACCOUNT
                参数名称：access_type　类型：string　描述：[required] access typ
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
        intef = collections.interface("NewModel", "ModelService_DeleteModelAccess")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_ids", account_ids)
        intef.update_params("access_type", access_type)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def ModelService_AddModelAccessPostApi(self, id, account_ids=None, access_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AddModelAccess 添加用户对Model的访问权限 """
        """  path: [post]/v1/llm/models/{id}/access API """
        """  body: 
                {
                    "access_type": "[ACCESS_TYPE_UNKNOWN]ACCESS_TYPE_UNKNOWN/ACCESS_TYPE_PUBLIC/ACCESS_TYPE_ACCOUNT",
                    "account_ids": []
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
        intef = collections.interface("NewModel", "ModelService_AddModelAccess")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("id", id)
        intef.update_body("account_ids", account_ids)
        intef.update_body("access_type", access_type)
        return intef.request() if sendRequest else intef

    def ModelService_GetRoutedModelGetApi(self, id, account_id=None, take_weight=None, permissions=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/v1/llm/models/{id}/routed_model API """
        """  params: 
                参数名称：account_id　类型：string　描述：[required] account id
                参数名称：take_weight　类型：boolean　描述：[required] take weight, default true
                参数名称：permissions　类型：array　描述：[optional
        """
        """  resp:
                200(A successful response.):
                {
                    "internal_model": {
                        "created_at": "",
                        "extra_info": {},
                        "id": "",
                        "inference_addresses": {},
                        "model_id": "",
                        "parent_internal_id": "",
                        "root_internal_id": "",
                        "updated_at": "",
                        "uri": ""
                    },
                    "model": {
                        "created_at": "",
                        "id": "",
                        "object": "[OBJECT_TYPE_UNKNOWN]OBJECT_TYPE_UNKNOWN/MODEL_PERMISSION/MODEL/LIST",
                        "owned_by": "",
                        "parent": "",
                        "permission": [],
                        "root": "",
                        "type": "[MODEL_TYPE_UNKNOWN]MODEL_TYPE_UNKNOWN/BASE_MODEL/FINE_TUNED_MODEL",
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
        intef = collections.interface("NewModel", "ModelService_GetRoutedModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        intef.update_params("take_weight", take_weight)
        intef.update_params("permissions", permissions)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

