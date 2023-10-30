#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#/home/SENSETIME/liangchen.vendor/git/apitest/testcase/test_belt/ras/api/test_rasmanager_api.py
import os
import time
#liangchen
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


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

    @pytest.mark.skip("内部接口")
    def test_api_RasManager_CallbackAssignmentState(self, config_obj, RasmanagerApi):
        """  内部接口，用于边缘上报 bot_assignment 的状态
route: prefix=, int... """
        states = None
        resp = RasmanagerApi.RasManager_CallbackAssignmentStatePostApi(states=states)
        assert resp.status_code == 200

    def test_api_RasManager_CallbackDataCollectingTaskStatus(self, config_obj, RasmanagerApi):
        """  CallbackDataCollectingTaskStatus 设置回流作业状态.
route: ... """
        cluster_id = None
        task_id = None
        status = None
        resp = RasmanagerApi.RasManager_CallbackDataCollectingTaskStatusPostApi(cluster_id=cluster_id, task_id=task_id, status=status)
        assert resp.status_code == 200

    def test_api_RasManager_CountDevices(self, config_obj, RasmanagerApi, AideBotInfo):
        """  CountDevices 返回 account 下的 device 总数.
route: prefi... """
        # spu_names = [AideBotInfo.spu_name]
        spu_names = None
        resp = RasmanagerApi.RasManager_CountDevicesGetApi(spu_names=spu_names)
        assert resp.status_code != 200

    def test_api_RasManager_CreateEasyBotAssignment(self, config_obj, RasmanagerEasyBotApi, RasmanagerAideApi):
        """  CreateAssignment 为指定的 device 创建 bot_assignment(推理能... """
        device_id = "ea646a7a716e4448882eacef6d70266c"
        assignment_config =  {
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
        "user_callback_url": "http://test-callback-service.crd.svc.cluster.local:9999"
    }
        rotate_config = {
        "retention": {
            "day": 70
        }
    }
        resp = RasmanagerEasyBotApi.RasManager_CreateAssignmentPostApi(device_id=device_id, assignment_config=assignment_config, rotate_config=rotate_config)
        assert resp.status_code == 200

    # 2023.2.15pass
    def test_api_RasManager_DeleteDataCollectingTask(self, config_obj, RasmanagerApi):
        """  DeleteDataCollectingTask 根据task_id删除回流作业
route: pr... """
        task_id = "c6487e89-18dd-4865-bfb1-96daf2b8d84f"
        resp = RasmanagerApi.RasManager_DeleteDataCollectingTaskPostApi(task_id=task_id)
        assert resp.status_code == 200

    #2023.2.15pass
    def test_api_RasManager_CreateDataCollectingTask(self, config_obj, RasmanagerApi):
        """  CreateDataCollectingTask 发起回流作业.
route: prefix=dat... """
        task = {
            "name": "lc001",
            "desc": "lc001_desc",
            "spu_name": "FallDetection",
            "time_config": {
                "start_date": "2023-02-10",
                "end_date": "2023-02-10",
                "windows": [
                    {
                        "start_time": 0,
                        "end_time": 86400
                    }
                ]
            },
            "target_config": {
                "target_type": 0,
                "ceph_config": {
                    "access_key": "BMK45P0SCC82M09UYZTS",
                    "secret_key": "93D8LFbUQhXc+szXEyVi8hMimNtSrSjLpnMc38pshNpoVDAJA0JAUAtG+DW1dXWJ",
                    "bucket": "monolith_t1",
                    "prefix": "belt/",
                    "protocol": "s3"
                },
                "cluster_name": "SH-Ceph1424SSD"
            },
            "data_type": 1,
            "devices": [
                "b8e8a1b3a75949afa41f3ef91ff91385"
            ],
            "auth_id": "A202211179",
            "acl": [
                {
                    "ad": "liangchen.vendor",
                    "name": "梁晨",
                    "expire_time": "2023-12-31T00:00:00.000Z"
                }
            ]
        }
        resp = RasmanagerApi.RasManager_CreateDataCollectingTaskPostApi(task=task)
        assert resp.status_code == 200

    def test_api_RasManager_DeleteAideAssignment(self, config_obj, RasmanagerAideApi):
        """  DeleteAssignment 移除 bot_assignment
route: prefix=r... """
        device_id = "c50924144eb242e3bfa0e0d85f157c93"
        resp = RasmanagerAideApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
        assert resp.status_code == 200

    def test_api_RasManager_DeleteDevice(self, config_obj, RasmanagerApi):
        """  DeleteDevice 删除设备信息. 同时校验设备是否有使用 ras 的资源, 如果有资源绑定关... """
        device_id = "575bfefa14ad4db5ba0c37831bf09d44"
        resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code == 200



    def test_api_RasManager_GetAssignment(self, config_obj, RasmanagerAideApi, RasmanagerEasyBotApi):
        """  GetAssignment 获取 bot_assignment 的信息 """
        device_id = "c7435bfcd9994ea3a7182193a0bc0401"
        spu_name = None
        verbose = True
        resp = RasmanagerAideApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=spu_name, verbose=verbose)
        assert resp.status_code == 200

    def test_api_RasManager_GetDataCollectingTask(self, config_obj, RasmanagerApi):
        """  GetDataCollectingTask 根据task_id获取回流作业
route: prefi... """
        task_id = "c6487e89-18dd-4865-bfb1-96daf2b8d84f"
        resp = RasmanagerApi.RasManager_GetDataCollectingTaskGetApi(task_id=task_id)
        assert resp.status_code == 200
        log().info("数据回流的taskid是%s" % resp.json_get("task.task_id"))

    def test_api_RasManager_GetDeviceDetail(self, config_obj, RasmanagerAideApi):
        """  GetDeviceDetail 获取单个设备信息, 包含设备绑定的 ras 信息.
route: p... """
        device_id = '3b725d83bda94183bbff3987091f1088'
        resp = RasmanagerAideApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200

    def test_api_RasManager_ListAccountDeviceSpus(self, config_obj, RasmanagerApi):
        """  ListAccountDeviceSpus 获取 account 下所有 device 订阅的 sp... """
        resp = RasmanagerApi.RasManager_ListAccountDeviceSpusGetApi()
        assert resp.status_code == 200

    # 2023.2.15pass
    @pytest.mark.Regression
    def test_api_RasManager_ListAllDeviceDetails(self, config_obj, RasmanagerApi):
        """  ListAllDeviceDetails 获取所有 account 的设备列表, 包含设备绑定的 r... """
        spu_names = "FallDetection"
        # spu_names = None
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = RasmanagerApi.RasManager_ListAllDeviceDetailsGetApi(spu_names=spu_names, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_RasManager_ListAssignments(self, config_obj, RasmanagerApi):
        """  ListAssignments 获取 bot_assignment 的列表，支持以 bot_name... """
        device_id = None
        verbose = True
        paging_offset = None
        paging_limit = None
        paging_total = None
        resp = RasmanagerApi.RasManager_ListAssignmentsGetApi(device_id=device_id, verbose=verbose, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    #2.16failed
    def test_api_RasManager_ListDataCollectingTask(self, config_obj, RasmanagerApi):
        """  ListDataCollectingTask 获取回流作业列表
route: prefix=data... """
        paging_offset = 0
        paging_limit = 100
        paging_total = 100
        resp = RasmanagerApi.RasManager_ListDataCollectingTaskGetApi(paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_RasManager_ListDeviceDetails(self, config_obj, RasmanagerApi):
        """  ListDeviceDetails 获取设备列表, 包含设备绑定的 ras 信息.
route: p... """
        # spu_names = ['FellDetective']
        # spu_names = "FallDetection"
        spu_names = None
        filter_with_spu = False
        paging_offset = None
        paging_limit = 51
        paging_total = None
        resp = RasmanagerApi.RasManager_ListDeviceDetailsGetApi(spu_names=spu_names, filter_with_spu=filter_with_spu, paging_offset=paging_offset, paging_limit=paging_limit, paging_total=paging_total)
        assert resp.status_code == 200

    def test_api_RasManager_UpdateAssignment(self, config_obj, RasmanagerAideApi,AideCallbackAddress1):
        """  UpdateAssignment 更新 bot_assignment 的配置
route: pref... """
        user_callback_url = AideCallbackAddress1
        device_id = "85815610f41d460a8a10fb3e43c80e10"
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
        resp = RasmanagerAideApi.RasManager_UpdateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code == 200

    def test_api_RasManager_UpdateDevice(self, config_obj, RasmanagerApi):
        """  UpdateDevice 更新设备信息. 同时检查设备是否已经绑定 ras 资源，如果有资源绑定关系... """
        device_id = None
        name = None
        desc = None
        driver = None
        extra_info = None
        resp = RasmanagerApi.RasManager_UpdateDevicePostApi(device_id=device_id, name=name, desc=desc, driver=driver, extra_info=extra_info)
        assert resp.status_code == 200
