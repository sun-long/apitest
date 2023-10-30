#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pytest
import datetime
import uuid
import os
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
from commonlib import  sign_utils
from commonlib.api_lib.base_api import BaseApi
from commonlib.config import ids_image_path,image_path


@pytest.mark.Regression
class TestIdentityH5Api(object):
    """ identity Api测试"""

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

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_without_session(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话,未传递session"""
        session = None
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session info provided"
        assert resp.json_get("error.details.0.reason") == 12003029
        assert resp.json_get("error.message") == "E12003029: no session info provided"    

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_without_h5_config(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话,未传递必填h5_config"""
        session = {

            "session_type": "IDENTITY_VERIFICATION"
        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no h5 config provided"
        assert resp.json_get("error.details.0.reason") == 12003082
        assert resp.json_get("error.message") == "E12003082: no h5 config provided"

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_without_redirect_url(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话,未传递必填redirect_url"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "h5_config": {
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
        }
        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no h5 config redirect url provided"
        assert resp.json_get("error.details.0.reason") == 12003085
        assert resp.json_get("error.message") == "E12003085: no h5 config redirect url provided"

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_invalid_session_type(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话,错误的session_type"""
        session = {
        
            "session_type": 5,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
        }
        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid session type"
        assert resp.json_get("error.details.0.reason") == 12003080
        assert resp.json_get("error.message") == "E12003080: invalid session type"

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_invalid_candidate_actions(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话,错误的candidate_actions"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
               6
            ],
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
        },
         "id_verification": {
                "certificate_type":"IDCARD"
            }
        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid candidate actions"
        assert resp.json_get("error.details.0.reason") == 12003031
        assert resp.json_get("error.message") == "E12003031: invalid candidate actions"   

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_invalid_action_number(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话,action_number>3"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "action_number": 4,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
        },
         "id_verification": {
                "certificate_type":"IDCARD"
            }
        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid action number"
        assert resp.json_get("error.details.0.reason") == 12003032
        assert resp.json_get("error.message") == "E12003032: invalid action number"  

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_invalid_quality_number(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话,质量留存数量>5"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "pick_images_by_quality_number": 6,
            "pick_images_per_action_number": 1,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
        },
         "id_verification": {
                "certificate_type":"IDCARD"
            }
        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid quality image number to pick"
        assert resp.json_get("error.details.0.reason") == 12003026
        assert resp.json_get("error.message") == "E12003026: invalid quality image number to pick" 
          
    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_invalid_aciont_number(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话,action留存数量>2"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "pick_images_by_quality_number": 5,
            "pick_images_per_action_number": 3,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
        },
         "id_verification": {
                "certificate_type":"IDCARD"
            }
        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid image number per action to pick"
        assert resp.json_get("error.details.0.reason") == 12003027
        assert resp.json_get("error.message") == "E12003027: invalid image number per action to pick"  

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_without_id_verification(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话,不检测ocr(id_verification未传递)"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
        }
        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no id verification provided"
        assert resp.json_get("error.details.0.reason") == 12003081
        assert resp.json_get("error.message") == "E12003081: no id verification provided"

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_without_name_cardno(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话，不检测ocr(name和idcard_number空串)"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
            "name": "",
            "idcard_number": "",
            "expiry_date": ""
            }

        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "id_verification.name and id_verification.idcard_number should be set when id_verification.certificate_types is empty"
        assert resp.json_get("error.details.0.reason") == 12003083
        assert resp.json_get("error.message") == "E12003083: id_verification.name and id_verification.idcard_number should be set when id_verification.certificate_types is empty"
    
    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_without_idcardinfo(self, config_obj, IdentityApi):
        """  异常：创建一个IDENTITY_VERIFICATION检测会话,不检测ocr(CERTIFICATE_TYPE_NONE,name和idcard_number未传递)"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "liveness"
            },
            "id_verification": {
                "certificate_type":"CERTIFICATE_TYPE_NONE"
            }

        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "id_verification.name and id_verification.idcard_number should be set when id_verification.certificate_types is empty"
        assert resp.json_get("error.details.0.reason") == 12003083
        assert resp.json_get("error.message") == "E12003083: id_verification.name and id_verification.idcard_number should be set when id_verification.certificate_types is empty"
   
    @pytest.mark.P2  
    def test_api_IdentityService_encrypted_CreateSession_expiried_date(self, config_obj, user_info,IdentityApi):
        """  异常：创建一个CBC加密IDENTITY_VERIFICATION检测会话,身份证过期校验 """
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "liveness"
            },
            "id_verification": {
                "certificate_type":"CERTIFICATE_TYPE_NONE",
                

            "name": "金阳",
            "idcard_number": "11010219781027232X",
            "expiry_date": yesterday 
            
            }

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
       
        resp = IdentityApi.IdentityService_CreateSessionPostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "id card expired"
        assert resp.json_get("error.details.0.reason") == 12003004
        assert resp.json_get("error.message") == "E12003004: id card expired"

    @pytest.mark.P1
    def test_api_IdentityService_encrypted_CreateSession_extra_info_too_long(self, config_obj, user_info,IdentityApi):
        """  异常：创建一个GCM加密IDENTITY_VERIFICATION检测会话,extra_info超长"""
   
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "liveness"
            },
            "id_verification": {
            "certificate_type":"CERTIFICATE_TYPE_NONE",
            "name": "金阳",
            "idcard_number": "11010219781027232X",
          
            
            },
            "extra_info": sign_utils.getUuid(1025)

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
        resp = IdentityApi.IdentityService_CreateSessionPostApi(encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "extra info size exceeded"
        assert resp.json_get("error.details.0.reason") == 12003033
        assert resp.json_get("error.message") == "E12003033: extra info size exceeded"

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_withoutocr_onlycolorful(self, config_obj, IdentityApi):
        """  正向：创建一个IDENTITY_VERIFICATION检测会话,不检测ocr,活体检测只有炫彩"""
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
            "name": "金阳",
            "idcard_number": "11010219781027232X",
            "expiry_date": today
            }

        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200")

    @pytest.mark.P1
    def test_api_IdentityService_CreateSession_withoutocr_onlyaction(self, config_obj, IdentityApi):
        """  正向：创建一个IDENTITY_VERIFICATION检测会话，不检测ocr，活体检测只有动作"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "disable_color_liveness":True,
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
            "name": "金阳",
            "idcard_number": "11010219781027232X",
            "expiry_date": "0000"
            }

        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200")

    @pytest.mark.P0
    def test_api_IdentityService_CreateEncryptSession_withoutocr_actions_colorful(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个CBC加密IDENTITY_VERIFICATION检测会话，不检测ocr(certificate_types未传递),活体检测动作+炫彩"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
            "name": "金阳",
            "idcard_number": "11010219781027232X",
            "expiry_date": "0000"
            }

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
        resp = IdentityApi.IdentityService_CreateSessionPostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200")
        biz_token  = resp.json_get("biz_token")
        session_id = resp.json_get("session_id")
        decode_token = sign_utils.decode_jwt_token(biz_token,user_info.sk)
        log().info(f"decode_token:{decode_token}")
        assert decode_token.get("iss") == user_info.ak
        assert decode_token.get("sid") == session_id
        assert decode_token.get("url") == ['H5GetSessionConfig', 'H5OCRIDCard', 'H5UpdateIDCard', 'InteractiveLiveness', 'ScanCard']
        
    

    @pytest.mark.P0
    def test_api_IdentityService_CreateEncryptSession_certificate_types_none_actions_colorful(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个GCM加密IDENTITY_VERIFICATION检测会话，不检测ocr(CERTIFICATE_TYPE_NONE),活体检测动作+炫彩"""
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
            "certificate_type":"CERTIFICATE_TYPE_NONE",         
            "name": "金阳",
            "idcard_number": "11010219781027232X",
            "expiry_date": today
            }

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
        resp = IdentityApi.IdentityService_CreateSessionPostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200")
        biz_token  = resp.json_get("biz_token")
        session_id = resp.json_get("session_id")
        decode_token = sign_utils.decode_jwt_token(biz_token,user_info.sk)
        log().info(f"decode_token:{decode_token}")
        assert decode_token.get("iss") == user_info.ak
        assert decode_token.get("sid") == session_id
        assert decode_token.get("url") == ['H5GetSessionConfig', 'H5OCRIDCard', 'H5UpdateIDCard', 'InteractiveLiveness', 'ScanCard']
        

    @pytest.mark.P1
    def test_api_IdentityService_CreateEncryptSession_withocrquality_actions_verifyIDcard(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个CBC加密IDENTITY_VERIFICATION检测会话验证，类型身份证ocr(身份证质量等级EXTREMELY_LOW),活体只有检测动作,"""
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "IDENTITY_VERIFICATION",
            "uuid": uuid_str,
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "disable_color_liveness":True,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
            "certificate_type":"IDCARD",     
            "min_quality_level":"EXTREMELY_LOW"    
            }
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
        resp = IdentityApi.IdentityService_CreateSessionPostApi(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200") 
        session_id  = resp.json_get("session_id")
        # 获取h5 config CBC加密
        jstr = {
            "session_id": session_id
        }
        cryptor = AESCipher(user_info.sk.encode())
        # cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["session"],
          
        }  
        resp = IdentityApi.IdentityService_H5GetSessionConfigPostApi(session_id = session_id,encrypt_info=encrypt_info)
        assert resp.status_code == 200
        encrypted_data = resp.json_get("encrypt_info.data")
        session_result  = cryptor.decrypt(encrypted_data)
        log().info(f"data:{session_result}")    
        assert json.loads(session_result)["session"]["id_verification"]["certificate_type"] == "IDCARD"  
        # assert resp.json_get("session.id_verification.certificate_type") == "IDCARD"  
        # 未完成检测获取结果
        resp = IdentityApi.IdentityService_GetSessionVerificationResultPostApi(session_id=session_id, encrypt_info=None)
        assert resp.status_code == 404
        assert resp.json_get("error.code") == 5
        assert resp.json_get("error.details.0.message") == "session result not ready"
        assert resp.json_get("error.details.0.reason") == 12005004
        assert resp.json_get("error.message") == "E12005004: session result not ready"        

    @pytest.mark.P1
    def test_api_IdentityService_CreateEncryptSession_withocrquality_colorful_verifyIDcard(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个GCM加密IDENTITY_VERIFICATION检测会话验证，类型身份证ocr(身份证质量等级NONE),活体只有炫彩"""
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "IDENTITY_VERIFICATION",
            "uuid": uuid_str,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
            "certificate_type":"IDCARD",     
            "min_quality_level":"EXTREMELY_LOW"    
            }
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
        resp = IdentityApi.IdentityService_CreateSessionPostApi(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200") 
        session_id  = resp.json_get("session_id")
        # 获取h5 config GCM加密,加密有问题先不加密了
        # jstr = {
        #     "session_id": session_id,
        # }
        # cypher = cryptor.encrypt(json.dumps(jstr))
        # encrypt_info = {
        #     "algorithm": "AES_256_GCM",
        #     "encrypted_fields": ["session_id"],
        #     "data": cypher
        # }  
        resp = IdentityApi.IdentityService_H5GetSessionConfigPostApi( session_id=session_id)
        assert resp.status_code == 200
        assert resp.json_get("session.id_verification.certificate_type") == "IDCARD"        

    @pytest.mark.P0
    def test_api_IdentityService_CreateSession_withocr_actions_colorful_verifyIDcard(self, config_obj, IdentityApi):
        """  正向：创建一个IDENTITY_VERIFICATION检测会话验证类型，身份证ocr(质量等级默认),活体检测动作+炫彩"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
            "certificate_type":"IDCARD",         
            }

        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200")  
        session_id  = resp.json_get("session_id")
        # 获取h5 config
        resp = IdentityApi.IdentityService_H5GetSessionConfigPostApi(session_id=session_id, encrypt_info=None)
        assert resp.status_code == 200
        assert resp.json_get("session.id_verification.certificate_type") == "IDCARD"

    @pytest.mark.P1
    def test_api_IdentityService_CreateEncryptSession_withocr_actions_colorful_verifyIDcard(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个CBC加密IDENTITY_VERIFICATION检测会话验证(质量等级HIGH)，类型身份证ocr,活体检测动作+炫彩"""
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "IDENTITY_VERIFICATION",
            "uuid": uuid_str,
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
            "certificate_type":"IDCARD",
            "min_quality_level":"HIGH"          
            }
          
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
        resp = IdentityApi.IdentityService_CreateSessionPostApi(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200") 
        session_id  = resp.json_get("session_id")
        # 获取h5 config
        resp = IdentityApi.IdentityService_H5GetSessionConfigPostApi(session_id=session_id, encrypt_info=None)
        assert resp.status_code == 200
        assert resp.json_get("session.id_verification.certificate_type") == "IDCARD"

    @pytest.mark.P1
    def test_api_IdentityService_CreateEncryptSession_withocrquality_actions_colorful_verifyIDcard(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个GCM加密IDENTITY_VERIFICATION检测会话验证，类型身份证ocr(身份证质量等级low),活体检测动作+炫彩,"""
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "IDENTITY_VERIFICATION",
            "uuid": uuid_str,
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "identity"
            },
            "id_verification": {
            "certificate_type":"IDCARD",     
            "min_quality_level":"LOW"    
            }
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
        resp = IdentityApi.IdentityService_CreateSessionPostApi(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200") 
        session_id  = resp.json_get("session_id")
        # 获取h5 config
        # jstr = {
        #     "session_id": session_id,
        # }
        # cypher = cryptor.encrypt(json.dumps(jstr))
        # encrypt_info = {
        #     "algorithm": "AES_256_GCM",
        #     "encrypted_fields": ["session_id"],
        #     "data": cypher
        # }  
        resp = IdentityApi.IdentityService_H5GetSessionConfigPostApi( session_id=session_id)
        assert resp.status_code == 200
        assert resp.json_get("session.id_verification.certificate_type") == "IDCARD"

    @pytest.mark.P1
    def test_api_h5_liveness_CreateEncryptSession_only_action(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个CBC加密H5_LIVENESS检测会话，活体检测只有动作"""
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "H5_LIVENESS",
            "uuid": uuid_str,
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "action_number": 2,
            "disable_color_liveness":True,
            "pick_images_by_quality_number": 1,
            "pick_images_per_action_number": 1,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "liveness"
            },
            "extra_info": "string"
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
        resp = IdentityApi.IdentityService_CreateSessionPostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200")  

    @pytest.mark.P1
    def test_api_h5_liveness_CreateEncryptSession_only_colorful(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个GCM加密H5_LIVENESS检测会话，活体检测只有炫彩"""
        session = {
            "session_type": "H5_LIVENESS",
            "pick_images_by_quality_number": 1,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "liveness"
            },
            "extra_info": "string"
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
        resp = IdentityApi.IdentityService_CreateSessionPostApi(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200")             

    @pytest.mark.P0
    def test_api_h5_liveness_CreateEncryptSession_actions_colorful(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个CBC加密H5_LIVENESS检测会话，活体检测动作+炫彩"""
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "H5_LIVENESS",
            "uuid": uuid_str,
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "action_number": 2,
            "pick_images_by_quality_number": 1,
            "pick_images_per_action_number": 1,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "liveness"
            },
            "extra_info": "string"
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
        resp = IdentityApi.IdentityService_CreateSessionPostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200") 
        biz_token  = resp.json_get("biz_token")
        session_id = resp.json_get("session_id")
        decode_token = sign_utils.decode_jwt_token(biz_token,user_info.sk)
        log().info(f"decode_token:{decode_token}")
        assert decode_token.get("iss") == user_info.ak
        assert decode_token.get("sid") == session_id
        assert decode_token.get("url") == ['H5GetSessionConfig', 'InteractiveLiveness']
        
        # 获取h5 config
        resp = IdentityApi.IdentityService_H5GetSessionConfigPostApi(session_id=session_id, encrypt_info=None)
        assert resp.status_code == 200
        assert resp.json_get("session.session_type") == "H5_LIVENESS"  
        
    @pytest.mark.P2
    def test_api_h5_liveness_CreateEncryptSession_save_process_video_invalid(self, config_obj,user_info, IdentityApi):
        """  异常：创建一个CBC加密H5_LIVENESS检测会话，save_process_video参数异常"""
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "H5_LIVENESS",
            "uuid": uuid_str,
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "action_number": 2,
            "pick_images_by_quality_number": 1,
            "pick_images_per_action_number": 1,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "liveness"
            },
            "extra_info": "string",
            "save_process_video":"key"
        }        
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=None)
        assert resp.status_code == 400    
        
    @pytest.mark.P1
    def test_api_h5_liveness_CreateEncryptSession_save_process_video_false(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个CBC加密H5_LIVENESS检测会话，不留存视频"""
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "H5_LIVENESS",
            "uuid": uuid_str,
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "action_number": 2,
            "pick_images_by_quality_number": 1,
            "pick_images_per_action_number": 1,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "liveness"
            },
            "extra_info": "string",
            "save_process_video":False
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
        resp = IdentityApi.IdentityService_CreateSessionPostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200") 
        session_id  = resp.json_get("session_id")
        # 获取h5 config
        resp = IdentityApi.IdentityService_H5GetSessionConfigPostApi(session_id=session_id, encrypt_info=None)
        assert resp.status_code == 200
        assert resp.json_get("session.session_type") == "H5_LIVENESS" 
        # 未完成检测获取结果
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=None)
        assert resp.status_code == 404
        assert resp.json_get("error.code") == 5
        assert resp.json_get("error.details.0.message") == "session result not ready"
        assert resp.json_get("error.details.0.reason") == 12005004
        assert resp.json_get("error.message") == "E12005004: session result not ready"   
        
    @pytest.mark.P1
    def test_api_h5_liveness_CreateEncryptSession_save_process_video_true(self, config_obj,user_info, IdentityApi):
        """  正向：创建一个CBC加密H5_LIVENESS检测会话，留存视频(实验特性)"""
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "H5_LIVENESS",
            "uuid": uuid_str,
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "action_number": 2,
            "pick_images_by_quality_number": 1,
            "pick_images_per_action_number": 1,
            "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "liveness"
            },
            "extra_info": "string",
            "save_process_video":True
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
        resp = IdentityApi.IdentityService_CreateSessionPostApi( encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.schema_validator(["biz_token", "session_id","verification_url"], response_type="200") 
        session_id  = resp.json_get("session_id")
        # 获取h5 config
        resp = IdentityApi.IdentityService_H5GetSessionConfigPostApi(session_id=session_id, encrypt_info=None)
        assert resp.status_code == 200
        assert resp.json_get("session.session_type") == "H5_LIVENESS"           

    @pytest.mark.P1
    def test_api_IdentityService_GetSessionLivenessResult_without_sessionId(self, config_obj, IdentityApi):
        """  异常：获取活体检测会话的最终结果,未传session_id"""
        session_id = None
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session id provided"
        assert resp.json_get("error.details.0.reason") == 12003028
        assert resp.json_get("error.message") == "E12003028: no session id provided"

    @pytest.mark.P1
    def test_api_IdentityService_GetSessionLivenessResult_expired_sessionId(self, config_obj, IdentityApi):
        """  异常：获取活体检测会话的最终结果,失效的session_id"""
        session_id = "HLI2NMsz6R0mmaRN8AX0AnJCVTl1a1"
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "session has expired"
        assert resp.json_get("error.details.0.reason") == 12003030
        assert resp.json_get("error.message") == "E12003030: session has expired"    

    @pytest.mark.P1
    def test_api_IdentityService_GetSessionVerificationResult_without_sessionId(self, config_obj, IdentityApi):
        """  异常：获取身份核验检测会话的最终结果，未传session_id"""
        session_id = None
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionVerificationResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session id provided"
        assert resp.json_get("error.details.0.reason") == 12003028
        assert resp.json_get("error.message") == "E12003028: no session id provided"

    @pytest.mark.P1
    def test_api_IdentityService_GetSessionVerificationResult_expired_sessionId(self, config_obj, IdentityApi):
        """  异常：获取身份核验检测会话的最终结果，失效的session_id"""
        session_id = "HID2NRndWZ6XE7q2Ve0mXLGcikj28R"
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionVerificationResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "session has expired"
        assert resp.json_get("error.details.0.reason") == 12003030
        assert resp.json_get("error.message") == "E12003030: session has expired"   

    @pytest.mark.skip(reason="手动执行，有时效性")
    def test_api_IdentityService_GetSessionLivenessResult_invalide_sessionId(self, config_obj, IdentityApi):
        """  异常：获取活体检测会话的最终结果,传入了identity类型的session_id"""
        session_id = "HID2Q8C6egrohE1vo2fXTcMM3MJKAiMkpxbX"
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid session id"
        assert resp.json_get("error.details.0.reason") == 12003084
        assert resp.json_get("error.message") == "E12003084: invalid session id"         

    @pytest.mark.skip(reason="手动执行，有时效性")
    def test_api_IdentityService_GetSessionVerificationResult_invalid_session_id(self, config_obj, IdentityApi):
        """  异常：获取身份核验检测会话的最终结果，传入了h5_liveness类型的session_id"""
        session_id = "HLI2Q8C7893xtnG0fYDiaAxBX8mnQFMkpxbX"
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionVerificationResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid session id"
        assert resp.json_get("error.details.0.reason") == 12003084
        assert resp.json_get("error.message") == "E12003084: invalid session id"      

    @pytest.mark.skip(reason="Liveness手动执行获取检测结果")
    def test_api_IdentityService_GetSessionLivenessResult(self, config_obj, IdentityApi):
        """  获取活体检测会话的最终结果"""
        session_id = "HLI2UKgiX0Q0ck7sVHZdbnLdudVPBRbmFpZH"
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200    

    @pytest.mark.skip(reason="Liveness手动执行返回加密response")
    def test_api_IdentityService_Encrypted_GetSessionLivenessResult(self, config_obj, IdentityApi,user_info):
        """  获取CBC加密活体检测会话的最终结果"""
        session_id = "HLI2UKgiX0Q0ck7sVHZdbnLdudVPBRbmFpZH"
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 1.0,
            "encrypted_fields": [""],
        }  
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200      
        cryptor = AESCipher(user_info.sk.encode())
        log().info(f"sk:{user_info.sk}")
        encrypted_data = resp.json_get("encrypt_info.data")
        session_result  = cryptor.decrypt(encrypted_data)
        log().info(f"data:{session_result}")  
    
    @pytest.mark.skip(reason="Liveness手动执行返回加密response")
    def test_api_IdentityService_Encrypted_GetSessionLivenessResult(self, config_obj, IdentityApi,user_info):
        """  获取GCM加密活体检测会话的最终结果"""
        session_id = "HLI2UKiQFl8xpH71rtRkMRBciD8Bk8bmFpZH"
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 1.0,
            "encrypted_fields": [""],
        }  
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200      
        cryptor = AESGCMCryptor(user_info.sk)
        log().info(f"sk:{user_info.sk}")
        encrypted_data = resp.json_get("encrypt_info.data")
        session_result  = json.loads(cryptor.decrypt(encrypted_data))
        log().info(f"data:{session_result}") 
        assert session_result["session_result"]["is_liveness"]
        assert session_result["session_result"]["liveness_score"]
        assert session_result["session_result"]["quality_images"]
        assert session_result["session_result"]["action_images"]

    @pytest.mark.skip(reason="Identity手动执行返回加密response")
    def test_api_IdentityService_Encrypted_GetSessionVerificationResult(self, config_obj,user_info, IdentityApi):
        """  获取CBC加密的身份核验检测会话的最终结果"""
        session_id = "HID2NgRIReeJYuGQ1GgSE8aVamNMYW"
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 1.0,
            "encrypted_fields": [""],
        }  
        resp = IdentityApi.IdentityService_GetSessionVerificationResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200    
        cryptor = AESCipher(user_info.sk.encode())
        log().info(f"sk:{user_info.sk}")
        encrypted_data = resp.json_get("encrypt_info.data")
        session_result  = json.loads(cryptor.decrypt(encrypted_data))
        log().info(f"data:{session_result}")
        assert session_result["session_result"]["is_liveness"]
        assert session_result["session_result"]["liveness_score"]
        assert session_result["session_result"]["quality_images"]
        assert session_result["session_result"]["action_images"]
        
    @pytest.mark.skip(reason="Identity手动执行返回加密response")
    def test_api_IdentityService_Encrypted_GetSessionVerificationResult(self, config_obj,user_info, IdentityApi):
        """  获取GCM加密的身份核验检测会话的最终结果"""
        session_id = "HID2Oid4TSWqLXKhRiE1zgEpqSuWBj"
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 1.0,
            "encrypted_fields": [""],
        }  
        resp = IdentityApi.IdentityService_GetSessionVerificationResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200    
        cryptor = AESGCMCryptor(user_info.sk)
        log().info(f"sk:{user_info.sk}")
        encrypted_data = resp.json_get("encrypt_info.data")
        session_result  = cryptor.decrypt(encrypted_data)
        log().info(f"data:{session_result}")    

    @pytest.mark.skip(reason="Identity手动执行返回检测结果")
    def test_api_IdentityService_GetSessionVerificationResult(self, config_obj, IdentityApi):
        """  获取身份核验检测会话的最终结果"""
        session_id = "HID2SlzyN6Dl7GbHX9l7J2sBqiWjlDMk1NTG"
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionVerificationResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200    