#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestEdgeApi(object):
    """ edge Api测试"""

    @pytest.fixture(scope="class", autouse=True)
    def init_func(self, config_obj):
        # 初始化测试集
        # 所有test运行前运行一次，接收外部参数env_obj，初始化测试环境
        log().info("==========%s测试开始==========" % self.__class__.__name__)

    def teardown_class(self):
        # 所有test运行完后运行一次
        log().info("==========%s测试结束==========\n" % self.__name__)
        log().info("clear tasks finish")

    def setup_method(self, method):
        # 每个测试用例执行之前做操作
        log().info("用例%s开始" % method.__name__)

    def teardown_method(self, method):
        # 每个测试用例执行之后做操作
        log().info("用例%s结束" % method.__name__)

    def test_api_AppletManagerSrv_ActivationCodeInfo(self, config_obj, EdgeApi):
        """  ActivationCodeInfo 查看当前激活信息. """
        resp = EdgeApi.AppletManagerSrv_ActivationCodeInfoGetApi()
        assert resp.status_code == 200

    def test_api_AppletManagerSrv_ActivationCodeUpsert(self, config_obj, EdgeApi):
        """  upsert activation code，导入或更新当前全量激活码. """
        code = None
        resp = EdgeApi.AppletManagerSrv_ActivationCodeUpsertPostApi(code=code)
        assert resp.status_code == 200

    def test_api_AppletManagerSrv_ListApplet(self, config_obj, EdgeApi):
        """  list所有applet信息，包括算力、验签、激活信息. """
        resp = EdgeApi.AppletManagerSrv_ListAppletGetApi()
        assert resp.status_code == 200

    def test_api_AppletManagerSrv_AppletImport(self, config_obj, EdgeApi):
        """  导入一个applet，解析出其中的applet包中的meta信息，并进行验签工作，当有相关的任务存在... """
        content = None
        path = None
        resource_quota = None
        kestrel_version = None
        resp = EdgeApi.AppletManagerSrv_AppletImportPostApi(content=content, path=path, resource_quota=resource_quota, kestrel_version=kestrel_version)
        assert resp.status_code == 200

    def test_api_AppletManagerSrv_AppletGC(self, config_obj, EdgeApi):
        """  [internal] gc applet，每个applet仅保留最新的3个版本. """
        runningApplet = None
        resp = EdgeApi.AppletManagerSrv_AppletGCPostApi(runningApplet=runningApplet)
        assert resp.status_code == 200

    def test_api_AppletManagerSrv_AppletDelete(self, config_obj, EdgeApi):
        """  删除一个applet，有worker正在运行的applet不能删除. """
        name = None
        version = None
        resp = EdgeApi.AppletManagerSrv_AppletDeleteDeleteApi(name, version)
        assert resp.status_code == 200

    def test_api_AppletManagerSrv_AppletUpdate(self, config_obj, EdgeApi):
        """  更新applet meta信息，如quota, kestrel_version等，当有相关的任务存在... """
        name = None
        version = None
        resource_quota = None
        kestrel_version = None
        resp = EdgeApi.AppletManagerSrv_AppletUpdatePutApi(name, version, resource_quota=resource_quota, kestrel_version=kestrel_version)
        assert resp.status_code == 200

    def test_api_BizAppManagerSrv_ListBizApp(self, config_obj, EdgeApi):
        """  list 所有通过bizapp-manager导入的BizApp """
        resp = EdgeApi.BizAppManagerSrv_ListBizAppGetApi()
        assert resp.status_code == 200

    def test_api_BizAppManagerSrv_BizAppDelete(self, config_obj, EdgeApi):
        """  删除bizApp: 删除bizapp表数据, 删除applet_meta表数据, 删除bizapp-... """
        resp = EdgeApi.BizAppManagerSrv_BizAppDeleteDeleteApi()
        assert resp.status_code == 200

    def test_api_BizAppManagerSrv_BizAppImport(self, config_obj, EdgeApi):
        """  导入一个BizApp: 解析BizApp包中的meta信息并启动服务 """
        content = None
        path = None
        resp = EdgeApi.BizAppManagerSrv_BizAppImportPostApi(content=content, path=path)
        assert resp.status_code == 200

    def test_api_BizAppManagerSrv_BizAppStart(self, config_obj, EdgeApi):
        """  启动bizapp服务 """
        name = None
        version = None
        resp = EdgeApi.BizAppManagerSrv_BizAppStartPostApi(name=name, version=version)
        assert resp.status_code == 200

    def test_api_BizAppManagerSrv_BizAppStop(self, config_obj, EdgeApi):
        """  停止bizapp: 停止服务, 停止bizapp-task任务 """
        name = None
        version = None
        resp = EdgeApi.BizAppManagerSrv_BizAppStopPostApi(name=name, version=version)
        assert resp.status_code == 200

    def test_api_CallbackAgent_BatchPutObject(self, config_obj, EdgeApi):
        """  图像推送接口 """
        object_requests = None
        resp = EdgeApi.CallbackAgent_BatchPutObjectPostApi(object_requests=object_requests)
        assert resp.status_code == 200

    def test_api_CallbackAgent_ListCallbackConfig(self, config_obj, EdgeApi):
        """  查询callback配置列表. """
        resp = EdgeApi.CallbackAgent_ListCallbackConfigGetApi()
        assert resp.status_code == 200

    def test_api_CallbackAgent_AddCallbackConfig(self, config_obj, EdgeApi):
        """  增加callback配置项. """
        config = None
        resp = EdgeApi.CallbackAgent_AddCallbackConfigPostApi(config=config)
        assert resp.status_code == 200

    def test_api_CallbackAgent_UpdateCallbackConfig(self, config_obj, EdgeApi):
        """  更新callback配置项. """
        config = None
        resp = EdgeApi.CallbackAgent_UpdateCallbackConfigPutApi(config=config)
        assert resp.status_code == 200

    def test_api_CallbackAgent_GetCallbackConfig(self, config_obj, EdgeApi):
        """  查询callback的配置. """
        id = None
        resp = EdgeApi.CallbackAgent_GetCallbackConfigGetApi(id)
        assert resp.status_code == 200

    def test_api_CallbackAgent_DeleteCallbackConfig(self, config_obj, EdgeApi):
        """  删除callback配置项. """
        id = None
        resp = EdgeApi.CallbackAgent_DeleteCallbackConfigDeleteApi(id)
        assert resp.status_code == 200

    def test_api_CallbackAgent_VIIDNew(self, config_obj, EdgeApi):
        """  创建视图库 """
        viid_id = None
        viid_param = None
        extra_infos = None
        resp = EdgeApi.CallbackAgent_VIIDNewPostApi(viid_id=viid_id, viid_param=viid_param, extra_infos=extra_infos)
        assert resp.status_code == 200

    def test_api_CallbackAgent_VIIDInfo(self, config_obj, EdgeApi):
        """  查看视图库信息 """
        viid_id = None
        resp = EdgeApi.CallbackAgent_VIIDInfoGetApi(viid_id)
        assert resp.status_code == 200

    def test_api_CallbackAgent_VIIDDelete(self, config_obj, EdgeApi):
        """  删除视图库 """
        viid_id = None
        resp = EdgeApi.CallbackAgent_VIIDDeleteDeleteApi(viid_id)
        assert resp.status_code == 200

    def test_api_NebulaDbSyncCallbackAgent_EventCallback(self, config_obj, EdgeApi):
        """  业务方实现，用来接收 nebula-db-sync-agent """
        content_type = None
        portrait_db_add = None
        portrait_db_delete = None
        portrait_db_update = None
        portrait_add = None
        portrait_delete = None
        portrait_update = None
        resp = EdgeApi.NebulaDbSyncCallbackAgent_EventCallbackPostApi(content_type=content_type, portrait_db_add=portrait_db_add, portrait_db_delete=portrait_db_delete, portrait_db_update=portrait_db_update, portrait_add=portrait_add, portrait_delete=portrait_delete, portrait_update=portrait_update)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetRealTimeBGIMG(self, config_obj, EdgeApi):
        """  GetRealTimeBGIMG 获取实时背景大图... """
        camera_id = None
        resp = EdgeApi.NebulaIOTAgentSrv_GetRealTimeBGIMGGetApi(camera_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetDefaultNic(self, config_obj, EdgeApi):
        """  获取默认网卡 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetDefaultNicGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_SetDefaultNicByName(self, config_obj, EdgeApi):
        """  设置网卡为默认网卡 """
        name = None
        resp = EdgeApi.NebulaIOTAgentSrv_SetDefaultNicByNamePostApi(name)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetDeviceDisksInfo(self, config_obj, EdgeApi):
        """  GetDeviceDisksInfo 获取设备磁盘信息 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetDeviceDisksInfoGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetDNSConfig(self, config_obj, EdgeApi):
        """  GetDNSConfig 获取 DNS 配置信息 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetDNSConfigGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_SetDNSConfig(self, config_obj, EdgeApi):
        """  SetDNSConfig 设置 DNS """
        dns = None
        resp = EdgeApi.NebulaIOTAgentSrv_SetDNSConfigPostApi(dns=dns)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetIPConfig(self, config_obj, EdgeApi):
        """  GetIPConfig 获取 IP 配置信息 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetIPConfigGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_SetIPConfig(self, config_obj, EdgeApi):
        """  SetIPConfig 设置 IP (Pallas平台, 不支持interface alias配置) """
        ip = None
        resp = EdgeApi.NebulaIOTAgentSrv_SetIPConfigPostApi(ip=ip)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetModemAPN(self, config_obj, EdgeApi):
        """  GetModemAPN 获取4G插卡状态，运营商信息，IMSI,信号强度,APN名称，用户名，密码 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetModemAPNGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_CloseModemAPN(self, config_obj, EdgeApi):
        """  关闭4G功能 """
        resp = EdgeApi.NebulaIOTAgentSrv_CloseModemAPNDeleteApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_OpenModemAPN(self, config_obj, EdgeApi):
        """  开启4G功能，4G卡未插卡时，4G功能不可开启 """
        apn = None
        resp = EdgeApi.NebulaIOTAgentSrv_OpenModemAPNPostApi(apn=apn)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetNTPConfig(self, config_obj, EdgeApi):
        """  GetNTPConfig 获取 NTP 配置信息 (Pallas平台, port参数设置为"123"... """
        resp = EdgeApi.NebulaIOTAgentSrv_GetNTPConfigGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_SetNTPConfig(self, config_obj, EdgeApi):
        """  SetNTPConfig 设置 NTP (Pallas平台，port参数只能是"123"或者"") """
        ntp = None
        resp = EdgeApi.NebulaIOTAgentSrv_SetNTPConfigPostApi(ntp=ntp)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_Ping(self, config_obj, EdgeApi):
        """  Ping ping 指定地址，用于测试网络情况 """
        address = None
        resp = EdgeApi.NebulaIOTAgentSrv_PingPostApi(address=address)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetRegisterState(self, config_obj, EdgeApi):
        """  获取设备注册信息 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetRegisterStateGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetROUTEConfig(self, config_obj, EdgeApi):
        """  GetROUTEConfig 获取 路由表 配置信息 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetROUTEConfigGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_SetROUTEConfig(self, config_obj, EdgeApi):
        """  SetROUTEConfig 设置 路由表 """
        route = None
        resp = EdgeApi.NebulaIOTAgentSrv_SetROUTEConfigPostApi(route=route)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetSerialNumber(self, config_obj, EdgeApi):
        """  GetSerialNumber 获取设备序列号 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetSerialNumberGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetTIMEConfig(self, config_obj, EdgeApi):
        """  GetTIMEConfig 获取 系统时间 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetTIMEConfigGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_SetTIMEConfig(self, config_obj, EdgeApi):
        """  SetTIMEConfig 设置 系统时间 """
        time = None
        resp = EdgeApi.NebulaIOTAgentSrv_SetTIMEConfigPostApi(time=time)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetRegisterUserMeta(self, config_obj, EdgeApi):
        """  GetRegisterUserMeta 获取用户自注册信息 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetRegisterUserMetaGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_SetRegisterUserMeta(self, config_obj, EdgeApi):
        """  SetRegisterUserMeta 设置用户自注册信息 """
        user_meta = None
        resp = EdgeApi.NebulaIOTAgentSrv_SetRegisterUserMetaPostApi(user_meta=user_meta)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetVersionInfo(self, config_obj, EdgeApi):
        """  GetVersionInfo 获取序列号SN，Pallas固件版本ROM(t4不提供)，Viperl... """
        resp = EdgeApi.NebulaIOTAgentSrv_GetVersionInfoGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetLicenseState(self, config_obj, EdgeApi):
        """  GetLicenseState 获取 license 信息 """
        resp = EdgeApi.NebulaIOTAgentSrv_GetLicenseStateGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_SetLicense(self, config_obj, EdgeApi):
        """  SetLicense 设置 license 信息(详情参考注释)
Use POST http met... """
        resp = EdgeApi.NebulaIOTAgentSrv_SetLicensePostApi()
        assert resp.status_code == 200

    # learn_2 fixture的使用
    # learn_3 api的使用
    def test_api_NebulaIOTAgentSrv_UpsertSubDevice(self, config_obj, EdgeApi, client_info, camera_info):
        """  UpsertSubDevice 更新/添加子设备, device_id不存在时添加，存在时更新。
该... """
        device_id = sign_utils.getUuid(32)
        subdevice = {
            "brand": camera_info.brand,
            "device_config": {
                "ip": {
                    "ips": [
                        {
                            "address": camera_info.ip
                        }
                    ]
                }
            },
            "device_id": device_id,  # 存在=>更新, 不存在=>创建
            "extra_config": {
                "camera_config": {
                    "auth": {
                        "username": camera_info.username,
                        "password": camera_info.password,
                    },
                    "manage_port": camera_info.port,
                    "video_source_config": {
                        "rtsp_parameter": {
                            "parameter": {
                                "url": camera_info.rtsp
                            }
                        }
                    },
                }
            },
            "name": device_id,
            "device_kind": camera_info.kind
        }
        skip = None
        resp = EdgeApi.NebulaIOTAgentSrv_UpsertSubDevicePostApi(subdevice=subdevice, skip=skip)
        assert resp.status_code == 200
        assert resp.json_get("code") == 0
        assert resp.json_get("subdevice.device_kind") == camera_info.kind
        assert resp.json_get("subdevice.device_id") == device_id
        assert resp.json_get("subdevice.extra_config.username") == camera_info.username
        assert resp.json_get("subdevice.extra_config.password") == '*****'
        assert resp.json_get("subdevice.brand") == camera_info.brand
        assert resp.json_get("subdevice.name") == device_id

    def test_api_NebulaIOTAgentSrv_ListAllSubDevices(self, config_obj, EdgeApi):
        """  ListAllSubDevices 获取所有子设备信息 """
        resp = EdgeApi.NebulaIOTAgentSrv_ListAllSubDevicesGetApi()
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetSubDeviceByFilter(self, config_obj, EdgeApi):
        """  GetSubDeviceByFilter 根据 ID, name, IP, rtsp_url 获取子... """
        sub_filter_device_id = None
        sub_filter_name = None
        sub_filter_address = None
        sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url = None
        resp = EdgeApi.NebulaIOTAgentSrv_GetSubDeviceByFilterGetApi(sub_filter_device_id=sub_filter_device_id, sub_filter_name=sub_filter_name, sub_filter_address=sub_filter_address, sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url=sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetSubDeviceStreamsByID(self, config_obj, EdgeApi):
        """   """
        id = None
        resp = EdgeApi.NebulaIOTAgentSrv_GetSubDeviceStreamsByIDGetApi(id)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_GetSubDeviceByID(self, config_obj, EdgeApi):
        """  GetSubDeviceByID 根据 ID 获取子设备信息 """
        id = "042cb55c1aa62a73f947387cd96f59ff"
        resp = EdgeApi.NebulaIOTAgentSrv_GetSubDeviceByIDGetApi(id)
        assert resp.status_code == 200

    def test_api_NebulaIOTAgentSrv_RemoveSubDeviceByID(self, config_obj, EdgeApi):
        """  RemoveSubDeviceByID 根据 ID 删除子设备 """
        id = "8ba2b80eb11f35a9cc0e8e05c01f2647"
        skip = None
        resp = EdgeApi.NebulaIOTAgentSrv_RemoveSubDeviceByIDDeleteApi(id, skip=skip)
        assert resp.status_code == 200

    def test_api_NebulaKongGatewaySrv_ImportKongConfigByBizapp(self, config_obj, EdgeApi):
        """  上传bizapp kong gateway配置文件 """
        bizapp = None
        config = None
        resp = EdgeApi.NebulaKongGatewaySrv_ImportKongConfigByBizappPostApi(bizapp=bizapp, config=config)
        assert resp.status_code == 200

    def test_api_NebulaKongGatewaySrv_GetPluginApiAuthWhiteUrls(self, config_obj, EdgeApi):
        """  获取nebula-api-auth.white_urls """
        resp = EdgeApi.NebulaKongGatewaySrv_GetPluginApiAuthWhiteUrlsGetApi()
        assert resp.status_code == 200

    def test_api_NebulaKongGatewaySrv_DelPluginApiAuthWhiteUrls(self, config_obj, EdgeApi):
        """  删除nebula-api-auth.white_urls """
        url_path = None
        url_method = None
        resp = EdgeApi.NebulaKongGatewaySrv_DelPluginApiAuthWhiteUrlsDeleteApi(url_path=url_path, url_method=url_method)
        assert resp.status_code == 200

    def test_api_NebulaKongGatewaySrv_AddPluginApiAuthWhiteUrls(self, config_obj, EdgeApi):
        """  增加nebula-api-auth.white_urls """
        url = None
        resp = EdgeApi.NebulaKongGatewaySrv_AddPluginApiAuthWhiteUrlsPostApi(url=url)
        assert resp.status_code == 200

    def test_api_NebulaKongGatewaySrv_GetPluginJwtWhiteUrls(self, config_obj, EdgeApi):
        """  获取nebula-jwt.white_urls """
        resp = EdgeApi.NebulaKongGatewaySrv_GetPluginJwtWhiteUrlsGetApi()
        assert resp.status_code == 200

    def test_api_NebulaKongGatewaySrv_DelPluginJwtWhiteUrls(self, config_obj, EdgeApi):
        """  删除nebula-jwt.white_urls """
        url_path = None
        url_method = None
        resp = EdgeApi.NebulaKongGatewaySrv_DelPluginJwtWhiteUrlsDeleteApi(url_path=url_path, url_method=url_method)
        assert resp.status_code == 200

    def test_api_NebulaKongGatewaySrv_AddPluginJwtWhiteUrls(self, config_obj, EdgeApi):
        """  增加nebula-jwt.white_urls """
        url = None
        resp = EdgeApi.NebulaKongGatewaySrv_AddPluginJwtWhiteUrlsPostApi(url=url)
        assert resp.status_code == 200

    def test_api_NebulaKongGatewaySrv_GetKongConfigByBizapp(self, config_obj, EdgeApi):
        """  获取bizapp kong gateway配置文件 """
        bizapp = None
        resp = EdgeApi.NebulaKongGatewaySrv_GetKongConfigByBizappGetApi(bizapp)
        assert resp.status_code == 200

    def test_api_NebulaKongGatewaySrv_RemoveKongConfigByBizapp(self, config_obj, EdgeApi):
        """  删除bizapp kong gateway配置文件 """
        bizapp = None
        resp = EdgeApi.NebulaKongGatewaySrv_RemoveKongConfigByBizappDeleteApi(bizapp)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_BatchCreateTask(self, config_obj, EdgeApi):
        """  创建任务 """
        requests = None
        resp = EdgeApi.BizAppTaskDefaultService_BatchCreateTaskPostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_DeleteRecord(self, config_obj, EdgeApi):
        """  删除记录 """
        ids = None
        resp = EdgeApi.BizAppTaskDefaultService_DeleteRecordPostApi(ids=ids)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_ExportRecord(self, config_obj, EdgeApi):
        """  导出记录 """
        start_time = None
        end_time = None
        sub_device_name = None
        sub_device_id = None
        task_name = None
        task_id = None
        task_type = None
        applet_record_type = None
        lib_type = None
        portrait_id = None
        name = None
        page = None
        attributes = None
        resp = EdgeApi.BizAppTaskDefaultService_ExportRecordPostApi(start_time=start_time, end_time=end_time, sub_device_name=sub_device_name, sub_device_id=sub_device_id, task_name=task_name, task_id=task_id, task_type=task_type, applet_record_type=applet_record_type, lib_type=lib_type, portrait_id=portrait_id, name=name, page=page, attributes=attributes)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_QueryRecord(self, config_obj, EdgeApi):
        """  查询记录 """
        start_time = None
        end_time = None
        sub_device_name = None
        sub_device_id = None
        task_name = None
        task_id = None
        task_type = None
        applet_record_type = None
        lib_type = None
        portrait_id = None
        name = None
        page = None
        attributes = None
        resp = EdgeApi.BizAppTaskDefaultService_QueryRecordPostApi(start_time=start_time, end_time=end_time, sub_device_name=sub_device_name, sub_device_id=sub_device_id, task_name=task_name, task_id=task_id, task_type=task_type, applet_record_type=applet_record_type, lib_type=lib_type, portrait_id=portrait_id, name=name, page=page, attributes=attributes)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_UpdateRecord(self, config_obj, EdgeApi):
        """  更新记录 """
        field = None
        ids = None
        resp = EdgeApi.BizAppTaskDefaultService_UpdateRecordPostApi(field=field, ids=ids)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_DeleteTask(self, config_obj, EdgeApi):
        """  删除任务 """
        resp = EdgeApi.BizAppTaskDefaultService_DeleteTaskDeleteApi()
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_CreateTask(self, config_obj, EdgeApi):
        """  创建任务 """
        name = None
        task_type = None
        desc = None
        detect_type = None
        active = None
        sub_device_ids = None
        object_config = None
        extend_config = None
        schedule = None
        identifier_id = None
        stream_type = None
        not_support_merge = None
        dbs = None
        resp = EdgeApi.BizAppTaskDefaultService_CreateTaskPostApi(name=name, task_type=task_type, desc=desc, detect_type=detect_type, active=active, sub_device_ids=sub_device_ids, object_config=object_config, extend_config=extend_config, schedule=schedule, identifier_id=identifier_id, stream_type=stream_type, not_support_merge=not_support_merge, dbs=dbs)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_UpdateTask(self, config_obj, EdgeApi):
        """  修改任务 """
        task_ids = None
        name = None
        desc = None
        object_config = None
        extend_config = None
        schedule = None
        dbs = None
        resp = EdgeApi.BizAppTaskDefaultService_UpdateTaskPutApi(task_ids=task_ids, name=name, desc=desc, object_config=object_config, extend_config=extend_config, schedule=schedule, dbs=dbs)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_QueryAllTask(self, config_obj, EdgeApi):
        """  查询所有任务(无分页)，使用场景：任务的下拉框查询 """
        active = None
        db_id = None
        task_types = None
        resp = EdgeApi.BizAppTaskDefaultService_QueryAllTaskPostApi(active=active, db_id=db_id, task_types=task_types)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_DisableTask(self, config_obj, EdgeApi):
        """  禁用任务 """
        task_ids = None
        resp = EdgeApi.BizAppTaskDefaultService_DisableTaskPutApi(task_ids=task_ids)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_EnableTask(self, config_obj, EdgeApi):
        """  启用任务 """
        task_ids = None
        resp = EdgeApi.BizAppTaskDefaultService_EnableTaskPutApi(task_ids=task_ids)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_QueryTask(self, config_obj, EdgeApi):
        """  查询任务(有分页)，正常的分页查询 """
        page_num = None
        page_size = None
        keyword = None
        sub_device_ids = None
        resp = EdgeApi.BizAppTaskDefaultService_QueryTaskPostApi(page_num=page_num, page_size=page_size, keyword=keyword, sub_device_ids=sub_device_ids)
        assert resp.status_code == 200

    def test_api_BizAppTaskDefaultService_DetailTask(self, config_obj, EdgeApi):
        """  详情任务 """
        task_id = None
        resp = EdgeApi.BizAppTaskDefaultService_DetailTaskGetApi(task_id)
        assert resp.status_code == 200

    def test_api_BizAppTaskService_DeleteTask(self, config_obj, EdgeApi):
        """  删除任务 """
        resp = EdgeApi.BizAppTaskService_DeleteTaskDeleteApi()
        assert resp.status_code == 200

    def test_api_BizAppTaskService_CreateTask(self, config_obj, EdgeApi):
        """  创建任务, response里始终包括匹配个数的Result, bizapp-default依赖此约... """
        name = None
        task_type = None
        desc = None
        detect_type = None
        active = None
        sub_device_ids = None
        object_config = None
        extend_config = None
        schedule = None
        identifier_id = None
        stream_type = None
        not_support_merge = None
        dbs = None
        resp = EdgeApi.BizAppTaskService_CreateTaskPostApi(name=name, task_type=task_type, desc=desc, detect_type=detect_type, active=active, sub_device_ids=sub_device_ids, object_config=object_config, extend_config=extend_config, schedule=schedule, identifier_id=identifier_id, stream_type=stream_type, not_support_merge=not_support_merge, dbs=dbs)
        assert resp.status_code == 200

    def test_api_BizAppTaskService_UpdateTask(self, config_obj, EdgeApi):
        """  修改任务 """
        task_ids = None
        name = None
        desc = None
        object_config = None
        extend_config = None
        schedule = None
        dbs = None
        resp = EdgeApi.BizAppTaskService_UpdateTaskPutApi(task_ids=task_ids, name=name, desc=desc, object_config=object_config, extend_config=extend_config, schedule=schedule, dbs=dbs)
        assert resp.status_code == 200

    def test_api_BizAppTaskService_QueryAllTask(self, config_obj, EdgeApi):
        """  查询所有任务(无分页)，使用场景：任务的下拉框查询 """
        active = None
        db_id = None
        task_types = None
        resp = EdgeApi.BizAppTaskService_QueryAllTaskPostApi(active=active, db_id=db_id, task_types=task_types)
        assert resp.status_code == 200

    def test_api_BizAppTaskService_DisableTask(self, config_obj, EdgeApi):
        """  禁用任务 """
        task_ids = None
        resp = EdgeApi.BizAppTaskService_DisableTaskPutApi(task_ids=task_ids)
        assert resp.status_code == 200

    def test_api_BizAppTaskService_EnableTask(self, config_obj, EdgeApi):
        """  启用任务 """
        task_ids = None
        resp = EdgeApi.BizAppTaskService_EnableTaskPutApi(task_ids=task_ids)
        assert resp.status_code == 200

    def test_api_BizAppTaskService_LicenseStatistics(self, config_obj, EdgeApi):
        """  License授权信息 """
        resp = EdgeApi.BizAppTaskService_LicenseStatisticsGetApi()
        assert resp.status_code == 200

    def test_api_BizAppTaskService_PowerInfo(self, config_obj, EdgeApi):
        """  获取算力信息 """
        resp = EdgeApi.BizAppTaskService_PowerInfoGetApi()
        assert resp.status_code == 200

    def test_api_BizAppTaskService_QueryTask(self, config_obj, EdgeApi):
        """  查询任务(有分页)，正常的分页查询 """
        page_num = None
        page_size = None
        keyword = None
        sub_device_ids = None
        resp = EdgeApi.BizAppTaskService_QueryTaskPostApi(page_num=page_num, page_size=page_size, keyword=keyword, sub_device_ids=sub_device_ids)
        assert resp.status_code == 200

    def test_api_BizAppTaskService_DetailTask(self, config_obj, EdgeApi):
        """  详情任务 """
        task_id = None
        resp = EdgeApi.BizAppTaskService_DetailTaskGetApi(task_id)
        assert resp.status_code == 200

    def test_api_ScheduleService_GetStorageInfo(self, config_obj, EdgeApi):
        """  获取当前抓拍图片存储空间信息 """
        resp = EdgeApi.ScheduleService_GetStorageInfoGetApi()
        assert resp.status_code == 200

    def test_api_ScheduleService_ClearRecord(self, config_obj, EdgeApi):
        """   """
        resp = EdgeApi.ScheduleService_ClearRecordDeleteApi()
        assert resp.status_code == 200

    def test_api_ScheduleService_GetSystemInfo(self, config_obj, EdgeApi):
        """  获取一些系统配置信息 """
        resp = EdgeApi.ScheduleService_GetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_ScheduleService_SetSystemInfo(self, config_obj, EdgeApi):
        """  设置一些系统配置信息 """
        save_days = None
        resp = EdgeApi.ScheduleService_SetSystemInfoPostApi(save_days=save_days)
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_BatchGetTask(self, config_obj, EdgeApi):
        """  批量获取任务 """
        task_ids = None
        resp = EdgeApi.TaskManagerSrv_BatchGetTaskGetApi(task_ids=task_ids)
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_BatchDeleteTask(self, config_obj, EdgeApi):
        """  批量删除任务 """
        task_ids = None
        resp = EdgeApi.TaskManagerSrv_BatchDeleteTaskDeleteApi(task_ids=task_ids)
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_BatchCreateTask(self, config_obj, EdgeApi):
        """  批量创建任务 """
        requests = None
        resp = EdgeApi.TaskManagerSrv_BatchCreateTaskPostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_BatchUpdateTask(self, config_obj, EdgeApi):
        """  批量更新任务 """
        requests = None
        resp = EdgeApi.TaskManagerSrv_BatchUpdateTaskPutApi(requests=requests)
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_Hello(self, config_obj, EdgeApi):
        """  Hello . """
        resp = EdgeApi.TaskManagerSrv_HelloGetApi()
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_GetPowerInfo(self, config_obj, EdgeApi):
        """  查询算力信息 """
        resp = EdgeApi.TaskManagerSrv_GetPowerInfoGetApi()
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_ListTask(self, config_obj, EdgeApi):
        """  获取任务列表 """
        resp = EdgeApi.TaskManagerSrv_ListTaskGetApi()
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_CreateTask(self, config_obj, EdgeApi):
        """  创建任务 """
        task = None
        resp = EdgeApi.TaskManagerSrv_CreateTaskPostApi(task=task)
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_GetTask(self, config_obj, EdgeApi):
        """  根据task_id获取任务 """
        task_id = None
        resp = EdgeApi.TaskManagerSrv_GetTaskGetApi(task_id)
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_DeleteTask(self, config_obj, EdgeApi):
        """  根据task_id删除任务 """
        task_id = None
        resp = EdgeApi.TaskManagerSrv_DeleteTaskDeleteApi(task_id)
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_UpdateTask(self, config_obj, EdgeApi):
        """  更新任务 """
        task_id = None
        task = None
        resp = EdgeApi.TaskManagerSrv_UpdateTaskPutApi(task_id, task=task)
        assert resp.status_code == 200

    def test_api_TaskManagerSrv_GetWorkerInfo(self, config_obj, EdgeApi):
        """  查询worker信息 """
        resp = EdgeApi.TaskManagerSrv_GetWorkerInfoGetApi()
        assert resp.status_code == 200

    def test_api_OTAEngineService_FirmwareList(self, config_obj, EdgeApi):
        """  固件列表 """
        list_applet_only = None
        resp = EdgeApi.OTAEngineService_FirmwareListGetApi(list_applet_only=list_applet_only)
        assert resp.status_code == 200

    def test_api_OTAEngineService_FirmwareUnregister(self, config_obj, EdgeApi):
        """  固件卸载 """
        name = None
        current_version = None
        resp = EdgeApi.OTAEngineService_FirmwareUnregisterDeleteApi(name=name, current_version=current_version)
        assert resp.status_code == 200

    def test_api_OTAEngineService_FirmwareRegister(self, config_obj, EdgeApi):
        """  固件注册 """
        name = None
        current_version = None
        ext_data = None
        resp = EdgeApi.OTAEngineService_FirmwareRegisterPostApi(name=name, current_version=current_version, ext_data=ext_data)
        assert resp.status_code == 200

    def test_api_OTAEngineService_FirmwareUpgrade(self, config_obj, EdgeApi):
        """  固件上传并执行安装，不负责升级的原子性，一但由于比如机器重启被打断之后不能恢复。
支持request... """
        resp = EdgeApi.OTAEngineService_FirmwareUpgradePostApi()
        assert resp.status_code == 200

    def test_api_Portraits_CreatePortraits(self, config_obj, EdgeApi):
        """  创建人像 """
        db_id = None
        portrait_infos = None
        quality_threshold = None
        resp = EdgeApi.Portraits_CreatePortraitsPostApi(db_id=db_id, portrait_infos=portrait_infos, quality_threshold=quality_threshold)
        assert resp.status_code == 200

    def test_api_Portraits_UpdatePortraits(self, config_obj, EdgeApi):
        """  更新人像 """
        db_id = None
        portrait_infos = None
        quality_threshold = None
        resp = EdgeApi.Portraits_UpdatePortraitsPutApi(db_id=db_id, portrait_infos=portrait_infos, quality_threshold=quality_threshold)
        assert resp.status_code == 200

    def test_api_Portraits_CompareImageInDB(self, config_obj, EdgeApi):
        """  单张图片跟库中指定人像进行1:1比对 """
        db_id = None
        portrait_id = None
        image = None
        resp = EdgeApi.Portraits_CompareImageInDBPostApi(db_id=db_id, portrait_id=portrait_id, image=image)
        assert resp.status_code == 200

    def test_api_Portraits_CompareOneToOne(self, config_obj, EdgeApi):
        """  图片1:1比对 """
        image_1 = None
        image_2 = None
        feature_version = None
        resp = EdgeApi.Portraits_CompareOneToOnePostApi(image_1=image_1, image_2=image_2, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_Portraits_GetPortraitsConfig(self, config_obj, EdgeApi):
        """  获取全局配置信息 """
        resp = EdgeApi.Portraits_GetPortraitsConfigGetApi()
        assert resp.status_code == 200

    def test_api_Portraits_ListPortraitDbs(self, config_obj, EdgeApi):
        """  查询人像库列表 """
        page_offset = None
        page_limit = None
        page_total = None
        token = EdgeApi.getToken()
        resp = EdgeApi.Portraits_ListPortraitDbsGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total,loginToken=token)
        assert resp.status_code == 200

    def test_api_Portraits_CreatePortraitDb(self, config_obj, EdgeApi):
        """  创建人像库 """
        db_name = None
        db_type = None
        db_capacity = None
        operator = None
        feature_version = None
        description = None
        resp = EdgeApi.Portraits_CreatePortraitDbPostApi(db_name=db_name, db_type=db_type, db_capacity=db_capacity, operator=operator, feature_version=feature_version, description=description)
        assert resp.status_code == 200

    def test_api_Portraits_DeletePortraitDb(self, config_obj, EdgeApi):
        """  删除人像库 """
        db_id = None
        unsafe_mode = None
        operator = None
        resp = EdgeApi.Portraits_DeletePortraitDbPostApi(db_id=db_id, unsafe_mode=unsafe_mode, operator=operator)
        assert resp.status_code == 200

    def test_api_Portraits_QueryPortraitDbs(self, config_obj, EdgeApi):
        """  查询人像库集合信息 """
        db_ids = None
        resp = EdgeApi.Portraits_QueryPortraitDbsPostApi(db_ids=db_ids)
        assert resp.status_code == 200

    def test_api_Portraits_UpdatePortraitDb(self, config_obj, EdgeApi):
        """  更新人像库 """
        db_id = None
        db_name = None
        db_type = None
        description = None
        operator = None
        resp = EdgeApi.Portraits_UpdatePortraitDbPutApi(db_id, db_name=db_name, db_type=db_type, description=description, operator=operator)
        assert resp.status_code == 200

    def test_api_Portraits_DecryptTexts(self, config_obj, EdgeApi):
        """  文本解密 """
        texts = None
        resp = EdgeApi.Portraits_DecryptTextsPutApi(texts=texts)
        assert resp.status_code == 200

    def test_api_Portraits_DeletePortraits(self, config_obj, EdgeApi):
        """  删除人像 """
        db_id = None
        portrait_ids = None
        resp = EdgeApi.Portraits_DeletePortraitsPostApi(db_id=db_id, portrait_ids=portrait_ids)
        assert resp.status_code == 200

    def test_api_Portraits_ExportPortraits(self, config_obj, EdgeApi):
        """  导出人像 """
        portraits_ids = None
        db_id = None
        resp = EdgeApi.Portraits_ExportPortraitsPostApi(portraits_ids=portraits_ids, db_id=db_id)
        assert resp.status_code == 200

    def test_api_Portraits_ListPortraits(self, config_obj, EdgeApi):
        """  查询人像列表 """
        db_id = None
        encrypted = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = EdgeApi.Portraits_ListPortraitsGetApi(db_id=db_id, encrypted=encrypted, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_Portraits_QueryPortraits(self, config_obj, EdgeApi):
        """  查询人像 """
        db_id = None
        encrypted = None
        portrait_ids = None
        resp = EdgeApi.Portraits_QueryPortraitsPostApi(db_id=db_id, encrypted=encrypted, portrait_ids=portrait_ids)
        assert resp.status_code == 200

    def test_api_Portraits_SearchPortraits(self, config_obj, EdgeApi):
        """  搜索人像 """
        db_ids = None
        encrypted = None
        page = None
        name = None
        job_number = None
        ic_number = None
        id_number = None
        start_activation_time = None
        end_activation_time = None
        start_expire_time = None
        end_expire_time = None
        status = None
        resp = EdgeApi.Portraits_SearchPortraitsPostApi(db_ids=db_ids, encrypted=encrypted, page=page, name=name, job_number=job_number, ic_number=ic_number, id_number=id_number, start_activation_time=start_activation_time, end_activation_time=end_activation_time, start_expire_time=start_expire_time, end_expire_time=end_expire_time, status=status)
        assert resp.status_code == 200

    def test_api_Portraits_SearchImageInDBs(self, config_obj, EdgeApi):
        """  在多个人像库进行图片1:N比对 """
        dbs = None
        image = None
        resp = EdgeApi.Portraits_SearchImageInDBsPostApi(dbs=dbs, image=image)
        assert resp.status_code == 200

    def test_api_RecordProcess_DeleteBizAppInfo(self, config_obj, EdgeApi):
        """  【内部接口】删除bizapp，用于删除用户自定义bizapp的topic等信息，则记录将不会转发给设... """
        bizapp_name = None
        bizapp_version = None
        resp = EdgeApi.RecordProcess_DeleteBizAppInfoPostApi(bizapp_name=bizapp_name, bizapp_version=bizapp_version)
        assert resp.status_code == 200

    def test_api_RecordProcess_GetBizAppInfo(self, config_obj, EdgeApi):
        """  【内部接口】查询具体bizapp的推送topic """
        biz_app_name = None
        resp = EdgeApi.RecordProcess_GetBizAppInfoGetApi(biz_app_name)
        assert resp.status_code == 200

    def test_api_RecordProcess_SetBizAppInfo(self, config_obj, EdgeApi):
        """  设置具体bizapp的推送topic，用于设置用户自定义bizapp的topic等信息，则记录会转发... """
        bizapp_info = None
        resp = EdgeApi.RecordProcess_SetBizAppInfoPostApi(bizapp_info=bizapp_info)
        assert resp.status_code == 200

    def test_api_RecordProcess_GetStorageSwitch(self, config_obj, EdgeApi):
        """  【内部接口】查询storage使用的是es还是pg """
        resp = EdgeApi.RecordProcess_GetStorageSwitchGetApi()
        assert resp.status_code == 200

    def test_api_RecordProcess_GetTracelessSwitch(self, config_obj, EdgeApi):
        """  查询当前无痕模式 """
        resp = EdgeApi.RecordProcess_GetTracelessSwitchGetApi()
        assert resp.status_code == 200

    def test_api_RecordProcess_SetTracelessSwitch(self, config_obj, EdgeApi):
        """  设置当前无痕模式
无痕模式设置开启时:会清除所有已经产生的记录，图片不清除，且后续记录将存记录，不... """
        storage_mode = None
        resp = EdgeApi.RecordProcess_SetTracelessSwitchPostApi(storage_mode=storage_mode)
        assert resp.status_code == 200

    def test_api_AgentUserService_ListAPIInfo(self, config_obj, EdgeApi):
        """  API信息列表. """
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = EdgeApi.AgentUserService_ListAPIInfoGetApi(paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_AgentUserService_AddAPIInfo(self, config_obj, EdgeApi):
        """  增加API信息. """
        api = None
        resp = EdgeApi.AgentUserService_AddAPIInfoPostApi(api=api)
        assert resp.status_code == 200

    def test_api_AgentUserService_UpdateAPIInfo(self, config_obj, EdgeApi):
        """  更新API信息. """
        api = None
        resp = EdgeApi.AgentUserService_UpdateAPIInfoPutApi(api=api)
        assert resp.status_code == 200

    def test_api_AgentUserService_GetAPIInfo(self, config_obj, EdgeApi):
        """  查询API信息. """
        id = None
        resp = EdgeApi.AgentUserService_GetAPIInfoGetApi(id)
        assert resp.status_code == 200

    def test_api_AgentUserService_DeleteAPIInfo(self, config_obj, EdgeApi):
        """  删除API信息. """
        id = None
        resp = EdgeApi.AgentUserService_DeleteAPIInfoDeleteApi(id)
        assert resp.status_code == 200

    def test_api_AgentUserService_Captcha(self, config_obj, EdgeApi):
        """  图形验证码. """
        resp = EdgeApi.AgentUserService_CaptchaGetApi()
        assert resp.status_code == 200

    def test_api_AgentUserService_ListRole(self, config_obj, EdgeApi):
        """  角色列表. """
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = EdgeApi.AgentUserService_ListRoleGetApi(paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_AgentUserService_AddRole(self, config_obj, EdgeApi):
        """  创建角色. """
        role = None
        resp = EdgeApi.AgentUserService_AddRolePostApi(role=role)
        assert resp.status_code == 200

    def test_api_AgentUserService_UpdateRole(self, config_obj, EdgeApi):
        """  修改角色. """
        role = None
        resp = EdgeApi.AgentUserService_UpdateRolePutApi(role=role)
        assert resp.status_code == 200

    def test_api_AgentUserService_GetRole(self, config_obj, EdgeApi):
        """  查询角色详情 """
        id = None
        resp = EdgeApi.AgentUserService_GetRoleGetApi(id)
        assert resp.status_code == 200

    def test_api_AgentUserService_DeleteRole(self, config_obj, EdgeApi):
        """  删除角色. """
        id = None
        resp = EdgeApi.AgentUserService_DeleteRoleDeleteApi(id)
        assert resp.status_code == 200

    def test_api_AgentUserService_ListUser(self, config_obj, EdgeApi):
        """  查询用户列表. """
        paging_offset = None
        paging_limit = None
        paging_total = None
        decrypt = None
        resp = EdgeApi.AgentUserService_ListUserGetApi(paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, decrypt=decrypt)
        assert resp.status_code == 200

    def test_api_AgentUserService_AddUser(self, config_obj, EdgeApi):
        """  增加用户. """
        user = None
        resp = EdgeApi.AgentUserService_AddUserPostApi(user=user)
        assert resp.status_code == 200

    def test_api_AgentUserService_UpdateUser(self, config_obj, EdgeApi):
        """  更新用户. """
        user = None
        resp = EdgeApi.AgentUserService_UpdateUserPutApi(user=user)
        assert resp.status_code == 200

    def test_api_AgentUserService_IsInitialized(self, config_obj, EdgeApi):
        """  用户是否初始化(admin账户是否首次登录). """
        resp = EdgeApi.AgentUserService_IsInitializedGetApi()
        assert resp.status_code == 200

    def test_api_AgentUserService_UserLogin(self, config_obj, EdgeApi):
        """  用户登录, 当返回错误码为11时, 表示需要下次登录需要验证码. """
        user_name = None
        password = None
        key = None
        captcha = None
        resp = EdgeApi.AgentUserService_UserLoginPostApi(user_name=user_name, password=password, key=key, captcha=captcha)
        assert resp.status_code == 200

    def test_api_AgentUserService_UserLogout(self, config_obj, EdgeApi):
        """  用户注销. """
        token = None
        resp = EdgeApi.AgentUserService_UserLogoutPostApi(token=token)
        assert resp.status_code == 200

    def test_api_AgentUserService_GetUser(self, config_obj, EdgeApi):
        """  查询用户信息 """
        id = None
        decrypt = None
        resp = EdgeApi.AgentUserService_GetUserGetApi(id, decrypt=decrypt)
        assert resp.status_code == 200

    def test_api_AgentUserService_DeleteUser(self, config_obj, EdgeApi):
        """  删除用户. """
        id = None
        resp = EdgeApi.AgentUserService_DeleteUserDeleteApi(id)
        assert resp.status_code == 200

    def test_api_AgentUserService_UpdateUserApiSecret(self, config_obj, EdgeApi):
        """  重新生成用户ApiSecret """
        id = None
        resp = EdgeApi.AgentUserService_UpdateUserApiSecretPostApi(id)
        assert resp.status_code == 200

    def test_api_NebulaVDDAgentSrv_DownloadLiveShot(self, config_obj, EdgeApi):
        """  获取实时背景大图. """
        RTSP = None
        resp = EdgeApi.NebulaVDDAgentSrv_DownloadLiveShotPostApi(RTSP=RTSP)
        assert resp.status_code == 200

    def test_api_NebulaVDDAgentSrv_DownloadReplayShot(self, config_obj, EdgeApi):
        """  批量下载回放图片. """
        source_type = None
        source = None
        timestamp = None
        resp = EdgeApi.NebulaVDDAgentSrv_DownloadReplayShotPostApi(source_type=source_type, source=source, timestamp=timestamp)
        assert resp.status_code == 200

    def test_api_NebulaVDDAgentSrv_DownloadReplayVideo(self, config_obj, EdgeApi):
        """  批量下载回放短视频. """
        source_type = None
        source = None
        timestamp = None
        before = None
        after = None
        resp = EdgeApi.NebulaVDDAgentSrv_DownloadReplayVideoPostApi(source_type=source_type, source=source, timestamp=timestamp, before=before, after=after)
        assert resp.status_code == 200

    def test_api_BatchCompareFeature(self, config_obj, EdgeApi):
        """  人脸特征1:1比对 [SINCE v3.1.0].
[EN] One to one Identity... """
        requests = None
        resp = EdgeApi.BatchCompareFeaturePostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_BatchDetect(self, config_obj, EdgeApi):
        """  对批量的图片中的人脸进行检测(只输出检测框和关键点坐标, 不输出特征和属性).
[EN] Detec... """
        requests = None
        detect_mode = None
        face_type = None
        resp = EdgeApi.BatchDetectPostApi(requests=requests, detect_mode=detect_mode, face_type=face_type)
        assert resp.status_code == 200

    def test_api_BatchDetectAndExtractAll2(self, config_obj, EdgeApi):
        """  对批量的图片中的所有人脸进行检测、提特征、提属性. v2.1.0之后用于替代BatchDetectA... """
        requests = None
        detect_mode = None
        face_type = None
        resp = EdgeApi.BatchDetectAndExtractAll2PostApi(requests=requests, detect_mode=detect_mode, face_type=face_type)
        assert resp.status_code == 200

    def test_api_BatchExtractWithBounding(self, config_obj, EdgeApi):
        """  对批量的图片中指定区域的人脸提特征.
[EN] Extract features of Identi... """
        requests = None
        resp = EdgeApi.BatchExtractWithBoundingPostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_CompareFeature(self, config_obj, EdgeApi):
        """  特征1：1比对.
[EN] One to one feature comparison. """
        one = None
        other = None
        resp = EdgeApi.CompareFeaturePostApi(one=one, other=other)
        assert resp.status_code == 200

    def test_api_GetSystemInfo(self, config_obj, EdgeApi):
        """  获取系统信息 [SINCE v2.2.0].
[EN] Get system info which ... """
        resp = EdgeApi.GetSystemInfoGetApi()
        assert resp.status_code == 200
