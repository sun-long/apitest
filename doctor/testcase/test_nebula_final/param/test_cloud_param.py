#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestCloudParam(object):
    """ cloud Param测试"""

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
    def test_api_BizAppCloudTaskService_LicenseStatisticsInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  License授权信息,【此接口为实验性接口, 以后极大概率会调整，仅用于人工请求，请不要用于生产环... """
        ak = None
        device_id = None
        intef = CloudApi.BizAppCloudTaskService_LicenseStatisticsGetApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppCloudTaskService_PowerInfoInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取算力信息 """
        ak = None
        device_id = None
        intef = CloudApi.BizAppCloudTaskService_PowerInfoGetApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_num', 'invalidpage_num'),
        ('page_num', ''),
        ('page_num', None),
        ('page_size', 'invalidpage_size'),
        ('page_size', ''),
        ('page_size', None),
        ('sub_device_ids', 'invalidsub_device_ids'),
        ('sub_device_ids', ''),
        ('sub_device_ids', None),
        ('keyword', 'invalidkeyword'),
        ('keyword', ''),
        ('keyword', None),
    ])
    def test_api_BizAppCloudTaskService_QueryTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  任务列表 """
        ak = None
        device_id = None
        page_num = None
        page_size = None
        sub_device_ids = None
        keyword = None
        intef = CloudApi.BizAppCloudTaskService_QueryTaskGetApi(ak, device_id, page_num=page_num, page_size=page_size, sub_device_ids=sub_device_ids, keyword=keyword, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppCloudTaskService_DeleteTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  删除任务 """
        ak = None
        device_id = None
        intef = CloudApi.BizAppCloudTaskService_DeleteTaskDeleteApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_BizAppCloudTaskService_CreateTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  批量创建任务(同一个设备), url path里的ak和device_id会覆盖body请求体的ak... """
        ak = None
        device_id = None
        requests = None
        intef = CloudApi.BizAppCloudTaskService_CreateTaskPostApi(ak, device_id, requests=requests, sendRequest=False)
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
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('dbs', 'invaliddbs'),
        ('dbs', ''),
        ('dbs', None),
    ])
    def test_api_BizAppCloudTaskService_UpdateTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
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
        intef = CloudApi.BizAppCloudTaskService_UpdateTaskPutApi(ak, device_id, task_ids=task_ids, name=name, desc=desc, object_config=object_config, extend_config=extend_config, schedule=schedule, dbs=dbs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
    ])
    def test_api_BizAppCloudTaskService_DisableTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  禁用任务, bizapp-task状态置为禁用,引擎侧任务将停止 """
        ak = None
        device_id = None
        task_ids = None
        intef = CloudApi.BizAppCloudTaskService_DisableTaskPutApi(ak, device_id, task_ids=task_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
    ])
    def test_api_BizAppCloudTaskService_EnableTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  启用任务, bizapp-task状态置为启用,引擎侧任务将开始调度并运行 """
        ak = None
        device_id = None
        task_ids = None
        intef = CloudApi.BizAppCloudTaskService_EnableTaskPutApi(ak, device_id, task_ids=task_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_BizAppCloudTaskService_DetailTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  任务详情 """
        ak = None
        device_id = None
        task_id = None
        intef = CloudApi.BizAppCloudTaskService_DetailTaskGetApi(ak, device_id, task_id, sendRequest=False)
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
        ('device_info', 'invaliddevice_info'),
        ('device_info', ''),
        ('device_info', None),
        ('object_config', 'invalidobject_config'),
        ('object_config', ''),
        ('object_config', None),
        ('extend_config', 'invalidextend_config'),
        ('extend_config', ''),
        ('extend_config', None),
        ('schedule', 'invalidschedule'),
        ('schedule', ''),
        ('schedule', None),
        ('stream_type', 'invalidstream_type'),
        ('stream_type', ''),
        ('stream_type', None),
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('not_support_merge', 'invalidnot_support_merge'),
        ('not_support_merge', ''),
        ('not_support_merge', None),
        ('dbs', 'invaliddbs'),
        ('dbs', ''),
        ('dbs', None),
    ])
    def test_api_BizAppCloudTaskService_CreateTaskMultipleDevicesInvalidParam(self, invalidParam, config_obj, CloudApi):
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
        intef = CloudApi.BizAppCloudTaskService_CreateTaskMultipleDevicesPostApi(ak, name=name, task_type=task_type, desc=desc, detect_type=detect_type, active=active, device_info=device_info, object_config=object_config, extend_config=extend_config, schedule=schedule, stream_type=stream_type, not_support_merge=not_support_merge, dbs=dbs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_type', 'invalidtask_type'),
        ('task_type', ''),
        ('task_type', None),
        ('task_status', 'invalidtask_status'),
        ('task_status', ''),
        ('task_status', None),
    ])
    def test_api_NebulaVDDServiceSrv_ListTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取租户任务. """
        ak = None
        task_type = None
        task_status = None
        intef = CloudApi.NebulaVDDServiceSrv_ListTaskGetApi(ak, task_type=task_type, task_status=task_status, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_CallbackService_ListCallbackConfigInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  查询callback配置列表. """
        ak = None
        intef = CloudApi.CallbackService_ListCallbackConfigGetApi(ak, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
    ])
    def test_api_CallbackService_AddCallbackConfigInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  增加callback配置项. """
        ak = None
        config = None
        intef = CloudApi.CallbackService_AddCallbackConfigPostApi(ak, config=config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
    ])
    def test_api_CallbackService_UpdateCallbackConfigInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  更新callback配置项,更新指定ak的配置. """
        ak = None
        config = None
        intef = CloudApi.CallbackService_UpdateCallbackConfigPutApi(ak, config=config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
    ])
    def test_api_CallbackService_GetCallbackConfigInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  查询callback的配置. """
        ak = None
        id = None
        name = None
        intef = CloudApi.CallbackService_GetCallbackConfigGetApi(ak, id, name=name, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_CallbackService_DeleteCallbackConfigInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  删除callback配置项. """
        ak = None
        id = None
        intef = CloudApi.CallbackService_DeleteCallbackConfigDeleteApi(ak, id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaDBSyncSrv_DBListInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取所有同步库信息的列表. """
        ak = None
        intef = CloudApi.NebulaDBSyncSrv_DBListGetApi(ak, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('db_type', 'invaliddb_type'),
        ('db_type', ''),
        ('db_type', None),
        ('db_size', 'invaliddb_size'),
        ('db_size', ''),
        ('db_size', None),
        ('oplog_sync_interval_sec', 'invalidoplog_sync_interval_sec'),
        ('oplog_sync_interval_sec', ''),
        ('oplog_sync_interval_sec', None),
        ('snapshot_object_changes', 'invalidsnapshot_object_changes'),
        ('snapshot_object_changes', ''),
        ('snapshot_object_changes', None),
        ('snapshot_interval_sec', 'invalidsnapshot_interval_sec'),
        ('snapshot_interval_sec', ''),
        ('snapshot_interval_sec', None),
        ('operator', 'invalidoperator'),
        ('operator', ''),
        ('operator', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('sync_info', 'invalidsync_info'),
        ('sync_info', ''),
        ('sync_info', None),
    ])
    def test_api_NebulaDBSyncSrv_DBNewInvalidParam(self, invalidParam, config_obj, CloudApi):
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
        intef = CloudApi.NebulaDBSyncSrv_DBNewPostApi(ak, name=name, db_type=db_type, db_size=db_size, oplog_sync_interval_sec=oplog_sync_interval_sec, snapshot_object_changes=snapshot_object_changes, snapshot_interval_sec=snapshot_interval_sec, operator=operator, feature_version=feature_version, description=description, sync_info=sync_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaDBSyncSrv_DBGetInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取指定同步库信息. """
        ak = None
        db_id = None
        intef = CloudApi.NebulaDBSyncSrv_DBGetGetApi(ak, db_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaDBSyncSrv_DBDeleteInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  删除指定同步库. """
        ak = None
        db_id = None
        intef = CloudApi.NebulaDBSyncSrv_DBDeleteDeleteApi(ak, db_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('operator', 'invalidoperator'),
        ('operator', ''),
        ('operator', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('db_type', 'invaliddb_type'),
        ('db_type', ''),
        ('db_type', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_NebulaDBSyncSrv_DBUpdateInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  修改指定同步库的名称或者库描述. """
        ak = None
        db_id = None
        operator = None
        name = None
        db_type = None
        description = None
        feature_version = None
        intef = CloudApi.NebulaDBSyncSrv_DBUpdatePatchApi(ak, db_id, operator=operator, name=name, db_type=db_type, description=description, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('objects', 'invalidobjects'),
        ('objects', ''),
        ('objects', None),
    ])
    def test_api_NebulaDBSyncSrv_PortraitBatchAddInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  将批量对象入指定同步库. """
        ak = None
        db_id = None
        objects = None
        intef = CloudApi.NebulaDBSyncSrv_PortraitBatchAddPostApi(ak, db_id, objects=objects, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('ids', 'invalidids'),
        ('ids', ''),
        ('ids', None),
    ])
    def test_api_NebulaDBSyncSrv_PortraitBatchDeleteInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  通过主key删除指定同步库中指定对象. """
        ak = None
        db_id = None
        ids = None
        intef = CloudApi.NebulaDBSyncSrv_PortraitBatchDeletePostApi(ak, db_id, ids=ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('ids', 'invalidids'),
        ('ids', ''),
        ('ids', None),
    ])
    def test_api_NebulaDBSyncSrv_PortraitBatchGetInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  通过主key在指定同步库中批量获取对象. """
        ak = None
        db_id = None
        ids = None
        intef = CloudApi.NebulaDBSyncSrv_PortraitBatchGetPostApi(ak, db_id, ids=ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('objects', 'invalidobjects'),
        ('objects', ''),
        ('objects', None),
    ])
    def test_api_NebulaDBSyncSrv_PortraitBatchUpdateInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  通过主key在指定同步库中批量更新对象. """
        ak = None
        db_id = None
        objects = None
        intef = CloudApi.NebulaDBSyncSrv_PortraitBatchUpdatePostApi(ak, db_id, objects=objects, sendRequest=False)
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
    def test_api_NebulaDBSyncSrv_DBDeviceListInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取同步库关联的所有设备. """
        ak = None
        db_id = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = CloudApi.NebulaDBSyncSrv_DBDeviceListGetApi(ak, db_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
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
    ])
    def test_api_NebulaDBSyncSrv_PortraitListInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  分页获取指定同步库中所有对象. """
        ak = None
        db_id = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = CloudApi.NebulaDBSyncSrv_PortraitListGetApi(ak, db_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaDBSyncSrv_DBSyncStartInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  启动指定同步库同步进程. """
        ak = None
        db_id = None
        intef = CloudApi.NebulaDBSyncSrv_DBSyncStartPutApi(ak, db_id, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaDBSyncSrv_DeviceDBListInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取设备关联的所有同步库. """
        ak = None
        device_id = None
        intef = CloudApi.NebulaDBSyncSrv_DeviceDBListGetApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('db_ids', 'invaliddb_ids'),
        ('db_ids', ''),
        ('db_ids', None),
    ])
    def test_api_NebulaDBSyncSrv_DeviceDBBatchUpdateInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  全量更新指定设备与同步库的关联关系. """
        ak = None
        device_id = None
        db_ids = None
        intef = CloudApi.NebulaDBSyncSrv_DeviceDBBatchUpdatePostApi(ak, device_id, db_ids=db_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaDBSyncSrv_DeviceSyncStatusGetInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取设备关联的所有同步库的同步状态, 相应业务影子在设备绑定时创建. """
        ak = None
        device_id = None
        intef = CloudApi.NebulaDBSyncSrv_DeviceSyncStatusGetGetApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('request_id', 'invalidrequest_id'),
        ('request_id', ''),
        ('request_id', None),
        ('registry_id', 'invalidregistry_id'),
        ('registry_id', ''),
        ('registry_id', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('content', 'invalidcontent'),
        ('content', ''),
        ('content', None),
    ])
    def test_api_NebulaIOTSrv_UploadAgentMetricInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  UploadAgentMetric agent回调上传metric """
        request_id = None
        registry_id = None
        device_id = None
        name = None
        content = None
        intef = CloudApi.NebulaIOTSrv_UploadAgentMetricPostApi(request_id=request_id, registry_id=registry_id, device_id=device_id, name=name, content=content, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('registry_id', 'invalidregistry_id'),
        ('registry_id', ''),
        ('registry_id', None),
    ])
    def test_api_NebulaIOTSrv_CreateTenantInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  CreateTenant 创建租户，可以指定租户绑定的 symphony registry_id。
... """
        registry_id = None
        intef = CloudApi.NebulaIOTSrv_CreateTenantPutApi(registry_id=registry_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_GetTenantByAKInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  GetTenant 获取 tenant 信息 """
        ak = None
        intef = CloudApi.NebulaIOTSrv_GetTenantByAKGetApi(ak, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_RemoveTenantByAKInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  RemoveTenantByAK 删除 tenant 信息 """
        ak = None
        intef = CloudApi.NebulaIOTSrv_RemoveTenantByAKDeleteApi(ak, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('registry_id', 'invalidregistry_id'),
        ('registry_id', ''),
        ('registry_id', None),
    ])
    def test_api_NebulaIOTSrv_UpdateTenantByAKInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  UpdateTenantByAK 修改 tenant 的信息 """
        ak = None
        registry_id = None
        intef = CloudApi.NebulaIOTSrv_UpdateTenantByAKPostApi(ak, registry_id=registry_id, sendRequest=False)
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
    def test_api_NebulaIOTSrv_GetDevicesInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  GetDevices 获取 ak 下所有device信息 """
        ak = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = CloudApi.NebulaIOTSrv_GetDevicesGetApi(ak, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_GetDeviceBySNInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  GetDeviceByDeviceSN 通过deviceSN获取device信息 """
        ak = None
        device_sn = None
        intef = CloudApi.NebulaIOTSrv_GetDeviceBySNGetApi(ak, device_sn, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_GetDeviceByDeviceIDInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  GetDeviceByDeviceID 获取 device 信息 """
        ak = None
        device_id = None
        intef = CloudApi.NebulaIOTSrv_GetDeviceByDeviceIDGetApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('device', 'invaliddevice'),
        ('device', ''),
        ('device', None),
    ])
    def test_api_NebulaIOTSrv_UpdateDeviceByDeviceIDInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  UpdateDeviceByDeviceID 获取 device 信息 """
        ak = None
        device_id = None
        device = None
        intef = CloudApi.NebulaIOTSrv_UpdateDeviceByDeviceIDPostApi(ak, device_id, device=device, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_GetActivationCodeInfoByDeviceIDInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  GetActivationCodeInfoByDeviceID 获取边侧设备当前激活码信息 """
        ak = None
        device_id = None
        intef = CloudApi.NebulaIOTSrv_GetActivationCodeInfoByDeviceIDGetApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('raw_code', 'invalidraw_code'),
        ('raw_code', ''),
        ('raw_code', None),
        ('code_name', 'invalidcode_name'),
        ('code_name', ''),
        ('code_name', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
    ])
    def test_api_NebulaIOTSrv_UpsertActivationCodeByDeviceIDInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  UpsertActivationCodeByDeviceID 下发activation code """
        ak = None
        device_id = None
        raw_code = None
        code_name = None
        description = None
        intef = CloudApi.NebulaIOTSrv_UpsertActivationCodeByDeviceIDPostApi(ak, device_id, raw_code=raw_code, code_name=code_name, description=description, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_ListAppletsByDeviceIDInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  ListAppletsByDeviceID 获取边侧设备当前applet信息 """
        ak = None
        device_id = None
        intef = CloudApi.NebulaIOTSrv_ListAppletsByDeviceIDGetApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_BatchRemoveSubDeviceInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  BatchRemoveSubDevice 批量删除 sub_device """
        ak = None
        device_id = None
        intef = CloudApi.NebulaIOTSrv_BatchRemoveSubDeviceDeleteApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('sub_devices', 'invalidsub_devices'),
        ('sub_devices', ''),
        ('sub_devices', None),
    ])
    def test_api_NebulaIOTSrv_BatchCreateSubDeviceInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  BatchCreateSubDevice 批量添加 sub_device 信息 """
        ak = None
        device_id = None
        sub_devices = None
        intef = CloudApi.NebulaIOTSrv_BatchCreateSubDevicePutApi(ak, device_id, sub_devices=sub_devices, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('request_id', 'invalidrequest_id'),
        ('request_id', ''),
        ('request_id', None),
        ('object_id', 'invalidobject_id'),
        ('object_id', ''),
        ('object_id', None),
        ('start', 'invalidstart'),
        ('start', ''),
        ('start', None),
        ('end', 'invalidend'),
        ('end', ''),
        ('end', None),
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
    def test_api_NebulaIOTSrv_GetOPLOGsInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  GetOPLOGs 获取设备操作日志，返回以时间倒序排列的 oplog """
        ak = None
        device_id = None
        request_id = None
        object_id = None
        start = None
        end = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = CloudApi.NebulaIOTSrv_GetOPLOGsGetApi(ak, device_id, request_id=request_id, object_id=object_id, start=start, end=end, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('session_id', 'invalidsession_id'),
        ('session_id', ''),
        ('session_id', None),
    ])
    def test_api_NebulaIOTSrv_GetSSHSessionsInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  GetSSHSessions 获取盒子对应的有效的 sessions。只要没过期的 session ... """
        ak = None
        device_id = None
        session_id = None
        intef = CloudApi.NebulaIOTSrv_GetSSHSessionsGetApi(ak, device_id, session_id=session_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('duration', 'invalidduration'),
        ('duration', ''),
        ('duration', None),
    ])
    def test_api_NebulaIOTSrv_CreateSSHSessionInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  CreateSSHSession 创建 ssh 链接的 session 信息，一个 device 可... """
        ak = None
        device_id = None
        duration = None
        intef = CloudApi.NebulaIOTSrv_CreateSSHSessionPostApi(ak, device_id, duration=duration, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_RemoveSSHSessionInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  RemoveSSHSession  删除 ssh session。 """
        ak = None
        device_id = None
        session_id = None
        intef = CloudApi.NebulaIOTSrv_RemoveSSHSessionDeleteApi(ak, device_id, session_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_GetSubDevicesInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  GetSubDevices 查询 sub_device 的信息 """
        ak = None
        device_id = None
        intef = CloudApi.NebulaIOTSrv_GetSubDevicesGetApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('device_sn', 'invaliddevice_sn'),
        ('device_sn', ''),
        ('device_sn', None),
        ('product_name', 'invalidproduct_name'),
        ('product_name', ''),
        ('product_name', None),
        ('device_kind', 'invaliddevice_kind'),
        ('device_kind', ''),
        ('device_kind', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('device_config', 'invaliddevice_config'),
        ('device_config', ''),
        ('device_config', None),
        ('extra_info', 'invalidextra_info'),
        ('extra_info', ''),
        ('extra_info', None),
        ('brand', 'invalidbrand'),
        ('brand', ''),
        ('brand', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('extra_config', 'invalidextra_config'),
        ('extra_config', ''),
        ('extra_config', None),
        ('optionsWhenConflict', 'invalidoptionsWhenConflict'),
        ('optionsWhenConflict', ''),
        ('optionsWhenConflict', None),
    ])
    def test_api_NebulaIOTSrv_CreateSubDeviceInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  CreateSubDevice 添加 sub_device 信息 """
        ak = None
        device_id = None
        device_sn = None
        product_name = None
        device_kind = None
        description = None
        device_config = None
        extra_info = None
        brand = None
        name = None
        extra_config = None
        optionsWhenConflict = None
        intef = CloudApi.NebulaIOTSrv_CreateSubDevicePutApi(ak, device_id, device_sn=device_sn, product_name=product_name, device_kind=device_kind, description=description, device_config=device_config, extra_info=extra_info, brand=brand, name=name, extra_config=extra_config, optionsWhenConflict=optionsWhenConflict, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_GetSubDeviceByIDInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  GetSubDeviceByID 获取 subDevice 信息 """
        ak = None
        device_id = None
        sub_device_id = None
        intef = CloudApi.NebulaIOTSrv_GetSubDeviceByIDGetApi(ak, device_id, sub_device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('optionsWhenConflict', 'invalidoptionsWhenConflict'),
        ('optionsWhenConflict', ''),
        ('optionsWhenConflict', None),
        ('skip', 'invalidskip'),
        ('skip', ''),
        ('skip', None),
    ])
    def test_api_NebulaIOTSrv_RemoveSubDeviceInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  RemoveSubDevice 删除 sub_device """
        ak = None
        device_id = None
        sub_device_id = None
        optionsWhenConflict = None
        skip = None
        intef = CloudApi.NebulaIOTSrv_RemoveSubDeviceDeleteApi(ak, device_id, sub_device_id, optionsWhenConflict=optionsWhenConflict, skip=skip, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('sub_device_id', 'invalidsub_device_id'),
        ('sub_device_id', ''),
        ('sub_device_id', None),
        ('extra_config', 'invalidextra_config'),
        ('extra_config', ''),
        ('extra_config', None),
        ('product_name', 'invalidproduct_name'),
        ('product_name', ''),
        ('product_name', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('device_config', 'invaliddevice_config'),
        ('device_config', ''),
        ('device_config', None),
        ('extra_info', 'invalidextra_info'),
        ('extra_info', ''),
        ('extra_info', None),
        ('brand', 'invalidbrand'),
        ('brand', ''),
        ('brand', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('device_sn', 'invaliddevice_sn'),
        ('device_sn', ''),
        ('device_sn', None),
        ('optionsWhenConflict', 'invalidoptionsWhenConflict'),
        ('optionsWhenConflict', ''),
        ('optionsWhenConflict', None),
        ('skip', 'invalidskip'),
        ('skip', ''),
        ('skip', None),
    ])
    def test_api_NebulaIOTSrv_UpdateSubDeviceInvalidParam(self, invalidParam, config_obj, CloudApi):
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
        intef = CloudApi.NebulaIOTSrv_UpdateSubDevicePostApi(ak, device_id, sub_device_id, extra_config=extra_config, product_name=product_name, description=description, device_config=device_config, extra_info=extra_info, brand=brand, name=name, device_sn=device_sn, optionsWhenConflict=optionsWhenConflict, skip=skip, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_GetSubDevicesV2InvalidParam(self, invalidParam, config_obj, CloudApi):
        """  GetSubDevicesV2 查询 sub_device 的信息(包含config, state,... """
        ak = None
        device_id = None
        intef = CloudApi.NebulaIOTSrv_GetSubDevicesV2GetApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('sk', 'invalidsk'),
        ('sk', ''),
        ('sk', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
    ])
    def test_api_NebulaIOTSrv_CreateTenantV2InvalidParam(self, invalidParam, config_obj, CloudApi):
        """  CreateTenantV2 同时添加symphony和iot-service租户，在该租户下添加内... """
        ak = None
        sk = None
        name = None
        description = None
        intef = CloudApi.NebulaIOTSrv_CreateTenantV2PutApi(ak=ak, sk=sk, name=name, description=description, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaIOTSrv_RemoveTenantByAKV2InvalidParam(self, invalidParam, config_obj, CloudApi):
        """  RemoveTenantByAKV2 删除symphony和iot-service tenant 的... """
        ak = None
        intef = CloudApi.NebulaIOTSrv_RemoveTenantByAKV2DeleteApi(ak, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('filters_product', 'invalidfilters_product'),
        ('filters_product', ''),
        ('filters_product', None),
        ('filters_module', 'invalidfilters_module'),
        ('filters_module', ''),
        ('filters_module', None),
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
    ])
    def test_api_NebulaOTAService_FirmwareListInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  列举固件信息.
[EN] List firmwares. """
        ak = None
        filters_product = None
        filters_module = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        reversed = None
        intef = CloudApi.NebulaOTAService_FirmwareListGetApi(ak=ak, filters_product=filters_product, filters_module=filters_module, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, reversed=reversed, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('firmware', 'invalidfirmware'),
        ('firmware', ''),
        ('firmware', None),
    ])
    def test_api_NebulaOTAService_FirmwareNewInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  创建新固件.
[EN] Create an firmware. """
        ak = None
        firmware = None
        intef = CloudApi.NebulaOTAService_FirmwareNewPostApi(ak=ak, firmware=firmware, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
    ])
    def test_api_NebulaOTAService_FirmwareGetInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取固件详细信息.
[EN] Get an firmware detail information. """
        firmware_id = None
        ak = None
        intef = CloudApi.NebulaOTAService_FirmwareGetGetApi(firmware_id, ak=ak, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
    ])
    def test_api_NebulaOTAService_FirmwareDeleteInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  删除指定固件. 使用中的固件不允许删除.
[EN] Delete an firmware. """
        firmware_id = None
        ak = None
        intef = CloudApi.NebulaOTAService_FirmwareDeleteDeleteApi(firmware_id, ak=ak, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('firmware_id', 'invalidfirmware_id'),
        ('firmware_id', ''),
        ('firmware_id', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
    ])
    def test_api_NebulaOTAService_FirmwareUpdateInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  修改固件信息.
[EN] Modify an firmware information. """
        firmware_id = None
        ak = None
        description = None
        intef = CloudApi.NebulaOTAService_FirmwareUpdatePatchApi(firmware_id, ak=ak, description=description, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('firmware_id', 'invalidfirmware_id'),
        ('firmware_id', ''),
        ('firmware_id', None),
        ('version_id', 'invalidversion_id'),
        ('version_id', ''),
        ('version_id', None),
        ('device_ids', 'invaliddevice_ids'),
        ('device_ids', ''),
        ('device_ids', None),
        ('marker', 'invalidmarker'),
        ('marker', ''),
        ('marker', None),
        ('ext_data', 'invalidext_data'),
        ('ext_data', ''),
        ('ext_data', None),
        ('upgrade_method', 'invalidupgrade_method'),
        ('upgrade_method', ''),
        ('upgrade_method', None),
    ])
    def test_api_NebulaOTAService_FirmwareBatchUpgradeInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  对一组设备批量下发固件升级通知.
[EN] Send firmware upgrade notifi... """
        firmware_id = None
        ak = None
        version_id = None
        device_ids = None
        marker = None
        ext_data = None
        upgrade_method = None
        intef = CloudApi.NebulaOTAService_FirmwareBatchUpgradePostApi(firmware_id, ak=ak, version_id=version_id, device_ids=device_ids, marker=marker, ext_data=ext_data, upgrade_method=upgrade_method, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
    ])
    def test_api_NebulaOTAService_FirmwareVersionListInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  查询指定固件的版本列表.
[EN] List the specified firmware's ve... """
        firmware_id = None
        ak = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        reversed = None
        intef = CloudApi.NebulaOTAService_FirmwareVersionListGetApi(firmware_id, ak=ak, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, reversed=reversed, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('firmware_id', 'invalidfirmware_id'),
        ('firmware_id', ''),
        ('firmware_id', None),
        ('version', 'invalidversion'),
        ('version', ''),
        ('version', None),
    ])
    def test_api_NebulaOTAService_FirmwareVersionNewInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  新增固件版本.
