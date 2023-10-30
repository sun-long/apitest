#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class StatSwaggerApi(BaseApi):
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

    def NovaStatService_GetVpStatUsageGetApi(self, vp_id=None, start_time=None, end_time=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取Vp统计用量
route: prefix=console action=GetVpStatUsa... """
        """  path: [get]/console/v1/vp_stat_usage API """
        """  params: 
                参数名称：vp_id　类型：string　描述：vp 编号
                参数名称：start_time　类型：string　描述：起始时间
                参数名称：end_time　类型：string　描述：结束时
        """
        """  resp:
                200(A successful response.):
                {
                    "daily_usages": [
                        {
                            "usage": "",
                            "usage_time": ""
                        }
                    ],
                    "history_accum_usage": "",
                    "realtime_usage": ""
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
        intef = collections.interface("Stat", "NovaStatService_GetVpStatUsage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("vp_id", vp_id)
        intef.update_params("start_time", start_time)
        intef.update_params("end_time", end_time)
        return intef.request() if sendRequest else intef

    def NovaStatService_ListVpsGetApi(self, spu_code=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取计费点
route: prefix=console action=ListVps version... """
        """  path: [get]/console/v1/vps API """
        """  params: 
                参数名称：spu_code　类型：string　描述：SPU cod
        """
        """  resp:
                200(A successful response.):
                {
                    "vps": [
                        {
                            "vp_id": "",
                            "vp_name": ""
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
        intef = collections.interface("Stat", "NovaStatService_ListVps")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("spu_code", spu_code)
        return intef.request() if sendRequest else intef

