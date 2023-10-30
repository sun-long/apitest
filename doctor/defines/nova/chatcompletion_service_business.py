#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time
from commonlib.decorator import wait
from defines.nova.api.chatcompletion_service_swagger import ChatcompletionSwaggerApi


"""
使用说明：


"""

from core.pm_utils import load_postman

collections_pm = load_postman("nova")


class ChatcompletionSwaggerBusiness(ChatcompletionSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(ChatcompletionSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Sensenova-Signature" # 默认token的key
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        # 限流1qps    
        time.sleep(1)    

    def ChatCompletionsRequestWrapperPostApi(self, know_ids=None, max_new_tokens=None, messages=None, model=None,knowledge_config=None,
                                             repetition_penalty=None, stream=None, temperature=None, top_p=None,
                                             user=None, loginToken=None, sendRequest=True,request_stream=False,
                                             print_log=True, interface_desc=None):
        """ 会话接口，支持流式封装"""
        intef = super().ChatCompletionsRequestWrapperPostApi(know_ids=know_ids, max_new_tokens=max_new_tokens, messages=messages, model=model,
                                             repetition_penalty=repetition_penalty, stream=stream, temperature=temperature, top_p=top_p,
                                             user=user, loginToken=loginToken, sendRequest=False, knowledge_config=knowledge_config,
                                             print_log=print_log, interface_desc=interface_desc)
        if request_stream is True:
            intef.set_stream_request(stream=True)
        else:
            intef.set_stream_request(stream=False)
        return intef.request() if sendRequest else intef
    
    def ChatRequestWrapperPostApi(self, knowledge_config=None, action=None, content=None, know_ids=None, model=None, session_id=None, stream=None, loginToken=None, sendRequest=True,request_stream=False, print_log=True, interface_desc=None):
        """  有状态对话. 支持流式封装"""
        intef = super().ChatRequestWrapperPostApi(action=action, content=content, know_ids=know_ids, model=model,
                                                  knowledge_config=knowledge_config,
                                                  session_id=session_id, stream=stream, loginToken=loginToken,
                                                  sendRequest=False, print_log=True, interface_desc=None)
        if request_stream is True:
            intef.set_stream_request(stream=True)
        else:
            intef.set_stream_request(stream=False)
        return intef.request() if sendRequest else intef