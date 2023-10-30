 # -*- coding: utf-8 -*-

import json
import pytest
import os
import uuid
from commonlib.log_utils import log
from commonlib import config
from pytest_check import check
from  commonlib.ids_ws_client import IdsWebSocketClient
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
from commonlib.api_lib.base_api import BaseApi
from commonlib.config import ids_image_path

@pytest.mark.Regression
@pytest.mark.P0
class TestInteracitveLivenss(object):
    """ Identity interactive liveness scenario test"""
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
        
    def create_session(self,actions,IdentityApi):
        uuid_str =str(uuid.uuid4())
        session = {
                "session_type": "LIVENESS",
                "uuid": uuid_str,
                "candidate_actions": actions,
                "action_number": len(actions),
                "pick_images_by_quality_number": 1,
                "pick_images_per_action_number": 1
    
        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        biz_tokens = []                                    
        biz_tokens.append(resp.json_get("biz_token"))
        session_id = resp.json_get("session_id")
        verification_url = resp.json_get("session_id")
        log().info(f"biz_token:{biz_tokens},session_id:{verification_url}")
    
        return biz_tokens,session_id
    
    def create_session_H5(self,actions,IdentityApi):
        uuid_str =str(uuid.uuid4())
        session = {
                "session_type": "H5_LIVENESS",
                "uuid": uuid_str,
                "candidate_actions": actions,
                "action_number": len(actions),
                "pick_images_by_quality_number": 1,
                "pick_images_per_action_number": 1,
                "h5_config": {
                "redirect_url": "https://baidu.com",
                "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                "page_title": "liveness"
            },
            "extra_info": "string"
    
        }
        
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        biz_tokens = []                                    
        biz_tokens.append(resp.json_get("biz_token"))
        session_id = resp.json_get("session_id")
        log().info(f"biz_token:{biz_tokens},session_id:{session_id}")
        return biz_tokens,session_id
    
    def create_session_H5_identity(self,actions,IdentityApi):
        uuid_str =str(uuid.uuid4())
        session = {
                "session_type": "IDENTITY_VERIFICATION",
                "uuid": uuid_str,
                "candidate_actions": actions,
                "action_number": len(actions),
                "pick_images_by_quality_number": 1,
                "pick_images_per_action_number": 1,
             "h5_config": {
                "redirect_url": "https://baidu.com"
            },
            "id_verification": {
            "name": "金阳",
            "idcard_number": "11010219781027232X",
            "expiry_date": ""
            }
        }
        
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        biz_tokens = []                                    
        biz_tokens.append(resp.json_get("biz_token"))
        session_id = resp.json_get("session_id")
        log().info(f"biz_token:{biz_tokens},session_id:{session_id}")
        return biz_tokens,session_id
    
    def create_session_H5_identity_withocr(self,actions,IdentityApi):
        uuid_str =str(uuid.uuid4())
        session = {
                "session_type": "IDENTITY_VERIFICATION",
                "uuid": uuid_str,
                "candidate_actions": actions,
                "action_number": len(actions),
                "pick_images_by_quality_number": 1,
                "pick_images_per_action_number": 1,
             "h5_config": {
                "redirect_url": "https://baidu.com"
            },
            "id_verification":{"certificate_types":[
                "IDCARD"]}
        }
        
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        biz_tokens = []                                    
        biz_tokens.append(resp.json_get("biz_token"))
        session_id = resp.json_get("session_id")
        log().info(f"biz_token:{biz_tokens},session_id:{session_id}")
        return biz_tokens,session_id

        
    def h5_ocr_idcard(self,token,name,id_card_number,OcrApi):
        
        front_image = BaseApi.imageToBase64(os.path.join(ids_image_path,"H5_front.jpg"))
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
        assert resp.status_code == 200
        encrypted_data = resp.json_get("encrypt_info.data")
        idcard_info  = cryptor.decrypt(encrypted_data)
        idcard_json = json.loads(idcard_info)
        # assert idcard_json["idcard"]["name"] == name
        # assert idcard_json["idcard"]["number"] == id_card_number  
        
    def h5_update_idcard(self,token,name,id_card_number,IdentityApi):
        jstr = {"name":name,"idcard_number":id_card_number}
                #用biztoken的内部接口加密key非sk
        key = token.split(".")[-1][:32]
        cryptor = AESGCMCryptor(key)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
                        "algorithm": "AES_256_GCM",
                        "data": cypher,
                        "encrypted_fields": ["name","idcard_number"]
                    }
        resp = IdentityApi.IdentityService_H5UpdateIDCardPostApi(loginToken=token,encrypt_info=encrypt_info)
        assert resp.status_code == 200  
        
    def get_result_liveness(self,session_id,IdentityApi):
        session_id = session_id
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200   
        is_liveness = resp.json_get("session_result.is_liveness")
        liveness_score = resp.json_get("session_result.liveness_score") 
        quality_image = resp.json_get("session_result.quality_images.0.image")
        log().info(f"is_liveness:{is_liveness},liveness_score:{liveness_score}")   
        with check: assert is_liveness
        with check: assert liveness_score > 0.5
        return quality_image
    
    def get_result_liveness_encrypted(self,session_id,IdentityApi):
        """  获取GCM加密的身份核验检测会话的最终结果"""
        session_id = session_id
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 1.0,
            "encrypted_fields": [""],
        }  
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200    
        
        cryptor = AESGCMCryptor(self.sk)
        encrypted_data = resp.json_get("encrypt_info.data")
        session_result  = json.loads(cryptor.decrypt(encrypted_data) )
        is_liveness = session_result["session_result"]["is_liveness"]
        liveness_score = session_result["session_result"]["liveness_score"] 
        quality_image = session_result["session_result"]["quality_images"][0]["image"]
        log().info(f"is_liveness:{is_liveness},liveness_score:{liveness_score}")   
        with check: assert is_liveness
        with check: assert liveness_score > 0.5
        return quality_image
    
        
    def get_result_identity_encrypted(self, session_id, IdentityApi,expect_result):

        session_id = session_id
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 1.0,
            "encrypted_fields": [""],
        }  
        resp = IdentityApi.IdentityService_GetSessionVerificationResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200 
          
        cryptor = AESGCMCryptor(self.sk)
        encrypted_data = resp.json_get("encrypt_info.data")
        session_result  = json.loads(cryptor.decrypt(encrypted_data) )
    
        is_liveness = session_result["session_result"]["is_liveness"]
        liveness_score = session_result["session_result"]["liveness_score"]
        face_score = session_result["session_result"]["face_score"]
        verify_result = session_result["session_result"]["verify_result"]  
        quality_images =  session_result["session_result"]["quality_images"]  
        
        log().info(f"is_liveness:{is_liveness},liveness_score:{liveness_score},verify_result:{verify_result},face_score:{face_score}")   
        with check: assert is_liveness
        with check: assert liveness_score > 0.5 
        with check: assert verify_result == expect_result
        with check: assert len(quality_images) == 1
        with check: assert face_score
        
    def get_result_identity(self, session_id, IdentityApi,expect_result):
        session_id = session_id
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionVerificationResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200    
        is_liveness = resp.json_get("session_result.is_liveness")
        liveness_score = resp.json_get("session_result.liveness_score") 
        face_score = resp.json_get("session_result.face_score") 
        verify_result = resp.json_get("session_result.verify_result")    
        log().info(f"is_liveness:{is_liveness},liveness_score:{liveness_score}")   
        with check: assert is_liveness
        with check: assert liveness_score > 0.5 
        with check: assert verify_result == expect_result
        with check: assert len(resp.json_get("session_result.quality_images")) == 1
        if verify_result!="INVALID_IDCARD_INFO":
            assert face_score
      
    def test_scenario_interactive_liveness(self,config_obj,user_info,IdentityApi):
        """  sdk金融活体检测流程 """

        
        self.ak = user_info.ak
        self.sk = user_info.sk
        host = config_obj.EnvInfo.BeltCloud.EdgeService.split("//")[1]
        self.client = IdsWebSocketClient(host)
        log().info(f"host:{host}")
        # actions = ["BLINK_EYES", "OPEN_MOUTH", "SHAKE_HEAD", "NOD_HEAD"]
        meta_file = os.path.join(config.ids_image_path, "interactive_liveness/interactiveLiveness_meta_positive_20230814165501.txt")
        #meta_file = "/home/SENSETIME/zhangrui2/Projects/tmp/interactiveLiveness_meta_positive_20230327154938.txt"
        with open(meta_file,"r",encoding="utf-8") as f:
            for line in f.readlines():
                print(line)
                data_json = json.loads(line)
                actions = []
                action_type_none_images = []
                blink_eyes_images=[]
                open_mouth_images = []
                shake_head_images = []
                nod_head_images = []
                colorful_images = []
                # log().info(data_json)

                if "InteractiveLiveness_nod_head" in data_json:
                    actions.append("NOD_HEAD")
                    nod_head_images = data_json["InteractiveLiveness_nod_head"]
                if "InteractiveLiveness_blink_eyes" in data_json:    
                    actions.append("BLINK_EYES")
                    blink_eyes_images = data_json["InteractiveLiveness_blink_eyes"]
                if "InteractiveLiveness_open_mouth"  in data_json:
                    actions.append("OPEN_MOUTH")
                    open_mouth_images = data_json["InteractiveLiveness_open_mouth"]
                if "InteractiveLiveness_shake_head"  in data_json:
                    actions.append("SHAKE_HEAD") 
                    shake_head_images = data_json["InteractiveLiveness_shake_head"]
                if "InteractiveLiveness_colorful" in data_json:
                    colorful_images = data_json["InteractiveLiveness_colorful"]
                if "InteractiveLiveness_detect" in data_json:
                    action_type_none_images =  data_json["InteractiveLiveness_detect"]  
                    
                detect_max_index =  data_json["InteractiveLiveness_detect_maxIndex"]     
                # tokens,session_id = self.get_token(actions)
                tokens,session_id = self.create_session(actions,IdentityApi)
                param_dict={
                    "tokens":tokens,
                    "session_id":session_id,
                    "ak":self.ak,
                    "sk":self.sk,
                    "action_type_none_images":action_type_none_images,
                    "blink_eyes_images":blink_eyes_images,
                    "open_mouth_images":open_mouth_images,
                    "shake_head_images":shake_head_images,
                    "nod_head_images":nod_head_images,
                    "colorful_images":colorful_images,
                    "detect_max_index":detect_max_index,
                    "IdentityApi":IdentityApi,
                    "host":host

                }
                self.client.start(**param_dict)
                self.get_result_liveness(session_id,IdentityApi)
    @pytest.mark.Paid            
    @pytest.mark.parametrize("datafile",[
        "interactiveLiveness_HLI2TyJ9qGftInhc6qBLpGvgBXsKFTMk9Yaj.json","interactiveLiveness_HLI2UHniAz7LDHW90tNviN6IIUxjxuMk9Yaj.json"],ids=["FACE_UNMATCH","MATCH"])
    def test_scenario_interactive_liveness_H5(self,config_obj,user_info,IdentityApi,datafile):
        """  H5金融活体检测+三要素身份核验流程 """

        
        self.ak = user_info.ak
        self.sk = user_info.sk
        host = config_obj.EnvInfo.BeltCloud.EdgeService.split("//")[1]
        self.client = IdsWebSocketClient(host)
        log().info(f"host:{host}")
        # meta_file = os.path.join(config.ids_image_path, "interactive_liveness/interactiveLiveness_meta_positive_20230413160952.txt")
        meta_file = os.path.join(config.ids_image_path,"interactive_liveness",datafile)
        log().info(f"meta_file:{meta_file}")
        with open(meta_file,"r",encoding="utf-8") as f:
            #for line in f.readlines():
                data_json = json.loads(f.read())
                
                actions = []
                action_type_none_images = []
                blink_eyes_images=[]
                open_mouth_images = []
                shake_head_images = []
                nod_head_images = []
                colorful_images = []
                # log().info(data_json)

                if "InteractiveLiveness_nod_head" in data_json:
                    actions.append("NOD_HEAD")
                    nod_head_images = data_json["InteractiveLiveness_nod_head"]
                if "InteractiveLiveness_blink_eyes" in data_json:    
                    actions.append("BLINK_EYES")
                    blink_eyes_images = data_json["InteractiveLiveness_blink_eyes"]
                if "InteractiveLiveness_open_mouth"  in data_json:
                    actions.append("OPEN_MOUTH")
                    open_mouth_images = data_json["InteractiveLiveness_open_mouth"]
                if "InteractiveLiveness_shake_head"  in data_json:
                    actions.append("SHAKE_HEAD") 
                    shake_head_images = data_json["InteractiveLiveness_shake_head"]
                if "InteractiveLiveness_colorful" in data_json:
                    colorful_images = data_json["InteractiveLiveness_colorful"]
                if "InteractiveLiveness_detect" in data_json:
                    action_type_none_images =  data_json["InteractiveLiveness_detect"]  
                    
                detect_max_index =  data_json["InteractiveLiveness_detect_maxIndex"]     
                name = data_json["name"]
                id_card_number =  data_json["id_card_number"]
                expect_result = data_json["verify_result"]

                tokens,session_id = self.create_session_H5(actions,IdentityApi)
                param_dict={
                    "tokens":tokens,
                    "session_id":session_id,
                    "ak":self.ak,
                    "sk":self.sk,
                    "action_type_none_images":action_type_none_images,
                    "blink_eyes_images":blink_eyes_images,
                    "open_mouth_images":open_mouth_images,
                    "shake_head_images":shake_head_images,
                    "nod_head_images":nod_head_images,
                    "colorful_images":colorful_images,
                    "detect_max_index":detect_max_index,
                    "IdentityApi":IdentityApi,
                    "host":host

                }
                self.client.start(**param_dict)
                quality_image = self.get_result_liveness(session_id,IdentityApi)
                
                resp = IdentityApi.verifyIDCardFace(name, id_card_number, image=quality_image)
                assert resp.status_code == 200
                assert resp.json_get("verify_result") == expect_result

    @pytest.mark.Paid            
    @pytest.mark.parametrize("datafile",["interactiveLiveness_HLI2TyJ9qGftInhc6qBLpGvgBXsKFTMk9Yaj.json","interactiveLiveness_HLI2UHniAz7LDHW90tNviN6IIUxjxuMk9Yaj.json","interactiveLiveness_HLI2UHniAz7LDHW90tNviN6IIUxjxuMk9Yaj_invalid_name.json",
        "interactiveLiveness_HLI2UHniAz7LDHW90tNviN6IIUxjxuMk9Yaj_invalid_number.json"],ids=["FACE_UNMATCH","MATCH","INVALID_IDCARD_INFO_name","INVALID_IDCARD_INFO_number"])
    def test_scenario_identity_interactive_liveness_H5(self,config_obj,user_info,IdentityApi,OcrApi,datafile):
        """  H5身份核验检测全流程(含H5ocr) """

        
        self.ak = user_info.ak
        self.sk = user_info.sk
        host = config_obj.EnvInfo.BeltCloud.EdgeService.split("//")[1]
        self.client = IdsWebSocketClient(host)
        log().info(f"host:{host}")
        meta_file = os.path.join(config.ids_image_path,"interactive_liveness",datafile)
        # meta_file = os.path.join(config.ids_image_path, "interactive_liveness/interactiveLiveness_meta_positive_20230413160952.txt")
        with open(meta_file,"r",encoding="utf-8") as f:
           # for line in f.readlines():
                
                data_json = json.loads(f.read())
                actions = []
                action_type_none_images = []
                blink_eyes_images=[]
                open_mouth_images = []
                shake_head_images = []
                nod_head_images = []
                colorful_images = []
                # log().info(data_json)

                if "InteractiveLiveness_nod_head" in data_json:
                    actions.append("NOD_HEAD")
                    nod_head_images = data_json["InteractiveLiveness_nod_head"]
                if "InteractiveLiveness_blink_eyes" in data_json:    
                    actions.append("BLINK_EYES")
                    blink_eyes_images = data_json["InteractiveLiveness_blink_eyes"]
                if "InteractiveLiveness_open_mouth"  in data_json:
                    actions.append("OPEN_MOUTH")
                    open_mouth_images = data_json["InteractiveLiveness_open_mouth"]
                if "InteractiveLiveness_shake_head"  in data_json:
                    actions.append("SHAKE_HEAD") 
                    shake_head_images = data_json["InteractiveLiveness_shake_head"]
                if "InteractiveLiveness_colorful" in data_json:
                    colorful_images = data_json["InteractiveLiveness_colorful"]
                if "InteractiveLiveness_detect" in data_json:
                    action_type_none_images =  data_json["InteractiveLiveness_detect"]  
                    
                detect_max_index =  data_json["InteractiveLiveness_detect_maxIndex"]     
                name = data_json["name"]
                id_card_number =  data_json["id_card_number"]
                expect_result = data_json["verify_result"]
                
                tokens,session_id = self.create_session_H5_identity_withocr(actions,IdentityApi)
                #H5OCRIDCard
                self.h5_ocr_idcard(tokens[0],name,id_card_number,OcrApi)
                #H5UpdateIDCard
                self.h5_update_idcard(tokens[0],name,id_card_number,IdentityApi)
                
                param_dict={
                    "tokens":tokens,
                    "session_id":session_id,
                    "ak":self.ak,
                    "sk":self.sk,
                    "action_type_none_images":action_type_none_images,
                    "blink_eyes_images":blink_eyes_images,
                    "open_mouth_images":open_mouth_images,
                    "shake_head_images":shake_head_images,
                    "nod_head_images":nod_head_images,
                    "colorful_images":colorful_images,
                    "detect_max_index":detect_max_index,
                    "IdentityApi":IdentityApi,
                    "host":host

                }
                self.client.start(**param_dict)
                self.get_result_identity(session_id,IdentityApi,expect_result)
                