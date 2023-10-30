import os
import pytest
from pytest_check import check

from commonlib import config, time_utils, sign_utils
from commonlib.api_lib.base_api import BaseApi
from commonlib.log_utils import log


class TestAideScenario(object):
    """ Adapter scenario test"""

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

    def test_scenario_000_ViperCheck(self, config_obj, ViperopenapiApi, ):
        res = ViperopenapiApi.create_NewDb()
        assert res.status_code == 200
        db_id = res.json["db_id"]

    # assginment层面创建老人跌倒Bot，curd
    # 12.6pass
    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_aide_assginment_crud(self, RasmanagerAideApi, config_obj, DeviceApi, deviceKindAide, cluster_info,
                                           camera_info,AideCallbackAddress1,AideBotInfo,user_info):
        """ 海目assginmentCRUD流程"""
        # 用这个能创建出海目的设备
        i=1
        camera_info = config_obj.Clients.SubDevice.camera2  # 摔倒长视频
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        spu_name = AideBotInfo.spu_name
        spu_display_name = AideBotInfo.spu_display_name
        # 1.创建设备device = device1
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
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
            "user_callback_url": AideCallbackAddress1
        }
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        resp = RasmanagerApi.createAssignment(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code == 200
        #拿到了assginment_id
        assignment_id = resp.json_get("assignment.assignment_id")
        assert resp.json_get("assignment.spu_name") == spu_name
        assert resp.json_get("assignment.account_id") == user_info.account_id
        assert resp.json_get("assignment.device_id") == device_id
        assert resp.json_get("assignment.assignment_config") == assignment_config
        assert resp.json_get("assignment.rotate_config") == rotate_config
        assert resp.json_get("assignment.state")=='AS_EL_PENDING'

        #查询到任务等于running为止,这个如果执行完了报错，说明２分钟之内没查到
        resp=RasmanagerAideApi.getAssignmentsUntilRunning(device_id=device_id)

        # 查询该bot下的所有的assignment list
        device_id = device_id
        paging_offset = None
        paging_limit = 100
        paging_total = None
        resp = RasmanagerAideApi.RasManager_ListAssignmentsGetApi(device_id=device_id, paging_offset=paging_offset,
                                                                  paging_limit=paging_limit,
                                                                  paging_total=paging_total)

        #理论上列表返回的第一个就是刚创建的assginment
        assert resp.status_code == 200
        assert resp.json_get("assignments.0.assignment_id")==assignment_id
        assert resp.json_get("assignments.0.spu_name") == spu_name
        assert resp.json_get("assignments.0.account_id")  == user_info.account_id
        assert resp.json_get("assignments.0.device_id") == device_id
        assert resp.json_get("assignments.0.assignment_config") == assignment_config
        assert resp.json_get("assignments.0.rotate_config") == rotate_config

        # #查询到任务等于running为止,这个如果执行完了报错，说明２分钟之内没查到
        # resp=RasmanagerAideApi.getAssignmentsUntilRunning(device_id=device_id)


        # assignments = RasmanagerAideApi.getAllAssignments()
        # assginment_list = []
        # for i in assignments:
        #     assginment_list.append(i["assignment_id"])
        # assert assginment_id in assginment_list
        #
        # # 更新assignment，rotate_config_update
        # rotate_config_update = {
        #     "retention": {
        #         "day": 1
        #     }
        # }
        # assignment_config_update = {
        #     "data": {
        #         "rules": [
        #             {
        #                 "roi": {
        #                     "vertices": [
        #                         {
        #                             "x": 0,
        #                             "y": 0
        #                         },
        #                         {
        #                             "x": 0.9,
        #                             "y": 0.9
        #                         }
        #                     ]
        #                 },
        #                 "rule_id": "b"
        #             }
        #         ]
        #     }
        # }
        # resp = RasmanagerAideApi.RasManager_UpdateAssignmentPostApi(device_id=device_id,
        #                                                             assignment_config=assignment_config_update,
        #                                                             rotate_config=rotate_config_update)
        # i = 1
        # assert resp.status_code == 200
        # assert resp.json["error"] == None
        #
        # # 修改后再次查询
        # # 查询该bot下的所有的assignment list
        # device_id = device_id
        # paging_offset = None
        # paging_limit = 100
        # paging_total = None
        # resp = RasmanagerAideApi.RasManager_ListAssignmentsGetApi(device_id=device_id, paging_offset=paging_offset,
        #                                                           paging_limit=paging_limit,
        #                                                           paging_total=paging_total)
        #
        # assert resp.status_code == 200
        # i = 1
        # assert resp.json_get("assignments")[0]["rotate_config"] == rotate_config_update
        # assert resp.json_get("assignments")[0]["assignment_config"] == assignment_config_update
        #
        # resp.json_get("assignments")[0]["state"] == "'AS_EL_PENDING'"
        #
        # #查询到任务等于running为止,这个如果执行完了报错，说明２分钟之内没查到
        # resp=RasmanagerAideApi.getAssignmentsUntilRunning(device_id=device_id)
        #
        # # 删除
        # # 删除assignment
        # # resp = RasmanagerAideApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
        # # assert resp.status_code == 200
        # # # 查询assignment
        # # resp = RasmanagerAideApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=None)
        # # assert resp.status_code == 404
        # # # 在所有list里面查询
        # # assignments = RasmanagerAideApi.getAllAssignments()
        # # assginment_list = []
        # # for i in assignments:
        # #     assginment_list.append(i["assignment_id"])
        # # assert assginment_id not in assginment_list

    # 有bug，1.16pass
    def test_scenario_aide_assginment_delete_all_assginment(self, RasmanagerAideApi):
        # 查询所有assginment
        assignments = RasmanagerAideApi.getAllAssignments()
        device_id_list = []
        for device_id in assignments:
            device_id_list.append(device_id["device_id"])
        # 删除所有assignemtn
        for device_id in device_id_list:
            resp = RasmanagerAideApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
            assert resp.status_code == 200
        assignments = RasmanagerAideApi.getAllAssignments()
        assert len(assignments) == 0


