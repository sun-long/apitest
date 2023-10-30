# -*- encoding: utf-8 -*-
import asyncio
import websockets
from protobuf_to_dict import protobuf_to_dict
from commonlib.pb import ids_ws_service_pb2
from commonlib import config
from commonlib.sign_utils import encode_jwt_token_pt
import logging
import time
import os
import requests
import json
import ssl
import urllib3
import jwt

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TestWsApi:

    def __init__(self):
        pass

    def get_token(self):
        url = "https://ids.test.sensebelt.net/identity"
        headers = {
            "X-Belt-Version": "v1",
            "X-Belt-Action": "CreateSession",
            "X-Belt-Signature": encode_jwt_token_pt("2L4Y8M8wZY2lEFr7s9IqQGVUwEq","sNPLIkt33QiuuvN9IyTOlZiAYdBHZMWJ")
        }
        data = {
            "session": {
                "session_type": "LIVENESS",
                "candidate_actions": ["BLINK_EYES", "OPEN_MOUTH", "SHAKE_HEAD", "NOD_HEAD"],
                "action_number": 2,
                "pick_images_by_quality_number": 5,
                "pick_images_per_action_number": 2
            }
        }
        token = []
        res = requests.post(url=url, headers=headers,
                            data=json.dumps(data), verify=False)
        token.append(res.json()["biz_token"])
        # print("token:", token, "\nsession_id:", res.json()["session_id"])
        return token

    def get_file_bytes(self, file_name):
        file_path = os.path.join(
             config.image_path, "go_image\\ids_ws_face", file_name)

        with open(file_path, 'rb') as f:
            bytes = f.read()
            return bytes

    async def send_msg(self, websocket, action_type_none_image, blink_eyes_image, open_mouth_image, shake_head_image, nod_head_image):
        '''
        发送请求数据
        '''
        tmsp = ids_ws_service_pb2.Timestamp()
        tmsp.seconds = int(time.time())
        nanos = time.time_ns()
        str_nanos = str(time.time_ns())
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
        # await recv_msg(websocket)
        
        while True:
            _, message_type, action_type, msg_id, select_policy, color_configs, max_frame_count = await self.recv_msg(websocket)
            
            cli_msg.server_msg_id = msg_id
            init_count = 8
            frame_count = max_frame_count - init_count
            # 采集请求
            if message_type == ids_ws_service_pb2.COLLECT_REQUEST:
                # await asyncio.sleep(1)
                cli_msg.frame_message.image = self.get_file_bytes(
                    'w6.jpg')
                if action_type == 1:
                    for i in range(init_count):

                        await websocket.send(cli_msg.SerializeToString())
                        
                    for i in range(frame_count):
                        # await asyncio.sleep(1)
                        cli_msg.frame_message.image = blink_eyes_image
                        await websocket.send(cli_msg.SerializeToString())
                    logging.error("发送成功!")

                elif action_type == 2:
                    for i in range(init_count):
                        await websocket.send(cli_msg.SerializeToString())

                    for i in range(frame_count):
                        cli_msg.frame_message.image = open_mouth_image
                        await websocket.send(cli_msg.SerializeToString())
                    logging.error("发送成功!")

                elif action_type == 3:
                    for i in range(init_count):
                        await websocket.send(cli_msg.SerializeToString())
                    for i in range(frame_count):
                        cli_msg.frame_message.image = shake_head_image
                        await websocket.send(cli_msg.SerializeToString())
                    logging.error("发送成功!")

                elif action_type == 4:
                    for i in range(init_count):
                        await websocket.send(cli_msg.SerializeToString())

                    for i in range(frame_count):
                        cli_msg.frame_message.image = nod_head_image
                        await websocket.send(cli_msg.SerializeToString())
                    logging.error("发送成功!")

                elif select_policy != ids_ws_service_pb2.SELECT_STAGE_START_END:
                    
                    for i in range(frame_count):
                        await websocket.send(cli_msg.SerializeToString())
                      
                if select_policy == ids_ws_service_pb2.SELECT_STAGE_START_END:
                    logging.error("进入炫彩对准!")
                    
                    for i in range(frame_count):
                        await websocket.send(cli_msg.SerializeToString())
                    
                    logging.error("进入炫彩检测")
                    for i in range(2 * (len(color_configs)-1)):
                        image = self.get_file_bytes('w6.jpg')
                        cli_msg.frame_message.image = image
                        await websocket.send(cli_msg.SerializeToString())
                        logging.error("发送炫彩数据!")
                else:
                    continue

            else:
                # 获取检测结果
                break

    async def recv_msg(self, websocket):
        # while True:
        # logging.error("等待接收消息!")
        # await asyncio.sleep(1)
        recv_text = await websocket.recv()
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
        print(d)
        # print(d['collect_request'])
        # print("ServerMessage:\n", server_message)
        return server_message, message_type, action_type, msg_id, select_policy, color, max_frame_count

    # 客户端主逻辑
    async def main_logic(self):
        print("开始连接服务端")
        self.wss_url = 'wss://ids.test.sensebelt.net/face?action=InteractiveLiveness&version=v1'
        ssl_context = ssl.SSLContext()
        ssl_context.verify_mode = ssl.CERT_NONE
        ssl_context.check_hostname = False
        async with websockets.connect(self.wss_url, subprotocols=self.get_token(), ssl=ssl_context) as websocket:
            await self.recv_msg(websocket)
            action_type_none_image = self.get_file_bytes('w6.jpg')
            blink_eyes_image = self.get_file_bytes('w1.jpg')
            open_mouth_image = self.get_file_bytes('w2.jpg')
            shake_head_image = self.get_file_bytes('w3.jpg')
            nod_head_image = self.get_file_bytes('w4.jpg')

            await self.send_msg(websocket, action_type_none_image,
                                blink_eyes_image, open_mouth_image, shake_head_image,
                                nod_head_image)

            
if __name__ == "__main__":
    client = TestWsApi()

    try:
        asyncio.run(client.main_logic())
    except websockets.ConnectionClosed as e:
        print(f'Terminated', e)
