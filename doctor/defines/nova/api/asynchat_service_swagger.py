#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class AsynchatSwaggerApi(BaseApi):
    """ web接口"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        self.host = host
        self.ext_info = ext_info
        self.config_obj = config_obj
        self.token = token
        self.host_map = self.readHostMap(collections.name)
        self.TOKEN_NAME = ""
        self.TOKEN_VALUE = "%s"  # token默认信息
        collections.init(self, conf=config_obj, ext_info=ext_info)

    def genPostMan(self):
        """ 生成postman接口文件"""
        self.ext_info.isRequestOpened = True
        self.genPostManFromSwagger(collections)

    def ChatCompletionsInvokePostApi(self, request_id=None, data=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  异步无状态补全调用. """
        """  path: [post]/v1/llm/chat-completions/invoke API """
        """  body: 
                {
                    "data": {
                        "know_ids": [],
                        "max_new_tokens": 0,
                        "messages": [
                            {
                                "content": "",
                                "role": ""
                            }
                        ],
                        "model": "",
                        "repetition_penalty": 0,
                        "stream": false,
                        "temperature": 0,
                        "top_p": 0,
                        "user": ""
                    },
                    "request_id": ""
                }
        """
        """  resp:
                default():
                ""

        """
        intef = collections.interface("AsynChat", "ChatCompletionsInvoke")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("request_id", request_id)
        intef.update_body("data", data)
        return intef.request() if sendRequest else intef

    def ChatCompletionsRetrievePostApi(self, request_id=None, data=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  异步无状态补全结果查询. """
        """  path: [post]/v1/llm/chat-completions/retrieve API """
        """  body: 
                {
                    "data": {},
                    "request_id": ""
                }
        """
        """  resp:
                200():
                ""
                201():
                ""
                202(请求已经发送但是未处理完成):
                ""

        """
        intef = collections.interface("AsynChat", "ChatCompletionsRetrieve")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("request_id", request_id)
        intef.update_body("data", data)
        return intef.request() if sendRequest else intef

