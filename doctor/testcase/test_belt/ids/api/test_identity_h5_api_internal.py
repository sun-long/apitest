#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pytest
import datetime
import os
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
from commonlib.api_lib.base_api import BaseApi
from commonlib.config import ids_image_path,image_path


@pytest.mark.Regression
class TestIdentityH5ApiInternal(object):
    """ H5调用内部Api测试"""

    @pytest.fixture(scope="class", autouse=True)
    def init_func(self, config_obj):
        # 初始化测试集
        # 所有test运行前运行一次，接收外部参数env_obj，初始化测试环境
        log().info("==========%s测试开始==========" % self.__class__.__name__)

    def teardown_class(self):
        # 所有test运行完后运行一次
        log().info("==========%s测试结束==========\n" % self.__name__)
        log().info("clear tasks finish")

    def setup_method(self, method):
        # 每个测试用例执行之前做操作
        log().info("用例%s开始" % method.__name__)

    def teardown_method(self, method):
        # 每个测试用例执行之后做操作
        log().info("用例%s结束" % method.__name__)

    
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_without_session(self, config_obj, OcrApi):
        """  异常：H5 调用的内部接口,检测识别图片中的身份证, 未传biz_token """
    
        front_image = None
        back_image = None
        encrypt_info = None
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(front_image=front_image, back_image=back_image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session id provided"
        assert resp.json_get("error.details.0.reason") == 12003028
        assert resp.json_get("error.message") == "E12003028: no session id provided"       

    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_without_front_image(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口,检测识别图片中的身份证, 未传front_image """
        token = create_session
        front_image = None
        back_image = None
        encrypt_info = None
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token,front_image=front_image, back_image=back_image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "front image data is empty"
        assert resp.json_get("error.details.0.reason") == 12003983
        assert resp.json_get("error.message") == "E12003983: front image data is empty"   

    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_without_back_image(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口,检测识别图片中的身份证, 未传back_image """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/idcard/normal/idcard_front_01.jpg"))
        back_image = None
        encrypt_info = None
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token,front_image=front_image, back_image=back_image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "back image data is empty"
        assert resp.json_get("error.details.0.reason") == 12003992
        assert resp.json_get("error.message") == "E12003992: back image data is empty"     
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_with_same_side(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口,检测识别图片中的身份证, 正反面一样 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/idcard/normal/idcard_front_01.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/idcard/normal/idcard_front_01.jpg"))
        encrypt_info = None
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token,front_image=front_image, back_image=back_image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid id card with the same side uploaded"
        assert resp.json_get("error.details.0.reason") == 12003034
        assert resp.json_get("error.message") == "E12003034: invalid id card with the same side uploaded"         
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_nonidcard(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口,检测识别图片中的身份证,来源非身份证 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/bankcard/icbc_01.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/bankcard/icbc_02.jpg"))
        encrypt_info = None
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token,front_image=front_image, back_image=back_image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid id card source"
        assert resp.json_get("error.details.0.reason") == 12003012
        assert resp.json_get("error.message") == "E12003012: invalid id card source"           
      

    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_invalid_address(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口CBC加密,检测识别图片中的身份证,地址与签发机关不一致 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/idcard/normal/idcard_front_01.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/idcard/normal/idcard_back_02.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESCipher(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_CBC",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token,front_image=front_image, back_image=back_image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "issue authority not included in the address"
        assert resp.json_get("error.details.0.reason") == 12003011
        assert resp.json_get("error.message") == "E12003011: issue authority not included in the address"   
        

    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_cropped(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,正面裁剪 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/idcard/normal/idcard_front_02.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/idcard/normal/idcard_back_02.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "front idcard cropped"
        assert resp.json_get("error.details.0.reason") == 12003986
        assert resp.json_get("error.message") == "E12003986: front idcard cropped" 
     
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_back_cropped(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,反面裁剪 """
        token = create_session
        front_image =  BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
        back_image =  BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_back_cropped.jpg"))
       
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "back idcard cropped"
        assert resp.json_get("error.details.0.reason") == 12003995
        assert resp.json_get("error.message") == "E12003995: back idcard cropped"    
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_front_occlusion(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,正面遮挡 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(image_path,"go_image/idcard_ws/idcard_occlusion1.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(image_path,"go_image/idcard_ws/idcard_occlusion2.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "front idcard occlusion"
        assert resp.json_get("error.details.0.reason") == 12003987
        assert resp.json_get("error.message") == "E12003987: front idcard occlusion"  
        
    @pytest.mark.P2   
    def test_api_OCRService_H5OCRIDCard_invalid_cardinfo(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,OCR识别字段不可信 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_back_occlusion.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid id card info"
        assert resp.json_get("error.details.0.reason") == 12003010
        assert resp.json_get("error.message") == "E12003010: invalid id card info" 
                           
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_back_occlusion(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,反面遮挡 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_back_occlusion2.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "back idcard occlusion"
        assert resp.json_get("error.details.0.reason") == 12003996
        assert resp.json_get("error.message") == "E12003996: back idcard occlusion"    
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_back_occlusion(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,反面遮挡 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_back_occlusion2.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "back idcard occlusion"
        assert resp.json_get("error.details.0.reason") == 12003996
        assert resp.json_get("error.message") == "E12003996: back idcard occlusion"     
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_front_oversize(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,正面图片大小超过4MB """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/beyond_size_7M.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_back.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400  
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "front image size is exceeded"
        assert resp.json_get("error.details.0.reason") == 12003982
        assert resp.json_get("error.message") == "E12003982: front image size is exceeded"         
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_back_oversize(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,反面图片大小超过4MB """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/beyond_size_7M.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400  
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "back image size is exceeded"
        assert resp.json_get("error.details.0.reason") == 12003991
        assert resp.json_get("error.message") == "E12003991: back image size is exceeded"            
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_front_error_format(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,正面错误的图片格式 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_front.gif"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_back.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400  
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "front image format not supported"
        assert resp.json_get("error.details.0.reason") == 12003984
        assert resp.json_get("error.message") == "E12003984: front image format not supported"    
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_back_error_format(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,反面错误的图片格式 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_back.gif"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400  
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "back image format not supported"
        assert resp.json_get("error.details.0.reason") == 12003993
        assert resp.json_get("error.message") == "E12003993: back image format not supported"  
    
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_front_low_resolutions(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,正面低分辨率 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_front_low_resolutions.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_back.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400  
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "front image low resolution"
        assert resp.json_get("error.details.0.reason") == 12003985
        assert resp.json_get("error.message") == "E12003985: front image low resolution"                 
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_back_low_resolutions(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,反面低分辨率 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_back_low_resolutions.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 400  
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "back image low resolution"
        assert resp.json_get("error.details.0.reason") == 12003994
        assert resp.json_get("error.message") == "E12003994: back image low resolution"    
        
        
    @pytest.mark.skip(reason="图片不合适")
    def test_api_OCRService_H5OCRIDCard_front_dark(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,正面光线弱 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_front_toodark_15.png"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_back.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token,encrypt_info=encrypt_info)
        assert resp.status_code == 400  
        assert resp.json_get("error.code") == 3       
        
    @pytest.mark.skip(reason="图片不合适")
    def test_api_OCRService_H5OCRIDCard_front_bright(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,正面光线弱 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_back_too_bright.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token,encrypt_info=encrypt_info)
        assert resp.status_code == 400  
        assert resp.json_get("error.code") == 3         
        
    @pytest.mark.P2
    def test_api_OCRService_H5OCRIDCard_back_dark(self, config_obj, OcrApi,create_session):
        """  异常：H5 调用的内部接口GCM加密,检测识别图片中的身份证,反面光线弱 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"ocr/h5ocridcard/H5_back_toodark_30.png"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token,front_image=front_image,back_image=back_image,encrypt_info=None)
        assert resp.status_code == 400  
        assert resp.json_get("error.code") == 3    
        assert resp.json_get("error.details.0.message") == "back idcard weak light"
        assert resp.json_get("error.details.0.reason") == 12003998
        assert resp.json_get("error.message") == "E12003998: back idcard weak light"         
        
    @pytest.mark.P0
    def test_api_OCRService_H5OCRIDCard_normal(self, config_obj, OcrApi,create_session):
        """  正向：H5 调用的内部接口CBC加密,检测识别图片中的身份证 """
        token = create_session
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
        back_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_back.jpg"))
        jstr = {"front_image":front_image,
                "back_image":back_image
        }
        key = token.split(".")[-1][:32]
        cryptor = AESCipher(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_CBC",
                        "data": cypher,
                        "encrypted_fields": ["front_image","back_image"]
                    }
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(loginToken=token,front_image=front_image, back_image=back_image, encrypt_info=encrypt_info)
        assert resp.status_code == 200
      
        
    @pytest.mark.P2
    def test_api_IdentityService_H5GetSessionConfig_without_sessionId(self, config_obj, IdentityApi):
        """  异常：H5 调用的内部接口, 获取H5全流程相关配置，未传递session_id """
        session_id = None
        encrypt_info = None
        resp = IdentityApi.IdentityService_H5GetSessionConfigPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session id provided"
        assert resp.json_get("error.details.0.reason") == 12003028
        assert resp.json_get("error.message") == "E12003028: no session id provided"   

    @pytest.mark.P2
    def test_api_IdentityService_H5UpdateIDCard_without_session(self, config_obj, IdentityApi):
        """  异常：H5 内部接口三要素身份核验, 未传递biz_token"""
        name = "金阳"
        idcard_number = "11010219781027232X"
        expiry_date = datetime.datetime.now().strftime('%Y-%m-%d')
        encrypt_info = None
        resp = IdentityApi.IdentityService_H5UpdateIDCardPostApi(name=name, idcard_number=idcard_number, expiry_date=expiry_date, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session id provided"
        assert resp.json_get("error.details.0.reason") == 12003028
        assert resp.json_get("error.message") == "E12003028: no session id provided"            

    @pytest.mark.P2
    def test_api_IdentityService_H5UpdateIDCard_without_name(self, config_obj, IdentityApi,create_session):
        """  异常：H5 内部接口三要素身份核验, 未传递name"""
        token = create_session
        name = None
        idcard_number = None
        expiry_date = None
        encrypt_info = None
        resp = IdentityApi.IdentityService_H5UpdateIDCardPostApi(loginToken=token,name=name, idcard_number=idcard_number, expiry_date=expiry_date, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid name"
        assert resp.json_get("error.details.0.reason") == 12003001
        assert resp.json_get("error.message") == "E12003001: invalid name"   

    @pytest.mark.P2
    def test_api_IdentityService_H5UpdateIDCard_without_idcard_number(self, config_obj, IdentityApi,create_session):
        """  异常：H5 内部接口三要素身份核验, 未传递idcard_number"""
        token = create_session
        name = "金阳"
        idcard_number = None
        expiry_date = None
        encrypt_info = None
        resp = IdentityApi.IdentityService_H5UpdateIDCardPostApi(loginToken=token,name=name, idcard_number=idcard_number, expiry_date=expiry_date, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid id card number"
        assert resp.json_get("error.details.0.reason") == 12003002
        assert resp.json_get("error.message") == "E12003002: invalid id card number"  

    @pytest.mark.P1
    def test_api_IdentityService_H5UpdateIDCard(self, config_obj, IdentityApi,create_session):
        """  正常：H5 内部接口三要素身份核验CBC加密, 根据权威源校验身份证号和姓名是否匹配, 并比对请求中人脸图片和权威库图片"""
        token = create_session
        name = "金阳"
        idcard_number = "11010219781027232X"
        expiry_date = datetime.datetime.now().strftime('%Y-%m-%d')
        jstr = {"name":name,"idcard_number":idcard_number,"expiry_date":expiry_date}
        #用biztoken的内部接口加密key非sk
        key = token.split(".")[-1][:32]
        cryptor = AESCipher(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_CBC",
                        "data": cypher,
                        "encrypted_fields": ["name","idcard_number","expiry_date"]
                    }
        resp = IdentityApi.IdentityService_H5UpdateIDCardPostApi(loginToken=token, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        
    @pytest.mark.P1
    def test_api_IdentityService_encrypted_H5UpdateIDCard(self, config_obj, user_info,IdentityApi,create_session):
        """  正常：加密H5 内部接口三要素身份核验GCM加密, 根据权威源校验身份证号和姓名是否匹配, 并比对请求中人脸图片和权威库图片"""
        token = create_session
        log().info(f"token:{token}")
        name = "金阳"
        idcard_number = "11010219781027232X"
        expiry_date = datetime.datetime.now().strftime('%Y-%m-%d')
        jstr = {"name":name,"idcard_number":idcard_number,"expiry_date":expiry_date}
        #用biztoken的内部接口加密key非sk
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["name","idcard_number","expiry_date"]
                    }
        resp = IdentityApi.IdentityService_H5UpdateIDCardPostApi(loginToken=token,encrypt_info=encrypt_info)
        assert resp.status_code == 200
        
        

    