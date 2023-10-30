#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class PlaygroundSwaggerApi(BaseApi):
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

    def PlaygroundService_ExampleCreatePostApi(self, example=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/console/v1/example/create API """
        """  body: 
                {
                    "example": {
                        "category": "",
                        "chat": {
                            "api_request": {
                                "know_ids": [],
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
                                "top_p": 0
                            },
                            "api_response": {
                                "sample": ""
                            }
                        },
                        "desc": "",
                        "kb_info": {
                            "content": "",
                            "know_id": ""
                        },
                        "kind": "[Chat]Chat",
                        "name": "",
                        "order": 0,
                        "tags": {
                            "tag_names": []
                        },
                        "thumb": ""
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "example_id": ""
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
        intef = collections.interface("Playground", "PlaygroundService_ExampleCreate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("example", example)
        return intef.request() if sendRequest else intef

    def PlaygroundService_ExampleGenerateSampleCodePostApi(self, chat=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  action=ExampleGenerateSampleCode """
        """  path: [post]/console/v1/example/generate_code API """
        """  body: 
                {
                    "chat": {
                        "know_ids": [],
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
                        "top_p": 0
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "codes": [
                        {
                            "code": "",
                            "lang": "[CURL]CURL/PYTHON"
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
        intef = collections.interface("Playground", "PlaygroundService_ExampleGenerateSampleCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("chat", chat)
        return intef.request() if sendRequest else intef

    def PlaygroundService_ExampleGetGetApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  action=ExampleGet """
        """  path: [get]/console/v1/example/get API """
        """  params: 
                参数名称：id　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "example": {
                        "category": "",
                        "chat": {
                            "api_request": {
                                "know_ids": [],
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
                                "top_p": 0
                            },
                            "api_response": {
                                "sample": ""
                            }
                        },
                        "desc": "",
                        "id": "",
                        "kb_info": {
                            "content": "",
                            "know_id": ""
                        },
                        "kind": "[Chat]Chat",
                        "name": "",
                        "order": 0,
                        "sample_codes": [
                            {
                                "code": "",
                                "lang": "[CURL]CURL/PYTHON"
                            }
                        ],
                        "tags": [
                            {
                                "display_name": "",
                                "name": ""
                            }
                        ],
                        "thumb": ""
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
        intef = collections.interface("Playground", "PlaygroundService_ExampleGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("id", id)
        return intef.request() if sendRequest else intef

    def PlaygroundService_ExampleListGetApi(self, example_category_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  action = ExampleList """
        """  path: [get]/console/v1/example/list API """
        """  params: 
                参数名称：example_category_id　类型：string　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "examples": [
                        {
                            "category": "",
                            "chat": {
                                "api_request": {
                                    "know_ids": [],
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
                                    "top_p": 0
                                },
                                "api_response": {
                                    "sample": ""
                                }
                            },
                            "desc": "",
                            "id": "",
                            "kb_info": {
                                "content": "",
                                "know_id": ""
                            },
                            "kind": "[Chat]Chat",
                            "name": "",
                            "order": 0,
                            "sample_codes": [
                                {
                                    "code": "",
                                    "lang": "[CURL]CURL/PYTHON"
                                }
                            ],
                            "tags": [
                                {
                                    "display_name": "",
                                    "name": ""
                                }
                            ],
                            "thumb": ""
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
        intef = collections.interface("Playground", "PlaygroundService_ExampleList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("example_category_id", example_category_id)
        return intef.request() if sendRequest else intef

    def PlaygroundService_ExampleUpdatePostApi(self, id=None, example=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/console/v1/example/update API """
        """  body: 
                {
                    "example": {
                        "category": "",
                        "chat": {
                            "api_request": {
                                "know_ids": [],
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
                                "top_p": 0
                            },
                            "api_response": {
                                "sample": ""
                            }
                        },
                        "desc": "",
                        "kb_info": {
                            "content": "",
                            "know_id": ""
                        },
                        "kind": "[Chat]Chat",
                        "name": "",
                        "order": 0,
                        "tags": {
                            "tag_names": []
                        },
                        "thumb": ""
                    },
                    "id": ""
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
        intef = collections.interface("Playground", "PlaygroundService_ExampleUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("example", example)
        return intef.request() if sendRequest else intef

    def PlaygroundService_ExampleCategoryCreatePostApi(self, example_category=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/console/v1/example_category/create API """
        """  body: 
                {
                    "example_category": {
                        "display_name": "",
                        "name": "",
                        "order": 0
                    }
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "example_category_id": ""
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
        intef = collections.interface("Playground", "PlaygroundService_ExampleCategoryCreate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("example_category", example_category)
        return intef.request() if sendRequest else intef

    def PlaygroundService_ExampleCategoryListGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  action=ExampleCategoryList """
        """  path: [get]/console/v1/example_category/list API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "example_categorys": [
                        {
                            "display_name": "",
                            "example_category_id": "",
                            "name": "",
                            "order": 0
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
        intef = collections.interface("Playground", "PlaygroundService_ExampleCategoryList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def PlaygroundService_ExampleTagCreatePostApi(self, name=None, display_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/console/v1/example_tag/create API """
        """  body: 
                {
                    "display_name": "",
                    "name": ""
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
        intef = collections.interface("Playground", "PlaygroundService_ExampleTagCreate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("display_name", display_name)
        return intef.request() if sendRequest else intef

    def PlaygroundService_ExamleTagListGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [get]/console/v1/example_tag/list API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "tags": [
                        {
                            "display_name": "",
                            "name": ""
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
        intef = collections.interface("Playground", "PlaygroundService_ExamleTagList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

