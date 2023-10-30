 # -*- coding: utf-8 -*-
from locust import User, task, TaskSet,events, between, FastHttpUser
from locust.runners import logger
import json
import requests
import inspect
from websocket import  WebSocketApp,ABNF
import websocket
from protobuf_to_dict import protobuf_to_dict
from commonlib.pb import ids_ws_service_pb2
import time
import os
import ssl
import queue
import uuid
from commonlib import config, sign_utils,utils
import urllib3
urllib3.disable_warnings()

def success_call(name, recvText, total_time):
    events.request_success.fire(
        request_type="[Success]",
        name=name,
        response_time=total_time,
        response_length=len(recvText)
    )


def fail_call(name, total_time, e):
    events.request_failure.fire(
        request_type="[Fail]",
        name=name,
        response_time=total_time,
        response_length=0,
        exception=e,
    )
    
def get_file_bytes(file_name):
    this = inspect.getfile(inspect.currentframe())
    file_path = os.path.join(
        config.image_path, "go_image/ids_ws_face", file_name)
    with open(file_path, 'rb') as f:
        bytes = f.read()
        return bytes
        
    
def get_aksks(filename):
    config_path = os.path.join(config.project_path, f"testcase/test_belt/ids/stress/{filename}")
    aksk_list=[]    
    if os.path.exists(config_path):
        aksk_list = utils.read_csv(config_path)
    return aksk_list
    
def get_token(aksk):
        url = "https://ids.test.sensebelt.net/identity"
        token =  sign_utils.encode_jwt_token_pt(aksk[0], aksk[1])
        # logger.info(f'token:{token}')
        headers = {
            "X-Belt-Version": "v1",
            "X-Belt-Action": "CreateSession",
            "X-Belt-Signature": token}
        uuid_str =str(uuid.uuid4())
        data = {
            "session": {
                "session_type": "H5_LIVENESS",
                "uuid": uuid_str,
                "candidate_actions": [
                    "BLINK_EYES",
                    "OPEN_MOUTH",
                    "SHAKE_HEAD",
                    "NOD_HEAD"],
                 "action_number": 2,
                "pick_images_by_quality_number": 1,
                "pick_images_per_action_number": 1,
                "h5_config": {
                    "redirect_url": "https://baidu.com",
                    "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                    "page_title": "liveness"
                },
                #"save_process_video":True,
                "extra_info": "string",

            }
        }
        res = requests.post(url=url, headers=headers,
                            data=json.dumps(data), verify=False)

        biz_tokens = []                                    
        biz_tokens.append(res.json()["biz_token"])
        session_id = res.json()["session_id"]
        logger.info(f"biz_token:{biz_tokens},session_id:{session_id}")
    
        return biz_tokens,session_id
def get_result(session_id,aksk):
        url = "https://ids.test.sensebelt.net/identity"
        token =  sign_utils.encode_jwt_token_pt(aksk[0], aksk[1])
        # logger.info(f'token:{token}')
        headers = {
            "X-Belt-Version": "v1",
            "X-Belt-Action": "GetSessionLivenessResult",
            "X-Belt-Signature": token}
        data = {
            "session_id": session_id
        }
        res = requests.post(url=url, headers=headers,
                            data=json.dumps(data), verify=False)   

        # print(f"session_result:{res.json()}")
        is_liveness = res.json()["session_result"]["is_liveness"]
        liveness_score = res.json()["session_result"]["liveness_score"]
        logger.info(f"is_liveness:{is_liveness},liveness_score:{liveness_score}")        


