#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("nova")


class BillSwaggerApi(BaseApi):
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

    def ConsoleBillService_ListDailyBillGetApi(self, spu_name=None, start_time=None, end_time=None, sort_by=None, sort_type=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询日账单列表
route: prefix=console action=ListDailyBill... """
        """  path: [get]/console/v1/dailybills API """
        """  params: 
                参数名称：spu_name　类型：string　描述：商品服务名称
                参数名称：start_time　类型：string　描述：商品消费开始时间
                参数名称：end_time　类型：string　描述：商品消费结束时间
                参数名称：sort_by　类型：string　描述：排序方式, 支持按照商品消费时间、商品服务名称、商品规格名称进行排序

 - BILL_TIME: 根据商品消费时间排序
 - SPU_NAME: 根据服务名称排序
 - VALUE_POINT_NAME: 根据规格名称排序
                参数名称：sort_type　类型：string　描述：排序类型, 默认倒序

 - DESC: 倒序排序
 - ASC: 正序排序
                参数名称：page_request.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条; 默认值为0.
返回本次请求返回的第一条记录实际位置(一般与输入一致).
[EN] Optional, start position, value: > = 0, 0 is the first line; the
default value is 0. In response, actual offset of the first returned record
is returned (generally equals to the offset in request).
                参数名称：page_request.limit　类型：integer　描述：长度, 取值范围[1,100], 如果超出范围, 则返回失败;
在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准. [EN] Length,
default value range [1,100], if it is out of the range, error will be
returned; as the limit range may be redefined in some APIs, please refer to
the supplementary description of these APIs.
                参数名称：page_request.total　类型：integer　描述：可选, 总数, 请求无须填此参数, 响应时填写.
[EN] Optional, this parameter is not required for request, but will be
filled in response
        """
        """  resp:
                200(A successful response.):
                {
                    "daily_bills": [
                        {
                            "actual_fee": "",
                            "bill_status": "[BILL_STATUS_UNKNOWN]BILL_STATUS_UNKNOWN/BILL_STATUS_UNPAID/BILL_STATUS_PAID",
                            "bill_time": "",
                            "bill_uuid": "",
                            "due_fee": "",
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
        intef = collections.interface("Bill", "ConsoleBillService_ListDailyBill")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("spu_name", spu_name)
        intef.update_params("start_time", start_time)
        intef.update_params("end_time", end_time)
        intef.update_params("sort_by", sort_by)
        intef.update_params("sort_type", sort_type)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleBillService_ListMonthlyBillGetApi(self, start_time=None, end_time=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  查询月账单列表
route: prefix=console action=ListMonthlyBi... """
        """  path: [get]/console/v1/monthlybills API """
        """  params: 
                参数名称：start_time　类型：string　描述：账期开始时间
                参数名称：end_time　类型：string　描述：账期结束时
        """
        """  resp:
                200(A successful response.):
                {
                    "monthly_bills": [
                        {
                            "actual_fee": "",
                            "bill_status": "[BILL_STATUS_UNKNOWN]BILL_STATUS_UNKNOWN/BILL_STATUS_UNPAID/BILL_STATUS_PAID",
                            "bill_time": "",
                            "created_at": "",
                            "due_fee": ""
                        }
                    ]
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
        intef = collections.interface("Bill", "ConsoleBillService_ListMonthlyBill")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("start_time", start_time)
        intef.update_params("end_time", end_time)
        return intef.request() if sendRequest else intef

