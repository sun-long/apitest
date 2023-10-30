#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class ModelSwaggerApi(BaseApi):
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

    def ModelService_ListImgenModelsV2GetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  [openapi] ListImgenModelsV2 获取 model 的列表 """
        """  path: [get]/v1/imgen/models API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "data": [
                        {
                            "created_at": "",
                            "display_name": "",
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
        intef = collections.interface("Model", "ModelService_ListImgenModelsV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ModelService_GetImgenModelV2GetApi(self, model_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  [openapi] GetImgenModelV2 获取 model 的信息 """
        """  path: [get]/v1/imgen/models/{model_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "data": {
                        "created_at": "",
                        "display_name": "",
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
        intef = collections.interface("Model", "ModelService_GetImgenModelV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("model_id", model_id)
        return intef.request() if sendRequest else intef

    def ModelService_DeleteImgenModelDeleteApi(self, model_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteImgenModel 移除 imgen model,  移除access 和 route... """
        """  path: [delete]/v1/imgen/models/{model_id} API """
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
        intef = collections.interface("Model", "ModelService_DeleteImgenModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("model_id", model_id)
        return intef.request() if sendRequest else intef

    def ModelService_ListInternalModelsGetApi(self, model_id=None, owner=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListInternalModels 获取 internal model列表 """
        """  path: [get]/v1/llm/internal_models API """
        """  params: 
                参数名称：model_id　类型：string　描述：[optional] model id, 格式: [a-zA-Z0-9\-]+
                参数名称：owner　类型：string　描述：[optional] model owner, model_id不为空时，必填
                参数名称：type　类型：string　描述：[optional] model 的类型: 基模型/微调模
        """
        """  resp:
                200(A successful response.):
                {
                    "internal_models": [
                        {
                            "created_at": "",
                            "extra_info": {},
                            "inference_addresses": {},
                            "internal_id": "",
                            "model_id": "",
                            "owned_by": "",
                            "parent_internal_id": "",
                            "parent_internal_uri": "",
                            "root_internal_id": "",
                            "root_internal_uri": "",
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
        intef = collections.interface("Model", "ModelService_ListInternalModels")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("model_id", model_id)
        intef.update_params("owner", owner)
        intef.update_params("type", type)
        return intef.request() if sendRequest else intef

    def ModelService_CreateInternalModelPostApi(self, internal_id=None, model_id=None, owner=None, root_internal_id=None, parent_internal_id=None, extra_info=None, uri=None, inference_address=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CreateInternalModel 创建 internal model """
        """  path: [post]/v1/llm/internal_models API """
        """  body: 
                {
                    "extra_info": {},
                    "inference_address": {},
                    "internal_id": "",
                    "model_id": "",
                    "owner": "",
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
                        "inference_addresses": {},
                        "internal_id": "",
                        "model_id": "",
                        "owned_by": "",
                        "parent_internal_id": "",
                        "parent_internal_uri": "",
                        "root_internal_id": "",
                        "root_internal_uri": "",
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
        intef = collections.interface("Model", "ModelService_CreateInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("internal_id", internal_id)
        intef.update_body("model_id", model_id)
        intef.update_body("owner", owner)
        intef.update_body("root_internal_id", root_internal_id)
        intef.update_body("parent_internal_id", parent_internal_id)
        intef.update_body("extra_info", extra_info)
        intef.update_body("uri", uri)
        intef.update_body("inference_address", inference_address)
        return intef.request() if sendRequest else intef

    def ModelService_GetInternalModelGetApi(self, internal_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetInternalModel 获取 internal model by id """
        """  path: [get]/v1/llm/internal_models/{internal_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "internal_model": {
                        "created_at": "",
                        "extra_info": {},
                        "inference_addresses": {},
                        "internal_id": "",
                        "model_id": "",
                        "owned_by": "",
                        "parent_internal_id": "",
                        "parent_internal_uri": "",
                        "root_internal_id": "",
                        "root_internal_uri": "",
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
        intef = collections.interface("Model", "ModelService_GetInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("internal_id", internal_id)
        return intef.request() if sendRequest else intef

    def ModelService_DeleteInternalModelDeleteApi(self, internal_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteInternalModel 删除 internal model """
        """  path: [delete]/v1/llm/internal_models/{internal_id} API """
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
        intef = collections.interface("Model", "ModelService_DeleteInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("internal_id", internal_id)
        return intef.request() if sendRequest else intef

    def ModelService_UpdateInternalModelPutApi(self, internal_id, root_internal_id=None, parent_internal_id=None, extra_info=None, uri=None, inference_address=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  UpdateInternalModel 更新 internal model """
        """  path: [put]/v1/llm/internal_models/{internal_id} API """
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
                        "inference_addresses": {},
                        "internal_id": "",
                        "model_id": "",
                        "owned_by": "",
                        "parent_internal_id": "",
                        "parent_internal_uri": "",
                        "root_internal_id": "",
                        "root_internal_uri": "",
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
        intef = collections.interface("Model", "ModelService_UpdateInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("internal_id", internal_id)
        intef.update_body("root_internal_id", root_internal_id)
        intef.update_body("parent_internal_id", parent_internal_id)
        intef.update_body("extra_info", extra_info)
        intef.update_body("uri", uri)
        intef.update_body("inference_address", inference_address)
        return intef.request() if sendRequest else intef

    def ModelService_ListModelRoutesGetApi(self, model_id=None, owner=None, account_id=None, primary=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListModelRoutes 获取model的路由策略 """
        """  path: [get]/v1/llm/model_routes API """
        """  params: 
                参数名称：model_id　类型：string　描述：[optional] model id, 格式: [a-zA-Z0-9\-]+
                参数名称：owner　类型：string　描述：[optional] model owner, model id不为空时，必填
                参数名称：account_id　类型：string　描述：[optional] account id, 格式: [a-zA-Z0-9\-]+
                参数名称：primary　类型：boolean　描述：[optional] primar
        """
        """  resp:
                200(A successful response.):
                {
                    "model_routes": [
                        {
                            "account": "",
                            "created_at": "",
                            "internal_id": "",
                            "model_id": "",
                            "owner": "",
                            "primary": false,
                            "route_id": "",
                            "updated_at": "",
                            "weight": 0
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
        intef = collections.interface("Model", "ModelService_ListModelRoutes")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("model_id", model_id)
        intef.update_params("owner", owner)
        intef.update_params("account_id", account_id)
        intef.update_params("primary", primary)
        return intef.request() if sendRequest else intef

    def ModelService_AddModelRoutePostApi(self, model_id=None, owner=None, model_internal_id=None, account=None, weight=None, primary=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AddModelRoute 添加model的路由策略 """
        """  path: [post]/v1/llm/model_routes API """
        """  body: 
                {
                    "account": "",
                    "model_id": "",
                    "model_internal_id": "",
                    "owner": "",
                    "primary": false,
                    "weight": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "model_route": {
                        "account": "",
                        "created_at": "",
                        "internal_id": "",
                        "model_id": "",
                        "owner": "",
                        "primary": false,
                        "route_id": "",
                        "updated_at": "",
                        "weight": 0
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
        intef = collections.interface("Model", "ModelService_AddModelRoute")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model_id", model_id)
        intef.update_body("owner", owner)
        intef.update_body("model_internal_id", model_internal_id)
        intef.update_body("account", account)
        intef.update_body("weight", weight)
        intef.update_body("primary", primary)
        return intef.request() if sendRequest else intef

    def ModelService_DeleteModelRouteDeleteApi(self, route_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteModelRoute 删除model的路由策略 """
        """  path: [delete]/v1/llm/model_routes/{route_id} API """
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
        intef = collections.interface("Model", "ModelService_DeleteModelRoute")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("route_id", route_id)
        return intef.request() if sendRequest else intef

    def ModelService_UpdateModelRoutePutApi(self, route_id, account_id=None, weight=None, primary=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  UpdateModelRoute 更新model的路由策略 """
        """  path: [put]/v1/llm/model_routes/{route_id} API """
        """  body: 
                {
                    "account_id": "",
                    "primary": false,
                    "weight": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "model_route": {
                        "account": "",
                        "created_at": "",
                        "internal_id": "",
                        "model_id": "",
                        "owner": "",
                        "primary": false,
                        "route_id": "",
                        "updated_at": "",
                        "weight": 0
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
        intef = collections.interface("Model", "ModelService_UpdateModelRoute")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("route_id", route_id)
        intef.update_body("account_id", account_id)
        intef.update_body("weight", weight)
        intef.update_body("primary", primary)
        return intef.request() if sendRequest else intef

    def ModelService_ListLLMModelsV2GetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  [openapi] ListLLMModelsV2 获取 model 的列表 """
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
        intef = collections.interface("Model", "ModelService_ListLLMModelsV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ModelService_CreateModelV2PostApi(self, model_id=None, type=None, permissions=None, owner=None, display_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CreateModelV2 创建 model """
        """  path: [post]/v1/llm/models API """
        """  body: 
                {
                    "display_name": "",
                    "model_id": "",
                    "owner": "",
                    "permissions": [],
                    "type": "[MODEL_TYPE_UNKNOWN]MODEL_TYPE_UNKNOWN/BASE_MODEL/FINE_TUNED_MODEL"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "model": {
                        "created_at": "",
                        "display_name": "",
                        "model_id": "",
                        "object": "[OBJECT_TYPE_UNKNOWN]OBJECT_TYPE_UNKNOWN/MODEL_PERMISSION/MODEL/LIST",
                        "owned_by": "",
                        "permission": [],
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
        intef = collections.interface("Model", "ModelService_CreateModelV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model_id", model_id)
        intef.update_body("type", type)
        intef.update_body("permissions", permissions)
        intef.update_body("owner", owner)
        intef.update_body("display_name", display_name)
        return intef.request() if sendRequest else intef

    def ModelService_ListModelAccessGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListModelAccess 获取用户对Model的访问权限 """
        """  path: [get]/v1/llm/models/access API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "accesses": [
                        {
                            "account_id": [],
                            "model_id": "",
                            "owned_by": "",
                            "public_access": false
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
        intef = collections.interface("Model", "ModelService_ListModelAccess")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ModelService_ListPermissionsGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListPermissions 获取所有permission """
        """  path: [get]/v1/llm/models/permissions API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "permissions": []
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
        intef = collections.interface("Model", "ModelService_ListPermissions")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ModelService_GetLLMModelV2GetApi(self, model_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  [openapi] GetLLMModelV2 获取 model 的信息 """
        """  path: [get]/v1/llm/models/{model_id} API """
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
        intef = collections.interface("Model", "ModelService_GetLLMModelV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("model_id", model_id)
        return intef.request() if sendRequest else intef

    def ModelService_DeleteLLMModelDeleteApi(self, model_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteLLMModel 移除 llm model,  移除access 和 route，需要提... """
        """  path: [delete]/v1/llm/models/{model_id} API """
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
        intef = collections.interface("Model", "ModelService_DeleteLLMModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("model_id", model_id)
        return intef.request() if sendRequest else intef

    def ModelService_UpdateModelV2PutApi(self, model_id, owner=None, permission=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  UpdateModel 更新 model """
        """  path: [put]/v1/llm/models/{model_id} API """
        """  body: 
                {
                    "owner": "",
                    "permission": []
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "data": {
                        "created_at": "",
                        "display_name": "",
                        "model_id": "",
                        "object": "[OBJECT_TYPE_UNKNOWN]OBJECT_TYPE_UNKNOWN/MODEL_PERMISSION/MODEL/LIST",
                        "owned_by": "",
                        "permission": [],
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
        intef = collections.interface("Model", "ModelService_UpdateModelV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("model_id", model_id)
        intef.update_body("owner", owner)
        intef.update_body("permission", permission)
        return intef.request() if sendRequest else intef

    def ModelService_DeleteModelAccessDeleteApi(self, model_id, owner=None, account_ids=None, access_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteModelAccess 删除用户对Model的访问权限 """
        """  path: [delete]/v1/llm/models/{model_id}/access API """
        """  params: 
                参数名称：owner　类型：string　描述：[required] model owner
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
        intef = collections.interface("Model", "ModelService_DeleteModelAccess")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("owner", owner)
        intef.update_params("account_ids", account_ids)
        intef.update_params("access_type", access_type)
        intef.set_path_param("model_id", model_id)
        return intef.request() if sendRequest else intef

    def ModelService_AddModelAccessPostApi(self, model_id, owner=None, account_ids=None, access_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AddModelAccess 添加用户对Model的访问权限 """
        """  path: [post]/v1/llm/models/{model_id}/access API """
        """  body: 
                {
                    "access_type": "[ACCESS_TYPE_UNKNOWN]ACCESS_TYPE_UNKNOWN/ACCESS_TYPE_PUBLIC/ACCESS_TYPE_ACCOUNT",
                    "account_ids": [],
                    "owner": ""
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
        intef = collections.interface("Model", "ModelService_AddModelAccess")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("model_id", model_id)
        intef.update_body("owner", owner)
        intef.update_body("account_ids", account_ids)
        intef.update_body("access_type", access_type)
        return intef.request() if sendRequest else intef

    def ModelService_GetRoutedModelGetApi(self, model_id, owner=None, take_weight=None, permissions=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/v1/llm/models/{model_id}/routed_model API """
        """  params: 
                参数名称：owner　类型：string　描述：[deprecated] deprecated
                参数名称：take_weight　类型：boolean　描述：[required] take weight, default true
                参数名称：permissions　类型：array　描述：[optional
        """
        """  resp:
                200(A successful response.):
                {
                    "internal_model": {
                        "created_at": "",
                        "extra_info": {},
                        "inference_addresses": {},
                        "internal_id": "",
                        "model_id": "",
                        "owned_by": "",
                        "parent_internal_id": "",
                        "parent_internal_uri": "",
                        "root_internal_id": "",
                        "root_internal_uri": "",
                        "updated_at": "",
                        "uri": ""
                    },
                    "model": {
                        "created_at": "",
                        "display_name": "",
                        "model_id": "",
                        "object": "[OBJECT_TYPE_UNKNOWN]OBJECT_TYPE_UNKNOWN/MODEL_PERMISSION/MODEL/LIST",
                        "owned_by": "",
                        "permission": [],
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
        intef = collections.interface("Model", "ModelService_GetRoutedModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("owner", owner)
        intef.update_params("take_weight", take_weight)
        intef.update_params("permissions", permissions)
        intef.set_path_param("model_id", model_id)
        return intef.request() if sendRequest else intef

