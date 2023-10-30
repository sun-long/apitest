#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class ImgfinetunemanagerSwaggerApi(BaseApi):
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

    def ImgFinetuneManager_CreateFinetuneTaskPostApi(self, suffix=None, model=None, display_name=None, description=None, trigger_word=None, main_object=None, task_type=None, datasets=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建finetune任务 """
        """  path: [post]/v1/imgen/internal/finetune API """
        """  body: 
                {
                    "datasets": [],
                    "description": "",
                    "display_name": "",
                    "main_object": "",
                    "model": "",
                    "suffix": "",
                    "task_type": "[NORMAL]NORMAL/VIP",
                    "trigger_word": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "task_id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("ImgFinetuneManager", "ImgFinetuneManager_CreateFinetuneTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("suffix", suffix)
        intef.update_body("model", model)
        intef.update_body("display_name", display_name)
        intef.update_body("description", description)
        intef.update_body("trigger_word", trigger_word)
        intef.update_body("main_object", main_object)
        intef.update_body("task_type", task_type)
        intef.update_body("datasets", datasets)
        return intef.request() if sendRequest else intef

    def ImgFinetuneManager_CancelFinetuneTaskPostApi(self, task_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  取消finetune任务，仅支持取消PENDING状态的任务 """
        """  path: [post]/v1/imgen/internal/finetune/cancel API """
        """  body: 
                {
                    "task_id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("ImgFinetuneManager", "ImgFinetuneManager_CancelFinetuneTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task_id", task_id)
        return intef.request() if sendRequest else intef

    def ImgFinetuneManager_UpdateFinetuneTaskProgressPostApi(self, task_id=None, versionid=None, training_progress=None, state=None, ckpt_path=None, basemodel_path=None, error_code=None, error_msg=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新finetune任务状态，为训练服务回调接口 """
        """  path: [post]/v1/imgen/internal/finetune/progress API """
        """  body: 
                {
                    "basemodel_path": "",
                    "ckpt_path": "",
                    "error_code": "",
                    "error_msg": "",
                    "state": "",
                    "task_id": "",
                    "training_progress": 0,
                    "versionid": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("ImgFinetuneManager", "ImgFinetuneManager_UpdateFinetuneTaskProgress")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task_id", task_id)
        intef.update_body("versionid", versionid)
        intef.update_body("training_progress", training_progress)
        intef.update_body("state", state)
        intef.update_body("ckpt_path", ckpt_path)
        intef.update_body("basemodel_path", basemodel_path)
        intef.update_body("error_code", error_code)
        intef.update_body("error_msg", error_msg)
        return intef.request() if sendRequest else intef

    def ImgFinetuneManager_GetFinetuneTaskGetApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取指定任务信息 """
        """  path: [get]/v1/imgen/internal/finetune/{task_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "task": {
                        "created_at": "",
                        "datasets": [],
                        "description": "",
                        "display_name": "",
                        "finetune_model": "",
                        "main_object": "",
                        "model": "",
                        "state": "[UNKNOWN]UNKNOWN/PENDING/RUNNING/DONE/ERROR/CANCELED",
                        "task_id": "",
                        "task_type": "[NORMAL]NORMAL/VIP",
                        "training_progress": 0,
                        "trigger_word": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("ImgFinetuneManager", "ImgFinetuneManager_GetFinetuneTask")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def ImgFinetuneManager_ListFinetuneTasksGetApi(self, paging_offset=None, paging_limit=None, paging_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取当前用户所有finetune任务列表 """
        """  path: [get]/v1/imgen/internal/finetunes API """
        """  params: 
                参数名称：paging.offset　类型：integer　描述：偏移量
                参数名称：paging.limit　类型：integer　描述：每页数量
                参数名称：paging.total　类型：integer　描述：总数
        """
        """  resp:
                200(A successful response.):
                {
                    "paging": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    },
                    "tasks": [
                        {
                            "created_at": "",
                            "datasets": [],
                            "description": "",
                            "display_name": "",
                            "finetune_model": "",
                            "main_object": "",
                            "model": "",
                            "state": "[UNKNOWN]UNKNOWN/PENDING/RUNNING/DONE/ERROR/CANCELED",
                            "task_id": "",
                            "task_type": "[NORMAL]NORMAL/VIP",
                            "training_progress": 0,
                            "trigger_word": ""
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("ImgFinetuneManager", "ImgFinetuneManager_ListFinetuneTasks")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("paging.offset", paging_offset)
        intef.update_params("paging.limit", paging_limit)
        intef.update_params("paging.total", paging_total)
        return intef.request() if sendRequest else intef

    def ImgFinetuneManager_HealthGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/v1/imgen/internal/health API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {}
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "@type": ""
                        }
                    ],
                    "message": ""
                }

        """
        intef = collections.interface("ImgFinetuneManager", "ImgFinetuneManager_Health")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

