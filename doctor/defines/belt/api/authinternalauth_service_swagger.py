#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class AuthinternalauthSwaggerApi(BaseApi):
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

    def ConsoleInternalAuthService_AdminGetPhoneOrEmailByAccountIDGetApi(self, account_id=None, mode=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员获取单个账户的真实手机号码或者邮箱账号
route: prefix=console-int... """
        """  path: [get]/console-internal/v1/account/phone_or_email API """
        """  params: 
                参数名称：account_id　类型：string　描述：账户ID.
                参数名称：mode　类型：integer　描述：模式 0：邮箱 1：手机.
                参数名称：code　类型：string　描述：验证码
        """
        """  resp:
                200(A successful response.):
                {
                    "email": "",
                    "need_code_check": 0,
                    "phone": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminGetPhoneOrEmailByAccountID")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        intef.update_params("mode", mode)
        intef.update_params("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminGetAccountListGetApi(self, account_name=None, account_type=None, status=None, business_status=None, account_id=None, user_id=None, user_name=None, enterprise_name=None, order=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员获取账户列表
route: prefix=console-internal action=... """
        """  path: [get]/console-internal/v1/accounts API """
        """  params: 
                参数名称：account_name　类型：string　描述：账户名称，可选.
                参数名称：account_type　类型：string　描述：账户类型 必选.

 - ACCOUNT_TYPE_UNSPECIFIED: 未指定
 - ACCOUNT_TYPE_PERSON: 个人账户
 - ACCOUNT_TYPE_ENTERPRISE: 企业账户
 - ACCOUNT_TYPE_UNKNOW: 未知类型
                参数名称：status　类型：string　描述：认证状态 必选.

 - ACCOUNT_STATUS_UNSPECIFIED: 未指定
 - ACCOUNT_STATUS_BERINGCERTIFIED: 认证中
 - ACCOUNT_STATUS_SUCCEEDED: 认证成功
 - ACCOUNT_STATUS_FAILED: 认证失败
 - ACCOUNT_STATUS_CHANGED: 认证变更待审核
 - ACCOUNT_STATUS_CHANGED_FAILED: 认证变更失败
 - ACCOUNT_AUDIT_STATUS_UNCERTIFIED: 未认证审核
                参数名称：business_status　类型：integer　描述：商务分配状态 (全部:-1  未分配:0  已分配:1) 必选.
                参数名称：account_id　类型：string　描述：账户ID.
                参数名称：user_id　类型：string　描述：主账号ID 已经弃用.
                参数名称：user_name　类型：string　描述：user_name 主账号ID.
                参数名称：enterprise_name　类型：string　描述：认证主体.
                参数名称：order　类型：string　描述：顺序；默认创建时间降序，可选.

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
                    "account_info": [
                        {
                            "account_id": "",
                            "account_level": "[ACCOUNT_LEVEL_UNDEFINED]ACCOUNT_LEVEL_UNDEFINED/ACCOUNT_LEVEL_A/ACCOUNT_LEVEL_C/ACCOUNT_LEVEL_D/ACCOUNT_LEVEL_N",
                            "account_name": "",
                            "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                            "account_used_status": "[ACCOUNT_USED_STATUS_UNSPECIFIED]ACCOUNT_USED_STATUS_UNSPECIFIED/ACCOUNT_USED_STATUS_UNBLOCKED/ACCOUNT_USED_STATUS_BLOCKED",
                            "audit_at": "",
                            "business_assigned": "",
                            "business_code": "",
                            "business_department": "",
                            "business_name": "",
                            "cellphone": "",
                            "created_at": "",
                            "email": "",
                            "empty_status": 0,
                            "enterprise_card_name": "",
                            "enterprise_name": "",
                            "have_second_confirm_recharge_log": 0,
                            "have_unprocessed_recharge_log": 0,
                            "payment_type": "[ACCOUNT_PAYMENT_UNSPECIFIED]ACCOUNT_PAYMENT_UNSPECIFIED/ACCOUNT_PAYMENT_POSTPAID/ACCOUNT_PAYMENT_UNPOSTPAID",
                            "recharge_log_id": "",
                            "status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED",
                            "submit_at": "",
                            "submit_recharge_time": "",
                            "the_last_three_months_bill_amount": "",
                            "updated_at": "",
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminGetAccountList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_name", account_name)
        intef.update_params("account_type", account_type)
        intef.update_params("status", status)
        intef.update_params("business_status", business_status)
        intef.update_params("account_id", account_id)
        intef.update_params("user_id", user_id)
        intef.update_params("user_name", user_name)
        intef.update_params("enterprise_name", enterprise_name)
        intef.update_params("order", order)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminUpdateAccountPostApi(self, account_id=None, update_mode=None, account_used_status=None, payment_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员更新付费模式、账户的启用和禁用状态
route: prefix=console-inter... """
        """  path: [post]/console-internal/v1/accounts/account API """
        """  body: 
                {
                    "account_id": "",
                    "account_used_status": "[ACCOUNT_USED_STATUS_UNSPECIFIED]ACCOUNT_USED_STATUS_UNSPECIFIED/ACCOUNT_USED_STATUS_UNBLOCKED/ACCOUNT_USED_STATUS_BLOCKED",
                    "payment_type": "[ACCOUNT_PAYMENT_UNSPECIFIED]ACCOUNT_PAYMENT_UNSPECIFIED/ACCOUNT_PAYMENT_POSTPAID/ACCOUNT_PAYMENT_UNPOSTPAID",
                    "update_mode": 0
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "account_id": "",
                    "account_used_status": "[ACCOUNT_USED_STATUS_UNSPECIFIED]ACCOUNT_USED_STATUS_UNSPECIFIED/ACCOUNT_USED_STATUS_UNBLOCKED/ACCOUNT_USED_STATUS_BLOCKED",
                    "payment_type": "[ACCOUNT_PAYMENT_UNSPECIFIED]ACCOUNT_PAYMENT_UNSPECIFIED/ACCOUNT_PAYMENT_POSTPAID/ACCOUNT_PAYMENT_UNPOSTPAID"
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminUpdateAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("update_mode", update_mode)
        intef.update_body("account_used_status", account_used_status)
        intef.update_body("payment_type", payment_type)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminGetEnterpriseAccountGetApi(self, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员获取单账号审核认证数据
route: prefix=console-internal ac... """
        """  path: [get]/console-internal/v1/accounts/auth_data API """
        """  params: 
                参数名称：account_id　类型：string　描述：账户ID
        """
        """  resp:
                200(A successful response.):
                {
                    "enterprise_account": {
                        "area_name": "",
                        "audit_at": "",
                        "audit_desc": "",
                        "audit_nick_name": "",
                        "audit_user_id": "",
                        "business_inviter": "",
                        "cellphone": "",
                        "end_user": "",
                        "enterprise_card_end_at": "",
                        "enterprise_card_name": "",
                        "enterprise_card_number": "",
                        "enterprise_card_photo1": "",
                        "enterprise_card_photo2": "",
                        "enterprise_card_start_at": "",
                        "enterprise_card_type": "[IDCREDENTIAL_TYPE_UNSPECIFIED]IDCREDENTIAL_TYPE_UNSPECIFIED/IDCREDENTIAL_TYPE_IDCARD/IDCREDENTIAL_TYPE_PASSPORT/IDCREDENTIAL_TYPE_HKMOCER/IDCREDENTIAL_TYPE_TWCER/IDCREDENTIAL_TYPE_FOREIGNERS/IDCREDENTIAL_TYPE_HKMORP",
                        "enterprise_name": "",
                        "enterprise_number": "",
                        "enterprise_photo": "",
                        "industry": "[INDUSTRY_TYPE_OTHERS]INDUSTRY_TYPE_OTHERS/INDUSTRY_TYPE_SECURITY_PROTECTION/INDUSTRY_TYPE_MUTUAL_ENTERTAINMENT/INDUSTRY_TYPE_CELLPHONE/INDUSTRY_TYPE_ON_BOARD/INDUSTRY_TYPE_FINANCIAL/INDUSTRY_TYPE_ESTATE/INDUSTRY_TYPE_OPERATOR/INDUSTRY_TYPE_SMART_TRANSPORTATION/INDUSTRY_TYPE_RETAIL/INDUSTRY_TYPE_EDUCATE/INDUSTRY_TYPE_MEDICAL/INDUSTRY_TYPE_ADVERTISE/INDUSTRY_TYPE_REMOTE_SENSING/INDUSTRY_TYPE_VIDEO_ANALYSIS/INDUSTRY_TYPE_SMART_CAMERA/INDUSTRY_TYPE_SMART_DEVICE/INDUSTRY_TYPE_CHIP/INDUSTRY_TYPE_INTEGRATORS/INDUSTRY_TYPE_NET_FINANCIAL/INDUSTRY_TYPE_CULTURAL_TOURISM/INDUSTRY_TYPE_EXPRESS_DELIVERY/INDUSTRY_TYPE_GAME/INDUSTRY_TYPE_CAR/INDUSTRY_TYPE_VEHICLE_ROAD_COORDINATION/INDUSTRY_TYPE_RESEARCH",
                        "position": "",
                        "scenario": "",
                        "status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED"
                    },
                    "new_enterprise_account": {
                        "area_name": "",
                        "audit_at": "",
                        "audit_desc": "",
                        "audit_nick_name": "",
                        "audit_user_id": "",
                        "business_inviter": "",
                        "cellphone": "",
                        "end_user": "",
                        "enterprise_card_end_at": "",
                        "enterprise_card_name": "",
                        "enterprise_card_number": "",
                        "enterprise_card_photo1": "",
                        "enterprise_card_photo2": "",
                        "enterprise_card_start_at": "",
                        "enterprise_card_type": "[IDCREDENTIAL_TYPE_UNSPECIFIED]IDCREDENTIAL_TYPE_UNSPECIFIED/IDCREDENTIAL_TYPE_IDCARD/IDCREDENTIAL_TYPE_PASSPORT/IDCREDENTIAL_TYPE_HKMOCER/IDCREDENTIAL_TYPE_TWCER/IDCREDENTIAL_TYPE_FOREIGNERS/IDCREDENTIAL_TYPE_HKMORP",
                        "enterprise_name": "",
                        "enterprise_number": "",
                        "enterprise_photo": "",
                        "industry": "[INDUSTRY_TYPE_OTHERS]INDUSTRY_TYPE_OTHERS/INDUSTRY_TYPE_SECURITY_PROTECTION/INDUSTRY_TYPE_MUTUAL_ENTERTAINMENT/INDUSTRY_TYPE_CELLPHONE/INDUSTRY_TYPE_ON_BOARD/INDUSTRY_TYPE_FINANCIAL/INDUSTRY_TYPE_ESTATE/INDUSTRY_TYPE_OPERATOR/INDUSTRY_TYPE_SMART_TRANSPORTATION/INDUSTRY_TYPE_RETAIL/INDUSTRY_TYPE_EDUCATE/INDUSTRY_TYPE_MEDICAL/INDUSTRY_TYPE_ADVERTISE/INDUSTRY_TYPE_REMOTE_SENSING/INDUSTRY_TYPE_VIDEO_ANALYSIS/INDUSTRY_TYPE_SMART_CAMERA/INDUSTRY_TYPE_SMART_DEVICE/INDUSTRY_TYPE_CHIP/INDUSTRY_TYPE_INTEGRATORS/INDUSTRY_TYPE_NET_FINANCIAL/INDUSTRY_TYPE_CULTURAL_TOURISM/INDUSTRY_TYPE_EXPRESS_DELIVERY/INDUSTRY_TYPE_GAME/INDUSTRY_TYPE_CAR/INDUSTRY_TYPE_VEHICLE_ROAD_COORDINATION/INDUSTRY_TYPE_RESEARCH",
                        "position": "",
                        "scenario": "",
                        "status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED"
                    },
                    "status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED"
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminGetEnterpriseAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminGetEnterpriseAccountUnRedactedInfoGetApi(self, mode=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员获取单账号审核认证未脱敏数据(姓名或者手机号)
route: prefix=console... """
        """  path: [get]/console-internal/v1/accounts/auth_data/unredacted_info API """
        """  params: 
                参数名称：mode　类型：integer　描述：0 获取真实姓名未脱敏信息
1 获取手机号未脱敏信息
2 获取邮箱账号未脱敏信息
3 获取身份证号码未脱敏信息.
                参数名称：account_id　类型：string　描述：账户ID
        """
        """  resp:
                200(A successful response.):
                {
                    "name": "",
                    "new_name": "",
                    "phone": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminGetEnterpriseAccountUnRedactedInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("mode", mode)
        intef.update_params("account_id", account_id)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminUpdateAccountStatusPostApi(self, account_id=None, audit_at=None, status=None, audit_desc=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员认证审核
route: prefix=console-internal action=Ad... """
        """  path: [post]/console-internal/v1/accounts/auth_status API """
        """  body: 
                {
                    "account_id": "",
                    "audit_at": "",
                    "audit_desc": "",
                    "status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED"
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "account_id": "",
                    "status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED"
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminUpdateAccountStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("audit_at", audit_at)
        intef.update_body("status", status)
        intef.update_body("audit_desc", audit_desc)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminBusinessAssignmentPostApi(self, account_id=None, business_department=None, business_name=None, business_code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员分配商务
route: prefix=console-internal action=Ad... """
        """  path: [post]/console-internal/v1/accounts/business_assignment API """
        """  body: 
                {
                    "account_id": "",
                    "business_code": "",
                    "business_department": "",
                    "business_name": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "account_id": "",
                    "business_code": "",
                    "business_department": "",
                    "business_name": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminBusinessAssignment")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("business_department", business_department)
        intef.update_body("business_name", business_name)
        intef.update_body("business_code", business_code)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminGetIndustryInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员获取行业信息
route: prefix=console action=AdminGetI... """
        """  path: [get]/console-internal/v1/accounts/industry_info API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "industry_info": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminGetIndustryInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminGetAccountUserListGetApi(self, user_id=None, user_name=None, order=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  系统工具 超级管理员用户管理
route: prefix=console-internal acti... """
        """  path: [get]/console-internal/v1/accounts/user_info API """
        """  params: 
                参数名称：user_id　类型：string　描述：userID 可选.
                参数名称：user_name　类型：string　描述：用户名 可选.
                参数名称：order　类型：string　描述：顺序；默认创建时间降序，可选.

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
                    "account_user_info": [
                        {
                            "created_at": "",
                            "last_login_at": "",
                            "nick_name": "",
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminGetAccountUserList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("user_id", user_id)
        intef.update_params("user_name", user_name)
        intef.update_params("order", order)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminGetCostManagementAccountListGetApi(self, account_type=None, account_id=None, user_id=None, user_name=None, enterprise_name=None, account_level=None, only_view_unprocessed_records_accounts=None, order=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员获取费用管理账户列表
route: prefix=console-internal act... """
        """  path: [get]/console-internal/v1/cost_management/accounts API """
        """  params: 
                参数名称：account_type　类型：string　描述：账户类型 必选.

 - ACCOUNT_TYPE_UNSPECIFIED: 未指定
 - ACCOUNT_TYPE_PERSON: 个人账户
 - ACCOUNT_TYPE_ENTERPRISE: 企业账户
 - ACCOUNT_TYPE_UNKNOW: 未知类型
                参数名称：account_id　类型：string　描述：账户ID.
                参数名称：user_id　类型：string　描述：主账号ID 已经弃用.
                参数名称：user_name　类型：string　描述：user_name 主账号ID.
                参数名称：enterprise_name　类型：string　描述：认证主体.
                参数名称：account_level　类型：string　描述：账户等级.

 - ACCOUNT_LEVEL_A: A级客户 合作超过一年（含），无超过90天（含）逾期应收的公司现有全部客户
 - ACCOUNT_LEVEL_C: C级客户 合作超过一年（含），有超过90天（不含含）逾期、但未超过360天（含）的客户
 - ACCOUNT_LEVEL_D: D级客户 合作超过一年（含），有超过360天（不含）逾期的客户
 - ACCOUNT_LEVEL_N: N级客户 合作不到一年的新客户
                参数名称：only_view_unprocessed_records_accounts　类型：integer　描述：仅查看有未处理充值申请记录的账户 0:否 1:是.
                参数名称：order　类型：string　描述：顺序；默认创建时间降序，可选.

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
                    "account_info": [
                        {
                            "account_id": "",
                            "account_level": "[ACCOUNT_LEVEL_UNDEFINED]ACCOUNT_LEVEL_UNDEFINED/ACCOUNT_LEVEL_A/ACCOUNT_LEVEL_C/ACCOUNT_LEVEL_D/ACCOUNT_LEVEL_N",
                            "account_name": "",
                            "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                            "account_used_status": "[ACCOUNT_USED_STATUS_UNSPECIFIED]ACCOUNT_USED_STATUS_UNSPECIFIED/ACCOUNT_USED_STATUS_UNBLOCKED/ACCOUNT_USED_STATUS_BLOCKED",
                            "audit_at": "",
                            "business_assigned": "",
                            "business_code": "",
                            "business_department": "",
                            "business_name": "",
                            "cellphone": "",
                            "created_at": "",
                            "email": "",
                            "empty_status": 0,
                            "enterprise_card_name": "",
                            "enterprise_name": "",
                            "have_second_confirm_recharge_log": 0,
                            "have_unprocessed_recharge_log": 0,
                            "payment_type": "[ACCOUNT_PAYMENT_UNSPECIFIED]ACCOUNT_PAYMENT_UNSPECIFIED/ACCOUNT_PAYMENT_POSTPAID/ACCOUNT_PAYMENT_UNPOSTPAID",
                            "recharge_log_id": "",
                            "status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED",
                            "submit_at": "",
                            "submit_recharge_time": "",
                            "the_last_three_months_bill_amount": "",
                            "updated_at": "",
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminGetCostManagementAccountList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_type", account_type)
        intef.update_params("account_id", account_id)
        intef.update_params("user_id", user_id)
        intef.update_params("user_name", user_name)
        intef.update_params("enterprise_name", enterprise_name)
        intef.update_params("account_level", account_level)
        intef.update_params("only_view_unprocessed_records_accounts", only_view_unprocessed_records_accounts)
        intef.update_params("order", order)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminGetInquiryAccountListGetApi(self, account_type=None, account_id=None, user_id=None, user_name=None, enterprise_name=None, only_view_pending_change_accounts=None, order=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员获取账户查询列表
route: prefix=console-internal actio... """
        """  path: [get]/console-internal/v1/inquiry_accounts API """
        """  params: 
                参数名称：account_type　类型：string　描述：账户类型 必选.

 - ACCOUNT_TYPE_UNSPECIFIED: 未指定
 - ACCOUNT_TYPE_PERSON: 个人账户
 - ACCOUNT_TYPE_ENTERPRISE: 企业账户
 - ACCOUNT_TYPE_UNKNOW: 未知类型
                参数名称：account_id　类型：string　描述：账户ID.
                参数名称：user_id　类型：string　描述：主账号ID 已经弃用.
                参数名称：user_name　类型：string　描述：user_name 主账号ID.
                参数名称：enterprise_name　类型：string　描述：认证主体.
                参数名称：only_view_pending_change_accounts　类型：integer　描述：仅查看有待更新余额的账户 0:否 1:是.
                参数名称：order　类型：string　描述：顺序；默认创建时间降序，可选.

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
                    "account_info": [
                        {
                            "account_id": "",
                            "account_level": "[ACCOUNT_LEVEL_UNDEFINED]ACCOUNT_LEVEL_UNDEFINED/ACCOUNT_LEVEL_A/ACCOUNT_LEVEL_C/ACCOUNT_LEVEL_D/ACCOUNT_LEVEL_N",
                            "account_name": "",
                            "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                            "account_used_status": "[ACCOUNT_USED_STATUS_UNSPECIFIED]ACCOUNT_USED_STATUS_UNSPECIFIED/ACCOUNT_USED_STATUS_UNBLOCKED/ACCOUNT_USED_STATUS_BLOCKED",
                            "audit_at": "",
                            "business_assigned": "",
                            "business_code": "",
                            "business_department": "",
                            "business_name": "",
                            "cellphone": "",
                            "created_at": "",
                            "email": "",
                            "empty_status": 0,
                            "enterprise_card_name": "",
                            "enterprise_name": "",
                            "have_second_confirm_recharge_log": 0,
                            "have_unprocessed_recharge_log": 0,
                            "payment_type": "[ACCOUNT_PAYMENT_UNSPECIFIED]ACCOUNT_PAYMENT_UNSPECIFIED/ACCOUNT_PAYMENT_POSTPAID/ACCOUNT_PAYMENT_UNPOSTPAID",
                            "recharge_log_id": "",
                            "status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED",
                            "submit_at": "",
                            "submit_recharge_time": "",
                            "the_last_three_months_bill_amount": "",
                            "updated_at": "",
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminGetInquiryAccountList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_type", account_type)
        intef.update_params("account_id", account_id)
        intef.update_params("user_id", user_id)
        intef.update_params("user_name", user_name)
        intef.update_params("enterprise_name", enterprise_name)
        intef.update_params("only_view_pending_change_accounts", only_view_pending_change_accounts)
        intef.update_params("order", order)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminListPolicyGroupGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  系统工具 超级管理员策略组列表
route: prefix=console-internal act... """
        """  path: [get]/console-internal/v1/policygroups API """
        """  params: 

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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminListPolicyGroup")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminGetAllPolicyGroupsByUserIDGetApi(self, user_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  系统工具 超级管理员根据user_id获取策略组列表
route: prefix=console-i... """
        """  path: [get]/console-internal/v1/user/policygroups API """
        """  params: 
                参数名称：user_id　类型：string　描述：权限组名称
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminGetAllPolicyGroupsByUserID")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("user_id", user_id)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_CreateInternalUserWithAccountPostApi(self, email=None, phone=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  运营后台主用户注册
route: prefix=console action=CreateInter... """
        """  path: [post]/console-internal/v1/user_accounts API """
        """  body: 
                {
                    "email": "",
                    "phone": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "account_info": {
                        "account_id": "",
                        "account_name": "",
                        "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                        "account_used_status": "[ACCOUNT_USED_STATUS_UNSPECIFIED]ACCOUNT_USED_STATUS_UNSPECIFIED/ACCOUNT_USED_STATUS_UNBLOCKED/ACCOUNT_USED_STATUS_BLOCKED",
                        "audit_at": "",
                        "business_assigned": "",
                        "business_code": "",
                        "business_department": "",
                        "business_name": "",
                        "cellphone": "",
                        "created_at": "",
                        "email": "",
                        "enterprise_card_name": "",
                        "enterprise_name": "",
                        "payment_type": "[ACCOUNT_PAYMENT_UNSPECIFIED]ACCOUNT_PAYMENT_UNSPECIFIED/ACCOUNT_PAYMENT_POSTPAID/ACCOUNT_PAYMENT_UNPOSTPAID",
                        "status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED",
                        "submit_at": "",
                        "updated_at": "",
                        "user_id": "",
                        "user_name": ""
                    },
                    "user_info": {
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
                        "password": "",
                        "profile_photo_id": "",
                        "user_id": "",
                        "user_name": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_CreateInternalUserWithAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("email", email)
        intef.update_body("phone", phone)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminGetUserBaseInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  超级管理员获取用户基本信息
route: prefix=console-internal actio... """
        """  path: [get]/console-internal/v1/users/base_info API """
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminGetUserBaseInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_ConsoleInternalUpdateUserCellphonePostApi(self, phone=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  运营后台手机号码修改
route: prefix=console action=ConsoleInt... """
        """  path: [post]/console-internal/v1/users/cellphone_set API """
        """  body: 
                {
                    "code": "",
                    "phone": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_ConsoleInternalUpdateUserCellphone")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("phone", phone)
        intef.update_body("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminSendSmsCodeGetApi(self, mode=None, value=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  运营后台申请验证码需要填写手机号或者邮箱账号
route: prefix=console actio... """
        """  path: [get]/console-internal/v1/users/code API """
        """  params: 
                参数名称：mode　类型：integer　描述：模式 0：邮箱 1：手机 必选.
                参数名称：value　类型：string　描述：邮箱/手机号 必选
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminSendSmsCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("mode", mode)
        intef.update_params("value", value)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminVerifySmsCodeGetApi(self, mode=None, value=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  运营后台验证验证码需要填写手机号或者邮箱账号
route: prefix=console actio... """
        """  path: [get]/console-internal/v1/users/code/verify API """
        """  params: 
                参数名称：mode　类型：integer　描述：模式 0：邮箱 1：手机 必选.
                参数名称：value　类型：string　描述：邮箱/手机号 必选.
                参数名称：code　类型：string　描述：验证码 必选
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminVerifySmsCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("mode", mode)
        intef.update_params("value", value)
        intef.update_params("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_SendCurrentAdminUserSmsCodeGetApi(self, mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  申请验证码用当前超级管理员用户user_id的手机号或者邮箱账号
route: prefix=con... """
        """  path: [get]/console-internal/v1/users/current_user/code API """
        """  params: 
                参数名称：mode　类型：integer　描述：模式 0：邮箱 1：手机 必选
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_SendCurrentAdminUserSmsCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("mode", mode)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_VerifyCurrentAdminUserSmsCodeGetApi(self, mode=None, code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  运营后台验证验证码用当前用户user_id的手机号或者邮箱账号
route: prefix=cons... """
        """  path: [get]/console-internal/v1/users/current_user/code/verify API """
        """  params: 
                参数名称：mode　类型：integer　描述：模式 0：邮箱 1：手机 必选.
                参数名称：code　类型：string　描述：验证码 必选
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_VerifyCurrentAdminUserSmsCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("mode", mode)
        intef.update_params("code", code)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_AdminBatchAddPolicyGroupToUserPostApi(self, user_id=None, group_id_list=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  系统工具 超级管理员批量授权子用户权限组
route: prefix=console-interna... """
        """  path: [post]/console-internal/v1/users/user_id/batch_policygroups API """
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_AdminBatchAddPolicyGroupToUser")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("group_id_list", group_id_list)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_GetWhitelistAccountsGetApi(self, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  运营后台查询白名单账户列表
route: prefix=console-internal actio... """
        """  path: [get]/console-internal/v1/white_list_accounts API """
        """  params: 
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
                            "account_id": "",
                            "mobile": "",
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_GetWhitelistAccounts")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_CreateWhitelistAccountPostApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  运营后台创建白名单账户
route: prefix=console-internal action=... """
        """  path: [post]/console-internal/v1/white_list_accounts API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                {
                    "password": "",
                    "user_name": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_CreateWhitelistAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleInternalAuthService_DeleteWhitelistAccountPostApi(self, user_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  运营后台移除白名单账户
route: prefix=console-internal action=... """
        """  path: [post]/console-internal/v1/white_list_accounts/delete API """
        """  body: 
                {
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("authInternalAuth", "ConsoleInternalAuthService_DeleteWhitelistAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        return intef.request() if sendRequest else intef

