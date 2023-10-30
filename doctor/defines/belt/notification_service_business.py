#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.notification_service_swagger import NotificationSwaggerApi


"""
使用说明：


"""


class NotificationSwaggerBusiness(NotificationSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(NotificationSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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
        inte_obj.set_headers("X-Belt-Version", "v1")
        if inte_obj.path == '/console/v1/notification_unread_count':
            inte_obj.set_headers('X-Belt-Action', 'GetUnReadCount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/delete_all_notification':
            inte_obj.set_headers('X-Belt-Action', 'DeleteAllMsg')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/delete_batch_notification':
            inte_obj.set_headers('X-Belt-Action', 'DeleteBatchMsg')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/all_notification':
            inte_obj.set_headers('X-Belt-Action', 'GetAllMsg')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/notification/all_msg_type':
            inte_obj.set_headers('X-Belt-Action', 'GetAllMsgType')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/notification':
            inte_obj.set_headers('X-Belt-Action', 'GetOneMsg')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/read_all_notification':
            inte_obj.set_headers('X-Belt-Action', 'ReadAllMsg')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/read_batch_notification':
            inte_obj.set_headers('X-Belt-Action', 'ReadBatchMsg')
            inte_obj.set_headers('X-Belt-Version', 'v1')



    def verifyMsgDeleteSuccess(self, msgId):
        resp = self.ConsoleNotificationService_GetAllGetApi(page_request_offset=0, page_request_limit=100)
        msg_list = resp.json_get("all_msgs")
        f = True
        for info in msg_list:
            if info["msg_id"] == msgId:
                f = False
        return f

    def perpareNotification(self, msgType):
        msgType = msgType
        resp = self.ConsoleNotificationService_GetAllGetApi(page_request_offset=0, page_request_limit=100)
        msg_list = resp.json_get("all_msgs")
        for info in msg_list:
            if info["msg_type"]["name"] == msgType:
                msgTypeId = info["msg_type"]["msg_type_id"]
                resp = self.ConsoleNotificationService_DeleteAllDeleteApi(msgTypeId)
        return
