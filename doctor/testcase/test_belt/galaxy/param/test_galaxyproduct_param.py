#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestGalaxyproductParam(object):
    """ galaxyProduct Param测试"""

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

    @pytest.mark.parametrize("invalidParam", [
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('fileNameList', 'invalidfileNameList'),
        ('fileNameList', ''),
        ('fileNameList', None),
    ])
    def test_api_modifyProduct_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  获取图片下载链接 """
        externalBizFrom = None
        fileNameList = None
        intef = GalaxyproductApi.modifyProduct_1PostApi(externalBizFrom=externalBizFrom, fileNameList=fileNameList, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('fileNameList', 'invalidfileNameList'),
        ('fileNameList', ''),
        ('fileNameList', None),
    ])
    def test_api_getProductUploadUrlInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  获取物品上传链接 """
        externalBizFrom = None
        fileNameList = None
        intef = GalaxyproductApi.getProductUploadUrlPostApi(externalBizFrom=externalBizFrom, fileNameList=fileNameList, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('productIdList', 'invalidproductIdList'),
        ('productIdList', ''),
        ('productIdList', None),
    ])
    def test_api_addProductInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  添加产品 """
        externalBizFrom = None
        productIdList = None
        intef = GalaxyproductApi.addProductPostApi(externalBizFrom=externalBizFrom, productIdList=productIdList, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('productIdList', 'invalidproductIdList'),
        ('productIdList', ''),
        ('productIdList', None),
    ])
    def test_api_batchDelProductInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  批量删除物品 """
        externalBizFrom = None
        productIdList = None
        intef = GalaxyproductApi.batchDelProductPostApi(externalBizFrom=externalBizFrom, productIdList=productIdList, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_编辑businessCodeInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  编辑businessCode """
        productId = None
        intef = GalaxyproductApi.editBusinessCodePutApi(productId, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('auditStatus', 'invalidauditStatus'),
        ('auditStatus', ''),
        ('auditStatus', None),
        ('dateEnd', 'invaliddateEnd'),
        ('dateEnd', ''),
        ('dateEnd', None),
        ('dateStart', 'invaliddateStart'),
        ('dateStart', ''),
        ('dateStart', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('pageOrderList', 'invalidpageOrderList'),
        ('pageOrderList', ''),
        ('pageOrderList', None),
        ('productId', 'invalidproductId'),
        ('productId', ''),
        ('productId', None),
        ('sceneType', 'invalidsceneType'),
        ('sceneType', ''),
        ('sceneType', None),
        ('size', 'invalidsize'),
        ('size', ''),
        ('size', None),
        ('tenantBusinessCode', 'invalidtenantBusinessCode'),
        ('tenantBusinessCode', ''),
        ('tenantBusinessCode', None),
    ])
    def test_api_getProductListInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
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
        intef = GalaxyproductApi.getProductListPostApi(auditStatus=auditStatus, dateEnd=dateEnd, dateStart=dateStart, externalBizFrom=externalBizFrom, name=name, page=page, pageOrderList=pageOrderList, productId=productId, sceneType=sceneType, size=size, tenantBusinessCode=tenantBusinessCode, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_editBusinessCodeUsingPUTInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  手动同步失败的sku """
        scene = None
        intef = GalaxyproductApi.editBusinessCodeUsingPUTPutApi(scene, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('barCode', 'invalidbarCode'),
        ('barCode', ''),
        ('barCode', None),
        ('brand', 'invalidbrand'),
        ('brand', ''),
        ('brand', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('height', 'invalidheight'),
        ('height', ''),
        ('height', None),
        ('imgList', 'invalidimgList'),
        ('imgList', ''),
        ('imgList', None),
        ('length', 'invalidlength'),
        ('length', ''),
        ('length', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('packing', 'invalidpacking'),
        ('packing', ''),
        ('packing', None),
        ('productId', 'invalidproductId'),
        ('productId', ''),
        ('productId', None),
        ('tag', 'invalidtag'),
        ('tag', ''),
        ('tag', None),
        ('tenantBusinessCode', 'invalidtenantBusinessCode'),
        ('tenantBusinessCode', ''),
        ('tenantBusinessCode', None),
        ('weight', 'invalidweight'),
        ('weight', ''),
        ('weight', None),
        ('width', 'invalidwidth'),
        ('width', ''),
        ('width', None),
    ])
    def test_api_modifyProductInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
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
        intef = GalaxyproductApi.modifyProductPostApi(barCode=barCode, brand=brand, externalBizFrom=externalBizFrom, height=height, imgList=imgList, length=length, name=name, packing=packing, productId=productId, tag=tag, tenantBusinessCode=tenantBusinessCode, weight=weight, width=width, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('barCode', 'invalidbarCode'),
        ('barCode', ''),
        ('barCode', None),
        ('brand', 'invalidbrand'),
        ('brand', ''),
        ('brand', None),
        ('createTenantId', 'invalidcreateTenantId'),
        ('createTenantId', ''),
        ('createTenantId', None),
        ('createUserId', 'invalidcreateUserId'),
        ('createUserId', ''),
        ('createUserId', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('height', 'invalidheight'),
        ('height', ''),
        ('height', None),
        ('imgList', 'invalidimgList'),
        ('imgList', ''),
        ('imgList', None),
        ('length', 'invalidlength'),
        ('length', ''),
        ('length', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('packing', 'invalidpacking'),
        ('packing', ''),
        ('packing', None),
        ('tag', 'invalidtag'),
        ('tag', ''),
        ('tag', None),
        ('tenantBusinessCode', 'invalidtenantBusinessCode'),
        ('tenantBusinessCode', ''),
        ('tenantBusinessCode', None),
        ('tenantScene', 'invalidtenantScene'),
        ('tenantScene', ''),
        ('tenantScene', None),
        ('weight', 'invalidweight'),
        ('weight', ''),
        ('weight', None),
        ('width', 'invalidwidth'),
        ('width', ''),
        ('width', None),
    ])
    def test_api_registerProductInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
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
        intef = GalaxyproductApi.registerProductPostApi(barCode=barCode, brand=brand, createTenantId=createTenantId, createUserId=createUserId, externalBizFrom=externalBizFrom, height=height, imgList=imgList, length=length, name=name, packing=packing, tag=tag, tenantBusinessCode=tenantBusinessCode, tenantScene=tenantScene, weight=weight, width=width, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_resetSkuImageInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  重置imageId """
        productId = None
        scene = None
        intef = GalaxyproductApi.resetSkuImagePutApi(productId, scene, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('brand', 'invalidbrand'),
        ('brand', ''),
        ('brand', None),
        ('dateEnd', 'invaliddateEnd'),
        ('dateEnd', ''),
        ('dateEnd', None),
        ('dateStart', 'invaliddateStart'),
        ('dateStart', ''),
        ('dateStart', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('packing', 'invalidpacking'),
        ('packing', ''),
        ('packing', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('pageOrderList', 'invalidpageOrderList'),
        ('pageOrderList', ''),
        ('pageOrderList', None),
        ('searchKey', 'invalidsearchKey'),
        ('searchKey', ''),
        ('searchKey', None),
        ('size', 'invalidsize'),
        ('size', ''),
        ('size', None),
    ])
    def test_api_getProductListBySceneInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
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
        intef = GalaxyproductApi.getProductListByScenePostApi(brand=brand, dateEnd=dateEnd, dateStart=dateStart, externalBizFrom=externalBizFrom, packing=packing, page=page, pageOrderList=pageOrderList, searchKey=searchKey, size=size, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_getProductDetailInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  查询产品详情 """
        productId = None
        intef = GalaxyproductApi.getProductDetailGetApi(productId, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_delProductInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  删除物品 """
        productId = None
        intef = GalaxyproductApi.delProductDeleteApi(productId, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('algorithmType', 'invalidalgorithmType'),
        ('algorithmType', ''),
        ('algorithmType', None),
        ('callBackUrl', 'invalidcallBackUrl'),
        ('callBackUrl', ''),
        ('callBackUrl', None),
        ('deviceId', 'invaliddeviceId'),
        ('deviceId', ''),
        ('deviceId', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('skuCompose', 'invalidskuCompose'),
        ('skuCompose', ''),
        ('skuCompose', None),
        ('videoSet', 'invalidvideoSet'),
        ('videoSet', ''),
        ('videoSet', None),
    ])
    def test_api_transactProductAsyncInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  异步交易 """
        algorithmType = None
        callBackUrl = None
        deviceId = None
        externalBizFrom = None
        orderId = None
        skuCompose = None
        videoSet = None
        intef = GalaxyproductApi.transactProductAsyncPostApi(algorithmType=algorithmType, callBackUrl=callBackUrl, deviceId=deviceId, externalBizFrom=externalBizFrom, orderId=orderId, skuCompose=skuCompose, videoSet=videoSet, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_asyncTransactStatusInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  查询异步交易状态 """
        transactCode = None
        intef = GalaxyproductApi.asyncTransactStatusGetApi(transactCode, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('imageInfo', 'invalidimageInfo'),
        ('imageInfo', ''),
        ('imageInfo', None),
    ])
    def test_api_cameraCheckInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  相机检测 """
        imageInfo = None
        intef = GalaxyproductApi.cameraCheckPostApi(imageInfo=imageInfo, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('sku_compose', 'invalidsku_compose'),
        ('sku_compose', ''),
        ('sku_compose', None),
    ])
    def test_api_conflictProductInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  冲突检测 """
        sku_compose = None
        intef = GalaxyproductApi.conflictProductPostApi(sku_compose=sku_compose, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('deviceId', 'invaliddeviceId'),
        ('deviceId', ''),
        ('deviceId', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('skuComposeIds', 'invalidskuComposeIds'),
        ('skuComposeIds', ''),
        ('skuComposeIds', None),
    ])
    def test_api_RecognizeProductInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  检测图片中物品以及物品框 """
        deviceId = None
        externalBizFrom = None
        image = None
        orderId = None
        skuComposeIds = None
        intef = GalaxyproductApi.RecognizeProductPostApi(deviceId=deviceId, externalBizFrom=externalBizFrom, image=image, orderId=orderId, skuComposeIds=skuComposeIds, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('sku_id', 'invalidsku_id'),
        ('sku_id', ''),
        ('sku_id', None),
    ])
    def test_api_queryProductListInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  查询所有已注册物品信息 """
        sku_id = None
        intef = GalaxyproductApi.queryProductListGetApi(sku_id=sku_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('deviceId', 'invaliddeviceId'),
        ('deviceId', ''),
        ('deviceId', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('imageList', 'invalidimageList'),
        ('imageList', ''),
        ('imageList', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('skuCompose', 'invalidskuCompose'),
        ('skuCompose', ''),
        ('skuCompose', None),
    ])
    def test_api_RecognizeMultipleProductInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  检测多张图片中物品以及物品框 """
        deviceId = None
        externalBizFrom = None
        imageList = None
        orderId = None
        skuCompose = None
        intef = GalaxyproductApi.RecognizeMultipleProductPostApi(deviceId=deviceId, externalBizFrom=externalBizFrom, imageList=imageList, orderId=orderId, skuCompose=skuCompose, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ProductNameSearchInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  查询skuName """
        intef = GalaxyproductApi.ProductNameSearchPostApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('image_set1', 'invalidimage_set1'),
        ('image_set1', ''),
        ('image_set1', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('sku_compose', 'invalidsku_compose'),
        ('sku_compose', ''),
        ('sku_compose', None),
    ])
    def test_api_recognizeProductInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  识别 """
        device_id = None
        image_set1 = None
        orderId = None
        sku_compose = None
        intef = GalaxyproductApi.recognizeProductPostApi(device_id=device_id, image_set1=image_set1, orderId=orderId, sku_compose=sku_compose, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('deviceId', 'invaliddeviceId'),
        ('deviceId', ''),
        ('deviceId', None),
        ('mediaSets', 'invalidmediaSets'),
        ('mediaSets', ''),
        ('mediaSets', None),
        ('skuCompose', 'invalidskuCompose'),
        ('skuCompose', ''),
        ('skuCompose', None),
        ('template', 'invalidtemplate'),
        ('template', ''),
        ('template', None),
    ])
    def test_api_replenishCheckInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  补货检测 """
        deviceId = None
        mediaSets = None
        skuCompose = None
        template = None
        intef = GalaxyproductApi.replenishCheckPostApi(deviceId=deviceId, mediaSets=mediaSets, skuCompose=skuCompose, template=template, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ProductSyncInfoInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  查询同步的sku信息,同步到测试环境用 """
        intef = GalaxyproductApi.ProductSyncInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_tenantConflictInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  获取租户所有冲突信息 """
        intef = GalaxyproductApi.tenantConflictGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('algorithm_type', 'invalidalgorithm_type'),
        ('algorithm_type', ''),
        ('algorithm_type', None),
        ('compose_id', 'invalidcompose_id'),
        ('compose_id', ''),
        ('compose_id', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('gravity', 'invalidgravity'),
        ('gravity', ''),
        ('gravity', None),
        ('image_set1', 'invalidimage_set1'),
        ('image_set1', ''),
        ('image_set1', None),
        ('image_set2', 'invalidimage_set2'),
        ('image_set2', ''),
        ('image_set2', None),
        ('image_set3', 'invalidimage_set3'),
        ('image_set3', ''),
        ('image_set3', None),
        ('order_id', 'invalidorder_id'),
        ('order_id', ''),
        ('order_id', None),
        ('sku_compose', 'invalidsku_compose'),
        ('sku_compose', ''),
        ('sku_compose', None),
    ])
    def test_api_compareProductInvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
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
        intef = GalaxyproductApi.compareProductPostApi(algorithm_type=algorithm_type, compose_id=compose_id, device_id=device_id, gravity=gravity, image_set1=image_set1, image_set2=image_set2, image_set3=image_set3, order_id=order_id, sku_compose=sku_compose, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('algorithmType', 'invalidalgorithmType'),
        ('algorithmType', ''),
        ('algorithmType', None),
        ('callBackUrl', 'invalidcallBackUrl'),
        ('callBackUrl', ''),
        ('callBackUrl', None),
        ('deviceId', 'invaliddeviceId'),
        ('deviceId', ''),
        ('deviceId', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('skuCompose', 'invalidskuCompose'),
        ('skuCompose', ''),
        ('skuCompose', None),
        ('videoSet', 'invalidvideoSet'),
        ('videoSet', ''),
        ('videoSet', None),
    ])
    def test_api_transactProductAsync_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  异步交易 """
        algorithmType = None
        callBackUrl = None
        deviceId = None
        externalBizFrom = None
        orderId = None
        skuCompose = None
        videoSet = None
        intef = GalaxyproductApi.transactProductAsync_1PostApi(algorithmType=algorithmType, callBackUrl=callBackUrl, deviceId=deviceId, externalBizFrom=externalBizFrom, orderId=orderId, skuCompose=skuCompose, videoSet=videoSet, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_asyncTransactStatus_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  查询异步交易状态 """
        transactCode = None
        intef = GalaxyproductApi.asyncTransactStatus_1GetApi(transactCode, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('imageInfo', 'invalidimageInfo'),
        ('imageInfo', ''),
        ('imageInfo', None),
    ])
    def test_api_cameraCheck_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  相机检测 """
        imageInfo = None
        intef = GalaxyproductApi.cameraCheck_1PostApi(imageInfo=imageInfo, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('sku_compose', 'invalidsku_compose'),
        ('sku_compose', ''),
        ('sku_compose', None),
    ])
    def test_api_conflictProduct_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  冲突检测 """
        sku_compose = None
        intef = GalaxyproductApi.conflictProduct_1PostApi(sku_compose=sku_compose, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('deviceId', 'invaliddeviceId'),
        ('deviceId', ''),
        ('deviceId', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('skuComposeIds', 'invalidskuComposeIds'),
        ('skuComposeIds', ''),
        ('skuComposeIds', None),
    ])
    def test_api_RecognizeProduct_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  检测图片中物品以及物品框 """
        deviceId = None
        externalBizFrom = None
        image = None
        orderId = None
        skuComposeIds = None
        intef = GalaxyproductApi.RecognizeProduct_1PostApi(deviceId=deviceId, externalBizFrom=externalBizFrom, image=image, orderId=orderId, skuComposeIds=skuComposeIds, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('sku_id', 'invalidsku_id'),
        ('sku_id', ''),
        ('sku_id', None),
    ])
    def test_api_queryProductList_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  查询所有已注册物品信息 """
        sku_id = None
        intef = GalaxyproductApi.queryProductList_1GetApi(sku_id=sku_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('deviceId', 'invaliddeviceId'),
        ('deviceId', ''),
        ('deviceId', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('imageList', 'invalidimageList'),
        ('imageList', ''),
        ('imageList', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('skuCompose', 'invalidskuCompose'),
        ('skuCompose', ''),
        ('skuCompose', None),
    ])
    def test_api_RecognizeMultipleProduct_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  检测多张图片中物品以及物品框 """
        deviceId = None
        externalBizFrom = None
        imageList = None
        orderId = None
        skuCompose = None
        intef = GalaxyproductApi.RecognizeMultipleProduct_1PostApi(deviceId=deviceId, externalBizFrom=externalBizFrom, imageList=imageList, orderId=orderId, skuCompose=skuCompose, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ProductNameSearch_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  查询skuName """
        intef = GalaxyproductApi.ProductNameSearch_1PostApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('image_set1', 'invalidimage_set1'),
        ('image_set1', ''),
        ('image_set1', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('sku_compose', 'invalidsku_compose'),
        ('sku_compose', ''),
        ('sku_compose', None),
    ])
    def test_api_recognizeProduct_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  识别 """
        device_id = None
        image_set1 = None
        orderId = None
        sku_compose = None
        intef = GalaxyproductApi.recognizeProduct_1PostApi(device_id=device_id, image_set1=image_set1, orderId=orderId, sku_compose=sku_compose, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('deviceId', 'invaliddeviceId'),
        ('deviceId', ''),
        ('deviceId', None),
        ('mediaSets', 'invalidmediaSets'),
        ('mediaSets', ''),
        ('mediaSets', None),
        ('skuCompose', 'invalidskuCompose'),
        ('skuCompose', ''),
        ('skuCompose', None),
        ('template', 'invalidtemplate'),
        ('template', ''),
        ('template', None),
    ])
    def test_api_replenishCheck_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  补货检测 """
        deviceId = None
        mediaSets = None
        skuCompose = None
        template = None
        intef = GalaxyproductApi.replenishCheck_1PostApi(deviceId=deviceId, mediaSets=mediaSets, skuCompose=skuCompose, template=template, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ProductSyncInfo_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  查询同步的sku信息,同步到测试环境用 """
        intef = GalaxyproductApi.ProductSyncInfo_1GetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_tenantConflict_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
        """  获取租户所有冲突信息 """
        intef = GalaxyproductApi.tenantConflict_1GetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('algorithm_type', 'invalidalgorithm_type'),
        ('algorithm_type', ''),
        ('algorithm_type', None),
        ('compose_id', 'invalidcompose_id'),
        ('compose_id', ''),
        ('compose_id', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('gravity', 'invalidgravity'),
        ('gravity', ''),
        ('gravity', None),
        ('image_set1', 'invalidimage_set1'),
        ('image_set1', ''),
        ('image_set1', None),
        ('image_set2', 'invalidimage_set2'),
        ('image_set2', ''),
        ('image_set2', None),
        ('image_set3', 'invalidimage_set3'),
        ('image_set3', ''),
        ('image_set3', None),
        ('order_id', 'invalidorder_id'),
        ('order_id', ''),
        ('order_id', None),
        ('sku_compose', 'invalidsku_compose'),
        ('sku_compose', ''),
        ('sku_compose', None),
    ])
    def test_api_compareProduct_1InvalidParam(self, invalidParam, config_obj, GalaxyproductApi):
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
        intef = GalaxyproductApi.compareProduct_1PostApi(algorithm_type=algorithm_type, compose_id=compose_id, device_id=device_id, gravity=gravity, image_set1=image_set1, image_set2=image_set2, image_set3=image_set3, order_id=order_id, sku_compose=sku_compose, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