[EN] Create firmware version. """
        firmware_id = None
        ak = None
        version = None
        intef = CloudApi.NebulaOTAService_FirmwareVersionNewPostApi(firmware_id, ak=ak, version=version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('show_download_url', 'invalidshow_download_url'),
        ('show_download_url', ''),
        ('show_download_url', None),
    ])
    def test_api_NebulaOTAService_FirmwareVersionGetInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取固件版本详细信息.
[EN] Get the specified firmware versio... """
        firmware_id = None
        version_id = None
        ak = None
        show_download_url = None
        intef = CloudApi.NebulaOTAService_FirmwareVersionGetGetApi(firmware_id, version_id, ak=ak, show_download_url=show_download_url, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
    ])
    def test_api_NebulaOTAService_FirmwareVersionDeleteInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  删除指定固件版本，使用中的版本不允许删除.
[EN] Delete the specified fi... """
        firmware_id = None
        version_id = None
        ak = None
        intef = CloudApi.NebulaOTAService_FirmwareVersionDeleteDeleteApi(firmware_id, version_id, ak=ak, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaOTAService_FirmwareVersionUploadInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  上传 firmware 的 version 包. 需要先创建 firmware_version. 仅... """
        firmware_id = None
        version_id = None
        intef = CloudApi.NebulaOTAService_FirmwareVersionUploadPostApi(firmware_id, version_id, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaOTAService_DeviceFirmwareStateQueryInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  DeviceFirmwareStateQuery 查询设备当前所有的固件和版本信息，直接获取设备的影... """
        ak = None
        device_id = None
        intef = CloudApi.NebulaOTAService_DeviceFirmwareStateQueryGetApi(ak, device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaOTAService_UpgradingDevicesInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取正在升级此固件的设备列表.
[EN] List devices that are being u... """
        ak = None
        firmware_id = None
        intef = CloudApi.NebulaOTAService_UpgradingDevicesGetApi(ak, firmware_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('firmware_id', 'invalidfirmware_id'),
        ('firmware_id', ''),
        ('firmware_id', None),
        ('device_ids', 'invaliddevice_ids'),
        ('device_ids', ''),
        ('device_ids', None),
        ('paging', 'invalidpaging'),
        ('paging', ''),
        ('paging', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
    ])
    def test_api_NebulaOTAService_FirmwareDeviceStateQueryInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  查询固件在设备上的版本和状态信息.
[EN] Query the version and statu... """
        ak = None
        firmware_id = None
        device_ids = None
        paging = None
        reversed = None
        intef = CloudApi.NebulaOTAService_FirmwareDeviceStateQueryPostApi(ak, firmware_id, device_ids=device_ids, paging=paging, reversed=reversed, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('filters_task_name', 'invalidfilters_task_name'),
        ('filters_task_name', ''),
        ('filters_task_name', None),
        ('filters_firmware_name', 'invalidfilters_firmware_name'),
        ('filters_firmware_name', ''),
        ('filters_firmware_name', None),
        ('filters_status', 'invalidfilters_status'),
        ('filters_status', ''),
        ('filters_status', None),
        ('paging_offset', 'invalidpaging_offset'),
        ('paging_offset', ''),
        ('paging_offset', None),
        ('paging_limit', 'invalidpaging_limit'),
        ('paging_limit', ''),
        ('paging_limit', None),
        ('paging_total', 'invalidpaging_total'),
        ('paging_total', ''),
        ('paging_total', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
    ])
    def test_api_NebulaOTAService_UpgradeTaskInfoListInvalidParam(self, invalidParam, config_obj, CloudApi):
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
        intef = CloudApi.NebulaOTAService_UpgradeTaskInfoListGetApi(ak, filters_task_name=filters_task_name, filters_firmware_name=filters_firmware_name, filters_status=filters_status, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, reversed=reversed, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
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
    def test_api_NebulaOTAService_UpgradeTaskGetInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  UpgradeTaskQuery 查询固件OTA升级任务的处理进度，不传 task_id 为 lis... """
        ak = None
        task_id = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = CloudApi.NebulaOTAService_UpgradeTaskGetGetApi(ak, task_id=task_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('firmware_id', 'invalidfirmware_id'),
        ('firmware_id', ''),
        ('firmware_id', None),
        ('version_id', 'invalidversion_id'),
        ('version_id', ''),
        ('version_id', None),
        ('device_ids', 'invaliddevice_ids'),
        ('device_ids', ''),
        ('device_ids', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('task_name', 'invalidtask_name'),
        ('task_name', ''),
        ('task_name', None),
        ('upgrade_method', 'invalidupgrade_method'),
        ('upgrade_method', ''),
        ('upgrade_method', None),
        ('start_at', 'invalidstart_at'),
        ('start_at', ''),
        ('start_at', None),
        ('end_at', 'invalidend_at'),
        ('end_at', ''),
        ('end_at', None),
    ])
    def test_api_NebulaOTAService_UpgradeTaskNewInvalidParam(self, invalidParam, config_obj, CloudApi):
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
        intef = CloudApi.NebulaOTAService_UpgradeTaskNewPostApi(ak, firmware_id=firmware_id, version_id=version_id, device_ids=device_ids, type=type, task_name=task_name, upgrade_method=upgrade_method, start_at=start_at, end_at=end_at, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaOTAService_UpgradeTaskDeleteInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  UpgradeTaskDelete 删除未下发的延迟固件升级任务 """
        ak = None
        task_id = None
        intef = CloudApi.NebulaOTAService_UpgradeTaskDeleteDeleteApi(ak, task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
        ('device_ids', 'invaliddevice_ids'),
        ('device_ids', ''),
        ('device_ids', None),
        ('start_at', 'invalidstart_at'),
        ('start_at', ''),
        ('start_at', None),
        ('end_at', 'invalidend_at'),
        ('end_at', ''),
        ('end_at', None),
    ])
    def test_api_NebulaOTAService_UpgradeTaskUpdateInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  UpgradeTaskUpdate 更新延迟固件升级任务的开始/结束时间 """
        ak = None
        task_id = None
        device_ids = None
        start_at = None
        end_at = None
        intef = CloudApi.NebulaOTAService_UpgradeTaskUpdatePatchApi(ak, task_id, device_ids=device_ids, start_at=start_at, end_at=end_at, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('list', 'invalidlist'),
        ('list', ''),
        ('list', None),
        ('task_start', 'invalidtask_start'),
        ('task_start', ''),
        ('task_start', None),
        ('task_end', 'invalidtask_end'),
        ('task_end', ''),
        ('task_end', None),
        ('start_now', 'invalidstart_now'),
        ('start_now', ''),
        ('start_now', None),
    ])
    def test_api_NebulaVDDServiceSrv_CreateBatchBGIMGTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  创建批量背景大图任务. """
        ak = None
        list = None
        task_start = None
        task_end = None
        start_now = None
        intef = CloudApi.NebulaVDDServiceSrv_CreateBatchBGIMGTaskPostApi(ak, list=list, task_start=task_start, task_end=task_end, start_now=start_now, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaVDDServiceSrv_GetBatchBGIMGTaskStatusInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取批量背景大图任务状态. """
        ak = None
        task_id = None
        intef = CloudApi.NebulaVDDServiceSrv_GetBatchBGIMGTaskStatusGetApi(ak, task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
        ('action', 'invalidaction'),
        ('action', ''),
        ('action', None),
        ('task_start', 'invalidtask_start'),
        ('task_start', ''),
        ('task_start', None),
        ('task_end', 'invalidtask_end'),
        ('task_end', ''),
        ('task_end', None),
        ('start_now', 'invalidstart_now'),
        ('start_now', ''),
        ('start_now', None),
    ])
    def test_api_NebulaVDDServiceSrv_UpdateBatchBGIMGTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  变更批量背景大图任务. """
        ak = None
        task_id = None
        action = None
        task_start = None
        task_end = None
        start_now = None
        intef = CloudApi.NebulaVDDServiceSrv_UpdateBatchBGIMGTaskPutApi(ak, task_id, action=action, task_start=task_start, task_end=task_end, start_now=start_now, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('object_id', 'invalidobject_id'),
        ('object_id', ''),
        ('object_id', None),
        ('rtsp', 'invalidrtsp'),
        ('rtsp', ''),
        ('rtsp', None),
        ('onvif_host', 'invalidonvif_host'),
        ('onvif_host', ''),
        ('onvif_host', None),
        ('onvif_port', 'invalidonvif_port'),
        ('onvif_port', ''),
        ('onvif_port', None),
        ('onvif_user', 'invalidonvif_user'),
        ('onvif_user', ''),
        ('onvif_user', None),
        ('onvif_password', 'invalidonvif_password'),
        ('onvif_password', ''),
        ('onvif_password', None),
        ('onvif_channel', 'invalidonvif_channel'),
        ('onvif_channel', ''),
        ('onvif_channel', None),
        ('onvif_protocol_type', 'invalidonvif_protocol_type'),
        ('onvif_protocol_type', ''),
        ('onvif_protocol_type', None),
        ('onvif_stream_type', 'invalidonvif_stream_type'),
        ('onvif_stream_type', ''),
        ('onvif_stream_type', None),
        ('onvif_profile_token', 'invalidonvif_profile_token'),
        ('onvif_profile_token', ''),
        ('onvif_profile_token', None),
    ])
    def test_api_NebulaVDDServiceSrv_GetLiveTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
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
        intef = CloudApi.NebulaVDDServiceSrv_GetLiveTaskGetApi(ak, device_id=device_id, object_id=object_id, rtsp=rtsp, onvif_host=onvif_host, onvif_port=onvif_port, onvif_user=onvif_user, onvif_password=onvif_password, onvif_channel=onvif_channel, onvif_protocol_type=onvif_protocol_type, onvif_stream_type=onvif_stream_type, onvif_profile_token=onvif_profile_token, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('object_id', 'invalidobject_id'),
        ('object_id', ''),
        ('object_id', None),
        ('audience_id', 'invalidaudience_id'),
        ('audience_id', ''),
        ('audience_id', None),
        ('rtsp', 'invalidrtsp'),
        ('rtsp', ''),
        ('rtsp', None),
        ('onvif_host', 'invalidonvif_host'),
        ('onvif_host', ''),
        ('onvif_host', None),
        ('onvif_port', 'invalidonvif_port'),
        ('onvif_port', ''),
        ('onvif_port', None),
        ('onvif_user', 'invalidonvif_user'),
        ('onvif_user', ''),
        ('onvif_user', None),
        ('onvif_password', 'invalidonvif_password'),
        ('onvif_password', ''),
        ('onvif_password', None),
        ('onvif_channel', 'invalidonvif_channel'),
        ('onvif_channel', ''),
        ('onvif_channel', None),
        ('onvif_protocol_type', 'invalidonvif_protocol_type'),
        ('onvif_protocol_type', ''),
        ('onvif_protocol_type', None),
        ('onvif_stream_type', 'invalidonvif_stream_type'),
        ('onvif_stream_type', ''),
        ('onvif_stream_type', None),
        ('onvif_profile_token', 'invalidonvif_profile_token'),
        ('onvif_profile_token', ''),
        ('onvif_profile_token', None),
    ])
    def test_api_NebulaVDDServiceSrv_StopLiveTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
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
        intef = CloudApi.NebulaVDDServiceSrv_StopLiveTaskDeleteApi(ak, device_id=device_id, object_id=object_id, audience_id=audience_id, rtsp=rtsp, onvif_host=onvif_host, onvif_port=onvif_port, onvif_user=onvif_user, onvif_password=onvif_password, onvif_channel=onvif_channel, onvif_protocol_type=onvif_protocol_type, onvif_stream_type=onvif_stream_type, onvif_profile_token=onvif_profile_token, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('object_id', 'invalidobject_id'),
        ('object_id', ''),
        ('object_id', None),
        ('rate', 'invalidrate'),
        ('rate', ''),
        ('rate', None),
        ('live_time', 'invalidlive_time'),
        ('live_time', ''),
        ('live_time', None),
        ('rtsp', 'invalidrtsp'),
        ('rtsp', ''),
        ('rtsp', None),
        ('heartbeat', 'invalidheartbeat'),
        ('heartbeat', ''),
        ('heartbeat', None),
        ('onvif', 'invalidonvif'),
        ('onvif', ''),
        ('onvif', None),
        ('protocol', 'invalidprotocol'),
        ('protocol', ''),
        ('protocol', None),
    ])
    def test_api_NebulaVDDServiceSrv_CreateLiveTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
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
        intef = CloudApi.NebulaVDDServiceSrv_CreateLiveTaskPostApi(ak, device_id=device_id, object_id=object_id, rate=rate, live_time=live_time, rtsp=rtsp, heartbeat=heartbeat, onvif=onvif, protocol=protocol, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('audience_id', 'invalidaudience_id'),
        ('audience_id', ''),
        ('audience_id', None),
    ])
    def test_api_NebulaVDDServiceSrv_LiveHeartbeatInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  直播任务心跳. """
        ak = None
        audience_id = None
        intef = CloudApi.NebulaVDDServiceSrv_LiveHeartbeatPostApi(ak, audience_id=audience_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('sub_device_id', 'invalidsub_device_id'),
        ('sub_device_id', ''),
        ('sub_device_id', None),
    ])
    def test_api_NebulaVDDServiceSrv_CreateLiveShotTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取实时背景大图. """
        ak = None
        device_id = None
        sub_device_id = None
        intef = CloudApi.NebulaVDDServiceSrv_CreateLiveShotTaskPostApi(ak, device_id=device_id, sub_device_id=sub_device_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaVDDServiceSrv_GetLiveShotTaskStatusInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取实时背景大图任务状态. """
        ak = None
        task_id = None
        intef = CloudApi.NebulaVDDServiceSrv_GetLiveShotTaskStatusGetApi(ak, task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('list', 'invalidlist'),
        ('list', ''),
        ('list', None),
        ('task_start', 'invalidtask_start'),
        ('task_start', ''),
        ('task_start', None),
        ('task_end', 'invalidtask_end'),
        ('task_end', ''),
        ('task_end', None),
        ('start_now', 'invalidstart_now'),
        ('start_now', ''),
        ('start_now', None),
    ])
    def test_api_NebulaVDDServiceSrv_CreateBatchShortVideoTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  创建批量短视频任务. """
        ak = None
        list = None
        task_start = None
        task_end = None
        start_now = None
        intef = CloudApi.NebulaVDDServiceSrv_CreateBatchShortVideoTaskPostApi(ak, list=list, task_start=task_start, task_end=task_end, start_now=start_now, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_NebulaVDDServiceSrv_GetBatchShortVideoTaskStatusInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  获取批量短视频任务状态. """
        ak = None
        task_id = None
        intef = CloudApi.NebulaVDDServiceSrv_GetBatchShortVideoTaskStatusGetApi(ak, task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
        ('action', 'invalidaction'),
        ('action', ''),
        ('action', None),
        ('task_start', 'invalidtask_start'),
        ('task_start', ''),
        ('task_start', None),
        ('task_end', 'invalidtask_end'),
        ('task_end', ''),
        ('task_end', None),
        ('start_now', 'invalidstart_now'),
        ('start_now', ''),
        ('start_now', None),
    ])
    def test_api_NebulaVDDServiceSrv_UpdateBatchShortVideoTaskInvalidParam(self, invalidParam, config_obj, CloudApi):
        """  变更批量短视频任务. """
        ak = None
        task_id = None
        action = None
        task_start = None
        task_end = None
        start_now = None
        intef = CloudApi.NebulaVDDServiceSrv_UpdateBatchShortVideoTaskPutApi(ak, task_id, action=action, task_start=task_start, task_end=task_end, start_now=start_now, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
