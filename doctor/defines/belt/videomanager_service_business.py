#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.videomanager_service_swagger import VideomanagerSwaggerApi


"""
使用说明：


"""


class VideomanagerSwaggerBusiness(VideomanagerSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(VideomanagerSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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
        if inte_obj.path == '/v1/CreateTask':
            inte_obj.set_headers('X-Belt-Action', 'CreateLiveTask')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/DeleteTask':
            inte_obj.set_headers('X-Belt-Action', 'DeleteLiveTask')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/GeneratePlayAddress':
            inte_obj.set_headers('X-Belt-Action', 'GeneratePlayAddress')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/GetTasks':
            inte_obj.set_headers('X-Belt-Action', 'GetLiveTasks')
            inte_obj.set_headers('X-Belt-Version', 'v1')

        elif inte_obj.path == '/v1/CreateRecordTask':
            inte_obj.set_headers('X-Belt-Action', 'CreateRecordTask')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/GetRecordTasks':
            inte_obj.set_headers('X-Belt-Action', 'GetRecordTasks')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/CancelRecordTask':
            inte_obj.set_headers('X-Belt-Action', 'CancelRecordTask')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        else:
            inte_obj.set_headers('X-Belt-Action', inte_obj.path_action)
            inte_obj.set_headers('X-Belt-Version', inte_obj.path_version)

    def createTask(self, device_id=None, ingress_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None, is_delete=True):
        """ 创建任务"""
        resp = self.VideoManagerCenter_CreateTaskPostApi(device_id=device_id, ingress_ids=ingress_ids,
                                                         loginToken=loginToken, sendRequest=sendRequest,
                                                         print_log=print_log, interface_desc=interface_desc)
        assert resp.status_code == 200
        task_id = resp.json_get("task.id")

        # 添加clear up
        def clearUp():
            self.VideoManagerCenter_DeleteTaskPostApi(task_id=task_id)

        # is_delete决定这个任务是否要删除
        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        return resp

    def getAllTask(self, task_ids=None, device_ids=None, loginToken=None):
        """ 获取所有任务"""
        offset = 0
        limit = 20
        task_list = []
        while True:
            resp = self.VideoManagerCenter_GetTasksGetApi(task_ids=task_ids, device_ids=device_ids, paging_offset=offset,
                                                          paging_limit=limit, paging_total=None, loginToken=loginToken,
                                                          sendRequest=True, print_log=True, interface_desc=None)
            assert resp.status_code == 200
            task_list.extend(resp.json_get("tasks"))
            if offset + limit >= resp.json_get("paging.total"):
                break
            offset += limit
        return task_list