#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.rasmanager_easybot_service_swagger import RasmanagerEasyBotSwaggerApi


"""
使用说明：


"""

def getAssignmentsUntilRunningFunc(resp):
    """ 仅适用于仅有1个ingressType的情况"""
    if resp.status_code == 200 and \
            resp.json_get("assignment.state") == "AS_EL_RUNNING":
        return True
    else:
        return False

class RasmanagerEasyBotSwaggerBusiness(RasmanagerEasyBotSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(RasmanagerEasyBotSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        # self.TOKEN_NAME = "X-Belt-Token"
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)

        easyBotPrefix = "%s/easy-bot-spu-test" % inte_obj.path_prefix
        if inte_obj.path == '/v1/CreateAssignment':
            inte_obj.set_headers('X-Belt-Action', 'CreateEasyBotAssignment')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix(easyBotPrefix)
        elif inte_obj.path == '/v1/DeleteAssignment':
            inte_obj.set_headers('X-Belt-Action', 'DeleteEasyBotAssignment')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix(easyBotPrefix)
        elif inte_obj.path == '/v1/GetAssignment':
            inte_obj.set_headers('X-Belt-Action', 'GetEasyBotAssignment')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix(easyBotPrefix)
        elif inte_obj.path == '/v1/UpdateAssignment':
            inte_obj.set_headers('X-Belt-Action', 'UpdateEasyBotAssignment')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix(easyBotPrefix)
        elif inte_obj.path == '/v1/ListAssignments':
            inte_obj.set_headers('X-Belt-Action', 'ListEasyBotAssignments')
            inte_obj.set_headers('X-Belt-Version', 'v1')
            inte_obj.set_path_prefix(easyBotPrefix)
        else:
            inte_obj.set_headers('X-Belt-Action', inte_obj.path_action)
            inte_obj.set_headers('X-Belt-Version', inte_obj.path_version)

    def createAssignment(self, device_id, assignment_config=None, rotate_config=None, is_delete=True):
        """ 创建Assignment"""
        if not assignment_config:
            assignment_config = {
                # "callback_url": "http://10.4.7.29:8877/sensego/v1.0/callback",
                "callback_url": "http://10.151.3.74:9999",
                "user_meta": "ymy-test-{{$isoTimestamp}}"
            }
        if not assignment_config:
            rotate_config = {
                "retention": {
                    "day": 7
                }
            }
        resp = self.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)

        # 添加clear up
        def clearUp():
            self.RasManager_DeleteAssignmentPostApi(device_id=device_id)

        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        return resp

    @wait(timeout=120, interval=2, util_func=getAssignmentsUntilRunningFunc, raise_exception=True)
    def getAssignmentsUntilRunning(self, device_id=None, spu_name=None):
        """ 查询设备直到设备可用"""
        return self.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=spu_name, print_log=False)

    def getAllAssignments(self, device_id=None, loginToken=None, print_log=False, interface_desc=None):
        """ 获取所有符合条件的Assignment"""
        offset = 0
        limit = 20
        assignment_list = []
        while True:
            resp = self.RasManager_ListAssignmentsGetApi(device_id=device_id, paging_offset=offset,
                                                         paging_limit=limit, loginToken=loginToken,
                                                         print_log=print_log, interface_desc=interface_desc)
            assert resp.status_code == 200
            assignment_list.extend(resp.json_get("assignments"))
            if offset + limit >= resp.json_get("paging.total"):
                break
            offset += limit
        return assignment_list

    def getAllDeviceDetail(self, spu_names=None, filter_with_spu=None, print_log=False):
        """ 获取所有符合条件的devices"""
        offset = 0
        limit = 20
        device_list = []
        while True:
            resp = self.RasManager_ListDeviceDetailsGetApi(spu_names=spu_names, filter_with_spu=filter_with_spu,
                                                       paging_offset=offset, paging_limit=limit, print_log=print_log)
            assert resp.status_code == 200
            device_list.extend(resp.json_get("device_detail"))
            if offset + limit >= resp.json_get("paging.total"):
                break
            offset += limit
        return device_list