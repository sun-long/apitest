#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.nova.api.imgfinetunemanager_service_swagger import ImgfinetunemanagerSwaggerApi


"""
使用说明：


"""

def getFinetuneTaskUntilRunningFunc(resp):
    """ 判断fineturn运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("task.state") in ["RUNNING", "DONE"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("task.state") in ["CANCELED", "ERROR"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("task.state"))
    else:
        return False

def getFinetuneTaskUntilDONEFunc(resp):
    """ 判断fineturn运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("task.state") in ["DONE"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("task.state") in ["CANCELED", "ERROR"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("task.state"))
    else:
        return False

def getFinetuneTaskUntilCANCELEDFunc(resp):
    """ 判断fineturn运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("task.state") in ["CANCELED"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("task.state") in ["DONE", "ERROR"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("task.state"))
    else:
        return False

def getFinetuneTaskUntilERRORFunc(resp):
    """ 判断fineturn运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("task.state") in ["ERROR"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("task.state") in ["DONE", "CANCELED"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("task.state"))
    else:
        return False

class ImgfinetunemanagerSwaggerBusiness(ImgfinetunemanagerSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(ImgfinetunemanagerSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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

    @wait(timeout=600, interval=2, util_func=getFinetuneTaskUntilRunningFunc, raise_exception=True)
    def getFinetuneTaskUntilRunning(self, task_id):
        """ 查询finetune任务直到任务运行起来"""
        return self.ImgFinetuneManager_GetFinetuneTaskGetApi(task_id, print_log=False)

    @wait(timeout=600, interval=2, util_func=getFinetuneTaskUntilDONEFunc, raise_exception=True)
    def getFinetuneTaskUntilDone(self, task_id):
        """ 查询finetune任务直到任务运行起来"""
        return self.ImgFinetuneManager_GetFinetuneTaskGetApi(task_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getFinetuneTaskUntilCANCELEDFunc, raise_exception=True)
    def getFinetuneTaskUntilCANCELED(self, task_id):
        """ 查询finetune任务直到任务运行起来"""
        return self.ImgFinetuneManager_GetFinetuneTaskGetApi(task_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getFinetuneTaskUntilERRORFunc, raise_exception=True)
    def getFinetuneTaskUntilERROR(self, task_id):
        """ 查询finetune任务直到任务运行起来"""
        return self.ImgFinetuneManager_GetFinetuneTaskGetApi(task_id, print_log=False)