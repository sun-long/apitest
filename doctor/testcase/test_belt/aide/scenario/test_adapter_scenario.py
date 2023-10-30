#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

import pytest
from pytest_check import check

from commonlib import config, time_utils, sign_utils
from commonlib.api_lib.base_api import BaseApi
from commonlib.log_utils import log


# xinfenzhi
class TestAdapterScenario(object):
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


    # 2023.3.16pass
    def test_scenario_001_Adapter_Image_CRD(self, config_obj, AdapterApi, adapter_CreateAlterDb):
        """ adapter回归image相关接口"""
        db_id = adapter_CreateAlterDb
        # 往库里插入一张图片 pass
        image1_path = os.path.join(config.image_path, 'go_image/belt/face_record.jpeg')
        image1 = AdapterApi.imageToBase64(image1_path)
        images = [
            {
                "image": {
                    "image": {
                        "data": image1
                    },
                    "face_selection": "LargestFace"
                },
                "quality_threshold": 0.3
            }
        ]
        resp = AdapterApi.BatchAddImageToDBPostApi(auto_rotation=None,
                                                   db_id=db_id,
                                                   extra_db_type="",
                                                   images=images,
                                                   save_images=True,
                                                   type="ALERT_FEATURE_DB",
                                                   loginToken=None,
                                                   sendRequest=True,
                                                   print_log=True,
                                                   interface_desc=None)

        assert resp.status_code == 200
        assert resp.json_get("results.0.status") == "OK"
        feature_id = resp.json_get("items.0.feature_id")

        # 在库里查询某一张图片pass
        resp = AdapterApi.Search_image_in_DB(db_id=db_id, image=image1)
        assert resp.status_code == 200
        assert resp.json_get("results.0.status") == 'OK'

        # 从库里删除一张图片 pass
        resp = AdapterApi.DeleteImageFromDB(feature_id=feature_id, db_id=db_id)
        assert resp.status_code == 200
        assert resp.json_get("results.0.status") == "OK"
        """ adapter回归image相关接口"""


    # 2023.3.16pass
    def test_scenario_002_Adapter_Feature(self, config_obj, AdapterApi, adapter_CreateAlterDb):
        """ adapter回归Feature相关接口"""

        db_id = adapter_CreateAlterDb
        # 往库里插入一张图片 pass
        image1_path = os.path.join(config.image_path, 'go_image/belt/face_record.jpeg')
        image1 = AdapterApi.imageToBase64(image1_path)
        resp = AdapterApi.batch_add_image(db_id=db_id, image=image1)
        feature_id = resp[2]

        # 单张图片提取特征值 pass
        resp = AdapterApi.DetectAndExtractPost(image=image1)
        assert resp.status_code == 200
        assert resp.json_get("feature.version") == 25000
        feature = resp.json["feature"]

        # 在指定静态库（单库）中进行特征1：N检索 pass
        features = [feature]
        resp = AdapterApi.AdapterFeatureBatchSearch(features=features, db_id=db_id)
        assert resp.status_code == 200
        assert resp.json["results"][0]["status"] == "OK"

        # 从库里删除一张图片 pass
        resp = AdapterApi.DeleteImageFromDB(feature_id=feature_id, db_id=db_id)
        assert resp.status_code == 200
        assert resp.json["results"][0]["status"] == "OK"

        # # 将批量特征入静态库 pass
        key = "8888"
        resp = AdapterApi.AdapterFeatureBatchAdd(feature=feature, db_id=db_id, key=key)
        assert resp.status_code == 200
        assert resp.json_get("results.0.status") == "OK"

        # 通过用户自定义key在指定静态库中批量获取特征.key可以重复(用户自定义),pass
        # 此处key是放在列表里的，需要加括号
        key = [key]
        resp = AdapterApi.AdapterFeatureBatchGetByKey(db_id=db_id, key=key)
        assert resp.status_code == 200
        assert resp.json_get("results.0.status") == "OK"


    # 2023.3.16pass
    def test_scenario_003_Adapter_Compare(self, config_obj, AdapterApi, adapter_CreateAlterDb):
        """ adapter回归image相关接口"""
        db_id = adapter_CreateAlterDb
        # 往库里插入一张图片 pass
        image1_path = os.path.join(config.image_path, 'go_image/belt/face_record.jpeg')
        image1 = AdapterApi.imageToBase64(image1_path)
        resp = AdapterApi.batch_add_image(db_id=db_id, image=image1)
        feature_id = resp[2]

        # 单张图片提取特征值 pass
        resp = AdapterApi.DetectAndExtractPost(image=image1)
        assert resp.status_code == 200
        feature = resp.json["feature"]

        # 调用图片1:1接口 pass
        resp = AdapterApi.Image_CompareOneToOne(image1=image1, image2=image1)
        assert resp.status_code == 200
        assert resp.json["score"] > 0.99

        # 特征1：1比对
        resp = AdapterApi.imageFaceExtractCompareFeature(one=feature, other=feature)
        assert resp.status_code == 200
        assert resp.json["score"] > 0.99


    # 2023.3.16pass
    def test_scenario_004_download_image(self, config_obj, AdapterApi, adapter_CreateAlterDb):
        """ adapter回归image相关接口"""
        db_id = adapter_CreateAlterDb
        # 往库里插入一张图片 pass
        image1_path = os.path.join(config.image_path, 'go_image/belt/face_record.jpeg')
        image1 = AdapterApi.imageToBase64(image1_path)
        resp = AdapterApi.batch_add_image(db_id=db_id, image=image1)
        bucket_name = resp[0]
        object_key = resp[1]

        # 以二进制形式下载 Object 数据
        resp = AdapterApi.OSGDownloadObjectGet(bucket_name=bucket_name, object_key=object_key)
        assert resp.status_code == 200
        # 下载的图片放在本机的tmp目录下
        save_path = os.path.join(config.temp_path, 'b.jpeg')
        if not os.path.exists(config.temp_path):
            os.makedirs(config.temp_path)
        if os.path.exists(save_path):
            os.remove(save_path)

        with open(file=save_path, mode="wb") as f:
            f.write(resp.origin_resp.content)

        assert sign_utils.getMd5ByFile(save_path) == sign_utils.getMd5ByFile(image1_path)

    def Totest_scenario_005_Adapter_Firetask_Check(self, config_obj, AdapterApi, ViperopenapiApi):
        # vps创建任务
        source_address = "rtsp://10.4.132.35:8554/long_fire_yancheng.264"
        resp = AdapterApi.AdapterTaskNewFire(source_address)
        task_id = resp[1]
        assert resp[0].status_code == 200

        # 查询任务
        resp = AdapterApi.AdapterTaskListGet()
        task_list = resp[1]
        assert resp[0].status_code == 200
        # 从列表里看这该任务的状态是不是已经创建成功了
        assert task_id in task_list
        for i in resp[0].json["tasks"]:
            if task_id == i["info"]["task_id"]:
                assert i["status"]["status"] == "PENDING"

        # 查询一个任务直到成功为止,这里先用viper的，回头可以注释掉
        resp = ViperopenapiApi.gettaskByIDUntilAvailable(task_id=task_id)
        assert resp.status_code == 200

        # pass

    @pytest.mark.P0
    @pytest.mark.Regression
    def test_scenario_006_Adapter_Old_Fell_Check(self, config_obj, AdapterApi, ViperopenapiApi, camera_info):
        """ adapter老人跌倒创建任务增删查"""
        # vps创建任务
        camera_info = config_obj.Clients.SubDevice.camera2
        source_address = camera_info['rtsp']
        # 这里roi可以不传也可以传四个点，不要传２个点,传2个点不报错，但是没有告警
        roi = {
            "vertices": [
                {
                    "x": 0,
                    "y": 0
                },
                {
                    "x": 1,
                    "y": 0
                },
                {
                    "x": 1,
                    "y": 1
                },
                {
                    "x": 0,
                    "y": 1
                }
            ]
        }
        resp, task_id = AdapterApi.AdapterTaskNewOldFell(source_address, roi=roi)
        assert resp.status_code == 200

        # 查询任务
        resp, task_list = AdapterApi.AdapterTaskListGet()
        assert resp.status_code == 200
        # 判断新建的这个任务是否在task_list里
        assert task_id in task_list

        # 查询一个任务直到成功为止(状态变成OK)
        AdapterApi.getAdaptertaskByIDUntilAvailable(task_id=task_id)

        # # vps删除这个任务
        # resp = AdapterApi.AdapterDeleteSignaltask(task_id=task_id)
        # assert resp.status_code == 200
        #
        # vps删除所有任务
        resp = AdapterApi.AdapterDeleteAlltask(task_list)
        assert resp.status_code == 200