class WebSocketClient(object):
    def __init__(self):
        self.ws= None
        self.session_id = None
        self.aksk = None

    def start(self,tokens,session_id,aksk):
        logger.info("Begin to connect to server")
        self.wss_url = 'wss://ids.test.sensebelt.net/face?action=InteractiveLiveness&version=v1'
        sslopt ={"cert_reqs": ssl.CERT_NONE,"check_hostname": False}
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(
            self.wss_url,
            subprotocols=tokens,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.session_id = session_id
        self.aksk = aksk
        # print(f"---------------{self.ws}-----")
        self.ws.run_forever(sslopt=sslopt,ping_interval=5,ping_timeout=3)


    def on_message(self,ws,message):
        logger.info("################# on_message #################")  
        # print("message%s" % message) 

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
                # total_time = int((time.time() - start) * 1000)
        logger.info(f"get message:{d}")
        
        # print("return:{},{},{},{},{},{},{}".format(server_message, message_type, action_type, msg_id, select_policy, color_configs, max_frame_count))
        action_type_none_image = get_file_bytes('w6.jpg')
        blink_eyes_image = get_file_bytes('w1.jpg')
        open_mouth_image = get_file_bytes('w2.jpg')
        shake_head_image = get_file_bytes('w3.jpg')
        nod_head_image = get_file_bytes('w4.jpg')

        tmsp = ids_ws_service_pb2.Timestamp()
        tmsp.seconds = int(time.time())
        nanos = time.time_ns()
        str_nanos = str(nanos)
        split_nanos = str_nanos[10:]
        tmsp.nanos = int(split_nanos)

        cli_msg = ids_ws_service_pb2.ClientMessage()
        cli_msg.server_msg_id = msg_id
        cli_msg.message_type = ids_ws_service_pb2.FRAME_MESSAGE
        cli_msg.frame_message.image = action_type_none_image
        cli_msg.frame_message.timestamp.seconds = tmsp.seconds
        cli_msg.frame_message.timestamp.nanos = tmsp.nanos
       
        for i in range(10):
            self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
        logger.info("发送成功!")   
        init_count = 15
        frame_count = max_frame_count - 15
        # 采集请求            
        if message_type == ids_ws_service_pb2.COLLECT_REQUEST:
                
            # await asyncio.sleep(1)
            if action_type == 1:
                for i in range(init_count):

                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                    
                for i in range(frame_count):
                    # await asyncio.sleep(1)
                    cli_msg.frame_message.image = blink_eyes_image
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                logger.info(f"发送成功!{action_type}")

            elif action_type == 2:
                for i in range(init_count):
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)

                for i in range(frame_count):
                    cli_msg.frame_message.image = open_mouth_image
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                logger.info(f"发送成功!{action_type}")

            elif action_type == 3:
                for i in range(init_count):
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                for i in range(frame_count):
                    cli_msg.frame_message.image = shake_head_image
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                logger.info(f"发送成功!{action_type}")

            elif action_type == 4:
                for i in range(init_count):
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                for i in range(frame_count):
                    cli_msg.frame_message.image = nod_head_image
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                logger.info(f"发送成功!{action_type}")
            # else:
            #     for i in range(init_count):
            #         print("cli_smg:",cli_msg)
            #         self.ws.send(cli_msg.SerializeToString())
            #     logger.info(f"发送成功!{action_type}")

            if select_policy == ids_ws_service_pb2.SELECT_STAGE_START_END:
                logger.info("进入炫彩检测")
                for i in range(2 * (len(color_configs)-1)):
                    image = get_file_bytes('w6.jpg')
                    cli_msg.frame_message.image = image
                    # cli_msg.frame_message.color = 15138560
                    self.ws.send(cli_msg.SerializeToString(),opcode=ABNF.OPCODE_BINARY)
                logger.info("发送炫彩数据!")
        elif message_type == ids_ws_service_pb2.DETECT_RESULT:
            logger.info("Get Result!")
            
            result = server_message.detect_result.err_msg
            if result == "ok":
                start = time.time() 
                get_result(self.session_id,self.aksk)
                total_time = int((time.time() - start) * 1000)
                success_call(name='result', recvText="ok", total_time= total_time)
            else:
                fail_call(name='result', total_time=total_time, e=result)
                    

    def on_error(self,ws,error):
        logger.info("################# on_error #################")       
        logger.info(f"error：{error}")   

    def on_close(self,ws, close_status_code, close_reason):
        logger.info("################# on_close #################")
        logger.info(f"on_close:{close_status_code}:{close_reason}")
        #logger.info("on_close", close_status_code, close_reason, sep=", ")

class WebsocketUser(User):
    abstract = True
    def __init__(self, *args, **kwargs):
        super(WebsocketUser, self).__init__(*args, **kwargs)
        self.client = WebSocketClient()
        
class TestWS(TaskSet):   
    
    def on_start(self):
        logger.info('hello')

    

    def on_stop(self):
        logger.info('goodbye')
                
    @task
    def run_ws(self):
        aksk = self.user.q.get()
        self.user.q.put(aksk)
        tokens,session_id = get_token(aksk)
        start = time.time()
        try:
            self.client.start(tokens,session_id,aksk)   
            total_time = int((time.time() - start) * 1000)
            success_call(name='wsconn', recvText="ok", total_time= total_time)
        except Exception as e:
            end = time.time()
            #events.request_failure.fire(request_type="connect", name='exception', response_time=end - start,response_length=0)
            fail_call(name='exception', total_time=end - start,e=e)

class Mytask(WebsocketUser):
    host = "ids.test.sensebelt.net"
    wait_time = between(0.5, 3)
    tasks = {
        TestWS: 1
    }
    filename = "aksk_test.csv"
    aksk_list = get_aksks(filename) 
    q =  queue.Queue()
    for i in range(len(aksk_list)):
        data=[]
        data.append(aksk_list[i][0])
        data.append(aksk_list[i][1])
        q.put_nowait(data)

