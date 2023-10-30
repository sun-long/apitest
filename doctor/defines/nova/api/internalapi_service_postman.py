#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import base64
import os
import time

from commonlib.api_lib.base_api import BaseApi
from commonlib import time_utils, config
from core.pm_utils import load_postman

pm_collections = load_postman("nova")


class InternalPostmanApi(BaseApi):
    """ 内部接口"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        self.host = host
        self.ext_info = ext_info
        self.config_obj = config_obj
        self.token = token
        # self.host_map = self.readHostMap(pm_collections.name)
        self.host_map = None
        self.TOKEN_NAME = ""
        self.TOKEN_VALUE = "%s"  # token默认信息
        pm_collections.init(self, conf=config_obj, ext_info=ext_info)

    def InternalApi_NewSession(self, biz_id=None, label=None, system_prompt=None, user_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  新建会话"""
        """
        request:
        {
          "biz_id": 0,
          "label": "string",
          "system_prompt": [
            {
              "content": "",
              "role": "system"
            }
          ],
          "user_id": "string"
        }
        
        """
        intef = pm_collections.interface("internalChat", "新建会话")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.update_body("biz_id", biz_id)
        intef.update_body("label", label)
        intef.update_body("system_prompt", system_prompt)
        intef.update_body("user_id", user_id)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def InternalApi_Chat(self, action=None, biz_id=None, input=None, model=None, parent_turn_id=None, know_ids=None,
                         session_id=None, stream=None, loginToken=None, sendRequest=True, print_log=True,
                         interface_desc=None,request_stream=False, knowledge_config=None):
        """  有状态会话"""
        """
        request:
       {
          "action": "next",
          "biz_id": 0,
          "input": "你是谁",
          "model": "nova-ptc-yue-xl-v1",
          "parent_turn_id": "string",
          "session_id": "50f0f8388a4d000",
          "stream": false
        }
    
        """
        intef = pm_collections.interface("internalChat", "有状态会话")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.update_body("action", action)
        intef.update_body("biz_id", biz_id)
        intef.update_body("input", input)
        intef.update_body("model", model)
        intef.update_body("know_ids", know_ids)
        intef.update_body("parent_turn_id", parent_turn_id)
        intef.update_body("session_id", session_id)
        intef.update_body("stream", stream)
        intef.update_body("knowledge_config", knowledge_config)
        if request_stream is True:
            intef.set_stream_request(stream=True)
        else:
            intef.set_stream_request(stream=False)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def InternalApi_CompareRating(self, biz_id=None, compare_rating=None, session_id=None, source_turn_id=None, turn_id=None,
                          loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  重新生成回复评分"""
        """
        request:
        {
          "biz_id": 0,
          "compare_rating": "better",
          "session_id": "5082cec46c46000",
          "source_turn_id": "5082cec47046000_3",
          "turn_id": "5080d5f8f959000_2"
        }

        """
        intef = pm_collections.interface("internalChat", "重新生成回复评分")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.update_body("biz_id", biz_id)
        intef.update_body("compare_rating", compare_rating)
        intef.update_body("session_id", session_id)
        intef.update_body("source_turn_id", source_turn_id)
        intef.update_body("turn_id", turn_id)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def InternalApi_Feedback(self, biz_id=None, score=None, session_id=None, tag=None, turn_id=None,
                          loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  用户评价"""
        """
        request:
        {
          "biz_id": 0,
          "score": 0,
          "session_id": "5082cec46c46000",
          "tag": [
            "string"
          ],
          "turn_id": "5082cec47046000_2"
        }

        """
        intef = pm_collections.interface("internalChat", "用户评价")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.update_body("biz_id", biz_id)
        intef.update_body("score", score)
        intef.update_body("session_id", session_id)
        intef.update_body("tag", tag)
        intef.update_body("turn_id", turn_id)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def InternalApi_NewTopic(self, biz_id=None, session_id=None,
                             loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  话题切换"""
        """
        request:
        {
          "biz_id": 0,
          "session_id": "5082cec46c46000"
        }

        """
        intef = pm_collections.interface("internalChat", "话题切换")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.update_body("biz_id", biz_id)
        intef.update_body("session_id", session_id)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def InternalApi_RewriteOutput(self, biz_id=None, content=None,session_id=None, turn_id=None,
                             loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  修改答案"""
        """
        request:{
          "biz_id": 0,
          "content": "lalal",
          "session_id": "5082cec46c46000",
          "turn_id": "5082cec47046000_2"
        }
        """
        intef = pm_collections.interface("internalChat", "修改答案")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.update_body("biz_id", biz_id)
        intef.update_body("content", content)
        intef.update_body("session_id", session_id)
        intef.update_body("turn_id", turn_id)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def CodingGenerator_Chat(self, max_new_tokens=None, messages=None, model=None, stop=None, n=None,
                             stream=None, temperature=None,
                             loginToken=None, sendRequest=True, print_log=True, interface_desc=None, request_stream=False):
        """ 代码生成-chat"""
        """
        {
            "max_new_tokens": 100,
            "messages": [
                {
                    "content": "1",
                    "role": "assistant"
                },
                {
                    "content": "使用python写一个你好函数",
                    "role": "user"
                }
            ],
            "model": "novs-ptc-s-v1-code",
            "stop": "",
            "n":2,
            "stream": false,
            "temperature": 0.8
        }
        """
        intef = pm_collections.interface("internalChat", "代码生成")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.update_body("max_new_tokens", max_new_tokens)
        intef.update_body("messages", messages)
        intef.update_body("model", model)
        intef.update_body("stop", stop)
        intef.update_body("n", n)
        intef.update_body("stream", stream)
        intef.update_body("temperature", temperature)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        if request_stream is True:
            intef.set_stream_request(stream=True)
        else:
            intef.set_stream_request(stream=False)
        return intef.request() if sendRequest else intef

    def Multimodal_Chat(self, image=None, messages=None, model=None,max_new_tokens=None,repetition_penalty=None,
                             top_p=None, temperature=None,stream=None,
                             loginToken=None, sendRequest=True, print_log=True, interface_desc=None,request_stream=False):
        """ 多模态-chat"""
        """
            {
            "image": "",
            "messages": [
                {
                    "role": "user",
                    "content": "你好"
                },
                {
                    "role": "assistant",
                    "content": "你好"
                },
                {
                    "role": "user",
                    "content": "图片中有什么"
                }
            ],
            "model": "nova-ptc-xs-v1",
            "max_new_tokens": 1024,
            "repetition_penalty": 1.05,
            "temperature": 0.8,
            "top_p": 0.7,
            "stream": false
        }
        """
        intef = pm_collections.interface("internalChat", "多模态")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.update_body("image", self.imageToBase64(image))
        intef.update_body("messages", messages)
        intef.update_body("model", model)
        intef.update_body("max_new_tokens", max_new_tokens)
        intef.update_body("repetition_penalty", repetition_penalty)
        intef.update_body("temperature", temperature)
        intef.update_body("top_p", top_p)
        intef.update_body("stream", stream)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        if request_stream is True:
            intef.set_stream_request(stream=True)
        else:
            intef.set_stream_request(stream=False)    
        return intef.request() if sendRequest else intef