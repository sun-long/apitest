#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   utils_websocket.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/11/5 下午7:01   wangan      1.0         None
'''

import asyncio
import websockets

# 向服务器端认证，用户名密码通过才能退出循环
async def auth_system(websocket):
    while True:
        cred_text = input("please enter your username and password: ")
        await websocket.send(cred_text)
        response_str = await websocket.recv()
        if "congratulation" in response_str:
            return True

# 向服务器端发送认证后的消息
async def send_msg(websocket):
    while True:
        _text = input("please enter your context: ")
        if _text == "exit":
            print(f'you have enter "exit", goodbye')
            await websocket.close(reason="user exit")
            return False
        await websocket.send(_text)
        recv_text = await websocket.recv()
        print(f"{recv_text}")

# 客户端主逻辑
async def main_logic():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjEyLCJleHAiOjE2MzYxMTM3NTB9.5PX_FkA2rtrlCPUvujCY92Dzl35dqjOzxb1kpllKbu4"
    async with websockets.connect('ws://staging.argus.sensetime.com/minos/message-notify/api/v1/message?access_token=%s' % token) as websocket:
        # await auth_system(websocket)

        await send_msg(websocket)

asyncio.get_event_loop().run_until_complete(main_logic())