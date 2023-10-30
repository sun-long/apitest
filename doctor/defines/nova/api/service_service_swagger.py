#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class ServiceSwaggerApi(BaseApi):
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

    def UserSrv_AddPendingAuditInfoPostApi(self, pending_audit_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/AddPendingAuditInfo API """
        """  body: 
                {
                    "pending_audit_info": {
                        "business_qpd": "",
                        "business_scene": "",
                        "business_scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                        "cellphone": "",
                        "company_homepage": "",
                        "company_name": "",
                        "company_type": "[CompanyType_Unset]CompanyType_Unset/Startup/SmallAndMicro/Medium/Large/StateOwned",
                        "email": "",
                        "id": "",
                        "inviter": "",
                        "job_title": "",
                        "lm": {
                            "internal_api": false,
                            "internal_multi_chat": false,
                            "lm_chat": false,
                            "lm_config": {
                                "chat_qps": 0,
                                "code_qps": 0,
                                "cv_qps": 0,
                                "default_offline_search": false,
                                "default_online": false,
                                "finetune_job_count": 0,
                                "knowledge_base_max_count": 0,
                                "knowledge_retrieve_timeout": 0,
                                "miaohua_qps": 0,
                                "online_knowledge_mode": 0,
                                "serving_count": 0
                            },
                            "lm_cv": false,
                            "lm_finetune": false,
                            "lm_knowledgebase": false,
                            "lm_miaohua": false,
                            "lm_role_play": false,
                            "lm_sense_code": false
                        },
                        "name": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "audit_info_id": ""
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
        intef = collections.interface("Service", "UserSrv_AddPendingAuditInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("pending_audit_info", pending_audit_info)
        return intef.request() if sendRequest else intef

    def UserSrv_AdminGetAccountUserListGetApi(self, user_id=None, user_name=None, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  系统工具 超级管理员用户管理 """
        """  path: [get]/v1/AdminGetAccountUserList API """
        """  params: 
                参数名称：user_id　类型：string　描述：userID 可选
                参数名称：user_name　类型：string　描述：用户名 可选
                参数名称：paging.offset　类型：integer　描述：null
                参数名称：paging.limit　类型：integer　描述：null
                参数名称：paging.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "account_user_info": [
                        {
                            "created_at": "",
                            "last_login_at": "",
                            "nick_name": "",
                            "user_id": "",
                            "user_name": ""
                        }
                    ],
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
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
        intef = collections.interface("Service", "UserSrv_AdminGetAccountUserList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("user_id", user_id)
        intef.update_params("user_name", user_name)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def UserSrv_AdminGetUserPageRoleListGetApi(self, user_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员获取其他用户的 page_role """
        """  path: [get]/v1/AdminGetUserPageRoleList API """
        """  params: 
                参数名称：user_id　类型：string　描述：查询的用户 i
        """
        """  resp:
                200(A successful response.):
                {
                    "page_roles": [
                        {
                            "authorized": false,
                            "page_role": {
                                "display_name": "",
                                "name": ""
                            }
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
        intef = collections.interface("Service", "UserSrv_AdminGetUserPageRoleList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("user_id", user_id)
        return intef.request() if sendRequest else intef

    def UserSrv_AdminUpdateUserPageRolePostApi(self, user_id=None, page_roles=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员更新用户的 page_role """
        """  path: [post]/v1/AdminUpdateUserPageRole API """
        """  body: 
                {
                    "page_roles": [
                        {
                            "authorized": false,
                            "page_role": {
                                "display_name": "",
                                "name": ""
                            }
                        }
                    ],
                    "user_id": ""
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
        intef = collections.interface("Service", "UserSrv_AdminUpdateUserPageRole")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("page_roles", page_roles)
        return intef.request() if sendRequest else intef

    def UserSrv_AuditPostApi(self, audit_list=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/Audit API """
        """  body: 
                {
                    "audit_list": [
                        {
                            "audit_detail": {
                                "audit_state": "[AuditStateUnset]AuditStateUnset/Waiting/Pass/Prohibit/Ignore",
                                "lm": {
                                    "internal_api": false,
                                    "internal_multi_chat": false,
                                    "lm_chat": false,
                                    "lm_config": {
                                        "chat_qps": 0,
                                        "code_qps": 0,
                                        "cv_qps": 0,
                                        "default_offline_search": false,
                                        "default_online": false,
                                        "finetune_job_count": 0,
                                        "knowledge_base_max_count": 0,
                                        "knowledge_retrieve_timeout": 0,
                                        "miaohua_qps": 0,
                                        "online_knowledge_mode": 0,
                                        "serving_count": 0
                                    },
                                    "lm_cv": false,
                                    "lm_finetune": false,
                                    "lm_knowledgebase": false,
                                    "lm_miaohua": false,
                                    "lm_role_play": false,
                                    "lm_sense_code": false
                                }
                            },
                            "audit_info_id": ""
                        }
                    ]
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "audit_result_list": [
                        {
                            "account_id": "",
                            "audit_info_id": "",
                            "audit_info_processed": false,
                            "create_account_success": false,
                            "send_cellphone_message_success": false,
                            "send_email_success": false,
                            "user_id": "",
                            "username": ""
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
        intef = collections.interface("Service", "UserSrv_Audit")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("audit_list", audit_list)
        return intef.request() if sendRequest else intef

    def UserSrv_AuditCSVPostApi(self, csv=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/AuditCSV API """
        """  body: 
                {
                    "csv": ""
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
        intef = collections.interface("Service", "UserSrv_AuditCSV")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("csv", csv)
        return intef.request() if sendRequest else intef

    def UserSrv_AuthModelWhitelistPostApi(self, id=None, public_access=None, account_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  授权用户访问Model """
        """  path: [post]/v1/AuthModelWhitelist API """
        """  body: 
                {
                    "account_ids": [],
                    "id": "",
                    "public_access": false
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
        intef = collections.interface("Service", "UserSrv_AuthModelWhitelist")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("public_access", public_access)
        intef.update_body("account_ids", account_ids)
        return intef.request() if sendRequest else intef

    def UserSrv_CheckAccountListGetApi(self, all_account_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  检查输入的白名单账号是否存在 """
        """  path: [get]/v1/CheckAccountList API """
        """  params: 
                参数名称：all_account_ids　类型：array　描述：白名单账户ID列
        """
        """  resp:
                200(A successful response.):
                {
                    "all_account_results": [
                        {
                            "info": {
                                "account_id": "",
                                "account_name": ""
                            },
                            "result": 0
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
        intef = collections.interface("Service", "UserSrv_CheckAccountList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("all_account_ids", all_account_ids)
        return intef.request() if sendRequest else intef

    def UserSrv_CreateInternalModelPostApi(self, model_id=None, internal_id=None, root_internal_id=None, parent_internal_id=None, uri=None, extra_info=None, inference_address=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建模型实例 """
        """  path: [post]/v1/CreateInternalModel API """
        """  body: 
                {
                    "extra_info": "",
                    "inference_address": "",
                    "internal_id": "",
                    "model_id": "",
                    "parent_internal_id": "",
                    "root_internal_id": "",
                    "uri": ""
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
        intef = collections.interface("Service", "UserSrv_CreateInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model_id", model_id)
        intef.update_body("internal_id", internal_id)
        intef.update_body("root_internal_id", root_internal_id)
        intef.update_body("parent_internal_id", parent_internal_id)
        intef.update_body("uri", uri)
        intef.update_body("extra_info", extra_info)
        intef.update_body("inference_address", inference_address)
        return intef.request() if sendRequest else intef

    def UserSrv_CreateModelPostApi(self, id=None, model_type=None, model_permissions=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建模型 """
        """  path: [post]/v1/CreateModel API """
        """  body: 
                {
                    "id": "",
                    "model_permissions": [],
                    "model_type": "[ModelType_Unknown]ModelType_Unknown/BaseModel/FinetunedModel"
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
        intef = collections.interface("Service", "UserSrv_CreateModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("model_type", model_type)
        intef.update_body("model_permissions", model_permissions)
        return intef.request() if sendRequest else intef

    def UserSrv_DeleteAccountPostApi(self, id=None, account_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除账户 """
        """  path: [post]/v1/DeleteAccount API """
        """  body: 
                {
                    "account_name": "",
                    "id": ""
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
        intef = collections.interface("Service", "UserSrv_DeleteAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("account_name", account_name)
        return intef.request() if sendRequest else intef

    def UserSrv_DeleteInternalModelDeleteApi(self, internal_id=None, confirm_internal_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除模型实例 """
        """  path: [delete]/v1/DeleteInternalModel API """
        """  params: 
                参数名称：internal_id　类型：string　描述：模型实例ID, 格式: [a-zA-Z0-9\-\:]+
                参数名称：confirm_internal_id　类型：string　描述：模型实例ID的确认值, 格式: [a-zA-Z0-9\-\:]
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
        intef = collections.interface("Service", "UserSrv_DeleteInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("internal_id", internal_id)
        intef.update_params("confirm_internal_id", confirm_internal_id)
        return intef.request() if sendRequest else intef

    def UserSrv_DeleteModelDeleteApi(self, id=None, confirm_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除模型 """
        """  path: [delete]/v1/DeleteModel API """
        """  params: 
                参数名称：id　类型：string　描述：模型ID, 格式: [a-zA-Z0-9\-]+
                参数名称：confirm_id　类型：string　描述：模型ID的确认值, 格式: [a-zA-Z0-9\-]
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
        intef = collections.interface("Service", "UserSrv_DeleteModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        intef.update_params("confirm_id", confirm_id)
        return intef.request() if sendRequest else intef

    def UserSrv_GetAccountDetailGetApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取账户详情 """
        """  path: [get]/v1/GetAccountDetail API """
        """  params: 
                参数名称：id　类型：string　描述：I
        """
        """  resp:
                200(A successful response.):
                {
                    "account_id": "",
                    "account_name": "",
                    "authentication": "[Identity_Unauthenticated]Identity_Unauthenticated/Business/Individual",
                    "business_scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "cellphone": "",
                    "company_name": "",
                    "email": "",
                    "first_login": false,
                    "inviter": "",
                    "locale": "",
                    "name": ""
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
        intef = collections.interface("Service", "UserSrv_GetAccountDetail")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        return intef.request() if sendRequest else intef

    def UserSrv_GetAccountSubscriptionGetApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取账户订阅配置 """
        """  path: [get]/v1/GetAccountSubscription API """
        """  params: 
                参数名称：id　类型：string　描述：I
        """
        """  resp:
                200(A successful response.):
                {
                    "internal_api": false,
                    "internal_multi_chat": false,
                    "lm_chat": false,
                    "lm_config": {
                        "chat_qps": 0,
                        "code_qps": 0,
                        "cv_qps": 0,
                        "default_offline_search": false,
                        "default_online": false,
                        "finetune_job_count": 0,
                        "knowledge_base_max_count": 0,
                        "knowledge_retrieve_timeout": 0,
                        "miaohua_qps": 0,
                        "online_knowledge_mode": 0,
                        "serving_count": 0
                    },
                    "lm_cv": false,
                    "lm_finetune": false,
                    "lm_knowledgebase": false,
                    "lm_miaohua": false,
                    "lm_role_play": false,
                    "lm_sense_code": false
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
        intef = collections.interface("Service", "UserSrv_GetAccountSubscription")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        return intef.request() if sendRequest else intef

    def UserSrv_GetAllModelPermissionsGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询模型所有的权限 """
        """  path: [get]/v1/GetAllModelPermissions API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "model_permissions": []
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
        intef = collections.interface("Service", "UserSrv_GetAllModelPermissions")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def UserSrv_GetInternalModelGetApi(self, internal_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询模型实例 """
        """  path: [get]/v1/GetInternalModel API """
        """  params: 
                参数名称：internal_id　类型：string　描述：模型实例I
        """
        """  resp:
                200(A successful response.):
                {
                    "extra_info": "",
                    "inference_address": "",
                    "internal_id": "",
                    "model_id": "",
                    "parent_internal_id": "",
                    "root_internal_id": "",
                    "uri": ""
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
        intef = collections.interface("Service", "UserSrv_GetInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("internal_id", internal_id)
        return intef.request() if sendRequest else intef

    def UserSrv_GetModelAccessGetApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取模型的访问权限 """
        """  path: [get]/v1/GetModelAccess API """
        """  params: 
                参数名称：id　类型：string　描述：model i
        """
        """  resp:
                200(A successful response.):
                {
                    "public_access": false,
                    "whitelistAccount": [
                        {
                            "account_id": "",
                            "account_name": ""
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
        intef = collections.interface("Service", "UserSrv_GetModelAccess")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        return intef.request() if sendRequest else intef

    def UserSrv_GetStatApiOptionsGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取 stat 接口支持的 option """
        """  path: [get]/v1/GetStatApiOptions API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "chat_stat_opt_apis": [
                        {
                            "display_name": "",
                            "value": ""
                        }
                    ],
                    "chat_stat_opts": [
                        {
                            "display_name": "",
                            "value": ""
                        }
                    ],
                    "finetue_stat_opts": [
                        {
                            "display_name": "",
                            "value": ""
                        }
                    ],
                    "image_generation_opts": [
                        {
                            "display_name": "",
                            "value": ""
                        }
                    ],
                    "user_stat_opts": [
                        {
                            "display_name": "",
                            "value": ""
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
        intef = collections.interface("Service", "UserSrv_GetStatApiOptions")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def UserSrv_GetUserBaseInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取用户的基本信息，包含用户可以访问的 page """
        """  path: [get]/v1/GetUserBaseInfo API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "email": "",
                    "nick_name": "",
                    "page_roles": [
                        {
                            "display_name": "",
                            "name": ""
                        }
                    ],
                    "phone": "",
                    "user_id": "",
                    "user_name": ""
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
        intef = collections.interface("Service", "UserSrv_GetUserBaseInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def UserSrv_InternalAuditPostApi(self, email=None, lm=None, company_name=None, name=None, locale=None, inviter=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/InternalAudit API """
        """  body: 
                {
                    "company_name": "",
                    "email": "",
                    "inviter": "",
                    "lm": {
                        "internal_api": false,
                        "internal_multi_chat": false,
                        "lm_chat": false,
                        "lm_config": {
                            "chat_qps": 0,
                            "code_qps": 0,
                            "cv_qps": 0,
                            "default_offline_search": false,
                            "default_online": false,
                            "finetune_job_count": 0,
                            "knowledge_base_max_count": 0,
                            "knowledge_retrieve_timeout": 0,
                            "miaohua_qps": 0,
                            "online_knowledge_mode": 0,
                            "serving_count": 0
                        },
                        "lm_cv": false,
                        "lm_finetune": false,
                        "lm_knowledgebase": false,
                        "lm_miaohua": false,
                        "lm_role_play": false,
                        "lm_sense_code": false
                    },
                    "locale": "[CN]CN/HK",
                    "name": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "result": {
                        "account_id": "",
                        "audit_info_id": "",
                        "audit_info_processed": false,
                        "create_account_success": false,
                        "send_cellphone_message_success": false,
                        "send_email_success": false,
                        "user_id": "",
                        "username": ""
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
        intef = collections.interface("Service", "UserSrv_InternalAudit")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("email", email)
        intef.update_body("lm", lm)
        intef.update_body("company_name", company_name)
        intef.update_body("name", name)
        intef.update_body("locale", locale)
        intef.update_body("inviter", inviter)
        return intef.request() if sendRequest else intef

    def UserSrv_ListAccountGetApi(self, accountId=None, cond=None, account_activated=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/v1/ListAccount API """
        """  params: 
                参数名称：accountId　类型：string　描述：账户ID
                参数名称：cond　类型：string　描述：查询条件：账户名称、公司名称、联系人、联系邮箱
                参数名称：account_activated　类型：integer　描述：账户激活, 0:全部， 1：已激活，2：未激活
                参数名称：page_request.offset　类型：integer　描述：null
                参数名称：page_request.limit　类型：integer　描述：null
                参数名称：page_request.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "account_list": [
                        {
                            "account_id": "",
                            "account_name": "",
                            "cellphone": "",
                            "company_name": "",
                            "created_at": "",
                            "email": "",
                            "first_login": false,
                            "id": "",
                            "inviter": "",
                            "name": ""
                        }
                    ],
                    "page_response": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
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
        intef = collections.interface("Service", "UserSrv_ListAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("accountId", accountId)
        intef.update_params("cond", cond)
        intef.update_params("account_activated", account_activated)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def UserSrv_ListAccountCSVGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  导出全部用户列表 """
        """  path: [get]/v1/ListAccountCSV API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Service", "UserSrv_ListAccountCSV")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def UserSrv_ListDistinctModelGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取去重的模型列表 """
        """  path: [get]/v1/ListDistinctModel API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "models": [
                        {
                            "display_name": "",
                            "value": ""
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
        intef = collections.interface("Service", "UserSrv_ListDistinctModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def UserSrv_ListInternalModelGetApi(self, model_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取模型实例列表 """
        """  path: [get]/v1/ListInternalModel API """
        """  params: 
                参数名称：model_id　类型：string　描述：模型i
        """
        """  resp:
                200(A successful response.):
                {
                    "internal_models": [
                        {
                            "created_at": "",
                            "internal_id": "",
                            "model_id": "",
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
        intef = collections.interface("Service", "UserSrv_ListInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("model_id", model_id)
        return intef.request() if sendRequest else intef

    def UserSrv_ListInviterGetApi(self, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取商务列表
包括已经创建邮箱的和未创建邮箱的，一个客户的多个商务会使用英文逗号分隔，需要分开显示 """
        """  path: [get]/v1/ListInviter API """
        """  params: 
                参数名称：page_request.offset　类型：integer　描述：null
                参数名称：page_request.limit　类型：integer　描述：null
                参数名称：page_request.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "inviters": [
                        {
                            "email": "",
                            "name": ""
                        }
                    ],
                    "page_response": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
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
        intef = collections.interface("Service", "UserSrv_ListInviter")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def UserSrv_ListModelGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取模型列表 """
        """  path: [get]/v1/ListModel API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "models": [
                        {
                            "id": "",
                            "model_permissions": [],
                            "model_type": "[ModelType_Unknown]ModelType_Unknown/BaseModel/FinetunedModel",
                            "public_access": false,
                            "whitelist_account_count": ""
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
        intef = collections.interface("Service", "UserSrv_ListModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def UserSrv_ListModelRoutesGetApi(self, model_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取model的路由策略 """
        """  path: [get]/v1/ListModelRoutes API """
        """  params: 
                参数名称：model_id　类型：string　描述：模型I
        """
        """  resp:
                200(A successful response.):
                {
                    "model_routes": [
                        {
                            "account_id": "",
                            "account_name": "",
                            "id": "",
                            "model_id": "",
                            "model_internal_id": "",
                            "primary": false,
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
        intef = collections.interface("Service", "UserSrv_ListModelRoutes")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("model_id", model_id)
        return intef.request() if sendRequest else intef

    def UserSrv_ListPendingAuditInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/v1/ListPendingAuditInfo API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "pending_audit_infos": [
                        {
                            "business_qpd": "",
                            "business_scene": "",
                            "business_scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                            "cellphone": "",
                            "company_homepage": "",
                            "company_name": "",
                            "company_type": "[CompanyType_Unset]CompanyType_Unset/Startup/SmallAndMicro/Medium/Large/StateOwned",
                            "email": "",
                            "id": "",
                            "inviter": "",
                            "job_title": "",
                            "lm": {
                                "internal_api": false,
                                "internal_multi_chat": false,
                                "lm_chat": false,
                                "lm_config": {
                                    "chat_qps": 0,
                                    "code_qps": 0,
                                    "cv_qps": 0,
                                    "default_offline_search": false,
                                    "default_online": false,
                                    "finetune_job_count": 0,
                                    "knowledge_base_max_count": 0,
                                    "knowledge_retrieve_timeout": 0,
                                    "miaohua_qps": 0,
                                    "online_knowledge_mode": 0,
                                    "serving_count": 0
                                },
                                "lm_cv": false,
                                "lm_finetune": false,
                                "lm_knowledgebase": false,
                                "lm_miaohua": false,
                                "lm_role_play": false,
                                "lm_sense_code": false
                            },
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
        intef = collections.interface("Service", "UserSrv_ListPendingAuditInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def UserSrv_ListPendingAuditInfoCSVGetApi(self, audit_state=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  导出申请用户，参数可以控制筛选 """
        """  path: [get]/v1/ListPendingAuditInfoCSV API """
        """  params: 
                参数名称：audit_state　类型：array　描述：默认选择未审核的，若参数不为空，则按audit_state过滤
若要筛选全部申请用户，可以传Waiting+Pass+Prohibit

 - Waiting: 待审核
 - Pass: 审核通过
 - Prohibit: 审核失
        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Service", "UserSrv_ListPendingAuditInfoCSV")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("audit_state", audit_state)
        return intef.request() if sendRequest else intef

    def UserSrv_StatChatCompletionPostApi(self, scope=None, time_range=None, granularity=None, module=None, model_name=None, url=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-对话生成 """
        """  path: [post]/v1/StatChatCompletion API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "model_name": "",
                    "module": "[StatChatCompletionModule_Unset]StatChatCompletionModule_Unset/Calls/UserInputToken/ModelOutputToken/ModelAcceptInputToken/FeatureTriggerSensitive/FeatureTriggerDefaultKnowledgeBase/FeatureTriggerKnowledgeFusion/FeatureTriggerCompanyKnowledgeBase",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    },
                    "url": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "usages": [
                        {
                            "count": "",
                            "month_on_month": 0,
                            "start_time": ""
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
        intef = collections.interface("Service", "UserSrv_StatChatCompletion")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("model_name", model_name)
        intef.update_body("url", url)
        intef.update_body("account_id", account_id)
        return intef.request() if sendRequest else intef

    def UserSrv_StatChatCompletionExportPostApi(self, scope=None, time_range=None, granularity=None, module=None, model_name=None, url=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-对话生成导出 """
        """  path: [post]/v1/StatChatCompletionExport API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "model_name": "",
                    "module": "[StatChatCompletionModule_Unset]StatChatCompletionModule_Unset/Calls/UserInputToken/ModelOutputToken/ModelAcceptInputToken/FeatureTriggerSensitive/FeatureTriggerDefaultKnowledgeBase/FeatureTriggerKnowledgeFusion/FeatureTriggerCompanyKnowledgeBase",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    },
                    "url": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Service", "UserSrv_StatChatCompletionExport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("model_name", model_name)
        intef.update_body("url", url)
        intef.update_body("account_id", account_id)
        return intef.request() if sendRequest else intef

    def UserSrv_StatChatCompletionTopNPostApi(self, scope=None, time_range=None, granularity=None, module=None, model_name=None, url=None, account_id=None, top_n=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-对话生成topN """
        """  path: [post]/v1/StatChatCompletionTopN API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "model_name": "",
                    "module": "[StatChatCompletionModule_Unset]StatChatCompletionModule_Unset/Calls/UserInputToken/ModelOutputToken/ModelAcceptInputToken/FeatureTriggerSensitive/FeatureTriggerDefaultKnowledgeBase/FeatureTriggerKnowledgeFusion/FeatureTriggerCompanyKnowledgeBase",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    },
                    "top_n": 0,
                    "url": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "usages": [
                        {
                            "account_id": "",
                            "account_name": "",
                            "count": ""
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
        intef = collections.interface("Service", "UserSrv_StatChatCompletionTopN")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("model_name", model_name)
        intef.update_body("url", url)
        intef.update_body("account_id", account_id)
        intef.update_body("top_n", top_n)
        return intef.request() if sendRequest else intef

    def UserSrv_StatChatCompletionTopNExportPostApi(self, scope=None, time_range=None, granularity=None, module=None, model_name=None, url=None, account_id=None, top_n=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-对话生成topN导出 """
        """  path: [post]/v1/StatChatCompletionTopNExport API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "model_name": "",
                    "module": "[StatChatCompletionModule_Unset]StatChatCompletionModule_Unset/Calls/UserInputToken/ModelOutputToken/ModelAcceptInputToken/FeatureTriggerSensitive/FeatureTriggerDefaultKnowledgeBase/FeatureTriggerKnowledgeFusion/FeatureTriggerCompanyKnowledgeBase",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    },
                    "top_n": 0,
                    "url": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Service", "UserSrv_StatChatCompletionTopNExport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("model_name", model_name)
        intef.update_body("url", url)
        intef.update_body("account_id", account_id)
        intef.update_body("top_n", top_n)
        return intef.request() if sendRequest else intef

    def UserSrv_StatFinetunePostApi(self, scope=None, time_range=None, granularity=None, module=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-模型微调 """
        """  path: [post]/v1/StatFinetune API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "module": "[StatFinetuneModule_Unset]StatFinetuneModule_Unset/Run_Duration/Deploy_Duration/Finetune_Run_Calls/Finetune_Deploy_Calls",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "usages": [
                        {
                            "count": "",
                            "month_on_month": 0,
                            "start_time": ""
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
        intef = collections.interface("Service", "UserSrv_StatFinetune")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("account_id", account_id)
        return intef.request() if sendRequest else intef

    def UserSrv_StatFinetuneExportPostApi(self, scope=None, time_range=None, granularity=None, module=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-模型微调导出 """
        """  path: [post]/v1/StatFinetuneExport API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "module": "[StatFinetuneModule_Unset]StatFinetuneModule_Unset/Run_Duration/Deploy_Duration/Finetune_Run_Calls/Finetune_Deploy_Calls",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Service", "UserSrv_StatFinetuneExport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("account_id", account_id)
        return intef.request() if sendRequest else intef

    def UserSrv_StatFinetuneTopNPostApi(self, scope=None, time_range=None, granularity=None, module=None, account_id=None, top_n=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-模型微调topN """
        """  path: [post]/v1/StatFinetuneTopN API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "module": "[StatFinetuneModule_Unset]StatFinetuneModule_Unset/Run_Duration/Deploy_Duration/Finetune_Run_Calls/Finetune_Deploy_Calls",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    },
                    "top_n": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "usages": [
                        {
                            "account_id": "",
                            "account_name": "",
                            "count": ""
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
        intef = collections.interface("Service", "UserSrv_StatFinetuneTopN")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("account_id", account_id)
        intef.update_body("top_n", top_n)
        return intef.request() if sendRequest else intef

    def UserSrv_StatFinetuneTopNExportPostApi(self, scope=None, time_range=None, granularity=None, module=None, account_id=None, top_n=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-模型微调topN导出 """
        """  path: [post]/v1/StatFinetuneTopNExport API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "module": "[StatFinetuneModule_Unset]StatFinetuneModule_Unset/Run_Duration/Deploy_Duration/Finetune_Run_Calls/Finetune_Deploy_Calls",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    },
                    "top_n": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Service", "UserSrv_StatFinetuneTopNExport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("account_id", account_id)
        intef.update_body("top_n", top_n)
        return intef.request() if sendRequest else intef

    def UserSrv_StatImageGenerationPostApi(self, scope=None, model_name=None, time_range=None, granularity=None, module=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-图片生成 """
        """  path: [post]/v1/StatImageGeneration API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "module": "[StatImageGeneration_Unset]StatImageGeneration_Unset/ImageGenerationTask/ImageGeneration/TextVolumeForImageGeneration/CreateImageGenerationTaskCalls",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "model_name":"",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "usages": [
                        {
                            "count": "",
                            "month_on_month": 0,
                            "start_time": ""
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
        intef = collections.interface("Service", "UserSrv_StatImageGeneration")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("account_id", account_id)
        intef.update_body("model_name", model_name)
        return intef.request() if sendRequest else intef

    def UserSrv_StatImageGenerationExportPostApi(self, scope=None, time_range=None, model_name=None, granularity=None, module=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-图片生成导出 """
        """  path: [post]/v1/StatImageGenerationExport API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "module": "[StatImageGeneration_Unset]StatImageGeneration_Unset/ImageGenerationTask/ImageGeneration/TextVolumeForImageGeneration/CreateImageGenerationTaskCalls",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "model_name":"",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Service", "UserSrv_StatImageGenerationExport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("account_id", account_id)
        intef.update_body("model_name", model_name)
        return intef.request() if sendRequest else intef

    def UserSrv_StatImageGenerationTopNPostApi(self, scope=None, time_range=None, model_name=None, granularity=None, module=None, account_id=None, top_n=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-图片生成topN """
        """  path: [post]/v1/StatImageGenerationTopN API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "module": "[StatImageGeneration_Unset]StatImageGeneration_Unset/ImageGenerationTask/ImageGeneration/TextVolumeForImageGeneration/CreateImageGenerationTaskCalls",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "model_name":"",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    },
                    "top_n": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "usages": [
                        {
                            "account_id": "",
                            "account_name": "",
                            "count": ""
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
        intef = collections.interface("Service", "UserSrv_StatImageGenerationTopN")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("account_id", account_id)
        intef.update_body("top_n", top_n)
        intef.update_body("model_name", model_name)
        return intef.request() if sendRequest else intef

    def UserSrv_StatImageGenerationTopNExportPostApi(self, scope=None, time_range=None, model_name=None, granularity=None, module=None, account_id=None, top_n=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-图片生成topN导出 """
        """  path: [post]/v1/StatImageGenerationTopNExport API """
        """  body: 
                {
                    "account_id": "",
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "module": "[StatImageGeneration_Unset]StatImageGeneration_Unset/ImageGenerationTask/ImageGeneration/TextVolumeForImageGeneration/CreateImageGenerationTaskCalls",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "model_name":"",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    },
                    "top_n": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Service", "UserSrv_StatImageGenerationTopNExport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        intef.update_body("account_id", account_id)
        intef.update_body("top_n", top_n)
        intef.update_body("model_name", model_name)
        return intef.request() if sendRequest else intef

    def UserSrv_StatUserPostApi(self, scope=None, time_range=None, granularity=None, module=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-用户 """
        """  path: [post]/v1/StatUser API """
        """  body: 
                {
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "module": "[StatUserModule_Unset]StatUserModule_Unset/WaitingList/All/ActiveAll/ActiveChatCompletion/ActiveStatefulChatCompletion/ActiveFinetune/ActiveKnowledgeBase/ActiveStatefulChatExternal/ActiveImageGeneration",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "users": [
                        {
                            "count": "",
                            "month_on_month": 0,
                            "start_time": ""
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
        intef = collections.interface("Service", "UserSrv_StatUser")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        return intef.request() if sendRequest else intef

    def UserSrv_StatUserExportPostApi(self, scope=None, time_range=None, granularity=None, module=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据报表-用户导出 """
        """  path: [post]/v1/StatUserExport API """
        """  body: 
                {
                    "granularity": "[GRANULARITY_MONTH]GRANULARITY_MONTH/GRANULARITY_DAY/GRANULARITY_HOUR/GRANULARITY_WEEK",
                    "module": "[StatUserModule_Unset]StatUserModule_Unset/WaitingList/All/ActiveAll/ActiveChatCompletion/ActiveStatefulChatCompletion/ActiveFinetune/ActiveKnowledgeBase/ActiveStatefulChatExternal/ActiveImageGeneration",
                    "scope": "[BusinessScope_Unset]BusinessScope_Unset/Internal/External",
                    "time_range": {
                        "time1": "",
                        "time2": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Service", "UserSrv_StatUserExport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("scope", scope)
        intef.update_body("time_range", time_range)
        intef.update_body("granularity", granularity)
        intef.update_body("module", module)
        return intef.request() if sendRequest else intef

    def UserSrv_UpdateAccountDetailPostApi(self, id=None, account_name=None, company_name=None, name=None, locale=None, inviter=None, authentication=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新账户详情 """
        """  path: [post]/v1/UpdateAccountDetail API """
        """  body: 
                {
                    "account_name": "",
                    "authentication": "[Identity_Unauthenticated]Identity_Unauthenticated/Business/Individual",
                    "company_name": "",
                    "id": "",
                    "inviter": "",
                    "locale": "",
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
        intef = collections.interface("Service", "UserSrv_UpdateAccountDetail")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("account_name", account_name)
        intef.update_body("company_name", company_name)
        intef.update_body("name", name)
        intef.update_body("locale", locale)
        intef.update_body("inviter", inviter)
        intef.update_body("authentication", authentication)
        return intef.request() if sendRequest else intef

    def UserSrv_UpdateAccountSubscriptionPostApi(self, id=None, lm=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新账户订阅配置 """
        """  path: [post]/v1/UpdateAccountSubscription API """
        """  body: 
                {
                    "id": "",
                    "lm": {
                        "internal_api": false,
                        "internal_multi_chat": false,
                        "lm_chat": false,
                        "lm_config": {
                            "chat_qps": 0,
                            "code_qps": 0,
                            "cv_qps": 0,
                            "default_offline_search": false,
                            "default_online": false,
                            "finetune_job_count": 0,
                            "knowledge_base_max_count": 0,
                            "knowledge_retrieve_timeout": 0,
                            "miaohua_qps": 0,
                            "online_knowledge_mode": 0,
                            "serving_count": 0
                        },
                        "lm_cv": false,
                        "lm_finetune": false,
                        "lm_knowledgebase": false,
                        "lm_miaohua": false,
                        "lm_role_play": false,
                        "lm_sense_code": false
                    }
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
        intef = collections.interface("Service", "UserSrv_UpdateAccountSubscription")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("lm", lm)
        return intef.request() if sendRequest else intef

    def UserSrv_UpdateInternalModelPostApi(self, internal_id=None, root_internal_id=None, parent_internal_id=None, uri=None, extra_info=None, inference_address=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  修改模型实例 """
        """  path: [post]/v1/UpdateInternalModel API """
        """  body: 
                {
                    "extra_info": "",
                    "inference_address": "",
                    "internal_id": "",
                    "parent_internal_id": "",
                    "root_internal_id": "",
                    "uri": ""
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
        intef = collections.interface("Service", "UserSrv_UpdateInternalModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("internal_id", internal_id)
        intef.update_body("root_internal_id", root_internal_id)
        intef.update_body("parent_internal_id", parent_internal_id)
        intef.update_body("uri", uri)
        intef.update_body("extra_info", extra_info)
        intef.update_body("inference_address", inference_address)
        return intef.request() if sendRequest else intef

    def UserSrv_UpdateModelPostApi(self, id=None, model_permissions=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  修改模型 """
        """  path: [post]/v1/UpdateModel API """
        """  body: 
                {
                    "id": "",
                    "model_permissions": []
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
        intef = collections.interface("Service", "UserSrv_UpdateModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("model_permissions", model_permissions)
        return intef.request() if sendRequest else intef

    def UserSrv_UpdateModelRoutePostApi(self, model_id=None, model_routes=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新model的路由策略 """
        """  path: [post]/v1/UpdateModelRoute API """
        """  body: 
                {
                    "model_id": "",
                    "model_routes": [
                        {
                            "account_id": "",
                            "id": "",
                            "model_internal_id": "",
                            "primary": false,
                            "weight": 0
                        }
                    ]
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
        intef = collections.interface("Service", "UserSrv_UpdateModelRoute")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model_id", model_id)
        intef.update_body("model_routes", model_routes)
        return intef.request() if sendRequest else intef

    def UserSrv_UpsertInviterGetApi(self, inviter_name=None, inviter_email=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  添加或者更新商务邮箱 """
        """  path: [get]/v1/UpsertInviter API """
        """  params: 
                参数名称：inviter.name　类型：string　描述：null
                参数名称：inviter.email　类型：string　描述：nul
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
        intef = collections.interface("Service", "UserSrv_UpsertInviter")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("inviter.name", inviter_name)
        intef.update_params("inviter.email", inviter_email)
        return intef.request() if sendRequest else intef

