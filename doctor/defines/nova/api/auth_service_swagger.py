#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class AuthSwaggerApi(BaseApi):
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

    def ConsoleAuthService_GetAccountInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取当前账户的信息 包含账户是否被禁用 是否开启后付费
route: prefix=console ... """
        """  path: [get]/console/v1/accounts/account_info API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                    "account_used_status": "[ACCOUNT_USED_STATUS_UNSPECIFIED]ACCOUNT_USED_STATUS_UNSPECIFIED/ACCOUNT_USED_STATUS_UNBLOCKED/ACCOUNT_USED_STATUS_BLOCKED",
                    "payment_type": "[ACCOUNT_PAYMENT_UNSPECIFIED]ACCOUNT_PAYMENT_UNSPECIFIED/ACCOUNT_PAYMENT_POSTPAID/ACCOUNT_PAYMENT_UNPOSTPAID"
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
        intef = collections.interface("Auth", "ConsoleAuthService_GetAccountInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleAuthService_GetAccountStatusGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账号中心实名认证 获取认证结果
route: prefix=console action=GetAc... """
        """  path: [get]/console/v1/accounts/auth_status API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "account_type": "[ACCOUNT_TYPE_UNSPECIFIED]ACCOUNT_TYPE_UNSPECIFIED/ACCOUNT_TYPE_PERSON/ACCOUNT_TYPE_ENTERPRISE/ACCOUNT_TYPE_UNKNOW",
                    "audit_desc": "",
                    "person_status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED",
                    "status": "[ACCOUNT_STATUS_UNSPECIFIED]ACCOUNT_STATUS_UNSPECIFIED/ACCOUNT_STATUS_BERINGCERTIFIED/ACCOUNT_STATUS_SUCCEEDED/ACCOUNT_STATUS_FAILED/ACCOUNT_STATUS_CHANGED/ACCOUNT_STATUS_CHANGED_FAILED/ACCOUNT_AUDIT_STATUS_UNCERTIFIED"
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
        intef = collections.interface("Auth", "ConsoleAuthService_GetAccountStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleAuthService_GetEnterpriseAccountGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账号中心实名认证 查看企业认证数据
route: prefix=console action=Get... """
        """  path: [get]/console/v1/accounts/enterprise API """
        """  params: 

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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("Auth", "ConsoleAuthService_GetEnterpriseAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleAuthService_GetEnterpriseAccountUnRedactedInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账号中心实名认证 查看企业认证未脱敏数据(姓名或者手机号)
route: prefix=consol... """
        """  path: [get]/console/v1/accounts/enterprise/unredacted_info API """
        """  params: 

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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("Auth", "ConsoleAuthService_GetEnterpriseAccountUnRedactedInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleAuthService_SubmitEnterpriseAccountPostApi(self, enterprise_account=None, phone_code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账号中心实名认证 企业提交认证
route: prefix=console action=Submi... """
        """  path: [post]/console/v1/accounts/enterprise_submit API """
        """  body: 
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
        intef = collections.interface("Auth", "ConsoleAuthService_SubmitEnterpriseAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("enterprise_account", enterprise_account)
        intef.update_body("phone_code", phone_code)
        return intef.request() if sendRequest else intef

    def ConsoleAuthService_UpdateEnterpriseAccountPostApi(self, enterprise_account=None, phone_code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账号中心实名认证 企业变更认证
route: prefix=console action=Updat... """
        """  path: [post]/console/v1/accounts/enterprise_update API """
        """  body: 
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
        intef = collections.interface("Auth", "ConsoleAuthService_UpdateEnterpriseAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("enterprise_account", enterprise_account)
        intef.update_body("phone_code", phone_code)
        return intef.request() if sendRequest else intef

    def ConsoleAuthService_GetIndustryInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账号中心实名认证 获取行业信息
route: prefix=console action=GetIn... """
        """  path: [get]/console/v1/accounts/industry_info API """
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
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("Auth", "ConsoleAuthService_GetIndustryInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleAuthService_GetPersonAccountGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账号中心实名认证 查看个人认证数据
route: prefix=console action=Get... """
        """  path: [get]/console/v1/accounts/person API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "cellphone": "",
                    "person_account": {
                        "cellphone": "",
                        "person_card_end_at": "",
                        "person_card_number": "",
                        "person_card_photo1": "",
                        "person_card_start_at": "",
                        "person_card_type": "[IDCREDENTIAL_TYPE_UNSPECIFIED]IDCREDENTIAL_TYPE_UNSPECIFIED/IDCREDENTIAL_TYPE_IDCARD/IDCREDENTIAL_TYPE_PASSPORT/IDCREDENTIAL_TYPE_HKMOCER/IDCREDENTIAL_TYPE_TWCER/IDCREDENTIAL_TYPE_FOREIGNERS/IDCREDENTIAL_TYPE_HKMORP",
                        "person_name": ""
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
        intef = collections.interface("Auth", "ConsoleAuthService_GetPersonAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleAuthService_GetPersonAccountUnRedactedInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账号中心实名认证 查看个人认证未脱敏数据(姓名或者手机号或者身份证号码)
route: prefix... """
        """  path: [get]/console/v1/accounts/person/unredacted_info API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "cellphone": "",
                    "person_account": {
                        "cellphone": "",
                        "person_card_end_at": "",
                        "person_card_number": "",
                        "person_card_photo1": "",
                        "person_card_start_at": "",
                        "person_card_type": "[IDCREDENTIAL_TYPE_UNSPECIFIED]IDCREDENTIAL_TYPE_UNSPECIFIED/IDCREDENTIAL_TYPE_IDCARD/IDCREDENTIAL_TYPE_PASSPORT/IDCREDENTIAL_TYPE_HKMOCER/IDCREDENTIAL_TYPE_TWCER/IDCREDENTIAL_TYPE_FOREIGNERS/IDCREDENTIAL_TYPE_HKMORP",
                        "person_name": ""
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
        intef = collections.interface("Auth", "ConsoleAuthService_GetPersonAccountUnRedactedInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleAuthService_SubmitPersonAccountPostApi(self, person_account=None, phone_code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账号中心实名认证 个人提交认证
route: prefix=console action=Submi... """
        """  path: [post]/console/v1/accounts/person_submit API """
        """  body: 
                {
                    "person_account": {
                        "cellphone": "",
                        "person_card_end_at": "",
                        "person_card_number": "",
                        "person_card_photo1": "",
                        "person_card_start_at": "",
                        "person_card_type": "[IDCREDENTIAL_TYPE_UNSPECIFIED]IDCREDENTIAL_TYPE_UNSPECIFIED/IDCREDENTIAL_TYPE_IDCARD/IDCREDENTIAL_TYPE_PASSPORT/IDCREDENTIAL_TYPE_HKMOCER/IDCREDENTIAL_TYPE_TWCER/IDCREDENTIAL_TYPE_FOREIGNERS/IDCREDENTIAL_TYPE_HKMORP",
                        "person_name": ""
                    },
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
        intef = collections.interface("Auth", "ConsoleAuthService_SubmitPersonAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("person_account", person_account)
        intef.update_body("phone_code", phone_code)
        return intef.request() if sendRequest else intef

    def ConsoleAuthService_UpdatePersonAccountPostApi(self, person_account=None, phone_code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  账号中心实名认证 个人变更认证
route: prefix=console action=Updat... """
        """  path: [post]/console/v1/accounts/person_update API """
        """  body: 
                {
                    "person_account": {
                        "cellphone": "",
                        "person_card_end_at": "",
                        "person_card_number": "",
                        "person_card_photo1": "",
                        "person_card_start_at": "",
                        "person_card_type": "[IDCREDENTIAL_TYPE_UNSPECIFIED]IDCREDENTIAL_TYPE_UNSPECIFIED/IDCREDENTIAL_TYPE_IDCARD/IDCREDENTIAL_TYPE_PASSPORT/IDCREDENTIAL_TYPE_HKMOCER/IDCREDENTIAL_TYPE_TWCER/IDCREDENTIAL_TYPE_FOREIGNERS/IDCREDENTIAL_TYPE_HKMORP",
                        "person_name": ""
                    },
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
        intef = collections.interface("Auth", "ConsoleAuthService_UpdatePersonAccount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("person_account", person_account)
        intef.update_body("phone_code", phone_code)
        return intef.request() if sendRequest else intef

