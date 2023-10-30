#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class MingmouSwaggerApi(BaseApi):
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

    def NovaCvMingMou_Classify2dPostApi(self, model=None, file=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  2D 分类模型推理 """
        """  path: [post]/v1/cv/2d_classify API """
        """  body: 
                {
                    "model": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "results": [
                        {
                            "label": "",
                            "score": 0
                        }
                    ]
                }

        """
        intef = collections.interface("Mingmou", "NovaCvMingMou_Classify2d")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.files["file"] = file
        return intef.request() if sendRequest else intef

    def NovaCvMingMou_Detect2dPostApi(self, model=None, file=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  2D 检测模型推理 """
        """  path: [post]/v1/cv/2d_detect API """
        """  body: 
                {
                    "model": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "results": [
                        {
                            "bounding_box": [],
                            "label": "",
                            "score": 0
                        }
                    ]
                }

        """
        intef = collections.interface("Mingmou", "NovaCvMingMou_Detect2d")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.files["file"] = file
        return intef.request() if sendRequest else intef

    def NovaCvMingMou_DetectClassify2dPostApi(self, model=None, file=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  2D 检测+分类模型推理 """
        """  path: [post]/v1/cv/2d_detect_classify API """
        """  body: 
                {
                    "model": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "results": [
                        {
                            "bounding_box": [],
                            "result": [
                                {
                                    "label": "",
                                    "score": 0
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("Mingmou", "NovaCvMingMou_DetectClassify2d")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.files["file"] = file
        return intef.request() if sendRequest else intef

    def NovaCvMingMou_DetectSegment2dPostApi(self, model=None, file=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  2D 检测+分割模型推理 """
        """  path: [post]/v1/cv/2d_detect_segment API """
        """  body: 
                {
                    "model": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "results": [
                        {
                            "bounding_box": [],
                            "label": "",
                            "score": 0,
                            "segmentation": ""
                        }
                    ]
                }

        """
        intef = collections.interface("Mingmou", "NovaCvMingMou_DetectSegment2d")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.files["file"] = file
        return intef.request() if sendRequest else intef

    def NovaCvMingMou_Segment2dPostApi(self, model=None, file=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  2D 分割模型推理 """
        """  path: [post]/v1/cv/2d_segment API """
        """  body: 
                {
                    "model": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "results": [
                        {
                            "area": 0,
                            "bounding_box": [],
                            "crop_box": [],
                            "point_coords": [],
                            "predicted_iou": 0,
                            "score": 0,
                            "segmentation": ""
                        }
                    ]
                }

        """
        intef = collections.interface("Mingmou", "NovaCvMingMou_Segment2d")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.files["file"] = file
        return intef.request() if sendRequest else intef

    def NovaCvMingMou_Detect3dPostApi(self, model=None, file=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  3D 检测模型推理 """
        """  path: [post]/v1/cv/3d_detect API """
        """  body: 
                {
                    "model": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "results": [
                        {
                            "bounding_box": [],
                            "label": "",
                            "score": 0
                        }
                    ]
                }

        """
        intef = collections.interface("Mingmou", "NovaCvMingMou_Detect3d")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.files["file"] = file
        return intef.request() if sendRequest else intef

    def NovaCvMingMou_ListModelsGetApi(self, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询模型列表 """
        """  path: [get]/v1/cv/models API """
        """  params: 
                参数名称：type　类型：string　描述：模型类
        """
        """  resp:
                200(OK):
                {
                    "data": [
                        {
                            "created_at": "",
                            "id": "",
                            "object": "",
                            "owned_by": "",
                            "type": "",
                            "updated_at": ""
                        }
                    ],
                    "object": ""
                }

        """
        intef = collections.interface("Mingmou", "NovaCvMingMou_ListModels")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("type", type)
        return intef.request() if sendRequest else intef

    def NovaCvMingMou_GetModelGetApi(self, model_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询模型详情 """
        """  path: [get]/v1/cv/models/{model_id} API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "data": {
                        "created_at": "",
                        "id": "",
                        "object": "",
                        "owned_by": "",
                        "type": "",
                        "updated_at": ""
                    }
                }

        """
        intef = collections.interface("Mingmou", "NovaCvMingMou_GetModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("model_id", model_id)
        return intef.request() if sendRequest else intef

