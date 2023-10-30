#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestCloudApi(object):
    """ cloud Api测试"""

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

    def test_api_BizAppCloudTaskService_LicenseStatistics(self, config_obj, CloudApi, deviceInfo):
        """  License授权信息,【此接口为实验性接口, 以后极大概率会调整，仅用于人工请求，请不要用于生产环... """
        ak = deviceInfo["ak"]
        device_id = deviceInfo["device_id"]
        resp = CloudApi.BizAppCloudTaskService_LicenseStatisticsGetApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_BizAppCloudTaskService_PowerInfo(self, config_obj, CloudApi, deviceInfo):
        """  获取算力信息 """
        ak = deviceInfo["ak"]
        device_id = deviceInfo["device_id"]
        resp = CloudApi.BizAppCloudTaskService_PowerInfoGetApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_BizAppCloudTaskService_QueryTask(self, config_obj, CloudApi):
        """  任务列表 """
        ak = None
        device_id = None
        page_num = None
        page_size = None
        sub_device_ids = None
        keyword = None
        resp = CloudApi.BizAppCloudTaskService_QueryTaskGetApi(ak, device_id, page_num=page_num, page_size=page_size, sub_device_ids=sub_device_ids, keyword=keyword)
        assert resp.status_code == 200

    def test_api_BizAppCloudTaskService_DeleteTask(self, config_obj, CloudApi):
        """  删除任务 """
        ak = None
        device_id = None
        resp = CloudApi.BizAppCloudTaskService_DeleteTaskDeleteApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_BizAppCloudTaskService_CreateTask(self, config_obj, CloudApi):
        """  批量创建任务(同一个设备), url path里的ak和device_id会覆盖body请求体的ak... """
        ak = None
        device_id = None
        requests = None
        resp = CloudApi.BizAppCloudTaskService_CreateTaskPostApi(ak, device_id, requests=requests)
        assert resp.status_code == 200

    def test_api_BizAppCloudTaskService_UpdateTask(self, config_obj, CloudApi):
        """  修改任务 """
        ak = None
        device_id = None
        task_ids = None
        name = None
        desc = None
        object_config = None
        extend_config = None
        schedule = None
        dbs = None
        resp = CloudApi.BizAppCloudTaskService_UpdateTaskPutApi(ak, device_id, task_ids=task_ids, name=name, desc=desc, object_config=object_config, extend_config=extend_config, schedule=schedule, dbs=dbs)
        assert resp.status_code == 200

    def test_api_BizAppCloudTaskService_DisableTask(self, config_obj, CloudApi):
        """  禁用任务, bizapp-task状态置为禁用,引擎侧任务将停止 """
        ak = None
        device_id = None
        task_ids = None
        resp = CloudApi.BizAppCloudTaskService_DisableTaskPutApi(ak, device_id, task_ids=task_ids)
        assert resp.status_code == 200

    def test_api_BizAppCloudTaskService_EnableTask(self, config_obj, CloudApi):
        """  启用任务, bizapp-task状态置为启用,引擎侧任务将开始调度并运行 """
        ak = None
        device_id = None
        task_ids = None
        resp = CloudApi.BizAppCloudTaskService_EnableTaskPutApi(ak, device_id, task_ids=task_ids)
        assert resp.status_code == 200

    def test_api_BizAppCloudTaskService_DetailTask(self, config_obj, CloudApi):
        """  任务详情 """
        ak = None
        device_id = None
        task_id = None
        resp = CloudApi.BizAppCloudTaskService_DetailTaskGetApi(ak, device_id, task_id)
        assert resp.status_code == 200

    def test_api_BizAppCloudTaskService_CreateTaskMultipleDevices(self, config_obj, CloudApi):
        """  创建任务,支持跨device_id """
        ak = None
        name = None
        task_type = None
        desc = None
        detect_type = None
        active = None
        device_info = None
        object_config = None
        extend_config = None
        schedule = None
        stream_type = None
        not_support_merge = None
        dbs = None
        resp = CloudApi.BizAppCloudTaskService_CreateTaskMultipleDevicesPostApi(ak, name=name, task_type=task_type, desc=desc, detect_type=detect_type, active=active, device_info=device_info, object_config=object_config, extend_config=extend_config, schedule=schedule, stream_type=stream_type, not_support_merge=not_support_merge, dbs=dbs)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_ListTask(self, config_obj, CloudApi):
        """  获取租户任务. """
        ak = None
        task_type = None
        task_status = None
        resp = CloudApi.NebulaVDDServiceSrv_ListTaskGetApi(ak, task_type=task_type, task_status=task_status)
        assert resp.status_code == 200

    def test_api_CallbackService_ListCallbackConfig(self, config_obj, CloudApi):
        """  查询callback配置列表. """
        ak = None
        resp = CloudApi.CallbackService_ListCallbackConfigGetApi(ak)
        assert resp.status_code == 200

    def test_api_CallbackService_AddCallbackConfig(self, config_obj, CloudApi):
        """  增加callback配置项. """
        ak = None
        config = None
        resp = CloudApi.CallbackService_AddCallbackConfigPostApi(ak, config=config)
        assert resp.status_code == 200

    def test_api_CallbackService_UpdateCallbackConfig(self, config_obj, CloudApi):
        """  更新callback配置项,更新指定ak的配置. """
        ak = None
        config = None
        resp = CloudApi.CallbackService_UpdateCallbackConfigPutApi(ak, config=config)
        assert resp.status_code == 200

    def test_api_CallbackService_GetCallbackConfig(self, config_obj, CloudApi):
        """  查询callback的配置. """
        ak = None
        id = None
        name = None
        resp = CloudApi.CallbackService_GetCallbackConfigGetApi(ak, id, name=name)
        assert resp.status_code == 200

    def test_api_CallbackService_DeleteCallbackConfig(self, config_obj, CloudApi):
        """  删除callback配置项. """
        ak = None
        id = None
        resp = CloudApi.CallbackService_DeleteCallbackConfigDeleteApi(ak, id)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_DBList(self, config_obj, CloudApi):
        """  获取所有同步库信息的列表. """
        ak = None
        resp = CloudApi.NebulaDBSyncSrv_DBListGetApi(ak)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_DBNew(self, config_obj, CloudApi):
        """  创建一个同步库 """
        ak = None
        name = None
        db_type = None
        db_size = None
        oplog_sync_interval_sec = None
        snapshot_object_changes = None
        snapshot_interval_sec = None
        operator = None
        feature_version = None
        description = None
        sync_info = None
        resp = CloudApi.NebulaDBSyncSrv_DBNewPostApi(ak, name=name, db_type=db_type, db_size=db_size, oplog_sync_interval_sec=oplog_sync_interval_sec, snapshot_object_changes=snapshot_object_changes, snapshot_interval_sec=snapshot_interval_sec, operator=operator, feature_version=feature_version, description=description, sync_info=sync_info)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_DBGet(self, config_obj, CloudApi):
        """  获取指定同步库信息. """
        ak = None
        db_id = None
        resp = CloudApi.NebulaDBSyncSrv_DBGetGetApi(ak, db_id)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_DBDelete(self, config_obj, CloudApi):
        """  删除指定同步库. """
        ak = None
        db_id = None
        resp = CloudApi.NebulaDBSyncSrv_DBDeleteDeleteApi(ak, db_id)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_DBUpdate(self, config_obj, CloudApi):
        """  修改指定同步库的名称或者库描述. """
        ak = None
        db_id = None
        operator = None
        name = None
        db_type = None
        description = None
        feature_version = None
        resp = CloudApi.NebulaDBSyncSrv_DBUpdatePatchApi(ak, db_id, operator=operator, name=name, db_type=db_type, description=description, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_PortraitBatchAdd(self, config_obj, CloudApi):
        """  将批量对象入指定同步库. """
        ak = None
        db_id = None
        objects = None
        resp = CloudApi.NebulaDBSyncSrv_PortraitBatchAddPostApi(ak, db_id, objects=objects)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_PortraitBatchDelete(self, config_obj, CloudApi):
        """  通过主key删除指定同步库中指定对象. """
        ak = None
        db_id = None
        ids = None
        resp = CloudApi.NebulaDBSyncSrv_PortraitBatchDeletePostApi(ak, db_id, ids=ids)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_PortraitBatchGet(self, config_obj, CloudApi):
        """  通过主key在指定同步库中批量获取对象. """
        ak = None
        db_id = None
        ids = None
        resp = CloudApi.NebulaDBSyncSrv_PortraitBatchGetPostApi(ak, db_id, ids=ids)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_PortraitBatchUpdate(self, config_obj, CloudApi):
        """  通过主key在指定同步库中批量更新对象. """
        ak = None
        db_id = None
        objects = None
        resp = CloudApi.NebulaDBSyncSrv_PortraitBatchUpdatePostApi(ak, db_id, objects=objects)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_DBDeviceList(self, config_obj, CloudApi):
        """  获取同步库关联的所有设备. """
        ak = None
        db_id = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = CloudApi.NebulaDBSyncSrv_DBDeviceListGetApi(ak, db_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_PortraitList(self, config_obj, CloudApi):
        """  分页获取指定同步库中所有对象. """
        ak = None
        db_id = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = CloudApi.NebulaDBSyncSrv_PortraitListGetApi(ak, db_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_DBSyncStart(self, config_obj, CloudApi):
        """  启动指定同步库同步进程. """
        ak = None
        db_id = None
        resp = CloudApi.NebulaDBSyncSrv_DBSyncStartPutApi(ak, db_id)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_DeviceDBList(self, config_obj, CloudApi):
        """  获取设备关联的所有同步库. """
        ak = None
        device_id = None
        resp = CloudApi.NebulaDBSyncSrv_DeviceDBListGetApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_DeviceDBBatchUpdate(self, config_obj, CloudApi):
        """  全量更新指定设备与同步库的关联关系. """
        ak = None
        device_id = None
        db_ids = None
        resp = CloudApi.NebulaDBSyncSrv_DeviceDBBatchUpdatePostApi(ak, device_id, db_ids=db_ids)
        assert resp.status_code == 200

    def test_api_NebulaDBSyncSrv_DeviceSyncStatusGet(self, config_obj, CloudApi):
        """  获取设备关联的所有同步库的同步状态, 相应业务影子在设备绑定时创建. """
        ak = None
        device_id = None
        resp = CloudApi.NebulaDBSyncSrv_DeviceSyncStatusGetGetApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_UploadAgentMetric(self, config_obj, CloudApi):
        """  UploadAgentMetric agent回调上传metric """
        request_id = None
        registry_id = None
        device_id = None
        name = None
        content = None
        resp = CloudApi.NebulaIOTSrv_UploadAgentMetricPostApi(request_id=request_id, registry_id=registry_id, device_id=device_id, name=name, content=content)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_CreateTenant(self, config_obj, CloudApi):
        """  CreateTenant 创建租户，可以指定租户绑定的 symphony registry_id。
... """
        registry_id = None
        resp = CloudApi.NebulaIOTSrv_CreateTenantPutApi(registry_id=registry_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_GetTenantByAK(self, config_obj, CloudApi):
        """  GetTenant 获取 tenant 信息 """
        ak = None
        resp = CloudApi.NebulaIOTSrv_GetTenantByAKGetApi(ak)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_RemoveTenantByAK(self, config_obj, CloudApi):
        """  RemoveTenantByAK 删除 tenant 信息 """
        ak = None
        resp = CloudApi.NebulaIOTSrv_RemoveTenantByAKDeleteApi(ak)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_UpdateTenantByAK(self, config_obj, CloudApi):
        """  UpdateTenantByAK 修改 tenant 的信息 """
        ak = None
        registry_id = None
        resp = CloudApi.NebulaIOTSrv_UpdateTenantByAKPostApi(ak, registry_id=registry_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_GetDevices(self, config_obj, CloudApi):
        """  GetDevices 获取 ak 下所有device信息 """
        ak = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = CloudApi.NebulaIOTSrv_GetDevicesGetApi(ak, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_GetDeviceBySN(self, config_obj, CloudApi):
        """  GetDeviceByDeviceSN 通过deviceSN获取device信息 """
        ak = None
        device_sn = None
        resp = CloudApi.NebulaIOTSrv_GetDeviceBySNGetApi(ak, device_sn)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_GetDeviceByDeviceID(self, config_obj, CloudApi):
        """  GetDeviceByDeviceID 获取 device 信息 """
        ak = None
        device_id = None
        resp = CloudApi.NebulaIOTSrv_GetDeviceByDeviceIDGetApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_UpdateDeviceByDeviceID(self, config_obj, CloudApi):
        """  UpdateDeviceByDeviceID 获取 device 信息 """
        ak = None
        device_id = None
        device = None
        resp = CloudApi.NebulaIOTSrv_UpdateDeviceByDeviceIDPostApi(ak, device_id, device=device)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_GetActivationCodeInfoByDeviceID(self, config_obj, CloudApi):
        """  GetActivationCodeInfoByDeviceID 获取边侧设备当前激活码信息 """
        ak = None
        device_id = None
        resp = CloudApi.NebulaIOTSrv_GetActivationCodeInfoByDeviceIDGetApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_UpsertActivationCodeByDeviceID(self, config_obj, CloudApi):
        """  UpsertActivationCodeByDeviceID 下发activation code """
        ak = None
        device_id = None
        raw_code = None
        code_name = None
        description = None
        resp = CloudApi.NebulaIOTSrv_UpsertActivationCodeByDeviceIDPostApi(ak, device_id, raw_code=raw_code, code_name=code_name, description=description)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_ListAppletsByDeviceID(self, config_obj, CloudApi):
        """  ListAppletsByDeviceID 获取边侧设备当前applet信息 """
        ak = None
        device_id = None
        resp = CloudApi.NebulaIOTSrv_ListAppletsByDeviceIDGetApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_BatchRemoveSubDevice(self, config_obj, CloudApi):
        """  BatchRemoveSubDevice 批量删除 sub_device """
        ak = None
        device_id = None
        resp = CloudApi.NebulaIOTSrv_BatchRemoveSubDeviceDeleteApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_BatchCreateSubDevice(self, config_obj, CloudApi):
        """  BatchCreateSubDevice 批量添加 sub_device 信息 """
        ak = None
        device_id = None
        sub_devices = None
        resp = CloudApi.NebulaIOTSrv_BatchCreateSubDevicePutApi(ak, device_id, sub_devices=sub_devices)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_GetOPLOGs(self, config_obj, CloudApi, deviceInfo):
        """  GetOPLOGs 获取设备操作日志，返回以时间倒序排列的 oplog """
        ak = deviceInfo["ak"]
        device_id = deviceInfo["device_id"]
        request_id = None
        object_id = None
        start = None
        end = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = CloudApi.NebulaIOTSrv_GetOPLOGsGetApi(ak, device_id, request_id=request_id, object_id=object_id, start=start, end=end, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_GetSSHSessions(self, config_obj, CloudApi):
        """  GetSSHSessions 获取盒子对应的有效的 sessions。只要没过期的 session ... """
        ak = None
        device_id = None
        session_id = None
        resp = CloudApi.NebulaIOTSrv_GetSSHSessionsGetApi(ak, device_id, session_id=session_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_CreateSSHSession(self, config_obj, CloudApi):
        """  CreateSSHSession 创建 ssh 链接的 session 信息，一个 device 可... """
        ak = None
        device_id = None
        duration = None
        resp = CloudApi.NebulaIOTSrv_CreateSSHSessionPostApi(ak, device_id, duration=duration)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_RemoveSSHSession(self, config_obj, CloudApi):
        """  RemoveSSHSession  删除 ssh session。 """
        ak = None
        device_id = None
        session_id = None
        resp = CloudApi.NebulaIOTSrv_RemoveSSHSessionDeleteApi(ak, device_id, session_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_GetSubDevices(self, config_obj, CloudApi):
        """  GetSubDevices 查询 sub_device 的信息 """
        ak = None
        device_id = None
        resp = CloudApi.NebulaIOTSrv_GetSubDevicesGetApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_CreateSubDevice(self, config_obj, CloudApi, deviceInfo, camera_info):
        """  CreateSubDevice 添加 sub_device 信息 """
        ak = deviceInfo["ak"]
        device_id = deviceInfo["device_id"]
        device_sn = sign_utils.getUuid(32)
        product_name = "test"
        device_kind = camera_info.kind
        description = "test"
        device_config = {
                "ip": {
                    "ips": [
                        {
                            "address": camera_info.ip
                        }
                    ]
                }
            }
        extra_info = None
        brand = camera_info.brand
        name = device_sn
        extra_config = {
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
            }
        optionsWhenConflict = None
        resp = CloudApi.NebulaIOTSrv_CreateSubDevicePutApi(ak, device_id, device_sn=device_sn, product_name=product_name, device_kind=device_kind, description=description, device_config=device_config, extra_info=extra_info, brand=brand, name=name, extra_config=extra_config, optionsWhenConflict=optionsWhenConflict)
        assert resp.status_code == 200
        subDeviceId = resp.json_get("config_sub_device.device_id")
        log().info("subDeviceId=>%s" % subDeviceId)

        resp = CloudApi.getSubDeviceByIDUntilFound(ak, device_id, subDeviceId)
        assert resp.status_code == 200
        assert resp.json_get("state_sub_device.device_id") == subDeviceId

    def test_api_NebulaIOTSrv_GetSubDeviceByID(self, config_obj, CloudApi, deviceInfo):
        """  GetSubDeviceByID 获取 subDevice 信息 """
        ak = deviceInfo["ak"]
        device_id = deviceInfo["device_id"]
        sub_device_id = "2ceda6ed3bee4d08a0ab0577b6476d94"
        resp = CloudApi.NebulaIOTSrv_GetSubDeviceByIDGetApi(ak, device_id, sub_device_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_RemoveSubDevice(self, config_obj, CloudApi):
        """  RemoveSubDevice 删除 sub_device """
        ak = None
        device_id = None
        sub_device_id = None
        optionsWhenConflict = None
        skip = None
        resp = CloudApi.NebulaIOTSrv_RemoveSubDeviceDeleteApi(ak, device_id, sub_device_id, optionsWhenConflict=optionsWhenConflict, skip=skip)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_UpdateSubDevice(self, config_obj, CloudApi):
        """  UpdateSubDevice 修改 sub_device 的信息 """
        ak = None
        device_id = None
        sub_device_id = None
        extra_config = None
        product_name = None
        description = None
        device_config = None
        extra_info = None
        brand = None
        name = None
        device_sn = None
        optionsWhenConflict = None
        skip = None
        resp = CloudApi.NebulaIOTSrv_UpdateSubDevicePostApi(ak, device_id, sub_device_id, extra_config=extra_config, product_name=product_name, description=description, device_config=device_config, extra_info=extra_info, brand=brand, name=name, device_sn=device_sn, optionsWhenConflict=optionsWhenConflict, skip=skip)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_GetSubDevicesV2(self, config_obj, CloudApi):
        """  GetSubDevicesV2 查询 sub_device 的信息(包含config, state,... """
        ak = None
        device_id = None
        resp = CloudApi.NebulaIOTSrv_GetSubDevicesV2GetApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_CreateTenantV2(self, config_obj, CloudApi):
        """  CreateTenantV2 同时添加symphony和iot-service租户，在该租户下添加内... """
        ak = None
        sk = None
        name = None
        description = None
        resp = CloudApi.NebulaIOTSrv_CreateTenantV2PutApi(ak=ak, sk=sk, name=name, description=description)
        assert resp.status_code == 200

    def test_api_NebulaIOTSrv_RemoveTenantByAKV2(self, config_obj, CloudApi):
        """  RemoveTenantByAKV2 删除symphony和iot-service tenant 的... """
        ak = None
        resp = CloudApi.NebulaIOTSrv_RemoveTenantByAKV2DeleteApi(ak)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareList(self, config_obj, CloudApi):
        """  列举固件信息.
[EN] List firmwares. """
        ak = None
        filters_product = None
        filters_module = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        reversed = None
        resp = CloudApi.NebulaOTAService_FirmwareListGetApi(ak=ak, filters_product=filters_product, filters_module=filters_module, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, reversed=reversed)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareNew(self, config_obj, CloudApi):
        """  创建新固件.
[EN] Create an firmware. """
        ak = None
        firmware = None
        resp = CloudApi.NebulaOTAService_FirmwareNewPostApi(ak=ak, firmware=firmware)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareGet(self, config_obj, CloudApi):
        """  获取固件详细信息.
[EN] Get an firmware detail information. """
        firmware_id = None
        ak = None
        resp = CloudApi.NebulaOTAService_FirmwareGetGetApi(firmware_id, ak=ak)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareDelete(self, config_obj, CloudApi):
        """  删除指定固件. 使用中的固件不允许删除.
[EN] Delete an firmware. """
        firmware_id = None
        ak = None
        resp = CloudApi.NebulaOTAService_FirmwareDeleteDeleteApi(firmware_id, ak=ak)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareUpdate(self, config_obj, CloudApi):
        """  修改固件信息.
[EN] Modify an firmware information. """
        firmware_id = None
        ak = None
        description = None
        resp = CloudApi.NebulaOTAService_FirmwareUpdatePatchApi(firmware_id, ak=ak, description=description)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareBatchUpgrade(self, config_obj, CloudApi):
        """  对一组设备批量下发固件升级通知.
[EN] Send firmware upgrade notifi... """
        firmware_id = None
        ak = None
        version_id = None
        device_ids = None
        marker = None
        ext_data = None
        upgrade_method = None
        resp = CloudApi.NebulaOTAService_FirmwareBatchUpgradePostApi(firmware_id, ak=ak, version_id=version_id, device_ids=device_ids, marker=marker, ext_data=ext_data, upgrade_method=upgrade_method)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareVersionList(self, config_obj, CloudApi):
        """  查询指定固件的版本列表.
[EN] List the specified firmware's ve... """
        firmware_id = None
        ak = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        reversed = None
        resp = CloudApi.NebulaOTAService_FirmwareVersionListGetApi(firmware_id, ak=ak, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, reversed=reversed)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareVersionNew(self, config_obj, CloudApi):
        """  新增固件版本.
[EN] Create firmware version. """
        firmware_id = None
        ak = None
        version = None
        resp = CloudApi.NebulaOTAService_FirmwareVersionNewPostApi(firmware_id, ak=ak, version=version)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareVersionGet(self, config_obj, CloudApi):
        """  获取固件版本详细信息.
[EN] Get the specified firmware versio... """
        firmware_id = None
        version_id = None
        ak = None
        show_download_url = None
        resp = CloudApi.NebulaOTAService_FirmwareVersionGetGetApi(firmware_id, version_id, ak=ak, show_download_url=show_download_url)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareVersionDelete(self, config_obj, CloudApi):
        """  删除指定固件版本，使用中的版本不允许删除.
[EN] Delete the specified fi... """
        firmware_id = None
        version_id = None
        ak = None
        resp = CloudApi.NebulaOTAService_FirmwareVersionDeleteDeleteApi(firmware_id, version_id, ak=ak)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareVersionUpload(self, config_obj, CloudApi):
        """  上传 firmware 的 version 包. 需要先创建 firmware_version. 仅... """
        firmware_id = None
        version_id = None
        resp = CloudApi.NebulaOTAService_FirmwareVersionUploadPostApi(firmware_id, version_id)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_DeviceFirmwareStateQuery(self, config_obj, CloudApi):
        """  DeviceFirmwareStateQuery 查询设备当前所有的固件和版本信息，直接获取设备的影... """
        ak = None
        device_id = None
        resp = CloudApi.NebulaOTAService_DeviceFirmwareStateQueryGetApi(ak, device_id)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_UpgradingDevices(self, config_obj, CloudApi):
        """  获取正在升级此固件的设备列表.
[EN] List devices that are being u... """
        ak = None
        firmware_id = None
        resp = CloudApi.NebulaOTAService_UpgradingDevicesGetApi(ak, firmware_id)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_FirmwareDeviceStateQuery(self, config_obj, CloudApi):
        """  查询固件在设备上的版本和状态信息.
[EN] Query the version and statu... """
        ak = None
        firmware_id = None
        device_ids = None
        paging = None
        reversed = None
        resp = CloudApi.NebulaOTAService_FirmwareDeviceStateQueryPostApi(ak, firmware_id, device_ids=device_ids, paging=paging, reversed=reversed)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_UpgradeTaskInfoList(self, config_obj, CloudApi):
        """  查询任务信息列表.
[EN] List upgrade tasks. """
        ak = None
        filters_task_name = None
        filters_firmware_name = None
        filters_status = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        reversed = None
        resp = CloudApi.NebulaOTAService_UpgradeTaskInfoListGetApi(ak, filters_task_name=filters_task_name, filters_firmware_name=filters_firmware_name, filters_status=filters_status, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, reversed=reversed)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_UpgradeTaskGet(self, config_obj, CloudApi):
        """  UpgradeTaskQuery 查询固件OTA升级任务的处理进度，不传 task_id 为 lis... """
        ak = None
        task_id = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = CloudApi.NebulaOTAService_UpgradeTaskGetGetApi(ak, task_id=task_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_UpgradeTaskNew(self, config_obj, CloudApi):
        """  UpgradeTaskNew 创建升级任务，目前升级任务都是静态的，
因此一个设备对一个固件仅允许创... """
        ak = None
        firmware_id = None
        version_id = None
        device_ids = None
        type = None
        task_name = None
        upgrade_method = None
        start_at = None
        end_at = None
        resp = CloudApi.NebulaOTAService_UpgradeTaskNewPostApi(ak, firmware_id=firmware_id, version_id=version_id, device_ids=device_ids, type=type, task_name=task_name, upgrade_method=upgrade_method, start_at=start_at, end_at=end_at)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_UpgradeTaskDelete(self, config_obj, CloudApi):
        """  UpgradeTaskDelete 删除未下发的延迟固件升级任务 """
        ak = None
        task_id = None
        resp = CloudApi.NebulaOTAService_UpgradeTaskDeleteDeleteApi(ak, task_id)
        assert resp.status_code == 200

    def test_api_NebulaOTAService_UpgradeTaskUpdate(self, config_obj, CloudApi):
        """  UpgradeTaskUpdate 更新延迟固件升级任务的开始/结束时间 """
        ak = None
        task_id = None
        device_ids = None
        start_at = None
        end_at = None
        resp = CloudApi.NebulaOTAService_UpgradeTaskUpdatePatchApi(ak, task_id, device_ids=device_ids, start_at=start_at, end_at=end_at)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_CreateBatchBGIMGTask(self, config_obj, CloudApi):
        """  创建批量背景大图任务. """
        ak = None
        list = None
        task_start = None
        task_end = None
        start_now = None
        resp = CloudApi.NebulaVDDServiceSrv_CreateBatchBGIMGTaskPostApi(ak, list=list, task_start=task_start, task_end=task_end, start_now=start_now)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_GetBatchBGIMGTaskStatus(self, config_obj, CloudApi):
        """  获取批量背景大图任务状态. """
        ak = None
        task_id = None
        resp = CloudApi.NebulaVDDServiceSrv_GetBatchBGIMGTaskStatusGetApi(ak, task_id)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_UpdateBatchBGIMGTask(self, config_obj, CloudApi):
        """  变更批量背景大图任务. """
        ak = None
        task_id = None
        action = None
        task_start = None
        task_end = None
        start_now = None
        resp = CloudApi.NebulaVDDServiceSrv_UpdateBatchBGIMGTaskPutApi(ak, task_id, action=action, task_start=task_start, task_end=task_end, start_now=start_now)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_GetLiveTask(self, config_obj, CloudApi):
        """  获取直播任务接口. """
        ak = None
        device_id = None
        object_id = None
        rtsp = None
        onvif_host = None
        onvif_port = None
        onvif_user = None
        onvif_password = None
        onvif_channel = None
        onvif_protocol_type = None
        onvif_stream_type = None
        onvif_profile_token = None
        resp = CloudApi.NebulaVDDServiceSrv_GetLiveTaskGetApi(ak, device_id=device_id, object_id=object_id, rtsp=rtsp, onvif_host=onvif_host, onvif_port=onvif_port, onvif_user=onvif_user, onvif_password=onvif_password, onvif_channel=onvif_channel, onvif_protocol_type=onvif_protocol_type, onvif_stream_type=onvif_stream_type, onvif_profile_token=onvif_profile_token)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_StopLiveTask(self, config_obj, CloudApi):
        """  停止直播任务接口. """
        ak = None
        device_id = None
        object_id = None
        audience_id = None
        rtsp = None
        onvif_host = None
        onvif_port = None
        onvif_user = None
        onvif_password = None
        onvif_channel = None
        onvif_protocol_type = None
        onvif_stream_type = None
        onvif_profile_token = None
        resp = CloudApi.NebulaVDDServiceSrv_StopLiveTaskDeleteApi(ak, device_id=device_id, object_id=object_id, audience_id=audience_id, rtsp=rtsp, onvif_host=onvif_host, onvif_port=onvif_port, onvif_user=onvif_user, onvif_password=onvif_password, onvif_channel=onvif_channel, onvif_protocol_type=onvif_protocol_type, onvif_stream_type=onvif_stream_type, onvif_profile_token=onvif_profile_token)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_CreateLiveTask(self, config_obj, CloudApi):
        """  创建直播任务接口. """
        ak = None
        device_id = None
        object_id = None
        rate = None
        live_time = None
        rtsp = None
        heartbeat = None
        onvif = None
        protocol = None
        resp = CloudApi.NebulaVDDServiceSrv_CreateLiveTaskPostApi(ak, device_id=device_id, object_id=object_id, rate=rate, live_time=live_time, rtsp=rtsp, heartbeat=heartbeat, onvif=onvif, protocol=protocol)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_LiveHeartbeat(self, config_obj, CloudApi):
        """  直播任务心跳. """
        ak = None
        audience_id = None
        resp = CloudApi.NebulaVDDServiceSrv_LiveHeartbeatPostApi(ak, audience_id=audience_id)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_CreateLiveShotTask(self, config_obj, CloudApi):
        """  获取实时背景大图. """
        ak = None
        device_id = None
        sub_device_id = None
        resp = CloudApi.NebulaVDDServiceSrv_CreateLiveShotTaskPostApi(ak, device_id=device_id, sub_device_id=sub_device_id)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_GetLiveShotTaskStatus(self, config_obj, CloudApi):
        """  获取实时背景大图任务状态. """
        ak = None
        task_id = None
        resp = CloudApi.NebulaVDDServiceSrv_GetLiveShotTaskStatusGetApi(ak, task_id)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_CreateBatchShortVideoTask(self, config_obj, CloudApi):
        """  创建批量短视频任务. """
        ak = None
        list = None
        task_start = None
        task_end = None
        start_now = None
        resp = CloudApi.NebulaVDDServiceSrv_CreateBatchShortVideoTaskPostApi(ak, list=list, task_start=task_start, task_end=task_end, start_now=start_now)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_GetBatchShortVideoTaskStatus(self, config_obj, CloudApi):
        """  获取批量短视频任务状态. """
        ak = None
        task_id = None
        resp = CloudApi.NebulaVDDServiceSrv_GetBatchShortVideoTaskStatusGetApi(ak, task_id)
        assert resp.status_code == 200

    def test_api_NebulaVDDServiceSrv_UpdateBatchShortVideoTask(self, config_obj, CloudApi):
        """  变更批量短视频任务. """
        ak = None
        task_id = None
        action = None
        task_start = None
        task_end = None
        start_now = None
        resp = CloudApi.NebulaVDDServiceSrv_UpdateBatchShortVideoTaskPutApi(ak, task_id, action=action, task_start=task_start, task_end=task_end, start_now=start_now)
        assert resp.status_code == 200
