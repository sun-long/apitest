from locust import User, task, TaskSet,events, between, FastHttpUser
from locust.runners import logger
import json
import requests
import inspect
import asyncio
import websockets
from protobuf_to_dict import protobuf_to_dict
from commonlib.pb import ids_ws_service_pb2
import time
import os
import ssl
import nest_asyncio
import queue
from commonlib import config, sign_utils,utils
nest_asyncio.apply()

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
        data = {
            "session": {
                "session_type": "LIVENESS",
                "candidate_actions": ["BLINK_EYES", "OPEN_MOUTH", "SHAKE_HEAD", "NOD_HEAD"],
                "action_number": 2,
                "pick_images_by_quality_number": 5,
                "pick_images_per_action_number": 2
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
        livenss_score = res.json()["session_result"]["livenss_score"]
        logger.info(f"is_liveness:{is_liveness},livenss_score:{livenss_score}")     

class WebSocketClient(object):
    def __init__(self):
        pass
    
    async def send_msg(self, websocket, action_type_none_image, blink_eyes_image, open_mouth_image, shake_head_image, nod_head_image,session_id,aksk):
            '''
            发送请求数据
            '''
            tmsp = ids_ws_service_pb2.Timestamp()
            tmsp.seconds = int(time.time())
            nanos = time.time_ns()
            str_nanos = str(nanos)
            split_nanos = str_nanos[10:]
            tmsp.nanos = int(split_nanos)

            cli_msg = ids_ws_service_pb2.ClientMessage()
            cli_msg.server_msg_id = 1
            cli_msg.message_type = ids_ws_service_pb2.FRAME_MESSAGE

            cli_msg.frame_message.image = action_type_none_image
            cli_msg.frame_message.timestamp.seconds = tmsp.seconds
            cli_msg.frame_message.timestamp.nanos = tmsp.nanos
            
            for i in range(10):
                await websocket.send(cli_msg.SerializeToString())
            logger.info("发送成功!")    
            # await recv_msg(websocket)
            while True:
                _, message_type, action_type, msg_id, select_policy, color_configs, max_frame_count = await WebSocketClient.recv_msg(self, websocket)
                cli_msg.server_msg_id = msg_id
                init_count = 15
                frame_count = max_frame_count - 15
                # 采集请求
                if message_type == ids_ws_service_pb2.COLLECT_REQUEST:
                    # await asyncio.sleep(1)
                    cli_msg.frame_message.image = get_file_bytes(
                        'w6.jpg')
                    if action_type == 1:
                        for i in range(init_count):

                            await websocket.send(cli_msg.SerializeToString())
                            
                        for i in range(frame_count):
                            # await asyncio.sleep(1)
                            cli_msg.frame_message.image = blink_eyes_image
                            await websocket.send(cli_msg.SerializeToString())
                        logger.info("发送成功1!")

                    elif action_type == 2:
                        for i in range(init_count):
                            await websocket.send(cli_msg.SerializeToString())

                        for i in range(frame_count):
                            cli_msg.frame_message.image = open_mouth_image
                            await websocket.send(cli_msg.SerializeToString())
                        logger.info("发送成功2!")

                    elif action_type == 3:
                        for i in range(init_count):
                            await websocket.send(cli_msg.SerializeToString())
                        for i in range(frame_count):
                            cli_msg.frame_message.image = shake_head_image
                            await websocket.send(cli_msg.SerializeToString())
                        logger.info("发送成功3!")

                    else:
                        for i in range(init_count):
                            await websocket.send(cli_msg.SerializeToString())

                        for i in range(frame_count):
                            cli_msg.frame_message.image = nod_head_image
                            await websocket.send(cli_msg.SerializeToString())
                        logger.info("发送成功4!")

                    if select_policy == ids_ws_service_pb2.SELECT_STAGE_START_END:
                        logger.info("进入炫彩检测")
                        for i in range(2 * (len(color_configs)-1)):
                            image = get_file_bytes('w6.jpg')
                            cli_msg.frame_message.image = image
                            # cli_msg.frame_message.color = 15138560
                            await websocket.send(cli_msg.SerializeToString())
                        logger.info("发送炫彩数据!")
                            # events.request_success.fire(request_type="websocket", name='wsUser', response_time=0,response_length=0)
                            
                    else:
                        continue

                else:
                    # 获取检测结果
                    get_result(session_id,aksk)
                    break

    async def recv_msg(self, websocket):
        while True:
            logger.info("等待接收消息!")
            await asyncio.sleep(1)
            # recv_text = await websocket.recv()
            # start = time.time()
            recv_text = await asyncio.wait_for(websocket.recv(), timeout=30)
            server_message = ids_ws_service_pb2.ServerMessage()
            server_message.ParseFromString(recv_text)
            msg_id = server_message.msg_id
            message_type = server_message.message_type
            action_type = server_message.collect_request.action_type
            select_policy = server_message.collect_request.frame_config.select_policy
            color = server_message.collect_request.color_configs
            # err_code = server_message.detect_result.err_code
            max_frame_count = server_message.collect_request.frame_config.max_frame_count
            d = protobuf_to_dict(server_message)
            # total_time = int((time.time() - start) * 1000)
            logger.info(f"get message:{d}")
            # events.request_success.fire(request_type="recv", name='wsUser', response_time=total_time,response_length=0)
            return server_message, message_type, action_type, msg_id, select_policy, color, max_frame_count

class WebsocketUser(User):
    abstract = True
    def __init__(self, *args, **kwargs):
        super(WebsocketUser, self).__init__(*args, **kwargs)
        self.client = WebSocketClient()
        
class TestWS(TaskSet):
    
    async def main_logic(self):
            print("开始连接服务端")
            self.wss_url = 'wss://ids.test-sensebelt.com/face?action=InteractiveLiveness&version=v1'
            ssl_context = ssl.SSLContext()
            ssl_context.verify_mode = ssl.CERT_NONE
            ssl_context.check_hostname = False
            aksk = self.user.q.get()
            self.user.q.put(aksk)
            tokens,session_id = get_token(aksk)
            try:
                start = time.time()
                async with websockets.connect(self.wss_url, subprotocols=tokens, ssl=ssl_context) as websocket:
                    total_time = int((time.time() - start) * 1000)
                    events.request_success.fire(request_type="connect", name='websocket', response_time= total_time,response_length=0)
                    start = time.time()
                    await WebSocketClient.recv_msg(self, websocket)
                    total_time = int((time.time() - start) * 1000)
                    events.request_success.fire(request_type="recv", name='wsUser', response_time=total_time,response_length=0)
                    action_type_none_image = get_file_bytes('w6.jpg')
                    blink_eyes_image = get_file_bytes('w1.jpg')
                    open_mouth_image = get_file_bytes('w2.jpg')
                    shake_head_image = get_file_bytes('w3.jpg')
                    nod_head_image = get_file_bytes('w4.jpg')
                    await WebSocketClient.send_msg(self, websocket, action_type_none_image,
                                        blink_eyes_image, open_mouth_image, shake_head_image,
                                        nod_head_image,session_id,aksk)
                    
            except websockets.ConnectionClosed:
                end = time.time()
                events.request_failure.fire(request_type="connect", name='exception', response_time=end - start,response_length=0)
                # print('Task runs %0.2f seconds.' % ( (end - start)))
                
    @task
    def run_ws(self):
        try:
            asyncio.run(self.main_logic())
        except websockets.ConnectionClosed as e:
            pass
            print(f'Terminated', e)
        # t2 = time.time()
        # selector = selectors.SelectSelector()       
        # loop = asyncio.SelectorEventLoop(selector)
        # try:
        #     loop.run_until_complete(self.main_logic())  # 完成事件循环，直到最后一个任务结束
        # finally:
        #     loop.close()
        # print("Async total time:", time.time() - t2)

class Mytask(WebsocketUser):
    host = "ids.test-sensebelt.com"
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

