#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from commonlib import utils, time_utils
from commonlib.decorator import wait
from defines.belt.api.rasmanager_service_swagger import RasmanagerSwaggerApi
from commonlib.log_utils import log

"""
使用说明：


"""

RASINGRESS_STATUS_AVAILABLE = 'AVAILABLE'
RASINGRESS_STATUS_UNAVAILABLE = 'UNAVAILABLE'


def getDeviceByIDUntilAvailableFunc(resp):
    """ 仅适用于仅有1个ingressType的情况"""
    if resp.status_code == 200 and \
            resp.error_code == 0 and \
            resp.json_get("device_detail.device.driver.ingresses.0.status") == RASINGRESS_STATUS_AVAILABLE:
        return True
    else:
        status = None
        try:
            status = resp.json_get("device_detail.device.driver.ingresses.0.status")
        except:
            pass
        log().info("status_code:%s, ingress_status:%s wait." % (resp.status_code, status))
        return False


def getDeviceByIDUntilNotFoundFunc(resp):
    """ 查询设备直到NotFound"""
    if resp.status_code == 404:
        return True
    else:
        return False


class RasmanagerSwaggerBusiness(RasmanagerSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(RasmanagerSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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

        inte_obj.set_headers('X-Belt-Action', inte_obj.path_action)
        inte_obj.set_headers('X-Belt-Version', inte_obj.path_version)

    @wait(timeout=180, interval=2, util_func=getDeviceByIDUntilAvailableFunc, raise_exception=True)
    def getDeviceByIDUntilAvailable(self, device_id):
        """ 查询设备直到设备可用"""
        return self.RasManager_GetDeviceDetailGetApi(device_id, print_log=False)

    @wait(timeout=120, interval=2, util_func=getDeviceByIDUntilNotFoundFunc, raise_exception=True)
    def getDeviceByIDUntilNotFound(self, device_id):
        """ 查询设备直到设备可用"""
        return self.RasManager_GetDeviceDetailGetApi(device_id, print_log=False)

    def deleteDeviceById(self, device_id):
        """ 根据id删除device"""
        resp = self.RasManager_GetDeviceDetailGetApi(device_id, print_log=False)
        if resp.status_code == 404:
            # 已经不存在就返回了
            return
        self.RasManager_DeleteDevicePostApi(device_id=device_id)
        self.getDeviceByIDUntilNotFound(device_id)

    def getAllAssignments(self, device_id=None, loginToken=None, print_log=False, interface_desc=None):
        """ 获取所有符合条件的Assignment"""
        offset = 0
        limit = 20
        assignment_list = []
        while True:
            resp = self.RasManager_ListAssignmentsGetApi(device_id=device_id, paging_offset=offset,
                                                         paging_limit=limit,loginToken=loginToken,
                                                         print_log=print_log, interface_desc=interface_desc)
            assert resp.status_code == 200
            assignment_list.extend(resp.json_get("assignments"))
            if offset + limit >= resp.json_get("paging.total"):
                break
            offset += limit
        return assignment_list

    def getAllDeviceDetail(self, spu_names=None, filter_with_spu=None, loginToken=None, print_log=False, interface_desc=None):
        """ 获取所有符合条件的devices"""
        offset = 0
        limit = 20
        device_list = []
        while True:
            resp = self.RasManager_ListDeviceDetailsGetApi(spu_names=spu_names, filter_with_spu=filter_with_spu,
                                                           paging_offset=offset, paging_limit=limit, loginToken=loginToken,
                                                           print_log=print_log, interface_desc=interface_desc)
            assert resp.status_code == 200
            device_list.extend(resp.json_get("device_detail"))
            if offset + limit >= resp.json_get("paging.total"):
                break
            offset += limit
        return device_list