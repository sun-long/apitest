#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
from commonlib.ocr_demo import rtsp_check


class TestRasTool(object):
    """ Ras工具代码"""

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

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_DeleteAllAssignment(self, RasmanagerAideApi, RasmanagerEasyBotApi):
        """  删除所有海目的Assignment"""
        RasmanagerApi = RasmanagerAideApi # 切换bot
        is_delete_device = True # 是否删除设备
        device_id = None
        assignmentList = RasmanagerApi.getAllAssignments(device_id=device_id,print_log=True)
        res_list = []
        res_device_list = []
        delete_device_list = []
        for i, assignment in enumerate(assignmentList):
            # if i > 3:
            #     break
            device_id = assignment["device_id"]
            resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id)
            if resp.status_code == 200:
                device_name = resp.json_get("device_detail.device.name")
                ingress_status = resp.json_get("device_detail.device.driver.ingresses.0.status")
            else:
                device_name = "Not Found"
                ingress_status = ""
            # -----可以在这里加删除的条件判断-----
            # if device_name.startswith("waDevice") and ingress_status or True:
            if device_name.startswith("aide_adapter") and ingress_status or True:
            # -----可以在这里加删除的条件判断-----
                resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
                delete_device_list.append(device_id)
                res_list.append("[%s][DeleteAssignment]deviceID:%s, status:%s" % (ingress_status,device_id, resp.status_code))
        if is_delete_device:
            for device_id in delete_device_list:
                resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id)
                res_device_list.append("[DeleteDevice]deviceID:%s, status:%s" % (device_id, resp.status_code))

        for x in res_list:
            log().info(x)
        for x in res_device_list:
            log().info(x)

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_DeleteAllDevice(self, RasmanagerApi):
        """ 删除所有未绑定设备，忽略已绑定的设备"""
        spu_names = None
        device_list = RasmanagerApi.getAllDeviceDetail(spu_names=spu_names,
                                                       filter_with_spu=None, print_log=True)
        res_list = []
        for i, device in enumerate(device_list):
            device_id = device["device"]["id"]
            device_name = device["device"]["name"]
            # -----可以在这里加删除的条件判断-----
            # if device_name.startswith("waDevice") or device_name.startswith("device"):
            if device_name.startswith("aide_adapter") or True:
            # -----可以在这里加删除的条件判断-----
                resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id)
                res_list.append("[DeleteDevice]deviceID:%s, deviceName:%s, status:%s" % (device_id, device_name, resp.status_code))

        for x in res_list:
            log().info(x)

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_ListAllDevice(self, RasmanagerApi):
        """ 查询所有设备状态，绑定关系"""
        spu_names = None
        device_list = RasmanagerApi.getAllDeviceDetail(spu_names=spu_names,
                                                       filter_with_spu=None, print_log=True)
        res_list = []
        for i, device in enumerate(device_list):
            device_id = device["device"]["id"]
            device_name = device["device"]["name"]
            spus = device["spus"]
            # -----可以在这里加删除的条件判断-----
            if device_name.startswith("waDevice"):
            # -----可以在这里加删除的条件判断-----
                res_list.append("[%s][%s][bind:%s]" % (device_id, device_name, spus))

        for x in res_list:
            log().info(x)

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_ListAllAssignment(self, RasmanagerAideApi, RasmanagerEasyBotApi):
        """  查询所有海目的Assignment"""
        RasmanagerApi = RasmanagerAideApi # 切换bot
        device_id = None
        assignmentList = RasmanagerApi.getAllAssignments(device_id=device_id,print_log=True)
        res_list = []
        for i, assignment in enumerate(assignmentList):
            device_id = assignment["device_id"]
            assignment_id = assignment["assignment_id"]
            resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id, print_log=False)
            if resp.status_code == 200:
                device_name = resp.json_get("device_detail.device.name")
                ingress_status = resp.json_get("device_detail.device.driver.ingresses.0.status")
            else:
                device_name = "Not Found"
                ingress_status = ""
            # -----可以在这里加删除的条件判断-----
            if device_name.startswith("waDevice") or True:
            # -----可以在这里加删除的条件判断-----
                res_list.append("[%s][ingressStatus:%s][deviceID:%s][assignment_id:%s][deviceName:%s]" % (i, ingress_status, device_id,assignment_id,device_name))
        for x in res_list:
            log().info(x)

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_GetAssignmentState(self, config_obj, RasmanagerAideApi, RasmanagerEasyBotApi):
        """  查询Assignment的状态"""
        RasmanagerApi = RasmanagerAideApi
        device_id = "b882624d494048f6bc6e2759ebc9390b"
        spu_name = None
        while True:
            resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=spu_name, print_log=False)
            assert resp.status_code == 200
            log().info("%s" % resp.json_get("assignment.state"))
            time.sleep(2)

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_createRTSPDevice(self, config_obj, DeviceApi, RasmanagerAideApi, cluster_info, AideBotInfo):
        """ 创建设备"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName # 设备类型id

        camera_info = config_obj.Clients.SubDevice.aide1 # live555模拟流
        # camera_info = config_obj.Clients.SubDevice.camera1 # 真实摄像头
        device_id_list = []
        for i in range(1):
            deviceName = None  # deviceName 支持默认不填,如需填写，不能重复
            device_id = DeviceApi.createDeviceWithRTSP(deviceKindName,
                                                       camera_info,
                                                       cluster_info,
                                                       name=deviceName,
                                                       is_delete=False # 控制是否自动删除
                                                       )
            device_id_list.append(device_id)
        for i in device_id_list:
            log().info("new deviceID:%s" % device_id)

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_createAideAssignment(self, config_obj, RasmanagerAideApi, DeviceApi,
                                       AideBotInfo, camera_info, cluster_info):
        """ 创建Assignment	"""
        res_list = []
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName

        camera_info = config_obj.Clients.SubDevice.aide1  # live555模拟流
        # camera_info = config_obj.Clients.SubDevice.camera1 # 真实摄像头

        for i in range(1):
            # 创建设备device
            deviceName = None
            device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info, name=deviceName,
                                                       is_delete=False)
            # 绑定设备
            resp = RasmanagerApi.createAssignment(device_id, is_delete=False)
            assert resp.status_code == 200
            time.sleep(2)
            # resp = RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)
            # # 查询bot及设备绑定关系
            # resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=True)
            # assert resp.status_code == 200
            # assert resp.json_get("assignment.state") == 'AS_EL_RUNNING'
            # assert resp.json_get("assignment.device_id") == device_id
            # status = resp.json_get("assignment.state")
            # res_list.append("[%s]%s" % (device_id, status))

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_GetDeviceDetail(self, config_obj, RasmanagerEasyBotApi):
        """ 查询一个设备"""
        device_id = ''
        resp = RasmanagerEasyBotApi.RasManager_GetDeviceDetailGetApi(device_id=device_id)
        assert resp.status_code == 200

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_GetAssignment(self, config_obj, RasmanagerAideApi):
        """  查询一个Assignment"""
        device_id = ""
        spu_name = None
        resp = RasmanagerAideApi.RasManager_GetAssignmentGetApi(device_id=device_id, spu_name=spu_name)
        assert resp.status_code == 200
        log().info("%s" % resp.json_get("assignment.state"))

    # @pytest.mark.skip("工具,默认跳过")
    def test_tool_createLiveTaskWithRtsp(self, VideomanagerApi, config_obj, DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 视频直播crd"""
        is_delete = False
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info=camera_info, cluster_info=cluster_info, is_delete=is_delete)
        # 2.创建视频任务
        resp = VideomanagerApi.createTask(device_id=None, is_delete=is_delete)
        task_id = resp.json_get("task.id")
        i=1

        # 3. 查询任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id])
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.id") == task_id
        # 4.生成播放地址
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id,protocol="RTMP",duration="NO_EXPIRED")
        assert resp.status_code == 200
        url = resp.json_get("url")

        # save_path = os.path.join(config.temp_path, "test.jpg")
        # if os.path.exists(save_path):
        #     os.remove(save_path)
        # try:
        #     rtsp_check.get_img_from_camera_net_1(url, save_path)
        # except Exception as e:
        #     assert None, "解析生成播放地址失败"
        # assert os.path.exists(save_path), "%s 未生成视频图片" % save_path

        log().info("url:%s" % url)

    def test_tool_deleteAllTask(self, config_obj, VideomanagerApi):
        """  删除所有视频直播任务"""
        task_list = VideomanagerApi.getAllTask()
        for task in task_list:
            task_id = task["id"]
            resp = VideomanagerApi.VideoManagerCenter_DeleteTaskPostApi(task_id=task_id)
            assert resp.status_code == 200

    def test_tool_getAllTask(self, config_obj, VideomanagerApi, internalLoginToken):
        """  查询所有视频直播任务"""
        task_list = VideomanagerApi.getAllTask()
