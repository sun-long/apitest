#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class ArgusdatacenterSwaggerApi(BaseApi):
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

    def DC_GetOriginMetaInfoGetApi(self, ak=None, store_id=None, device_id=None, camera_id=None, person_id=None, request_id=None, start_time=None, end_time=None, page_number=None, page_size=None, mis_request_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  origin_meta_info API """
        """  path: [get]/sensego/datacenter/unicron/meta/origin_meta_info API """
        """  params: 
                *参数名称：ak　类型：string　描述：ak
                *参数名称：store_id　类型：string　描述：store_id
                *参数名称：device_id　类型：string　描述：device_id
                *参数名称：camera_id　类型：string　描述：camera_id
                *参数名称：person_id　类型：string　描述：person_id
                *参数名称：request_id　类型：string　描述：request_id
                *参数名称：start_time　类型：integer　描述：起始时间
                *参数名称：end_time　类型：integer　描述：终止时间
                *参数名称：page_number　类型：integer　描述：从第几页开始取
                *参数名称：page_size　类型：integer　描述：取多少个
                *参数名称：mis_request_ids　类型：array　描述：这些requestid的数据不会被查出
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "results": [
                        {
                            "age": 0,
                            "body_id": "",
                            "camera_id": "",
                            "camera_name": "",
                            "device_id": "",
                            "face_id": "",
                            "gender": "",
                            "group_id": "",
                            "person_id": "",
                            "plate_image_bucket": "",
                            "plate_image_url": "",
                            "product_line": "",
                            "request_id": "",
                            "result_type": "",
                            "snap_image_bucket": "",
                            "snap_image_url": "",
                            "source_group": "",
                            "time": 0
                        }
                    ],
                    "total": 0
                }

        """
        intef = collections.interface("argusDatacenter", "DC_GetOriginMetaInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ak", ak)
        intef.update_params("store_id", store_id)
        intef.update_params("device_id", device_id)
        intef.update_params("camera_id", camera_id)
        intef.update_params("person_id", person_id)
        intef.update_params("request_id", request_id)
        intef.update_params("start_time", start_time)
        intef.update_params("end_time", end_time)
        intef.update_params("page_number", page_number)
        intef.update_params("page_size", page_size)
        intef.update_params("mis_request_ids", mis_request_ids)
        return intef.request() if sendRequest else intef

