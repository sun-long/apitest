#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明:
"""

collections = load_swagger("belt")


class CtidServiceSwaggerApi(BaseApi):
    """ web api 接口"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        self.host = host
        self.ext_info = ext_info
        self.config_obj = config_obj
        self.token = token
        self.host_map = self.readHostMap(collections.name)
        self.TOKEN_NAME = ""
        self.TOKEN_VALUE = "%s"  # tokenĬ����Ϣ
        collections.init(self, conf=config_obj, ext_info=ext_info)

    def genPostMan(self):
        """生成postman接口文件"""
        self.ext_info.isRequestOpened = True
        self.genPostManFromSwagger(collections)

    def CTIDService_DetectFacesPostApi(self, bizSerialNo=None, photoData=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  人脸检测 """
        """  path: [post]/face-detect API """
        """  body: 
                {
                    "bizSerialNo": "",
                    "photoData": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "bizSerialNo": "",
                    "costTime": "",
                    "endTime": "",
                    "errCode": "",
                    "facelist": [
                        {
                            "lefttopx": "",
                            "lefttopy": "",
                            "rightbottomx": "",
                            "rightbottomy": ""
                        }
                    ],
                    "productName": "",
                    "startTime": "",
                    "version": "",
                    "workerTitle": ""
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
        intef = collections.interface("ctid-service", "CTIDService_DetectFaces")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bizSerialNo", bizSerialNo)
        intef.update_body("photoData", photoData)
        return intef.request() if sendRequest else intef

    def CTIDService_CheckQualityPostApi(self, bizSerialNo=None, photoData=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """人脸质量检测"""
        """  path: [post]/face-quality-check API """
        """  body: 
                {
                    "bizSerialNo": "",
                    "photoData": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "bizSerialNo": "",
                    "costTime": "",
                    "endTime": "",
                    "errCode": "",
                    "productName": "",
                    "qualityInfo": {
                        "eyeSize": "",
                        "faceBlur": "",
                        "faceBright": "",
                        "faceOcclusion": "",
                        "posePitch": "",
                        "poseRoll": "",
                        "poseYaw": ""
                    },
                    "qualityScore": "",
                    "startTime": "",
                    "version": "",
                    "workerTitle": ""
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
        intef = collections.interface("ctid-service", "CTIDService_CheckQuality")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bizSerialNo", bizSerialNo)
        intef.update_body("photoData", photoData)
        return intef.request() if sendRequest else intef

    def CTIDService_CompareFeaturesPostApi(self, bizSerialNo=None, feature1=None, feature2=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  face1:1 人脸特征提取 """
        """  path: [post]/feature-compare API """
        """  body: 
                {
                    "bizSerialNo": "",
                    "feature1": "",
                    "feature2": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "bizSerialNo": "",
                    "costTime": "",
                    "endTime": "",
                    "errCode": "",
                    "faceEngineName": "",
                    "faceEngineVersion": "",
                    "feature": "",
                    "photoAuthResult": "",
                    "photoCompareScore": "",
                    "startTime": "",
                    "thresholdE3": "",
                    "thresholdE4": "",
                    "workerTitle": ""
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
        intef = collections.interface("ctid-service", "CTIDService_CompareFeatures")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bizSerialNo", bizSerialNo)
        intef.update_body("feature1", feature1)
        intef.update_body("feature2", feature2)
        return intef.request() if sendRequest else intef

    def CTIDService_ExtractFeaturePostApi(self, bizSerialNo=None, photoData=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  图像特征提取"""
        """  path: [post]/feature-extract API """
        """  body: 
                {
                    "bizSerialNo": "",
                    "photoData": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "bizSerialNo": "",
                    "costTime": "",
                    "endTime": "",
                    "errCode": "",
                    "faceEngineName": "",
                    "faceEngineVersion": "",
                    "feature": "",
                    "photoAuthResult": "",
                    "photoCompareScore": "",
                    "startTime": "",
                    "thresholdE3": "",
                    "thresholdE4": "",
                    "workerTitle": ""
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
        intef = collections.interface("ctid-service", "CTIDService_ExtractFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bizSerialNo", bizSerialNo)
        intef.update_body("photoData", photoData)
        return intef.request() if sendRequest else intef

    def CTIDService_CheckHealthGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """心跳检测"""
        """  path: [get]/hello-world API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "errCode": "",
                    "errDesc": "",
                    "timeStamp": "",
                    "workerTitle": ""
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
        intef = collections.interface("ctid-service", "CTIDService_CheckHealth")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def CTIDService_CompareImageAndFeaturePostApi(self, bizSerialNo=None, feature=None, photoData=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  图像和特征1:1比对 """
        """  path: [post]/photo-feature-verify API """
        """  body: 
                {
                    "bizSerialNo": "",
                    "feature": "",
                    "photoData": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "bizSerialNo": "",
                    "costTime": "",
                    "endTime": "",
                    "errCode": "",
                    "faceEngineName": "",
                    "faceEngineVersion": "",
                    "feature": "",
                    "photoAuthResult": "",
                    "photoCompareScore": "",
                    "startTime": "",
                    "thresholdE3": "",
                    "thresholdE4": "",
                    "workerTitle": ""
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
        intef = collections.interface("ctid-service", "CTIDService_CompareImageAndFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bizSerialNo", bizSerialNo)
        intef.update_body("feature", feature)
        intef.update_body("photoData", photoData)
        return intef.request() if sendRequest else intef

    def CTIDService_CompareAndExtractFeaturePostApi(self, bizSerialNo=None, photoData1=None, photoData2=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  两张图像1:1、特征比对"""
        """  path: [post]/two-photos-feature-verify API """
        """  body: 
                {
                    "bizSerialNo": "",
                    "photoData1": "",
                    "photoData2": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "bizSerialNo": "",
                    "costTime": "",
                    "endTime": "",
                    "errCode": "",
                    "faceEngineName": "",
                    "faceEngineVersion": "",
                    "feature": "",
                    "photoAuthResult": "",
                    "photoCompareScore": "",
                    "startTime": "",
                    "thresholdE3": "",
                    "thresholdE4": "",
                    "workerTitle": ""
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
        intef = collections.interface("ctid-service", "CTIDService_CompareAndExtractFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bizSerialNo", bizSerialNo)
        intef.update_body("photoData1", photoData1)
        intef.update_body("photoData2", photoData2)
        return intef.request() if sendRequest else intef

    def CTIDService_CompareImagesPostApi(self, bizSerialNo=None, photoData1=None, photoData2=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  两张人脸1:1比对"""
        """  path: [post]/two-photos-verify API """
        """  body: 
                {
                    "bizSerialNo": "",
                    "photoData1": "",
                    "photoData2": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "bizSerialNo": "",
                    "costTime": "",
                    "endTime": "",
                    "errCode": "",
                    "faceEngineName": "",
                    "faceEngineVersion": "",
                    "feature": "",
                    "photoAuthResult": "",
                    "photoCompareScore": "",
                    "startTime": "",
                    "thresholdE3": "",
                    "thresholdE4": "",
                    "workerTitle": ""
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
        intef = collections.interface("ctid-service", "CTIDService_CompareImages")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bizSerialNo", bizSerialNo)
        intef.update_body("photoData1", photoData1)
        intef.update_body("photoData2", photoData2)
        return intef.request() if sendRequest else intef

