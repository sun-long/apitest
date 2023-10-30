#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.notificationinternal_service_swagger import NotificationinternalSwaggerApi


"""
使用说明：


"""


class NotificationinternalSwaggerBusiness(NotificationinternalSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(NotificationinternalSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Token"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        #inte_obj.set_headers('Grpc-Metadata-ak', '10001')
        inte_obj.set_headers("X-Belt-Version", "v1")
        if inte_obj.path == '/console-internal/v1/notification/all_msg_type':
            inte_obj.set_headers('X-Belt-Action', 'GetAllMsgType')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console-internal/v1/notification':
            inte_obj.set_headers('X-Belt-Action', 'SendNotification')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console-internal/v1/notification/delete_msg_type':
            inte_obj.set_headers('X-Belt-Action', 'DeleteMsgType')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console-internal/v1/notification/delete_template':
            inte_obj.set_headers('X-Belt-Action', 'DeleteTemplate')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console-internal/v1/notification/all_template':
            inte_obj.set_headers('X-Belt-Action', 'GetAllTemplate')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console-internal/v1/notification/msg_type':
            if inte_obj.method == "get":
                inte_obj.set_headers('X-Belt-Action', 'GetMsgType')
                inte_obj.set_headers('X-Belt-Version', 'v1')
            elif inte_obj.method == "post":
                inte_obj.set_headers('X-Belt-Action', 'CreateMsgType')
                inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console-internal/v1/notification/template':
            if inte_obj.method == "get":
                inte_obj.set_headers('X-Belt-Action', 'GetTemplate')
                inte_obj.set_headers('X-Belt-Version', 'v1')
            elif inte_obj.method == "post":
                inte_obj.set_headers('X-Belt-Action', 'CreateTemplate')
                inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console-internal/v1/notification/update_msg_type':
            inte_obj.set_headers('X-Belt-Action', 'UpdateMsgType')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console-internal/v1/notification/update_template':
            inte_obj.set_headers('X-Belt-Action', 'UpdateTemplate')
            inte_obj.set_headers('X-Belt-Version', 'v1')


    def getMsgTypeIdByName(self, typeName):
        """ 根据msgTypeName获取MsgTypeId"""
        resp = self.ConsoleNotificationInternalService_GetAllMsgTypeGetApi(
            page_request_offset=0, page_request_limit=100)
        msg_type_list = resp.json_get("all_msg_types")
        msg_type_id = None
        for info in msg_type_list:
            if info["name"] == typeName:
                msg_type_id = info["msg_type_id"]
                break
        return msg_type_id

    def getMsgTemplateIdByName(self, templateName):
        """ 根据msgTemplateName获取MsgTemplateId"""
        resp = self.ConsoleNotificationInternalService_GetAllTemplateGetApi(
            page_request_offset=0, page_request_limit=100)
        msg_template_list = resp.json_get("all_templates")
        msg_template_id = None
        for info in msg_template_list:
            if info["name"] == templateName:
                msg_template_id = info["template_id"]
                break
        return msg_template_id

    def verifyMsgTypeDeleteSuccess(self, typeId):
        resp = self.ConsoleNotificationInternalService_GetAllMsgTypeGetApi(page_request_offset=0, page_request_limit=100)
        msg_type_list = resp.json_get("all_msg_types")
        f = True
        for info in msg_type_list:
            if info["msg_type_id"] == typeId:
                f = False
        return f

    def verifyMsgTempalesDeleteSuccess(self, templateId):
        resp = self.ConsoleNotificationInternalService_GetAllTemplateGetApi(page_request_offset=0, page_request_limit=100)
        msg_template_list = resp.json_get("all_templates")
        f = True
        for info in msg_template_list:
            if info["template_id"] == templateId:
                f = False
        return f

    def prepareInternalNotification(self, msgType, msgTemplate):
        msgType = msgType
        msgTemplate = msgTemplate
        resp = self.ConsoleNotificationInternalService_GetAllTemplateGetApi(page_request_offset=0, page_request_limit=100)
        msg_template_list = resp.json_get("all_templates")
        for info in msg_template_list:
            if info["name"] == msgTemplate:
                msgTemplateId = info["template_id"]
                resp = self.ConsoleNotificationInternalService_DeleteTemplateDeleteApi(msgTemplateId)
        resp = self.ConsoleNotificationInternalService_GetAllMsgTypeGetApi(page_request_offset=0, page_request_limit=100)
        msg_type_list = resp.json_get("all_msg_types")
        for info in msg_type_list:
            if info["name"] == msgType:
                msgTypeId = info["msg_type_id"]
                resp = self.ConsoleNotificationInternalService_DeleteMsgTypeDeleteApi(msgTypeId)
        return

    def prepareInternalNotification(self, msgType, msgTemplate):
        msgType = msgType
        msgTemplate = msgTemplate
        resp = self.ConsoleNotificationInternalService_GetAllTemplateGetApi(page_request_offset=0, page_request_limit=100)
        msg_template_list = resp.json_get("all_templates")
        for info in msg_template_list:
            if info["name"] == msgTemplate:
                msgTemplateId = info["template_id"]
                resp = self.ConsoleNotificationInternalService_DeleteTemplateDeleteApi(msgTemplateId)
        resp = self.ConsoleNotificationInternalService_GetAllMsgTypeGetApi(page_request_offset=0, page_request_limit=100)
        msg_type_list = resp.json_get("all_msg_types")
        for info in msg_type_list:
            if info["name"] == msgType:
                msgTypeId = info["msg_type_id"]
                resp = self.ConsoleNotificationInternalService_DeleteMsgTypeDeleteApi(msgTypeId)
        return






