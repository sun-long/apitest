#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestGalaxybeltoplogApi(object):
    """ galaxyBeltOplog Api测试"""

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

    def test_api_dayAggregation(self, config_obj, GalaxybeltoplogApi):
        """  查询当日调用量 """
        resp = GalaxybeltoplogApi.dayAggregationGetApi()
        assert resp.status_code == 200

    def test_api_rangeAggregation(self, config_obj, GalaxybeltoplogApi):
        """  查询统计周期调用量 """
        endTime = None
        externalBizFrom = None
        startTime = None
        resp = GalaxybeltoplogApi.rangeAggregationPostApi(endTime=endTime, externalBizFrom=externalBizFrom, startTime=startTime)
        assert resp.status_code == 200

    def test_api_overview(self, config_obj, GalaxybeltoplogApi):
        """  场景数据概览 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        tenant = None
        resp = GalaxybeltoplogApi.overviewPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime, tenant=tenant)
        assert resp.status_code == 200

    def test_api_overviewExport(self, config_obj, GalaxybeltoplogApi):
        """  场景数据概览导出 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        tenant = None
        resp = GalaxybeltoplogApi.overviewExportPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime, tenant=tenant)
        assert resp.status_code == 200

    def test_api_summary(self, config_obj, GalaxybeltoplogApi):
        """  数据总览 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        resp = GalaxybeltoplogApi.summaryPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime)
        assert resp.status_code == 200

    def test_api_summaryExport(self, config_obj, GalaxybeltoplogApi):
        """  数据总览导出 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        resp = GalaxybeltoplogApi.summaryExportPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime)
        assert resp.status_code == 200

    def test_api_statistic(self, config_obj, GalaxybeltoplogApi):
        """  租户数据概览 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        tenant = None
        resp = GalaxybeltoplogApi.statisticPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime, tenant=tenant)
        assert resp.status_code == 200

    def test_api_tenantStatisticExport(self, config_obj, GalaxybeltoplogApi):
        """  租户数据概览导出 """
        endTime = None
        externalBizFrom = None
        scene = None
        startTime = None
        tenant = None
        resp = GalaxybeltoplogApi.tenantStatisticExportPostApi(endTime=endTime, externalBizFrom=externalBizFrom, scene=scene, startTime=startTime, tenant=tenant)
        assert resp.status_code == 200

    def test_api_opLogAbnormal(self, config_obj, GalaxybeltoplogApi):
        """  上报异常数据 """
        business_order_id = None
        business_order_type = None
        business_reporter_id = None
        device_id = None
        externalBizFrom = None
        remark = None
        request_id = None
        resp = GalaxybeltoplogApi.opLogAbnormalPostApi(business_order_id=business_order_id, business_order_type=business_order_type, business_reporter_id=business_reporter_id, device_id=device_id, externalBizFrom=externalBizFrom, remark=remark, request_id=request_id)
        assert resp.status_code == 200

    def test_api_abnormalLogsQuery(self, config_obj, GalaxybeltoplogApi):
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
        resp = GalaxybeltoplogApi.abnormalLogsQueryPostApi(dateEnd=dateEnd, dateStart=dateStart, externalBizFrom=externalBizFrom, orderId=orderId, page=page, pageOrderList=pageOrderList, requestId=requestId, scene=scene, size=size, status=status, tenantInfo=tenantInfo)
        assert resp.status_code == 200

    def test_api_abnormalLogProcess(self, config_obj, GalaxybeltoplogApi):
        """  处理异常上报 """
        errorDescription = None
        errorType = None
        externalBizFrom = None
        id = None
        resp = GalaxybeltoplogApi.abnormalLogProcessPostApi(errorDescription=errorDescription, errorType=errorType, externalBizFrom=externalBizFrom, id=id)
        assert resp.status_code == 200

    def test_api_opLogIdQuery(self, config_obj, GalaxybeltoplogApi):
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
        resp = GalaxybeltoplogApi.opLogIdQueryPostApi(algoCode=algoCode, costMax=costMax, costMin=costMin, dateEnd=dateEnd, dateStart=dateStart, deviceId=deviceId, externalBizFrom=externalBizFrom, host=host, method=method, orderId=orderId, page=page, pageOrderList=pageOrderList, scene=scene, size=size, statusCode=statusCode, tag=tag, targetPath=targetPath, timeStampMax=timeStampMax, timeStampMin=timeStampMin)
        assert resp.status_code == 200

    def test_api_opLogsQuery(self, config_obj, GalaxybeltoplogApi):
        """  根据requestIds查询opLog信息 """
        dataIgnore = None
        externalBizFrom = None
        requestIds = None
        resp = GalaxybeltoplogApi.opLogsQueryPostApi(dataIgnore=dataIgnore, externalBizFrom=externalBizFrom, requestIds=requestIds)
        assert resp.status_code == 200

    def test_api_opLogListQuery(self, config_obj, GalaxybeltoplogApi):
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
        resp = GalaxybeltoplogApi.opLogListQueryPostApi(dateEnd=dateEnd, dateStart=dateStart, deviceNo=deviceNo, endTime=endTime, externalBizFrom=externalBizFrom, orderId=orderId, page=page, pageOrderList=pageOrderList, requestId=requestId, requestType=requestType, size=size, startTime=startTime, status=status, warningCode=warningCode, whetherError=whetherError)
        assert resp.status_code == 200

    def test_api_opLogsQueryWithProduct(self, config_obj, GalaxybeltoplogApi):
        """  根据requestIds查询opLog信息附加商品信息 """
        dataIgnore = None
        externalBizFrom = None
        requestIds = None
        resp = GalaxybeltoplogApi.opLogsQueryWithProductPostApi(dataIgnore=dataIgnore, externalBizFrom=externalBizFrom, requestIds=requestIds)
        assert resp.status_code == 200

    def test_api_opLogSync(self, config_obj, GalaxybeltoplogApi):
        """  同步oplog """
        externalBizFrom = None
        requestId = None
        taskName = None
        resp = GalaxybeltoplogApi.opLogSyncPostApi(externalBizFrom=externalBizFrom, requestId=requestId, taskName=taskName)
        assert resp.status_code == 200

    def test_api_opLogTaskQuery(self, config_obj, GalaxybeltoplogApi):
        """  查询oplog同步任务 """
        dateEnd = None
        dateStart = None
        externalBizFrom = None
        page = None
        pageOrderList = None
        size = None
        resp = GalaxybeltoplogApi.opLogTaskQueryPostApi(dateEnd=dateEnd, dateStart=dateStart, externalBizFrom=externalBizFrom, page=page, pageOrderList=pageOrderList, size=size)
        assert resp.status_code == 200

    def test_api_opLogAbnormal_1(self, config_obj, GalaxybeltoplogApi):
        """  上报异常数据 """
        business_order_id = None
        business_order_type = None
        business_reporter_id = None
        device_id = None
        externalBizFrom = None
        remark = None
        request_id = None
        resp = GalaxybeltoplogApi.opLogAbnormal_1PostApi(business_order_id=business_order_id, business_order_type=business_order_type, business_reporter_id=business_reporter_id, device_id=device_id, externalBizFrom=externalBizFrom, remark=remark, request_id=request_id)
        assert resp.status_code == 200

    def test_api_opLogQuery(self, config_obj, GalaxybeltoplogApi):
        """  根据requestId查询opLog信息 """
        requestId = None
        resp = GalaxybeltoplogApi.opLogQueryGetApi(requestId=requestId)
        assert resp.status_code == 200

    def test_api_opLogAbnormal_2(self, config_obj, GalaxybeltoplogApi):
        """  上报异常数据 """
        business_order_id = None
        business_order_type = None
        business_reporter_id = None
        device_id = None
        externalBizFrom = None
        remark = None
        request_id = None
        resp = GalaxybeltoplogApi.opLogAbnormal_2PostApi(business_order_id=business_order_id, business_order_type=business_order_type, business_reporter_id=business_reporter_id, device_id=device_id, externalBizFrom=externalBizFrom, remark=remark, request_id=request_id)
        assert resp.status_code == 200

    def test_api_opLogQuery_1(self, config_obj, GalaxybeltoplogApi):
        """  根据requestId查询opLog信息 """
        requestId = None
        resp = GalaxybeltoplogApi.opLogQuery_1GetApi(requestId=requestId)
        assert resp.status_code == 200
