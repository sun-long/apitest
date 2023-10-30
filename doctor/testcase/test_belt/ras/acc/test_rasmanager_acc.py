#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import os
import time

import pytest
from commonlib import config, time_utils, sign_utils, utils
from commonlib.log_utils import log
from pytest_check import check

FF_DIR = "/home/SENSETIME/wangan/belt/ff"
GT_DIR = "/home/SENSETIME/wangan/belt/gt"
RES_DIR = "/home/SENSETIME/wangan/belt/res"

RTSP_LIST = [
    "10.198.21.115",
    "10.211.41.108",
    "10.53.4.12",
    "10.53.4.176",
    "10.53.5.22",
    "10.53.6.118",
    "10.53.7.217",
]

@pytest.fixture(scope="class")
def res_list():
    return traversal_files_res()


def traversal_files():
    path = FF_DIR
    file_list = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            file_list.append(name.split(".")[0])

    print("file num:%s" % len(file_list))
    return file_list


def traversal_files_res():
    path = RES_DIR
    file_list = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if 'error' in name:
                continue
            file_list.append("_".join(name.split(".")[0].split("_")[:2]))

    print("finished file num:%s" % len(file_list))
    return file_list


def save_json(data, save_path):
    data = json.dumps(data, sort_keys=True, indent=2)
    with open(save_path, 'w') as f:
        f.write(data)
    print("文件写入成功.path:%s" % save_path)

