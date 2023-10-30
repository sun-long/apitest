#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import os
import time

import pytest
from pytest_check import check

from commonlib import config, time_utils, sign_utils, utils_websocket, utils
from commonlib.log_utils import log


class TestCloudScenario(object):
    """ Cloud scenario test"""

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

    # learn_7  异步测试, wait方法 callback方法 pytest.assume
    def test_scenario_NebulaIOTSrv_CreateSubDevice(self, config_obj, CloudApi, deviceInfo, camera_info):
        """  异步接口测试举例 """
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
        request_id = resp.json_get("header.trace.requestid")
        log().info("subDeviceId=>%s" % subDeviceId)
        log().info("requestid=>%s" % request_id)

        def callback_func():
            CloudApi.getOplogByRequestId(ak, device_id, request_id, desc="CreateSubDeviceOplog")

        resp = CloudApi.getSubDeviceByIDUntilFound(ak, device_id, subDeviceId, call_back=callback_func)
        assert resp.status_code == 200
        assert resp.json_get("state_sub_device.device_id") == subDeviceId

    def test_scenario_NebulaIOTSrv_RemoveAllSubDevice(self, config_obj, CloudApi, deviceInfo):
        """ 移除所有子设备 异步等待"""
        ak = deviceInfo["ak"]
        device_id = deviceInfo["device_id"]
        resp = CloudApi.NebulaIOTSrv_GetSubDevicesGetApi(ak, device_id)
        subDeviceList = resp.json_get("state_sub_devices")
        delete_list = []
        for subDevice in subDeviceList:
            subDeviceId = subDevice["device_id"]
            resp = CloudApi.NebulaIOTSrv_RemoveSubDeviceDeleteApi(ak, device_id, subDeviceId)
            if resp.status_code == 200:
                delete_list.append(subDeviceId)
            time.sleep(0.1)

        for subDeviceId in delete_list:
            CloudApi.getSubDeviceByIDUntilNotFound(ak, device_id, subDeviceId)

        resp = CloudApi.NebulaIOTSrv_GetSubDevicesGetApi(ak, device_id)
        log().info("当前子设备数量:%s" % len(resp.json_get("state_sub_devices")))

    def test_scenario_bizapp_websoket_check(self, config_obj, edgeLogin, client_info):
        """ 这是一个websoket的demo"""
        url = 'wss://%s:5043/v1/callback/websocket' % client_info.ip  # websocket地址
        token = "Bearer %s" % edgeLogin  # websocket需要token认证
        send_req = '{"types":["RECORD_OUTPUT_RESULT"]}'  # websocket需要发送请求告知要获取记录数据
        wsc = utils_websocket.WebSocketClient(url, token=token, send_req=send_req)
        wsc.start()  # 开始接受
        # 这里可以启动任务,开始向websocket推送数据啦
        # 这里可以启动任务,开始向websocket推送数据啦
        # 这里可以启动任务,开始向websocket推送数据啦
        _len = len(wsc.received_data_list)
        wsc.ws.send()
        while True:
            if len(wsc.received_data_list) > _len:
                break
            time.sleep(1)
        ret = wsc.received_data_list[-1]
        ret = ret.pb_sexxxxstring()
        assert ret[xxx] == 0



        time.sleep(120)
        wsc.stop() # 停止接受
        received_data_list = wsc.received_data_list  # 获取接受到的数据

        # 以下这一步是去重, 因为websocket不区分任务的, 这个步骤我就注释啦,按需处理
        received_list = received_data_list
        # received_list = [info["Content"]["RecordOutputResult"] for info in received_data_list if
        #                  info["Content"]["RecordOutputResult"]["task_id"] == task_ids[0]]
        with check: assert (len(received_list) > 0, "websoket查询记录为空")

        # 接下来就可以逐条验证了每条里的各个字段是否与预期的一致啦

    def test_scenario_bizapp_websoket_check_batch(self, config_obj, edgeLogin, client_info):
        """ 这是一个多websocket的例子"""
        batch_num = 3
        websoket_num = 2
        test_time = 120  # 测试时间
        offset_time = 300  # 任务执行完后的等待时间
        url = 'wss://%s:5043/v1/callback/websocket' % client_info.ip  # websocket地址
        token = "Bearer %s" % edgeLogin  # websoket需要token认证
        send_req = '{"types":["RECORD_OUTPUT_RESULT"]}'  # websoket需要发送请求告知要获取记录数据

        wscObj_list = []
        for x in range(websoket_num):
            wsc = utils_websocket.WebSocketClient(url, token=token, send_req=send_req)
            wsc.start()
            wscObj_list.append({"wsc": wsc})

        # 这里就是起多个任务了, 所有任务都是往同一个websocket上去发
        # 这里就是起多个任务了, 所有任务都是往同一个websocket上去发
        # 这里就是起多个任务了, 所有任务都是往同一个websocket上去发

        log().info("等待任务运行120秒")
        time.sleep(test_time)

        # 停止websocket
        for info in wscObj_list:
            info["wsc"].stop()
            # received_data_list = wsc.received_data_list

        # 以下是解析的过程, 因为是从nebula代码库copy过来的, 所有接口调用风格不同, 凑合看哈, 太多了,我就不一一改了
        # for idx, wsc_info in enumerate(wscObj_list):
        #     logging.info("##开始分析第%s个websoket结果:" % idx)
        #     received_data_list = wsc_info["wsc"].received_data_list
        #     received_list_dict = {x: {"received_list": [], "record_list": [], "error_list": []} for x in task_ids}
        #     for info in received_data_list:
        #         tid = info["Content"]["RecordOutputResult"]["task_id"]
        #         if tid in received_list_dict:
        #             received_list_dict[tid]["received_list"].append(info["Content"]["RecordOutputResult"])
        #
        #     self.logTestStep("查询记录存储")
        #     for task_id, info in received_list_dict.items():
        #         received_list = info["received_list"]
        #         record_list = self.get_all_record_by_task_id(task_id=task_id)
        #         received_list_dict[task_id]["record_list"].extend(record_list)
        #         receivedDict = {}
        #         error_list = []
        #         if len(received_list) != len(record_list):
        #             error_list.append("##[websoket_%s][%s]数量不同, websoket:record=%s:%s" % (idx, task_ids[0], len(received_list), len(record_list)))
        #
        #         check_list = ["object_id", 'portrait_image_location', 'captured_time', 'received_time', 'create_time', 'sub_device_id',
        #                       'sub_device_name', 'task_id', 'task_name', 'task_type','detect_type', 'lib_info', 'attrs', 'applet_record_type']
        #         # websoket里没有ak,
        #         # websocket接收有,而记录里没有:device_id,
        #         # 记录里有,而websocket接收里没有, event_id,record_type, roi,stacked,push_interval,applet,particular
        #         for info in received_list:
        #             receivedDict[info["id"]] = info
        #         for info in record_list:
        #             if info["id"] in receivedDict:
        #                 received_info = receivedDict[info["id"]]
        #                 for field in check_list:
        #                     if sorted(str(received_info[field]).strip().replace(' ', '')) != sorted(
        #                             str(info[field]).strip().replace(' ', '')):
        #                         error_list.append("##[%s][%s] %s不一致  websoket:record=| %s | record | %s |" % (
        #                         info["task_id"], info["id"], field,
        #                         sorted(str(received_info[field]).strip().replace(' ', '')),
        #                         sorted(str(info[field]).strip().replace(' ', ''))))
        #
        #                 # 验证图片
        #                 if "portrait_image" not in received_info or not received_info['portrait_image']:
        #                     error_list.append("##[websoket_%s][%s][%s] portrait_image字段为空" % (idx, info["task_id"], info["id"]))
        #                 if "panoramic_image" not in received_info or not received_info['panoramic_image']:
        #                     error_list.append("##[websoket_%s][%s][%s] panoramic_image字段为空" % (idx,info["task_id"], info["id"]))
        #             else:
        #                 error_list.append("##[websoket_%s][%s][%s] websoket未收到" % (idx, info["task_id"], info["id"]))
        #         for msg in error_list:
        #             logging.info(msg)
        #         received_list_dict[task_id]["error_list"].extend(error_list)
        #     for task_id, info in received_list_dict.items():
        #         error_list = info["error_list"]
        #         self.soft_assert(self.assertTrue, len(error_list) == 0, "[websoket_%s][%s]存在错误信息, 请用## grep日志" % (idx, task_id))
        #     wscObj_list[idx]["res"] = received_list_dict

        res = []
        for idx, wsc_info in enumerate(wscObj_list):
            res.append(wsc_info["res"])

        # self.biz_delete_tasks(task_ids=task_ids)

        # 最后这块是 把文件保存到本地, 会在apitest/temp/log/<本次测试时间戳>/<save_dir> 目录下生成
        utils.save_post_data('websocket_log', res, save_dir='websockets')

