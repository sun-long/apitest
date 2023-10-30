#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestGalaxybeltproductApi(object):
    """ galaxyBeltProduct Api测试"""

    @pytest.fixture(scope="class", autouse=True)
    def init_func(self, config_obj):
        # 初始化测试集
        # 所有test运行前运行一次，接收外部参数env_obj，初始化测试环境
        log().info("==========%s测试开始==========" % self.__class__.__name__)

    def teardown_class(self):
        # 所有test运行完后运行一次
        log().info("==========%s测试结束==========\n" % self.__name__)
        log().info("clear tasks finish")

    def setup_method(self, method):
        # 每个测试用例执行之前做操作
        log().info("用例%s开始" % method.__name__)

    def teardown_method(self, method):
        # 每个测试用例执行之后做操作
        log().info("用例%s结束" % method.__name__)

    def test_api_transactProductAsync_dynamic(self, user_info_galaxy, config_obj, GalaxybeltproductDynamicApi, getProductUrls):
        """  异步交易 """
        productUrls = getProductUrls
        algorithmType = 1
        callBackUrl = "https://sensegalaxy-pre-release.sensetime.com/api/user-management/api/v1/ums/test"
        deviceId = "device_id"
        externalBizFrom = None
        orderId = "111_%s" % time_utils.get_time_str()
        skuCompose = {
            "sku": [
              {
                "businessCode": "",
                "number": 0,
                "skuId": "1502242678031519744"
              }
            ]
          }
        videoSet =  [
            {
              "url": productUrls[0],
              "videoOrder": 0
            },
            {
              "url": productUrls[1],
              "videoOrder": 1
            },
            {
              "url": productUrls[2],
              "videoOrder": 2
            }
        ]
        resp = GalaxybeltproductDynamicApi.transactProductAsync_1PostApi(algorithmType=algorithmType, callBackUrl=callBackUrl, deviceId=deviceId, externalBizFrom=externalBizFrom, orderId=orderId, skuCompose=skuCompose, videoSet=videoSet)
        if user_info_galaxy.type == "static":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("message") == "success"

    def test_api_asyncTransactStatus_dynamic(self, user_info_galaxy, config_obj, GalaxybeltproductDynamicApi):
        """  查询异步交易状态 """
        transactCode = "1681546027723231233"
        resp = GalaxybeltproductDynamicApi.asyncTransactStatus_1GetApi(transactCode)
        if user_info_galaxy.type == "static":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("message") == "success"

    def test_api_cameraCheck_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  相机检测 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/camera.jpg")
        img = GalaxybeltproductStaticApi.imageToBase64(image_path)
        imageInfo = [img,]
        resp = GalaxybeltproductStaticApi.cameraCheck_1PostApi(imageInfo=imageInfo)
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("header.error_code") == 0

    def test_api_cameraCheck_dynamic(self, user_info_galaxy, config_obj, GalaxybeltproductDynamicApi):
        """  相机检测 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/camera.jpg")
        img = GalaxybeltproductDynamicApi.imageToBase64(image_path)
        imageInfo = [img,]
        resp = GalaxybeltproductDynamicApi.cameraCheck_1PostApi(imageInfo=imageInfo)
        if user_info_galaxy.type == "static":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("header.error_code") == 0

    def test_api_conflictProduct_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  冲突检测 """
        sku_compose = {
            "skus": [
                {
                    "sku_id": "6901939621608"
                },
                {
                    "sku_id": "1590175275715592193"
                },
            ]
        }
        resp = GalaxybeltproductStaticApi.conflictProduct_1PostApi(sku_compose=sku_compose)
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("header.error_code") == 0

    def test_api_conflictProduct_dynamic(self, user_info_galaxy, config_obj, GalaxybeltproductDynamicApi):
        """  冲突检测 """
        sku_compose = {
            "skus": [
                {
                    "sku_id": "6901939621608"
                },
                {
                    "sku_id": "1590175275715592193"
                },
            ]
        }
        resp = GalaxybeltproductDynamicApi.conflictProduct_1PostApi(sku_compose=sku_compose)
        if user_info_galaxy.type == "static":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("header.error_code") == 0

    def test_api_RecognizeProduct_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  检测图片中物品以及物品框 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxybeltproductStaticApi.imageToBase64(image_path)
        deviceId = "device1"
        externalBizFrom = None
        image = img
        orderId = "111"
        skuComposeIds = [
            "6901939621608"
        ]
        resp = GalaxybeltproductStaticApi.RecognizeProduct_1PostApi(deviceId=deviceId, externalBizFrom=externalBizFrom, image=image, orderId=orderId, skuComposeIds=skuComposeIds)
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("message") == "success"

    def test_api_queryProductList_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  查询所有已注册物品信息 """
        # sku_id = "6901939621608"
        sku_id = None
        resp = GalaxybeltproductStaticApi.queryProductList_1GetApi(sku_id=sku_id)
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("header.error_code") == 0

    def test_api_queryProductList_dynamic(self, user_info_galaxy, config_obj, GalaxybeltproductDynamicApi):
        """  查询所有已注册物品信息 """
        # sku_id = "6901939621608"
        sku_id = None
        resp = GalaxybeltproductDynamicApi.queryProductList_1GetApi(sku_id=sku_id)
        if user_info_galaxy.type == "static":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("header.error_code") == 0

    def test_api_RecognizeMultipleProduct_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  检测多张图片中物品以及物品框 """
        image1_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        image2_path = os.path.join(config.image_path, "go_image/belt/galaxy/p2.jpg")
        img1 = GalaxybeltproductStaticApi.imageToBase64(image1_path)
        img2 = GalaxybeltproductStaticApi.imageToBase64(image2_path)
        deviceId = "device1"
        externalBizFrom = None
        imageList = [
            {
                "image": img1,
                "uniqueId": "1"
            },
            {
                "image": img2,
                "uniqueId": "2"
            },
        ]
        orderId = "111"
        skuCompose = {
            "sku": [
                {
                    "businessCode": "",
                    "number": 0,
                    "skuId": "6901939621608"
                }
            ]
        }
        resp = GalaxybeltproductStaticApi.RecognizeMultipleProduct_1PostApi(deviceId=deviceId, externalBizFrom=externalBizFrom, imageList=imageList, orderId=orderId, skuCompose=skuCompose)
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("message") == "success"

    def test_api_ProductNameSearch_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  查询skuName """
        data = ["1646819630968176641"]
        resp = GalaxybeltproductStaticApi.ProductNameSearch_1PostApi(data=data)
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("message") == "success"

    def test_api_ProductNameSearch_dynamic(self, user_info_galaxy, config_obj, GalaxybeltproductDynamicApi):
        """  查询skuName """
        data = ["1646819630968176641"]
        resp = GalaxybeltproductDynamicApi.ProductNameSearch_1PostApi(data=data)
        if user_info_galaxy.type == "static":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("message") == "success"

    def test_api_recognizeProduct_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  识别 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxybeltproductStaticApi.imageToBase64(image_path)
        device_id = "device1"
        image_set1 = [
            {
                "camera_id": "",
                "content": img
            }
        ]
        orderId = "111"
        sku_compose = {
            "skus":
                [{"sku_id": "6901939621608"}]
        }
        resp = GalaxybeltproductStaticApi.recognizeProduct_1PostApi(device_id=device_id, image_set1=image_set1, orderId=orderId, sku_compose=sku_compose)
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("header.error_code") == 0

    def test_api_replenishCheck_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  补货检测 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxybeltproductStaticApi.imageToBase64(image_path)
        deviceId = "device"
        mediaSets = [
            {
                "content": img,
                "index": 0,
                "mediaId": "",
                "url": ""
            }
        ]
        skuCompose = {
            "skus": [
                {
                    "business_code": "",
                    "gravity": 0,
                    "sku_id": "6901939621608"
                }
            ]
        }
        template = [{"columns": [{"number": 1, "skuId": "6901939621608"}]}]
        resp = GalaxybeltproductStaticApi.replenishCheck_1PostApi(deviceId=deviceId, mediaSets=mediaSets, skuCompose=skuCompose, template=template)
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("header.error_code") == 0

    def test_api_ProductSyncInfo_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  查询同步的sku信息,同步到测试环境用 """
        resp = GalaxybeltproductStaticApi.ProductSyncInfo_1GetApi()
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("message") == "success"

    def test_api_ProductSyncInfo_dynamic(self, user_info_galaxy, config_obj, GalaxybeltproductDynamicApi):
        """  查询同步的sku信息,同步到测试环境用 """
        resp = GalaxybeltproductDynamicApi.ProductSyncInfo_1GetApi()
        if user_info_galaxy.type == "static":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("message") == "success"

    def test_api_tenantConflict_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  获取租户所有冲突信息 """
        resp = GalaxybeltproductStaticApi.tenantConflict_1GetApi()
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("message") == "success"

    def test_api_tenantConflict_dynamic(self, user_info_galaxy, config_obj, GalaxybeltproductDynamicApi):
        """  获取租户所有冲突信息 """
        resp = GalaxybeltproductDynamicApi.tenantConflict_1GetApi()
        if user_info_galaxy.type == "static":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("message") == "success"

    def test_api_compareProduct_static(self, user_info_galaxy, config_obj, GalaxybeltproductStaticApi):
        """  识别两组图片前后的商品数量变化，仅与传入模版商品比对 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxybeltproductStaticApi.imageToBase64(image_path)
        algorithm_type = 1
        compose_id = None
        device_id = "device1"
        gravity = [
            {
                "gravities": [

                ],
                "timestamp": "231"
            }
        ]
        image_set1 = [
            {
                "camera_id": "",
                "content": img,
                "url": "",
                "图片顺序": 0
            }
        ]
        image_set2 = [
            {
                "camera_id": "",
                "content": img,
                "url": "",
                "图片顺序": 0
            }
        ]
        image_set3 = [
            {
                "camera_id": "",
                "content": img,
                "url": "",
                "图片顺序": 0
            }
        ]
        order_id = "1234"
        sku_compose = {
            "skus":
                [{"sku_id": "6901939621608"}]
        }
        resp = GalaxybeltproductStaticApi.compareProduct_1PostApi(algorithm_type=algorithm_type, compose_id=compose_id, device_id=device_id, gravity=gravity, image_set1=image_set1, image_set2=image_set2, image_set3=image_set3, order_id=order_id, sku_compose=sku_compose)
        if user_info_galaxy.type == "dynamic":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("header.error_code") == 0

    def test_api_compareProduct_dynamic(self, user_info_galaxy, config_obj, GalaxybeltproductDynamicApi, getProductUrls):
        """  识别两组图片前后的商品数量变化，仅与传入模版商品比对 """
        productUrls = getProductUrls
        log().info("productUrls:%s" % productUrls)
        algorithm_type = 1
        compose_id = None
        device_id = "device1"
        gravity = None
        image_set1 = [
            {
                "camera_id": "",
                "content": "",
                "url": productUrls[0],
            }
        ]
        image_set2 = [
            {
                "camera_id": "",
                "content": "",
                "url": productUrls[1],
            }
        ]
        image_set3 = [
            {
                "camera_id": "",
                "content": "",
                "url": productUrls[1],
            }
        ]
        order_id = "1234"
        sku_compose = {
            "skus":
                [{"sku_id": "1502242678031519744"}]
        }
        resp = GalaxybeltproductDynamicApi.compareProduct_1PostApi(algorithm_type=algorithm_type, compose_id=compose_id, device_id=device_id, gravity=gravity, image_set1=image_set1, image_set2=image_set2, image_set3=image_set3, order_id=order_id, sku_compose=sku_compose)
        if user_info_galaxy.type == "static":
            assert resp.status_code == 403
            assert resp.json_get("error.message") == "Forbidden"
            assert resp.json_get("error.status") == "PERMISSION_DENIED"
        else:
            assert resp.status_code == 200
            assert resp.json_get("header.error_code") == 0
