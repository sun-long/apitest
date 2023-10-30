#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time
from commonlib import config
from commonlib.decorator import wait
from defines.belt.api.identity_service_swagger import IdentitySwaggerApi


"""
使用说明：


"""


class IdentitySwaggerBusiness(IdentitySwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(IdentitySwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        if inte_obj.path == '/v1/identity/verify_idcard':
            inte_obj.set_headers('X-Belt-Action', 'VerifyIDCard')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/identity/verify_idcard_face':
            inte_obj.set_headers('X-Belt-Action', 'VerifyIDCardFace')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif  inte_obj.path == '/v1/identity/create_session':
            inte_obj.set_headers('X-Belt-Action', 'CreateSession')
            inte_obj.set_headers('X-Belt-Version', 'v1')   
        elif inte_obj.path == '/v1/identity/get_session_verification_result':
            inte_obj.set_headers('X-Belt-Action', 'GetSessionVerificationResult')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/identity/get_session_liveness_result':
            inte_obj.set_headers('X-Belt-Action', 'GetSessionLivenessResult')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/h5/identity/get_session_config':
            inte_obj.set_headers('X-Belt-Action', 'H5GetSessionConfig')
            inte_obj.set_headers('X-Belt-Version', 'v1')    
        elif inte_obj.path == '/v1/h5/identity/update_idcard':
            inte_obj.set_headers('X-Belt-Action', 'H5UpdateIDCard')
            inte_obj.set_headers('X-Belt-Version', 'v1')    
        elif inte_obj.path == '/v1/identity/compare_face_idcard':
            inte_obj.set_headers('X-Belt-Action', 'CompareFaceIDCard')
            inte_obj.set_headers('X-Belt-Version', 'v1')   
        elif inte_obj.path == '/v1/identity/verify_enterprise':
            inte_obj.set_headers('X-Belt-Action', 'VerifyEnterprise')
            inte_obj.set_headers('X-Belt-Version', 'v1')   
        elif inte_obj.path == '/v1/identity/verify_bankcard':
            inte_obj.set_headers('X-Belt-Action', 'VerifyBankcard')
            inte_obj.set_headers('X-Belt-Version', 'v1')   
            
        #qps limit 5/s
        time.sleep(0.2)        

    def idsImageToBase64(self, image_name):
        return self.imageToBase64(os.path.join(config.ids_image_path, image_name))

    def verifyIDCard(self, name=None, idcard_number=None, expiry_date=None, encrypt_info=None):
        """ 验证二要素身份核验_验证核验功能_设置身份证号正确+名字匹配_有效期大于出生日期_预期匹配"""
        if expiry_date is None:
            expiry_date = '2050-12-12'
        if encrypt_info is None:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                # "iv": "string",
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.IdentityService_VerifyIDCardPostApi(name=name, idcard_number=idcard_number,
                                                        expiry_date=expiry_date, encrypt_info=encrypt_info)
        return resp

    def verifyIDCardFace(self, name=None, idcard_number=None, image=None, expiry_date=None, encrypt_info=None):
        """ 验证三要素身份核验_验证核验功能_设置身份证号正确+名字+图片匹配_有效期大于出生日期_预期匹配"""
        if expiry_date is None:
            expiry_date = '2050-12-12'
        if image and not image.startswith("/"):
            image = self.idsImageToBase64(image)
        if encrypt_info is None:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                # "iv": "string",
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.IdentityService_VerifyIDCardFacePostApi(name=name, idcard_number=idcard_number, image=image,
                                                            expiry_date=expiry_date, encrypt_info=encrypt_info)
        return resp
    


    def CompareFaceIDCard(self, image=None, auto_rotate=None, min_quality_level=None,encrypt_info=None):
        """ 验证手持身份证_验证核验功能_设置身份证号正确+名字+图片匹配_有效期大于出生日期_预期匹配"""
        
        if image and not image.startswith("/"):
            image=self.idsImageToBase64(image)
        elif image:
            image=self.imageToBase64(image)
        if encrypt_info is None:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                # "iv": "string",
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }        
        resp = self.IdentityService_CompareFaceIDCardPostApi(image=image, auto_rotate=auto_rotate, min_quality_level=min_quality_level, encrypt_info=encrypt_info)
        return resp
