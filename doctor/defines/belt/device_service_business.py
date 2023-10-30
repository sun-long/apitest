#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from commonlib import utils, time_utils, sign_utils
from commonlib.decorator import wait
from defines.belt.api.device_service_swagger import DeviceSwaggerApi
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
            resp.json_get("device.driver.ingresses.0.status") == RASINGRESS_STATUS_AVAILABLE:
        return True
    else:
        status = None
        try:
            status = resp.json_get("device.driver.ingresses.0.status")
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


class DeviceSwaggerBusiness(DeviceSwaggerApi):
    """ 业务类代码写在这里"""

    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(DeviceSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        # self.TOKEN_NAME = "X-Belt-Token"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)
        if inte_obj.path == '/v1/CreateDeviceByKindName':
            inte_obj.set_headers('X-Belt-Action', 'CreateDevice')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/v1/BatchCreateDevicesByKindName':
            inte_obj.set_headers('X-Belt-Action', 'BatchCreateDevices')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        else:
            inte_obj.set_headers('X-Belt-Action', inte_obj.path_action)
            inte_obj.set_headers('X-Belt-Version', inte_obj.path_version)

    def DeviceManagerCenter_GetDeviceGetApi(self, id=None, loginToken=None, sendRequest=True, print_log=True,
                                            interface_desc=None):
        """  根据device_id获取Device """
        intef = super(DeviceSwaggerBusiness, self).DeviceManagerCenter_GetDeviceGetApi(id=id, loginToken=loginToken,
                                                                                       sendRequest=False,
                                                                                       print_log=print_log,
                                                                                       interface_desc=interface_desc)
        intef.set_headers('X-Belt-Action', 'GetCenterDevice')
        intef.set_headers('X-Belt-Version', intef.path_version)
        return intef.request() if sendRequest else intef

    def DeviceManagerCenter_GetDevicesGetApi(self, ids=None, names=None, paging_offset=None, paging_limit=None,
                                             paging_total=None, loginToken=None, sendRequest=True, print_log=True,
                                             interface_desc=None):
        """  获取Device列表及总数，支持分页查询 """
        intef = super(DeviceSwaggerBusiness, self).DeviceManagerCenter_GetDevicesGetApi(ids=ids, names=names,
                                                                                        paging_offset=paging_offset,
                                                                                        paging_limit=paging_limit,
                                                                                        paging_total=paging_total,
                                                                                        loginToken=loginToken,
                                                                                        sendRequest=False,
                                                                                        print_log=print_log,
                                                                                        interface_desc=interface_desc)
        intef.set_headers('X-Belt-Action', 'GetCenterDevices')
        intef.set_headers('X-Belt-Version', intef.path_version)
        return intef.request() if sendRequest else intef

    @wait(timeout=180, interval=2, util_func=getDeviceByIDUntilAvailableFunc, raise_exception=True)
    def getDeviceByIDUntilAvailable(self, device_id):
        """ 查询设备直到设备可用"""
        return self.DeviceManagerCenter_GetDeviceGetApi(device_id, print_log=False)

    @wait(timeout=120, interval=2, util_func=getDeviceByIDUntilNotFoundFunc, raise_exception=True)
    def getDeviceByIDUntilNotFound(self, device_id):
        """ 查询设备直到设备可用"""
        return self.DeviceManagerCenter_GetDeviceGetApi(device_id, print_log=False)

    def getDeviceKindInfoByKindName(self, name):
        """ 根据设备类型名称查询设备类型"""
        resp = self.DeviceManagerCenter_GetDeviceKindsGetApi(paging_limit=100, print_log=False)
        for devicekindInfo in resp.json_get("devicekinds"):
            if devicekindInfo["name"] == name:
                return devicekindInfo
        return None

    def createDeviceKindWithRTSP(self, name=None, desc=None, is_delete=True):
        """ 创建一个rtsp设备类型"""
        if not name:
            name = "deviceKind_%s" % time_utils.get_time_str()
        resp = self.DeviceManagerCenter_CreateDeviceKindPostApi(name=name, desc=desc, ingress_types=["RTSP"],
                                                                verify_method="USER")
        deviceKind_id = resp.json_get("devicekind.id")

        # 添加clear up
        def clearUp():
            self.deleteDeviceKindById(deviceKind_id)

        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        return deviceKind_id

    def deleteDeviceKindById(self, deviceKind_id):
        """ 删除设备类型"""
        resp = self.DeviceManagerCenter_GetDeviceKindGetApi(deviceKind_id)
        if resp.status_code == 404:
            return
        return self.DeviceManagerCenter_DeleteDeviceKindPostApi(deviceKind_id)

    def deleteDeviceById(self, device_id):
        """ 根据id删除device"""
        resp = self.DeviceManagerCenter_GetDeviceGetApi(device_id, print_log=False)
        if resp.status_code == 404:
            # 已经不存在就返回了
            return
        self.DeviceManagerCenter_DeleteDevicePostApi(id=device_id)
        self.getDeviceByIDUntilNotFound(device_id)

    def createDeviceWithRTSP(self, deviceKindName, camera_info, cluster_info, name=None, driver=None, desc=None,
                             is_delete=True):
        """ 创建一个rtsp设备"""
        if not name:
            name = "waDevice_%s_%s" % (sign_utils.getUuid(4),time_utils.get_time_str())
        cluster = {"id": cluster_info["id"]}
        if not driver:
            driver = {
                "enable": True,
                "ingresses": [
                    {
                        "information": {
                            "rtsp": {
                                "source_url": camera_info["rtsp"]
                            },
                            "type": camera_info["type"]
                        },
                        "name": name,
                        "description": ""
                    }
                ],
            }
        resp = self.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=deviceKindName, name=name,
                                                                      cluster=cluster, driver=driver, desc=desc)
        assert resp.status_code == 200
        device_id = resp.json_get("device.id")

        # 添加clear up
        def clearUp():

            self.ext_info.RasmanagerApi.deleteDeviceById(device_id)

        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        # self.ext_info.RasmanagerApi.getDeviceByIDUntilAvailable(device_id)
        return device_id

    def createDeviceWithRTMP(self, deviceKindName, camera_info, cluster_info, name=None, driver=None, desc=None,
                             is_delete=True, ret_response=False):
        """ 创建一个rtsp设备"""
        if not name:
            name = "waDevice_%s" % time_utils.get_time_str()
        cluster = {"id": cluster_info["id"]}
        if not driver:
            driver = {
                "enable": True,
                "ingresses": [
                  {
                    "description": "",
                    "information": {
                      "rtmp": {
                        "verification": {
                          "method": "TOKEN"
                        }
                      },
                      "type": "RTMP"
                    },
                    "name": name
                  }
                ]
              }
        resp = self.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=deviceKindName, name=name,
                                                            cluster=cluster, driver=driver, desc=desc)
        assert resp.status_code == 200
        device_id = resp.json_get("device.id")

        # 添加clear up
        def clearUp():
            self.ext_info.RasmanagerApi.deleteDeviceById(device_id)

        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        # self.ext_info.RasmanagerApi.getDeviceByIDUntilAvailable(device_id)
        if ret_response:
            return resp
        else:
            return device_id


    def createIOTDeviceWithRTMP(self, config_obj,cluster_info, name=None, driver=None, desc=None,
                                is_delete=True):
        """ 创建一个IOT类型的rtmp设备"""
        devicekind_name=config_obj.Clients.devicekind.name
        i=1
        if not name:
            name = "IOT_rtsp_Device_%s_%s" % (sign_utils.getUuid(4), time_utils.get_time_str())
        cluster = {"id": cluster_info["id"]}
        if not driver:
            driver = {
                         "ingresses": [
                             {
                                 "name": "ingress_rtmp_test",
                                 "description": "for rtmp test",
                                 "information": {
                                     "type": "RTMP",
                                     "rtmp": {
                                         "verification": {
                                             "method": "TOKEN"
                                         }
                                     }
                                 }
                             }
                         ],
                         "iot": {
                             "name": "symphony-1",
                             "information": {
                                 "type": "SYMPHONY"
                             }
                         },
                         "enable": True
                     }
        resp = self.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=devicekind_name, name=name,
                                                                      cluster=cluster, driver=driver, desc=desc)
        assert resp.status_code == 200
        device_id = resp.json_get("device.id")

        # 添加clear up
        def clearUp():

            self.ext_info.RasmanagerApi.deleteDeviceById(device_id)

        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        return resp

    def createIOTDeviceWithRTC(self, config_obj, cluster_info, name=None, driver=None, desc=None,
                               is_delete=True, ret_response=False):
        """ 创建一个IOT类型的rtc设备"""
        devicekind_name = config_obj.Clients.devicekind.name
        if not name:
            name = "IOT_RTC_Device_%s_%s" % (sign_utils.getUuid(4), time_utils.get_time_str())
        cluster = {"id": cluster_info["id"]}
        if not driver:
            driver = {
                "ingresses": [
                    {
                        "name": "ingress_webrtc_test",
                        "description": "for webrtc test",
                        "information": {
                            "type": "WEBRTC",
                            "webrtc": {}
                        }
                    }
                ],
                "iot": {
                    "name": "symphony-1",
                    "information": {
                        "type": "SYMPHONY"
                    }
                },
                "enable": True
            }
        resp = self.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=devicekind_name, name=name,
                                                                      cluster=cluster, driver=driver, desc=desc)
        assert resp.status_code == 200
        device_id = resp.json_get("device.id")

        # 添加clear up
        def clearUp():
            self.ext_info.RasmanagerApi.deleteDeviceById(device_id)

        if self.ext_info and is_delete:
            self.ext_info.addAfterFunc(clearUp)

        # self.ext_info.RasmanagerApi.getDeviceByIDUntilAvailable(device_id)
        if ret_response:
            return resp
        else:
            return resp
