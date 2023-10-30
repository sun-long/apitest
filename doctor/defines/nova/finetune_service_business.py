#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

from commonlib.decorator import wait
from defines.nova.api.finetune_service_swagger import FinetuneSwaggerApi


"""
使用说明：


"""

def getServingTaskUntilFailedFunc(resp):
    """ 判断serving运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("job.status") in ["FAILED"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("job.status") in ["CANCELLED",  "EXPIRED"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("job.status"))
    else:
        return False

def getServingTaskUntilRunningFunc(resp):
    """ 判断serving运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("job.status") in ["RUNNING",]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("job.status") in ["CANCELLED", "FAILED", "EXPIRED"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("job.status"))
    else:
        return False

def getServingTaskUntilExpiredFunc(resp):
    """ 判断serving运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("job.status") in ["EXPIRED"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("job.status") in ["FAILED", "CANCELLED"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("job.status"))
    else:
        return False


def getServingTaskUntilCancelledFunc(resp):
    """ 判断serving运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("job.status") in ["CANCELLED"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("job.status") in ["FAILED", "EXPIRED"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("job.status"))
    else:
        return False

def getFinetuneTaskUntilPendingFunc(resp):
    """ 判断fineturn运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("job.status") in ["PENDING", ]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("job.status") in ["CANCELLED", "FAILED", "SUCCEEDED", "RUNNING"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("job.status"))
    else:
        return False

def getFinetuneTaskUntilRunningFunc(resp):
    """ 判断fineturn运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("job.status") in ["RUNNING", "SUCCEEDED"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("job.status") in ["CANCELLED", "FAILED"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("job.status"))
    else:
        return False

def getFinetuneTaskUntilCancelledFunc(resp):
    """ 判断fineturn运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("job.status") in ["CANCELLED"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("job.status") in ["FAILED"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("job.status"))
    else:
        return False

def getFinetuneTaskUntilSucceededFunc(resp):
    """ 判断fineturn运行的方法"""
    if resp.status_code == 200 and \
            resp.json_get("job.status") in ["SUCCEEDED"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("job.status") in ["FAILED"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("job.status"))
    else:
        return False

def getFinetuneTaskUntilFailedFunc(resp):
    if resp.status_code == 200 and \
            resp.json_get("job.status") in ["FAILED"]:
        return True
    elif resp.status_code == 200 and \
            resp.json_get("job.status") in ["SUCCEEDED"]:
        raise Exception("finetune任务状态为%s!" % resp.json_get("job.status"))
    else:
        return False

def relaunchServingsFunc(resp):
    if resp.status_code == 200:
        return True
    else:
        return False

def deleteServingsFunc(resp):
    if resp.status_code == 200 or resp.status_code == 404:
        return True
    else:
        return False

class FinetuneSwaggerBusiness(FinetuneSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(FinetuneSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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

    @wait(timeout=180, interval=2, util_func=getServingTaskUntilFailedFunc, raise_exception=True)
    def getServingTaskUntilFailed(self, serving_id):
        """ 查询serving任务直到任务失败"""
        return self.FinetuneManager_GetServingsGetApi(serving_id, print_log=False)

    @wait(timeout=600, interval=2, util_func=getServingTaskUntilRunningFunc, raise_exception=True)
    def getServingTaskUntilRunning(self, serving_id):
        """ 查询serving任务直到任务运行起来"""
        return self.FinetuneManager_GetServingsGetApi(serving_id, print_log=False)

    @wait(timeout=60*65, interval=2, util_func=getServingTaskUntilExpiredFunc, raise_exception=True)
    def getServingTaskUntilExpired(self, serving_id):
        """ 查询Serving任务直到任务超时"""
        return self.FinetuneManager_GetServingsGetApi(serving_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getServingTaskUntilCancelledFunc, raise_exception=True)
    def getServingTaskUntilCancelled(self, serving_id):
        """ 查询finetune任务直到任务取消"""
        return self.FinetuneManager_GetServingsGetApi(serving_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getFinetuneTaskUntilRunningFunc, raise_exception=True)
    def getFinetuneTaskUntilRunning(self, finetune_id):
        """ 查询finetune任务直到任务运行起来"""
        return self.FinetuneManager_GetFinetuneJobGetApi(finetune_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getFinetuneTaskUntilPendingFunc, raise_exception=True)
    def getFinetuneTaskUntilPending(self, finetune_id):
        """ 查询finetune任务直到任务pending"""
        return self.FinetuneManager_GetFinetuneJobGetApi(finetune_id, print_log=False)


    @wait(timeout=180, interval=2, util_func=getFinetuneTaskUntilCancelledFunc, raise_exception=True)
    def getFinetuneTaskUntilCancelled(self, finetune_id):
        """ 查询finetune任务直到任务取消"""
        return self.FinetuneManager_GetFinetuneJobGetApi(finetune_id, print_log=False)

    @wait(timeout=60*30, interval=2, util_func=getFinetuneTaskUntilSucceededFunc, raise_exception=True)
    def getFinetuneTaskUntilSucceeded(self, finetune_id):
        """ 查询finetune任务直到任务取消"""
        return self.FinetuneManager_GetFinetuneJobGetApi(finetune_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=getFinetuneTaskUntilFailedFunc, raise_exception=True)
    def getFinetuneTaskUntilFailed(self, finetune_id):
        """ 查询finetune任务直到任务失败"""
        return self.FinetuneManager_GetFinetuneJobGetApi(finetune_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=relaunchServingsFunc, raise_exception=True)
    def relaunchServings(self, serving_id):
        """ 重启重试"""
        return self.FinetuneManager_RelaunchServingsPostApi(serving_id, print_log=False)

    @wait(timeout=180, interval=2, util_func=deleteServingsFunc, raise_exception=True)
    def deleteServings(self, serving_id):
        """ 重启重试"""
        return self.FinetuneManager_DeleteServingsDeleteApi(serving_id)

    def createFinetuneTask(self, training_file=None, model=None, suffix=None, hyperparams=None, loginToken=None,
                          sendRequest=True, print_log=True, interface_desc=None, is_delete=True, wait_running=True,
                          wait_success=False):
        """ 创建finetune任务"""
        time.sleep(30)
        if not hyperparams:
            hyperparams = {"training": {"max_steps": 3}}
        resp = self.FinetuneManager_CreateFinetuneJobPostApi(training_file=training_file, model=model, suffix=suffix,
                                                                    hyperparams=hyperparams, loginToken=loginToken,
                                                                    sendRequest=sendRequest, print_log=print_log,
                                                                    interface_desc=interface_desc)
        finetune_id = resp.json_get("job.id") if sendRequest else None
        # 添加clear up
        def clearUp():
            self.cancelFineturnTask(finetune_id)
            self.FinetuneManager_DeleteFinetuneJobDeleteApi(finetune_id)

        if self.ext_info and is_delete and finetune_id:
            self.ext_info.addAfterFunc(clearUp)

        if wait_running and finetune_id:
            self.getFinetuneTaskUntilRunning(finetune_id)
        if wait_success and finetune_id:
            self.getFinetuneTaskUntilSucceeded(finetune_id)
        return resp

    def createServingTask(self, model=None, config=None, loginToken=None,
                          sendRequest=True, print_log=True, interface_desc=None, is_delete=True, wait_running=True):
        """ 创建serving任务"""
        resp = self.FinetuneManager_CreateServingsPostApi(model=model, config=config, loginToken=loginToken,
                                                                 sendRequest=sendRequest, print_log=print_log,
                                                                 interface_desc=interface_desc)
        serving_id = resp.json_get("job.id") if sendRequest else None

        # 添加clear up
        def clearUp():
            self.cancelServingTask(serving_id)
            self.FinetuneManager_DeleteServingsDeleteApi(serving_id)

        if self.ext_info and is_delete and serving_id:
            self.ext_info.addAfterFunc(clearUp)

        if wait_running and serving_id:
            self.getServingTaskUntilRunning(serving_id)
        return resp

    def cancelFineturnTask(self, finetune_id):
        """ 取消finetune任务"""
        resp = self.FinetuneManager_GetFinetuneJobGetApi(finetune_id)
        if resp.status_code == 404:
            return
        status = resp.json_get("job.status")
        if status in ["RUNNING", "SUBMITTED", "PENDING", "RESTARTING"]:
            resp = self.FinetuneManager_CancelFinetuneJobPostApi(finetune_id)
            self.getFinetuneTaskUntilCancelled(finetune_id)

    def cancelServingTask(self, serving_id):
        """ 取消serving任务"""
        resp = self.FinetuneManager_GetServingsGetApi(serving_id)
        if resp.status_code == 404:
            return
        status = resp.json_get("job.status")
        if status in ["RUNNING", "SUBMITTED", "PENDING", "RESTARTING"]:
            resp = self.FinetuneManager_CancelServingsPostApi(serving_id)
            self.getServingTaskUntilCancelled(serving_id)