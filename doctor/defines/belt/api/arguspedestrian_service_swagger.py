#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class ArguspedestrianSwaggerApi(BaseApi):
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

    def Pedestrain_RecognizePostApi(self, associates=None, bg_image_upload=None, body=None, device=None, face=None, faceTrack=None, flag=None, image=None, location=None, meta=None, misc=None, monitor=None, relation=None, timestamp=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  pedestrian API """
        """  path: [post]/argus/v1/recognize/pedestrian API """
        """  body: 
                {
                    "associates": [
                        {
                            "begin_timestamp": 0,
                            "end_timestamp": 0,
                            "score": 0,
                            "target_id": ""
                        }
                    ],
                    "bg_image_upload": false,
                    "body": {},
                    "device": {},
                    "face": {},
                    "faceTrack": {},
                    "flag": 0,
                    "image": {},
                    "location": {},
                    "meta": {},
                    "misc": {
                        "access_timestamp": 0,
                        "callback": "",
                        "error_code": 0,
                        "error_msg": "",
                        "extra_type": "",
                        "replay_timestamp": 0
                    },
                    "monitor": {},
                    "relation": {},
                    "timestamp": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "error_code": 0,
                    "error_msg": "",
                    "extra": {
                        "bg_oss_url": ""
                    },
                    "request_id": ""
                }

        """
        intef = collections.interface("argusPedestrian", "Pedestrain_Recognize")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("associates", associates)
        intef.update_body("bg_image_upload", bg_image_upload)
        intef.update_body("body", body)
        intef.update_body("device", device)
        intef.update_body("face", face)
        intef.update_body("faceTrack", faceTrack)
        intef.update_body("flag", flag)
        intef.update_body("image", image)
        intef.update_body("location", location)
        intef.update_body("meta", meta)
        intef.update_body("misc", misc)
        intef.update_body("monitor", monitor)
        intef.update_body("relation", relation)
        intef.update_body("timestamp", timestamp)
        return intef.request() if sendRequest else intef

