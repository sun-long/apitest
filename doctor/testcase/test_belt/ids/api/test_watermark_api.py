#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
import json,base64
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
from commonlib.api_lib.AES_new import  AESCipher

@pytest.mark.P0
@pytest.mark.Regression
class TestWatermarkApi(object):
    """ watermark Api测试"""

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

    def test_api_DataSecurityService_SignImage_0(self, config_obj, WatermarkApi,test_watermark):
        """验证可加入水印功能_输入image_输出水印后的图片"""
        image =WatermarkApi.idsImageToBase64(test_watermark)
        watermark="5ZWG5rGk56eR5oqA"#sensetime
        encrypt_info = None
        resp = WatermarkApi.DataSecurityService_SignImagePostApi(image=image, watermark=watermark, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        watermarked_image=resp.json_get("image")
        with open("test1.json","w") as f:
            json.dump(watermarked_image,f)
        #生成一组商汤科技的水印图片
        test_watermark_path=os.path.splitext(os.path.basename(test_watermark))[0]+"_sensetime"+os.path.splitext(os.path.basename(test_watermark))[-1]
        WatermarkApi.idsBase64ToImage(watermarked_image,test_watermark_path)
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=watermarked_image, watermark=watermark, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")==1
        
    @pytest.mark.xfail(reason="已知算法模型问题")   
    def test_api_DataSecurityService_SignImage_1(self, config_obj, WatermarkApi,test_have_watermarked):
        """验证水印不可覆盖功能_输入已加密后的水印图片_输出不再水印"""
        image =WatermarkApi.idsImageToBase64(test_have_watermarked)
        watermark_str="5YaN5qyh"#再次
        encrypt_info = None
        resp = WatermarkApi.DataSecurityService_SignImagePostApi(image=image, watermark=watermark_str, encrypt_info=encrypt_info)
        assert resp.status_code != 200

    def test_api_DataSecurityService_SignImage_GCM_image(self, config_obj, WatermarkApi,test_watermark,user_info):
        """验证水印GCM加密功能_仅加密image"""
        image =WatermarkApi.idsImageToBase64(test_watermark)
        watermark="5ZWG5rGk56eR5oqA"#sensetime
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": image}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = WatermarkApi.DataSecurityService_SignImagePostApi(image=None, watermark=watermark, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        encrypt_info_data = cryptor.decrypt(resp.json_get("encrypt_info.data"))
        encrypt_info_data = json.loads(encrypt_info_data)
        watermarked_image=encrypt_info_data["image"]
        with open("test2.json","w") as f:
            json.dump(watermarked_image,f)
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=watermarked_image, watermark=watermark, encrypt_info=None)
        assert resp.status_code == 200
        assert resp.json_get("score")==1

    def test_api_DataSecurityService_SignImage_GCM_watermark(self, config_obj, WatermarkApi,test_watermark,user_info):
        """验证水印GCM加密功能_仅加密watermark"""
        image =WatermarkApi.idsImageToBase64(test_watermark)
        watermark="5ZWG5rGk56eR5oqA"#sensetime
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"watermark":watermark}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["watermark"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = WatermarkApi.DataSecurityService_SignImagePostApi(image=image, watermark=None, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        encrypt_info_data = cryptor.decrypt(resp.json_get("encrypt_info.data"))
        encrypt_info_data = json.loads(encrypt_info_data)
        watermarked_image=encrypt_info_data["image"]
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=watermarked_image, watermark=watermark, encrypt_info=None)
        assert resp.status_code == 200
        assert resp.json_get("score")==1

    def test_api_DataSecurityService_SignImage_GCM(self, config_obj, WatermarkApi,test_watermark,user_info):
        """验证水印GCM加密功能"""
        image =WatermarkApi.idsImageToBase64(test_watermark)
        watermark="5ZWG5rGk56eR5oqA"#sensetime
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": image,"watermark":watermark}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image","watermark"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = WatermarkApi.DataSecurityService_SignImagePostApi(image=None, watermark=None, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        encrypt_info_data = cryptor.decrypt(resp.json_get("encrypt_info.data"))
        encrypt_info_data = json.loads(encrypt_info_data)
        watermarked_image=encrypt_info_data["image"]
        # with open("test2.json","w") as f:
        #     json.dump(watermarked_image,f)
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=watermarked_image, watermark=watermark, encrypt_info=None)
        assert resp.status_code == 200
        assert resp.json_get("score")==1


    def test_api_DataSecurityService_SignImage_CBC(self, config_obj, WatermarkApi,test_watermark,user_info):
        """验证水印CBC加密功能"""
        image =WatermarkApi.idsImageToBase64(test_watermark)
        watermark="5ZWG5rGk56eR5oqA"#sensetime
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": image,"watermark":watermark}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image","watermark"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = WatermarkApi.DataSecurityService_SignImagePostApi(image=None, watermark=None, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        encrypt_info_data = cryptor.decrypt(resp.json_get("encrypt_info.data"))
        encrypt_info_data = json.loads(encrypt_info_data)
        watermarked_image=encrypt_info_data["image"]
        # with open("test2.json","w") as f:
        #     json.dump(watermarked_image,f)
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=watermarked_image, watermark=watermark, encrypt_info=None)
        assert resp.status_code == 200
        assert resp.json_get("score")==1          


    def test_api_DataSecurityService_VerifyImage(self, config_obj, WatermarkApi,test_have_watermarked):
        """  图片数字水印验签接口"""
        image =WatermarkApi.idsImageToBase64(test_have_watermarked)
        watermark="5ZWG5rGk56eR5oqA"#sensetime
        encrypt_info = None
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=image, watermark=watermark, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")==1   

    def test_api_DataSecurityService_VerifyImage_CBC(self, config_obj, WatermarkApi,test_have_watermarked,user_info):
        """  图片数字水印验签接口_CBC加密"""
        image =WatermarkApi.idsImageToBase64(test_have_watermarked)
        watermark="5ZWG5rGk56eR5oqA"#m
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": image,"watermark":watermark}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image","watermark"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=image, watermark=watermark, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")==1        

    def test_api_DataSecurityService_VerifyImage_CBC_image(self, config_obj, WatermarkApi,test_have_watermarked,user_info):
        """  图片数字水印验签接口_CBC加密_仅加密image"""
        image =WatermarkApi.idsImageToBase64(test_have_watermarked)
        watermark="5ZWG5rGk56eR5oqA"#m
        cryptor = AESCipher(user_info.sk)
        jstr = {"image": image}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=None, watermark=watermark, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")==1 

    def test_api_DataSecurityService_VerifyImage_CBC_watermark(self, config_obj, WatermarkApi,test_have_watermarked,user_info):
        """  图片数字水印验签接口_CBC加密_仅加密watermark"""
        image =WatermarkApi.idsImageToBase64(test_have_watermarked)
        watermark="5ZWG5rGk56eR5oqA"#m
        cryptor = AESCipher(user_info.sk)
        jstr = {"watermark": watermark}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["watermark"]        
        encrypt_info={
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=image, watermark=None, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")==1    

    def test_api_DataSecurityService_VerifyImage_GCM(self, config_obj, WatermarkApi,test_have_watermarked,user_info):
        """  图片数字水印验签接口_GCM加密"""
        image =WatermarkApi.idsImageToBase64(test_have_watermarked)
        watermark="5ZWG5rGk56eR5oqA"#m
        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": image,"watermark":watermark}
        txt = json.dumps(jstr)
        cypher = cryptor.encrypt(txt)
        # de_cypher=cryptor.decrypt(cypher)
        feilds=["image","watermark"]        
        encrypt_info={
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": feilds,
            "data": cypher
        }
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=image, watermark=watermark, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")==1  


    def test_api_DataSecurityService_VerifyImage_errorcode(self, config_obj, WatermarkApi,test_have_watermarked,user_info):
        """  图片数字验签接口_错误码字"""
        image =WatermarkApi.idsImageToBase64(test_have_watermarked)
        watermark=None
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=image, watermark=watermark, encrypt_info=None)
        assert resp.status_code !=200
        assert resp.json_get("error")["code"]==3
        assert resp.json_get("error")["message"]=="E12003150: watermark is empty"


    def test_api_DataSecurityService_SignImage_errorcode(self, config_obj, WatermarkApi,test_watermark):
        """验证图片水印功能_错误码字"""
        image =WatermarkApi.idsImageToBase64(test_watermark)
        watermark=None
        encrypt_info = None
        resp = WatermarkApi.DataSecurityService_SignImagePostApi(image=image, watermark=watermark, encrypt_info=encrypt_info)
        assert resp.status_code != 200
        assert resp.json_get("error")["code"]==3
        assert resp.json_get("error")["message"]=="E12003150: watermark is empty"


    def test_api_DataSecurityService_VerifyImage_accuracy(self, config_obj, WatermarkApi,test_watermark_accuracy):
        """验证验签功能的精度"""
        image =WatermarkApi.idsImageToBase64(test_watermark_accuracy)
        watermark="5ZWG5rGk56eR5oqA"
        encrypt_info = None
        resp = WatermarkApi.DataSecurityService_VerifyImagePostApi(image=image, watermark=watermark, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("score")>0.5
        

if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])
