#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class ImggenerationSwaggerApi(BaseApi):
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

    def maka_TaskListGetApi(self, task_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  list generation_task """
        """  path: [get]/v1/imgen/internal/generation_tasks API """
        """  params: 
                参数名称：task_ids　类型：array　描述：required get tasks by task_ids, this length must be in [1,50]
        """
        """  resp:
                200(任务列表):
                {
                    "tasks": [
                        {
                            "result": [
                                {
                                    "error": "",
                                    "index": 0,
                                    "raw": "",
                                    "sensitive_rating": 0,
                                    "small": ""
                                }
                            ],
                            "state": "",
                            "state_message": "",
                            "task_id": ""
                        }
                    ]
                }

        """
        intef = collections.interface("ImgGeneration", "maka_TaskList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("task_ids", task_ids)
        return intef.request() if sendRequest else intef

    def maka_TaskSubmitPostApi(self, cfg_scale=None, controlnet_configs=None, height=None, image_strength=None, init_image_url=None, lora_configs=None, model_id=None, neg_prompt=None, prompt=None, sampler=None, samples=None, seed=None, steps=None, vae=None, watermark_config=None, width=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  image generation """
        """  path: [post]/v1/imgen/internal/generation_tasks API """
        """  body: 
                {
                    "cfg_scale": 0,
                    "controlnet_configs": [
                        {
                            "canny_high_thresthold": 0,
                            "canny_low_thresthold": 0,
                            "guidance_end": 0,
                            "guidance_start": 0,
                            "img_url": "",
                            "mlsd_distance_threshold": 0,
                            "mlsd_value_thresthold": 0,
                            "mode": "",
                            "pre_processor": "",
                            "reference_style_fidelity": 0,
                            "resize_mode": "",
                            "tile_down_sample_rate": 0,
                            "type": "",
                            "weight": 0
                        }
                    ],
                    "height": 0,
                    "image_strength": 0,
                    "init_image_url": "",
                    "lora_configs": [
                        {
                            "merge_weight": 0,
                            "model_id": ""
                        }
                    ],
                    "model_id": "",
                    "neg_prompt": "",
                    "prompt": "",
                    "sampler": {},
                    "samples": 0,
                    "seed": 0,
                    "steps": 0,
                    "vae": "",
                    "watermark_config": {},
                    "width": 0
                }
        """
        """  resp:
                200(响应):
                {
                    "task_id": ""
                }

        """
        intef = collections.interface("ImgGeneration", "maka_TaskSubmit")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("cfg_scale", cfg_scale)
        intef.update_body("controlnet_configs", controlnet_configs)
        intef.update_body("height", height)
        intef.update_body("image_strength", image_strength)
        intef.update_body("init_image_url", init_image_url)
        intef.update_body("lora_configs", lora_configs)
        intef.update_body("model_id", model_id)
        intef.update_body("neg_prompt", neg_prompt)
        intef.update_body("prompt", prompt)
        intef.update_body("sampler", sampler)
        intef.update_body("samples", samples)
        intef.update_body("seed", seed)
        intef.update_body("steps", steps)
        intef.update_body("vae", vae)
        intef.update_body("watermark_config", watermark_config)
        intef.update_body("width", width)
        return intef.request() if sendRequest else intef

    def maka_TaskGetGetApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  get generation_task by id """
        """  path: [get]/v1/imgen/internal/generation_tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200(任务详情):
                {
                    "task": {}
                }

        """
        intef = collections.interface("ImgGeneration", "maka_TaskGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def maka_Img2txtPostApi(self, image=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  image generation """
        """  path: [post]/v1/imgen/internal/img2txt API """
        """  body: 
                {
                    "image": {
                        "filename": "",
                        "header": {
                            "additionalProp1": [],
                            "additionalProp2": [],
                            "additionalProp3": []
                        },
                        "size": 0
                    }
                }
        """
        """  resp:
                200(响应):
                {
                    "prompt": ""
                }

        """
        intef = collections.interface("ImgGeneration", "maka_Img2txt")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        return intef.request() if sendRequest else intef

    def commonchat_CommonChatCompletionPostApi(self, max_new_tokens=None, messages=None, model=None, n=None, repetition_penalty=None, stop=None, stream=None, temperature=None, top_p=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  common chat """
        """  path: [post]/v1/llm/chat-completions API """
        """  body: 
                {
                    "max_new_tokens": 0,
                    "messages": [
                        {
                            "content": "",
                            "role": ""
                        }
                    ],
                    "model": "",
                    "n": 0,
                    "repetition_penalty": 0,
                    "stop": "",
                    "stream": false,
                    "temperature": 0,
                    "top_p": 0
                }
        """
        """  resp:
                200(stream response):
                {
                    "data": {
                        "choices": [
                            {
                                "delta": "",
                                "finish_reason": "",
                                "index": 0,
                                "role": ""
                            }
                        ],
                        "id": "",
                        "usage": {
                            "completion_tokens": 0,
                            "prompt_tokens": 0,
                            "total_tokens": 0
                        }
                    },
                    "status": {
                        "code": 0,
                        "message": ""
                    }
                }
                default(normal response):
                {
                    "data": {
                        "choices": [
                            {
                                "finish_reason": "",
                                "index": 0,
                                "message": "",
                                "role": ""
                            }
                        ],
                        "id": "",
                        "usage": {
                            "completion_tokens": 0,
                            "prompt_tokens": 0,
                            "total_tokens": 0
                        }
                    }
                }

        """
        intef = collections.interface("ImgGeneration", "commonchat_CommonChatCompletion")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("max_new_tokens", max_new_tokens)
        intef.update_body("messages", messages)
        intef.update_body("model", model)
        intef.update_body("n", n)
        intef.update_body("repetition_penalty", repetition_penalty)
        intef.update_body("stop", stop)
        intef.update_body("stream", stream)
        intef.update_body("temperature", temperature)
        intef.update_body("top_p", top_p)
        return intef.request() if sendRequest else intef

    def codechat_CodeChatCompletionPostApi(self, max_new_tokens=None, messages=None, model=None, n=None, stop=None, stream=None, temperature=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None, request_stream=False):
        """  code chat """
        """  path: [post]/v1/llm/code/chat-completions API """
        """  body: 
                {
                    "max_new_tokens": 0,
                    "messages": [
                        {
                            "content": "",
                            "role": ""
                        }
                    ],
                    "model": "",
                    "n": 0,
                    "stop": "",
                    "stream": false,
                    "temperature": 0
                }
        """
        """  resp:
                200(stream response):
                {
                    "data": {
                        "choices": [
                            {
                                "delta": "",
                                "finish_reason": "",
                                "index": 0,
                                "role": ""
                            }
                        ],
                        "id": "",
                        "usage": {
                            "completion_tokens": 0,
                            "prompt_tokens": 0,
                            "total_tokens": 0
                        }
                    },
                    "status": {
                        "code": 0,
                        "message": ""
                    }
                }
                default(normal response):
                {
                    "data": {
                        "choices": [
                            {
                                "finish_reason": "",
                                "index": 0,
                                "message": "",
                                "role": ""
                            }
                        ],
                        "id": "",
                        "usage": {
                            "completion_tokens": 0,
                            "prompt_tokens": 0,
                            "total_tokens": 0
                        }
                    }
                }

        """
        intef = collections.interface("ImgGeneration", "codechat_CodeChatCompletion")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("max_new_tokens", max_new_tokens)
        intef.update_body("messages", messages)
        intef.update_body("model", model)
        intef.update_body("n", n)
        intef.update_body("stop", stop)
        intef.update_body("stream", stream)
        intef.update_body("temperature", temperature)
        if request_stream is True:
            intef.set_stream_request(stream=True)
        else:
            intef.set_stream_request(stream=False)
        return intef.request() if sendRequest else intef

    def completion_CompletionsPostApi(self, max_new_tokens=None, model=None, n=None, prompt=None, repetition_penalty=None, stop=None, stream=None, temperature=None, top_p=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  completions """
        """  path: [post]/v1/llm/completions API """
        """  body: 
                {
                    "max_new_tokens": 0,
                    "model": "",
                    "n": 0,
                    "prompt": "",
                    "repetition_penalty": 0,
                    "stop": "",
                    "stream": false,
                    "temperature": 0,
                    "top_p": 0
                }
        """
        """  resp:
                200(stream response):
                {
                    "data": {
                        "choices": [
                            {
                                "delta": "",
                                "finish_reason": "",
                                "index": 0
                            }
                        ],
                        "id": "",
                        "usage": {
                            "completion_tokens": 0,
                            "prompt_tokens": 0,
                            "total_tokens": 0
                        }
                    },
                    "status": {
                        "code": 0,
                        "message": ""
                    }
                }
                default(normal response):
                {
                    "data": {
                        "choices": [
                            {
                                "finish_reason": "",
                                "index": 0,
                                "text": ""
                            }
                        ],
                        "id": "",
                        "usage": {
                            "completion_tokens": 0,
                            "prompt_tokens": 0,
                            "total_tokens": 0
                        }
                    }
                }

        """
        intef = collections.interface("ImgGeneration", "completion_Completions")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("max_new_tokens", max_new_tokens)
        intef.update_body("model", model)
        intef.update_body("n", n)
        intef.update_body("prompt", prompt)
        intef.update_body("repetition_penalty", repetition_penalty)
        intef.update_body("stop", stop)
        intef.update_body("stream", stream)
        intef.update_body("temperature", temperature)
        intef.update_body("top_p", top_p)
        return intef.request() if sendRequest else intef

    def multimodal_MultimodalChatPostApi(self, image=None, max_new_tokens=None, messages=None, model=None, repetition_penalty=None, session_id=None, stream=None, temperature=None, top_p=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  多模态 """
        """  path: [post]/v1/llm/internal/multi-chat API """
        """  body: 
                {
                    "image": "",
                    "max_new_tokens": 0,
                    "messages": [
                        {
                            "content": "",
                            "role": ""
                        }
                    ],
                    "model": "",
                    "repetition_penalty": 0,
                    "session_id": "",
                    "stream": false,
                    "temperature": 0,
                    "top_p": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "data": {
                        "choices": [
                            {
                                "finish_reason": "",
                                "message": ""
                            }
                        ],
                        "id": "",
                        "usage": {
                            "completion_tokens": 0,
                            "prompt_tokens": 0,
                            "total_tokens": 0
                        }
                    }
                }

        """
        intef = collections.interface("ImgGeneration", "multimodal_MultimodalChat")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("max_new_tokens", max_new_tokens)
        intef.update_body("messages", messages)
        intef.update_body("model", model)
        intef.update_body("repetition_penalty", repetition_penalty)
        intef.update_body("session_id", session_id)
        intef.update_body("stream", stream)
        intef.update_body("temperature", temperature)
        intef.update_body("top_p", top_p)
        return intef.request() if sendRequest else intef

    def roleplay_RoleplayCompletionPostApi(self, beam_width=None, bot_setting=None, mask_sensitive_info=None, messages=None, model=None, reply_constraints=None, session_id=None, tokens_to_generate=None, traceID=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  拟人对话 """
        """  path: [post]/v1/llm/internal/role-play/chat-completions API """
        """  body: 
                {
                    "beam_width": 0,
                    "bot_setting": [
                        {
                            "bot_name": "",
                            "content": ""
                        }
                    ],
                    "mask_sensitive_info": false,
                    "messages": [
                        {
                            "sender_name": "",
                            "sender_type": "",
                            "text": ""
                        }
                    ],
                    "model": "",
                    "reply_constraints": {},
                    "session_id": "",
                    "tokens_to_generate": 0,
                    "traceID": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "base_resp": {},
                    "choices": [
                        {
                            "finish_reason": "",
                            "index": 0,
                            "messages": [
                                {
                                    "sender_name": "",
                                    "sender_type": "",
                                    "text": ""
                                }
                            ]
                        }
                    ],
                    "created": 0,
                    "id": "",
                    "model": "",
                    "reply": "",
                    "usage": {
                        "completion_tokens": 0,
                        "prompt_tokens": 0,
                        "total_tokens": 0
                    }
                }

        """
        intef = collections.interface("ImgGeneration", "roleplay_RoleplayCompletion")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("beam_width", beam_width)
        intef.update_body("bot_setting", bot_setting)
        intef.update_body("mask_sensitive_info", mask_sensitive_info)
        intef.update_body("messages", messages)
        intef.update_body("model", model)
        intef.update_body("reply_constraints", reply_constraints)
        intef.update_body("session_id", session_id)
        intef.update_body("tokens_to_generate", tokens_to_generate)
        intef.update_body("traceID", traceID)
        intef.update_body("initmacy", 3) # TODO 临时添加 亲密度
        intef.update_body("text_type", 1) # TODO 临时添加 1位写信
        return intef.request() if sendRequest else intef

