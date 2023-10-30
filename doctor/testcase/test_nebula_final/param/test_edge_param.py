#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestEdgeParam(object):
    """ edge Param测试"""

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

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AppletManagerSrv_ActivationCodeInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  ActivationCodeInfo 查看当前激活信息. """
        intef = EdgeApi.AppletManagerSrv_ActivationCodeInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('code', 'invalidcode'),
        ('code', ''),
        ('code', None),
    ])
    def test_api_AppletManagerSrv_ActivationCodeUpsertInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  upsert activation code，导入或更新当前全量激活码. """
        code = None
        intef = EdgeApi.AppletManagerSrv_ActivationCodeUpsertPostApi(code=code, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AppletManagerSrv_ListAppletInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  list所有applet信息，包括算力、验签、激活信息. """
        intef = EdgeApi.AppletManagerSrv_ListAppletGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('content', 'invalidcontent'),
        ('content', ''),
        ('content', None),
        ('path', 'invalidpath'),
        ('path', ''),
        ('path', None),
        ('resource_quota', 'invalidresource_quota'),
        ('resource_quota', ''),
        ('resource_quota', None),
        ('kestrel_version', 'invalidkestrel_version'),
        ('kestrel_version', ''),
        ('kestrel_version', None),
    ])
    def test_api_AppletManagerSrv_AppletImportInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  导入一个applet，解析出其中的applet包中的meta信息，并进行验签工作，当有相关的任务存在... """
        content = None
        path = None
        resource_quota = None
        kestrel_version = None
        intef = EdgeApi.AppletManagerSrv_AppletImportPostApi(content=content, path=path, resource_quota=resource_quota, kestrel_version=kestrel_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('runningApplet', 'invalidrunningApplet'),
        ('runningApplet', ''),
        ('runningApplet', None),
    ])
    def test_api_AppletManagerSrv_AppletGCInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  [internal] gc applet，每个applet仅保留最新的3个版本. """
        runningApplet = None
        intef = EdgeApi.AppletManagerSrv_AppletGCPostApi(runningApplet=runningApplet, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AppletManagerSrv_AppletDeleteInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除一个applet，有worker正在运行的applet不能删除. """
        name = None
        version = None
        intef = EdgeApi.AppletManagerSrv_AppletDeleteDeleteApi(name, version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('version', 'invalidversion'),
        ('version', ''),
        ('version', None),
        ('resource_quota', 'invalidresource_quota'),
        ('resource_quota', ''),
        ('resource_quota', None),
        ('kestrel_version', 'invalidkestrel_version'),
        ('kestrel_version', ''),
        ('kestrel_version', None),
    ])
    def test_api_AppletManagerSrv_AppletUpdateInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  更新applet meta信息，如quota, kestrel_version等，当有相关的任务存在... """
        name = None
        version = None
        resource_quota = None
        kestrel_version = None
        intef = EdgeApi.AppletManagerSrv_AppletUpdatePutApi(name, version, resource_quota=resource_quota, kestrel_version=kestrel_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppManagerSrv_ListBizAppInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  list 所有通过bizapp-manager导入的BizApp """
        intef = EdgeApi.BizAppManagerSrv_ListBizAppGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppManagerSrv_BizAppDeleteInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除bizApp: 删除bizapp表数据, 删除applet_meta表数据, 删除bizapp-... """
        intef = EdgeApi.BizAppManagerSrv_BizAppDeleteDeleteApi(sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('content', 'invalidcontent'),
        ('content', ''),
        ('content', None),
        ('path', 'invalidpath'),
        ('path', ''),
        ('path', None),
    ])
    def test_api_BizAppManagerSrv_BizAppImportInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  导入一个BizApp: 解析BizApp包中的meta信息并启动服务 """
        content = None
        path = None
        intef = EdgeApi.BizAppManagerSrv_BizAppImportPostApi(content=content, path=path, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('version', 'invalidversion'),
        ('version', ''),
        ('version', None),
    ])
    def test_api_BizAppManagerSrv_BizAppStartInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  启动bizapp服务 """
        name = None
        version = None
        intef = EdgeApi.BizAppManagerSrv_BizAppStartPostApi(name=name, version=version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('version', 'invalidversion'),
        ('version', ''),
        ('version', None),
    ])
    def test_api_BizAppManagerSrv_BizAppStopInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  停止bizapp: 停止服务, 停止bizapp-task任务 """
        name = None
        version = None
        intef = EdgeApi.BizAppManagerSrv_BizAppStopPostApi(name=name, version=version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('object_requests', 'invalidobject_requests'),
        ('object_requests', ''),
        ('object_requests', None),
    ])
    def test_api_CallbackAgent_BatchPutObjectInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  图像推送接口 """
        object_requests = None
        intef = EdgeApi.CallbackAgent_BatchPutObjectPostApi(object_requests=object_requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_CallbackAgent_ListCallbackConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询callback配置列表. """
        intef = EdgeApi.CallbackAgent_ListCallbackConfigGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
    ])
    def test_api_CallbackAgent_AddCallbackConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  增加callback配置项. """
        config = None
        intef = EdgeApi.CallbackAgent_AddCallbackConfigPostApi(config=config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
    ])
    def test_api_CallbackAgent_UpdateCallbackConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  更新callback配置项. """
        config = None
        intef = EdgeApi.CallbackAgent_UpdateCallbackConfigPutApi(config=config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_CallbackAgent_GetCallbackConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询callback的配置. """
        id = None
        intef = EdgeApi.CallbackAgent_GetCallbackConfigGetApi(id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_CallbackAgent_DeleteCallbackConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除callback配置项. """
        id = None
        intef = EdgeApi.CallbackAgent_DeleteCallbackConfigDeleteApi(id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('viid_id', 'invalidviid_id'),
        ('viid_id', ''),
        ('viid_id', None),
        ('viid_param', 'invalidviid_param'),
        ('viid_param', ''),
        ('viid_param', None),
        ('extra_infos', 'invalidextra_infos'),
        ('extra_infos', ''),
        ('extra_infos', None),
    ])
    def test_api_CallbackAgent_VIIDNewInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  创建视图库 """
        viid_id = None
        viid_param = None
        extra_infos = None
        intef = EdgeApi.CallbackAgent_VIIDNewPostApi(viid_id=viid_id, viid_param=viid_param, extra_infos=extra_infos, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_CallbackAgent_VIIDInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查看视图库信息 """
        viid_id = None
        intef = EdgeApi.CallbackAgent_VIIDInfoGetApi(viid_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_CallbackAgent_VIIDDeleteInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除视图库 """
        viid_id = None
        intef = EdgeApi.CallbackAgent_VIIDDeleteDeleteApi(viid_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('content_type', 'invalidcontent_type'),
        ('content_type', ''),
        ('content_type', None),
        ('portrait_db_add', 'invalidportrait_db_add'),
        ('portrait_db_add', ''),
        ('portrait_db_add', None),
        ('portrait_db_delete', 'invalidportrait_db_delete'),
        ('portrait_db_delete', ''),
        ('portrait_db_delete', None),
        ('portrait_db_update', 'invalidportrait_db_update'),
        ('portrait_db_update', ''),
        ('portrait_db_update', None),
        ('portrait_add', 'invalidportrait_add'),
        ('portrait_add', ''),
        ('portrait_add', None),
        ('portrait_delete', 'invalidportrait_delete'),
        ('portrait_delete', ''),
        ('portrait_delete', None),
        ('portrait_update', 'invalidportrait_update'),
        ('portrait_update', ''),
        ('portrait_update', None),
    ])
    def test_api_NebulaDbSyncCallbackAgent_EventCallbackInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  业务方实现，用来接收 nebula-db-sync-agent """
        content_type = None
        portrait_db_add = None
        portrait_db_delete = None
        portrait_db_update = None
        portrait_add = None
        portrait_delete = None
        portrait_update = None
        intef = EdgeApi.NebulaDbSyncCallbackAgent_EventCallbackPostApi(content_type=content_type, portrait_db_add=portrait_db_add, portrait_db_delete=portrait_db_delete, portrait_db_update=portrait_db_update, portrait_add=portrait_add, portrait_delete=portrait_delete, portrait_update=portrait_update, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetRealTimeBGIMGInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetRealTimeBGIMG 获取实时背景大图... """
        camera_id = None
        intef = EdgeApi.NebulaIOTAgentSrv_GetRealTimeBGIMGGetApi(camera_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetDefaultNicInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取默认网卡 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetDefaultNicGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_SetDefaultNicByNameInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  设置网卡为默认网卡 """
        name = None
        intef = EdgeApi.NebulaIOTAgentSrv_SetDefaultNicByNamePostApi(name, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetDeviceDisksInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetDeviceDisksInfo 获取设备磁盘信息 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetDeviceDisksInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetDNSConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetDNSConfig 获取 DNS 配置信息 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetDNSConfigGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('dns', 'invaliddns'),
        ('dns', ''),
        ('dns', None),
    ])
    def test_api_NebulaIOTAgentSrv_SetDNSConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  SetDNSConfig 设置 DNS """
        dns = None
        intef = EdgeApi.NebulaIOTAgentSrv_SetDNSConfigPostApi(dns=dns, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetIPConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetIPConfig 获取 IP 配置信息 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetIPConfigGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ip', 'invalidip'),
        ('ip', ''),
        ('ip', None),
    ])
    def test_api_NebulaIOTAgentSrv_SetIPConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  SetIPConfig 设置 IP (Pallas平台, 不支持interface alias配置) """
        ip = None
        intef = EdgeApi.NebulaIOTAgentSrv_SetIPConfigPostApi(ip=ip, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetModemAPNInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetModemAPN 获取4G插卡状态，运营商信息，IMSI,信号强度,APN名称，用户名，密码 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetModemAPNGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_CloseModemAPNInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  关闭4G功能 """
        intef = EdgeApi.NebulaIOTAgentSrv_CloseModemAPNDeleteApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('apn', 'invalidapn'),
        ('apn', ''),
        ('apn', None),
    ])
    def test_api_NebulaIOTAgentSrv_OpenModemAPNInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  开启4G功能，4G卡未插卡时，4G功能不可开启 """
        apn = None
        intef = EdgeApi.NebulaIOTAgentSrv_OpenModemAPNPostApi(apn=apn, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetNTPConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetNTPConfig 获取 NTP 配置信息 (Pallas平台, port参数设置为"123"... """
        intef = EdgeApi.NebulaIOTAgentSrv_GetNTPConfigGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ntp', 'invalidntp'),
        ('ntp', ''),
        ('ntp', None),
    ])
    def test_api_NebulaIOTAgentSrv_SetNTPConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  SetNTPConfig 设置 NTP (Pallas平台，port参数只能是"123"或者"") """
        ntp = None
        intef = EdgeApi.NebulaIOTAgentSrv_SetNTPConfigPostApi(ntp=ntp, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('address', 'invalidaddress'),
        ('address', ''),
        ('address', None),
    ])
    def test_api_NebulaIOTAgentSrv_PingInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  Ping ping 指定地址，用于测试网络情况 """
        address = None
        intef = EdgeApi.NebulaIOTAgentSrv_PingPostApi(address=address, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetRegisterStateInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取设备注册信息 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetRegisterStateGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetROUTEConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetROUTEConfig 获取 路由表 配置信息 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetROUTEConfigGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('route', 'invalidroute'),
        ('route', ''),
        ('route', None),
    ])
    def test_api_NebulaIOTAgentSrv_SetROUTEConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  SetROUTEConfig 设置 路由表 """
        route = None
        intef = EdgeApi.NebulaIOTAgentSrv_SetROUTEConfigPostApi(route=route, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetSerialNumberInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetSerialNumber 获取设备序列号 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetSerialNumberGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetTIMEConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetTIMEConfig 获取 系统时间 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetTIMEConfigGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('time', 'invalidtime'),
        ('time', ''),
        ('time', None),
    ])
    def test_api_NebulaIOTAgentSrv_SetTIMEConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  SetTIMEConfig 设置 系统时间 """
        time = None
        intef = EdgeApi.NebulaIOTAgentSrv_SetTIMEConfigPostApi(time=time, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetRegisterUserMetaInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetRegisterUserMeta 获取用户自注册信息 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetRegisterUserMetaGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_meta', 'invaliduser_meta'),
        ('user_meta', ''),
        ('user_meta', None),
    ])
    def test_api_NebulaIOTAgentSrv_SetRegisterUserMetaInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  SetRegisterUserMeta 设置用户自注册信息 """
        user_meta = None
        intef = EdgeApi.NebulaIOTAgentSrv_SetRegisterUserMetaPostApi(user_meta=user_meta, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetVersionInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetVersionInfo 获取序列号SN，Pallas固件版本ROM(t4不提供)，Viperl... """
        intef = EdgeApi.NebulaIOTAgentSrv_GetVersionInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetLicenseStateInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetLicenseState 获取 license 信息 """
        intef = EdgeApi.NebulaIOTAgentSrv_GetLicenseStateGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_SetLicenseInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  SetLicense 设置 license 信息(详情参考注释)
Use POST http met... """
        intef = EdgeApi.NebulaIOTAgentSrv_SetLicensePostApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('subdevice', 'invalidsubdevice'),
        ('subdevice', ''),
        ('subdevice', None),
        ('skip', 'invalidskip'),
        ('skip', ''),
        ('skip', None),
    ])
    def test_api_NebulaIOTAgentSrv_UpsertSubDeviceInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  UpsertSubDevice 更新/添加子设备, device_id不存在时添加，存在时更新。
该... """
        subdevice = None
        skip = None
        intef = EdgeApi.NebulaIOTAgentSrv_UpsertSubDevicePostApi(subdevice=subdevice, skip=skip, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    # learn_6 边界值测试
    @pytest.mark.parametrize("invalidParam", [
        ('subdevice.brand', 'invalidBrand'),
        ('subdevice.brand', ''),
        ('subdevice.brand', None),
        ('subdevice.device_id', ''),
        ('subdevice.device_id', None),
    ])
    def test_api_NebulaIOTAgentSrv_UpsertSubDeviceInvalidParamDemo(self, invalidParam, config_obj, EdgeApi, client_info, camera_info):
        """  UpsertSubDevice 参数测试例子"""
        # 第一步: 构造正常可以通过的接口参数
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
            "device_id": device_id,
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
        # 第二步: 获取接口对象,传入sendRequest=False,使接口不自动调用
        intef = EdgeApi.NebulaIOTAgentSrv_UpsertSubDevicePostApi(subdevice=subdevice, skip=None, sendRequest=False)
        # 第三步: 更新需要验证的参数, 准则是一次只验证一个参数
        # get, delete 只需要验证param,使用intef.update_params(invalidParam[0], invalidParam[1]) 更新
        # post put, 只需要验证body, 使用intef.update_body(invalidParam[0], invalidParam[1]) 更新
        # 如果对某个参数有特殊要求, 使用如下方法, 进行定制修改
        # if invalidParam[0] == 'subdevice.brand':
        #     intef.update_body(invalidParam[0], invalidParam[1])
        intef.update_body(invalidParam[0], invalidParam[1])
        # 第四步: 调接口,发送请求
        resp = intef.request()
        # 第五步: 验证返回值
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_ListAllSubDevicesInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  ListAllSubDevices 获取所有子设备信息 """
        intef = EdgeApi.NebulaIOTAgentSrv_ListAllSubDevicesGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('sub_filter_device_id', 'invalidsub_filter_device_id'),
        ('sub_filter_device_id', ''),
        ('sub_filter_device_id', None),
        ('sub_filter_name', 'invalidsub_filter_name'),
        ('sub_filter_name', ''),
        ('sub_filter_name', None),
        ('sub_filter_address', 'invalidsub_filter_address'),
        ('sub_filter_address', ''),
        ('sub_filter_address', None),
        ('sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url', 'invalidsub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url'),
        ('sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url', ''),
        ('sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url', None),
    ])
    def test_api_NebulaIOTAgentSrv_GetSubDeviceByFilterInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetSubDeviceByFilter 根据 ID, name, IP, rtsp_url 获取子... """
        sub_filter_device_id = None
        sub_filter_name = None
        sub_filter_address = None
        sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url = None
        intef = EdgeApi.NebulaIOTAgentSrv_GetSubDeviceByFilterGetApi(sub_filter_device_id=sub_filter_device_id, sub_filter_name=sub_filter_name, sub_filter_address=sub_filter_address, sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url=sub_filter_extra_config_camera_config_video_source_config_rtsp_parameter_parameter_url, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetSubDeviceStreamsByIDInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """   """
        id = None
        intef = EdgeApi.NebulaIOTAgentSrv_GetSubDeviceStreamsByIDGetApi(id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTAgentSrv_GetSubDeviceByIDInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  GetSubDeviceByID 根据 ID 获取子设备信息 """
        id = None
        intef = EdgeApi.NebulaIOTAgentSrv_GetSubDeviceByIDGetApi(id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('skip', 'invalidskip'),
        ('skip', ''),
        ('skip', None),
    ])
    def test_api_NebulaIOTAgentSrv_RemoveSubDeviceByIDInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  RemoveSubDeviceByID 根据 ID 删除子设备 """
        id = None
        skip = None
        intef = EdgeApi.NebulaIOTAgentSrv_RemoveSubDeviceByIDDeleteApi(id, skip=skip, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bizapp', 'invalidbizapp'),
        ('bizapp', ''),
        ('bizapp', None),
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
    ])
    def test_api_NebulaKongGatewaySrv_ImportKongConfigByBizappInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  上传bizapp kong gateway配置文件 """
        bizapp = None
        config = None
        intef = EdgeApi.NebulaKongGatewaySrv_ImportKongConfigByBizappPostApi(bizapp=bizapp, config=config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaKongGatewaySrv_GetPluginApiAuthWhiteUrlsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取nebula-api-auth.white_urls """
        intef = EdgeApi.NebulaKongGatewaySrv_GetPluginApiAuthWhiteUrlsGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('url_path', 'invalidurl_path'),
        ('url_path', ''),
        ('url_path', None),
        ('url_method', 'invalidurl_method'),
        ('url_method', ''),
        ('url_method', None),
    ])
    def test_api_NebulaKongGatewaySrv_DelPluginApiAuthWhiteUrlsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除nebula-api-auth.white_urls """
        url_path = None
        url_method = None
        intef = EdgeApi.NebulaKongGatewaySrv_DelPluginApiAuthWhiteUrlsDeleteApi(url_path=url_path, url_method=url_method, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('url', 'invalidurl'),
        ('url', ''),
        ('url', None),
    ])
    def test_api_NebulaKongGatewaySrv_AddPluginApiAuthWhiteUrlsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  增加nebula-api-auth.white_urls """
        url = None
        intef = EdgeApi.NebulaKongGatewaySrv_AddPluginApiAuthWhiteUrlsPostApi(url=url, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaKongGatewaySrv_GetPluginJwtWhiteUrlsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取nebula-jwt.white_urls """
        intef = EdgeApi.NebulaKongGatewaySrv_GetPluginJwtWhiteUrlsGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('url_path', 'invalidurl_path'),
        ('url_path', ''),
        ('url_path', None),
        ('url_method', 'invalidurl_method'),
        ('url_method', ''),
        ('url_method', None),
    ])
    def test_api_NebulaKongGatewaySrv_DelPluginJwtWhiteUrlsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除nebula-jwt.white_urls """
        url_path = None
        url_method = None
        intef = EdgeApi.NebulaKongGatewaySrv_DelPluginJwtWhiteUrlsDeleteApi(url_path=url_path, url_method=url_method, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('url', 'invalidurl'),
        ('url', ''),
        ('url', None),
    ])
    def test_api_NebulaKongGatewaySrv_AddPluginJwtWhiteUrlsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  增加nebula-jwt.white_urls """
        url = None
        intef = EdgeApi.NebulaKongGatewaySrv_AddPluginJwtWhiteUrlsPostApi(url=url, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaKongGatewaySrv_GetKongConfigByBizappInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取bizapp kong gateway配置文件 """
        bizapp = None
        intef = EdgeApi.NebulaKongGatewaySrv_GetKongConfigByBizappGetApi(bizapp, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaKongGatewaySrv_RemoveKongConfigByBizappInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除bizapp kong gateway配置文件 """
        bizapp = None
        intef = EdgeApi.NebulaKongGatewaySrv_RemoveKongConfigByBizappDeleteApi(bizapp, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_BizAppTaskDefaultService_BatchCreateTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  创建任务 """
        requests = None
        intef = EdgeApi.BizAppTaskDefaultService_BatchCreateTaskPostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ids', 'invalidids'),
        ('ids', ''),
        ('ids', None),
    ])
    def test_api_BizAppTaskDefaultService_DeleteRecordInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除记录 """
        ids = None
        intef = EdgeApi.BizAppTaskDefaultService_DeleteRecordPostApi(ids=ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('start_time', 'invalidstart_time'),
        ('start_time', ''),
        ('start_time', None),
        ('end_time', 'invalidend_time'),
        ('end_time', ''),
        ('end_time', None),
        ('sub_device_name', 'invalidsub_device_name'),
        ('sub_device_name', ''),
        ('sub_device_name', None),
        ('sub_device_id', 'invalidsub_device_id'),
        ('sub_device_id', ''),
        ('sub_device_id', None),
        ('task_name', 'invalidtask_name'),
        ('task_name', ''),
        ('task_name', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
        ('task_type', 'invalidtask_type'),
        ('task_type', ''),
        ('task_type', None),
        ('applet_record_type', 'invalidapplet_record_type'),
        ('applet_record_type', ''),
        ('applet_record_type', None),
        ('lib_type', 'invalidlib_type'),
        ('lib_type', ''),
        ('lib_type', None),
        ('portrait_id', 'invalidportrait_id'),
        ('portrait_id', ''),
        ('portrait_id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('attributes', 'invalidattributes'),
        ('attributes', ''),
        ('attributes', None),
    ])
    def test_api_BizAppTaskDefaultService_ExportRecordInvalidParam(self, invalidParam, config_obj, EdgeApi):
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
        intef = EdgeApi.BizAppTaskDefaultService_ExportRecordPostApi(start_time=start_time, end_time=end_time, sub_device_name=sub_device_name, sub_device_id=sub_device_id, task_name=task_name, task_id=task_id, task_type=task_type, applet_record_type=applet_record_type, lib_type=lib_type, portrait_id=portrait_id, name=name, page=page, attributes=attributes, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('start_time', 'invalidstart_time'),
        ('start_time', ''),
        ('start_time', None),
        ('end_time', 'invalidend_time'),
        ('end_time', ''),
        ('end_time', None),
        ('sub_device_name', 'invalidsub_device_name'),
        ('sub_device_name', ''),
        ('sub_device_name', None),
        ('sub_device_id', 'invalidsub_device_id'),
        ('sub_device_id', ''),
        ('sub_device_id', None),
        ('task_name', 'invalidtask_name'),
        ('task_name', ''),
        ('task_name', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
        ('task_type', 'invalidtask_type'),
        ('task_type', ''),
        ('task_type', None),
        ('applet_record_type', 'invalidapplet_record_type'),
        ('applet_record_type', ''),
        ('applet_record_type', None),
        ('lib_type', 'invalidlib_type'),
        ('lib_type', ''),
        ('lib_type', None),
        ('portrait_id', 'invalidportrait_id'),
        ('portrait_id', ''),
        ('portrait_id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('attributes', 'invalidattributes'),
        ('attributes', ''),
        ('attributes', None),
    ])
    def test_api_BizAppTaskDefaultService_QueryRecordInvalidParam(self, invalidParam, config_obj, EdgeApi):
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
        intef = EdgeApi.BizAppTaskDefaultService_QueryRecordPostApi(start_time=start_time, end_time=end_time, sub_device_name=sub_device_name, sub_device_id=sub_device_id, task_name=task_name, task_id=task_id, task_type=task_type, applet_record_type=applet_record_type, lib_type=lib_type, portrait_id=portrait_id, name=name, page=page, attributes=attributes, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('field', 'invalidfield'),
        ('field', ''),
        ('field', None),
        ('ids', 'invalidids'),
        ('ids', ''),
        ('ids', None),
    ])
    def test_api_BizAppTaskDefaultService_UpdateRecordInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  更新记录 """
        field = None
        ids = None
        intef = EdgeApi.BizAppTaskDefaultService_UpdateRecordPostApi(field=field, ids=ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppTaskDefaultService_DeleteTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除任务 """
        intef = EdgeApi.BizAppTaskDefaultService_DeleteTaskDeleteApi(sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('task_type', 'invalidtask_type'),
        ('task_type', ''),
        ('task_type', None),
        ('desc', 'invaliddesc'),
        ('desc', ''),
        ('desc', None),
        ('detect_type', 'invaliddetect_type'),
        ('detect_type', ''),
        ('detect_type', None),
        ('active', 'invalidactive'),
        ('active', ''),
        ('active', None),
        ('sub_device_ids', 'invalidsub_device_ids'),
        ('sub_device_ids', ''),
        ('sub_device_ids', None),
        ('object_config', 'invalidobject_config'),
        ('object_config', ''),
        ('object_config', None),
        ('extend_config', 'invalidextend_config'),
        ('extend_config', ''),
        ('extend_config', None),
        ('schedule', 'invalidschedule'),
        ('schedule', ''),
        ('schedule', None),
        ('identifier_id', 'invalididentifier_id'),
        ('identifier_id', ''),
        ('identifier_id', None),
        ('stream_type', 'invalidstream_type'),
        ('stream_type', ''),
        ('stream_type', None),
        ('not_support_merge', 'invalidnot_support_merge'),
        ('not_support_merge', ''),
        ('not_support_merge', None),
        ('dbs', 'invaliddbs'),
        ('dbs', ''),
        ('dbs', None),
    ])
    def test_api_BizAppTaskDefaultService_CreateTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
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
        intef = EdgeApi.BizAppTaskDefaultService_CreateTaskPostApi(name=name, task_type=task_type, desc=desc, detect_type=detect_type, active=active, sub_device_ids=sub_device_ids, object_config=object_config, extend_config=extend_config, schedule=schedule, identifier_id=identifier_id, stream_type=stream_type, not_support_merge=not_support_merge, dbs=dbs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('desc', 'invaliddesc'),
        ('desc', ''),
        ('desc', None),
        ('object_config', 'invalidobject_config'),
        ('object_config', ''),
        ('object_config', None),
        ('extend_config', 'invalidextend_config'),
        ('extend_config', ''),
        ('extend_config', None),
        ('schedule', 'invalidschedule'),
        ('schedule', ''),
        ('schedule', None),
        ('dbs', 'invaliddbs'),
        ('dbs', ''),
        ('dbs', None),
    ])
    def test_api_BizAppTaskDefaultService_UpdateTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  修改任务 """
        task_ids = None
        name = None
        desc = None
        object_config = None
        extend_config = None
        schedule = None
        dbs = None
        intef = EdgeApi.BizAppTaskDefaultService_UpdateTaskPutApi(task_ids=task_ids, name=name, desc=desc, object_config=object_config, extend_config=extend_config, schedule=schedule, dbs=dbs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('active', 'invalidactive'),
        ('active', ''),
        ('active', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('task_types', 'invalidtask_types'),
        ('task_types', ''),
        ('task_types', None),
    ])
    def test_api_BizAppTaskDefaultService_QueryAllTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询所有任务(无分页)，使用场景：任务的下拉框查询 """
        active = None
        db_id = None
        task_types = None
        intef = EdgeApi.BizAppTaskDefaultService_QueryAllTaskPostApi(active=active, db_id=db_id, task_types=task_types, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
    ])
    def test_api_BizAppTaskDefaultService_DisableTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  禁用任务 """
        task_ids = None
        intef = EdgeApi.BizAppTaskDefaultService_DisableTaskPutApi(task_ids=task_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
    ])
    def test_api_BizAppTaskDefaultService_EnableTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  启用任务 """
        task_ids = None
        intef = EdgeApi.BizAppTaskDefaultService_EnableTaskPutApi(task_ids=task_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_num', 'invalidpage_num'),
        ('page_num', ''),
        ('page_num', None),
        ('page_size', 'invalidpage_size'),
        ('page_size', ''),
        ('page_size', None),
        ('keyword', 'invalidkeyword'),
        ('keyword', ''),
        ('keyword', None),
        ('sub_device_ids', 'invalidsub_device_ids'),
        ('sub_device_ids', ''),
        ('sub_device_ids', None),
    ])
    def test_api_BizAppTaskDefaultService_QueryTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询任务(有分页)，正常的分页查询 """
        page_num = None
        page_size = None
        keyword = None
        sub_device_ids = None
        intef = EdgeApi.BizAppTaskDefaultService_QueryTaskPostApi(page_num=page_num, page_size=page_size, keyword=keyword, sub_device_ids=sub_device_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppTaskDefaultService_DetailTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  详情任务 """
        task_id = None
        intef = EdgeApi.BizAppTaskDefaultService_DetailTaskGetApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppTaskService_DeleteTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除任务 """
        intef = EdgeApi.BizAppTaskService_DeleteTaskDeleteApi(sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('task_type', 'invalidtask_type'),
        ('task_type', ''),
        ('task_type', None),
        ('desc', 'invaliddesc'),
        ('desc', ''),
        ('desc', None),
        ('detect_type', 'invaliddetect_type'),
        ('detect_type', ''),
        ('detect_type', None),
        ('active', 'invalidactive'),
        ('active', ''),
        ('active', None),
        ('sub_device_ids', 'invalidsub_device_ids'),
        ('sub_device_ids', ''),
        ('sub_device_ids', None),
        ('object_config', 'invalidobject_config'),
        ('object_config', ''),
        ('object_config', None),
        ('extend_config', 'invalidextend_config'),
        ('extend_config', ''),
        ('extend_config', None),
        ('schedule', 'invalidschedule'),
        ('schedule', ''),
        ('schedule', None),
        ('identifier_id', 'invalididentifier_id'),
        ('identifier_id', ''),
        ('identifier_id', None),
        ('stream_type', 'invalidstream_type'),
        ('stream_type', ''),
        ('stream_type', None),
        ('not_support_merge', 'invalidnot_support_merge'),
        ('not_support_merge', ''),
        ('not_support_merge', None),
        ('dbs', 'invaliddbs'),
        ('dbs', ''),
        ('dbs', None),
    ])
    def test_api_BizAppTaskService_CreateTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
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
        intef = EdgeApi.BizAppTaskService_CreateTaskPostApi(name=name, task_type=task_type, desc=desc, detect_type=detect_type, active=active, sub_device_ids=sub_device_ids, object_config=object_config, extend_config=extend_config, schedule=schedule, identifier_id=identifier_id, stream_type=stream_type, not_support_merge=not_support_merge, dbs=dbs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('desc', 'invaliddesc'),
        ('desc', ''),
        ('desc', None),
        ('object_config', 'invalidobject_config'),
        ('object_config', ''),
        ('object_config', None),
        ('extend_config', 'invalidextend_config'),
        ('extend_config', ''),
        ('extend_config', None),
        ('schedule', 'invalidschedule'),
        ('schedule', ''),
        ('schedule', None),
        ('dbs', 'invaliddbs'),
        ('dbs', ''),
        ('dbs', None),
    ])
    def test_api_BizAppTaskService_UpdateTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  修改任务 """
        task_ids = None
        name = None
        desc = None
        object_config = None
        extend_config = None
        schedule = None
        dbs = None
        intef = EdgeApi.BizAppTaskService_UpdateTaskPutApi(task_ids=task_ids, name=name, desc=desc, object_config=object_config, extend_config=extend_config, schedule=schedule, dbs=dbs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('active', 'invalidactive'),
        ('active', ''),
        ('active', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('task_types', 'invalidtask_types'),
        ('task_types', ''),
        ('task_types', None),
    ])
    def test_api_BizAppTaskService_QueryAllTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询所有任务(无分页)，使用场景：任务的下拉框查询 """
        active = None
        db_id = None
        task_types = None
        intef = EdgeApi.BizAppTaskService_QueryAllTaskPostApi(active=active, db_id=db_id, task_types=task_types, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
    ])
    def test_api_BizAppTaskService_DisableTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  禁用任务 """
        task_ids = None
        intef = EdgeApi.BizAppTaskService_DisableTaskPutApi(task_ids=task_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
    ])
    def test_api_BizAppTaskService_EnableTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  启用任务 """
        task_ids = None
        intef = EdgeApi.BizAppTaskService_EnableTaskPutApi(task_ids=task_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppTaskService_LicenseStatisticsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  License授权信息 """
        intef = EdgeApi.BizAppTaskService_LicenseStatisticsGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppTaskService_PowerInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取算力信息 """
        intef = EdgeApi.BizAppTaskService_PowerInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_num', 'invalidpage_num'),
        ('page_num', ''),
        ('page_num', None),
        ('page_size', 'invalidpage_size'),
        ('page_size', ''),
        ('page_size', None),
        ('keyword', 'invalidkeyword'),
        ('keyword', ''),
        ('keyword', None),
        ('sub_device_ids', 'invalidsub_device_ids'),
        ('sub_device_ids', ''),
        ('sub_device_ids', None),
    ])
    def test_api_BizAppTaskService_QueryTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询任务(有分页)，正常的分页查询 """
        page_num = None
        page_size = None
        keyword = None
        sub_device_ids = None
        intef = EdgeApi.BizAppTaskService_QueryTaskPostApi(page_num=page_num, page_size=page_size, keyword=keyword, sub_device_ids=sub_device_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppTaskService_DetailTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  详情任务 """
        task_id = None
        intef = EdgeApi.BizAppTaskService_DetailTaskGetApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ScheduleService_GetStorageInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取当前抓拍图片存储空间信息 """
        intef = EdgeApi.ScheduleService_GetStorageInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ScheduleService_ClearRecordInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """   """
        intef = EdgeApi.ScheduleService_ClearRecordDeleteApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_ScheduleService_GetSystemInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取一些系统配置信息 """
        intef = EdgeApi.ScheduleService_GetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('save_days', 'invalidsave_days'),
        ('save_days', ''),
        ('save_days', None),
    ])
    def test_api_ScheduleService_SetSystemInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  设置一些系统配置信息 """
        save_days = None
        intef = EdgeApi.ScheduleService_SetSystemInfoPostApi(save_days=save_days, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
    ])
    def test_api_TaskManagerSrv_BatchGetTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  批量获取任务 """
        task_ids = None
        intef = EdgeApi.TaskManagerSrv_BatchGetTaskGetApi(task_ids=task_ids, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
    ])
    def test_api_TaskManagerSrv_BatchDeleteTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  批量删除任务 """
        task_ids = None
        intef = EdgeApi.TaskManagerSrv_BatchDeleteTaskDeleteApi(task_ids=task_ids, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_TaskManagerSrv_BatchCreateTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  批量创建任务 """
        requests = None
        intef = EdgeApi.TaskManagerSrv_BatchCreateTaskPostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_TaskManagerSrv_BatchUpdateTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  批量更新任务 """
        requests = None
        intef = EdgeApi.TaskManagerSrv_BatchUpdateTaskPutApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_TaskManagerSrv_HelloInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  Hello . """
        intef = EdgeApi.TaskManagerSrv_HelloGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_TaskManagerSrv_GetPowerInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询算力信息 """
        intef = EdgeApi.TaskManagerSrv_GetPowerInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_TaskManagerSrv_ListTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取任务列表 """
        intef = EdgeApi.TaskManagerSrv_ListTaskGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task', 'invalidtask'),
        ('task', ''),
        ('task', None),
    ])
    def test_api_TaskManagerSrv_CreateTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  创建任务 """
        task = None
        intef = EdgeApi.TaskManagerSrv_CreateTaskPostApi(task=task, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_TaskManagerSrv_GetTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  根据task_id获取任务 """
        task_id = None
        intef = EdgeApi.TaskManagerSrv_GetTaskGetApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_TaskManagerSrv_DeleteTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  根据task_id删除任务 """
        task_id = None
        intef = EdgeApi.TaskManagerSrv_DeleteTaskDeleteApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
        ('task', 'invalidtask'),
        ('task', ''),
        ('task', None),
    ])
    def test_api_TaskManagerSrv_UpdateTaskInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  更新任务 """
        task_id = None
        task = None
        intef = EdgeApi.TaskManagerSrv_UpdateTaskPutApi(task_id, task=task, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_TaskManagerSrv_GetWorkerInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询worker信息 """
        intef = EdgeApi.TaskManagerSrv_GetWorkerInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('list_applet_only', 'invalidlist_applet_only'),
        ('list_applet_only', ''),
        ('list_applet_only', None),
    ])
    def test_api_OTAEngineService_FirmwareListInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  固件列表 """
        list_applet_only = None
        intef = EdgeApi.OTAEngineService_FirmwareListGetApi(list_applet_only=list_applet_only, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('current_version', 'invalidcurrent_version'),
        ('current_version', ''),
        ('current_version', None),
    ])
    def test_api_OTAEngineService_FirmwareUnregisterInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  固件卸载 """
        name = None
        current_version = None
        intef = EdgeApi.OTAEngineService_FirmwareUnregisterDeleteApi(name=name, current_version=current_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('current_version', 'invalidcurrent_version'),
        ('current_version', ''),
        ('current_version', None),
        ('ext_data', 'invalidext_data'),
        ('ext_data', ''),
        ('ext_data', None),
    ])
    def test_api_OTAEngineService_FirmwareRegisterInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  固件注册 """
        name = None
        current_version = None
        ext_data = None
        intef = EdgeApi.OTAEngineService_FirmwareRegisterPostApi(name=name, current_version=current_version, ext_data=ext_data, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_OTAEngineService_FirmwareUpgradeInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  固件上传并执行安装，不负责升级的原子性，一但由于比如机器重启被打断之后不能恢复。
支持request... """
        intef = EdgeApi.OTAEngineService_FirmwareUpgradePostApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('portrait_infos', 'invalidportrait_infos'),
        ('portrait_infos', ''),
        ('portrait_infos', None),
        ('quality_threshold', 'invalidquality_threshold'),
        ('quality_threshold', ''),
        ('quality_threshold', None),
    ])
    def test_api_Portraits_CreatePortraitsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  创建人像 """
        db_id = None
        portrait_infos = None
        quality_threshold = None
        intef = EdgeApi.Portraits_CreatePortraitsPostApi(db_id=db_id, portrait_infos=portrait_infos, quality_threshold=quality_threshold, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('portrait_infos', 'invalidportrait_infos'),
        ('portrait_infos', ''),
        ('portrait_infos', None),
        ('quality_threshold', 'invalidquality_threshold'),
        ('quality_threshold', ''),
        ('quality_threshold', None),
    ])
    def test_api_Portraits_UpdatePortraitsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  更新人像 """
        db_id = None
        portrait_infos = None
        quality_threshold = None
        intef = EdgeApi.Portraits_UpdatePortraitsPutApi(db_id=db_id, portrait_infos=portrait_infos, quality_threshold=quality_threshold, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('portrait_id', 'invalidportrait_id'),
        ('portrait_id', ''),
        ('portrait_id', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
    ])
    def test_api_Portraits_CompareImageInDBInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  单张图片跟库中指定人像进行1:1比对 """
        db_id = None
        portrait_id = None
        image = None
        intef = EdgeApi.Portraits_CompareImageInDBPostApi(db_id=db_id, portrait_id=portrait_id, image=image, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image_1', 'invalidimage_1'),
        ('image_1', ''),
        ('image_1', None),
        ('image_2', 'invalidimage_2'),
        ('image_2', ''),
        ('image_2', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_Portraits_CompareOneToOneInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  图片1:1比对 """
        image_1 = None
        image_2 = None
        feature_version = None
        intef = EdgeApi.Portraits_CompareOneToOnePostApi(image_1=image_1, image_2=image_2, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_Portraits_GetPortraitsConfigInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取全局配置信息 """
        intef = EdgeApi.Portraits_GetPortraitsConfigGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_Portraits_ListPortraitDbsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询人像库列表 """
        page_offset = None
        page_limit = None
        page_total = None
        intef = EdgeApi.Portraits_ListPortraitDbsGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_name', 'invaliddb_name'),
        ('db_name', ''),
        ('db_name', None),
        ('db_type', 'invaliddb_type'),
        ('db_type', ''),
        ('db_type', None),
        ('db_capacity', 'invaliddb_capacity'),
        ('db_capacity', ''),
        ('db_capacity', None),
        ('operator', 'invalidoperator'),
        ('operator', ''),
        ('operator', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
    ])
    def test_api_Portraits_CreatePortraitDbInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  创建人像库 """
        db_name = None
        db_type = None
        db_capacity = None
        operator = None
        feature_version = None
        description = None
        intef = EdgeApi.Portraits_CreatePortraitDbPostApi(db_name=db_name, db_type=db_type, db_capacity=db_capacity, operator=operator, feature_version=feature_version, description=description, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('unsafe_mode', 'invalidunsafe_mode'),
        ('unsafe_mode', ''),
        ('unsafe_mode', None),
        ('operator', 'invalidoperator'),
        ('operator', ''),
        ('operator', None),
    ])
    def test_api_Portraits_DeletePortraitDbInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除人像库 """
        db_id = None
        unsafe_mode = None
        operator = None
        intef = EdgeApi.Portraits_DeletePortraitDbPostApi(db_id=db_id, unsafe_mode=unsafe_mode, operator=operator, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_ids', 'invaliddb_ids'),
        ('db_ids', ''),
        ('db_ids', None),
    ])
    def test_api_Portraits_QueryPortraitDbsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询人像库集合信息 """
        db_ids = None
        intef = EdgeApi.Portraits_QueryPortraitDbsPostApi(db_ids=db_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('db_name', 'invaliddb_name'),
        ('db_name', ''),
        ('db_name', None),
        ('db_type', 'invaliddb_type'),
        ('db_type', ''),
        ('db_type', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('operator', 'invalidoperator'),
        ('operator', ''),
        ('operator', None),
    ])
    def test_api_Portraits_UpdatePortraitDbInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  更新人像库 """
        db_id = None
        db_name = None
        db_type = None
        description = None
        operator = None
        intef = EdgeApi.Portraits_UpdatePortraitDbPutApi(db_id, db_name=db_name, db_type=db_type, description=description, operator=operator, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('texts', 'invalidtexts'),
        ('texts', ''),
        ('texts', None),
    ])
    def test_api_Portraits_DecryptTextsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  文本解密 """
        texts = None
        intef = EdgeApi.Portraits_DecryptTextsPutApi(texts=texts, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('portrait_ids', 'invalidportrait_ids'),
        ('portrait_ids', ''),
        ('portrait_ids', None),
    ])
    def test_api_Portraits_DeletePortraitsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除人像 """
        db_id = None
        portrait_ids = None
        intef = EdgeApi.Portraits_DeletePortraitsPostApi(db_id=db_id, portrait_ids=portrait_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('portraits_ids', 'invalidportraits_ids'),
        ('portraits_ids', ''),
        ('portraits_ids', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
    ])
    def test_api_Portraits_ExportPortraitsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  导出人像 """
        portraits_ids = None
        db_id = None
        intef = EdgeApi.Portraits_ExportPortraitsPostApi(portraits_ids=portraits_ids, db_id=db_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('encrypted', 'invalidencrypted'),
        ('encrypted', ''),
        ('encrypted', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_Portraits_ListPortraitsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询人像列表 """
        db_id = None
        encrypted = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = EdgeApi.Portraits_ListPortraitsGetApi(db_id=db_id, encrypted=encrypted, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('encrypted', 'invalidencrypted'),
        ('encrypted', ''),
        ('encrypted', None),
        ('portrait_ids', 'invalidportrait_ids'),
        ('portrait_ids', ''),
        ('portrait_ids', None),
    ])
    def test_api_Portraits_QueryPortraitsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询人像 """
        db_id = None
        encrypted = None
        portrait_ids = None
        intef = EdgeApi.Portraits_QueryPortraitsPostApi(db_id=db_id, encrypted=encrypted, portrait_ids=portrait_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_ids', 'invaliddb_ids'),
        ('db_ids', ''),
        ('db_ids', None),
        ('encrypted', 'invalidencrypted'),
        ('encrypted', ''),
        ('encrypted', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('job_number', 'invalidjob_number'),
        ('job_number', ''),
        ('job_number', None),
        ('ic_number', 'invalidic_number'),
        ('ic_number', ''),
        ('ic_number', None),
        ('id_number', 'invalidid_number'),
        ('id_number', ''),
        ('id_number', None),
        ('start_activation_time', 'invalidstart_activation_time'),
        ('start_activation_time', ''),
        ('start_activation_time', None),
        ('end_activation_time', 'invalidend_activation_time'),
        ('end_activation_time', ''),
        ('end_activation_time', None),
        ('start_expire_time', 'invalidstart_expire_time'),
        ('start_expire_time', ''),
        ('start_expire_time', None),
        ('end_expire_time', 'invalidend_expire_time'),
        ('end_expire_time', ''),
        ('end_expire_time', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
    ])
    def test_api_Portraits_SearchPortraitsInvalidParam(self, invalidParam, config_obj, EdgeApi):
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
        intef = EdgeApi.Portraits_SearchPortraitsPostApi(db_ids=db_ids, encrypted=encrypted, page=page, name=name, job_number=job_number, ic_number=ic_number, id_number=id_number, start_activation_time=start_activation_time, end_activation_time=end_activation_time, start_expire_time=start_expire_time, end_expire_time=end_expire_time, status=status, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('dbs', 'invaliddbs'),
        ('dbs', ''),
        ('dbs', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
    ])
    def test_api_Portraits_SearchImageInDBsInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  在多个人像库进行图片1:N比对 """
        dbs = None
        image = None
        intef = EdgeApi.Portraits_SearchImageInDBsPostApi(dbs=dbs, image=image, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bizapp_name', 'invalidbizapp_name'),
        ('bizapp_name', ''),
        ('bizapp_name', None),
        ('bizapp_version', 'invalidbizapp_version'),
        ('bizapp_version', ''),
        ('bizapp_version', None),
    ])
    def test_api_RecordProcess_DeleteBizAppInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  【内部接口】删除bizapp，用于删除用户自定义bizapp的topic等信息，则记录将不会转发给设... """
        bizapp_name = None
        bizapp_version = None
        intef = EdgeApi.RecordProcess_DeleteBizAppInfoPostApi(bizapp_name=bizapp_name, bizapp_version=bizapp_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_RecordProcess_GetBizAppInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  【内部接口】查询具体bizapp的推送topic """
        biz_app_name = None
        intef = EdgeApi.RecordProcess_GetBizAppInfoGetApi(biz_app_name, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bizapp_info', 'invalidbizapp_info'),
        ('bizapp_info', ''),
        ('bizapp_info', None),
    ])
    def test_api_RecordProcess_SetBizAppInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  设置具体bizapp的推送topic，用于设置用户自定义bizapp的topic等信息，则记录会转发... """
        bizapp_info = None
        intef = EdgeApi.RecordProcess_SetBizAppInfoPostApi(bizapp_info=bizapp_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_RecordProcess_GetStorageSwitchInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  【内部接口】查询storage使用的是es还是pg """
        intef = EdgeApi.RecordProcess_GetStorageSwitchGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_RecordProcess_GetTracelessSwitchInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询当前无痕模式 """
        intef = EdgeApi.RecordProcess_GetTracelessSwitchGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('storage_mode', 'invalidstorage_mode'),
        ('storage_mode', ''),
        ('storage_mode', None),
    ])
    def test_api_RecordProcess_SetTracelessSwitchInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  设置当前无痕模式
无痕模式设置开启时:会清除所有已经产生的记录，图片不清除，且后续记录将存记录，不... """
        storage_mode = None
        intef = EdgeApi.RecordProcess_SetTracelessSwitchPostApi(storage_mode=storage_mode, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
    ])
    def test_api_AgentUserService_ListAPIInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  API信息列表. """
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = EdgeApi.AgentUserService_ListAPIInfoGetApi(paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('api', 'invalidapi'),
        ('api', ''),
        ('api', None),
    ])
    def test_api_AgentUserService_AddAPIInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  增加API信息. """
        api = None
        intef = EdgeApi.AgentUserService_AddAPIInfoPostApi(api=api, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('api', 'invalidapi'),
        ('api', ''),
        ('api', None),
    ])
    def test_api_AgentUserService_UpdateAPIInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  更新API信息. """
        api = None
        intef = EdgeApi.AgentUserService_UpdateAPIInfoPutApi(api=api, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AgentUserService_GetAPIInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询API信息. """
        id = None
        intef = EdgeApi.AgentUserService_GetAPIInfoGetApi(id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AgentUserService_DeleteAPIInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除API信息. """
        id = None
        intef = EdgeApi.AgentUserService_DeleteAPIInfoDeleteApi(id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AgentUserService_CaptchaInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  图形验证码. """
        intef = EdgeApi.AgentUserService_CaptchaGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
    ])
    def test_api_AgentUserService_ListRoleInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  角色列表. """
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = EdgeApi.AgentUserService_ListRoleGetApi(paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('role', 'invalidrole'),
        ('role', ''),
        ('role', None),
    ])
    def test_api_AgentUserService_AddRoleInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  创建角色. """
        role = None
        intef = EdgeApi.AgentUserService_AddRolePostApi(role=role, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('role', 'invalidrole'),
        ('role', ''),
        ('role', None),
    ])
    def test_api_AgentUserService_UpdateRoleInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  修改角色. """
        role = None
        intef = EdgeApi.AgentUserService_UpdateRolePutApi(role=role, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AgentUserService_GetRoleInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询角色详情 """
        id = None
        intef = EdgeApi.AgentUserService_GetRoleGetApi(id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AgentUserService_DeleteRoleInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除角色. """
        id = None
        intef = EdgeApi.AgentUserService_DeleteRoleDeleteApi(id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
        ('decrypt', 'invaliddecrypt'),
        ('decrypt', ''),
        ('decrypt', None),
    ])
    def test_api_AgentUserService_ListUserInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询用户列表. """
        paging_offset = None
        paging_limit = None
        paging_total = None
        decrypt = None
        intef = EdgeApi.AgentUserService_ListUserGetApi(paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, decrypt=decrypt, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user', 'invaliduser'),
        ('user', ''),
        ('user', None),
    ])
    def test_api_AgentUserService_AddUserInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  增加用户. """
        user = None
        intef = EdgeApi.AgentUserService_AddUserPostApi(user=user, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user', 'invaliduser'),
        ('user', ''),
        ('user', None),
    ])
    def test_api_AgentUserService_UpdateUserInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  更新用户. """
        user = None
        intef = EdgeApi.AgentUserService_UpdateUserPutApi(user=user, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AgentUserService_IsInitializedInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  用户是否初始化(admin账户是否首次登录). """
        intef = EdgeApi.AgentUserService_IsInitializedGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('user_name', 'invaliduser_name'),
        ('user_name', ''),
        ('user_name', None),
        ('password', 'invalidpassword'),
        ('password', ''),
        ('password', None),
        ('key', 'invalidkey'),
        ('key', ''),
        ('key', None),
        ('captcha', 'invalidcaptcha'),
        ('captcha', ''),
        ('captcha', None),
    ])
    def test_api_AgentUserService_UserLoginInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  用户登录, 当返回错误码为11时, 表示需要下次登录需要验证码. """
        user_name = None
        password = None
        key = None
        captcha = None
        intef = EdgeApi.AgentUserService_UserLoginPostApi(user_name=user_name, password=password, key=key, captcha=captcha, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('token', 'invalidtoken'),
        ('token', ''),
        ('token', None),
    ])
    def test_api_AgentUserService_UserLogoutInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  用户注销. """
        token = None
        intef = EdgeApi.AgentUserService_UserLogoutPostApi(token=token, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('decrypt', 'invaliddecrypt'),
        ('decrypt', ''),
        ('decrypt', None),
    ])
    def test_api_AgentUserService_GetUserInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  查询用户信息 """
        id = None
        decrypt = None
        intef = EdgeApi.AgentUserService_GetUserGetApi(id, decrypt=decrypt, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AgentUserService_DeleteUserInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  删除用户. """
        id = None
        intef = EdgeApi.AgentUserService_DeleteUserDeleteApi(id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_AgentUserService_UpdateUserApiSecretInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  重新生成用户ApiSecret """
        id = None
        intef = EdgeApi.AgentUserService_UpdateUserApiSecretPostApi(id, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('RTSP', 'invalidRTSP'),
        ('RTSP', ''),
        ('RTSP', None),
    ])
    def test_api_NebulaVDDAgentSrv_DownloadLiveShotInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取实时背景大图. """
        RTSP = None
        intef = EdgeApi.NebulaVDDAgentSrv_DownloadLiveShotPostApi(RTSP=RTSP, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('source_type', 'invalidsource_type'),
        ('source_type', ''),
        ('source_type', None),
        ('source', 'invalidsource'),
        ('source', ''),
        ('source', None),
        ('timestamp', 'invalidtimestamp'),
        ('timestamp', ''),
        ('timestamp', None),
    ])
    def test_api_NebulaVDDAgentSrv_DownloadReplayShotInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  批量下载回放图片. """
        source_type = None
        source = None
        timestamp = None
        intef = EdgeApi.NebulaVDDAgentSrv_DownloadReplayShotPostApi(source_type=source_type, source=source, timestamp=timestamp, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('source_type', 'invalidsource_type'),
        ('source_type', ''),
        ('source_type', None),
        ('source', 'invalidsource'),
        ('source', ''),
        ('source', None),
        ('timestamp', 'invalidtimestamp'),
        ('timestamp', ''),
        ('timestamp', None),
        ('before', 'invalidbefore'),
        ('before', ''),
        ('before', None),
        ('after', 'invalidafter'),
        ('after', ''),
        ('after', None),
    ])
    def test_api_NebulaVDDAgentSrv_DownloadReplayVideoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  批量下载回放短视频. """
        source_type = None
        source = None
        timestamp = None
        before = None
        after = None
        intef = EdgeApi.NebulaVDDAgentSrv_DownloadReplayVideoPostApi(source_type=source_type, source=source, timestamp=timestamp, before=before, after=after, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_BatchCompareFeatureInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  人脸特征1:1比对 [SINCE v3.1.0].
[EN] One to one Identity... """
        requests = None
        intef = EdgeApi.BatchCompareFeaturePostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('face_type', 'invalidface_type'),
        ('face_type', ''),
        ('face_type', None),
    ])
    def test_api_BatchDetectInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  对批量的图片中的人脸进行检测(只输出检测框和关键点坐标, 不输出特征和属性).
[EN] Detec... """
        requests = None
        detect_mode = None
        face_type = None
        intef = EdgeApi.BatchDetectPostApi(requests=requests, detect_mode=detect_mode, face_type=face_type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('face_type', 'invalidface_type'),
        ('face_type', ''),
        ('face_type', None),
    ])
    def test_api_BatchDetectAndExtractAll2InvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  对批量的图片中的所有人脸进行检测、提特征、提属性. v2.1.0之后用于替代BatchDetectA... """
        requests = None
        detect_mode = None
        face_type = None
        intef = EdgeApi.BatchDetectAndExtractAll2PostApi(requests=requests, detect_mode=detect_mode, face_type=face_type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_BatchExtractWithBoundingInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  对批量的图片中指定区域的人脸提特征.
[EN] Extract features of Identi... """
        requests = None
        intef = EdgeApi.BatchExtractWithBoundingPostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('one', 'invalidone'),
        ('one', ''),
        ('one', None),
        ('other', 'invalidother'),
        ('other', ''),
        ('other', None),
    ])
    def test_api_CompareFeatureInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  特征1：1比对.
[EN] One to one feature comparison. """
        one = None
        other = None
        intef = EdgeApi.CompareFeaturePostApi(one=one, other=other, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_GetSystemInfoInvalidParam(self, invalidParam, config_obj, EdgeApi):
        """  获取系统信息 [SINCE v2.2.0].
[EN] Get system info which ... """
        intef = EdgeApi.GetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200
