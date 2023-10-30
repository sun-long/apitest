#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class UserSwaggerApi(BaseApi):
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

    def ConsoleUserService_OCRIDCardPostApi(self, id_card_image=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  身份张照片识别
route: prefix=console action=OCRIDCard ver... """
        """  path: [post]/console/v1/accounts/ocr API """
        """  body: 
                {
                    "id_card_image": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "id_card_name": "",
                    "id_card_number": ""
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
        intef = collections.interface("User", "ConsoleUserService_OCRIDCard")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id_card_image", id_card_image)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_ListPolicyGroupGetApi(self, nick_name=None, description=None, order=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  策略组列表
route: prefix=console action=ListPolicyGroup... """
        """  path: [get]/console/v1/policygroups API """
        """  params: 
                参数名称：nick_name　类型：string　描述：权限组名称
                参数名称：description　类型：string　描述：描述
                参数名称：order　类型：string　描述：顺序；默认创建时间降序，可选

 - LIST_ORDER_UNSPECIFIED: 未指定
 - LIST_ORDER_CREATED_TIME_ASC: 创建时间升序排列
 - LIST_ORDER_CREATED_TIME_DESC: 创建时间降序排列
 - LIST_ORDER_NAME_ASC: 名称升序排列
 - LIST_ORDER_NAME_DESC: 名称降序排列
 - LIST_ORDER_SUBMIT_AT_ASC: 提交时间升序排列
 - LIST_ORDER_SUBMIT_AT_DESC: 提交时间降序排列
 - LIST_ORDER_RECHARGE_AT_ASC: 提交充值申请时间升序排列
 - LIST_ORDER_RECHARGE_AT_DESC: 提交充值申请时间降序排
        """
        """  resp:
                200(A successful response.):
                {
                    "list": [
                        {
                            "attributes": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "create_at": "",
                            "description": "",
                            "group_id": "",
                            "group_name": "",
                            "nick_name": "",
                            "type": 0,
                            "used_num": ""
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
        intef = collections.interface("User", "ConsoleUserService_ListPolicyGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("nick_name", nick_name)
        intef.update_params("description", description)
        intef.update_params("order", order)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_GetPolicyGroupAssociatedInfoByIDGetApi(self, group_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  策略组详情
route: prefix=console action=GetPolicyGroupA... """
        """  path: [get]/console/v1/policygroups/group_id API """
        """  params: 
                参数名称：group_id　类型：string　描述：策略组ID 必
        """
        """  resp:
                200(A successful response.):
                {
                    "create_at": "",
                    "description": "",
                    "group_id": "",
                    "group_name": "",
                    "nick_name": "",
                    "policy_list": [
                        {
                            "body": {
                                "statements": [
                                    {
                                        "actions": [],
                                        "effect": "",
                                        "resources": []
                                    }
                                ],
                                "version": 0
                            },
                            "description": "",
                            "name": "",
                            "nick_name": "",
                            "policy_id": ""
                        }
                    ],
                    "user_list": [
                        {
                            "attributes": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "blocked": false,
                            "cellphone": "",
                            "create_at": "",
                            "description": "",
                            "email": "",
                            "last_login_at": "",
                            "nick_name": "",
                            "profile_photo_id": "",
                            "user_id": "",
                            "user_name": ""
                        }
                    ],
                    "user_num": ""
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
        intef = collections.interface("User", "ConsoleUserService_GetPolicyGroupAssociatedInfoByID")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("group_id", group_id)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_GetAllPolicyGroupsByUserIDGetApi(self, user_id=None, order=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据user_id获取策略组列表
route: prefix=console action=GetA... """
        """  path: [get]/console/v1/user/policygroups API """
        """  params: 
                参数名称：user_id　类型：string　描述：权限组名称
                参数名称：order　类型：string　描述：顺序；默认创建时间降序，可选

 - LIST_ORDER_UNSPECIFIED: 未指定
 - LIST_ORDER_CREATED_TIME_ASC: 创建时间升序排列
 - LIST_ORDER_CREATED_TIME_DESC: 创建时间降序排列
 - LIST_ORDER_NAME_ASC: 名称升序排列
 - LIST_ORDER_NAME_DESC: 名称降序排列
 - LIST_ORDER_SUBMIT_AT_ASC: 提交时间升序排列
 - LIST_ORDER_SUBMIT_AT_DESC: 提交时间降序排列
 - LIST_ORDER_RECHARGE_AT_ASC: 提交充值申请时间升序排列
 - LIST_ORDER_RECHARGE_AT_DESC: 提交充值申请时间降序排
        """
        """  resp:
                200(A successful response.):
                {
                    "group_id_list": []
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
        intef = collections.interface("User", "ConsoleUserService_GetAllPolicyGroupsByUserID")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("user_id", user_id)
        intef.update_params("order", order)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_CreateUserWithAccountPostApi(self, attr_locale=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  主用户注册
route: prefix=console action=CreateUserWithA... """
        """  path: [post]/console/v1/user_accounts API """
        """  body: 
                {
                    "attr_locale": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "account_id": "",
                    "password": "",
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
        intef = collections.interface("User", "ConsoleUserService_CreateUserWithAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("attr_locale", attr_locale)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_UserLoginForgotPasswordPostApi(self, password=None, value=None, code=None, mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  portal主用户忘记密码时 用手机号码或者邮箱重置密码操作（0914版本修改）
route: pr... """
        """  path: [post]/console/v1/user_accounts/login_forgot_poassword API """
        """  body: 
                {
                    "code": "",
                    "mode": 0,
                    "password": "",
                    "value": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "user_id": ""
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
        intef = collections.interface("User", "ConsoleUserService_UserLoginForgotPassword")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("password", password)
        intef.update_body("value", value)
        intef.update_body("code", code)
        intef.update_body("mode", mode)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_ListAccountSubscriptionsGetApi(self, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取用户订阅列表
route: prefix=console action=ListAccountS... """
        """  path: [get]/console/v1/user_accounts/subscriptions API """
        """  params: 
                参数名称：account_id　类型：string　描述：用户I
        """
        """  resp:
                200(A successful response.):
                {
                    "subscriptions": [
                        {
                            "display_name": "",
                            "service_classify": "",
                            "status": "[OPENED]OPENED",
                            "subscription_name": ""
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
        intef = collections.interface("User", "ConsoleUserService_ListAccountSubscriptions")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_CreateSubsriptionToAccountPostApi(self, account_id=None, subscription_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建订阅 """
        """  path: [post]/console/v1/user_accounts/subscriptions API """
        """  body: 
                {
                    "account_id": "",
                    "subscription_name": ""
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
        intef = collections.interface("User", "ConsoleUserService_CreateSubsriptionToAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("subscription_name", subscription_name)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_SetAccountSubscriptionsPostApi(self, account_id=None, subscription_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  设置用户的订阅 """
        """  path: [post]/console/v1/user_accounts/subscriptions/set API """
        """  body: 
                {
                    "account_id": "",
                    "subscription_name": []
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
        intef = collections.interface("User", "ConsoleUserService_SetAccountSubscriptions")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("subscription_name", subscription_name)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_VerifyUserRegisterInfoPostApi(self, password=None, value=None, code=None, mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  portal验证邮箱账号、手机号、手机验证码信息（0914版本修改）
route: prefix=c... """
        """  path: [post]/console/v1/user_accounts/verify_user_register_info API """
        """  body: 
                {
                    "code": "",
                    "mode": 0,
                    "password": "",
                    "value": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "email_available": 0
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
        intef = collections.interface("User", "ConsoleUserService_VerifyUserRegisterInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("password", password)
        intef.update_body("value", value)
        intef.update_body("code", code)
        intef.update_body("mode", mode)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_GetUserListGetApi(self, nick_name=None, description=None, blocked=None, order=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取子用户列表
route: prefix=console action=GetUserList v... """
        """  path: [get]/console/v1/users API """
        """  params: 
                参数名称：nick_name　类型：string　描述：显示用名称
                参数名称：description　类型：string　描述：描述
                参数名称：blocked　类型：integer　描述：状态 (1：停用) (0：启用) (-1：全部) 必选
                参数名称：order　类型：string　描述：顺序；默认创建时间降序，可选

 - LIST_ORDER_UNSPECIFIED: 未指定
 - LIST_ORDER_CREATED_TIME_ASC: 创建时间升序排列
 - LIST_ORDER_CREATED_TIME_DESC: 创建时间降序排列
 - LIST_ORDER_NAME_ASC: 名称升序排列
 - LIST_ORDER_NAME_DESC: 名称降序排列
 - LIST_ORDER_SUBMIT_AT_ASC: 提交时间升序排列
 - LIST_ORDER_SUBMIT_AT_DESC: 提交时间降序排列
 - LIST_ORDER_RECHARGE_AT_ASC: 提交充值申请时间升序排列
 - LIST_ORDER_RECHARGE_AT_DESC: 提交充值申请时间降序排列
                参数名称：page_request.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条; 默认值为0.
返回本次请求返回的第一条记录实际位置(一般与输入一致).
[EN] Optional, start position, value: > = 0, 0 is the first line; the
default value is 0. In response, actual offset of the first returned record
is returned (generally equals to the offset in request).
                参数名称：page_request.limit　类型：integer　描述：长度, 取值范围[1,100], 如果超出范围, 则返回失败;
在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准. [EN] Length,
default value range [1,100], if it is out of the range, error will be
returned; as the limit range may be redefined in some APIs, please refer to
the supplementary description of these APIs.
                参数名称：page_request.total　类型：integer　描述：可选, 总数, 请求无须填此参数, 响应时填写.
[EN] Optional, this parameter is not required for request, but will be
filled in response
        """
        """  resp:
                200(A successful response.):
                {
                    "list": [
                        {
                            "attributes": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "blocked": false,
                            "cellphone": "",
                            "create_at": "",
                            "description": "",
                            "email": "",
                            "last_login_at": "",
                            "nick_name": "",
                            "profile_photo_id": "",
                            "user_id": "",
                            "user_name": ""
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
        intef = collections.interface("User", "ConsoleUserService_GetUserList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("nick_name", nick_name)
        intef.update_params("description", description)
        intef.update_params("blocked", blocked)
        intef.update_params("order", order)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_CreateUserPostApi(self, nick_name=None, access_mode=None, password=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建子用户
route: prefix=console action=CreateUser vers... """
        """  path: [post]/console/v1/users API """
        """  body: 
                {
                    "access_mode": "",
                    "code": "",
                    "nick_name": "",
                    "password": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "access_key_info": {
                        "access_key_id": "",
                        "blocked": false,
                        "created_at": "",
                        "description": "",
                        "secret_access_key": ""
                    },
                    "csv_file": "",
                    "description": "",
                    "nick_name": "",
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
        intef = collections.interface("User", "ConsoleUserService_CreateUser")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("nick_name", nick_name)
        intef.update_body("access_mode", access_mode)
        intef.update_body("password", password)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_UpdateUserAccessModePostApi(self, user_id=None, access_mode=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  子用户编辑 包括用户访问方式（编程访问、控制台访问）
route: prefix=console a... """
        """  path: [post]/console/v1/users/access_mode/user_id API """
        """  body: 
                {
                    "access_mode": "",
                    "code": "",
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
        intef = collections.interface("User", "ConsoleUserService_UpdateUserAccessMode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("access_mode", access_mode)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_GetUserAssociatedInfoByIDGetApi(self, user_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  子用户详情包括用户基本信息、所属权限组（用户所拥有的权限组列表）、安全设置（用户所拥有的access... """
        """  path: [get]/console/v1/users/associated_info/user_id API """
        """  params: 
                参数名称：user_id　类型：string　描述：用户ID 必
        """
        """  resp:
                200(A successful response.):
                {
                    "access_key_list": [
                        {
                            "access_key_id": "",
                            "blocked": false,
                            "created_at": "",
                            "description": "",
                            "secret_access_key": ""
                        }
                    ],
                    "access_mode": "",
                    "blocked": false,
                    "create_at": "",
                    "description": "",
                    "master_user": 0,
                    "nick_name": "",
                    "password": "",
                    "policy_group_list": [
                        {
                            "description": "",
                            "group_id": "",
                            "group_name": ""
                        }
                    ],
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
        intef = collections.interface("User", "ConsoleUserService_GetUserAssociatedInfoByID")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("user_id", user_id)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_GetUserBaseInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取用户基本信息
route: prefix=console action=GetUserBaseI... """
        """  path: [get]/console/v1/users/base_info API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "account_id": "",
                    "account_level": "[ACCOUNT_LEVEL_UNDEFINED]ACCOUNT_LEVEL_UNDEFINED/ACCOUNT_LEVEL_A/ACCOUNT_LEVEL_C/ACCOUNT_LEVEL_D/ACCOUNT_LEVEL_N",
                    "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                    "account_used_status": "[ACCOUNT_USED_STATUS_UNSPECIFIED]ACCOUNT_USED_STATUS_UNSPECIFIED/ACCOUNT_USED_STATUS_UNBLOCKED/ACCOUNT_USED_STATUS_BLOCKED",
                    "email": "",
                    "master_user": 0,
                    "nick_name": "",
                    "payment_type": "[ACCOUNT_PAYMENT_UNSPECIFIED]ACCOUNT_PAYMENT_UNSPECIFIED/ACCOUNT_PAYMENT_POSTPAID/ACCOUNT_PAYMENT_UNPOSTPAID",
                    "phone": "",
                    "user_id": "",
                    "user_name": "",
                    "user_photo": ""
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
        intef = collections.interface("User", "ConsoleUserService_GetUserBaseInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_UpdateUserBaseInfoPostApi(self, nick_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新用户基本信息 包括昵称
route: prefix=console action=UpdateU... """
        """  path: [post]/console/v1/users/base_info API """
        """  body: 
                {
                    "nick_name": ""
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
        intef = collections.interface("User", "ConsoleUserService_UpdateUserBaseInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("nick_name", nick_name)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_SendSmsCodeGetApi(self, value=None, mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  申请验证码需要填写手机号或者邮箱账号（0914版本修改）
route: prefix=console... """
        """  path: [get]/console/v1/users/code API """
        """  params: 
                参数名称：value　类型：string　描述：邮箱或手机号 必选
                参数名称：mode　类型：integer　描述：模式 0：邮箱 1：手机 必选（0914版本增加
        """
        """  resp:
                200(A successful response.):
                {
                    "cooling_interval": 0,
                    "result": "[Send_Result_Success]Send_Result_Success/Send_Result_TryAgainLater"
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
        intef = collections.interface("User", "ConsoleUserService_SendSmsCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("value", value)
        intef.update_params("mode", mode)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_VerifySmsCodeGetApi(self, value=None, code=None, mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  验证验证码需要填写手机号或者邮箱账号（0914版本修改）
route: prefix=console... """
        """  path: [get]/console/v1/users/code/verify API """
        """  params: 
                参数名称：value　类型：string　描述：邮箱或手机号 必选
                参数名称：code　类型：string　描述：验证码 必选
                参数名称：mode　类型：integer　描述：模式 0：邮箱 1：手机 必选（0914版本增加
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
        intef = collections.interface("User", "ConsoleUserService_VerifySmsCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("value", value)
        intef.update_params("code", code)
        intef.update_params("mode", mode)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_SendCurrentUserSmsCodeGetApi(self, mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  申请验证码用当前用户user_id的手机号或者邮箱账号（0914版本修改）
route: prefi... """
        """  path: [get]/console/v1/users/current_user/code API """
        """  params: 
                参数名称：mode　类型：integer　描述：模式 0：邮箱 1：手机 必选（0914版本增加
        """
        """  resp:
                200(A successful response.):
                {
                    "cooling_interval": 0,
                    "result": "[Send_Result_Success]Send_Result_Success/Send_Result_TryAgainLater"
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
        intef = collections.interface("User", "ConsoleUserService_SendCurrentUserSmsCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("mode", mode)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_VerifyCurrentUserSmsCodeGetApi(self, code=None, mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  验证验证码用当前用户user_id的手机号或者邮箱账号（0914版本修改）
route: prefi... """
        """  path: [get]/console/v1/users/current_user/code/verify API """
        """  params: 
                参数名称：code　类型：string　描述：验证码 必选
                参数名称：mode　类型：integer　描述：模式 0：邮箱 1：手机 必选（0914版本增加
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
        intef = collections.interface("User", "ConsoleUserService_VerifyCurrentUserSmsCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("code", code)
        intef.update_params("mode", mode)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_UsePhoneOrUserIDDeleteUserPostApi(self, user_id=None, phone=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  用手机号码或者userID删除主用户 """
        """  path: [post]/console/v1/users/delete_root_user API """
        """  body: 
                {
                    "phone": "",
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
        intef = collections.interface("User", "ConsoleUserService_UsePhoneOrUserIDDeleteUser")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("phone", phone)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_UpdateUserDescInfoPostApi(self, user_id=None, nick_name=None, description=None, blocked=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  子用户编辑 包括用户名称、状态、描述
route: prefix=console action=Up... """
        """  path: [post]/console/v1/users/desc_info/user_id API """
        """  body: 
                {
                    "blocked": false,
                    "description": "",
                    "nick_name": "",
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
        intef = collections.interface("User", "ConsoleUserService_UpdateUserDescInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("nick_name", nick_name)
        intef.update_body("description", description)
        intef.update_body("blocked", blocked)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_UserFirstLoginUpdateNewPasswordPostApi(self, password=None, value=None, code=None, mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  用户首次登录用手机号码或者邮箱重置密码操作（0914版本修改）
route: prefix=cons... """
        """  path: [post]/console/v1/users/login_update_new_poassword API """
        """  body: 
                {
                    "code": "",
                    "mode": 0,
                    "password": "",
                    "value": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "user_id": ""
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
        intef = collections.interface("User", "ConsoleUserService_UserFirstLoginUpdateNewPassword")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("password", password)
        intef.update_body("value", value)
        intef.update_body("code", code)
        intef.update_body("mode", mode)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_SecuritySetUpdateUserCellphonePostApi(self, phone_code=None, phone=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  安全设置 手机号码修改（0914版本修改）
route: prefix=console action... """
        """  path: [post]/console/v1/users/security_set/cellphone API """
        """  body: 
                {
                    "code": "",
                    "phone": "",
                    "phone_code": ""
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
        intef = collections.interface("User", "ConsoleUserService_SecuritySetUpdateUserCellphone")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("phone_code", phone_code)
        intef.update_body("phone", phone)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_SecuritySetUpdateUserEmailPostApi(self, email=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  安全设置 绑定邮箱
route: prefix=console action=SecuritySet... """
        """  path: [post]/console/v1/users/security_set/email API """
        """  body: 
                {
                    "code": "",
                    "email": ""
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
        intef = collections.interface("User", "ConsoleUserService_SecuritySetUpdateUserEmail")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("email", email)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_SecuritySetUpdateUserPasswordPostApi(self, mode=None, password=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  安全设置 修改登录密码
route: prefix=console action=SecurityS... """
        """  path: [post]/console/v1/users/security_set/password API """
        """  body: 
                {
                    "code": "",
                    "mode": 0,
                    "password": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "same": false
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
        intef = collections.interface("User", "ConsoleUserService_SecuritySetUpdateUserPassword")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("mode", mode)
        intef.update_body("password", password)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_UpdateSubUserPasswordPostApi(self, user_id=None, password=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  子用户编辑 更新子用户密码
route: prefix=console action=UpdateS... """
        """  path: [post]/console/v1/users/sub_user/password API """
        """  body: 
                {
                    "password": "",
                    "user_id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "same": false,
                    "user_id": ""
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
        intef = collections.interface("User", "ConsoleUserService_UpdateSubUserPassword")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("password", password)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_GetUserUnRedactedInfoGetApi(self, mode=None, user_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取用户未脱敏的基本信息(电话或者邮箱)
route: prefix=console action=... """
        """  path: [get]/console/v1/users/unredacted_info API """
        """  params: 
                参数名称：mode　类型：integer　描述：0 获取真实姓名未脱敏信息
1 获取手机号未脱敏信息
2 获取邮箱账号未脱敏信息
3 获取身份证号码未脱敏信息
                参数名称：user_id　类型：string　描述：用户I
        """
        """  resp:
                200(A successful response.):
                {
                    "email": "",
                    "phone": ""
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
        intef = collections.interface("User", "ConsoleUserService_GetUserUnRedactedInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("mode", mode)
        intef.update_params("user_id", user_id)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_DeleteUserPostApi(self, user_id=None, code=None, force=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  子用户删除
route: prefix=console action=DeleteUser vers... """
        """  path: [post]/console/v1/users/user_id API """
        """  body: 
                {
                    "code": "",
                    "force": false,
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
        intef = collections.interface("User", "ConsoleUserService_DeleteUser")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("code", code)
        intef.update_body("force", force)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_CreateUserAKSKPostApi(self, user_id=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  子用户新增访问密钥
route: prefix=console action=CreateUserA... """
        """  path: [post]/console/v1/users/user_id/accesskeys API """
        """  body: 
                {
                    "code": "",
                    "user_id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "access_key_id": "",
                    "blocked": false,
                    "create_at": "",
                    "csv_file": "",
                    "secret_access_key": ""
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
        intef = collections.interface("User", "ConsoleUserService_CreateUserAKSK")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_DeleteAccessKeyPostApi(self, user_id=None, access_key_id=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  子用户移除访问密钥
route: prefix=console action=DeleteAcces... """
        """  path: [post]/console/v1/users/user_id/accesskeys/access_key_id API """
        """  body: 
                {
                    "access_key_id": "",
                    "code": "",
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
        intef = collections.interface("User", "ConsoleUserService_DeleteAccessKey")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("access_key_id", access_key_id)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_ExportUserAKSKExcelPostApi(self, user_id=None, access_key_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  将aksk信息导出为excel文件
route: prefix=console action=Exp... """
        """  path: [post]/console/v1/users/user_id/accesskeys/excel_export API """
        """  body: 
                {
                    "access_key_id": "",
                    "user_id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "access_key_id": "",
                    "file": "",
                    "file_name": "",
                    "user_id": ""
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
        intef = collections.interface("User", "ConsoleUserService_ExportUserAKSKExcel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("access_key_id", access_key_id)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_SetAccessKeyStatusPostApi(self, user_id=None, access_key_id=None, blocked=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  设置子用户aksk状态
route: prefix=console action=SetAccess... """
        """  path: [post]/console/v1/users/user_id/accesskeys/status API """
        """  body: 
                {
                    "access_key_id": "",
                    "blocked": false,
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
        intef = collections.interface("User", "ConsoleUserService_SetAccessKeyStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("access_key_id", access_key_id)
        intef.update_body("blocked", blocked)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_BatchAddPolicyGroupToUserPostApi(self, user_id=None, group_id_list=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  批量授权子用户权限组
route: prefix=console action=BatchAddPo... """
        """  path: [post]/console/v1/users/user_id/batch_policygroups API """
        """  body: 
                {
                    "group_id_list": [],
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
        intef = collections.interface("User", "ConsoleUserService_BatchAddPolicyGroupToUser")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("group_id_list", group_id_list)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_RemovePolicyGroupFromUserPostApi(self, group_id=None, user_id=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  用户移除授权权限组
route: prefix=console action=RemovePolic... """
        """  path: [post]/console/v1/users/user_id/policygroups/group_id API """
        """  body: 
                {
                    "code": "",
                    "group_id": "",
                    "user_id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "group_id": "",
                    "user_id": ""
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
        intef = collections.interface("User", "ConsoleUserService_RemovePolicyGroupFromUser")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("group_id", group_id)
        intef.update_body("user_id", user_id)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleUserService_UserNameExistInAccountPostApi(self, user_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询创建的新子用户名称是否已经存在
route: prefix=console action=Use... """
        """  path: [post]/console/v1/users/user_name_exist API """
        """  body: 
                {
                    "user_name": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "exist": 0
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
        intef = collections.interface("User", "ConsoleUserService_UserNameExistInAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_name", user_name)
        return intef.request() if sendRequest else intef

