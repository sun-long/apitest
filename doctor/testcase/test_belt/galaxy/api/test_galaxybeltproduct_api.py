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

    def test_api_modifyProduct_1(self, config_obj, GalaxybeltproductApi):
        """  获取图片下载链接 """
        externalBizFrom = None
        fileNameList = None
        resp = GalaxybeltproductApi.modifyProduct_1PostApi(externalBizFrom=externalBizFrom, fileNameList=fileNameList)
        assert resp.status_code == 200

    def test_api_getProductUploadUrl(self, config_obj, GalaxybeltproductApi):
        """  获取物品上传链接 """
        externalBizFrom = None
        fileNameList = None
        resp = GalaxybeltproductApi.getProductUploadUrlPostApi(externalBizFrom=externalBizFrom, fileNameList=fileNameList)
        assert resp.status_code == 200

    def test_api_addProduct(self, config_obj, GalaxybeltproductApi):
        """  添加产品 """
        externalBizFrom = None
        productIdList = None
        resp = GalaxybeltproductApi.addProductPostApi(externalBizFrom=externalBizFrom, productIdList=productIdList)
        assert resp.status_code == 200

    def test_api_batchDelProduct(self, config_obj, GalaxybeltproductApi):
        """  批量删除物品 """
        externalBizFrom = None
        productIdList = None
        resp = GalaxybeltproductApi.batchDelProductPostApi(externalBizFrom=externalBizFrom, productIdList=productIdList)
        assert resp.status_code == 200

    def test_api_编辑businessCode(self, config_obj, GalaxybeltproductApi):
        """  编辑businessCode """
        productId = None
        resp = GalaxybeltproductApi.editBusinessCodePutApi(productId)
        assert resp.status_code == 200

    def test_api_getProductList(self, config_obj, GalaxybeltproductApi):
        """  查询产品列表 """
        auditStatus = None
        dateEnd = None
        dateStart = None
        externalBizFrom = None
        name = None
        page = None
        pageOrderList = None
        productId = None
        sceneType = None
        size = None
        tenantBusinessCode = None
        resp = GalaxybeltproductApi.getProductListPostApi(auditStatus=auditStatus, dateEnd=dateEnd, dateStart=dateStart, externalBizFrom=externalBizFrom, name=name, page=page, pageOrderList=pageOrderList, productId=productId, sceneType=sceneType, size=size, tenantBusinessCode=tenantBusinessCode)
        assert resp.status_code == 200

    def test_api_editBusinessCodeUsingPUT(self, config_obj, GalaxybeltproductApi):
        """  手动同步失败的sku """
        scene = None
        resp = GalaxybeltproductApi.editBusinessCodeUsingPUTPutApi(scene)
        assert resp.status_code == 200

    def test_api_modifyProduct(self, config_obj, GalaxybeltproductApi):
        """  修改产品 """
        barCode = None
        brand = None
        externalBizFrom = None
        height = None
        imgList = None
        length = None
        name = None
        packing = None
        productId = None
        tag = None
        tenantBusinessCode = None
        weight = None
        width = None
        resp = GalaxybeltproductApi.modifyProductPostApi(barCode=barCode, brand=brand, externalBizFrom=externalBizFrom, height=height, imgList=imgList, length=length, name=name, packing=packing, productId=productId, tag=tag, tenantBusinessCode=tenantBusinessCode, weight=weight, width=width)
        assert resp.status_code == 200

    def test_api_registerProduct(self, config_obj, GalaxybeltproductApi):
        """  注册产品 """
        barCode = None
        brand = None
        createTenantId = None
        createUserId = None
        externalBizFrom = None
        height = None
        imgList = None
        length = None
        name = None
        packing = None
        tag = None
        tenantBusinessCode = None
        tenantScene = None
        weight = None
        width = None
        resp = GalaxybeltproductApi.registerProductPostApi(barCode=barCode, brand=brand, createTenantId=createTenantId, createUserId=createUserId, externalBizFrom=externalBizFrom, height=height, imgList=imgList, length=length, name=name, packing=packing, tag=tag, tenantBusinessCode=tenantBusinessCode, tenantScene=tenantScene, weight=weight, width=width)
        assert resp.status_code == 200

    def test_api_resetSkuImage(self, config_obj, GalaxybeltproductApi):
        """  重置imageId """
        productId = None
        scene = None
        resp = GalaxybeltproductApi.resetSkuImagePutApi(productId, scene)
        assert resp.status_code == 200

    def test_api_getProductListByScene(self, config_obj, GalaxybeltproductApi):
        """  查询产品仓库列表 """
        brand = None
        dateEnd = None
        dateStart = None
        externalBizFrom = None
        packing = None
        page = None
        pageOrderList = None
        searchKey = None
        size = None
        resp = GalaxybeltproductApi.getProductListByScenePostApi(brand=brand, dateEnd=dateEnd, dateStart=dateStart, externalBizFrom=externalBizFrom, packing=packing, page=page, pageOrderList=pageOrderList, searchKey=searchKey, size=size)
        assert resp.status_code == 200

    def test_api_getProductDetail(self, config_obj, GalaxybeltproductApi):
        """  查询产品详情 """
        productId = None
        resp = GalaxybeltproductApi.getProductDetailGetApi(productId)
        assert resp.status_code == 200

    def test_api_delProduct(self, config_obj, GalaxybeltproductApi):
        """  删除物品 """
        productId = None
        resp = GalaxybeltproductApi.delProductDeleteApi(productId)
        assert resp.status_code == 200

    def test_api_transactProductAsync(self, config_obj, GalaxybeltproductApi):
        """  异步交易 """
        algorithmType = None
        callBackUrl = None
        deviceId = None
        externalBizFrom = None
        orderId = None
        skuCompose = None
        videoSet = None
        resp = GalaxybeltproductApi.transactProductAsyncPostApi(algorithmType=algorithmType, callBackUrl=callBackUrl, deviceId=deviceId, externalBizFrom=externalBizFrom, orderId=orderId, skuCompose=skuCompose, videoSet=videoSet)
        assert resp.status_code == 200

    def test_api_asyncTransactStatus(self, config_obj, GalaxybeltproductApi):
        """  查询异步交易状态 """
        transactCode = None
        resp = GalaxybeltproductApi.asyncTransactStatusGetApi(transactCode)
        assert resp.status_code == 200

    def test_api_cameraCheck(self, config_obj, GalaxybeltproductApi):
        """  相机检测 """
        imageInfo = None
        resp = GalaxybeltproductApi.cameraCheckPostApi(imageInfo=imageInfo)
        assert resp.status_code == 200

    def test_api_conflictProduct(self, config_obj, GalaxybeltproductApi):
        """  冲突检测 """
        sku_compose = None
        resp = GalaxybeltproductApi.conflictProductPostApi(sku_compose=sku_compose)
        assert resp.status_code == 200

    def test_api_RecognizeProduct(self, config_obj, GalaxybeltproductApi):
        """  检测图片中物品以及物品框 """
        deviceId = None
        externalBizFrom = None
        image = None
        orderId = None
        skuComposeIds = None
        resp = GalaxybeltproductApi.RecognizeProductPostApi(deviceId=deviceId, externalBizFrom=externalBizFrom, image=image, orderId=orderId, skuComposeIds=skuComposeIds)
        assert resp.status_code == 200

    def test_api_queryProductList(self, config_obj, GalaxybeltproductApi):
        """  查询所有已注册物品信息 """
        sku_id = None
        resp = GalaxybeltproductApi.queryProductListGetApi(sku_id=sku_id)
        assert resp.status_code == 200

    def test_api_RecognizeMultipleProduct(self, config_obj, GalaxybeltproductApi):
        """  检测多张图片中物品以及物品框 """
        deviceId = None
        externalBizFrom = None
        imageList = None
        orderId = None
        skuCompose = None
        resp = GalaxybeltproductApi.RecognizeMultipleProductPostApi(deviceId=deviceId, externalBizFrom=externalBizFrom, imageList=imageList, orderId=orderId, skuCompose=skuCompose)
        assert resp.status_code == 200

    def test_api_ProductNameSearch(self, config_obj, GalaxybeltproductApi):
        """  查询skuName """
        resp = GalaxybeltproductApi.ProductNameSearchPostApi()
        assert resp.status_code == 200

    def test_api_recognizeProduct(self, config_obj, GalaxybeltproductApi):
        """  识别 """
        device_id = None
        image_set1 = None
        orderId = None
        sku_compose = None
        resp = GalaxybeltproductApi.recognizeProductPostApi(device_id=device_id, image_set1=image_set1, orderId=orderId, sku_compose=sku_compose)
        assert resp.status_code == 200

    def test_api_replenishCheck(self, config_obj, GalaxybeltproductApi):
        """  补货检测 """
        deviceId = None
        mediaSets = None
        skuCompose = None
        template = None
        resp = GalaxybeltproductApi.replenishCheckPostApi(deviceId=deviceId, mediaSets=mediaSets, skuCompose=skuCompose, template=template)
        assert resp.status_code == 200

    def test_api_ProductSyncInfo(self, config_obj, GalaxybeltproductApi):
        """  查询同步的sku信息,同步到测试环境用 """
        resp = GalaxybeltproductApi.ProductSyncInfoGetApi()
        assert resp.status_code == 200

    def test_api_tenantConflict(self, config_obj, GalaxybeltproductApi):
        """  获取租户所有冲突信息 """
        resp = GalaxybeltproductApi.tenantConflictGetApi()
        assert resp.status_code == 200

    def test_api_compareProduct(self, config_obj, GalaxybeltproductApi):
        """  识别两组图片前后的商品数量变化，仅与传入模版商品比对 """
        algorithm_type = None
        compose_id = None
        device_id = None
        gravity = None
        image_set1 = None
        image_set2 = None
        image_set3 = None
        order_id = None
        sku_compose = None
        resp = GalaxybeltproductApi.compareProductPostApi(algorithm_type=algorithm_type, compose_id=compose_id, device_id=device_id, gravity=gravity, image_set1=image_set1, image_set2=image_set2, image_set3=image_set3, order_id=order_id, sku_compose=sku_compose)
        assert resp.status_code == 200

    def test_api_transactProductAsync_1(self, config_obj, GalaxybeltproductApi):
        """  异步交易 """
        algorithmType = None
        callBackUrl = None
        deviceId = None
        externalBizFrom = None
        orderId = None
        skuCompose = None
        videoSet = None
        resp = GalaxybeltproductApi.transactProductAsync_1PostApi(algorithmType=algorithmType, callBackUrl=callBackUrl, deviceId=deviceId, externalBizFrom=externalBizFrom, orderId=orderId, skuCompose=skuCompose, videoSet=videoSet)
        assert resp.status_code == 200

    def test_api_asyncTransactStatus_1(self, config_obj, GalaxybeltproductApi):
        """  查询异步交易状态 """
        transactCode = None
        resp = GalaxybeltproductApi.asyncTransactStatus_1GetApi(transactCode)
        assert resp.status_code == 200

    def test_api_cameraCheck_1(self, config_obj, GalaxybeltproductApi):
        """  相机检测 """
        imageInfo = None
        resp = GalaxybeltproductApi.cameraCheck_1PostApi(imageInfo=imageInfo)
        assert resp.status_code == 200

    def test_api_conflictProduct_1(self, config_obj, GalaxybeltproductApi):
        """  冲突检测 """
        sku_compose = None
        resp = GalaxybeltproductApi.conflictProduct_1PostApi(sku_compose=sku_compose)
        assert resp.status_code == 200

    def test_api_RecognizeProduct_1(self, config_obj, GalaxybeltproductApi):
        """  检测图片中物品以及物品框 """
        deviceId = None
        externalBizFrom = None
        image = None
        orderId = None
        skuComposeIds = None
        resp = GalaxybeltproductApi.RecognizeProduct_1PostApi(deviceId=deviceId, externalBizFrom=externalBizFrom, image=image, orderId=orderId, skuComposeIds=skuComposeIds)
        assert resp.status_code == 200

    def test_api_queryProductList_1(self, config_obj, GalaxybeltproductApi):
        """  查询所有已注册物品信息 """
        sku_id = None
        resp = GalaxybeltproductApi.queryProductList_1GetApi(sku_id=sku_id)
        assert resp.status_code == 200

    def test_api_RecognizeMultipleProduct_1(self, config_obj, GalaxybeltproductApi):
        """  检测多张图片中物品以及物品框 """
        deviceId = None
        externalBizFrom = None
        imageList = None
        orderId = None
        skuCompose = None
        resp = GalaxybeltproductApi.RecognizeMultipleProduct_1PostApi(deviceId=deviceId, externalBizFrom=externalBizFrom, imageList=imageList, orderId=orderId, skuCompose=skuCompose)
        assert resp.status_code == 200

    def test_api_ProductNameSearch_1(self, config_obj, GalaxybeltproductApi):
        """  查询skuName """
        resp = GalaxybeltproductApi.ProductNameSearch_1PostApi()
        assert resp.status_code == 200

    def test_api_recognizeProduct_1(self, config_obj, GalaxybeltproductApi):
        """  识别 """
        device_id = None
        image_set1 = None
        orderId = None
        sku_compose = None
        resp = GalaxybeltproductApi.recognizeProduct_1PostApi(device_id=device_id, image_set1=image_set1, orderId=orderId, sku_compose=sku_compose)
        assert resp.status_code == 200

    def test_api_replenishCheck_1(self, config_obj, GalaxybeltproductApi):
        """  补货检测 """
        deviceId = None
        mediaSets = None
        skuCompose = None
        template = None
        resp = GalaxybeltproductApi.replenishCheck_1PostApi(deviceId=deviceId, mediaSets=mediaSets, skuCompose=skuCompose, template=template)
        assert resp.status_code == 200

    def test_api_ProductSyncInfo_1(self, config_obj, GalaxybeltproductApi):
        """  查询同步的sku信息,同步到测试环境用 """
        resp = GalaxybeltproductApi.ProductSyncInfo_1GetApi()
        assert resp.status_code == 200

    def test_api_tenantConflict_1(self, config_obj, GalaxybeltproductApi):
        """  获取租户所有冲突信息 """
        resp = GalaxybeltproductApi.tenantConflict_1GetApi()
        assert resp.status_code == 200

    def test_api_compareProduct_1(self, config_obj, GalaxybeltproductApi):
        """  识别两组图片前后的商品数量变化，仅与传入模版商品比对 """
        algorithm_type = None
        compose_id = None
        device_id = None
        gravity = None
        image_set1 = None
        image_set2 = None
        image_set3 = None
        order_id = None
        sku_compose = None
        resp = GalaxybeltproductApi.compareProduct_1PostApi(algorithm_type=algorithm_type, compose_id=compose_id, device_id=device_id, gravity=gravity, image_set1=image_set1, image_set2=image_set2, image_set3=image_set3, order_id=order_id, sku_compose=sku_compose)
        assert resp.status_code == 200
