#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class ChatcompletionSwaggerApi(BaseApi):
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

    def ChatCompletionsRequestWrapperPostApi(self, model=None, messages=None, temperature=None, top_p=None, max_new_tokens=None, repetition_penalty=None, stream=None, user=None, know_ids=None, knowledge_config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  无状态补全. """
        """  path: [post]/v1/llm/chat-completions API """
        """  body: 
                {
                    "know_ids": [],
                    "knowledge_config": {
                        "control_level": "[normal]",
                        "knowledge_base_result": false,
                        "online_search_result": false
                    },
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
                }
        """
        """  resp:
                200():
                ""
                201():
                ""
                400():
                ""
                500():
                ""

        """
        intef = collections.interface("ChatCompletion", "ChatCompletionsRequestWrapper")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.update_body("messages", messages)
        intef.update_body("temperature", temperature)
        intef.update_body("top_p", top_p)
        intef.update_body("max_new_tokens", max_new_tokens)
        intef.update_body("repetition_penalty", repetition_penalty)
        intef.update_body("stream", stream)
        intef.update_body("user", user)
        intef.update_body("know_ids", know_ids)
        intef.update_body("knowledge_config", knowledge_config)
        return intef.request() if sendRequest else intef

    def ChatCompletionsOriginRequestWrapperPostApi(self, model=None, messages=None, temperature=None, top_p=None, max_new_tokens=None, repetition_penalty=None, user=None, know_ids=None, knowledge_config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  无状态补全（裸模型）. """
        """  path: [post]/v1/llm/chat-completions/origin API """
        """  body: 
                {
                    "know_ids": [],
                    "knowledge_config": {
                        "control_level": "[normal]",
                        "knowledge_base_result": false,
                        "online_search_result": false
                    },
                    "max_new_tokens": 0,
                    "messages": [
                        {
                            "content": "",
                            "role": ""
                        }
                    ],
                    "model": "",
                    "repetition_penalty": 0,
                    "temperature": 0,
                    "top_p": 0,
                    "user": ""
                }
        """
        """  resp:
                200():
                ""
                400():
                ""
                500():
                ""

        """
        intef = collections.interface("ChatCompletion", "ChatCompletionsOriginRequestWrapper")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.update_body("messages", messages)
        intef.update_body("temperature", temperature)
        intef.update_body("top_p", top_p)
        intef.update_body("max_new_tokens", max_new_tokens)
        intef.update_body("repetition_penalty", repetition_penalty)
        intef.update_body("user", user)
        intef.update_body("know_ids", know_ids)
        intef.update_body("knowledge_config", knowledge_config)
        return intef.request() if sendRequest else intef

    def ChatRequestWrapperPostApi(self, action=None, content=None, model=None, session_id=None, stream=None, know_ids=None, knowledge_config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  有状态对话. """
        """  path: [post]/v1/llm/chat-conversations API """
        """  body: 
                {
                    "action": "[next]",
                    "content": "",
                    "know_ids": [],
                    "knowledge_config": {
                        "control_level": "[normal]",
                        "knowledge_base_result": false,
                        "online_search_result": false
                    },
                    "model": "",
                    "session_id": "",
                    "stream": false
                }
        """
        """  resp:
                200():
                ""
                201():
                ""
                400():
                ""
                500():
                ""

        """
        intef = collections.interface("ChatCompletion", "StatefulChatRequestWrapper")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("action", action)
        intef.update_body("content", content)
        intef.update_body("model", model)
        intef.update_body("session_id", session_id)
        intef.update_body("stream", stream)
        intef.update_body("know_ids", know_ids)
        intef.update_body("knowledge_config", knowledge_config)
        return intef.request() if sendRequest else intef

    def ChatNewSessionRequestWrapperPostApi(self, system_prompt=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  有状态对话创建会话. """
        """  path: [post]/v1/llm/chat/sessions API """
        """  body: 
                {
                    "system_prompt": [
                        {
                            "content": "",
                            "role": ""
                        }
                    ]
                }
        """
        """  resp:
                200():
                ""
                400():
                ""
                500():
                ""

        """
        intef = collections.interface("ChatCompletion", "ChatNewSessionRequestWrapper")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("system_prompt", system_prompt)
        return intef.request() if sendRequest else intef

    def InternalChatRequestWrapperPostApi(self, action=None, biz_id=None, input=None, model=None, parent_turn_id=None, session_id=None, stream=None, know_ids=None, knowledge_config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  内部有状态对话. """
        """  path: [post]/v1/llm/internal/chat API """
        """  body: 
                {
                    "action": "[next]",
                    "biz_id": 0,
                    "input": "",
                    "know_ids": [],
                    "knowledge_config": {
                        "control_level": "[normal]",
                        "knowledge_base_result": false,
                        "online_search_result": false
                    },
                    "model": "",
                    "parent_turn_id": "",
                    "session_id": "",
                    "stream": false
                }
        """
        """  resp:
                200():
                ""
                400():
                ""
                500():
                ""

        """
        intef = collections.interface("ChatCompletion", "InternalChatRequestWrapper")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("action", action)
        intef.update_body("biz_id", biz_id)
        intef.update_body("input", input)
        intef.update_body("model", model)
        intef.update_body("parent_turn_id", parent_turn_id)
        intef.update_body("session_id", session_id)
        intef.update_body("stream", stream)
        intef.update_body("know_ids", know_ids)
        intef.update_body("knowledge_config", knowledge_config)
        return intef.request() if sendRequest else intef

