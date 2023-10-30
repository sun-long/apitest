# -*- encoding: utf-8 -*-
import asyncio
import websockets
from protobuf_to_dict import protobuf_to_dict
from commonlib.pb import ids_ws_service_pb2
from commonlib import config, sign_utils
from commonlib.sign_utils import encode_jwt_token_pt

import logging
import time
import os
import requests
import json
import ssl
import urllib3


class TestWsApi:

    def __init__(self):
        self.wss_url = 'wss://ids.test.sensebelt.net/ocr?action=ScanCard&version=v1'

    def get_token(self):
        url = "https://ids.test.sensebelt.net/identity"
        headers = {
            "X-Belt-Version": "v1",
            "X-Belt-Action": "CreateSession",
            "X-Belt-Signature": encode_jwt_token_pt("2L4Y8M8wZY2lEFr7s9IqQGVUwEq", "sNPLIkt33QiuuvN9IyTOlZiAYdBHZMWJ")
        }
        data = {
            "session": {
                "session_type": "IDENTITY_VERIFICATION",
                "id_verification": {
                    "certificate_type": "IDCARD",
                    "min_quality_level": "NORMAL"
                },
                "h5_config": {
                    "redirect_url": "www.baidu.com"
                }
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
             config.image_path, "go_image/idcard_ws", file_name)

        with open(file_path, 'rb') as f:
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
    
    def create_ws_connection(self):
        ssl_context = ssl.SSLContext()
        ssl_context.verify_mode = ssl.CERT_NONE
        ssl_context.check_hostname = False
        ws = websockets.connect(self.wss_url, subprotocols=self.get_token(), ssl=ssl_context)
        logging.error("建立 WebSocket 连接")
        return ws

    async def send_msg(self, ws_conn, **kwargs):
        '''
        发送消息到WebSocket服务器
        '''
        # _, max_frame_count = await self.recv_msg(ws_conn)
        # logging.error(f"接收到帧数：{max_frame_count}")
        if "idcard_front_image" in kwargs:
            idcard_front_image = kwargs["idcard_front_image"]
            roi = kwargs.get("roi", None)
            cli_msg = self.get_client_message(ids_ws_service_pb2.IDCARD_FRONT, idcard_front_image, roi)
            await ws_conn.send(cli_msg.SerializeToString())
            logging.error("发送身份证人像面成功!")

        elif "idcard_back_image" in kwargs:
            roi = kwargs.get("roi", None)
            idcard_back_image = kwargs["idcard_back_image"]   
            cli_msg = self.get_client_message(ids_ws_service_pb2.IDCARD_BACK, idcard_back_image, roi)
            await ws_conn.send(cli_msg.SerializeToString()) 
            logging.error("发送身份证国徽面成功!")
        else:
            raise Exception("invalid params")

    
    async def recv_msg(self, ws_conn):
        while True:
            logging.debug("等待接收消息!")
            recv_text = await ws_conn.recv()
            server_message = ids_ws_service_pb2.ServerMessage()
            server_message.ParseFromString(recv_text)
            max_frame_count = server_message.collect_request.frame_config.max_frame_count
            d = protobuf_to_dict(server_message)
            logging.error(f"ServerMessage: {d}")
            return d
             
    async def send_idcard_front_and_wait(self, idcard_front_image, roi=None):
        '''
        发送身份证人像面并等待结果
        '''
        ws_conn = await self.create_ws_connection()
        await self.recv_msg(ws_conn)

        t1 = time.time()
        await self.send_msg(ws_conn, idcard_front_image=idcard_front_image, roi=roi)
        t2 = time.time()
        logging.error(f"发送身份证人像面总耗时为：{t2 - t1:.3f}s")

        result = await self.recv_msg(ws_conn)
        return result


    async def send_idcard_back_and_wait(self, idcard_back_image, roi=None):
        '''
        发送身份证国徽面并等待结果
        '''
        ws_conn = await self.create_ws_connection()
        await self.recv_msg(ws_conn)

        t1 = time.time()
        await self.send_msg(ws_conn, idcard_back_image=idcard_back_image, roi=roi)
        t2 = time.time()
        logging.error(f"发送身份证国徽面总耗时为：{t2 - t1:.3f}s")

        result = await self.recv_msg(ws_conn)
        return result
      
if __name__ == "__main__":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    client = TestWsApi()
    
    idcard_front_image = client.get_file_bytes('idcard_normal1.jpg')
    idcard_back_image = client.get_file_bytes('idcard_normal2.jpg')

    asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi={'left': 0, 'top': 0, 'width': 1050, 'height': 670}))
    asyncio.run(client.send_idcard_back_and_wait(idcard_back_image))