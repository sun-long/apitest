#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo4.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/5/6 下午2:01   wangan      1.0         None
'''


import json
import time
import logging

from ws4py.client.threadedclient import WebSocketClient


class CG_Client(WebSocketClient):

    def initVar(self, send_req):
        self.send_req = send_req
        self.received_data_list = []

    def opened(self):
        if self.send_req:
            self.send(self.send_req)

    def closed(self, code, reason=None):
        logging.info(f"closed down: {code} : {reason}")

    def received_message(self, resp):
        resp = json.loads(str(resp))
        self.received_data_list.append(resp)


class WebSocketClient(object):
    def __init__(self, url, token=None, send_req=None):
        self.url = url
        self.token = token
        headers = None
        if self.token:
            headers = [("Authorization", token)]
        self.ws = CG_Client(self.url, headers=headers)
        self.ws.initVar(send_req)

    @property
    def received_data_list(self):
        return self.ws.received_data_list

    def start(self):
        self.ws.connect()
        logging.info("WebSocket Client start. url:%s" % self.url)

    def stop(self):
        self.ws.close()
        logging.info("WebSocket Client stop. url:%s" % self.url)


if __name__ == '__main__':

    url = 'wss://10.151.5.205:5043/v1/callback/websocket'
    token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOiJ1c2VyX2FkbWluIiwiZXhwIjoxNjUxODMxNzcyfQ.EW9OEkN1Ho1FSSuMLp1tqC5CXfVPTgbOYeL_yBuj8dE"
    send_req = '{"types":["RECORD_OUTPUT_RESULT"]}'
    wsc = WebSocketClient(url, token=token, send_req=send_req)
    wsc1 = WebSocketClient(url, token=token, send_req=send_req)
    wsc.start()
    wsc1.start()
    #启动任务
    time.sleep(20)
    #任务结束
    wsc.stop()
    wsc1.stop()
    a = wsc.received_data_list
    b = wsc1.received_data_list

    i = 1
