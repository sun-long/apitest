
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


class IdsScanWebSocketClient(object):
    def __init__(self):
        self.ws= None
        self.session_id = None
        
    def start(self,**kwargs):
        log().info("Begin to connect to server")
        self.host = kwargs["host"]
        self.wss_url = f'wss://{self.host}/ocr?action=ScanCard&version=v1'
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
        self.OcrApi = kwargs["OcrApi"]
        self.image = kwargs["image"]
        self.roi = kwargs["roi"]
        self.label = kwargs["label"]
        self.ws.run_forever(sslopt=sslopt,ping_interval=5,ping_timeout=3)
        
    def get_file_bytes(self,file_name):
        this = inspect.getfile(inspect.currentframe())
        # file_path = os.path.join(config.image_path, "go_image/ids_ws_face", file_name)
        with open(file_name, 'rb') as f:
            bytes = f.read()
            return bytes   
        
    def get_client_message(self, label, image, roi=None):
        '''
        获取 ClientMessage 对象
        '''
        tmsp = ids_ws_service_pb2.Timestamp()
        tmsp.seconds = int(time.time())
        str_nanos = str(time.time_ns())
        tmsp.nanos = int(str_nanos[10:])
            
        cli_msg = ids_ws_service_pb2.ClientMessage()
        cli_msg.server_msg_id = 1
        cli_msg.message_type = ids_ws_service_pb2.FRAME_MESSAGE  
        cli_msg.frame_message.timestamp.seconds = tmsp.seconds
        cli_msg.frame_message.timestamp.nanos = tmsp.nanos
            
        if roi is not None:
                cli_msg.frame_message.roi.left = roi['left']
                cli_msg.frame_message.roi.top = roi['top']
                cli_msg.frame_message.roi.width = roi['width']
                cli_msg.frame_message.roi.height = roi['height']
        else:
            cli_msg.frame_message.roi.left = 0
            cli_msg.frame_message.roi.top = 0
            cli_msg.frame_message.roi.width = 1050
            cli_msg.frame_message.roi.height = 670

        cli_msg.frame_message.label = label
        cli_msg.frame_message.image = image
        
        return cli_msg    
        
    def getWSresult(self):
        return self.result
    def on_message(self,ws,message):

        log().info("################# on_message #################")  
        # print("message%s" % message) 
        base_path =  os.path.join(config.image_path, "go_image/idcard_ws")
        
        server_message = ids_ws_service_pb2.ServerMessage()
        server_message.ParseFromString(message)
        msg_id = server_message.msg_id
        message_type = server_message.message_type
        max_frame_count = server_message.collect_request.frame_config.max_frame_count
        d = protobuf_to_dict(server_message)
        log().info(f"get message:{d}")

        if message_type == ids_ws_service_pb2.COLLECT_REQUEST:
                    
            log().info("进入卡证扫描")
            image = self.get_file_bytes(os.path.join(base_path,self.image))
            if self.label == "FRONT":
                label = ids_ws_service_pb2.IDCARD_FRONT
            elif self.label == "BACK":
                label = ids_ws_service_pb2.IDCARD_BACK
                
            cli_msg = self.get_client_message(label, image, self.roi)
            self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
            log().info("发送卡证数据!")
        elif message_type == ids_ws_service_pb2.DETECT_RESULT:
            log().info("Get Result!")
            self.result = d
 
                    

    def on_error(self,ws,error):
        log().info("################# on_error #################")       
        log().info(f"error：{error}")   

    def on_close(self,ws, close_status_code, close_reason):
        log().info("################# on_close #################")
        log().info(f"on_close:{close_status_code}:{close_reason}")
