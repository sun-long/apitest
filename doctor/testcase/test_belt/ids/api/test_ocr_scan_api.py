#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
import uuid
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor


class TestOcrScanApi(object):
    """ 身份证\银行卡扫描相关Api测试"""

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

    @pytest.mark.P0
    def test_api_OCRService_CreateSession_idcard(self, config_obj, OcrApi):
        """  创建一个身份证扫描会话 """
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "IDCARD_SCAN",
            "uuid": uuid_str
        }
        encrypt_info = None
        resp = OcrApi.OCRService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token","session_id"], response_type="200")
    
    @pytest.mark.P0   
    def test_api_OCRService_CreateSession_idcard_GCM(self, config_obj, user_info,OcrApi):
        """  创建一个GCM加密身份证扫描会话 """
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "IDCARD_SCAN",
            "uuid": uuid_str
        }        
        jstr = {
            "session": session,
        }
        cryptor = AESGCMCryptor(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": ["session"],
            "data": cypher
        }  
        resp = OcrApi.OCRService_CreateSessionPostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id"], response_type="200")
        
    @pytest.mark.P0
    @pytest.mark.parametrize("quality_level", [
        "EXTREMELY_LOW",
        "LOW",
        "NORMAL",
        "HIGH"
    ])    
    def test_api_OCRService_CreateSession_idcard_quality(self, config_obj, user_info,OcrApi,quality_level):
        """  创建一个GCM加密身份证扫描会话,质量等级控制 """
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "IDCARD_SCAN",
            "uuid": uuid_str,
            "idcard_min_quality_level":quality_level
        }        
        jstr = {
            "session": session,
        }
        cryptor = AESGCMCryptor(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": ["session"],
            "data": cypher
        }  
        resp = OcrApi.OCRService_CreateSessionPostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id"], response_type="200")    

    @pytest.mark.P0 
    def test_api_OCRService_CreateSession_bankcard(self, config_obj, OcrApi):
        """  创建一个银行卡扫描会话 """
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "BANKCARD_SCAN",
            "uuid": uuid_str
        }
        encrypt_info = None
        resp = OcrApi.OCRService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token","session_id"], response_type="200")     
    
    @pytest.mark.P0
    def test_api_OCRService_CreateSession_bankcard_CBC(self, config_obj, user_info,OcrApi):
        """  创建一个CBC加密身份证扫描会话 """
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "BANKCARD_SCAN",
            "uuid": uuid_str
        }        
        jstr = {
            "session": session,
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["session"],
            "data": cypher
        }  
        resp = OcrApi.OCRService_CreateSessionPostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id"], response_type="200")    
        
    @pytest.mark.P1
    def test_api_OCRService_CreateSession_without_session(self, config_obj, OcrApi):
        """  异常：创建一个ocr检测会话,未传递session"""
        session = None
        encrypt_info = None
        resp = OcrApi.OCRService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session info provided"
        assert resp.json_get("error.details.0.reason") == 12003029
        assert resp.json_get("error.message") == "E12003029: no session info provided"        
        
    @pytest.mark.P1
    @pytest.mark.parametrize("session_type", [
        None,
        "LIVENESS",
        "H5_LIVENESS",
        "IDENTITY_VERIFICATION"
    ])    
    def test_api_OCRService_CreateSession_invalid_sessiontype(self, config_obj, OcrApi,session_type):
        """  异常：创建一个ocr检测会话,非法session_type"""
        uuid_str =str(uuid.uuid4())
        session = { "uuid": uuid_str,
                   "session_type":session_type}
        encrypt_info = None
        resp = OcrApi.OCRService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid session type"
        assert resp.json_get("error.details.0.reason") == 12003080
        assert resp.json_get("error.message") == "E12003080: invalid session type"   
        
        
    @pytest.mark.P1 
    def test_api_OCRService_CreateSession_invalid_quality_level(self, config_obj, OcrApi):
        """  异常：创建一个身份证ocr检测会话,非法idcard_min_quality_level"""
        uuid_str =str(uuid.uuid4())
        session = { "uuid": uuid_str,
                   "session_type":"IDCARD_SCAN",
                   "idcard_min_quality_level":100}
        encrypt_info = None
        resp = OcrApi.OCRService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        # assert resp.json_get("error.code") == 3
        # assert resp.json_get("error.details.0.message") == "invalid session type"
        # assert resp.json_get("error.details.0.reason") == 12003080
        # assert resp.json_get("error.message") == "E12003080: invalid session type"                  
   
    @pytest.mark.skip(reason="手动测试")
    def test_api_OCRService_OCRIDCard(self, config_obj, OcrApi):
        """  检测识别图片中的身份证.
route prefix=ids internal_prefix=ids ... """
        image = None
        side = "FRONT"
        detect_quality = True
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 1.0,
            "encrypted_fields": ["idcard"],
        }  
        session_id = "SIC2RVeKji6PlILkPoNr2j2y0pC0vkMkpxbX"
        resp = OcrApi.OCRService_OCRIDCardPostApi(image=image, side=side, detect_quality=detect_quality, encrypt_info=encrypt_info, session_id=session_id)
        assert resp.status_code == 200
        
    @pytest.mark.skip(reason="手动测试")    
    def test_api_OCRService_OCRBankcard(self, config_obj, OcrApi):
        """  对图片中的文字进行模板检测识别.
route prefix=ids internal_prefix=... """
        image = None
        encrypt_info = None
        session_id = None
        resp = OcrApi.OCRService_OCRBankcardPostApi(image=image, encrypt_info=encrypt_info, session_id=session_id)
        assert resp.status_code == 200    
