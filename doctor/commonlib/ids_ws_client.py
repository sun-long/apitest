
import inspect
from websocket import  WebSocketApp,ABNF
import websocket
from protobuf_to_dict import protobuf_to_dict
from commonlib.pb import ids_ws_service_pb2
import time
import os
import ssl
from commonlib.log_utils import log
from commonlib import config
import urllib3
urllib3.disable_warnings()


class IdsWebSocketClient(object):
        
    def __init__(self,host):
        self.ws= None
        self.session_id = None
        self.host = host        
        
    def start(self,**kwargs):
        log().info("Begin to connect to server")
        # self.host = kwargs["host"]
        self.wss_url = f'wss://{self.host}/face?action=InteractiveLiveness&version=v1'
        sslopt ={"cert_reqs": ssl.CERT_NONE,"check_hostname": False}
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(
            self.wss_url,
            subprotocols=kwargs["tokens"],
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.session_id = kwargs["session_id"]
        self.ak = kwargs["ak"]
        self.sk = kwargs["sk"] 
        self.action_type_none_images = kwargs["action_type_none_images"]
        self.blink_eyes_images = kwargs["blink_eyes_images"]
        self.open_mouth_images = kwargs["open_mouth_images"]
        self.shake_head_images = kwargs["shake_head_images"]
        self.nod_head_images= kwargs["nod_head_images"]
        self.colorful_images = kwargs["colorful_images"]
        self.detect_max_index = kwargs["detect_max_index"]
        self.IdentityApi = kwargs["IdentityApi"]

        log().info(f"action_type_none_images{self.action_type_none_images}")
        log().info(f"blink_eyes_images{self.blink_eyes_images}")
        log().info(f"open_mouth_images{self.open_mouth_images}")
        log().info(f"shake_head_images{self.shake_head_images}")
        log().info(f"nod_head_images{self.nod_head_images}")
        log().info(f"colorful_images{self.colorful_images}")
        # print(f"---------------{self.ws}-----")
        self.ws.run_forever(sslopt=sslopt,ping_interval=5,ping_timeout=3)
    def get_file_bytes(self,file_name):
        this = inspect.getfile(inspect.currentframe())
        # file_path = os.path.join(config.image_path, "go_image/ids_ws_face", file_name)
        with open(file_name, 'rb') as f:
            bytes = f.read()
            return bytes   
        
    def get_result(self,session_id,IdentityApi):
        session_id = session_id
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200   
        is_liveness = resp.json_get("session_result.is_liveness")
        liveness_score = resp.json_get("session_result.liveness_score") 
        log().info(f"is_liveness:{is_liveness},liveness_score:{liveness_score}")   
        assert is_liveness
        assert liveness_score > 0.5

    def on_message(self,ws,message):
        log().info("################# on_message #################")  
        # print("message%s" % message) 
        base_path =  os.path.join(config.ids_image_path, "interactive_liveness")
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
        # init_count = 15
        # frame_count = max_frame_count - 15
        # 采集请求            
        if message_type == ids_ws_service_pb2.COLLECT_REQUEST:    

            if action_type == 1:
                for item in self.blink_eyes_images:
                    cli_msg.frame_message.image = self.get_file_bytes(os.path.join(base_path,item["image"]))
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                log().info(f"发送成功!{action_type}")

            elif action_type == 2:
                for item in self.open_mouth_images:
                    cli_msg.frame_message.image = self.get_file_bytes(os.path.join(base_path,item["image"]))
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                log().info(f"发送成功!{action_type}")

            elif action_type == 3:
                for item in self.shake_head_images:
                    cli_msg.frame_message.image = self.get_file_bytes(os.path.join(base_path,item["image"]))
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                log().info(f"发送成功!{action_type}")

            elif action_type == 4:
                for item in self.nod_head_images:
                    cli_msg.frame_message.image = self.get_file_bytes(os.path.join(base_path,item["image"]))
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                log().info(f"发送成功!{action_type}")
                
            elif select_policy != ids_ws_service_pb2.SELECT_STAGE_START_END:
                if msg_id == 1:
                    for item in self.action_type_none_images[:self.detect_max_index]:
                        cli_msg.frame_message.image = self.get_file_bytes(os.path.join(base_path,item["image"]))
                        self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                    log().info(f"第一次对准发送成功!")
                else:    
                    log().info("进入炫彩对准")
                    for item in self.action_type_none_images[self.detect_max_index:]:
                        cli_msg.frame_message.image = self.get_file_bytes(os.path.join(base_path,item["image"]))
                        self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                    log().info(f"炫彩对准发送成功!")

            if select_policy == ids_ws_service_pb2.SELECT_STAGE_START_END:
                    
                log().info("进入炫彩检测")
                color_list = []
                i=0 
                # 颜色顺序ABBCCDDE
                for color_config in color_configs:
                    if i in [1,2,3]:
                        color_list.append(color_config.color)
                    color_list.append(color_config.color)
                    i = i + 1    
                log().info(f"颜色序列!{color_list}")    
                for i in range(2 * (len(color_configs)-1)):
                    cli_msg.frame_message.color = color_list[i]
                    
                    for item in self.colorful_images:
                        if color_list[i] == 0:
                            color = 'black'
                        elif color_list[i]== 16711680:
                            color = 'red' 
                        elif color_list[i] == 65280:   
                            color = 'green'
                        elif color_list[i] == 16776960:   
                            color = 'yellow'
                        elif color_list[i] == 255:     
                            color = 'blue'
                        if 'color' in item and item['color'] == color:
                            image = self.get_file_bytes(os.path.join(base_path,item["image"]))
                    cli_msg.frame_message.image = image        
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                log().info("发送炫彩数据!")
        elif message_type == ids_ws_service_pb2.DETECT_RESULT:
            log().info("Get Result!")
            # result = server_message.detect_result.err_msg
            # if result == "ok":
            #     get_result(self.session_id,self.ak,self.sk)
            #     self.get_result(self.session_id,self.IdentityApi)
            # else:
            #     pass
                    

    def on_error(self,ws,error):
        log().info("################# on_error #################")       
        log().info(f"error：{error}")   

    def on_close(self,ws, close_status_code, close_reason):
        log().info("################# on_close #################")
        log().info(f"on_close:{close_status_code}:{close_reason}")