class TestRasmanagerAcc(object):
    """ Rasmanager Acc test"""

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

    # @pytest.mark.skip("手工测试用例")
    @pytest.mark.parametrize("video_name", traversal_files())
    def test_acc_001_aide(self,  RasmanagerAideApi, DeviceApi, AideBotInfo, cluster_info, video_name, res_list):
        """ 准确性测试-执行部分"""
        if video_name in res_list:
            log().info("%s task exist. skip" % video_name)
            pytest.skip("%s task exist. skip" % video_name)
        RasmanagerApi = RasmanagerAideApi
        deviceKindId = AideBotInfo.deviceKindId
        camera_info = {
            "rtsp": 'rtsp://10.53.4.176:8554/%s.264' % video_name,
            "type": 'RTSP'
        }
        gt_file = os.path.join(GT_DIR, "%s.mp4.json" % video_name)
        gt_info = utils.read_temp_json(gt_file)
        duration = gt_info["step_1"]["result"][0]["duration"]
        delay = duration + 30
        aid = "error"
        res = {
            "name": video_name,
            "rtsp": camera_info["rtsp"],
            "gt_info": gt_info,
            "error": None,
        }
        try:
            # 1.创建设备device0
            device_id = DeviceApi.createDeviceWithRTSP(deviceKindId, camera_info, cluster_info)

            # 2.绑定设备device0到demo bot上
            resp = RasmanagerApi.createAssignment(device_id)
            assert resp.status_code == 200
            assignmentInfo = resp.json_get("assignment")
            aid = resp.json_get("assignment.assignment_id")
            s1 = time.time()
            RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)
            s2 = time.time()
            log().info("等待任务执行%ss" % delay)
            startTime = time.time()
            status = []
            keepRunning = True
            while True:
                current_time = time.time()
                if current_time - startTime > delay:
                    break
                resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id, print_log=False)
                state = resp.json_get("assignment.state")
                status.append({
                    "time": current_time,
                    "state": state
                })
                if state != "AS_EL_RUNNING":
                    keepRunning = False
                log().info("status=%s, %s/%s" % (state, round(current_time-startTime,2), delay))
                time.sleep(2)
            resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id)
            deleteSuccess = True
            if resp.status_code != 200:
                deleteSuccess = False
            log().info("[%s]运行完成.deviceid=%s" % (video_name, device_id))
            res = {
                "name": video_name,
                "device_id": device_id,
                "start_time": startTime,
                "end_time": startTime,
                "keepRunning": keepRunning,
                "deleteAssignmentSuccess": deleteSuccess,
                "status": status,
                "rtsp": camera_info["rtsp"],
                "gt_info": gt_info,
                "CreateAssignmentDelay": round(s2 - s1, 2),
                "duration": duration,
                "assignment": assignmentInfo
            }
        except Exception as e:
            res.update({"error": str(e)})
            raise
        finally:
            save_json(res, os.path.join(RES_DIR, "%s_%s.json" % (video_name, aid)))

    # @pytest.mark.skip("手工测试用例")
    @pytest.mark.parametrize("video_name", [x for x in range(100)])
    def test_acc_002_aide(self,  RasmanagerAideApi, DeviceApi, AideBotInfo, cluster_info, video_name):
        """ 准确性测试-固定流"""
        video_name = 'realCamera_%s' % video_name
        RasmanagerApi = RasmanagerAideApi
        deviceKindId = AideBotInfo.deviceKindId
        camera_info = {
            "rtsp": 'rtsp://admin:t2mksense@10.4.7.11:554',
            "type": 'RTSP'
        }
        # gt_file = os.path.join(GT_DIR, "%s.mp4.json" % video_name)
        # gt_info = utils.read_temp_json(gt_file)
        # duration = gt_info["step_1"]["result"][0]["duration"]
        duration = 90
        delay = duration + 30
        aid = "error"
        res = {
            "name": video_name,
            "rtsp": camera_info["rtsp"],
            # "gt_info": gt_info,
            "error": None,
        }
        try:
            # 1.创建设备device0
            device_id = DeviceApi.createDeviceWithRTSP(deviceKindId, camera_info, cluster_info)

            # 2.绑定设备device0到demo bot上
            resp = RasmanagerApi.createAssignment(device_id)
            assert resp.status_code == 200
            assignmentInfo = resp.json_get("assignment")
            aid = resp.json_get("assignment.assignment_id")
            s1 = time.time()
            RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)
            s2 = time.time()
            log().info("等待任务执行%ss" % delay)
            startTime = time.time()
            status = []
            deviceStatus = []
            keepRunning = True
            while True:
                current_time = time.time()
                if current_time - startTime > delay:
                    break
                resp = RasmanagerApi.RasManager_GetAssignmentGetApi(device_id, print_log=False)
                state = resp.json_get("assignment.state")
                status.append({
                    "time": current_time,
                    "state": state
                })
                if state != "AS_EL_RUNNING":
                    keepRunning = False
                resp = RasmanagerApi.RasManager_GetDeviceDetailGetApi(device_id=device_id, print_log=False)
                deviceState = resp.json_get("device_detail.device.driver.ingresses.0.status")
                deviceStatus.append({
                    "time": current_time,
                    "state": deviceState
                })
                log().info("assignment=%s, device=%s, %s/%s" % (state, deviceState, round(current_time-startTime,2), delay))
                time.sleep(2)
            resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id)
            deleteSuccess = True
            if resp.status_code != 200:
                deleteSuccess = False
            log().info("[%s]运行完成.deviceid=%s" % (video_name, device_id))
            res = {
                "name": video_name,
                "device_id": device_id,
                "start_time": startTime,
                "end_time": startTime,
                "keepRunning": keepRunning,
                "deleteAssignmentSuccess": deleteSuccess,
                "status": status,
                "rtsp": camera_info["rtsp"],
                # "gt_info": gt_info,
                "CreateAssignmentDelay": round(s2 - s1, 2),
                "duration": duration,
                "assignment": assignmentInfo
            }
        except Exception as e:
            res.update({"error": str(e)})
            raise
        finally:
            save_json(res, os.path.join(RES_DIR, "%s_%s.json" % (video_name, aid)))


    @pytest.mark.parametrize("video_name", traversal_files())
    def test_acc_003_aide(self, RasmanagerAideApi, DeviceApi, AideBotInfo, cluster_info, video_name):
        """ 准确性测试-执行部分 不删除"""
        RasmanagerApi = RasmanagerAideApi
        deviceKindId = AideBotInfo.deviceKindId
        camera_info = {
            "rtsp": 'rtsp://10.53.4.176:8554/%s.264' % video_name,
            "type": 'RTSP'
        }
        gt_file = os.path.join(GT_DIR, "%s.mp4.json" % video_name)
        gt_info = utils.read_temp_json(gt_file)
        duration = gt_info["step_1"]["result"][0]["duration"]
        delay = duration + 60
        # 1.创建设备device0
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindId, camera_info, cluster_info, is_delete=False)

        # 2.绑定设备device0到demo bot上
        assignmentConfig = None
        resp = RasmanagerApi.createAssignment(device_id, is_delete=False, assignment_config=assignmentConfig)
        assert resp.status_code == 200
        RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)
        i = 1

    @pytest.mark.parametrize("video_name", [x for x in range(7)])
    def test_acc_004_aide(self, RasmanagerAideApi, DeviceApi, AideBotInfo, cluster_info, video_name):
        """ 准确性测试-执行部分 不删除"""
        file_list = traversal_files()
        RasmanagerApi = RasmanagerAideApi
        deviceKindId = AideBotInfo.deviceKindId
        rtsp_ip = RTSP_LIST[video_name]
        camera_info = {
            # "rtsp": 'rtsp://admin:t2mksense@10.4.7.11:554',
            "rtsp": 'rtsp://%s:8554/%s.264' % (rtsp_ip, file_list[0]),
            "type": 'RTSP'
        }
        # 1.创建设备device0
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindId, camera_info, cluster_info, is_delete=False)

        # 2.绑定设备device0到demo bot上
        assignmentConfig = {
            "user_callback_url": "http://10.4.132.19:9999"
        }
        resp = RasmanagerApi.createAssignment(device_id, assignment_config=assignmentConfig, is_delete=False)
        assert resp.status_code == 200
        RasmanagerApi.getAssignmentsUntilRunning(device_id=device_id)
