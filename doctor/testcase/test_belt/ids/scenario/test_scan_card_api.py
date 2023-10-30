
import json
import pytest
import os
import uuid
from commonlib.log_utils import log
from commonlib import config
from pytest_check import check
from  commonlib.ids_scan_ws_client import IdsScanWebSocketClient
from commonlib.api_lib.AES_new import *
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
from commonlib.api_lib.base_api import BaseApi
from commonlib.config import ids_image_path
from commonlib.api_lib.validator import schema_validator, digit_number_validator, idc_verify

class TestOCRScanCardScenario(object):
    """ OCR scan card scenario test"""

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
        

    def create_session_ocr(self,session_type,OcrApi):
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": session_type,
            "uuid": uuid_str
        }        
        resp = OcrApi.OCRService_CreateSessionPostApi( session=session)
        assert resp.status_code == 200
        biz_tokens = []                                    
        biz_tokens.append(resp.json_get("biz_token"))
        session_id = resp.json_get("session_id")
        log().info(f"biz_token:{biz_tokens},session_id:{session_id}")
    
        return biz_tokens,session_id
    
    def create_session_ocr_idcard_quality_level(self,quality_level,OcrApi):
        uuid_str =str(uuid.uuid4())
        session = {
            "session_type": "IDCARD_SCAN",
            "uuid": uuid_str,
            "idcard_min_quality_level":quality_level
        }        
        resp = OcrApi.OCRService_CreateSessionPostApi(session=session)
        assert resp.status_code == 200
        biz_tokens = []                                    
        biz_tokens.append(resp.json_get("biz_token"))
        session_id = resp.json_get("session_id")
        log().info(f"biz_token:{biz_tokens},session_id:{session_id}")
    
        return biz_tokens,session_id

    def api_OCRService_OCRIDCard(self, session_id,side, OcrApi):

        side = side
        detect_quality = True
        encrypt_info = None
        session_id = session_id
        resp = OcrApi.OCRService_OCRIDCardPostApi(image=None, side=side, detect_quality=detect_quality, encrypt_info=encrypt_info, session_id=session_id)
        assert resp.status_code == 200
        if side == "FRONT":
            required_list=["side","name","sex","nation","birth_date","address","number","image"]   
        else:
            required_list=["side","issue_date","expiry_date","image"] 
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="idcard"), "Json_schema验证失败"
        resp.json_get("idcard.side")== side
        
    
    def api_OCRService_OCRIDCard_CBC(self, sk,session_id,side, OcrApi):

        side = side
        detect_quality = True
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 1.0,
            "encrypted_fields": ["idcard"],
        }  
        session_id = session_id
        resp = OcrApi.OCRService_OCRIDCardPostApi(image=None, side=side, detect_quality=detect_quality, encrypt_info=encrypt_info, session_id=session_id)
        cryptor = AESCipher(sk.encode())
        encrypted_data = resp.json_get("encrypt_info.data")
        idcard_result  = cryptor.decrypt(encrypted_data)
        log().info(f"data:{idcard_result}")
        assert resp.status_code == 200
        data_json=json.loads(idcard_result).get("idcard")
        if side == "FRONT":
            required_list=["side","name","sex","nation","birth_date","address","number","image"]   
        else:
            required_list=["side","issue_date","expiry_date","image"] 
        ocrIDCard_schema = resp.get_definitions_by_name("ocrIDCard")  # 根据名字获取definitions
        del ocrIDCard_schema["properties"]["side"]  
        del ocrIDCard_schema["properties"]["idcard_source"]  
        ocrIDCard_schema.update({"required": required_list})
        assert schema_validator(data_json, ocrIDCard_schema)  
        
    def api_OCRService_OCRIDCard_GCM(self, sk,session_id,side, OcrApi):

        side = side
        detect_quality = True
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 1.0,
            "encrypted_fields": ["idcard"],
        }  
        session_id = session_id
        resp = OcrApi.OCRService_OCRIDCardPostApi(image=None, side=side, detect_quality=detect_quality, encrypt_info=encrypt_info, session_id=session_id)
        cryptor = AESGCMCryptor(sk)
        encrypted_data = resp.json_get("encrypt_info.data")
        idcard_result  = cryptor.decrypt(encrypted_data)
        log().info(f"data:{idcard_result}")
        assert resp.status_code == 200
        data_json=json.loads(idcard_result).get("idcard")
        if side == "FRONT":
            required_list=["side","name","sex","nation","birth_date","address","number","image"]   
        else:
            required_list=["side","issue_date","expiry_date","image"] 
        ocrIDCard_schema = resp.get_definitions_by_name("ocrIDCard")  # 根据名字获取definitions
        del ocrIDCard_schema["properties"]["side"]  
        del ocrIDCard_schema["properties"]["idcard_source"]  
        ocrIDCard_schema.update({"required": required_list})
        assert schema_validator(data_json, ocrIDCard_schema)

        
          
    def api_OCRService_OCRBankcard(self, session_id, OcrApi):

        encrypt_info = None
        session_id = session_id
        resp = OcrApi.OCRService_OCRBankcardPostApi(image=None, encrypt_info=encrypt_info, session_id=session_id)
        assert resp.status_code == 200    
        
        
    def test_scenario_IDCARD_SCAN_FRONT(self,config_obj,user_info,OcrApi):
        """  身份证单面扫描ocr-正面 """

        self.client = IdsScanWebSocketClient()
        self.ak = user_info.ak
        self.sk = user_info.sk
        host = config_obj.EnvInfo.BeltCloud.EdgeService.split("//")[1]
        log().info(f"host:{host}")
        tokens,session_id = self.create_session_ocr("IDCARD_SCAN",OcrApi)
        front_image = "idcard_normal1.jpg"
        front_roi={'left': 0, 'top': 0, 'width': 1050, 'height': 670}
        param_dict={
                    "tokens":tokens,
                    "session_id":session_id,
                    "ak":self.ak,
                    "sk":self.sk,
                    "OcrApi":OcrApi,
                    "label":"FRONT",
                    "image":front_image,
                    "roi":front_roi,
                    "host":host

                }
        self.client.start(**param_dict)
        result =  self.client.getWSresult()
        assert result.get('detect_result').get('label') == 1
        assert result.get('detect_result').get('err_msg') == 'ok'
        self.api_OCRService_OCRIDCard(session_id,"FRONT",OcrApi)  
        # self.api_OCRService_OCRIDCard_GCM(self.sk,session_id,"FRONT",OcrApi)
        # self.api_OCRService_OCRIDCard_CBC(self.sk,session_id,"FRONT",OcrApi)
        
    def test_scenario_IDCARD_SCAN_BACK(self,config_obj,user_info,OcrApi):
        """  身份证单面扫描ocr-反面 """

        self.client = IdsScanWebSocketClient()
        self.ak = user_info.ak
        self.sk = user_info.sk
        host = config_obj.EnvInfo.BeltCloud.EdgeService.split("//")[1]
        log().info(f"host:{host}")
        tokens,session_id = self.create_session_ocr("IDCARD_SCAN",OcrApi)
        back_image = "idcard_normal2.jpg"
        back_roi={'left': 0, 'top': 0, 'width': 550, 'height': 345}  
        param_dict={
                    "tokens":tokens,
                    "session_id":session_id,
                    "ak":self.ak,
                    "sk":self.sk,
                    "OcrApi":OcrApi,
                    "label":"BACK",
                    "image":back_image,
                    "roi":back_roi,
                    "host":host

                }
        self.client.start(**param_dict)
        result =  self.client.getWSresult()
        assert result.get('detect_result').get('label') == 2
        assert result.get('detect_result').get('err_msg') == 'ok'
        self.api_OCRService_OCRIDCard(session_id,"BACK",OcrApi)  
        #self.api_OCRService_OCRIDCard_GCM(self.sk,session_id,"BACK",OcrApi)
        #self.api_OCRService_OCRIDCard_CBC(self.sk,session_id,"BACK",OcrApi)   
       
    def test_scenario_IDCARD_SCAN_quality_normal(self,config_obj,user_info,OcrApi):
        """  身份证单面扫描ocr-质量等级-HIGH-blur """

        self.client = IdsScanWebSocketClient()
        self.ak = user_info.ak
        self.sk = user_info.sk
        host = config_obj.EnvInfo.BeltCloud.EdgeService.split("//")[1]
        log().info(f"host:{host}")
        tokens,session_id = self.create_session_ocr_idcard_quality_level("HIGH",OcrApi)
        front_image = "idcard_blur1.jpg"
        front_roi={'left': 0, 'top': 0, 'width': 1050, 'height': 670}
        param_dict={
                    "tokens":tokens,
                    "session_id":session_id,
                    "ak":self.ak,
                    "sk":self.sk,
                    "OcrApi":OcrApi,
                    "label":"FRONT",
                    "image":front_image,
                    "roi":front_roi,
                    "host":host

                }
        self.client.start(**param_dict)
        result =  self.client.getWSresult()
        log().info(f"result:{result}")
        assert result.get('detect_result').get('err_code') == 214
        assert result.get('detect_result').get('err_msg') == 'idcard too blur'
        # self.api_OCRService_OCRIDCard(session_id,"FRONT",OcrApi)  