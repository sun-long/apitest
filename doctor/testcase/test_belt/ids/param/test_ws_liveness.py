import pytest
import inspect
import uuid
import time
import os
import ssl
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
from commonlib import  config
from websocket import create_connection
from websocket import  ABNF
from protobuf_to_dict import protobuf_to_dict
from commonlib.pb import ids_ws_service_pb2

import urllib3
urllib3.disable_warnings()

@pytest.mark.P2
@pytest.mark.Regression
class TestWSLiveness:
    """ Interactive Liveness ws 错误码测试"""

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
        
    def get_file_bytes(self,file_name):
        this = inspect.getfile(inspect.currentframe())
        # file_path = os.path.join(config.image_path, "go_image/ids_ws_face", file_name)
        with open(file_name, 'rb') as f:
            bytes = f.read()
            return bytes      
     
    def get_msg_content(self,message):
        server_message = ids_ws_service_pb2.ServerMessage()
        server_message.ParseFromString(message)
        msg_id = server_message.msg_id
        message_type = server_message.message_type
        action_type = server_message.collect_request.action_type
        select_policy = server_message.collect_request.frame_config.select_policy
        color_configs = server_message.collect_request.color_configs
        # err_code = server_message.detect_result.err_code
        max_frame_count = server_message.collect_request.frame_config.max_frame_count
        d = protobuf_to_dict(server_message) 
        log().info(f"get message:{d}")
        return msg_id,max_frame_count,action_type,d
    def send_msg(self,msg_id,max_frame_count,action_type,imagefile):
        tmsp = ids_ws_service_pb2.Timestamp()
        tmsp.seconds = int(time.time())
        nanos = time.time_ns()
        str_nanos = str(nanos)
        split_nanos = str_nanos[10:]
        tmsp.nanos = int(split_nanos)
        
        cli_msg = ids_ws_service_pb2.ClientMessage()
        cli_msg.server_msg_id = msg_id
        cli_msg.message_type = ids_ws_service_pb2.FRAME_MESSAGE
        cli_msg.frame_message.timestamp.seconds = tmsp.seconds
        cli_msg.frame_message.timestamp.nanos = tmsp.nanos
        
        init_count = 5
        frame_count = max_frame_count - 5
        if action_type not in [1,2,3,4]:
            for i in range(init_count+frame_count):
                cli_msg.frame_message.image = self.get_file_bytes(os.path.join(config.image_path, "go_image/ids_ws_face", imagefile))
                self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
        else:
            for i in range(init_count+frame_count):
                cli_msg.frame_message.image = self.get_file_bytes(os.path.join(config.image_path, "go_image/ids_ws_face", imagefile))
                self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)    
                
        log().info(f"发送成功!")
        
    
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
    
    @pytest.mark.parametrize("imagefile,expected_err_code,expected_err_msg",[
        ("../partbody.jpg",101,"no face detected"),
        ("../twoface.jpg",102,"2 faces detected"),
        ("../noface.jpg",104,"height[64/628] less than min ratio[0.2]"),
        ("w0_eye_occlusion.jpg",106,"left_eye occlusion"),
        ("w0_nose_occlusion.jpg",106,"nose occlusion"),
        ("w4.jpg",107,"face down")
    ])
    def test_ws_error(self,imagefile,expected_err_code,expected_err_msg,config_obj,IdentityApi):  
        """ 异常：交互活体检测异常case """
        actions = ["NOD_HEAD"]
        tokens,session_id = self.create_session_H5_identity(actions,IdentityApi)
        host = config_obj.EnvInfo.BeltCloud.EdgeService.split("//")[1] 
        wss_url = f'wss://{host}/face?action=InteractiveLiveness&version=v1'
        sslopt ={"cert_reqs": ssl.CERT_NONE,"check_hostname": False}
        self.ws = create_connection(wss_url,sslopt=sslopt,subprotocols=tokens)
        message = self.ws.recv()
        msg_id,max_frame_count,action_type,content = self.get_msg_content(message)
        self.send_msg(msg_id,max_frame_count,action_type,imagefile)
        
        while True:
          message = self.ws.recv()
          if  isinstance(message, bytes)  and len(message) > 2 :
            break
        _,_,_,content = self.get_msg_content(message)
      
        err_code =  content["detect_result"]["err_code"]
        err_msg =  content["detect_result"]["err_msg"]
        log().info(f"err_code:{err_code},err_msg:{err_msg}")
        assert err_code == expected_err_code
        assert err_msg == expected_err_msg
        self.ws.close()
        
    @pytest.mark.skip(reason = "不能检测出来")
    @pytest.mark.parametrize("imagefile,expected_err_code,expected_err_msg",[
        ("w0_mouth_occlusion.jpg",106,"mouth occlusion"),
        ("w0_eye_occlusion_1.jpg",106,"left_eye occlusion"),
    ])
    def test_ws_error_2(self,imagefile,expected_err_code,expected_err_msg,config_obj,IdentityApi):  
        """ 异常：交互活体检测异常case """
        actions = ["NOD_HEAD"]
        tokens,session_id = self.create_session_H5_identity(actions,IdentityApi)
        host = config_obj.EnvInfo.BeltCloud.EdgeService.split("//")[1] 
        wss_url = f'wss://{host}/face?action=InteractiveLiveness&version=v1'
        sslopt ={"cert_reqs": ssl.CERT_NONE,"check_hostname": False}
        self.ws = create_connection(wss_url,sslopt=sslopt,subprotocols=tokens)
        message = self.ws.recv()
        msg_id,max_frame_count,action_type,content = self.get_msg_content(message)
        self.send_msg(msg_id,max_frame_count,action_type,imagefile)
        
        while True:
          message = self.ws.recv()
          if  isinstance(message, bytes)  and len(message) > 2 :
            break
        _,_,_,content = self.get_msg_content(message)
      
        err_code =  content["detect_result"]["err_code"]
        err_msg =  content["detect_result"]["err_msg"]
        log().info(f"err_code:{err_code},err_msg:{err_msg}")
        assert err_code == expected_err_code
        assert err_msg == expected_err_msg
        self.ws.close()
         
    @pytest.mark.skip(reason = "不稳定")    
    def test_ws_action_timeout_4(self,config_obj,IdentityApi):  
        """ 异常：交互活体检测动作超时 """
        actions = ["NOD_HEAD"]
        action_type_none_image = 'w6.jpg'
        tokens,session_id = self.create_session_H5_identity(actions,IdentityApi)
        host = config_obj.EnvInfo.BeltCloud.EdgeService.split("//")[1] 
        wss_url = f'wss://{host}/face?action=InteractiveLiveness&version=v1'
        sslopt ={"cert_reqs": ssl.CERT_NONE,"check_hostname": False}
        self.ws = create_connection(wss_url,sslopt=sslopt,subprotocols=tokens)
        message = self.ws.recv()
        msg_id,max_frame_count,action_type,content = self.get_msg_content(message)
        self.send_msg(msg_id,max_frame_count,action_type,action_type_none_image)
        
        message = self.ws.recv()
        msg_id,max_frame_count,action_type,content = self.get_msg_content(message)
        self.send_msg(msg_id,max_frame_count,action_type,action_type_none_image)
        
        while True:
          message = self.ws.recv()
          if  isinstance(message, bytes)  and len(message) > 2 :
            break
        _,_,_,content = self.get_msg_content(message)
      
        err_code =  content["detect_result"]["err_code"]
        err_msg =  content["detect_result"]["err_msg"]
        log().info(f"err_code:{err_code},err_msg:{err_msg}")
        assert err_code == 4
        assert err_msg == "NOD_HEAD action detect tried too many times"
        self.ws.close()
        
