#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from pytest_check import check

from commonlib import config, time_utils, sign_utils, config_utils, utils
from commonlib.log_utils import log


class TestEdgeScenario(object):
    """ Edge scenario test"""

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

    def test_scenario_000_subDeviceCRUD(self, EdgeApi, client_info, camera_info):
        """ 一个完整的crud测试用例"""
        # crud:
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
            "device_id": device_id,  # 存在=>更新, 不存在=>创建
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

        resp = EdgeApi.NebulaIOTAgentSrv_UpsertSubDevicePostApi(subdevice=subdevice)

        assert resp.status_code == 200
        assert resp.json_get("code") == 0
        assert resp.json_get("subdevice.device_id") == device_id

        resp = EdgeApi.NebulaIOTAgentSrv_GetSubDeviceByIDGetApi(device_id)
        assert resp.status_code == 200
        assert resp.json_get("code") == 0
        assert resp.json_get("subdevice.device_id") == device_id

        resp = EdgeApi.NebulaIOTAgentSrv_RemoveSubDeviceByIDDeleteApi(device_id)
        assert resp.status_code == 200

        resp = EdgeApi.NebulaIOTAgentSrv_GetSubDeviceByIDGetApi(device_id)
        assert resp.status_code == 400

    def test_scenario_001_readConfigObjInfo(self, EdgeApi, config_obj):
        """ 读取configObj中指定key的值"""
        cloud_host = config_obj.EnvInfo.NebulaCloud.Service
        client_ec1 = config_obj.Clients.Aiot.ec1
        log().info(cloud_host)
        log().info(client_ec1)

    def test_scenario_002_saveJsonFile(self, EdgeApi, config_obj):
        """ 如何保存临时json文件"""
        resp = EdgeApi.NebulaIOTAgentSrv_ListAllSubDevicesGetApi()
        utils.save_json_file('temp', resp.json)

    def test_scenario_003_assertMethod(self, EdgeApi, config_obj):
        """ 断言的两种方法"""
        # 不抛出异常, 代码可以继续执行, 同时代码执行后,能够提示验证失败
        # pytest.assume(1 == 2, "1不等于2")
        # log().info("pytest.assume:程序继续进行")
        with check: assert 1 == 2, "1不等于2"
        log().info("with check:1不等于2")
        # 抛出异常,代码不会继续执行,该case结束
        assert 1 == 2, "1不等于2"
        log().info("assert:程序继续进行")

    @pytest.mark.skip(msg='跳过测试')
    def test_scenario_004_skip(self):
        """ 跳过测试"""
        # 跳过测试的方法: 在case前添加@pytest.mark.skip(msg='')
        pass

    def test_scenario_005_skip_in_case(self):
        """ 代码中跳过该测试用例"""
        if 1 != 2:
            pytest.skip(msg='skip case!')

    def test_scenario_006_todo(self):
        """ todo的用法"""
        # 当某个功能还没写完,或者需要后期完成,作为提醒使用
        # TODO: 后期完成该测试用例
        pass

    @pytest.mark.repeat(4)
    def test_scenario_006_repeat(self):
        """ 重复执行"""
        "https://blog.csdn.net/Tangerine02/article/details/122960553"
        log().info("11111111111")

    @pytest.mark.parametrize('test_input,expected', [('3+5', 8), ('2-1', 1), ('7*5', 30)])
    def test_scenario_006_parametrize1(self, test_input, expected):
        """ 参数化举例1"""
        assert eval(test_input) == expected  # eval把字符串转换成表达式

    # indirect=True是把login当作函数去执行
    @pytest.mark.parametrize('edgeLogin', [
        {"user_name": "admin", "password": "1cb20016275914a448c19f89c92e8b00ba773d76af7b1961a360d94574bbe35b"},
        {"user_name": "wang", "password": "123"},
    ], indirect=True)
    def test_scenario_006_parametrize2(self, edgeLogin):
        """ 参数化举例2 登录"""
        log().info("token:%s" % edgeLogin)

    @pytest.mark.parametrize('logName', ['aaa', 'bbb', 'ccc'], indirect=True)
    @pytest.mark.parametrize('edgeLogin', [
        {"user_name": "admin", "password": "1cb20016275914a448c19f89c92e8b00ba773d76af7b1961a360d94574bbe35b"},
        {"user_name": "wang", "password": "123"},
    ], indirect=True)
    def test_scenario_006_parametrize3(self, edgeLogin, logName):
        """ 参数化举例3 登录,获取不同的logName 3*2 """
        # 另一个更实际的例子 test_scenario_000_subDeviceCRUD
        log().info("token:%s" % edgeLogin)
        log().info("logName:%s" % logName)

    def test_scenario_006_base64(self, EdgeApi):
        """ 图片转化为base64"""
        image_path = "go_image/facebody.jpg"
        image_path = os.path.join(config.image_path, image_path)
        big_pic = EdgeApi.imageToBase64(image_path)
        log().info(big_pic)

    # learn 6 host_map 路径后缀
    def test_scenario_007_getDeviceInfoFromClient(self, EdgeApi, config_obj, CloudApi):
        """ 获取云侧device信息"""
        resp = EdgeApi.NebulaIOTAgentSrv_GetSerialNumberGetApi()
        assert resp.status_code == 200
        serial_number = resp.json_get("serial_number")

        resp = EdgeApi.NebulaIOTAgentSrv_GetLicenseStateGetApi()
        assert resp.status_code == 200
        nebula_registry = resp.json_get("license.nebula_registry")

        ak = nebula_registry
        device_sn = serial_number
        resp = CloudApi.NebulaIOTSrv_GetDeviceBySNGetApi(ak, device_sn)
        assert resp.status_code == 200

        log().info("ak:%s" % ak)
        log().info("sn:%s" % device_sn)
        log().info("device_id:%s" % resp.json_get("device.device.metadata.device_id"))