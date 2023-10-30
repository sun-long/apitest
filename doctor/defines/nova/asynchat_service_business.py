#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

from commonlib.decorator import wait
from defines.nova.api.asynchat_service_swagger import AsynchatSwaggerApi


"""
使用说明：


"""


def ChatCompletionsRetrieveReadyFunc(resp):
    """ 判断文件状态"""
    if resp.status_code == 200:
        return True
    elif resp.status_code == 202:
        return False
    else:
        raise Exception("status_code:%s!" % resp.status_code)


class AsynchatSwaggerBusiness(AsynchatSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(AsynchatSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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
        time.sleep(0.5)

    @wait(timeout=60, interval=2, util_func=ChatCompletionsRetrieveReadyFunc, raise_exception=True)
    def ChatCompletionsRetrieveReady(self, request_id):
        """ 等待Retrieve Ready"""
        return self.ChatCompletionsRetrievePostApi(request_id=request_id, print_log=False)
