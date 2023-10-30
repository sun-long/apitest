
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pytest

from commonlib.decorator import wait
from defines.nebula_final.api.cloud_service_swagger import CloudSwaggerApi


"""
使用说明：


"""


def getSubDeviceByIDUntilFoundFunc(resp):
    if resp.status_code == 200 and resp.error_code == 0 and "state_sub_device" in resp.json and resp.json_get('state_sub_device'):
        return True
    else:
        return False


def getSubDeviceByIDUntilNotFoundFunc(resp):
    if resp.status_code == 404:
        return True
    else:
        return False

class CloudSwaggerBusiness(CloudSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(CloudSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)

    @wait(timeout=60, interval=2, util_func=getSubDeviceByIDUntilFoundFunc, raise_exception=True)
    def getSubDeviceByIDUntilFound(self, ak, device_id, sub_device_id, call_back=None):
        return self.NebulaIOTSrv_GetSubDeviceByIDGetApi(ak, device_id, sub_device_id, print_log=False)

    @wait(timeout=120, interval=2, util_func=getSubDeviceByIDUntilNotFoundFunc, raise_exception=True)
    def getSubDeviceByIDUntilNotFound(self, ak, device_id, sub_device_id, call_back=None):
        return self.NebulaIOTSrv_GetSubDeviceByIDGetApi(ak, device_id, sub_device_id, print_log=False)

    def getOplogByRequestId(self, ak, device_id, request_id, desc="defaultOplog", verify_error=True):
        """ """
        resp = self.NebulaIOTSrv_GetOPLOGsGetApi(ak, device_id, request_id, interface_desc=desc)
        assert resp.status_code == 200
        if verify_error:
            for oplog in resp.json_get('oplogs'):
                pytest.assume(oplog['level'] != 'ERROR', 'oplog error.%s' % oplog)
        return resp