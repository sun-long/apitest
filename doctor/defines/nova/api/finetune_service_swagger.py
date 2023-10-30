#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class FinetuneSwaggerApi(BaseApi):
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

    def FinetuneManager_ListServingsGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListServings 获取模型推理任务 """
        """  path: [get]/v1/llm/fine-tune/servings API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "jobs": [
                        {
                            "config": {
                                "run_time": 0
                            },
                            "created_at": "",
                            "end_time": "",
                            "id": "",
                            "model": "",
                            "start_time": "",
                            "status": "[UNKNOWN]UNKNOWN/SUBMITTED/PENDING/RUNNING/RESTARTING/CANCELLED/SUCCEEDED/FAILED/EXPIRED",
                            "updated_at": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_ListServings")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def FinetuneManager_CreateServingsPostApi(self, model=None, config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CreateServings 创建模型推理任务 """
        """  path: [post]/v1/llm/fine-tune/servings API """
        """  body: 
                {
                    "config": {
                        "run_time": 0
                    },
                    "model": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "job": {
                        "config": {
                            "run_time": 0
                        },
                        "created_at": "",
                        "end_time": "",
                        "id": "",
                        "model": "",
                        "start_time": "",
                        "status": "[UNKNOWN]UNKNOWN/SUBMITTED/PENDING/RUNNING/RESTARTING/CANCELLED/SUCCEEDED/FAILED/EXPIRED",
                        "updated_at": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_CreateServings")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.update_body("config", config)
        return intef.request() if sendRequest else intef

    def FinetuneManager_CheckModelRunningGetApi(self, model_internal_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CheckModelRunning 内部使用，获取模型推理任务是否正在运行 """
        """  path: [get]/v1/llm/fine-tune/servings/internal/{model_internal_id}/is_running API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "running": false
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
        intef = collections.interface("Finetune", "FinetuneManager_CheckModelRunning")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("model_internal_id", model_internal_id)
        return intef.request() if sendRequest else intef

    def FinetuneManager_GetServingsGetApi(self, serving_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetServings 获取模型推理任务 """
        """  path: [get]/v1/llm/fine-tune/servings/{serving_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "job": {
                        "config": {
                            "run_time": 0
                        },
                        "created_at": "",
                        "end_time": "",
                        "id": "",
                        "model": "",
                        "start_time": "",
                        "status": "[UNKNOWN]UNKNOWN/SUBMITTED/PENDING/RUNNING/RESTARTING/CANCELLED/SUCCEEDED/FAILED/EXPIRED",
                        "updated_at": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_GetServings")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("serving_id", serving_id)
        return intef.request() if sendRequest else intef

    def FinetuneManager_DeleteServingsDeleteApi(self, serving_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteServings 删除模型推理任务 """
        """  path: [delete]/v1/llm/fine-tune/servings/{serving_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_DeleteServings")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("serving_id", serving_id)
        return intef.request() if sendRequest else intef

    def FinetuneManager_CancelServingsPostApi(self, serving_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CancelServings 取消模型推理任务 """
        """  path: [post]/v1/llm/fine-tune/servings/{serving_id}/cancel API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "job": {
                        "config": {
                            "run_time": 0
                        },
                        "created_at": "",
                        "end_time": "",
                        "id": "",
                        "model": "",
                        "start_time": "",
                        "status": "[UNKNOWN]UNKNOWN/SUBMITTED/PENDING/RUNNING/RESTARTING/CANCELLED/SUCCEEDED/FAILED/EXPIRED",
                        "updated_at": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_CancelServings")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("serving_id", serving_id)
        return intef.request() if sendRequest else intef

    def FinetuneManager_RelaunchServingsPostApi(self, serving_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  RelaunchServings 重启模型推理任务 """
        """  path: [post]/v1/llm/fine-tune/servings/{serving_id}/relaunch API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "job": {
                        "config": {
                            "run_time": 0
                        },
                        "created_at": "",
                        "end_time": "",
                        "id": "",
                        "model": "",
                        "start_time": "",
                        "status": "[UNKNOWN]UNKNOWN/SUBMITTED/PENDING/RUNNING/RESTARTING/CANCELLED/SUCCEEDED/FAILED/EXPIRED",
                        "updated_at": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_RelaunchServings")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("serving_id", serving_id)
        return intef.request() if sendRequest else intef

    def FinetuneManager_ListFinetuneJobGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListFinetuneJob 获取 fine-tune 任务 """
        """  path: [get]/v1/llm/fine-tunes API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "jobs": [
                        {
                            "created_at": "",
                            "fine_tuned_model": "",
                            "hyperparams": {
                                "learning_rate": 0,
                                "lora_alpha": 0,
                                "lora_dropout": 0,
                                "lora_rank": 0,
                                "lr_scheduler_type": "",
                                "max_steps": 0,
                                "method": "",
                                "modules_to_save": "",
                                "save_steps": 0,
                                "warmup_ratio": 0,
                                "weight_decay": 0
                            },
                            "id": "",
                            "model": "",
                            "object": "",
                            "status": "[UNKNOWN]UNKNOWN/SUBMITTED/PENDING/RUNNING/RESTARTING/CANCELLED/SUCCEEDED/FAILED/EXPIRED",
                            "training_file": "",
                            "updated_at": ""
                        }
                    ],
                    "object": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_ListFinetuneJob")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def FinetuneManager_CreateFinetuneJobPostApi(self, training_file=None, model=None, suffix=None, hyperparams=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CreateFinetuneJob 创建 fine-tune 任务 """
        """  path: [post]/v1/llm/fine-tunes API """
        """  body: 
                {
                    "hyperparams": {
                        "learning_rate": 0,
                        "lora_alpha": 0,
                        "lora_dropout": 0,
                        "lora_rank": 0,
                        "lr_scheduler_type": "",
                        "max_steps": 0,
                        "method": "",
                        "modules_to_save": "",
                        "save_steps": 0,
                        "warmup_ratio": 0,
                        "weight_decay": 0
                    },
                    "model": "",
                    "suffix": "",
                    "training_file": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "job": {
                        "created_at": "",
                        "fine_tuned_model": "",
                        "hyperparams": {
                            "learning_rate": 0,
                            "lora_alpha": 0,
                            "lora_dropout": 0,
                            "lora_rank": 0,
                            "lr_scheduler_type": "",
                            "max_steps": 0,
                            "method": "",
                            "modules_to_save": "",
                            "save_steps": 0,
                            "warmup_ratio": 0,
                            "weight_decay": 0
                        },
                        "id": "",
                        "model": "",
                        "object": "",
                        "status": "[UNKNOWN]UNKNOWN/SUBMITTED/PENDING/RUNNING/RESTARTING/CANCELLED/SUCCEEDED/FAILED/EXPIRED",
                        "training_file": "",
                        "updated_at": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_CreateFinetuneJob")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("training_file", training_file)
        intef.update_body("model", model)
        intef.update_body("suffix", suffix)
        intef.update_body("hyperparams", hyperparams)
        return intef.request() if sendRequest else intef

    def FinetuneManager_GetFinetuneJobGetApi(self, fine_tune_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetFinetuneJob 获取 fine-tune 任务 """
        """  path: [get]/v1/llm/fine-tunes/{fine_tune_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "job": {
                        "created_at": "",
                        "fine_tuned_model": "",
                        "hyperparams": {
                            "learning_rate": 0,
                            "lora_alpha": 0,
                            "lora_dropout": 0,
                            "lora_rank": 0,
                            "lr_scheduler_type": "",
                            "max_steps": 0,
                            "method": "",
                            "modules_to_save": "",
                            "save_steps": 0,
                            "warmup_ratio": 0,
                            "weight_decay": 0
                        },
                        "id": "",
                        "model": "",
                        "object": "",
                        "status": "[UNKNOWN]UNKNOWN/SUBMITTED/PENDING/RUNNING/RESTARTING/CANCELLED/SUCCEEDED/FAILED/EXPIRED",
                        "training_file": "",
                        "updated_at": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_GetFinetuneJob")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("fine_tune_id", fine_tune_id)
        return intef.request() if sendRequest else intef

    def FinetuneManager_DeleteFinetuneJobDeleteApi(self, fine_tune_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteFinetuneJob 删除 fine-tune 任务 """
        """  path: [delete]/v1/llm/fine-tunes/{fine_tune_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_DeleteFinetuneJob")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("fine_tune_id", fine_tune_id)
        return intef.request() if sendRequest else intef

    def FinetuneManager_CancelFinetuneJobPostApi(self, fine_tune_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CancelFinetuneJob 取消 fine-tune 任务 """
        """  path: [post]/v1/llm/fine-tunes/{fine_tune_id}/cancel API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                {
                    "error": {
                        "code": 0,
                        "details": [
                            {
                                "@type": ""
                            }
                        ],
                        "message": ""
                    },
                    "job": {
                        "created_at": "",
                        "fine_tuned_model": "",
                        "hyperparams": {
                            "learning_rate": 0,
                            "lora_alpha": 0,
                            "lora_dropout": 0,
                            "lora_rank": 0,
                            "lr_scheduler_type": "",
                            "max_steps": 0,
                            "method": "",
                            "modules_to_save": "",
                            "save_steps": 0,
                            "warmup_ratio": 0,
                            "weight_decay": 0
                        },
                        "id": "",
                        "model": "",
                        "object": "",
                        "status": "[UNKNOWN]UNKNOWN/SUBMITTED/PENDING/RUNNING/RESTARTING/CANCELLED/SUCCEEDED/FAILED/EXPIRED",
                        "training_file": "",
                        "updated_at": ""
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
        intef = collections.interface("Finetune", "FinetuneManager_CancelFinetuneJob")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("fine_tune_id", fine_tune_id)
        return intef.request() if sendRequest else intef

