#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestGalaxyoplogParam(object):
    """ galaxyOplog Param测试"""

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
    ])
    def test_api_dayAggregationInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  查询当日调用量 """
        intef = GalaxyoplogApi.dayAggregationGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('endTime', 'invalidendTime'),
        ('endTime', ''),
        ('endTime', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('startTime', 'invalidstartTime'),
        ('startTime', ''),
        ('startTime', None),
    ])
    def test_api_rangeAggregationInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  查询统计周期调用量 """
        endTime = None
        externalBizFrom = None
        startTime = None
        intef = GalaxyoplogApi.rangeAggregationPostApi(endTime=endTime, externalBizFrom=externalBizFrom, startTime=startTime, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('endTime', 'invalidendTime'),
        ('endTime', ''),
        ('endTime', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('scene', 'invalidscene'),
        ('scene', ''),
        ('scene', None),
        ('startTime', 'invalidstartTime'),
        ('startTime', ''),
        ('startTime', None),
        ('tenant', 'invalidtenant'),
        ('tenant', ''),
        ('tenant', None),
    ])
    def test_api_overviewInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  场景数据概览 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        tenant = None
        intef = GalaxyoplogApi.overviewPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime, tenant=tenant, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('endTime', 'invalidendTime'),
        ('endTime', ''),
        ('endTime', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('scene', 'invalidscene'),
        ('scene', ''),
        ('scene', None),
        ('startTime', 'invalidstartTime'),
        ('startTime', ''),
        ('startTime', None),
        ('tenant', 'invalidtenant'),
        ('tenant', ''),
        ('tenant', None),
    ])
    def test_api_overviewExportInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  场景数据概览导出 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        tenant = None
        intef = GalaxyoplogApi.overviewExportPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime, tenant=tenant, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('endTime', 'invalidendTime'),
        ('endTime', ''),
        ('endTime', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('scene', 'invalidscene'),
        ('scene', ''),
        ('scene', None),
        ('startTime', 'invalidstartTime'),
        ('startTime', ''),
        ('startTime', None),
    ])
    def test_api_summaryInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  数据总览 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        intef = GalaxyoplogApi.summaryPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('endTime', 'invalidendTime'),
        ('endTime', ''),
        ('endTime', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('scene', 'invalidscene'),
        ('scene', ''),
        ('scene', None),
        ('startTime', 'invalidstartTime'),
        ('startTime', ''),
        ('startTime', None),
    ])
    def test_api_summaryExportInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  数据总览导出 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        intef = GalaxyoplogApi.summaryExportPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('endTime', 'invalidendTime'),
        ('endTime', ''),
        ('endTime', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('scene', 'invalidscene'),
        ('scene', ''),
        ('scene', None),
        ('startTime', 'invalidstartTime'),
        ('startTime', ''),
        ('startTime', None),
        ('tenant', 'invalidtenant'),
        ('tenant', ''),
        ('tenant', None),
    ])
    def test_api_statisticInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  租户数据概览 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        tenant = None
        intef = GalaxyoplogApi.statisticPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime, tenant=tenant, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('endTime', 'invalidendTime'),
        ('endTime', ''),
        ('endTime', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('scene', 'invalidscene'),
        ('scene', ''),
        ('scene', None),
        ('startTime', 'invalidstartTime'),
        ('startTime', ''),
        ('startTime', None),
        ('tenant', 'invalidtenant'),
        ('tenant', ''),
        ('tenant', None),
    ])
    def test_api_tenantStatisticExportInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  租户数据概览导出 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        tenant = None
        intef = GalaxyoplogApi.tenantStatisticExportPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime, tenant=tenant, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('business_order_id', 'invalidbusiness_order_id'),
        ('business_order_id', ''),
        ('business_order_id', None),
        ('business_order_type', 'invalidbusiness_order_type'),
        ('business_order_type', ''),
        ('business_order_type', None),
        ('business_reporter_id', 'invalidbusiness_reporter_id'),
        ('business_reporter_id', ''),
        ('business_reporter_id', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('remark', 'invalidremark'),
        ('remark', ''),
        ('remark', None),
        ('request_id', 'invalidrequest_id'),
        ('request_id', ''),
        ('request_id', None),
    ])
    def test_api_opLogAbnormalInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  上报异常数据 """
        business_order_id = None
        business_order_type = None
        business_reporter_id = None
        device_id = None
        externalBizFrom = None
        remark = None
        request_id = None
        intef = GalaxyoplogApi.opLogAbnormalPostApi(business_order_id=business_order_id, business_order_type=business_order_type, business_reporter_id=business_reporter_id, device_id=device_id, externalBizFrom=externalBizFrom, remark=remark, request_id=request_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('dateEnd', 'invaliddateEnd'),
        ('dateEnd', ''),
        ('dateEnd', None),
        ('dateStart', 'invaliddateStart'),
        ('dateStart', ''),
        ('dateStart', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('pageOrderList', 'invalidpageOrderList'),
        ('pageOrderList', ''),
        ('pageOrderList', None),
        ('requestId', 'invalidrequestId'),
        ('requestId', ''),
        ('requestId', None),
        ('scene', 'invalidscene'),
        ('scene', ''),
        ('scene', None),
        ('size', 'invalidsize'),
        ('size', ''),
        ('size', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
        ('tenantInfo', 'invalidtenantInfo'),
        ('tenantInfo', ''),
        ('tenantInfo', None),
    ])
    def test_api_abnormalLogsQueryInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  查询所有异常上报信息 """
        dateEnd = None
        dateStart = None
        externalBizFrom = None
        orderId = None
        page = None
        pageOrderList = None
        requestId = None
        scene = None
        size = None
        status = None
        tenantInfo = None
        intef = GalaxyoplogApi.abnormalLogsQueryPostApi(dateEnd=dateEnd, dateStart=dateStart, externalBizFrom=externalBizFrom, orderId=orderId, page=page, pageOrderList=pageOrderList, requestId=requestId, scene=scene, size=size, status=status, tenantInfo=tenantInfo, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('errorDescription', 'invaliderrorDescription'),
        ('errorDescription', ''),
        ('errorDescription', None),
        ('errorType', 'invaliderrorType'),
        ('errorType', ''),
        ('errorType', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_abnormalLogProcessInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  处理异常上报 """
        errorDescription = None
        errorType = None
        externalBizFrom = None
        id = None
        intef = GalaxyoplogApi.abnormalLogProcessPostApi(errorDescription=errorDescription, errorType=errorType, externalBizFrom=externalBizFrom, id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('algoCode', 'invalidalgoCode'),
        ('algoCode', ''),
        ('algoCode', None),
        ('costMax', 'invalidcostMax'),
        ('costMax', ''),
        ('costMax', None),
        ('costMin', 'invalidcostMin'),
        ('costMin', ''),
        ('costMin', None),
        ('dateEnd', 'invaliddateEnd'),
        ('dateEnd', ''),
        ('dateEnd', None),
        ('dateStart', 'invaliddateStart'),
        ('dateStart', ''),
        ('dateStart', None),
        ('deviceId', 'invaliddeviceId'),
        ('deviceId', ''),
        ('deviceId', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('host', 'invalidhost'),
        ('host', ''),
        ('host', None),
        ('method', 'invalidmethod'),
        ('method', ''),
        ('method', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('pageOrderList', 'invalidpageOrderList'),
        ('pageOrderList', ''),
        ('pageOrderList', None),
        ('scene', 'invalidscene'),
        ('scene', ''),
        ('scene', None),
        ('size', 'invalidsize'),
        ('size', ''),
        ('size', None),
        ('statusCode', 'invalidstatusCode'),
        ('statusCode', ''),
        ('statusCode', None),
        ('tag', 'invalidtag'),
        ('tag', ''),
        ('tag', None),
        ('targetPath', 'invalidtargetPath'),
        ('targetPath', ''),
        ('targetPath', None),
        ('timeStampMax', 'invalidtimeStampMax'),
        ('timeStampMax', ''),
        ('timeStampMax', None),
        ('timeStampMin', 'invalidtimeStampMin'),
        ('timeStampMin', ''),
        ('timeStampMin', None),
    ])
    def test_api_opLogIdQueryInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  查询requestId """
        algoCode = None
        costMax = None
        costMin = None
        dateEnd = None
        dateStart = None
        deviceId = None
        externalBizFrom = None
        host = None
        method = None
        orderId = None
        page = None
        pageOrderList = None
        scene = None
        size = None
        statusCode = None
        tag = None
        targetPath = None
        timeStampMax = None
        timeStampMin = None
        intef = GalaxyoplogApi.opLogIdQueryPostApi(algoCode=algoCode, costMax=costMax, costMin=costMin, dateEnd=dateEnd, dateStart=dateStart, deviceId=deviceId, externalBizFrom=externalBizFrom, host=host, method=method, orderId=orderId, page=page, pageOrderList=pageOrderList, scene=scene, size=size, statusCode=statusCode, tag=tag, targetPath=targetPath, timeStampMax=timeStampMax, timeStampMin=timeStampMin, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('dataIgnore', 'invaliddataIgnore'),
        ('dataIgnore', ''),
        ('dataIgnore', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('requestIds', 'invalidrequestIds'),
        ('requestIds', ''),
        ('requestIds', None),
    ])
    def test_api_opLogsQueryInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  根据requestIds查询opLog信息 """
        dataIgnore = None
        externalBizFrom = None
        requestIds = None
        intef = GalaxyoplogApi.opLogsQueryPostApi(dataIgnore=dataIgnore, externalBizFrom=externalBizFrom, requestIds=requestIds, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('dateEnd', 'invaliddateEnd'),
        ('dateEnd', ''),
        ('dateEnd', None),
        ('dateStart', 'invaliddateStart'),
        ('dateStart', ''),
        ('dateStart', None),
        ('deviceNo', 'invaliddeviceNo'),
        ('deviceNo', ''),
        ('deviceNo', None),
        ('endTime', 'invalidendTime'),
        ('endTime', ''),
        ('endTime', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('orderId', 'invalidorderId'),
        ('orderId', ''),
        ('orderId', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('pageOrderList', 'invalidpageOrderList'),
        ('pageOrderList', ''),
        ('pageOrderList', None),
        ('requestId', 'invalidrequestId'),
        ('requestId', ''),
        ('requestId', None),
        ('requestType', 'invalidrequestType'),
        ('requestType', ''),
        ('requestType', None),
        ('size', 'invalidsize'),
        ('size', ''),
        ('size', None),
        ('startTime', 'invalidstartTime'),
        ('startTime', ''),
        ('startTime', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
        ('warningCode', 'invalidwarningCode'),
        ('warningCode', ''),
        ('warningCode', None),
        ('whetherError', 'invalidwhetherError'),
        ('whetherError', ''),
        ('whetherError', None),
    ])
    def test_api_opLogListQueryInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  查询租户oplog 列表 """
        dateEnd = None
        dateStart = None
        deviceNo = None
        endTime = None
        externalBizFrom = None
        orderId = None
        page = None
        pageOrderList = None
        requestId = None
        requestType = None
        size = None
        startTime = None
        status = None
        warningCode = None
        whetherError = None
        intef = GalaxyoplogApi.opLogListQueryPostApi(dateEnd=dateEnd, dateStart=dateStart, deviceNo=deviceNo, endTime=endTime, externalBizFrom=externalBizFrom, orderId=orderId, page=page, pageOrderList=pageOrderList, requestId=requestId, requestType=requestType, size=size, startTime=startTime, status=status, warningCode=warningCode, whetherError=whetherError, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('dataIgnore', 'invaliddataIgnore'),
        ('dataIgnore', ''),
        ('dataIgnore', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('requestIds', 'invalidrequestIds'),
        ('requestIds', ''),
        ('requestIds', None),
    ])
    def test_api_opLogsQueryWithProductInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  根据requestIds查询opLog信息附加商品信息 """
        dataIgnore = None
        externalBizFrom = None
        requestIds = None
        intef = GalaxyoplogApi.opLogsQueryWithProductPostApi(dataIgnore=dataIgnore, externalBizFrom=externalBizFrom, requestIds=requestIds, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('requestId', 'invalidrequestId'),
        ('requestId', ''),
        ('requestId', None),
        ('taskName', 'invalidtaskName'),
        ('taskName', ''),
        ('taskName', None),
    ])
    def test_api_opLogSyncInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  同步oplog """
        externalBizFrom = None
        requestId = None
        taskName = None
        intef = GalaxyoplogApi.opLogSyncPostApi(externalBizFrom=externalBizFrom, requestId=requestId, taskName=taskName, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('dateEnd', 'invaliddateEnd'),
        ('dateEnd', ''),
        ('dateEnd', None),
        ('dateStart', 'invaliddateStart'),
        ('dateStart', ''),
        ('dateStart', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('pageOrderList', 'invalidpageOrderList'),
        ('pageOrderList', ''),
        ('pageOrderList', None),
        ('size', 'invalidsize'),
        ('size', ''),
        ('size', None),
    ])
    def test_api_opLogTaskQueryInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  查询oplog同步任务 """
        dateEnd = None
        dateStart = None
        externalBizFrom = None
        page = None
        pageOrderList = None
        size = None
        intef = GalaxyoplogApi.opLogTaskQueryPostApi(dateEnd=dateEnd, dateStart=dateStart, externalBizFrom=externalBizFrom, page=page, pageOrderList=pageOrderList, size=size, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('business_order_id', 'invalidbusiness_order_id'),
        ('business_order_id', ''),
        ('business_order_id', None),
        ('business_order_type', 'invalidbusiness_order_type'),
        ('business_order_type', ''),
        ('business_order_type', None),
        ('business_reporter_id', 'invalidbusiness_reporter_id'),
        ('business_reporter_id', ''),
        ('business_reporter_id', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('remark', 'invalidremark'),
        ('remark', ''),
        ('remark', None),
        ('request_id', 'invalidrequest_id'),
        ('request_id', ''),
        ('request_id', None),
    ])
    def test_api_opLogAbnormal_1InvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  上报异常数据 """
        business_order_id = None
        business_order_type = None
        business_reporter_id = None
        device_id = None
        externalBizFrom = None
        remark = None
        request_id = None
        intef = GalaxyoplogApi.opLogAbnormal_1PostApi(business_order_id=business_order_id, business_order_type=business_order_type, business_reporter_id=business_reporter_id, device_id=device_id, externalBizFrom=externalBizFrom, remark=remark, request_id=request_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requestId', 'invalidrequestId'),
        ('requestId', ''),
        ('requestId', None),
    ])
    def test_api_opLogQueryInvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  根据requestId查询opLog信息 """
        requestId = None
        intef = GalaxyoplogApi.opLogQueryGetApi(requestId=requestId, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('business_order_id', 'invalidbusiness_order_id'),
        ('business_order_id', ''),
        ('business_order_id', None),
        ('business_order_type', 'invalidbusiness_order_type'),
        ('business_order_type', ''),
        ('business_order_type', None),
        ('business_reporter_id', 'invalidbusiness_reporter_id'),
        ('business_reporter_id', ''),
        ('business_reporter_id', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('externalBizFrom', 'invalidexternalBizFrom'),
        ('externalBizFrom', ''),
        ('externalBizFrom', None),
        ('remark', 'invalidremark'),
        ('remark', ''),
        ('remark', None),
        ('request_id', 'invalidrequest_id'),
        ('request_id', ''),
        ('request_id', None),
    ])
    def test_api_opLogAbnormal_2InvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  上报异常数据 """
        business_order_id = None
        business_order_type = None
        business_reporter_id = None
        device_id = None
        externalBizFrom = None
        remark = None
        request_id = None
        intef = GalaxyoplogApi.opLogAbnormal_2PostApi(business_order_id=business_order_id, business_order_type=business_order_type, business_reporter_id=business_reporter_id, device_id=device_id, externalBizFrom=externalBizFrom, remark=remark, request_id=request_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requestId', 'invalidrequestId'),
        ('requestId', ''),
        ('requestId', None),
    ])
    def test_api_opLogQuery_1InvalidParam(self, invalidParam, config_obj, GalaxyoplogApi):
        """  根据requestId查询opLog信息 """
        requestId = None
        intef = GalaxyoplogApi.opLogQuery_1GetApi(requestId=requestId, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200
