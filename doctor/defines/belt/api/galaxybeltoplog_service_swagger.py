#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class GalaxybeltoplogSwaggerApi(BaseApi):
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

    def dayAggregationGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询当日调用量 """
        """  path: [get]/api/v1/aggregation/day API """
        """  params: 

        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "totalDeviceNum": 0,
                        "totalInvokeNum": 0
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
        intef = collections.interface("galaxyBeltOplog", "dayAggregation")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def rangeAggregationPostApi(self, endTime=None, externalBizFrom=None, startTime=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询统计周期调用量 """
        """  path: [post]/api/v1/aggregation/range API """
        """  body: 
                {
                    "endTime": 0,
                    "externalBizFrom": "",
                    "startTime": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "activeDeviceNum": 0,
                        "avgInvokeNum": 0,
                        "timeInvokeDetails": [
                            {
                                "deviceNum": 0,
                                "invokeNum": 0,
                                "invokeTime": ""
                            }
                        ],
                        "totalInvokeNum": 0
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
        intef = collections.interface("galaxyBeltOplog", "rangeAggregation")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("endTime", endTime)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("startTime", startTime)
        return intef.request() if sendRequest else intef

    def overviewPostApi(self, endTime=None, externalBizFrom=None, scene=None, startTime=None, tenant=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  场景数据概览 """
        """  path: [post]/api/v1/dashboard/overview API """
        """  body: 
                {
                    "endTime": 0,
                    "externalBizFrom": "",
                    "scene": "",
                    "startTime": 0,
                    "tenant": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "activeDeviceNum": 0,
                        "activeDeviceTransactTrend": {
                            "series": [
                                {
                                    "data": [],
                                    "name": "",
                                    "type": ""
                                }
                            ],
                            "xaxis": []
                        },
                        "tenantNum": 0,
                        "tenantTransactActiveDeviceRank": [
                            {
                                "activeDeviceNum": 0,
                                "tenantName": "",
                                "transactInvokeNum": 0
                            }
                        ],
                        "threeCameraActiveDeviceTransactTrend": {
                            "series": [
                                {
                                    "data": [],
                                    "name": "",
                                    "type": ""
                                }
                            ],
                            "xaxis": []
                        },
                        "threeCameraInvokeNum": 0,
                        "transactInvokeNum": 0,
                        "twoCameraActiveDeviceTransactTrend": {
                            "series": [
                                {
                                    "data": [],
                                    "name": "",
                                    "type": ""
                                }
                            ],
                            "xaxis": []
                        },
                        "twoCameraInvokeNum": 0
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
        intef = collections.interface("galaxyBeltOplog", "overview")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("endTime", endTime)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("scene", scene)
        intef.update_body("startTime", startTime)
        intef.update_body("tenant", tenant)
        return intef.request() if sendRequest else intef

    def overviewExportPostApi(self, endTime=None, externalBizFrom=None, scene=None, startTime=None, tenant=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  场景数据概览导出 """
        """  path: [post]/api/v1/dashboard/overview/export API """
        """  body: 
                {
                    "endTime": 0,
                    "externalBizFrom": "",
                    "scene": "",
                    "startTime": 0,
                    "tenant": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": "",
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
        intef = collections.interface("galaxyBeltOplog", "overviewExport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("endTime", endTime)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("scene", scene)
        intef.update_body("startTime", startTime)
        intef.update_body("tenant", tenant)
        return intef.request() if sendRequest else intef

    def summaryPostApi(self, endTime=None, externalBizFrom=None, scene=None, startTime=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据总览 """
        """  path: [post]/api/v1/dashboard/summary API """
        """  body: 
                {
                    "endTime": 0,
                    "externalBizFrom": "",
                    "scene": "",
                    "startTime": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": [
                        {
                            "accuracy": 0,
                            "activeDevice": 0,
                            "errorOrderNum": 0,
                            "inventoryRecognitionNum": 0,
                            "manualOrderNum": 0,
                            "manualOrderNumRatio": 0,
                            "orderNum": 0,
                            "tenantName": "",
                            "type": ""
                        }
                    ],
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
        intef = collections.interface("galaxyBeltOplog", "summary")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("endTime", endTime)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("scene", scene)
        intef.update_body("startTime", startTime)
        return intef.request() if sendRequest else intef

    def summaryExportPostApi(self, endTime=None, externalBizFrom=None, scene=None, startTime=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  数据总览导出 """
        """  path: [post]/api/v1/dashboard/summary/export API """
        """  body: 
                {
                    "endTime": 0,
                    "externalBizFrom": "",
                    "scene": "",
                    "startTime": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": "",
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
        intef = collections.interface("galaxyBeltOplog", "summaryExport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("endTime", endTime)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("scene", scene)
        intef.update_body("startTime", startTime)
        return intef.request() if sendRequest else intef

    def statisticPostApi(self, endTime=None, externalBizFrom=None, scene=None, startTime=None, tenant=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  租户数据概览 """
        """  path: [post]/api/v1/dashboard/tenant/statistic API """
        """  body: 
                {
                    "endTime": 0,
                    "externalBizFrom": "",
                    "scene": "",
                    "startTime": 0,
                    "tenant": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "activeDeviceNum": 0,
                        "activeDeviceTransactTrend": {
                            "series": [
                                {
                                    "data": [],
                                    "name": "",
                                    "type": ""
                                }
                            ],
                            "xaxis": []
                        },
                        "avgTimeTrend": {
                            "series": [
                                {
                                    "data": [],
                                    "name": "",
                                    "type": ""
                                }
                            ],
                            "xaxis": []
                        },
                        "deviceOrders": [
                            {
                                "deviceName": "",
                                "orders": 0
                            }
                        ],
                        "productNum": 0,
                        "productSales": [
                            {
                                "productName": "",
                                "sales": 0
                            }
                        ],
                        "recognizeTrend": {
                            "series": [
                                {
                                    "data": [],
                                    "name": "",
                                    "type": ""
                                }
                            ],
                            "xaxis": []
                        },
                        "stockAvgTime": 0,
                        "stockInvokeNum": 0,
                        "threeCameraAvgTime": 0,
                        "threeCameraDeviceNum": 0,
                        "threeCameraInvokeNum": 0,
                        "threeCameraManualDistribute": {
                            "series": [
                                {
                                    "data": [
                                        {
                                            "name": "",
                                            "value": 0
                                        }
                                    ],
                                    "name": "",
                                    "type": ""
                                }
                            ],
                            "yaxis": []
                        },
                        "threeCameraManualNum": 0,
                        "top1": "",
                        "transactAvgTime": 0,
                        "transactInvokeNum": 0,
                        "transactInvokeTrend": {
                            "series": [
                                {
                                    "data": [],
                                    "name": "",
                                    "type": ""
                                }
                            ],
                            "xaxis": []
                        },
                        "twoCameraAvgTime": 0,
                        "twoCameraDeviceNum": 0,
                        "twoCameraInvokeNum": 0,
                        "twoCameraManualDistribute": {
                            "series": [
                                {
                                    "data": [
                                        {
                                            "name": "",
                                            "value": 0
                                        }
                                    ],
                                    "name": "",
                                    "type": ""
                                }
                            ],
                            "yaxis": []
                        },
                        "twoCameraManualNum": 0
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
        intef = collections.interface("galaxyBeltOplog", "statistic")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("endTime", endTime)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("scene", scene)
        intef.update_body("startTime", startTime)
        intef.update_body("tenant", tenant)
        return intef.request() if sendRequest else intef

    def tenantStatisticExportPostApi(self, endTime=None, externalBizFrom=None, scene=None, startTime=None, tenant=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  租户数据概览导出 """
        """  path: [post]/api/v1/dashboard/tenant/statistic/export API """
        """  body: 
                {
                    "endTime": 0,
                    "externalBizFrom": "",
                    "scene": "",
                    "startTime": 0,
                    "tenant": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": "",
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
        intef = collections.interface("galaxyBeltOplog", "tenantStatisticExport")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("endTime", endTime)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("scene", scene)
        intef.update_body("startTime", startTime)
        intef.update_body("tenant", tenant)
        return intef.request() if sendRequest else intef

    def opLogAbnormalPostApi(self, business_order_id=None, business_order_type=None, business_reporter_id=None, device_id=None, externalBizFrom=None, remark=None, request_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  上报异常数据 """
        """  path: [post]/api/v1/oplogs/abnormal API """
        """  body: 
                {
                    "business_order_id": "",
                    "business_order_type": "",
                    "business_reporter_id": "",
                    "device_id": "",
                    "externalBizFrom": "",
                    "remark": "",
                    "request_id": ""
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
        intef = collections.interface("galaxyBeltOplog", "opLogAbnormal")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("business_order_id", business_order_id)
        intef.update_body("business_order_type", business_order_type)
        intef.update_body("business_reporter_id", business_reporter_id)
        intef.update_body("device_id", device_id)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("remark", remark)
        intef.update_body("request_id", request_id)
        return intef.request() if sendRequest else intef

    def abnormalLogsQueryPostApi(self, dateEnd=None, dateStart=None, externalBizFrom=None, orderId=None, page=None, pageOrderList=None, requestId=None, scene=None, size=None, status=None, tenantInfo=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询所有异常上报信息 """
        """  path: [post]/api/v1/oplogs/abnormal/logs API """
        """  body: 
                {
                    "dateEnd": "",
                    "dateStart": "",
                    "externalBizFrom": "",
                    "orderId": "",
                    "page": 0,
                    "pageOrderList": [
                        {
                            "orderField": "",
                            "orderType": ""
                        }
                    ],
                    "requestId": "",
                    "scene": "",
                    "size": 0,
                    "status": "",
                    "tenantInfo": ""
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "abnormalLogList": [
                            {
                                "cameraType": "",
                                "deviceId": "",
                                "errorDescription": "",
                                "errorType": 0,
                                "id": "",
                                "interfaceName": "",
                                "orderId": "",
                                "processTime": "",
                                "reportTime": "",
                                "requestId": "",
                                "requestTime": "",
                                "scene": "",
                                "tenantName": ""
                            }
                        ],
                        "empty": false,
                        "list": [],
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
        intef = collections.interface("galaxyBeltOplog", "abnormalLogsQuery")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("dateEnd", dateEnd)
        intef.update_body("dateStart", dateStart)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("orderId", orderId)
        intef.update_body("page", page)
        intef.update_body("pageOrderList", pageOrderList)
        intef.update_body("requestId", requestId)
        intef.update_body("scene", scene)
        intef.update_body("size", size)
        intef.update_body("status", status)
        intef.update_body("tenantInfo", tenantInfo)
        return intef.request() if sendRequest else intef

    def abnormalLogProcessPostApi(self, errorDescription=None, errorType=None, externalBizFrom=None, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  处理异常上报 """
        """  path: [post]/api/v1/oplogs/abnormal/process API """
        """  body: 
                {
                    "errorDescription": "",
                    "errorType": 0,
                    "externalBizFrom": "",
                    "id": ""
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
        intef = collections.interface("galaxyBeltOplog", "abnormalLogProcess")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("errorDescription", errorDescription)
        intef.update_body("errorType", errorType)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def opLogIdQueryPostApi(self, algoCode=None, costMax=None, costMin=None, dateEnd=None, dateStart=None, deviceId=None, externalBizFrom=None, host=None, method=None, orderId=None, page=None, pageOrderList=None, scene=None, size=None, statusCode=None, tag=None, targetPath=None, timeStampMax=None, timeStampMin=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询requestId """
        """  path: [post]/api/v1/oplogs/id API """
        """  body: 
                {
                    "algoCode": 0,
                    "costMax": 0,
                    "costMin": 0,
                    "dateEnd": "",
                    "dateStart": "",
                    "deviceId": "",
                    "externalBizFrom": "",
                    "host": "",
                    "method": "",
                    "orderId": "",
                    "page": 0,
                    "pageOrderList": [
                        {
                            "orderField": "",
                            "orderType": ""
                        }
                    ],
                    "scene": "",
                    "size": 0,
                    "statusCode": 0,
                    "tag": 0,
                    "targetPath": "",
                    "timeStampMax": 0,
                    "timeStampMin": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "empty": false,
                        "list": [],
                        "page": 0,
                        "requestIds": [],
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
        intef = collections.interface("galaxyBeltOplog", "opLogIdQuery")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("algoCode", algoCode)
        intef.update_body("costMax", costMax)
        intef.update_body("costMin", costMin)
        intef.update_body("dateEnd", dateEnd)
        intef.update_body("dateStart", dateStart)
        intef.update_body("deviceId", deviceId)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("host", host)
        intef.update_body("method", method)
        intef.update_body("orderId", orderId)
        intef.update_body("page", page)
        intef.update_body("pageOrderList", pageOrderList)
        intef.update_body("scene", scene)
        intef.update_body("size", size)
        intef.update_body("statusCode", statusCode)
        intef.update_body("tag", tag)
        intef.update_body("targetPath", targetPath)
        intef.update_body("timeStampMax", timeStampMax)
        intef.update_body("timeStampMin", timeStampMin)
        return intef.request() if sendRequest else intef

    def opLogsQueryPostApi(self, dataIgnore=None, externalBizFrom=None, requestIds=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据requestIds查询opLog信息 """
        """  path: [post]/api/v1/oplogs/logs API """
        """  body: 
                {
                    "dataIgnore": false,
                    "externalBizFrom": "",
                    "requestIds": []
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "opLogList": [
                            {
                                "composes": [
                                    {
                                        "composeId": "",
                                        "composeName": ""
                                    }
                                ],
                                "dynamicVisualDTO": {
                                    "crossLines": [
                                        {
                                            "crossLineSet": [
                                                {
                                                    "crossLine": 0,
                                                    "fileName": "",
                                                    "frameId": 0,
                                                    "imageUrlLKey": "",
                                                    "skuId": "",
                                                    "timeStamp": 0
                                                }
                                            ]
                                        }
                                    ],
                                    "videoUrlLKeys": []
                                },
                                "header": {
                                    "algo_code": 0,
                                    "cost": 0,
                                    "end_time": 0,
                                    "host": "",
                                    "method": "",
                                    "params": "",
                                    "scene": "",
                                    "source_ip": "",
                                    "status_code": 0,
                                    "tag": 0,
                                    "target_path": "",
                                    "timestamp": 0
                                },
                                "initData": "",
                                "meta": [
                                    {
                                        "cost": 0,
                                        "cost_since_start": 0,
                                        "data": "",
                                        "keyword": ""
                                    }
                                ],
                                "orderId": "",
                                "request_id": "",
                                "tenantName": ""
                            }
                        ]
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
        intef = collections.interface("galaxyBeltOplog", "opLogsQuery")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("dataIgnore", dataIgnore)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("requestIds", requestIds)
        return intef.request() if sendRequest else intef

    def opLogListQueryPostApi(self, dateEnd=None, dateStart=None, deviceNo=None, endTime=None, externalBizFrom=None, orderId=None, page=None, pageOrderList=None, requestId=None, requestType=None, size=None, startTime=None, status=None, warningCode=None, whetherError=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询租户oplog 列表 """
        """  path: [post]/api/v1/oplogs/oplog/list API """
        """  body: 
                {
                    "dateEnd": "",
                    "dateStart": "",
                    "deviceNo": "",
                    "endTime": 0,
                    "externalBizFrom": "",
                    "orderId": "",
                    "page": 0,
                    "pageOrderList": [
                        {
                            "orderField": "",
                            "orderType": ""
                        }
                    ],
                    "requestId": "",
                    "requestType": "",
                    "size": 0,
                    "startTime": 0,
                    "status": "",
                    "warningCode": "",
                    "whetherError": false
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "empty": false,
                        "list": [],
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
        intef = collections.interface("galaxyBeltOplog", "opLogListQuery")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("dateEnd", dateEnd)
        intef.update_body("dateStart", dateStart)
        intef.update_body("deviceNo", deviceNo)
        intef.update_body("endTime", endTime)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("orderId", orderId)
        intef.update_body("page", page)
        intef.update_body("pageOrderList", pageOrderList)
        intef.update_body("requestId", requestId)
        intef.update_body("requestType", requestType)
        intef.update_body("size", size)
        intef.update_body("startTime", startTime)
        intef.update_body("status", status)
        intef.update_body("warningCode", warningCode)
        intef.update_body("whetherError", whetherError)
        return intef.request() if sendRequest else intef

    def opLogsQueryWithProductPostApi(self, dataIgnore=None, externalBizFrom=None, requestIds=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据requestIds查询opLog信息附加商品信息 """
        """  path: [post]/api/v1/oplogs/product/logs API """
        """  body: 
                {
                    "dataIgnore": false,
                    "externalBizFrom": "",
                    "requestIds": []
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "opLogList": [
                            {
                                "composes": [
                                    {
                                        "composeId": "",
                                        "composeName": ""
                                    }
                                ],
                                "dynamicVisualDTO": {
                                    "crossLines": [
                                        {
                                            "crossLineSet": [
                                                {
                                                    "crossLine": 0,
                                                    "fileName": "",
                                                    "frameId": 0,
                                                    "imageUrlLKey": "",
                                                    "skuId": "",
                                                    "timeStamp": 0
                                                }
                                            ]
                                        }
                                    ],
                                    "videoUrlLKeys": []
                                },
                                "header": {
                                    "algo_code": 0,
                                    "cost": 0,
                                    "end_time": 0,
                                    "host": "",
                                    "method": "",
                                    "params": "",
                                    "scene": "",
                                    "source_ip": "",
                                    "status_code": 0,
                                    "tag": 0,
                                    "target_path": "",
                                    "timestamp": 0
                                },
                                "initData": "",
                                "meta": [
                                    {
                                        "cost": 0,
                                        "cost_since_start": 0,
                                        "data": "",
                                        "keyword": ""
                                    }
                                ],
                                "orderId": "",
                                "request_id": "",
                                "tenantName": ""
                            }
                        ]
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
        intef = collections.interface("galaxyBeltOplog", "opLogsQueryWithProduct")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("dataIgnore", dataIgnore)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("requestIds", requestIds)
        return intef.request() if sendRequest else intef

    def opLogSyncPostApi(self, externalBizFrom=None, requestId=None, taskName=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  同步oplog """
        """  path: [post]/api/v1/oplogs/sync API """
        """  body: 
                {
                    "externalBizFrom": "",
                    "requestId": [],
                    "taskName": ""
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
        intef = collections.interface("galaxyBeltOplog", "opLogSync")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("requestId", requestId)
        intef.update_body("taskName", taskName)
        return intef.request() if sendRequest else intef

    def opLogTaskQueryPostApi(self, dateEnd=None, dateStart=None, externalBizFrom=None, page=None, pageOrderList=None, size=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询oplog同步任务 """
        """  path: [post]/api/v1/oplogs/task/list API """
        """  body: 
                {
                    "dateEnd": "",
                    "dateStart": "",
                    "externalBizFrom": "",
                    "page": 0,
                    "pageOrderList": [
                        {
                            "orderField": "",
                            "orderType": ""
                        }
                    ],
                    "size": 0
                }
        """
        """  resp:
                200(OK):
                {
                    "code": 0,
                    "data": {
                        "empty": false,
                        "list": [],
                        "opLogSyncTaskDetailList": [
                            {
                                "failDetail": [],
                                "statusCode": 0,
                                "taskName": ""
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
        intef = collections.interface("galaxyBeltOplog", "opLogTaskQuery")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("dateEnd", dateEnd)
        intef.update_body("dateStart", dateStart)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("page", page)
        intef.update_body("pageOrderList", pageOrderList)
        intef.update_body("size", size)
        return intef.request() if sendRequest else intef

    def opLogAbnormal_1PostApi(self, business_order_id=None, business_order_type=None, business_reporter_id=None, device_id=None, externalBizFrom=None, remark=None, request_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  上报异常数据 """
        """  path: [post]/openapi/v1/oplog/abnormal API """
        """  body: 
                {
                    "business_order_id": "",
                    "business_order_type": "",
                    "business_reporter_id": "",
                    "device_id": "",
                    "externalBizFrom": "",
                    "remark": "",
                    "request_id": ""
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
        intef = collections.interface("galaxyBeltOplog", "opLogAbnormal_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("business_order_id", business_order_id)
        intef.update_body("business_order_type", business_order_type)
        intef.update_body("business_reporter_id", business_reporter_id)
        intef.update_body("device_id", device_id)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("remark", remark)
        intef.update_body("request_id", request_id)
        return intef.request() if sendRequest else intef

    def opLogQueryGetApi(self, requestId=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据requestId查询opLog信息 """
        """  path: [get]/openapi/v1/oplog/queryById API """
        """  params: 
                *参数名称：requestId　类型：string　描述：requestI
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
        intef = collections.interface("galaxyBeltOplog", "opLogQuery")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("requestId", requestId)
        return intef.request() if sendRequest else intef

    def opLogAbnormal_2PostApi(self, business_order_id=None, business_order_type=None, business_reporter_id=None, device_id=None, externalBizFrom=None, remark=None, request_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  上报异常数据 """
        """  path: [post]/openapi/v2/oplog/abnormal API """
        """  body: 
                {
                    "business_order_id": "",
                    "business_order_type": "",
                    "business_reporter_id": "",
                    "device_id": "",
                    "externalBizFrom": "",
                    "remark": "",
                    "request_id": ""
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
        intef = collections.interface("galaxyBeltOplog", "opLogAbnormal_2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("business_order_id", business_order_id)
        intef.update_body("business_order_type", business_order_type)
        intef.update_body("business_reporter_id", business_reporter_id)
        intef.update_body("device_id", device_id)
        intef.update_body("externalBizFrom", externalBizFrom)
        intef.update_body("remark", remark)
        intef.update_body("request_id", request_id)
        return intef.request() if sendRequest else intef

    def opLogQuery_1GetApi(self, requestId=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据requestId查询opLog信息 """
        """  path: [get]/openapi/v2/oplog/queryById API """
        """  params: 
                *参数名称：requestId　类型：string　描述：requestI
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
        intef = collections.interface("galaxyBeltOplog", "opLogQuery_1")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("requestId", requestId)
        return intef.request() if sendRequest else intef

