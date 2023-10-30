#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class EmbeddingSwaggerApi(BaseApi):
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

    def EmbeddingService_EmbeddingPostApi(self, model=None, input=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """   """
        """  path: [post]/v1/llm/embeddings API """
        """  body: 
                {
                    "input": [],
                    "model": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "embeddings": [
                        {
                            "embedding": [],
                            "index": 0,
                            "status_code": 0,
                            "status_message": ""
                        }
                    ],
                    "usage": {
                        "prompt_tokens": 0,
                        "total_tokens": 0
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
        intef = collections.interface("Embedding", "EmbeddingService_Embedding")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.update_body("input", input)
        return intef.request() if sendRequest else intef

