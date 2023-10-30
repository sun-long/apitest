#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class NotificationinternalSwaggerApi(BaseApi):
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

    def ConsoleNotificationInternalService_SendNotificationPostApi(self, user_id=None, template_id=None, content=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  发送系统消息
route: prefix=console-internal action=SendN... """
        """  path: [post]/console-internal/v1/notification API """
        """  body: 
                {
                    "content": "",
                    "template_id": "",
                    "user_id": ""
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_SendNotification")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("user_id", user_id)
        intef.update_body("template_id", template_id)
        intef.update_body("content", content)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationInternalService_GetAllMsgTypeGetApi(self, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  拉取消息类型列表
route: prefix=console-internal action=Get... """
        """  path: [get]/console-internal/v1/notification/all_msg_type API """
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_GetAllMsgType")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationInternalService_GetAllTemplateGetApi(self, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  拉取消息模板列表
route: prefix=console-internal action=Get... """
        """  path: [get]/console-internal/v1/notification/all_template API """
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
                    "all_templates": [
                        {
                            "content": "",
                            "create_at": "",
                            "msg_type": {
                                "msg_type_id": "",
                                "name": ""
                            },
                            "name": "",
                            "sender": "",
                            "template_id": ""
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_GetAllTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationInternalService_DeleteMsgTypePostApi(self, msg_type_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除消息类型
route: prefix=console-internal action=Delet... """
        """  path: [post]/console-internal/v1/notification/delete_msg_type API """
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_DeleteMsgType")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("msg_type_id", msg_type_id)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationInternalService_DeleteTemplatePostApi(self, template_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  删除消息模板
route: prefix=console-internal action=Delet... """
        """  path: [post]/console-internal/v1/notification/delete_template API """
        """  body: 
                {
                    "template_id": ""
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_DeleteTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("template_id", template_id)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationInternalService_GetMsgTypeGetApi(self, msg_type_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取消息类型详情
route: prefix=console-internal action=Get... """
        """  path: [get]/console-internal/v1/notification/msg_type API """
        """  params: 
                参数名称：msg_type_id　类型：string　描述：消息类型ID
        """
        """  resp:
                200(A successful response.):
                {
                    "msg_type_info": {
                        "msg_type_id": "",
                        "name": ""
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_GetMsgType")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("msg_type_id", msg_type_id)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationInternalService_CreateMsgTypePostApi(self, name=None, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  添加消息类型
route: prefix=console-internal action=Creat... """
        """  path: [post]/console-internal/v1/notification/msg_type API """
        """  body: 
                {
                    "id": "",
                    "name": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "msg_type_info": {
                        "msg_type_id": "",
                        "name": ""
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_CreateMsgType")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("name", name)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationInternalService_GetTemplateGetApi(self, template_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  获取消息模板详情
route: prefix=console-internal action=Get... """
        """  path: [get]/console-internal/v1/notification/template API """
        """  params: 
                参数名称：template_id　类型：string　描述：消息模板ID
        """
        """  resp:
                200(A successful response.):
                {
                    "template_info": {
                        "content": "",
                        "create_at": "",
                        "msg_type": {
                            "msg_type_id": "",
                            "name": ""
                        },
                        "name": "",
                        "sender": "",
                        "template_id": ""
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_GetTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("template_id", template_id)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationInternalService_CreateTemplatePostApi(self, msg_type_id=None, name=None, content=None, sender=None, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  创建消息模板
route: prefix=console-internal action=Creat... """
        """  path: [post]/console-internal/v1/notification/template API """
        """  body: 
                {
                    "content": "",
                    "id": "",
                    "msg_type_id": "",
                    "name": "",
                    "sender": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "template_info": {
                        "content": "",
                        "create_at": "",
                        "msg_type": {
                            "msg_type_id": "",
                            "name": ""
                        },
                        "name": "",
                        "sender": "",
                        "template_id": ""
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_CreateTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("msg_type_id", msg_type_id)
        intef.update_body("name", name)
        intef.update_body("content", content)
        intef.update_body("sender", sender)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationInternalService_UpdateMsgTypePostApi(self, msg_type_id=None, name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  修改消息类型
route: prefix=console-internal action=Updat... """
        """  path: [post]/console-internal/v1/notification/update_msg_type API """
        """  body: 
                {
                    "msg_type_id": "",
                    "name": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "msg_type_info": {
                        "msg_type_id": "",
                        "name": ""
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_UpdateMsgType")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("msg_type_id", msg_type_id)
        intef.update_body("name", name)
        return intef.request() if sendRequest else intef

    def ConsoleNotificationInternalService_UpdateTemplatePostApi(self, template_id=None, msg_type_id=None, name=None, content=None, sender=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  修改消息模板
route: prefix=console-internal action=Updat... """
        """  path: [post]/console-internal/v1/notification/update_template API """
        """  body: 
                {
                    "content": "",
                    "msg_type_id": "",
                    "name": "",
                    "sender": "",
                    "template_id": ""
                }
        """
        """  resp:
                200(A successful response.):
                {
                    "template_info": {
                        "content": "",
                        "create_at": "",
                        "msg_type": {
                            "msg_type_id": "",
                            "name": ""
                        },
                        "name": "",
                        "sender": "",
                        "template_id": ""
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
        intef = collections.interface("notificationInternal", "ConsoleNotificationInternalService_UpdateTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("template_id", template_id)
        intef.update_body("msg_type_id", msg_type_id)
        intef.update_body("name", name)
        intef.update_body("content", content)
        intef.update_body("sender", sender)
        return intef.request() if sendRequest else intef

