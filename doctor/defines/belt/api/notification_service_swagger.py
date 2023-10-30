#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class NotificationSwaggerApi(BaseApi):
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

    def ConsoleNotificationService_GetAllMsgGetApi(self, msg_type_id=None, status=None, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  拉取消息列表
route: prefix=console action=GetAllMsg vers... """
        """  path: [get]/console/v1/all_notification API """
        """  params: 
                参数名称：msg_type_id　类型：string　描述：可选，拉取的消息类型，不填则是所有消息.
                参数名称：status　类型：string　描述：可选，拉取的消息状态，不填则是所有消息.

 - STATUS_UNKOWN: 未知
 - STATUS_UNREAD: 未读
 - STATUS_READ: 已读
                参数名称：page_request.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条; 默认值为0.
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page_request.limit　类型：integer　描述：长度, 取值范围[1,100], 如果超出范围, 则返回失败;
在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page_request.total　类型：string　描述：可选, 总数, 请求无须填此参数, 响应时填写
        """
        """  resp:
                200(A successful response.):
                {
                    "all_msgs": [
                        {
                            "content": "",
                            "create_at": "",
                            "msg_id": "",
                            "msg_type": {
                                "msg_type_id": "",
                                "name": ""
                            },
                            "name": "",
                            "status": "[STATUS_UNKOWN]STATUS_UNKOWN/STATUS_UNREAD/STATUS_READ"
                        }
                    ],
                    "count": "",
                    "page_response": {
                        "limit": 0,
                        "offset": 0,
                        "total": ""
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
        intef = collections.interface("notification", "ConsoleNotificationService_GetAllMsg")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("msg_type_id", msg_type_id)
        intef.update_params("status", status)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationService_DeleteAllMsgPostApi(self, msg_type_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除全部消息
route: prefix=console action=DeleteAllMsg v... """
        """  path: [post]/console/v1/delete_all_notification API """
        """  body: 
                {
                    "msg_type_id": ""
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
        intef = collections.interface("notification", "ConsoleNotificationService_DeleteAllMsg")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("msg_type_id", msg_type_id)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationService_DeleteBatchMsgPostApi(self, all_msg_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  批量删除消息
route: prefix=console action=DeleteBatchMsg... """
        """  path: [post]/console/v1/delete_batch_notification API """
        """  body: 
                {
                    "all_msg_ids": []
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
        intef = collections.interface("notification", "ConsoleNotificationService_DeleteBatchMsg")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("all_msg_ids", all_msg_ids)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationService_GetOneMsgGetApi(self, msg_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取消息详情
route: prefix=console action=GetOneMsg vers... """
        """  path: [get]/console/v1/notification API """
        """  params: 
                参数名称：msg_id　类型：string　描述：消息ID
        """
        """  resp:
                200(A successful response.):
                {
                    "msg_info": {
                        "content": "",
                        "create_at": "",
                        "msg_id": "",
                        "msg_type": {
                            "msg_type_id": "",
                            "name": ""
                        },
                        "name": "",
                        "status": "[STATUS_UNKOWN]STATUS_UNKOWN/STATUS_UNREAD/STATUS_READ"
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
        intef = collections.interface("notification", "ConsoleNotificationService_GetOneMsg")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("msg_id", msg_id)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationService_GetAllMsgTypeGetApi(self, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  拉取消息类型列表
route: prefix=console action=GetAllMsgTyp... """
        """  path: [get]/console/v1/notification/all_msg_type API """
        """  params: 
                参数名称：page_request.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条; 默认值为0.
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page_request.limit　类型：integer　描述：长度, 取值范围[1,100], 如果超出范围, 则返回失败;
在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page_request.total　类型：string　描述：可选, 总数, 请求无须填此参数, 响应时填写
        """
        """  resp:
                200(A successful response.):
                {
                    "all_msg_types": [
                        {
                            "msg_type_id": "",
                            "name": ""
                        }
                    ],
                    "page_response": {
                        "limit": 0,
                        "offset": 0,
                        "total": ""
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
        intef = collections.interface("notification", "ConsoleNotificationService_GetAllMsgType")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationService_GetUnReadCountGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取未读消息数
route: prefix=console action=GetUnReadCoun... """
        """  path: [get]/console/v1/notification_unread_count API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                {
                    "count": ""
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
        intef = collections.interface("notification", "ConsoleNotificationService_GetUnReadCount")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationService_ReadAllMsgPostApi(self, msg_type_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  全部标记为已读
route: prefix=console action=ReadAllMsg ve... """
        """  path: [post]/console/v1/read_all_notification API """
        """  body: 
                {
                    "msg_type_id": ""
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
        intef = collections.interface("notification", "ConsoleNotificationService_ReadAllMsg")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("msg_type_id", msg_type_id)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationService_ReadBatchMsgPostApi(self, all_msg_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  批量标记为已读
route: prefix=console action=ReadBatchMsg ... """
        """  path: [post]/console/v1/read_batch_notification API """
        """  body: 
                {
                    "all_msg_ids": []
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
        intef = collections.interface("notification", "ConsoleNotificationService_ReadBatchMsg")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("all_msg_ids", all_msg_ids)
        return intef.request() if sendRequest else intef

