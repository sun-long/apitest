#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class RasclusterSwaggerApi(BaseApi):
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

    def RasCluster_GetClustersGetApi(self, siteIds=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetClusters 外网使用，返回的 cluster 信息不包含 ingress 地址.
rou... """
        """  path: [get]/v1/clusters API """
        """  params: 
                参数名称：siteIds　类型：array　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "center": {
                        "id": "",
                        "infraClusterId": "",
                        "name": "",
                        "privateIngress": "",
                        "publicIngress": "",
                        "siteId": "",
                        "type": "[CT_UNKNOWN]CT_UNKNOWN/CT_CENTER/CT_EDGE"
                    },
                    "edges": [
                        {
                            "id": "",
                            "infraClusterId": "",
                            "name": "",
                            "privateIngress": "",
                            "publicIngress": "",
                            "siteId": "",
                            "type": "[CT_UNKNOWN]CT_UNKNOWN/CT_CENTER/CT_EDGE"
                        }
                    ],
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
        intef = collections.interface("rasCluster", "RasCluster_GetClusters")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("siteIds", siteIds)
        return intef.request() if sendRequest else intef

