
import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestErrorCodeMessage(object):
    """ 错误码测试"""

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

    # pass
    @pytest.mark.Regression
    def test_ErrorCode_CreateAssignmentNoDevice(self,  config_obj, RasmanagerAideApi,
                                                         camera_info, cluster_info, DeviceApi, AideBotInfo):
        """  CreateAssignment 为指定的 device 创建 bot_assignment(推理能... """
        #device_id = DeviceApi.createDeviceWithRTSP(AideBotInfo.deviceKindName, camera_info, cluster_info)
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
        intef = RasmanagerAideApi.RasManager_CreateAssignmentPostApi(device_id=None, assignment_config=assignment_config, rotate_config=rotate_config, sendRequest=False)
        resp = intef.request()
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason")==11203002
        assert resp.json_get("error.details.0.message") == "device_id is required"

    # pass
    @pytest.mark.Regression
    def test_ErrorCode_assignment_invalid(self, DeviceApi, config_obj, RasmanagerAideApi, AideBotInfo,
                                           cluster_info):
        """  assignment_config不填 """
        # 1.准备设备
        camera_info = config_obj.Clients.SubDevice.camera2  # 真实摄像头
        i = 1
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=None,
                                                                rotate_config=rotate_config)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 30101001
        assert resp.json_get("error.details.0.message") == "assignment invalid"

    #pass
    @pytest.mark.Regression
    def test_ErrorCode_Json_unmarshal_failed(self, DeviceApi, config_obj, RasmanagerAideApi, AideBotInfo,
                                           cluster_info):
        """  json格式不正确 """
        # 1.准备设备
        camera_info = config_obj.Clients.SubDevice.camera2  # 真实摄像头
        i = 1
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        assignment_config = {
            "data": [],
            "user_callback_url": "http://10.151.3.74:9999"
        }
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 30101004
        assert resp.json_get("error.details.0.message") == "json marshal or unmarshal failed"

    #pass
    @pytest.mark.Regression
    def test_ErrorCode_roi_not_between_0and1(self, config_obj, RasmanagerAideApi,
                                                         camera_info, cluster_info, DeviceApi, AideBotInfo, ext_info):
        """  roi不在0-1范围内 """
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
                                    "x": -1,
                                    "y": -1
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
        resp = intef.request()

        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 30101009
        assert resp.json_get("error.details.0.message") == "roi points vertex must between 0 and 1"

    # pass
    @pytest.mark.Regression
    def test_ErrorCode_roi_at_least_twopoint(self, config_obj, RasmanagerAideApi,
                                                         camera_info, cluster_info, DeviceApi, AideBotInfo, ext_info):
        """  roi至少需要２个点 """
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
        resp = intef.request()

        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 30101008
        assert resp.json_get("error.details.0.message") == "roi must have at least 2 points"

    # pass
    @pytest.mark.Regression
    def test_ErrorCode_same_device_id(self, config_obj, RasmanagerAideApi,
                                                         camera_info, cluster_info, DeviceApi, AideBotInfo, ext_info):
        """  创建任务时候deice_id重复 """
        camera_info = config_obj.Clients.SubDevice.camera2
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        assignment_config = {
            "data": {
                "rules": [{
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
                    "rule_id": "lcrules",
                }]
            },
            "user_callback_url": "http://10.4.132.35:9999"
        }
        rotate_config = {
            "retention": {
                "day": 7
            }
        }
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code == 200
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 11206001
        assert resp.json_get("error.details.0.message") == "assignment already exists"
        #assignment already exists
        #最后清理任务
        resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
        assert resp.status_code == 200

    # pass
    @pytest.mark.Regression
    def test_ErrorCode_retention_out_of_range(self, config_obj, RasmanagerAideApi,
                                                         camera_info, cluster_info, DeviceApi, AideBotInfo, ext_info):
        """  创建任务时候deice_id重复 """
        camera_info = config_obj.Clients.SubDevice.camera2
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        assignment_config = {
            "data": {
                "rules": [{
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
                    "rule_id": "lcrules",
                }]
            },
            "user_callback_url": "http://10.4.132.35:9999"
        }
        rotate_config = {
            "retention": {
                "day": 31
            }
        }
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 11203006
        assert resp.json_get("error.details.0.message") == "day is invalid, expect > 0 && <= 30"

    #pass
    @pytest.mark.Regression
    def test_ErrorCode_delete_device_when_task_running(self, config_obj, RasmanagerAideApi,
                                                         camera_info, cluster_info, DeviceApi, AideBotInfo, RasmanagerApi):
        """存在任务的时候强行删除设备"""
        camera_info = config_obj.Clients.SubDevice.camera2
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        assignment_config = {
            "data": {
                "rules": [{
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
                    "rule_id": "lcrules",
                }]
            },
            "user_callback_url": "http://10.4.132.35:9999"
        }
        rotate_config = {
            "retention": {
                "day": 30
            }
        }
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code == 200


        resp=RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 11207002
        assert resp.json_get("error.details.0.message") == "operate on device is denied, because device has subscribed spu"
        #删除任务
        resp = RasmanagerApi.RasManager_DeleteAssignmentPostApi(device_id=device_id)
        assert resp.status_code == 200
        #删除设备
        resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code == 200

    #pass
    #@pytest.mark.Regression
    @pytest.mark.skip("这个case只能在test环境跑，因为只有test环境有这个WebRTC-test的设备类型")
    def test_ErrorCode_devicekind_invalid(self, config_obj, RasmanagerAideApi,
                                                         camera_info, cluster_info, DeviceApi, AideBotInfo, RasmanagerApi):
        """输入错误的device_kind"""
        camera_info = config_obj.Clients.SubDevice.camera2
        RasmanagerApi = RasmanagerAideApi
        deviceKindName ="WebRTC-test"
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info, cluster_info)
        # 2.创建assignment
        assignment_config = {
            "data": {
                "rules": [{
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
                    "rule_id": "lcrules",
                }]
            },
            "user_callback_url": "http://10.4.132.35:9999"
        }
        rotate_config = {
            "retention": {
                "day": 30
            }
        }
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 11203005
        assert resp.json_get("error.details.0.message") == "device_kind is invalid"

    #pass
    @pytest.mark.Regression
    def test_ErrorCode_two_ingress_id(self, config_obj, RasmanagerAideApi,
                                                         camera_info, cluster_info, DeviceApi, AideBotInfo, RasmanagerApi):
        """1个设备有２个ingress"""
        camera_info = config_obj.Clients.SubDevice.camera2
        RasmanagerApi = RasmanagerAideApi
        deviceKindName = AideBotInfo.deviceKindName
        #创建一个rtsp设备,包含2个ingress"""
        name = "waDevice_%s" % time_utils.get_time_str()
        cluster = {"id": cluster_info["id"]}
        driver = {
                "enable": True,
                "ingresses": [
                    {
                        "information": {
                            "rtsp": {
                                "source_url": camera_info["rtsp"]
                            },
                            "type": camera_info["type"]
                        },
                        "name": name,
                        "description": ""
                    },
                    {
                        "information": {
                            "rtsp": {
                                "source_url": camera_info["rtsp"]
                            },
                            "type": camera_info["type"]
                        },
                        "name": name,
                        "description": ""
                    }
                ],
            }
        resp = DeviceApi.DeviceManagerCenter_CreateDeviceByKindNamePostApi(devicekind_name=deviceKindName, name=name,
                                                            cluster=cluster, driver=driver)
        assert resp.status_code == 200
        device_id = resp.json_get("device.id")

        # 2.创建assignment
        assignment_config = {
            "data": {
                "rules": [{
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
                    "rule_id": "lcrules",
                }]
            },
            "user_callback_url": "http://10.4.132.35:9999"
        }
        rotate_config = {
            "retention": {
                "day": 30
            }
        }
        resp = RasmanagerApi.RasManager_CreateAssignmentPostApi(device_id=device_id,
                                                                assignment_config=assignment_config,
                                                                rotate_config=rotate_config)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 30101003
        assert resp.json_get("error.details.0.message") == "only one ingress is support"

        resp = RasmanagerApi.RasManager_DeleteDevicePostApi(device_id=device_id)
        assert resp.status_code == 200

    #pass
    @pytest.mark.Regression
    def test_ErrorCode_LiveTaskInvalid_argument(self, VideomanagerApi, config_obj, DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 创建直播任务device_id填空"""
        # 1.创建视频任务
        resp = VideomanagerApi.VideoManagerCenter_CreateTaskPostApi(device_id=None, ingress_ids=None)
        i=1
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 11503002
        assert resp.json_get("error.message") == "video task argument invalid"

    #pass
    @pytest.mark.Regression
    def test_ErrorCode_LiveTask_device_not_exist(self, VideomanagerApi, config_obj, DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 创建直播任务device_id填空"""
        resp = VideomanagerApi.VideoManagerCenter_CreateTaskPostApi(device_id="111111", ingress_ids=None)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 11501002
        assert resp.json_get("error.message") == "device not found"

    #pass
    @pytest.mark.Regression
    def test_ErrorCode_LiveTask_task_not_exist(self, VideomanagerApi, config_obj, DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 删除任务的时候，输入不存在的task_id"""
        taksid="111"
        resp = VideomanagerApi.VideoManagerCenter_DeleteTaskPostApi(task_id=taksid)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 11501001
        assert resp.json_get("error.message") == "task not found"

    #nopass
    @pytest.mark.Regression
    def test_ErrorCode_ingress_not_found(self, VideomanagerApi, config_obj, DeviceApi, AideBotInfo, camera_info, cluster_info):
        """ 视频直播crd"""
        is_delete = True
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info=camera_info, cluster_info=cluster_info, is_delete=is_delete)
        # 2.创建视频任务
        resp = VideomanagerApi.VideoManagerCenter_CreateTaskPostApi(device_id=device_id, ingress_ids=['111'])
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 11501003
        assert resp.json_get("error.message") == "ingress not found"

    @pytest.mark.Regression
    def test_ErrorCode_Video_live_duration_invalid(self, config_obj, VideomanagerApi,
                                                                    AideBotInfo, DeviceApi, camera_info,cluster_info):
        """  duration invalid持续时间不填 """
        deviceKindName = AideBotInfo.deviceKindName
        # 1.创建设备
        device_id = DeviceApi.createDeviceWithRTSP(deviceKindName, camera_info=camera_info, cluster_info=cluster_info)
        # 2.创建视频任务
        resp = VideomanagerApi.createTask(device_id=device_id)
        task_id = resp.json_get("task.id")
        # 3. 查询任务
        resp = VideomanagerApi.VideoManagerCenter_GetTasksGetApi([task_id])
        assert resp.status_code == 200
        assert resp.json_get("tasks.0.id") == task_id

        protocol = None
        duration = None
        resp = VideomanagerApi.VideoManagerCenter_GeneratePlayAddressPostApi(task_id=task_id, protocol=protocol, duration=duration, sendRequest=True)
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.reason") == 11513004
        assert resp.json_get("error.message") == "duration invalid"

