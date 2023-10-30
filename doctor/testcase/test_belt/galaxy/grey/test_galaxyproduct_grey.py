#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

import pytest
from commonlib import config, time_utils, sign_utils, utils
from commonlib.log_utils import log
from pytest_check import check

verify_tag = True
verify_op = True
verify_request_id = True
save_resp = True

class TestGalaxyproductGrey(object):
    """ galaxyProduct 灰度测试"""

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

    def verify_resp_header(self, resp, greyMap, galaxyTenant, galaxyDevice, config_obj):
        """ 验证返回结果header"""
        grey_info = greyMap[galaxyTenant.name][galaxyDevice.name]

        if save_resp:
            result_dir = os.path.join(config_obj.result_path, "galaxy")
            if not os.path.exists(result_dir):
                os.makedirs(result_dir)
            requestId = "undefines"
            op = "undefines"
            tag = "undefines"
            if "X-Belt-Request-Id" in resp.origin_resp.headers:
                requestId = resp.origin_resp.headers["X-Belt-Request-Id"]
            if "X-Belt-Grayscale-OP" in resp.origin_resp.headers:
                op = resp.origin_resp.headers["X-Belt-Grayscale-OP"]
            if "X-Belt-host-Tag" in resp.origin_resp.headers:
                tag = resp.origin_resp.headers["X-Belt-host-Tag"]
            alaxy_result_path = os.path.join(result_dir, "%s_%s_%s_%s_%s.json" %(galaxyTenant.name, galaxyDevice.name,resp.inte_obj.name, op, requestId))

            result = {
                "request_id": requestId,
                "interface_name": resp.inte_obj.name,
                "op": op, # 返回的
                "tag": tag,
                "request_id": requestId,
                "status_code": resp.status_code,
                "url": resp.inte_obj.url,
                "header": resp.inte_obj.headers,
                "body": resp.inte_obj.body_dict ,
                "params": resp.inte_obj.params,
                "response": resp.json,
                "response_header": dict(resp.origin_resp.headers),
                "grey_info": grey_info,
                "galaxyTenant": {
                    'name': galaxyTenant.name,
                    'type': galaxyTenant.type,
                    'username': galaxyTenant.username,
                    'ak': galaxyTenant.ak,
                    'sk': galaxyTenant.sk,
                },
                "galaxyDevice": {
                    'name': galaxyDevice.name,
                    'id': galaxyDevice.id,
                },
            }
            utils.write_alaxy_result(alaxy_result_path, result)
        if verify_request_id:
            log().info("resp=>X-Belt-Request-Id:%s" % resp.origin_resp.headers["X-Belt-Request-Id"])
        if verify_op:
            log().info("resp=>X-Belt-Grayscale-OP:%s" % resp.origin_resp.headers["X-Belt-Grayscale-OP"])
            with check: assert op == grey_info["op"]
        if verify_tag:
            log().info("resp=>X-Belt-host-Tag:%s" % resp.origin_resp.headers["X-Belt-host-Tag"])
            with check: assert tag == grey_info["tag"]

    # @pytest.mark.parametrize("count", [x for x in range(30)])
    def test_grey_v1_transactProductAsync(self, config_obj, GalaxyproductApi,greyMap, galaxyTenant, galaxyDevice,
                                       getProductUrlsFromPreEnv):
        """  异步交易 """
        productUrls = getProductUrlsFromPreEnv
        log().info("productUrls:%s" % productUrls)
        algorithmType = 1
        callBackUrl = "https://sensegalaxy-pre-release.sensetime.com/api/user-management/api/v1/ums/test"
        deviceId = galaxyDevice["id"]
        externalBizFrom = None
        orderId = "%s" % sign_utils.getUuid(10)
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
        intef = GalaxyproductApi.transactProductAsyncPostApi(algorithmType=algorithmType, callBackUrl=callBackUrl,
                                                            deviceId=deviceId, externalBizFrom=externalBizFrom,
                                                            orderId=orderId, skuCompose=skuCompose, videoSet=videoSet,
                                                            sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v1_asyncTransactStatus(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice, getProductUrlsFromPreEnv):
        """  查询异步交易状态 """
        if '/openapi/v1/product/async/{transactCode}/status' not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        productUrls = getProductUrlsFromPreEnv
        log().info("productUrls:%s" % productUrls)
        algorithmType = 1
        callBackUrl = "https://sensegalaxy-pre-release.sensetime.com/api/user-management/api/v1/ums/test"
        deviceId = galaxyDevice["id"]
        externalBizFrom = None
        orderId = "%s" % sign_utils.getUuid(10)
        skuCompose = {
            "sku": [
                {
                    "businessCode": "",
                    "number": 0,
                    "skuId": "1502242678031519744"
                }
            ]
        }
        videoSet = [
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
        intef = GalaxyproductApi.transactProductAsyncPostApi(algorithmType=algorithmType, callBackUrl=callBackUrl,
                                                             deviceId=deviceId, externalBizFrom=externalBizFrom,
                                                             orderId=orderId, skuCompose=skuCompose, videoSet=videoSet,
                                                             sendRequest=False)
        resp = intef.request()
        assert resp.status_code == 200

        time.sleep(10)
        transactCode = resp.json_get("data.transactCode")
        intef = GalaxyproductApi.asyncTransactStatusGetApi(transactCode,device_id=deviceId, sendRequest=False)
        # if '/openapi/v1/product/async/{transactCode}/status' not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
        #     pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)
        # log().info("requestId:%s" % resp.json_get("data.requestId"))

    def test_grey_v1_cameraCheck(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  相机检测 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/camera.jpg")
        img = GalaxyproductApi.imageToBase64(image_path)
        imageInfo = [img,]
        intef = GalaxyproductApi.cameraCheckPostApi(imageInfo=imageInfo, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)
        # log().info("requestId:%s" % resp.json_get("header.request_id"))

    def test_grey_v1_conflictProduct(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
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
        intef = GalaxyproductApi.conflictProductPostApi(sku_compose=sku_compose,sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)
        # log().info("requestId:%s" % resp.json_get("header.request_id"))

    def test_grey_v1_RecognizeProductDetail(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  检测图片中物品以及物品框 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxyproductApi.imageToBase64(image_path)
        deviceId = galaxyDevice["id"]
        externalBizFrom = None
        image = img
        orderId = "111"
        skuComposeIds = [
            "6901939621608"
        ]
        intef = GalaxyproductApi.RecognizeProductDetailPostApi(deviceId=deviceId, externalBizFrom=externalBizFrom,
                                                         image=image, orderId=orderId, skuComposeIds=skuComposeIds,
                                                         sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)
        # log().info("requestId:%s" % resp.json_get("data.requestId"))

    def test_grey_v1_queryProductList(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  查询所有已注册物品信息 """
        # sku_id = "6901939621608"
        sku_id = None
        intef = GalaxyproductApi.queryProductListGetApi(sku_id=sku_id,sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)
        # log().info("requestId:%s" % resp.json_get("header.request_id"))

    def test_grey_v1_RecognizeMultipleProduct(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  检测多张图片中物品以及物品框 """
        image1_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        image2_path = os.path.join(config.image_path, "go_image/belt/galaxy/p2.jpg")
        img1 = GalaxyproductApi.imageToBase64(image1_path)
        img2 = GalaxyproductApi.imageToBase64(image2_path)
        deviceId = galaxyDevice["id"]
        externalBizFrom = None
        imageList =  [
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
        # 全集 0b1ff0ae-9c65-4ae9-af7b-0f2ae97f84d1
        # skuCompose = {
        #     "sku": [
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "6901939621608"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1590175275715592193"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1590177151924240386"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "6937962102531"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1502245660945027072"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1537280580482240512"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1502221919833821184"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1475349320948518912"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1483036516845359104"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1429708409195728896"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1570327683189633025"
        #       },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1534734494248996864"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "6901939621202"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1466659301408903168"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "6970399920415"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "6902538004045"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1463045581042618368"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1523552235814916096"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "6972549660097"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1501810391766798336"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "6921168550142"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1468477362667524096"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1466638257809788928"
        #         }
        #     ]
        #   }
        skuCompose = {
            "sku": [
              {
                "businessCode": "",
                "number": 0,
                "skuId": "6901939621608"
              }
            ]
          }
        intef = GalaxyproductApi.RecognizeMultipleProductPostApi(deviceId=deviceId, externalBizFrom=externalBizFrom,
                                                                imageList=imageList, orderId=orderId,
                                                                skuCompose=skuCompose, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)
        # log().info("requestId:%s" % resp.json_get("data.requestId"))

    def test_grey_v1_ProductNameSearch(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  查询skuName """
        data = ["1646819630968176641"]
        intef = GalaxyproductApi.ProductNameSearchPostApi(data=data, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v1_recognizeProduct(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  识别 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxyproductApi.imageToBase64(image_path)
        device_id = galaxyDevice["id"]
        image_set1 = [
            {
              "camera_id": "",
              "content": img
              # "url": "",
              # "图片顺序": 0
            }
          ]
        orderId = "111"
        sku_compose = {
            "skus":
                [{"sku_id": "6901939621608"}]
        }
        intef = GalaxyproductApi.recognizeProductPostApi(device_id=device_id, image_set1=image_set1, orderId=orderId,
                                                         sku_compose=sku_compose, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)
        # log().info("requestId:%s" % resp.json_get("header.request_id"))

    def test_grey_v1_replenishCheck(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  补货检测 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxyproductApi.imageToBase64(image_path)
        deviceId = galaxyDevice["id"]
        mediaSets = [
            {
              "content": img,
              "index": 0,
              "mediaId": "",
              "url": ""
            }
          ]
        skuCompose =  {
            "skus": [
              {
                "business_code": "",
                "gravity": 0,
                "sku_id": "6901939621608"
              }
            ]
          }
        template = [{"columns": [{"number": 1, "skuId": "6901939621608"}]}]
        intef = GalaxyproductApi.replenishCheckPostApi(deviceId=deviceId, mediaSets=mediaSets, skuCompose=skuCompose,
                                                       template=template, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)
        # log().info("requestId:%s" % resp.json_get("header.request_id"))

    def test_grey_v1_ProductSyncInfo(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  查询同步的sku信息,同步到测试环境用 """
        intef = GalaxyproductApi.ProductSyncInfoGetApi(sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v1_tenantConflict(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  获取租户所有冲突信息 """
        intef = GalaxyproductApi.tenantConflictGetApi(sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v1_static_compareProduct(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  识别两组图片前后的商品数量变化，仅与传入模版商品比对 (静态)"""
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxyproductApi.imageToBase64(image_path)
        algorithm_type = 1
        compose_id = None
        device_id = galaxyDevice["id"]
        gravity = [
        {
            "gravities":[

            ],
            "timestamp":"231"
        }
        ]
        image_set1 =  [
        {
          "camera_id": "",
          "content": img,
          "url": "",
          "图片顺序": 0
        }
        ]
        image_set2 =  [
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
        intef = GalaxyproductApi.compareProductPostApi(algorithm_type=algorithm_type, compose_id=compose_id,
                                                       device_id=device_id, gravity=gravity, image_set1=image_set1,
                                                       image_set2=image_set2, image_set3=image_set3, order_id=order_id,
                                                       sku_compose=sku_compose, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        if galaxyTenant.type != 'static':
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)
        # log().info("requestId:%s" % resp.json_get("header.request_id"))

    def test_grey_v1_dynamic_compareProduct(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice,getProductUrlsFromPreEnv):
        """  识别两组图片前后的商品数量变化，仅与传入模版商品比对 (动态)"""
        productUrls = getProductUrlsFromPreEnv
        log().info("productUrls:%s" % productUrls)
        algorithm_type = 1
        compose_id = None
        device_id = galaxyDevice["id"]
        gravity = None
        image_set1 =  [
        {
          "camera_id": "",
          "content": "",
          "url": productUrls[0],
        }
        ]
        image_set2 =  [
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
        intef = GalaxyproductApi.compareProductPostApi(algorithm_type=algorithm_type, compose_id=compose_id,
                                                       device_id=device_id, gravity=gravity, image_set1=image_set1,
                                                       image_set2=image_set2, image_set3=image_set3, order_id=order_id,
                                                       sku_compose=sku_compose, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        if galaxyTenant.type != 'dynamic':
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)
        # log().info("requestId:%s" % resp.json_get("header.request_id"))

    def test_grey_v2_transactProductAsync(self, config_obj, GalaxyproductApi,greyMap, galaxyTenant, galaxyDevice,
                                       getProductUrlsFromPreEnv):
        """  异步交易 """
        productUrls = getProductUrlsFromPreEnv
        log().info("productUrls:%s" % productUrls)
        algorithmType = 1
        callBackUrl = "https://sensegalaxy-pre-release.sensetime.com/api/user-management/api/v1/ums/test"
        deviceId = galaxyDevice["id"]
        externalBizFrom = None
        orderId = "%s" % sign_utils.getUuid(10)
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
        intef = GalaxyproductApi.transactProductAsync_1PostApi(algorithmType=algorithmType, callBackUrl=callBackUrl,
                                                            deviceId=deviceId, externalBizFrom=externalBizFrom,
                                                            orderId=orderId, skuCompose=skuCompose, videoSet=videoSet,
                                                            sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_asyncTransactStatus(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice,
                                         getProductUrlsFromPreEnv):
        """  查询异步交易状态 """
        if '/openapi/v2/product/async/{transactCode}/status' not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        productUrls = getProductUrlsFromPreEnv
        log().info("productUrls:%s" % productUrls)
        algorithmType = 1
        callBackUrl = "https://sensegalaxy-pre-release.sensetime.com/api/user-management/api/v1/ums/test"
        deviceId = galaxyDevice["id"]
        externalBizFrom = None
        orderId = "%s" % sign_utils.getUuid(10)
        skuCompose = {
            "sku": [
                {
                    "businessCode": "",
                    "number": 0,
                    "skuId": "1502242678031519744"
                }
            ]
        }
        videoSet = [
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
        intef = GalaxyproductApi.transactProductAsync_1PostApi(algorithmType=algorithmType, callBackUrl=callBackUrl,
                                                               deviceId=deviceId, externalBizFrom=externalBizFrom,
                                                               orderId=orderId, skuCompose=skuCompose,
                                                               videoSet=videoSet,
                                                               sendRequest=False)
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"

        time.sleep(10)
        transactCode = resp.json_get("data.transactCode")
        intef = GalaxyproductApi.asyncTransactStatus_1GetApi(transactCode, device_id=deviceId, sendRequest=False)
        # if '/openapi/v2/product/async/{transactCode}/status' not in greyMap[galaxyTenant.name][galaxyDevice.name][
        #     "interface_group"]:
        #     pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_cameraCheck(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  相机检测 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/camera.jpg")
        img = GalaxyproductApi.imageToBase64(image_path)
        imageInfo = [img, ]
        intef = GalaxyproductApi.cameraCheck_1PostApi(imageInfo=imageInfo, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_conflictProduct(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
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
        intef = GalaxyproductApi.conflictProduct_1PostApi(sku_compose=sku_compose, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_RecognizeProductDetail(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  检测图片中物品以及物品框 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxyproductApi.imageToBase64(image_path)
        deviceId = galaxyDevice["id"]
        externalBizFrom = None
        image = img
        orderId = "111"
        skuComposeIds = [
            "6901939621608"
        ]
        intef = GalaxyproductApi.RecognizeProductDetail_1PostApi(deviceId=deviceId, externalBizFrom=externalBizFrom,
                                                         image=image, orderId=orderId, skuComposeIds=skuComposeIds,
                                                         sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_queryProductList(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  查询所有已注册物品信息 """
        # sku_id = "6901939621608"
        sku_id = None
        intef = GalaxyproductApi.queryProductList_1GetApi(sku_id=sku_id, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_RecognizeMultipleProduct(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  检测多张图片中物品以及物品框 """
        image1_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        image2_path = os.path.join(config.image_path, "go_image/belt/galaxy/p2.jpg")
        img1 = GalaxyproductApi.imageToBase64(image1_path)
        img2 = GalaxyproductApi.imageToBase64(image2_path)
        deviceId = galaxyDevice["id"]
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
        # 全集 0b1ff0ae-9c65-4ae9-af7b-0f2ae97f84d1
        # skuCompose = {
        #     "sku": [
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "6901939621608"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1590175275715592193"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1590177151924240386"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "6937962102531"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1502245660945027072"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1537280580482240512"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1502221919833821184"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1475349320948518912"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1483036516845359104"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1429708409195728896"
        #       },
        #       {
        #         "businessCode": "",
        #         "number": 0,
        #         "skuId": "1570327683189633025"
        #       },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1534734494248996864"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "6901939621202"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1466659301408903168"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "6970399920415"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "6902538004045"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1463045581042618368"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1523552235814916096"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "6972549660097"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1501810391766798336"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "6921168550142"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1468477362667524096"
        #         },
        #         {
        #             "businessCode": "",
        #             "number": 0,
        #             "skuId": "1466638257809788928"
        #         }
        #     ]
        #   }
        skuCompose = {
            "sku": [
                {
                    "businessCode": "",
                    "number": 0,
                    "skuId": "6901939621608"
                }
            ]
        }
        intef = GalaxyproductApi.RecognizeMultipleProduct_1PostApi(deviceId=deviceId, externalBizFrom=externalBizFrom,
                                                                 imageList=imageList, orderId=orderId,
                                                                 skuCompose=skuCompose, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_ProductNameSearch(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  查询skuName """
        data = ["1646819630968176641"]
        intef = GalaxyproductApi.ProductNameSearch_1PostApi(data=data, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_recognizeProduct(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  识别 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxyproductApi.imageToBase64(image_path)
        device_id = galaxyDevice["id"]
        image_set1 = [
            {
                "camera_id": "",
                "content": img
                # "url": "",
                # "图片顺序": 0
            }
        ]
        orderId = "111"
        sku_compose = {
            "skus":
                [{"sku_id": "6901939621608"}]
        }
        intef = GalaxyproductApi.recognizeProduct_1PostApi(device_id=device_id, image_set1=image_set1, orderId=orderId,
                                                         sku_compose=sku_compose, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_replenishCheck(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  补货检测 """
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxyproductApi.imageToBase64(image_path)
        deviceId = galaxyDevice["id"]
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
        intef = GalaxyproductApi.replenishCheck_1PostApi(deviceId=deviceId, mediaSets=mediaSets, skuCompose=skuCompose,
                                                       template=template, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_ProductSyncInfo(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  查询同步的sku信息,同步到测试环境用 """
        intef = GalaxyproductApi.ProductSyncInfo_1GetApi(sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_tenantConflict(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  获取租户所有冲突信息 """
        intef = GalaxyproductApi.tenantConflict_1GetApi(sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("message") == "success"
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_static_compareProduct(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice):
        """  识别两组图片前后的商品数量变化，仅与传入模版商品比对 (静态)"""
        image_path = os.path.join(config.image_path, "go_image/belt/galaxy/p1.jpg")
        img = GalaxyproductApi.imageToBase64(image_path)
        algorithm_type = 1
        compose_id = None
        device_id = galaxyDevice["id"]
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
        intef = GalaxyproductApi.compareProduct_1PostApi(algorithm_type=algorithm_type, compose_id=compose_id,
                                                       device_id=device_id, gravity=gravity, image_set1=image_set1,
                                                       image_set2=image_set2, image_set3=image_set3, order_id=order_id,
                                                       sku_compose=sku_compose, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        if galaxyTenant.type != 'static':
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

    def test_grey_v2_dynamic_compareProduct(self, config_obj, GalaxyproductApi, greyMap, galaxyTenant, galaxyDevice,
                                            getProductUrlsFromPreEnv):
        """  识别两组图片前后的商品数量变化，仅与传入模版商品比对 (动态)"""
        productUrls = getProductUrlsFromPreEnv
        log().info("productUrls:%s" % productUrls)
        algorithm_type = 1
        compose_id = None
        device_id = galaxyDevice["id"]
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
        intef = GalaxyproductApi.compareProduct_1PostApi(algorithm_type=algorithm_type, compose_id=compose_id,
                                                       device_id=device_id, gravity=gravity, image_set1=image_set1,
                                                       image_set2=image_set2, image_set3=image_set3, order_id=order_id,
                                                       sku_compose=sku_compose, sendRequest=False)
        if intef.path not in greyMap[galaxyTenant.name][galaxyDevice.name]["interface_group"]:
            pytest.skip("skip")
        if galaxyTenant.type != 'dynamic':
            pytest.skip("skip")
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("header.error_code") == 0
        self.verify_resp_header(resp, greyMap, galaxyTenant, galaxyDevice, config_obj)

