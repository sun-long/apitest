#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

class TestRasmanagerParam(object):
    """ rasManager Param测试"""

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

    @pytest.mark.skip("内部接口不验证")
    @pytest.mark.parametrize("invalidParam", [
        ('states', 'invalidstates'),
        ('states', ''),
        ('states', None),
    ])
    def test_api_RasManager_CallbackAssignmentStateInvalidParam(self, invalidParam, config_obj, RasmanagerApi):
        """  内部接口，用于边缘上报 bot_assignment 的状态
route: prefix=, int... """
        states = None
        intef = RasmanagerApi.RasManager_CallbackAssignmentStatePostApi(states=states, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('assignment_config', 'invalidassignment_config'),
        ('assignment_config', ''),
        ('assignment_config', None),
        ('assignment_config.data', 'invalid'),
        ('assignment_config.data', ''),
        ('assignment_config.data.rules', ''),
        ('assignment_config.data.rules', 'invalid'),
        ('assignment_config.data.rules.0.roi.vertices.0.x', -1),
        ('assignment_config.data.rules.0.roi.vertices.0.x', 2),
        ('assignment_config.data.rules.0.roi.vertices.0.y', -1),
        ('assignment_config.data.rules.0.roi.vertices.0.y', 2),
        ('assignment_config.data.rules.0.roi.vertices', [{"x": 0, "y": 0}]),
        # ('assignment_config.data.rules.0.roi.vertices', []), # TODO
        ('rotate_config', 'invalidrotate_config'),
        ('rotate_config', ''),
        ('rotate_config.retention.day', 31),
        ('rotate_config.retention.day', 0),
        ('rotate_config.retention.day', -1),
    ])
    def test_api_RasManager_CreateAssignmentInvalidParam(self, invalidParam, config_obj, RasmanagerAideApi,
                                                         camera_info, cluster_info, DeviceApi, AideBotInfo, ext_info):
        """  CreateAssignment 为指定的 device 创建 bot_assignment(推理能... """
        device_id = DeviceApi.createDeviceWithRTSP(AideBotInfo.deviceKindName, camera_info, cluster_info)
        assignment_config = {
            "data": {
                "rules": [
                    {
                        "roi": {
                            "vertices": [
                                {
                                    "x": 0,
                                    "y": 0
                                },
                                {
                                    "x": 1,
                                    "y": 1
                                }
                            ]
                        },
                        "rule_id": "lcrules"
                    }
                ]
            },
            "user_callback_url": "http://10.151.3.74:9999"
        }
        rotate_config = {
            "retention": {
              "day": 7
            }
        }
        intef = RasmanagerAideApi.RasManager_CreateAssignmentPostApi(device_id=device_id, assignment_config=assignment_config, rotate_config=rotate_config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()

        def clearUp():
            RasmanagerAideApi.RasManager_DeleteAssignmentPostApi(device_id)

        if ext_info:
            ext_info.addAfterFunc(clearUp)
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
    ])
    def test_api_RasManager_DeleteAssignmentInvalidParam(self, invalidParam, config_obj, RasmanagerAideApi):
        """  DeleteAssignment 移除 bot_assignment
route: prefix=r... """
        device_id = None
        intef = RasmanagerAideApi.RasManager_DeleteAssignmentPostApi(device_id=device_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
    ])
    def test_api_RasManager_DeleteDeviceInvalidParam(self, invalidParam, config_obj, RasmanagerAideApi):
        """  DeleteDevice 删除设备信息. 同时校验设备是否有使用 ras 的资源, 如果有资源绑定关... """
        device_id = None
        intef = RasmanagerAideApi.RasManager_DeleteDevicePostApi(device_id=device_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
    ])
    def test_api_RasManager_GetAssignmentInvalidParam(self, invalidParam, config_obj, RasmanagerAideApi):
        """  GetAssignment 获取 bot_assignment 的信息
route: prefix=... """
        device_id = None
        spu_name = None
        verbose = True
        intef = RasmanagerAideApi.RasManager_GetAssignmentGetApi(device_id=device_id, verbose=verbose,spu_name=spu_name, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
    ])
    def test_api_RasManager_GetDeviceDetailInvalidParam(self, invalidParam, config_obj, RasmanagerAideApi):
        """  GetDeviceDetail 获取单个设备信息, 包含设备绑定的 ras 信息.
route: p... """
        device_id = None
        intef = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.skip("错误的deviceid 会返回空列表， 不传会返回全部列表")
    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', None),
        ('verbose', 'invalidverbose'),
        ('verbose', ''),
        ('verbose', None),
    ])
    def test_api_RasManager_ListAssignmentsInvalidParam(self, invalidParam, config_obj, RasmanagerAideApi):
        """  ListAssignments 获取 bot_assignment 的列表，支持以 bot_name... """
        device_id = None
        verbose = True
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = RasmanagerAideApi.RasManager_ListAssignmentsGetApi(device_id=device_id, verbose=verbose, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [

        ('filter_with_spu', 'invalidfilter_with_spu'),
        ('filter_with_spu', ''),
    ])
    def test_api_RasManager_ListDeviceDetailsInvalidParam(self, invalidParam, config_obj, RasmanagerAideApi):
        """  ListDeviceDetails 获取设备列表, 包含设备绑定的 ras 信息.
route: p... """
        spu_name = None
        filter_with_spu = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = RasmanagerAideApi.RasManager_ListDeviceDetailsGetApi(spu_names=spu_name, filter_with_spu=filter_with_spu, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.P0
    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
    ])
    def test_api_RasManager_UpdateAssignmentInvalidParam(self, invalidParam, config_obj, RasmanagerAideApi):
        """  UpdateAssignment 更新 bot_assignment 的配置
route: pref... """
        device_id = None
        assignment_config = None
        rotate_config = None
        intef = RasmanagerAideApi.RasManager_UpdateAssignmentPostApi(device_id=device_id, assignment_config=assignment_config, rotate_config=rotate_config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('device_name', 'invaliddevice_name'),
        ('device_name', ''),
        ('device_name', None),
        ('device_desc', 'invaliddevice_desc'),
        ('device_desc', ''),
        ('device_desc', None),
        ('driver', 'invaliddriver'),
        ('driver', ''),
        ('driver', None),
        ('extra_info', 'invalidextra_info'),
        ('extra_info', ''),
        ('extra_info', None),
    ])
    def test_api_RasManager_UpdateDeviceInvalidParam(self, invalidParam, config_obj, RasmanagerApi):
        """  UpdateDevice 更新设备信息. 同时检查设备是否已经绑定 ras 资源，如果有资源绑定关系... """
        device_id = None
        device_name = None
        device_desc = None
        driver = None
        extra_info = None
        intef = RasmanagerApi.RasManager_UpdateDevicePostApi(device_id=device_id, device_name=device_name, device_desc=device_desc, driver=driver, extra_info=extra_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('message_type', 'invalidmessage_type'),
        ('message_type', ''),
        ('message_type', None),
        ('service_quota', 'invalidservice_quota'),
        ('service_quota', ''),
        ('service_quota', None),
        ('service_status', 'invalidservice_status'),
        ('service_status', ''),
        ('service_status', None),
    ])
    def test_api_RasManager_CallbackAccountPostQuotaStatusInvalidParam(self, invalidParam, config_obj, RasmanagerApi):
        """  CallbackAccountPostQuotaStatus 用来接收 bss 订单状态变化的 ca... """
        message_type = None
        service_quota = None
        service_status = None
        intef = RasmanagerApi.RasManager_CallbackAccountPostQuotaStatusPostApi(message_type=message_type, service_quota=service_quota, service_status=service_status, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200


    @pytest.mark.parametrize("invalidParam", [
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
    ])
    def test_api_RasManager_GetDataCollectingTaskInvalidParam(self, invalidParam, config_obj, RasmanagerApi):
        """  GetDataCollectingTask 根据task_id获取回流作业
route: prefi... """
        task_id = None
        intef = RasmanagerApi.RasManager_GetDataCollectingTaskGetApi(task_id=task_id, sendRequest=False)
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
    def test_api_RasManager_ListDataCollectingTaskInvalidParam(self, invalidParam, config_obj, RasmanagerApi):
        """  ListDataCollectingTask 获取回流作业列表
route: prefix=data... """
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = RasmanagerApi.RasManager_ListDataCollectingTaskGetApi(paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('cluster_id', 'invalidcluster_id'),
        ('cluster_id', ''),
        ('cluster_id', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
    ])
    def test_api_RasManager_CallbackDataCollectingTaskStatusInvalidParam(self, invalidParam, config_obj, RasmanagerApi):
        """  CallbackDataCollectingTaskStatus 设置回流作业状态.
route: ... """
        cluster_id = None
        task_id = None
        status = None
        intef = RasmanagerApi.RasManager_CallbackDataCollectingTaskStatusPostApi(cluster_id=cluster_id, task_id=task_id, status=status, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task', 'invalidtask'),
        ('task', ''),
        ('task', None),
    ])
    def test_api_RasManager_CreateDataCollectingTaskInvalidParam(self, invalidParam, config_obj, RasmanagerApi):
        """  CreateDataCollectingTask 发起回流作业.
route: prefix=dat... """
        task = None
        intef = RasmanagerApi.RasManager_CreateDataCollectingTaskPostApi(task=task, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
    ])
    def test_api_RasManager_DeleteDataCollectingTaskInvalidParam(self, invalidParam, config_obj, RasmanagerApi):
        """  DeleteDataCollectingTask 根据task_id删除回流作业
route: pr... """
        task_id = None
        intef = RasmanagerApi.RasManager_DeleteDataCollectingTaskPostApi(task_id=task_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('spu_names', 'invalidspu_names'),
        ('spu_names', ''),
        ('spu_names', None),
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
    def test_api_RasManager_ListAllDeviceDetailsInvalidParam(self, invalidParam, config_obj, RasmanagerApi):
        """  ListAllDeviceDetails 获取所有 account 的设备列表, 包含设备绑定的 r... """
        spu_names = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        intef = RasmanagerApi.RasManager_ListAllDeviceDetailsGetApi(spu_names=spu_names, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200
