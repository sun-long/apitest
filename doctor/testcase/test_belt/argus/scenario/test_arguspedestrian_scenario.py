#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from pytest_check import check
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestArguspedestrianScenario(object):
    """ Arguspedestrian scenario test"""

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

    def test_scenario_pedestrain_000_createDB(self, config_obj, ArguspedestrianApi, staticGroup, streamGroup):
        """ 建库"""
        log().info("static:%s" % staticGroup)
        log().info("stream:%s" % streamGroup)

    def test_scenario_pedestrain_001_PedRegular(self, config_obj, ArguspedestrianApi, staticGroup, streamGroup):
        """  测试pedestrian推送人脸 """
        ak = config_obj.Argus.ak
        image_path = os.path.join(config.goimage_path, "face/zgj/guojin1.jpg")
        timestamp = time_utils.get_today_timestamp("08:01")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="testcamera")
        assert resp.status_code == 200
        time_utils.sleep(1)

        image_path = os.path.join(config.goimage_path, "face/zgj/guojin2.jpg")
        timestamp = time_utils.get_today_timestamp("08:02")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="testcamera")
        assert resp.status_code == 200
        time_utils.sleep(1)

        image_path = os.path.join(config.goimage_path, "face/zgj/guojin3.jpg")
        timestamp = time_utils.get_today_timestamp("08:03")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="testcamera")
        assert resp.status_code == 200
        time_utils.sleep(1)

        image_path = os.path.join(config.goimage_path, "face/zgj/guojin4.jpg")
        timestamp = time_utils.get_today_timestamp("08:04")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="testcamera")
        assert resp.status_code == 200
        time_utils.sleep(1)

        image_path = os.path.join(config.goimage_path, "face/zgj/guojin5.jpg")
        timestamp = time_utils.get_today_timestamp("08:05")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="testcamera")
        assert resp.status_code == 200
        time_utils.sleep(1)

    def test_scenario_pedestrain_002_Mutilstrategy(self, config_obj, ArgusdbApi, ArguspedestrianApi, staticGroup, streamGroup):
        """ 测试多级库查询,静态库；动态小库。"""
        """
        1. 先添加静态库人员cyf，以及动态库的静态小库人员zxq，personadd
        2. 添加静态库人员和静态小库人员到访，recognize推送
        """
        # 1. 先添加静态库人员cyf，以及动态库的静态小库人员zxq，personadd
        ak = config_obj.Argus.ak
        personID = "cyf"
        override = "0"
        # image = ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/cyf/cyf1.jpg"))
        # resp = ArgusdbApi.DB_CreatePersonPostApi(ak=ak, group_id=staticGroup, person_id=personID, override=override, image=image)

        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticGroup, person_id=personID, override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        personID = "zxq"
        override = "0"
        file_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=streamGroup, person_id=personID,
                                                   override=override)
        # image = ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg"))
        # resp = ArgusdbApi.DB_CreatePersonPostApi(ak=ak, group_id=streamGroup, person_id=personID, override=override,
        #                                          image=image)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 2. 添加静态库人员和静态小库人员到访，recognize推送
        image_path = os.path.join(config.goimage_path, "face/cyf/cyf2.jpg")
        timestamp = time_utils.get_today_timestamp("08:11")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="teststatic")
        assert resp.status_code == 200
        time_utils.sleep(1)

        image_path = os.path.join(config.goimage_path, "face/zxq/xueqi2.jpg")
        timestamp = time_utils.get_today_timestamp("08:12")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="testdynamic")
        assert resp.status_code == 200
        time_utils.sleep(1)

    def test_scenario_pedestrain_003_DynamicMutiFace(self, config_obj, ArgusdbApi, ArguspedestrianApi, staticGroup, streamGroup):
        """ 测试动态入库，多人脸的情况；meister应该调用overlap接口"""
        """
        这个case的逻辑不太理解
        1. 多人脸的情况，传入图片的框，期望拿到的是大脸的person（诗涵）
        2. 多人脸的情况，传入小脸的框，期望拿到的是小脸的person（凤姐）
        """
        ak = config_obj.Argus.ak
        image_path = os.path.join(config.goimage_path, "twoface.jpg")
        timestamp = time_utils.get_today_timestamp("08:21")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="multi")
        assert resp.status_code == 200
        time_utils.sleep(1)

        image_path = os.path.join(config.goimage_path, "face/wsh/shihan3.jpg")
        timestamp = time_utils.get_today_timestamp("08:22")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="multi")
        assert resp.status_code == 200
        time_utils.sleep(1)

        # 2. 多人脸的情况，传入小脸的框，期望拿到的是小脸的person（凤姐）
        rect = {
            "left": 0,
            "right": 850,
            "top": 0,
            "bottom": 850
        }
        image_path = os.path.join(config.goimage_path, "twoface.jpg")
        timestamp = time_utils.get_today_timestamp("08:31")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="multi", rect=rect, origin_rect=rect)
        assert resp.status_code == 200
        time_utils.sleep(1)

        image_path = os.path.join(config.goimage_path, "face/cyf/cyf3.jpg")
        timestamp = time_utils.get_today_timestamp("08:32")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="multi")
        assert resp.status_code == 200
        time_utils.sleep(1)

    def test_scenario_pedestrain_004_FilterFace(self, config_obj, ArgusdbApi, ArguspedestrianApi, staticGroup, streamGroup):
        """ 推送能被过滤的图片"""
        ak = config_obj.Argus.ak
        image_path = os.path.join(config.goimage_path, "filterface.jpg")
        timestamp = time_utils.get_today_timestamp("08:58")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="filterface")
        assert resp.status_code == 200
        time_utils.sleep(1)

    def test_scenario_pedestrain_005_Mergestrategy(self, config_obj, ArgusdbApi, ArguspedestrianApi, staticGroup, streamGroup):
        """ 推送能产生merge的数据"""
        ak = config_obj.Argus.ak
        image_path = os.path.join(config.goimage_path, "merge/merge2.jpg")
        timestamp = time_utils.get_today_timestamp("09:01")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="merge")
        assert resp.status_code == 200
        time_utils.sleep(1)

        image_path = os.path.join(config.goimage_path, "merge/merge1.jpg")
        timestamp = time_utils.get_today_timestamp("09:05")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="merge")
        assert resp.status_code == 200
        time_utils.sleep(1)

        image_path = os.path.join(config.goimage_path, "merge/merge2to1.jpg")
        timestamp = time_utils.get_today_timestamp("09:09")
        resp = ArguspedestrianApi.Pedestrian_face(streamGroup, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="merge")
        assert resp.status_code == 200
        time_utils.sleep(1)

    def test_scenario_pedestrain_006_PedRegularExpects(self, config_obj, ArgusdbApi, ArguspedestrianApi, ArgusdatacenterApi,
                                                       staticGroup, streamGroup):
        """ TestPedRegular测试识别结果,期望有5个face不扩散"""
        ak = config_obj.Argus.ak
        store_id = streamGroup
        device_id = None
        camera_id = None
        person_id = None
        request_id = None
        start_time = time_utils.get_today_timestamp("08:00")
        end_time = time_utils.get_today_timestamp("08:10")
        page_number = None
        page_size = None
        mis_request_ids = None
        resp = ArgusdatacenterApi.DC_GetOriginMetaInfoGetApi(ak=ak, store_id=store_id, device_id=device_id,
                                                             camera_id=camera_id, person_id=person_id,
                                                             request_id=request_id, start_time=start_time,
                                                             end_time=end_time, page_number=page_number,
                                                             page_size=page_size, mis_request_ids=mis_request_ids)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 5
        results = resp.json_get("results")
        for idx, res in enumerate(results):
            with check: assert res["gender"] == "male"
            with check: assert res["camera_name"] == "testcamera"
            with check: assert res["device_id"] == "testdevice"
            with check: assert res["face_id"] == res["person_id"]
            # with check: assert res["plate_image_url"]
            # with check: assert res["snap_image_url"] # 未开启寸土
            with check: assert res["time"]
            if idx < len(results) - 1:
                with check: assert res["person_id"] == results[idx+1]["person_id"]
            if idx == len(results) - 1:
                with check: assert res["result_type"] == "new"
            else:
                with check: assert res["result_type"] == "matched"


    def test_scenario_pedestrain_007_Mutilstrategy(self, config_obj, ArgusdbApi, ArguspedestrianApi, ArgusdatacenterApi,
                                                       staticGroup, streamGroup):
        """ TestMutilstrategy拉取识别结果，期望数据正确，期望匹配上静态库的cyf，以及动态小库的zxq。"""
        ak = config_obj.Argus.ak
        store_id = streamGroup
        device_id = None
        camera_id = None
        person_id = None
        request_id = None
        start_time = time_utils.get_today_timestamp("08:10")
        end_time = time_utils.get_today_timestamp("08:20")
        page_number = None
        page_size = None
        mis_request_ids = None
        resp = ArgusdatacenterApi.DC_GetOriginMetaInfoGetApi(ak=ak, store_id=store_id, device_id=device_id,
                                                             camera_id=camera_id, person_id=person_id,
                                                             request_id=request_id, start_time=start_time,
                                                             end_time=end_time, page_number=page_number,
                                                             page_size=page_size, mis_request_ids=mis_request_ids)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 2
        results = resp.json_get("results")
        for idx, res in enumerate(results):
            if res["camera_name"] == "teststatic":
                with check: assert res["result_type"] == "matched"
                with check: assert res["person_id"] == "cyf"
                with check: assert res["group_id"] == staticGroup
            if res["camera_name"] == "testdynamic":
                with check: assert res["result_type"] == "matched"
                with check: assert res["person_id"] == "zxq"
                with check: assert res["group_id"] == streamGroup

    def test_scenario_pedestrain_008_DynamicMutiFaceExpects(self, config_obj, ArgusdbApi, ArguspedestrianApi, ArgusdatacenterApi,
                                                       staticGroup, streamGroup):
        """ TestDynamicMutiFace/overlap为大脸，拉取识别结果，期望数据正确匹配上大脸wsh"""
        ak = config_obj.Argus.ak
        store_id = streamGroup
        device_id = None
        camera_id = None
        person_id = None
        request_id = None
        start_time = time_utils.get_today_timestamp("08:20")
        end_time = time_utils.get_today_timestamp("08:25")
        page_number = None
        page_size = None
        mis_request_ids = None
        resp = ArgusdatacenterApi.DC_GetOriginMetaInfoGetApi(ak=ak, store_id=store_id, device_id=device_id,
                                                             camera_id=camera_id, person_id=person_id,
                                                             request_id=request_id, start_time=start_time,
                                                             end_time=end_time, page_number=page_number,
                                                             page_size=page_size, mis_request_ids=mis_request_ids)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 2
        results = resp.json_get("results")
        for idx, res in enumerate(results):
            if idx < len(results) - 1:
                with check: assert res["person_id"] == results[idx + 1]["person_id"]

    def test_scenario_pedestrain_009_DynamicMutiFaceExpects2(self, config_obj, ArgusdbApi, ArguspedestrianApi, ArgusdatacenterApi,
                                                       staticGroup, streamGroup):
        """ TestDynamicMutiFace/指定框小脸，拉取识别结果，期望数据正确，匹配上cyf"""
        ak = config_obj.Argus.ak
        store_id = streamGroup
        device_id = None
        camera_id = None
        person_id = None
        request_id = None
        start_time = time_utils.get_today_timestamp("08:30")
        end_time = time_utils.get_today_timestamp("08:35")
        page_number = None
        page_size = None
        mis_request_ids = None
        resp = ArgusdatacenterApi.DC_GetOriginMetaInfoGetApi(ak=ak, store_id=store_id, device_id=device_id,
                                                             camera_id=camera_id, person_id=person_id,
                                                             request_id=request_id, start_time=start_time,
                                                             end_time=end_time, page_number=page_number,
                                                             page_size=page_size, mis_request_ids=mis_request_ids)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 2
        results = resp.json_get("results")
        for idx, res in enumerate(results):
            if idx < len(results) - 1:
                with check: assert res["person_id"] == results[idx + 1]["person_id"]

    def test_scenario_pedestrain_010_FilterFaceExpects(self, config_obj, ArgusdbApi, ArguspedestrianApi,
                                                             ArgusdatacenterApi,
                                                             staticGroup, streamGroup):
        """ TestFilterFace拉取识别结果，期望数据正确，face被过滤"""
        ak = config_obj.Argus.ak
        store_id = streamGroup
        device_id = None
        camera_id = None
        person_id = None
        request_id = None
        start_time = time_utils.get_today_timestamp("08:55")
        end_time = time_utils.get_today_timestamp("08:59")
        page_number = None
        page_size = None
        mis_request_ids = None
        resp = ArgusdatacenterApi.DC_GetOriginMetaInfoGetApi(ak=ak, store_id=store_id, device_id=device_id,
                                                             camera_id=camera_id, person_id=person_id,
                                                             request_id=request_id, start_time=start_time,
                                                             end_time=end_time, page_number=page_number,
                                                             page_size=page_size, mis_request_ids=mis_request_ids)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 0

    def test_scenario_pedestrain_011_MergestrategyExpects(self, config_obj, ArgusdbApi, ArguspedestrianApi,
                                                       ArgusdatacenterApi,
                                                       staticGroup, streamGroup):
        """ TestMergestrategy拉取识别结果，期望数据正确，期望在线merge功能正常"""
        ak = config_obj.Argus.ak
        store_id = streamGroup
        device_id = None
        camera_id = None
        person_id = None
        request_id = None
        start_time = time_utils.get_today_timestamp("09:00")
        end_time = time_utils.get_today_timestamp("09:10")
        page_number = None
        page_size = None
        mis_request_ids = None
        resp = ArgusdatacenterApi.DC_GetOriginMetaInfoGetApi(ak=ak, store_id=store_id, device_id=device_id,
                                                             camera_id=camera_id, person_id=person_id,
                                                             request_id=request_id, start_time=start_time,
                                                             end_time=end_time, page_number=page_number,
                                                             page_size=page_size, mis_request_ids=mis_request_ids)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 3
        assert resp.json_get("results.0.person_id") == resp.json_get("results.1.person_id")
        assert resp.json_get("results.1.person_id") == resp.json_get("results.2.person_id")