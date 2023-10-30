#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys
import pytest
import requests
from commonlib.cache_dict import CacheDict
from commonlib import sign_utils
from commonlib import time_utils
from commonlib import config

@pytest.fixture(scope='function')
def staticGroup(config_obj, ArgusdbApi, cache_obj):
    """ db"""
    ak = config_obj.Argus.ak
    key = '%s_static_ak_%s' % (sys._getframe().f_code.co_name, ak)

    def cache_func():
        group_id = config_obj.Argus.staticGroup
        if group_id:
            def clear_func():
                pass
            return group_id, clear_func
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,save_image_option=False,
                                            pedes_cb_url=pedes_cb_url, is_delete=False)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        group_id = resp.json_get("group_id")
        def clear_func():
            # ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=group_id)
            pass
        return group_id, clear_func

    yield cache_obj.get_value(key, func=cache_func)


@pytest.fixture(scope='function')
def streamGroup(config_obj, ArgusdbApi, cache_obj, staticGroup):
    """ db"""
    ak = config_obj.Argus.ak
    key = '%s_stream_ak_%s' % (sys._getframe().f_code.co_name, ak)

    def cache_func():
        group_id = config_obj.Argus.streamGroup
        if group_id:
            def clear_func():
                pass
            return group_id, clear_func
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 6000000
        bind_groups = [staticGroup]
        group_tag = None
        expired_time = 180
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,save_image_option=False,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url, is_delete=False)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        group_id = resp.json_get("group_id")
        time_utils.sleep(65)
        def clear_func():
            # ArgusdbApi.DB_DeleteStreamGroupPostApi(ak=ak, group_id=group_id)
            pass
        return group_id, clear_func

    yield cache_obj.get_value(key, func=cache_func)

@pytest.fixture(scope='function')
def groups4BatchImageSearch(config_obj, ArgusdbApi, ArguspedestrianApi, cache_obj):
    """ db"""
    ak = config_obj.Argus.ak
    key = '%s_groupInfo4BatchImageSearch_%s' % (sys._getframe().f_code.co_name, ak)

    def cache_func():
        """
        1. 创建staticid1
        2. 向staticid1中添加人：shihan1~shihan6
        3. 向staticid1中添加人：cyf1
        4. 创建staticid2
        5. 向staticid2中添加人：cyf1
        6. 创建streamid1
        7. 向streamid1中推送cyf1， shihan4
        8. 创建streamid2

        汇总：
        staticid1：shihan1~shihan6，cyf1
        staticid2：cyf1
        streamid1：cyf1， shihan4
        streamid2：空
        """
        staticid1 = config_obj.Argus.staticid1
        staticid2 = config_obj.Argus.staticid2
        streamid1 = config_obj.Argus.streamid1
        streamid2 = config_obj.Argus.streamid2
        if staticid1:
            def clear_func():
                pass
            return [staticid1, staticid2, streamid1, streamid2], clear_func

        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url, is_delete=False)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        staticid1 = resp.json_get("group_id")

        # 添加人
        for idx in range(1, 7):
            personID = "shihan%s" % idx
            override = "0"
            file_path = os.path.join(config.goimage_path, "face/wsh/shihan%s.jpg" % idx)
            resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticid1, person_id=personID,
                                                       override=override)
            assert resp.status_code == 200
            assert resp.json_get("error_code") == 0
            assert resp.json_get("error_msg") == "OK"
            assert resp.json_get("person_id") == personID
            time_utils.sleep(2)

        personID = "cyf1_2.20"
        override = "0"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticid1, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 再创建一个静态库
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url, is_delete=False)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        staticid2 = resp.json_get("group_id")

        personID2 = "cyf1_2.20"
        override = "0"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=staticid2, person_id=personID2,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID2

        # 创建动态库
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 6000000
        bind_groups = None
        group_tag = None
        expired_time = 100
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url, is_delete=False)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        streamid1 = resp.json_get("group_id")
        time_utils.sleep(65)

        # 推人
        image_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        timestamp = time_utils.get_timestamp()
        resp = ArguspedestrianApi.Pedestrian_face(streamid1, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="testcamera", requestId="faceRequestID1")
        assert resp.status_code == 200
        time_utils.sleep(1)

        image_path = os.path.join(config.goimage_path, "face/wsh/shihan4.jpg")
        timestamp = time_utils.get_timestamp()
        resp = ArguspedestrianApi.Pedestrian_face(streamid1, image_path, timestamp, ak=ak, device_id="testdevice",
                                                  camera_name="testcamera", requestId="faceRequestID2")
        assert resp.status_code == 200
        time_utils.sleep(1)

        # 创建动态库2
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 6000000
        bind_groups = None
        group_tag = None
        expired_time = 100
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url, is_delete=False)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        streamid2 = resp.json_get("group_id")
        time_utils.sleep(2)

        def clear_func():
            # ArgusdbApi.DB_DeleteStreamGroupPostApi(ak=ak, group_id=streamid1)
            # ArgusdbApi.DB_DeleteStreamGroupPostApi(ak=ak, group_id=streamid2)
            # ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=staticid1)
            # ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=staticid2)
            pass
        return [staticid1, staticid2, streamid1, streamid2], clear_func

    yield cache_obj.get_value(key, func=cache_func)