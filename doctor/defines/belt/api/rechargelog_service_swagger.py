#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class RechargelogSwaggerApi(BaseApi):
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

    def ConsoleRechargelogService_GetCurRechargeLogGetApi(self, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台获取当前待二次确认的充值记录详情
route: prefix=console-internal ... """
        """  path: [get]/console-internal/v1/cur_recharge API """
        """  params: 
                参数名称：account_id　类型：string　描述：账号ID
        """
        """  resp:
                200(A successful response.):
                {
                    "current_amount": "",
                    "info": {
                        "account_id": "",
                        "created_at": "",
                        "id": "",
                        "mode": "[RECHARGE_MODE_UNKOWN]RECHARGE_MODE_UNKOWN/RECHARGE_MODE_USER/RECHARGE_MODE_INTERNAL/RECHARGE_MODE_UPDATE",
                        "money": "",
                        "op_user": "",
                        "realy_money": "",
                        "remark": "",
                        "status": "[RECHARGE_LOG_STATUS_NONE]RECHARGE_LOG_STATUS_NONE/RECHARGE_LOG_STATUS_WAIT/RECHARGE_LOG_STATUS_WAITCONFIRM/RECHARGE_LOG_STATUS_CONFIRM/RECHARGE_LOG_STATUS_REJECT/RECHARGE_LOG_STATUS_CANCEL",
                        "updated_at": "",
                        "user_name": ""
                    }
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_GetCurRechargeLog")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_GetLastThreeMonthBillAmountsByAccountIDListGetApi(self, account_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据多个accountID查找对应的最近三月账单金额
route: prefix=console-i... """
        """  path: [get]/console-internal/v1/last_three_month_bill_amount/all API """
        """  params: 
                参数名称：account_ids　类型：array　描述：多个账户id 至少一个，最多100个
        """
        """  resp:
                200(A successful response.):
                {
                    "list": [
                        {
                            "account_id": "",
                            "created_at": "",
                            "empty_status": 0,
                            "last_three_month_bill_money": "",
                            "updated_at": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_GetLastThreeMonthBillAmountsByAccountIDList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_ids", account_ids)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_RechargePostApi(self, id=None, money=None, remark=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台充值
route: prefix=console-internal action=Recharg... """
        """  path: [post]/console-internal/v1/recharge API """
        """  body: 
                {
                    "id": "",
                    "money": "",
                    "remark": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_Recharge")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("money", money)
        intef.update_body("remark", remark)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_UpdateAccountAmountInfoPostApi(self, account_id=None, account_level=None, the_last_three_months_bill_amount=None, empty_status=None, account_amount_less_than=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台更新账户等级 最近三月金额 账户余额低于阈值
route: prefix=console-int... """
        """  path: [post]/console-internal/v1/recharge/account_amount API """
        """  body: 
                {
                    "account_amount_less_than": "",
                    "account_id": "",
                    "account_level": "[ACCOUNT_LEVEL_UNDEFINED]ACCOUNT_LEVEL_UNDEFINED/ACCOUNT_LEVEL_A/ACCOUNT_LEVEL_C/ACCOUNT_LEVEL_D/ACCOUNT_LEVEL_N",
                    "empty_status": 0,
                    "the_last_three_months_bill_amount": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_UpdateAccountAmountInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("account_level", account_level)
        intef.update_body("the_last_three_months_bill_amount", the_last_three_months_bill_amount)
        intef.update_body("empty_status", empty_status)
        intef.update_body("account_amount_less_than", account_amount_less_than)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_GetAccountAmountInfoGetApi(self, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台获取账户余额的账户信息
route: prefix=console-internal actio... """
        """  path: [get]/console-internal/v1/recharge/account_amount_info API """
        """  params: 
                参数名称：account_id　类型：string　描述：账号ID
        """
        """  resp:
                200(A successful response.):
                {
                    "account_amount": "",
                    "account_amount_less_than": "",
                    "account_level": "[ACCOUNT_LEVEL_UNDEFINED]ACCOUNT_LEVEL_UNDEFINED/ACCOUNT_LEVEL_A/ACCOUNT_LEVEL_C/ACCOUNT_LEVEL_D/ACCOUNT_LEVEL_N",
                    "empty_status": 0,
                    "enterprise_name": "",
                    "the_last_three_months_bill_amount": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_GetAccountAmountInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_CountSecondConfirmRechargeLogByAccountIDsGetApi(self, account_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取多个accountID对应的待更新充值申请记录(也就是待二次确认的充值申请记录)数目
route... """
        """  path: [get]/console-internal/v1/recharge/accounts/second_confirm/count API """
        """  params: 
                参数名称：account_ids　类型：array　描述：多个账户id 至少一个，最多100个
        """
        """  resp:
                200(A successful response.):
                {
                    "list": [
                        {
                            "account_id": "",
                            "total": 0
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_CountSecondConfirmRechargeLogByAccountIDs")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_ids", account_ids)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_CountUnprocessedRechargelogByAccountIDsGetApi(self, account_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取多个accountID对应的未处理充值申请记录数目
route: prefix=console-... """
        """  path: [get]/console-internal/v1/recharge/accounts/unprocessed/count API """
        """  params: 
                参数名称：account_ids　类型：array　描述：多个账户id 至少一个，最多100个
        """
        """  resp:
                200(A successful response.):
                {
                    "list": [
                        {
                            "account_id": "",
                            "total": 0
                        }
                    ]
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_CountUnprocessedRechargelogByAccountIDs")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_ids", account_ids)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_GetAllRechargeLogGetApi(self, account_id=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台获取所有充值记录
route: prefix=console-internal action=G... """
        """  path: [get]/console-internal/v1/recharge/all API """
        """  params: 
                参数名称：account_id　类型：string　描述：账号ID.
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
                    "all_infos": [
                        {
                            "account_id": "",
                            "created_at": "",
                            "id": "",
                            "mode": "[RECHARGE_MODE_UNKOWN]RECHARGE_MODE_UNKOWN/RECHARGE_MODE_USER/RECHARGE_MODE_INTERNAL/RECHARGE_MODE_UPDATE",
                            "money": "",
                            "op_user": "",
                            "realy_money": "",
                            "remark": "",
                            "status": "[RECHARGE_LOG_STATUS_NONE]RECHARGE_LOG_STATUS_NONE/RECHARGE_LOG_STATUS_WAIT/RECHARGE_LOG_STATUS_WAITCONFIRM/RECHARGE_LOG_STATUS_CONFIRM/RECHARGE_LOG_STATUS_REJECT/RECHARGE_LOG_STATUS_CANCEL",
                            "updated_at": "",
                            "user_name": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_GetAllRechargeLog")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_GetInternalAmountGetApi(self, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台获取用户账户余额
route: prefix=console-internal action=G... """
        """  path: [get]/console-internal/v1/recharge/amount API """
        """  params: 
                参数名称：account_id　类型：string　描述：账号ID
        """
        """  resp:
                200(A successful response.):
                {
                    "amount": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_GetInternalAmount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_GetBalancelogsGetApi(self, account_id=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取余额变更记录列表 GetBalancelogs
route: prefix=console-in... """
        """  path: [get]/console-internal/v1/recharge/balance_logs API """
        """  params: 
                参数名称：account_id　类型：string　描述：账户ID.
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
                    "list": [
                        {
                            "nick_name": "",
                            "transaction_detail": {
                                "account_id": "",
                                "action": "[ACTION_RECHARGE_MANUAL]ACTION_RECHARGE_MANUAL/ACTION_RESET/ACTION_WITHDRAW/ACTION_DEDUCTION_MANUAL/ACTION_DEDUCTION_MANUAL_BILL/ACTION_DEDUCTION_MANUAL_ORDER/ACTION_DEDUCTION_AUTO_BILL/ACTION_DEDUCTION_AUTO_ORDER/ACTION_DEDUCTION_NONE",
                                "amount": {
                                    "cash_amount": ""
                                },
                                "balance": {
                                    "cash_balance": ""
                                },
                                "charge_id": "",
                                "created_at": "",
                                "description": "",
                                "operator_id": "",
                                "transaction_id": "",
                                "updated_at": ""
                            },
                            "user_name": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_GetBalancelogs")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_id", account_id)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_CancelRechargePostApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台取消充值
route: prefix=console-internal action=Cance... """
        """  path: [post]/console-internal/v1/recharge/cancel API """
        """  body: 
                {
                    "id": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_CancelRecharge")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_CreateRechargePostApi(self, account_id=None, money=None, remark=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台直接充值
route: prefix=console-internal action=Creat... """
        """  path: [post]/console-internal/v1/recharge/create API """
        """  body: 
                {
                    "account_id": "",
                    "money": "",
                    "remark": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_CreateRecharge")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("account_id", account_id)
        intef.update_body("money", money)
        intef.update_body("remark", remark)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_GetLatestRechargelogsByAccountIDListGetApi(self, account_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  根据多个accountID查找最新的充值申请记录
route: prefix=console-int... """
        """  path: [get]/console-internal/v1/recharge/latest/all API """
        """  params: 
                参数名称：account_ids　类型：array　描述：多个账户id 至少一个，最多100个
        """
        """  resp:
                200(A successful response.):
                {
                    "list": [
                        {
                            "account_id": "",
                            "created_at": "",
                            "id": "",
                            "mode": "[RECHARGE_MODE_UNKOWN]RECHARGE_MODE_UNKOWN/RECHARGE_MODE_USER/RECHARGE_MODE_INTERNAL/RECHARGE_MODE_UPDATE",
                            "money": "",
                            "op_user": "",
                            "realy_money": "",
                            "remark": "",
                            "status": "[RECHARGE_LOG_STATUS_NONE]RECHARGE_LOG_STATUS_NONE/RECHARGE_LOG_STATUS_WAIT/RECHARGE_LOG_STATUS_WAITCONFIRM/RECHARGE_LOG_STATUS_CONFIRM/RECHARGE_LOG_STATUS_REJECT/RECHARGE_LOG_STATUS_CANCEL",
                            "updated_at": "",
                            "user_name": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_GetLatestRechargelogsByAccountIDList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("account_ids", account_ids)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_UpdateOwedAmountPostApi(self, bill_id=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台确认修改欠款金额
route: prefix=console-internal action=U... """
        """  path: [post]/console-internal/v1/recharge/owed_amount API """
        """  body: 
                {
                    "account_id": "",
                    "bill_id": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_UpdateOwedAmount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bill_id", bill_id)
        intef.update_body("account_id", account_id)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_RejectRechargePostApi(self, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台驳回充值
route: prefix=console-internal action=Rejec... """
        """  path: [post]/console-internal/v1/recharge/reject API """
        """  body: 
                {
                    "id": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_RejectRecharge")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_SecondConfirmationRechargePostApi(self, id=None, account_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台二次确认充值
route: prefix=console-internal action=Sec... """
        """  path: [post]/console-internal/v1/recharge/second_confirm API """
        """  body: 
                {
                    "account_id": "",
                    "id": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_SecondConfirmationRecharge")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("id", id)
        intef.update_body("account_id", account_id)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_GetSecondConfirmationRechargelogListGetApi(self, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台获取待二次确认状态下的所有充值记录
route: prefix=console-internal... """
        """  path: [get]/console-internal/v1/recharge/second_confirm/all API """
        """  params: 
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
                    "all_infos": [
                        {
                            "account_id": "",
                            "created_at": "",
                            "id": "",
                            "mode": "[RECHARGE_MODE_UNKOWN]RECHARGE_MODE_UNKOWN/RECHARGE_MODE_USER/RECHARGE_MODE_INTERNAL/RECHARGE_MODE_UPDATE",
                            "money": "",
                            "op_user": "",
                            "realy_money": "",
                            "remark": "",
                            "status": "[RECHARGE_LOG_STATUS_NONE]RECHARGE_LOG_STATUS_NONE/RECHARGE_LOG_STATUS_WAIT/RECHARGE_LOG_STATUS_WAITCONFIRM/RECHARGE_LOG_STATUS_CONFIRM/RECHARGE_LOG_STATUS_REJECT/RECHARGE_LOG_STATUS_CANCEL",
                            "updated_at": "",
                            "user_name": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_GetSecondConfirmationRechargelogList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_GetUnprocessedRechargelogListGetApi(self, recharge_at_list_order=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  后台获取有未处理充值申请记录的账户 未处理完成包括的状态有：待处理、待二次确认、驳回
route: ... """
        """  path: [get]/console-internal/v1/recharge/unprocessed/all API """
        """  params: 
                参数名称：recharge_at_list_order　类型：integer　描述：提交充值申请时间排列方式  0:降序排列  1:升序排列.
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
                    "list": [
                        {
                            "account_id": "",
                            "created_at": "",
                            "id": "",
                            "mode": "[RECHARGE_MODE_UNKOWN]RECHARGE_MODE_UNKOWN/RECHARGE_MODE_USER/RECHARGE_MODE_INTERNAL/RECHARGE_MODE_UPDATE",
                            "money": "",
                            "op_user": "",
                            "realy_money": "",
                            "remark": "",
                            "status": "[RECHARGE_LOG_STATUS_NONE]RECHARGE_LOG_STATUS_NONE/RECHARGE_LOG_STATUS_WAIT/RECHARGE_LOG_STATUS_WAITCONFIRM/RECHARGE_LOG_STATUS_CONFIRM/RECHARGE_LOG_STATUS_REJECT/RECHARGE_LOG_STATUS_CANCEL",
                            "updated_at": "",
                            "user_name": ""
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
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_GetUnprocessedRechargelogList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("recharge_at_list_order", recharge_at_list_order)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_GetAmountGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取账户余额
route: prefix=console action=GetAmount vers... """
        """  path: [get]/console/v1/recharge/amount API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "amount": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_GetAmount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleRechargelogService_ApplyRechargePostApi(self, money=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  申请充值
route: prefix=console action=ApplyRecharge ve... """
        """  path: [post]/console/v1/recharge/apply API """
        """  body: 
                {
                    "money": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "id": ""
                }
                default(An unexpected error response.):
                {
                    "code": 0,
                    "details": [
                        {
                            "type_url": "",
                            "value": ""
                        }
                    ],
                    "error": "",
                    "message": ""
                }

        """
        intef = collections.interface("rechargeLog", "ConsoleRechargelogService_ApplyRecharge")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("money", money)
        return intef.request() if sendRequest else intef

