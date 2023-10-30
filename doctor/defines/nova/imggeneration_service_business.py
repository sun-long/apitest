#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

from commonlib.decorator import wait
from defines.nova.api.imggeneration_service_swagger import ImggenerationSwaggerApi


"""
使用说明：


"""
Running = "RUNNING"
Success = "SUCCESS"
Failed = "FAILED"


def getStatusUntilRunningFunc(resp):
    """ 判断任务状态"""
    if resp.status_code == 200 and \
            resp.json_get("task.state") in [Running]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("task.state") in [Success, Failed]:
        raise Exception("task状态为%s!" % resp.json_get("task.state"))
    else:
        return False

def getStatusUntilSuccessFunc(resp):
    """ 判断任务状态"""
    if resp.status_code == 200 and \
            resp.json_get("task.state") in [Success]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("task.state") in [Failed]:
        raise Exception("task状态为%s!" % resp.json_get("task.state"))
    else:
        return False

def getStatusUntilFailedFunc(resp):
    """ 判断任务状态"""
    if resp.status_code == 200 and \
            resp.json_get("task.state") in [Failed]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("task.state") in [Success]:
        raise Exception("task状态为%s!" % resp.json_get("task.state"))
    else:
        return False

class ImggenerationSwaggerBusiness(ImggenerationSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(ImggenerationSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "Authorization" # 默认token的key
        self.TOKEN_VALUE = "Bearer %s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        time.sleep(1)

    @wait(timeout=180, interval=2, util_func=getStatusUntilRunningFunc, raise_exception=True)
    def getStatusUntilRunning(self, task_id):
        """ 查询任务直到running"""
        return self.maka_TaskGetGetApi(task_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getStatusUntilSuccessFunc, raise_exception=True)
    def getStatusUntilSuccess(self, task_id):
        """ 查询任务直到running"""
        return self.maka_TaskGetGetApi(task_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getStatusUntilFailedFunc, raise_exception=True)
    def getStatusUntilFailed(self, task_id):
        """ 查询任务直到running"""
        return self.maka_TaskGetGetApi(task_id, print_log=False)
    
    def commonchat_CommonChatCompletionPostApi(self, max_new_tokens=None, messages=None, model=None, n=None, repetition_penalty=None, stop=None, stream=None, temperature=None, top_p=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None,request_stream=False):
        """ commonchat接口，支持流式封装"""
        intef = super().commonchat_CommonChatCompletionPostApi(max_new_tokens=max_new_tokens, messages=messages, model=model,n=n,
                                             repetition_penalty=repetition_penalty, stop=stop,stream=stream, temperature=temperature, top_p=top_p,
                                            loginToken=loginToken, sendRequest=False, print_log=print_log, interface_desc=interface_desc)
        if request_stream is True:
            intef.set_stream_request(stream=True)
        else:
            intef.set_stream_request(stream=False)
        return intef.request() if sendRequest else intef

    def commonCompletion_CommonChatCompletionPostApi(self, max_new_tokens=None, prompt=None, model=None, n=None, repetition_penalty=None, stop=None, stream=None, temperature=None, top_p=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None,request_stream=False):
        """ commonCompletion接口，支持流式封装"""
        intef = super().completion_CompletionsPostApi(max_new_tokens=max_new_tokens, prompt=prompt, model=model,n=n,
                                             repetition_penalty=repetition_penalty, stop=stop,stream=stream, temperature=temperature, top_p=top_p,
                                            loginToken=loginToken, sendRequest=False, print_log=print_log, interface_desc=interface_desc)
        if request_stream is True:
            intef.set_stream_request(stream=True)
        else:
            intef.set_stream_request(stream=False)
        return intef.request() if sendRequest else intef
