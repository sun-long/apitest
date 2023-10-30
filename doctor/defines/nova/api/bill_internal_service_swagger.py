#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class Bill_internalSwaggerApi(BaseApi):
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

    def NovaBillInternalService_ExportDailyBillPostApi(self, account_id=None, spu_name=None, start_time=None, end_time=None, sort_by=None, sort_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  导出日账单列表 """
        """  path: [post]/v1/ExportDailyBill API """
        """  body: 
                {
                    "account_id": "",
                    "end_time": "",
                    "sort_by": "[BILL_TIME]BILL_TIME/SPU_NAME/VALUE_POINT_NAME",
                    "sort_type": "[DESC]DESC/ASC",
                    "spu_name": "",
                    "start_time": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Bill_internal", "NovaBillInternalService_ExportDailyBill")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("spu_name", spu_name)
        intef.update_body("start_time", start_time)
        intef.update_body("end_time", end_time)
        intef.update_body("sort_by", sort_by)
        intef.update_body("sort_type", sort_type)
        return intef.request() if sendRequest else intef

    def NovaBillInternalService_ExportMonthlyBillPostApi(self, account_id=None, bill_time=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  导出月账单列表 """
        """  path: [post]/v1/ExportMonthlyBill API """
        """  body: 
                {
                    "account_id": "",
                    "bill_time": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "csv": ""
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
        intef = collections.interface("Bill_internal", "NovaBillInternalService_ExportMonthlyBill")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("bill_time", bill_time)
        return intef.request() if sendRequest else intef

    def NovaBillInternalService_ListDailyBillGetApi(self, account_id=None, spu_name=None, start_time=None, end_time=None, sort_by=None, sort_type=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询日账单列表 """
        """  path: [get]/v1/ListDailyBill API """
        """  params: 
                参数名称：account_id　类型：string　描述：账户ID
                参数名称：spu_name　类型：string　描述：商品服务名称
                参数名称：start_time　类型：string　描述：商品消费开始时间
                参数名称：end_time　类型：string　描述：商品消费结束时间
                参数名称：sort_by　类型：string　描述：排序方式, 支持按照商品消费时间、商品服务名称、商品规格名称进行排序 .

 - BILL_TIME: 根据商品消费时间排序
 - SPU_NAME: 根据服务名称排序
 - VALUE_POINT_NAME: 根据规格名称排序
                参数名称：sort_type　类型：string　描述：排序类型, 默认倒序

 - DESC: 倒序排序
 - ASC: 正序排序
                参数名称：page_request.offset　类型：integer　描述：null
                参数名称：page_request.limit　类型：integer　描述：null
                参数名称：page_request.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "daily_bills": [
                        {
                            "account_id": "",
                            "account_name": "",
                            "actual_fee": "",
                            "bill_status": "[BILL_STATUS_UNKNOWN]BILL_STATUS_UNKNOWN/BILL_STATUS_UNPAID/BILL_STATUS_PAID",
                            "bill_time": "",
                            "bill_uuid": "",
                            "due_fee": "",
                            "order_id": "",
                            "pay_type": "",
                            "spu_name": "",
                            "usage": "",
                            "value_point_name": ""
                        }
                    ],
                    "page_response": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    }
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
        intef = collections.interface("Bill_internal", "NovaBillInternalService_ListDailyBill")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        intef.update_params("spu_name", spu_name)
        intef.update_params("start_time", start_time)
        intef.update_params("end_time", end_time)
        intef.update_params("sort_by", sort_by)
        intef.update_params("sort_type", sort_type)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def NovaBillInternalService_ListMonthlyBillGetApi(self, account_id=None, bill_time=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询月账单列表 """
        """  path: [get]/v1/ListMonthlyBill API """
        """  params: 
                参数名称：account_id　类型：string　描述：账户ID
                参数名称：bill_time　类型：string　描述：账期
                参数名称：page_request.offset　类型：integer　描述：null
                参数名称：page_request.limit　类型：integer　描述：null
                参数名称：page_request.total　类型：integer　描述：nul
        """
        """  resp:
                200(A successful response.):
                {
                    "monthly_bills": [
                        {
                            "account_id": "",
                            "account_name": "",
                            "actual_fee": "",
                            "bill_status": "[BILL_STATUS_UNKNOWN]BILL_STATUS_UNKNOWN/BILL_STATUS_UNPAID/BILL_STATUS_PAID",
                            "bill_time": "",
                            "created_at": "",
                            "due_fee": ""
                        }
                    ],
                    "page_response": {
                        "limit": 0,
                        "offset": 0,
                        "total": 0
                    }
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
        intef = collections.interface("Bill_internal", "NovaBillInternalService_ListMonthlyBill")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        intef.update_params("bill_time", bill_time)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def NovaBillInternalService_ReduceMonthlyBillFeePutApi(self, account_id=None, bill_time=None, reduce_fee=None, operation_notes=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  核减月账单金额 """
        """  path: [put]/v1/ReduceMonthlyBillFee API """
        """  body: 
                {
                    "account_id": "",
                    "bill_time": "",
                    "operation_notes": "",
                    "reduce_fee": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
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
        intef = collections.interface("Bill_internal", "NovaBillInternalService_ReduceMonthlyBillFee")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("bill_time", bill_time)
        intef.update_body("reduce_fee", reduce_fee)
        intef.update_body("operation_notes", operation_notes)
        return intef.request() if sendRequest else intef

    def NovaBillInternalService_UpdateMonthlyBillPaidPutApi(self, account_id=None, bill_time=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  更新月账单已结清 """
        """  path: [put]/v1/UpdateMonthlyBillPaid API """
        """  body: 
                {
                    "account_id": "",
                    "bill_time": ""
                }
        """
        """  resp:
                200(A successful response.):
                {}
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
        intef = collections.interface("Bill_internal", "NovaBillInternalService_UpdateMonthlyBillPaid")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("bill_time", bill_time)
        return intef.request() if sendRequest else intef

