#!/usr/bin/env python
from core.request_data import BaseRequestData


class PutDeviceLicense(BaseRequestData):
    """ 修改设备的license"""

    def __init__(self, config_obj):
        self.url = '$(EnvInfo.ArgusCloud.Service)/argus/operation/v1/device/license'
        self.method = 'put'
        self.headers = {'token': ''}
        self.body = {
            "ak": "xxx",
            "dongle_sn": "",
            "video_number": 12,
            "expired_time": 0
        }
        super(PutDeviceLicense, self).__init__(config_obj)


class GetDeviceLicense(BaseRequestData):
    """ 获取设备的license"""

    def __init__(self, config_obj):
        self.url = '$(EnvInfo.ArgusCloud.Service)/argus/operation/v1/device/license'
        self.method = 'get'
        self.headers = {'token': ''}
        self.params = {
            "ak": "xxx",
            "dongle_sn": "",
        }
        super(GetDeviceLicense, self).__init__(config_obj)


class DeviceLicenseCollection(object):

    @staticmethod
    def putDeviceLicense(config_obj):
        return PutDeviceLicense(config_obj).interface()

    @staticmethod
    def getDeviceLicense(config_obj):
        return GetDeviceLicense(config_obj).interface()

if __name__ == '__main__':
    pass