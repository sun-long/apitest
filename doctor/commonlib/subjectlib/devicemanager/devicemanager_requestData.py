#!/usr/bin/env python
from core.request_data import BaseRequestData


class GetDevicesData(BaseRequestData):
    """ """

    def __init__(self, config_obj):
        self.url = '$(SpecInfo.deviceManager.Service)'
        self.body = {
            "AK": "$(SpecInfo.deviceManager.Ak)",
            "deviceID": "112233"
            }
        super(GetDevicesData, self).__init__(config_obj)


class InsertDevicesData(BaseRequestData):
    """ """

    def __init__(self, config_obj):
        self.url = '$(SpecInfo.deviceManager.Service)'
        self.body = {
            "AK": "$(SpecInfo.deviceManager.Ak)",
            "deviceID": "112233"
            }
        super(InsertDevicesData, self).__init__(config_obj)


class DeviceManagerCollection(object):

    @staticmethod
    def getDevice():
        return GetDevicesData().interface()
    def insertDevice(self):
        return InsertDevicesData().interface()




    #
    # def getDeviceApi(self):
    #     insertDevice =self.insertDevice()
    #     resp =insertDevice.request()
    #     task_id = resp.json_get('task_id')
    #     getDevice = self.getDevice()
    #     getDevice.request(task_id)

if __name__ == '__main__':
    getDevice = DeviceManagerApi.getDevice()
    getDevice.request()
    insertDevice = DeviceManagerApi.insertDevice()