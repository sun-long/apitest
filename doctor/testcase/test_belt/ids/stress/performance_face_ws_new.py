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
from  commonlib.ids_ws_client import IdsWebSocketClient
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
        
    
def get_aksks(filename):
    config_path = os.path.join(config.project_path, f"testcase/test_belt/ids/stress/{filename}")
    aksk_list=[]    
    if os.path.exists(config_path):
        aksk_list = utils.read_csv(config_path)
    return aksk_list
    
def get_token(host,ak,sk,actions):
        url = f"https://{host}/identity"
        token =  sign_utils.encode_jwt_token_pt(ak, sk)
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
                "candidate_actions": actions,
                 "action_number": len(actions),
                "pick_images_by_quality_number": 1,
                "pick_images_per_action_number": 1,
                "h5_config": {
                    "redirect_url": "https://baidu.com",
                    "logo_url": "https://sensebelt.com/assets/logo.8fed4046.png",
                    "page_title": "liveness"
                },
                "extra_info": "string",

            }
        }
        res = requests.post(url=url, headers=headers,
                            data=json.dumps(data), verify=False)
        logger.info(res.status_code)
        biz_tokens = []                                    
        biz_tokens.append(res.json()["biz_token"])
        session_id = res.json()["session_id"]
        logger.info(f"biz_token:{biz_tokens},session_id:{session_id}")
    
        return biz_tokens,session_id
def get_result(host,session_id,ak,sk):
        url = f"https://{host}/identity"
        token =  sign_utils.encode_jwt_token_pt(ak,sk)
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


class WebsocketUser(User):
    abstract = True
    def __init__(self, *args, **kwargs):
        super(WebsocketUser, self).__init__(*args, **kwargs)
        self.client = IdsWebSocketClient(self.host)
        
        #self.client._locust_environment = self.environmen
        
class TestWS(TaskSet):   
    
    def on_start(self):
        logger.info('hello')

        aksk = self.user.q.get()
        self.user.q.put(aksk)
        meta_file = os.path.join(config.ids_image_path, "interactive_liveness/interactiveLiveness_HLI2UHniAz7LDHW90tNviN6IIUxjxuMk9Yaj.json")
        with open(meta_file,"r",encoding="utf-8") as f:
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
        
                self.param_dict={
                    "ak":aksk[0],
                    "sk":aksk[1],
                    "action_type_none_images":action_type_none_images,
                    "blink_eyes_images":blink_eyes_images,
                    "open_mouth_images":open_mouth_images,
                    "shake_head_images":shake_head_images,
                    "nod_head_images":nod_head_images,
                    "colorful_images":colorful_images,
                    "detect_max_index":detect_max_index,
                    "IdentityApi":None,
                  #  "host":self.client.host,
                    "actions":actions

                }

    def on_stop(self):
        logger.info('goodbye')
                
    @task
    def run_ws(self): 
        start = time.time()    
        tokens,session_id = get_token(self.client.host,self.param_dict["ak"],self.param_dict["sk"],self.param_dict["actions"])
        self.param_dict["tokens"]=tokens
        self.param_dict["session_id"]=session_id
        try:
            self.client.start(**self.param_dict)
            get_result(self.client.host,session_id,self.param_dict["ak"],self.param_dict["sk"])
            total_time = int((time.time() - start) * 1000)
            success_call(name='interactive_liveness', recvText="ok", total_time= total_time)
        except Exception as e:
            end = time.time()
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

