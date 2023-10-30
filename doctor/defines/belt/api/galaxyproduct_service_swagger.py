#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class GalaxyproductSwaggerApi(BaseApi):
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

    def modifyProduct_1PostApi(self, externalBizFrom=None, fileNameList=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取图片下载链接 """
        """  path: [post]/api/v1/product/urls/download API """
        """  body: 
                {
                    "externalBizFrom": "",
                    "fileNameList": []
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "productUrls": []
                    },
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "modifyProduct_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("fileNameList", fileNameList)
        return intef.request() if sendRequest else intef

    def getProductUploadUrlPostApi(self, externalBizFrom=None, fileNameList=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取物品上传链接 """
        """  path: [post]/api/v1/product/urls/upload API """
        """  body: 
                {
                    "externalBizFrom": "",
                    "fileNameList": []
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "productUrls": []
                    },
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "getProductUploadUrl")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("fileNameList", fileNameList)
        return intef.request() if sendRequest else intef

    def addProductPostApi(self, externalBizFrom=None, productIdList=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  添加产品 """
        """  path: [post]/api/v1/products/add API """
        """  body: 
                {
                    "externalBizFrom": "",
                    "productIdList": []
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "addProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("productIdList", productIdList)
        return intef.request() if sendRequest else intef

    def batchDelProductPostApi(self, externalBizFrom=None, productIdList=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  批量删除物品 """
        """  path: [post]/api/v1/products/batch/del API """
        """  body: 
                {
                    "externalBizFrom": "",
                    "productIdList": []
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "batchDelProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("productIdList", productIdList)
        return intef.request() if sendRequest else intef

    def editBusinessCodePutApi(self, productId, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  编辑businessCode """
        """  path: [put]/api/v1/products/edit/businessCode/{productId} API """
        """  body: 
                {}
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "编辑businessCode")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("productId", productId)
        return intef.request() if sendRequest else intef

    def getProductListPostApi(self, auditStatus=None, dateEnd=None, dateStart=None, externalBizFrom=None, name=None, page=None, pageOrderList=None, productId=None, sceneType=None, size=None, tenantBusinessCode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询产品列表 """
        """  path: [post]/api/v1/products/list API """
        """  body: 
                {
                    "auditStatus": 0,
                    "dateEnd": "",
                    "dateStart": "",
                    "externalBizFrom": "",
                    "name": "",
                    "page": 0,
                    "pageOrderList": [
                        {
                            "orderField": "",
                            "orderType": ""
                        }
                    ],
                    "productId": "",
                    "sceneType": "",
                    "size": 0,
                    "tenantBusinessCode": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "empty": false,
                        "list": [
                            {
                                "auditStatus": 0,
                                "barCode": "",
                                "brand": "",
                                "chooseFlag": 0,
                                "createTime": 0,
                                "effectStartTime": 0,
                                "height": "",
                                "imgList": [
                                    {
                                        "fileName": "",
                                        "imageType": 0,
                                        "md5": ""
                                    }
                                ],
                                "length": "",
                                "name": "",
                                "packing": "",
                                "productId": "",
                                "remark": "",
                                "tag": "",
                                "tenantBusinessCode": "",
                                "urls": [],
                                "weight": "",
                                "width": ""
                            }
                        ],
                        "page": 0,
                        "size": 0,
                        "total": 0,
                        "totalPage": 0
                    },
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "getProductList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("auditStatus", auditStatus)
        intef.update_body("dateEnd", dateEnd)
        intef.update_body("dateStart", dateStart)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("name", name)
        intef.update_body("page", page)
        intef.update_body("pageOrderList", pageOrderList)
        intef.update_body("productId", productId)
        intef.update_body("sceneType", sceneType)
        intef.update_body("size", size)
        intef.update_body("tenantBusinessCode", tenantBusinessCode)
        return intef.request() if sendRequest else intef

    def editBusinessCodeUsingPUTPutApi(self, scene, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  手动同步失败的sku """
        """  path: [put]/api/v1/products/manual/sync/{scene} API """
        """  body: 
                {}
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "editBusinessCodeUsingPUT")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("scene", scene)
        return intef.request() if sendRequest else intef

    def modifyProductPostApi(self, barCode=None, brand=None, externalBizFrom=None, height=None, imgList=None, length=None, name=None, packing=None, productId=None, tag=None, tenantBusinessCode=None, weight=None, width=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  修改产品 """
        """  path: [post]/api/v1/products/modify API """
        """  body: 
                {
                    "barCode": "",
                    "brand": "",
                    "externalBizFrom": "",
                    "height": "",
                    "imgList": [
                        {
                            "fileName": "",
                            "imageType": 0,
                            "md5": ""
                        }
                    ],
                    "length": "",
                    "name": "",
                    "packing": "",
                    "productId": "",
                    "tag": "",
                    "tenantBusinessCode": "",
                    "weight": "",
                    "width": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "modifyProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("barCode", barCode)
        intef.update_body("brand", brand)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("height", height)
        intef.update_body("imgList", imgList)
        intef.update_body("length", length)
        intef.update_body("name", name)
        intef.update_body("packing", packing)
        intef.update_body("productId", productId)
        intef.update_body("tag", tag)
        intef.update_body("tenantBusinessCode", tenantBusinessCode)
        intef.update_body("weight", weight)
        intef.update_body("width", width)
        return intef.request() if sendRequest else intef

    def registerProductPostApi(self, barCode=None, brand=None, createTenantId=None, createUserId=None, externalBizFrom=None, height=None, imgList=None, length=None, name=None, packing=None, tag=None, tenantBusinessCode=None, tenantScene=None, weight=None, width=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  注册产品 """
        """  path: [post]/api/v1/products/register API """
        """  body: 
                {
                    "barCode": "",
                    "brand": "",
                    "createTenantId": "",
                    "createUserId": 0,
                    "externalBizFrom": "",
                    "height": "",
                    "imgList": [
                        {
                            "fileName": "",
                            "imageType": 0,
                            "md5": ""
                        }
                    ],
                    "length": "",
                    "name": "",
                    "packing": "",
                    "tag": "",
                    "tenantBusinessCode": "",
                    "tenantScene": "",
                    "weight": "",
                    "width": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "registerProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("barCode", barCode)
        intef.update_body("brand", brand)
        intef.update_body("createTenantId", createTenantId)
        intef.update_body("createUserId", createUserId)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("height", height)
        intef.update_body("imgList", imgList)
        intef.update_body("length", length)
        intef.update_body("name", name)
        intef.update_body("packing", packing)
        intef.update_body("tag", tag)
        intef.update_body("tenantBusinessCode", tenantBusinessCode)
        intef.update_body("tenantScene", tenantScene)
        intef.update_body("weight", weight)
        intef.update_body("width", width)
        return intef.request() if sendRequest else intef

    def resetSkuImagePutApi(self, productId, scene, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  重置imageId """
        """  path: [put]/api/v1/products/reset/image/{productId}/{scene} API """
        """  body: 
                {}
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "resetSkuImage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("productId", productId)
        intef.set_path_param("scene", scene)
        return intef.request() if sendRequest else intef

    def getProductListByScenePostApi(self, brand=None, dateEnd=None, dateStart=None, externalBizFrom=None, packing=None, page=None, pageOrderList=None, searchKey=None, size=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询产品仓库列表 """
        """  path: [post]/api/v1/products/scene/list API """
        """  body: 
                {
                    "brand": "",
                    "dateEnd": "",
                    "dateStart": "",
                    "externalBizFrom": "",
                    "packing": "",
                    "page": 0,
                    "pageOrderList": [
                        {
                            "orderField": "",
                            "orderType": ""
                        }
                    ],
                    "searchKey": "",
                    "size": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "empty": false,
                        "list": [
                            {
                                "auditStatus": 0,
                                "barCode": "",
                                "brand": "",
                                "chooseFlag": 0,
                                "createTime": 0,
                                "effectStartTime": 0,
                                "height": "",
                                "imgList": [
                                    {
                                        "fileName": "",
                                        "imageType": 0,
                                        "md5": ""
                                    }
                                ],
                                "length": "",
                                "name": "",
                                "packing": "",
                                "productId": "",
                                "remark": "",
                                "tag": "",
                                "tenantBusinessCode": "",
                                "urls": [],
                                "weight": "",
                                "width": ""
                            }
                        ],
                        "page": 0,
                        "size": 0,
                        "total": 0,
                        "totalPage": 0
                    },
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "getProductListByScene")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("brand", brand)
        intef.update_body("dateEnd", dateEnd)
        intef.update_body("dateStart", dateStart)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("packing", packing)
        intef.update_body("page", page)
        intef.update_body("pageOrderList", pageOrderList)
        intef.update_body("searchKey", searchKey)
        intef.update_body("size", size)
        return intef.request() if sendRequest else intef

    def getProductDetailGetApi(self, productId, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询产品详情 """
        """  path: [get]/api/v1/products/{productId} API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "auditStatus": 0,
                        "barCode": "",
                        "brand": "",
                        "categoryId": 0,
                        "effectEndTime": 0,
                        "effectStartTime": 0,
                        "height": "",
                        "imgList": [
                            {
                                "fileName": "",
                                "imageType": 0,
                                "md5": ""
                            }
                        ],
                        "imgSetting": "",
                        "length": "",
                        "name": "",
                        "packing": "",
                        "productId": "",
                        "recommendId": 0,
                        "remark": "",
                        "remoteUrls": [],
                        "sceneType": "",
                        "size": "",
                        "tag": "",
                        "tenantBusinessCode": "",
                        "weight": "",
                        "width": ""
                    },
                    "message": "",
                    "success": false
                }
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "getProductDetail")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("productId", productId)
        return intef.request() if sendRequest else intef

    def delProductDeleteApi(self, productId, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除物品 """
        """  path: [delete]/api/v1/products/{productId} API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "message": "",
                    "success": false
                }
                204(No Content):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""

        """
        intef = collections.interface("galaxyProduct", "delProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("productId", productId)
        return intef.request() if sendRequest else intef

    def transactProductAsyncPostApi(self, algorithmType=None, callBackUrl=None, deviceId=None, externalBizFrom=None, orderId=None, skuCompose=None, videoSet=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  异步交易 """
        """  path: [post]/openapi/v1/product/async/transact API """
        """  body: 
                {
                    "algorithmType": 0,
                    "callBackUrl": "",
                    "deviceId": "",
                    "externalBizFrom": "",
                    "orderId": "",
                    "skuCompose": {
                        "sku": [
                            {
                                "businessCode": "",
                                "number": 0,
                                "skuId": ""
                            }
                        ]
                    },
                    "videoSet": [
                        {
                            "url": "",
                            "videoOrder": 0
                        }
                    ]
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "transactCode": ""
                    },
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "transactProductAsync")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("algorithmType", algorithmType)
        intef.update_body("callBackUrl", callBackUrl)
        intef.update_body("deviceId", deviceId)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("orderId", orderId)
        intef.update_body("skuCompose", skuCompose)
        intef.update_body("videoSet", videoSet)
        return intef.request() if sendRequest else intef

    def asyncTransactStatusGetApi(self, transactCode, device_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询异步交易状态 """
        """  path: [get]/openapi/v1/product/async/{transactCode}/status API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "requestId": "",
                        "status": ""
                    },
                    "message": "",
                    "success": false
                }
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "asyncTransactStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.add_params("device_id", device_id)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("transactCode", transactCode)
        return intef.request() if sendRequest else intef

    def cameraCheckPostApi(self, imageInfo=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  相机检测 """
        """  path: [post]/openapi/v1/product/camera API """
        """  body: 
                {
                    "imageInfo": []
                }
        """
        """  resp:
                200(OK):
                {}
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "cameraCheck")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("imageInfo", imageInfo)
        return intef.request() if sendRequest else intef

    def conflictProductPostApi(self, sku_compose=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  冲突检测 """
        """  path: [post]/openapi/v1/product/conflict API """
        """  body: 
                {
                    "sku_compose": {
                        "skus": [
                            {
                                "business_code": "",
                                "gravity": 0,
                                "sku_id": ""
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(OK):
                {}
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "conflictProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("sku_compose", sku_compose)
        return intef.request() if sendRequest else intef

    def RecognizeProductDetailPostApi(self, deviceId=None, externalBizFrom=None, image=None, orderId=None, skuComposeIds=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  检测图片中物品以及物品框 """
        """  path: [post]/openapi/v1/product/detail/recognize API """
        """  body: 
                {
                    "deviceId": "",
                    "externalBizFrom": "",
                    "image": "",
                    "orderId": "",
                    "skuComposeIds": []
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "recognizeBodyList": [
                            {
                                "boundingPoly": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "skuInfoList": [
                                    {
                                        "businessCode": "",
                                        "confidence": 0,
                                        "price": 0,
                                        "skuId": "",
                                        "skuName": ""
                                    }
                                ]
                            }
                        ],
                        "requestId": "",
                        "uniqueId": ""
                    },
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "RecognizeProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("deviceId", deviceId)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("image", image)
        intef.update_body("orderId", orderId)
        intef.update_body("skuComposeIds", skuComposeIds)
        return intef.request() if sendRequest else intef

    def queryProductListGetApi(self, sku_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询所有已注册物品信息 """
        """  path: [get]/openapi/v1/product/list API """
        """  params: 
                参数名称：sku_id　类型：integer　描述：sku_i
        """
        """  resp:
                200(OK):
                {}
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "queryProductList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("sku_id", sku_id)
        return intef.request() if sendRequest else intef

    def RecognizeMultipleProductPostApi(self, deviceId=None, externalBizFrom=None, imageList=None, orderId=None, skuCompose=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  检测多张图片中物品以及物品框 """
        """  path: [post]/openapi/v1/product/multiple/detail/recognize API """
        """  body: 
                {
                    "deviceId": "",
                    "externalBizFrom": "",
                    "imageList": [
                        {
                            "image": "",
                            "uniqueId": ""
                        }
                    ],
                    "orderId": "",
                    "skuCompose": {
                        "sku": [
                            {
                                "businessCode": "",
                                "number": 0,
                                "skuId": ""
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "multiRecognizeBody": [
                            {
                                "recognizeBodyList": [
                                    {
                                        "boundingPoly": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "skuInfoList": [
                                            {
                                                "businessCode": "",
                                                "confidence": 0,
                                                "price": 0,
                                                "skuId": "",
                                                "skuName": ""
                                            }
                                        ]
                                    }
                                ],
                                "requestId": "",
                                "uniqueId": ""
                            }
                        ],
                        "requestId": ""
                    },
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "RecognizeMultipleProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("deviceId", deviceId)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("imageList", imageList)
        intef.update_body("orderId", orderId)
        intef.update_body("skuCompose", skuCompose)
        return intef.request() if sendRequest else intef

    def ProductNameSearchPostApi(self, data=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询skuName """
        """  path: [post]/openapi/v1/product/name API """
        """  body: 
                {}
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": [],
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "ProductNameSearch")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.body_dict = data
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def recognizeProductPostApi(self, device_id=None, image_set1=None, orderId=None, sku_compose=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  识别 """
        """  path: [post]/openapi/v1/product/recognize API """
        """  body: 
                {
                    "device_id": "",
                    "image_set1": [
                        {
                            "camera_id": "",
                            "content": "",
                            "url": "",
                            "\u56fe\u7247\u987a\u5e8f": 0
                        }
                    ],
                    "orderId": "",
                    "sku_compose": {
                        "skus": [
                            {
                                "business_code": "",
                                "gravity": 0,
                                "sku_id": ""
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(OK):
                {}
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "recognizeProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("image_set1", image_set1)
        intef.update_body("orderId", orderId)
        intef.update_body("sku_compose", sku_compose)
        return intef.request() if sendRequest else intef

    def replenishCheckPostApi(self, deviceId=None, mediaSets=None, skuCompose=None, template=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  补货检测 """
        """  path: [post]/openapi/v1/product/replenish API """
        """  body: 
                {
                    "deviceId": "",
                    "mediaSets": [
                        {
                            "content": "",
                            "index": 0,
                            "mediaId": "",
                            "url": ""
                        }
                    ],
                    "skuCompose": {
                        "skus": [
                            {
                                "business_code": "",
                                "gravity": 0,
                                "sku_id": ""
                            }
                        ]
                    },
                    "template": [
                        {
                            "columns": [
                                {
                                    "number": 0,
                                    "skuId": ""
                                }
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200(OK):
                {}
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "replenishCheck")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("deviceId", deviceId)
        intef.update_body("mediaSets", mediaSets)
        intef.update_body("skuCompose", skuCompose)
        intef.update_body("template", template)
        return intef.request() if sendRequest else intef

    def ProductSyncInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询同步的sku信息,同步到测试环境用 """
        """  path: [get]/openapi/v1/product/sync/product API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "simpleProductSyncRecordList": [
                            {
                                "auditStatus": 0,
                                "barCode": "",
                                "brand": "",
                                "categoryId": 0,
                                "createTime": 0,
                                "effectEndTime": 0,
                                "effectStartTime": 0,
                                "imageInfo": "",
                                "name": "",
                                "packing": "",
                                "productId": 0,
                                "scene": "",
                                "size": "",
                                "tag": "",
                                "weight": ""
                            }
                        ]
                    },
                    "message": "",
                    "success": false
                }
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "ProductSyncInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def tenantConflictGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取租户所有冲突信息 """
        """  path: [get]/openapi/v1/product/tenant/conflict API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "conflictDetailList": [
                            {
                                "businessCode": "",
                                "conflictList": []
                            }
                        ]
                    },
                    "message": "",
                    "success": false
                }
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "tenantConflict")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def compareProductPostApi(self, algorithm_type=None, compose_id=None, device_id=None, gravity=None, image_set1=None, image_set2=None, image_set3=None, order_id=None, sku_compose=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  识别两组图片前后的商品数量变化，仅与传入模版商品比对 """
        """  path: [post]/openapi/v1/product/transact API """
        """  body: 
                {
                    "algorithm_type": 0,
                    "compose_id": "",
                    "device_id": "",
                    "gravity": [
                        {
                            "gravities": [],
                            "timestamp": ""
                        }
                    ],
                    "image_set1": [
                        {
                            "camera_id": "",
                            "content": "",
                            "url": "",
                            "\u56fe\u7247\u987a\u5e8f": 0
                        }
                    ],
                    "image_set2": [
                        {
                            "camera_id": "",
                            "content": "",
                            "url": "",
                            "\u56fe\u7247\u987a\u5e8f": 0
                        }
                    ],
                    "image_set3": [
                        {
                            "camera_id": "",
                            "content": "",
                            "url": "",
                            "\u56fe\u7247\u987a\u5e8f": 0
                        }
                    ],
                    "order_id": "",
                    "sku_compose": {
                        "skus": [
                            {
                                "business_code": "",
                                "gravity": 0,
                                "sku_id": ""
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(OK):
                {}
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "compareProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("algorithm_type", algorithm_type)
        intef.update_body("compose_id", compose_id)
        intef.update_body("device_id", device_id)
        intef.update_body("gravity", gravity)
        intef.update_body("image_set1", image_set1)
        intef.update_body("image_set2", image_set2)
        intef.update_body("image_set3", image_set3)
        intef.update_body("order_id", order_id)
        intef.update_body("sku_compose", sku_compose)
        return intef.request() if sendRequest else intef

    def transactProductAsync_1PostApi(self, algorithmType=None, callBackUrl=None, deviceId=None, externalBizFrom=None, orderId=None, skuCompose=None, videoSet=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  异步交易 """
        """  path: [post]/openapi/v2/product/async/transact API """
        """  body: 
                {
                    "algorithmType": 0,
                    "callBackUrl": "",
                    "deviceId": "",
                    "externalBizFrom": "",
                    "orderId": "",
                    "skuCompose": {
                        "sku": [
                            {
                                "businessCode": "",
                                "number": 0,
                                "skuId": ""
                            }
                        ]
                    },
                    "videoSet": [
                        {
                            "url": "",
                            "videoOrder": 0
                        }
                    ]
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "transactCode": ""
                    },
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "transactProductAsync_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("algorithmType", algorithmType)
        intef.update_body("callBackUrl", callBackUrl)
        intef.update_body("deviceId", deviceId)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("orderId", orderId)
        intef.update_body("skuCompose", skuCompose)
        intef.update_body("videoSet", videoSet)
        return intef.request() if sendRequest else intef

    def asyncTransactStatus_1GetApi(self, transactCode, device_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询异步交易状态 """
        """  path: [get]/openapi/v2/product/async/{transactCode}/status API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "requestId": "",
                        "status": ""
                    },
                    "message": "",
                    "success": false
                }
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "asyncTransactStatus_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.add_params("device_id", device_id)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("transactCode", transactCode)
        return intef.request() if sendRequest else intef

    def cameraCheck_1PostApi(self, imageInfo=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  相机检测 """
        """  path: [post]/openapi/v2/product/camera API """
        """  body: 
                {
                    "imageInfo": []
                }
        """
        """  resp:
                200(OK):
                {}
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "cameraCheck_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("imageInfo", imageInfo)
        return intef.request() if sendRequest else intef

    def conflictProduct_1PostApi(self, sku_compose=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  冲突检测 """
        """  path: [post]/openapi/v2/product/conflict API """
        """  body: 
                {
                    "sku_compose": {
                        "skus": [
                            {
                                "business_code": "",
                                "gravity": 0,
                                "sku_id": ""
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(OK):
                {}
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "conflictProduct_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("sku_compose", sku_compose)
        return intef.request() if sendRequest else intef

    def RecognizeProductDetail_1PostApi(self, deviceId=None, externalBizFrom=None, image=None, orderId=None, skuComposeIds=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  检测图片中物品以及物品框 """
        """  path: [post]/openapi/v2/product/detail/recognize API """
        """  body: 
                {
                    "deviceId": "",
                    "externalBizFrom": "",
                    "image": "",
                    "orderId": "",
                    "skuComposeIds": []
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "recognizeBodyList": [
                            {
                                "boundingPoly": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ]
                                },
                                "skuInfoList": [
                                    {
                                        "businessCode": "",
                                        "confidence": 0,
                                        "price": 0,
                                        "skuId": "",
                                        "skuName": ""
                                    }
                                ]
                            }
                        ],
                        "requestId": "",
                        "uniqueId": ""
                    },
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "RecognizeProduct_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("deviceId", deviceId)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("image", image)
        intef.update_body("orderId", orderId)
        intef.update_body("skuComposeIds", skuComposeIds)
        return intef.request() if sendRequest else intef

    def queryProductList_1GetApi(self, sku_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询所有已注册物品信息 """
        """  path: [get]/openapi/v2/product/list API """
        """  params: 
                参数名称：sku_id　类型：integer　描述：sku_i
        """
        """  resp:
                200(OK):
                {}
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "queryProductList_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("sku_id", sku_id)
        return intef.request() if sendRequest else intef

    def RecognizeMultipleProduct_1PostApi(self, deviceId=None, externalBizFrom=None, imageList=None, orderId=None, skuCompose=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  检测多张图片中物品以及物品框 """
        """  path: [post]/openapi/v2/product/multiple/detail/recognize API """
        """  body: 
                {
                    "deviceId": "",
                    "externalBizFrom": "",
                    "imageList": [
                        {
                            "image": "",
                            "uniqueId": ""
                        }
                    ],
                    "orderId": "",
                    "skuCompose": {
                        "sku": [
                            {
                                "businessCode": "",
                                "number": 0,
                                "skuId": ""
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "multiRecognizeBody": [
                            {
                                "recognizeBodyList": [
                                    {
                                        "boundingPoly": {
                                            "vertices": [
                                                {
                                                    "x": 0,
                                                    "y": 0
                                                }
                                            ]
                                        },
                                        "skuInfoList": [
                                            {
                                                "businessCode": "",
                                                "confidence": 0,
                                                "price": 0,
                                                "skuId": "",
                                                "skuName": ""
                                            }
                                        ]
                                    }
                                ],
                                "requestId": "",
                                "uniqueId": ""
                            }
                        ],
                        "requestId": ""
                    },
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "RecognizeMultipleProduct_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("deviceId", deviceId)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("imageList", imageList)
        intef.update_body("orderId", orderId)
        intef.update_body("skuCompose", skuCompose)
        return intef.request() if sendRequest else intef

    def ProductNameSearch_1PostApi(self, data=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询skuName """
        """  path: [post]/openapi/v2/product/name API """
        """  body: 
                {}
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": [],
                    "message": "",
                    "success": false
                }
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "ProductNameSearch_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        intef.body_dict = data
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def recognizeProduct_1PostApi(self, device_id=None, image_set1=None, orderId=None, sku_compose=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  识别 """
        """  path: [post]/openapi/v2/product/recognize API """
        """  body: 
                {
                    "device_id": "",
                    "image_set1": [
                        {
                            "camera_id": "",
                            "content": "",
                            "url": "",
                            "\u56fe\u7247\u987a\u5e8f": 0
                        }
                    ],
                    "orderId": "",
                    "sku_compose": {
                        "skus": [
                            {
                                "business_code": "",
                                "gravity": 0,
                                "sku_id": ""
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(OK):
                {}
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "recognizeProduct_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_id", device_id)
        intef.update_body("image_set1", image_set1)
        intef.update_body("orderId", orderId)
        intef.update_body("sku_compose", sku_compose)
        return intef.request() if sendRequest else intef

    def replenishCheck_1PostApi(self, deviceId=None, mediaSets=None, skuCompose=None, template=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  补货检测 """
        """  path: [post]/openapi/v2/product/replenish API """
        """  body: 
                {
                    "deviceId": "",
                    "mediaSets": [
                        {
                            "content": "",
                            "index": 0,
                            "mediaId": "",
                            "url": ""
                        }
                    ],
                    "skuCompose": {
                        "skus": [
                            {
                                "business_code": "",
                                "gravity": 0,
                                "sku_id": ""
                            }
                        ]
                    },
                    "template": [
                        {
                            "columns": [
                                {
                                    "number": 0,
                                    "skuId": ""
                                }
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200(OK):
                {}
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "replenishCheck_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("deviceId", deviceId)
        intef.update_body("mediaSets", mediaSets)
        intef.update_body("skuCompose", skuCompose)
        intef.update_body("template", template)
        return intef.request() if sendRequest else intef

    def ProductSyncInfo_1GetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询同步的sku信息,同步到测试环境用 """
        """  path: [get]/openapi/v2/product/sync/product API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "simpleProductSyncRecordList": [
                            {
                                "auditStatus": 0,
                                "barCode": "",
                                "brand": "",
                                "categoryId": 0,
                                "createTime": 0,
                                "effectEndTime": 0,
                                "effectStartTime": 0,
                                "imageInfo": "",
                                "name": "",
                                "packing": "",
                                "productId": 0,
                                "scene": "",
                                "size": "",
                                "tag": "",
                                "weight": ""
                            }
                        ]
                    },
                    "message": "",
                    "success": false
                }
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "ProductSyncInfo_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def tenantConflict_1GetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取租户所有冲突信息 """
        """  path: [get]/openapi/v2/product/tenant/conflict API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "conflictDetailList": [
                            {
                                "businessCode": "",
                                "conflictList": []
                            }
                        ]
                    },
                    "message": "",
                    "success": false
                }
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "tenantConflict_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def compareProduct_1PostApi(self, algorithm_type=None, compose_id=None, device_id=None, gravity=None, image_set1=None, image_set2=None, image_set3=None, order_id=None, sku_compose=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  识别两组图片前后的商品数量变化，仅与传入模版商品比对 """
        """  path: [post]/openapi/v2/product/transact API """
        """  body: 
                {
                    "algorithm_type": 0,
                    "compose_id": "",
                    "device_id": "",
                    "gravity": [
                        {
                            "gravities": [],
                            "timestamp": ""
                        }
                    ],
                    "image_set1": [
                        {
                            "camera_id": "",
                            "content": "",
                            "url": "",
                            "\u56fe\u7247\u987a\u5e8f": 0
                        }
                    ],
                    "image_set2": [
                        {
                            "camera_id": "",
                            "content": "",
                            "url": "",
                            "\u56fe\u7247\u987a\u5e8f": 0
                        }
                    ],
                    "image_set3": [
                        {
                            "camera_id": "",
                            "content": "",
                            "url": "",
                            "\u56fe\u7247\u987a\u5e8f": 0
                        }
                    ],
                    "order_id": "",
                    "sku_compose": {
                        "skus": [
                            {
                                "business_code": "",
                                "gravity": 0,
                                "sku_id": ""
                            }
                        ]
                    }
                }
        """
        """  resp:
                200(OK):
                {}
                201(Created):
                ""
                401(Unauthorized):
                ""
                403(Forbidden):
                ""
                404(Not Found):
                ""

        """
        intef = collections.interface("galaxyProduct", "compareProduct_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("algorithm_type", algorithm_type)
        intef.update_body("compose_id", compose_id)
        intef.update_body("device_id", device_id)
        intef.update_body("gravity", gravity)
        intef.update_body("image_set1", image_set1)
        intef.update_body("image_set2", image_set2)
        intef.update_body("image_set3", image_set3)
        intef.update_body("order_id", order_id)
        intef.update_body("sku_compose", sku_compose)
        return intef.request() if sendRequest else intef

