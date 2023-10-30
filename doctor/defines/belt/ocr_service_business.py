#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time

from commonlib import config
from commonlib.decorator import wait
from commonlib.sign_utils import encode_jwt_token
from defines.belt.api.ocr_service_swagger import OcrSwaggerApi


"""
使用说明：


"""


class OcrSwaggerBusiness(OcrSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(OcrSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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
        inte_obj.set_headers("X-Belt-Version", "v1")
        if inte_obj.path == '/v1/ocr/bankcard':
            inte_obj.set_headers('X-Belt-Action', 'OCRBankcard')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/h5/ocr/idcard':
            inte_obj.set_headers('X-Belt-Action', 'H5OCRIDCard')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/ocr/business_license':
            inte_obj.set_headers('X-Belt-Action', 'OCRBusinessLicense')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/ocr/driving_license':
            inte_obj.set_headers('X-Belt-Action', 'OCRDrivingLicense')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/ocr/hk_macau_exit_entry_permit':
            inte_obj.set_headers('X-Belt-Action', 'OCRHKMacauExitEntryPermit')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/ocr/idcard':
            inte_obj.set_headers('X-Belt-Action', 'OCRIDCard')
            inte_obj.set_headers('X-Belt-Version', 'v1')     
        elif inte_obj.path == '/v1/ocr/passport':
            inte_obj.set_headers('X-Belt-Action', 'OCRPassport')
            inte_obj.set_headers('X-Belt-Version', 'v1')      
        elif inte_obj.path == '/v1/ocr/taiwan_exit_entry_permit':
            inte_obj.set_headers('X-Belt-Action', 'OCRTaiwanExitEntryPermit')
            inte_obj.set_headers('X-Belt-Version', 'v1')        
        elif inte_obj.path == '/v1/ocr/vehicle_license':
            inte_obj.set_headers('X-Belt-Action', 'OCRVehicleLicense')
            inte_obj.set_headers('X-Belt-Version', 'v1')                   
        elif inte_obj.path == '/v1/ocr/car_plate':
            inte_obj.set_headers('X-Belt-Action', 'OCRCarPlate')
            inte_obj.set_headers('X-Belt-Version', 'v1')    
        elif inte_obj.path == '/v1/ocr/create_session':
            inte_obj.set_headers('X-Belt-Action', 'CreateSession')
            inte_obj.set_headers('X-Belt-Version', 'v1')       
            
            
        #qps limit 5/s
        time.sleep(0.2)        

    def idsImageToBase64(self, image_name):
        return self.imageToBase64(os.path.join(config.ids_image_path, image_name))

    def OCRBankcard(self, image=None, encrypt_info=None):
        """ 银行卡单接口"""
        if image and not image.startswith("/"):
            image = self.idsImageToBase64(image)
        elif image:
            image=self.imageToBase64(image)
        if not encrypt_info:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.OCRService_OCRBankcardPostApi(image=image, encrypt_info=encrypt_info)
        return resp
    
    def OCRBusinessLicense(self, image=None, encrypt_info=None):
        """ 营业执照单接口"""
        if image and not image.startswith("/"):
            image = self.idsImageToBase64(image)
        if not encrypt_info:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.OCRService_OCRBusinessLicensePostApi(image=image, encrypt_info=encrypt_info)
        return resp

    def OCRDrivingLicense(self, image=None, encrypt_info=None):
        """ 驾驶证单接口"""
        if image and not image.startswith("/"):
            image = self.idsImageToBase64(image)
        if not encrypt_info:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.OCRService_OCRDrivingLicensePostApi(image=image, encrypt_info=encrypt_info)
        return resp

    def OCRHKMacauExitEntryPermit(self, image=None, encrypt_info=None):
        """港澳通行证单接口"""
        if image and not image.startswith("/"):
            image = self.idsImageToBase64(image)
        if not encrypt_info:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.OCRService_OCRHKMacauExitEntryPermitPostApi(image=image, encrypt_info=encrypt_info)
        return resp

    def OCRIDCard(self, image=None, side=None,detect_quality=None,encrypt_info=None):
        """身份证单接口"""
        if image and not image.startswith("/"):
            image = self.idsImageToBase64(image)
        if not encrypt_info:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.OCRService_OCRIDCardPostApi(image=image, side=side, detect_quality=detect_quality, encrypt_info=encrypt_info)
        return resp


    def OCRPassport(self, image=None, encrypt_info=None):
        """护照单接口"""
        if image and not image.startswith("/"):
            image = self.idsImageToBase64(image)
        if not encrypt_info:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.OCRService_OCRPassportPostApi(image=image, encrypt_info=encrypt_info)
        return resp


    def OCRTaiwanExitEntryPermit(self, image=None, encrypt_info=None):
        """台湾通行证单接口"""
        if image and not image.startswith("/"):
            image = self.idsImageToBase64(image)
        if not encrypt_info:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.OCRService_OCRTaiwanExitEntryPermitPostApi(image=image, encrypt_info=encrypt_info)
        return resp


    def OCRVehicleLicense(self, image=None, encrypt_info=None):
        """行驶证单接口"""
        if image and not image.startswith("/"):
            image = self.idsImageToBase64(image)
        if not encrypt_info:
            encrypt_info = {
                "algorithm": "ENCRPT_ALGORITHM_NONE",
                "version": 0,
                "encrypted_fields": [
                    "string"
                ],
                "data": "string"
            }
        resp = self.OCRService_OCRVehicleLicensePostApi(image=image, encrypt_info=encrypt_info)
        return resp


    def OCRBusinessLicenseBySubUser(self, ak, sk):
        """ 子账户营业执照识别."""
        aksk_token = encode_jwt_token(ak, sk)
        print('aksk_token {}'.format(aksk_token))

        image_path = os.path.join(
            config.ids_image_path, "ocr/business_license/business_01.jpg")
        image = self.imageToBase64(image_path)
        encrypt_info = None
        resp = self.OCRService_OCRBusinessLicensePostApi(image=image, encrypt_info=encrypt_info, loginToken=aksk_token)
        return resp

    def OCRBankcardBySubUser(self, ak, sk):
        """  子账户银行卡识别."""
        aksk_token = encode_jwt_token(ak, sk)
        print('aksk_token {}'.format(aksk_token))

        image_path = os.path.join(
            config.ids_image_path, "ocr/bankcard/debit_card.jpg")
        image = self.imageToBase64(image_path)
        encrypt_info = None
        resp = self.OCRService_OCRBankcardPostApi(image=image, encrypt_info=encrypt_info, loginToken=aksk_token)
        return resp
