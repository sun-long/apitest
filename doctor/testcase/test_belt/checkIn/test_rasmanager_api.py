#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import pytest
from commonlib.log_utils import log


@pytest.mark.checkin
@pytest.mark.rasManager
class TestRasmanagerApi(object):
    """ rasManager Api测试"""

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

    def test_api_RasManager_CountDevices(self, config_obj, RasmanagerApi, AideBotInfo):
        """  CountDevices 返回 account 下的 device 总数."""
        spu_names = None
        resp = RasmanagerApi.RasManager_CountDevicesGetApi(spu_names=spu_names)
        assert resp.status_code == 200

    def test_api_RasManager_CreateAideAssignment(self, config_obj, RasmanagerAideApi, AideCallbackAddress1):
        """  CreateAssignment 为指定的 device 创建 bot_assignment"""
        user_callback_url = AideCallbackAddress1
        device_id = "1c6dfff3b46b416cae0c2a1543fa6275"
        assignment_config = {
            "data": {
                "rules": [{
                    "roi": {
                        "vertices": [{
                            "x": 0,
                            "y": 0
                        },
                            {
                                "x": 1,
                                "y": 1
                            }
                        ]
                    },
                    "rule_id": "a",
                }]
            },
            "user_callback_url": user_callback_url
        }
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        resp = RasmanagerAideApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                    assignment_config=assignment_config,
                                                                    rotate_config=rotate_config)
        assert resp.status_code == 404
        assert resp.json_get("error.message") == "device not found"

    def test_api_RasManager_DeleteAideAssignment(self, config_obj, RasmanagerAideApi):
        """  DeleteAssignment 移除 bot_assignment"""
        device_id = "fd59a9302e1e48ff9a41f6485c992099"
        resp = RasmanagerAideApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
        assert resp.status_code == 404
        assert resp.json_get("error.message") == "device not found"

    def test_api_RasManager_DeleteDevice(self, config_obj, RasmanagerAideApi):
        """  DeleteDevice 删除设备信息."""
        device_id = "1e3edcd56ec34a77b14456b2b60bfc4f"
        resp = RasmanagerAideApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code == 404
        assert resp.json_get("error.message") == "device not found"

    def test_api_RasManager_GetAssignment(self, config_obj, RasmanagerAideApi):
        """  GetAssignment 获取 bot_assignment 的信息 """
        device_id = "b882624d494048f6bc6e2759ebc9390b"
        spu_name = None
        resp = RasmanagerAideApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=spu_name)
        assert resp.status_code == 404
        assert resp.json_get("error.message") == "device not found"

    def test_api_RasManager_GetDeviceDetail(self, config_obj, RasmanagerAideApi):
        """  GetDeviceDetail 获取单个设备信息, 包含设备绑定的 ras 信息."""
        device_id = '34905d69dfb94908a5fd1f3671d5b5ac'
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 404
        assert resp.json_get("error.message") == "device not found"

    def test_api_RasManager_ListAssignments(self, config_obj, RasmanagerAideApi):
        """  ListAssignments 获取 bot_assignment 的列表，"""
        device_id = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = RasmanagerAideApi.RasManager_ListAssignmentsGetApi(device_id=device_id, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_RasManager_ListDeviceDetails(self, config_obj, RasmanagerAideApi):
        """  ListDeviceDetails 获取设备列表, 包含设备绑定的 ras 信息."""
        spu_names = None
        filter_with_spu = False
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = RasmanagerAideApi.RasManager_ListDeviceDetailsGetApi(spu_names=spu_names, filter_with_spu=filter_with_spu, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_RasManager_UpdateAssignment(self, config_obj, RasmanagerAideApi):
        """  UpdateAssignment 更新 bot_assignment 的配置"""
        device_id = None
        assignment_config = None
        rotate_config = None
        resp = RasmanagerAideApi.RasManager_UpdateAssignmentPostApi(device_id=device_id, assignment_config=assignment_config, rotate_config=rotate_config)
        assert resp.status_code == 400
        assert resp.json_get("error.message") == "device_id is required"


    def test_api_RasManager_CreateDataCollectingTask(self, config_obj, RasmanagerAideApi):
        """  创建数据回流任务... """
        resp = RasmanagerAideApi.RasManager_CreateDataCollectingTaskPostApi(task={})
        assert resp.status_code == 400
        assert resp.json_get("error.code")==3
        assert resp.json_get("error.message") == "data collecting auth id is required"

    def test_api_RasManager_GetDataCollectingTask(self, config_obj, RasmanagerAideApi):
        """  查询数据回流任务... """
        resp = RasmanagerAideApi.RasManager_GetDataCollectingTaskGetApi(task_id=None)
        assert resp.status_code != 200
        assert resp.json_get("error.message") == "data collecting task id is required"

    def test_api_RasManager_DeleteDataCollectingTask(self, config_obj, RasmanagerAideApi):
        """  删除数据回流任务... """
        resp = RasmanagerAideApi.RasManager_DeleteDataCollectingTaskPostApi(task_id="")
        assert resp.status_code == 400
        assert resp.json_get("error.code")==3
        assert resp.json_get("error.message") == "data collecting task id is required"

    def test_api_RasManager_GetDataCollectingTaskNull(self, config_obj, RasmanagerAideApi):
        """  根据task_id查询数据回流任务... """
        resp = RasmanagerAideApi.RasManager_GetDataCollectingTaskGetApi(task_id=" ")
        assert resp.status_code == 404
        assert resp.json_get("error.code") == 5
        assert resp.json_get("error.message") == "data_collecting_task is not found"

    def test_api_RasManager_ListDataCollectingTask(self, config_obj, RasmanagerAideApi):
        """  查询数据回流任务list... """
        resp = RasmanagerAideApi.RasManager_ListDataCollectingTaskGetApi(paging_offset=-1)
        assert resp.status_code == 200
        assert len(resp.json_get("tasks")) == 0


    def test_api_RasManager_ListAllDeviceDetailsGetApi(self, config_obj, RasmanagerAideApi):
        """  获取设备列表... """
        resp = RasmanagerAideApi.RasManager_ListAllDeviceDetailsGetApi(spu_names=None)
        assert resp.status_code == 400
        assert resp.json_get("error.message") == "spu_name is required"

    def test_api_RasManager_UpdateDevice(self, config_obj, RasmanagerAideApi):
        """  UpdateDevice 更新设备信息. 同时检查设备是否已经绑定 ras 资源，如果有资源绑定关系... """
        device_id = "1234"
        name = None
        desc = None
        driver = None
        extra_info = None
        resp = RasmanagerAideApi.RasManager_UpdateDevicePostApi(device_id=device_id, name=name, desc=desc, driver=driver, extra_info=extra_info)
        assert resp.status_code == 404
        assert resp.json_get("error.details.0.message") == "device not found"

    def test_api_RasManager_ListAccountDeviceSpus(self, config_obj, RasmanagerAideApi):
        """  ListAccountDeviceSpus 获取 account 下所有 device 订阅的 sp... """
        resp = RasmanagerAideApi.RasManager_ListAccountDeviceSpusGetApi()
        assert resp.status_code == 200
