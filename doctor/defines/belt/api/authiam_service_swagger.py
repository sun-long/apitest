#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class AuthiamSwaggerApi(BaseApi):
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

    def authorizeGetApi(self, redirect_uri=None, response_type=None, client_id=None, scope=None, state=None,
                 expires_after=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  授权 """
        """  path: [get]/v1/authorize API """
        """  params: 
                *参数名称：redirect_uri　类型：string　描述：必填,授权成功后重定向路径
                *参数名称：response_type　类型：string　描述：选填,默认token
                参数名称：client_id　类型：string　描述：client_id
                参数名称：scope　类型：string　描述：scope
                参数名称：state　类型：string　描述：state
                *参数名称：expires_after　类型：string　描述：必填,jwt过期时间,单位[s
        """
        """  resp:
                301(Moved Permanently):
                ""
                400(Bad Request):
                {
                    "code": 0,
                    "message": ""
                }

        """
        intef = collections.interface("authIam", "授权")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("redirect_uri", redirect_uri)
        intef.update_params("response_type", response_type)
        intef.update_params("client_id", client_id)
        intef.update_params("scope", scope)
        intef.update_params("state", state)
        intef.update_params("expires_after", expires_after)
        return intef.request() if sendRequest else intef

    def captchaGetApi(self, width=None, height=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  图片验证码 """
        """  path: [get]/v1/captcha API """
        """  params: 
                *参数名称：width　类型：integer　描述：必填,验证码宽度像素
                *参数名称：height　类型：integer　描述：选填,验证码高度像
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": "",
                    "digits": "",
                    "id": "",
                    "message": "",
                    "type": ""
                }
                400(Bad Request):
                {
                    "code": 0,
                    "message": ""
                }

        """
        intef = collections.interface("authIam", "图片验证码")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("width", width)
        intef.update_params("height", height)
        return intef.request() if sendRequest else intef

    def changePasswordPostApi(self, data=None, digits=None, id=None, type=None, loginToken=None, sendRequest=True, print_log=True,interface_desc=None):
        """  修改密码 """
        """  path: [post]/v1/change-password API """
        """  body: 
                {
                    "data": "",
                    "digits": "",
                    "id": "",
                    "type": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": ""
                }
                400(Bad Request):
                {
                    "code": 0,
                    "message": ""
                }
                401(Unauthorized):
                {
                    "code": 0,
                    "message": ""
                }

        """
        intef = collections.interface("authIam", "修改密码")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("data", data)
        intef.update_body("digits", digits)
        intef.update_body("id", id)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def emailFindPasswordPostApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  邮箱找回密码 """
        """  path: [post]/v1/email-find-password API """
        """  body: 
                {}
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": ""
                }
                400(Bad Request):
                {
                    "code": 0,
                    "message": ""
                }

        """
        intef = collections.interface("authIam", "邮箱找回密码")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def loginPostApi(self, captcha=None, client_id=None, expires_after=None, email=None,
                     phone=None,verification_code=None,username=None,password=None, source=None,
                     loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  登录 """
        """  path: [post]/v1/login API """
        """  body: 
                {
                    "captcha": {
                      "data": "string",
                      "digits": "string",
                      "id": "string",
                      "type": "string"
                    }, # 验证码
                    "client_id": "",
                    "expires_after": "",  # jwt有效时间,直接登录必填
                    "email": "", # 邮箱地址,邮箱登录必填
                    "phone": "", # 手机号目前仅指出+86,手机登录必填
                    "verification_code": "", # 验证码,手机/邮箱登录必填
                    "username": "", # 用户名,用户名登录必填
                    "password": "", # 密码,md5,用户名登录必填                    
                    "source": "", # 来源必填 【console】【console-internal】            
                }
        """
        """  resp:
                200(OK):
                {
                    "access_token": "",
                    "code": 0,
                    "expires_in": 0,
                    "message": "",
                    "refresh_token": "",
                    "token_type": ""
                }
                301(Moved Permanently):
                ""
                400(Bad Request):
                {
                    "code": 0,
                    "message": ""
                }

        """
        intef = collections.interface("authIam", "登录")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.del_body("data")
        intef.del_body("digits")
        intef.del_body("id")
        intef.del_body("type")
        intef.update_body("captcha", captcha)
        intef.update_body("client_id", client_id)
        intef.update_body("expires_after", expires_after)
        intef.update_body("email", email)
        intef.update_body("phone", phone)
        intef.update_body("verification_code", verification_code)
        intef.update_body("username", username)
        # password = sign_utils.getMd5(password)
        intef.update_body("password", password)
        intef.update_body("source", source)
        return intef.request() if sendRequest else intef

    def loginGetApi(self, redirect_uri=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  登出 """
        """  path: [get]/v1/logout API """
        """  params: 
                *参数名称：redirect_uri　类型：string　描述：必填,登出成功后重定向路
        """
        """  resp:
                301(Moved Permanently):
                ""
                400(Bad Request):
                {
                    "code": 0,
                    "message": ""
                }

        """
        intef = collections.interface("authIam", "登出")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("redirect_uri", redirect_uri)
        return intef.request() if sendRequest else intef

    def ssoLoginGetApi(self, id_token=None, source=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  商汤sso登录地址 """
        """  path: [get]/v1/sensetime-login API """
        """  params: 
                *参数名称：id_token　类型：string　描述：必填,sensetime sso 签发jwt
                参数名称：source　类型：string　描述：用户隔离源,必
        """
        """  resp:
                301(Moved Permanently):
                {
                    "code": 0,
                    "message": ""
                }
                400(Bad Request):
                {
                    "code": 0,
                    "message": ""
                }

        """
        intef = collections.interface("authIam", "商汤sso登录地址")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id_token", id_token)
        intef.update_params("source", source)
        return intef.request() if sendRequest else intef

    def freshTokenPostApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  刷新token """
        """  path: [post]/v1/token API """
        """  body: 
                {}
        """
        """  resp:
                200(OK):
                {
                    "access_token": "",
                    "code": 0,
                    "expires_in": 0,
                    "message": "",
                    "refresh_token": "",
                    "token_type": ""
                }
                400(Bad Request):
                {
                    "code": 0,
                    "message": ""
                }
                401(Unauthorized):
                {
                    "code": 0,
                    "message": ""
                }

        """
        intef = collections.interface("authIam", "刷新token")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def verifyGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  认证 """
        """  path: [get]/v1/verify API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": "",
                    "user_info": {
                        "address": "",
                        "attributes": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        },
                        "blocked": false,
                        "cellphone": "",
                        "company": "",
                        "created_at": "",
                        "description": "",
                        "email": "",
                        "first_login": false,
                        "nick_name": "",
                        "profile_photo_id": 0,
                        "source": "",
                        "source_registry": 0,
                        "st_ladp_name": "",
                        "updated_at": "",
                        "user_id": 0,
                        "user_name": ""
                    }
                }
                400(Bad Request):
                {
                    "code": 0,
                    "message": ""
                }
                401(Unauthorized):
                {
                    "code": 0,
                    "message": ""
                }

        """
        intef = collections.interface("authIam", "认证")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def verificationCodePostApi(self, number=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  发送验证码 """
        """  path: [post]/v1/verification-code API """
        """  body: 
                {
                    "number": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "cooling_interval": 0,
                    "message": "",
                    "status": 0
                }
                400(Bad Request):
                {
                    "code": 0,
                    "message": ""
                }

        """
        intef = collections.interface("authIam", "发送验证码")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("number", number)
        return intef.request() if sendRequest else intef