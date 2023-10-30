#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

import pytest
from pytest_check import check
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
from PIL import Image



class TestArgusdbScenario(object):
    """ Argusdb scenario test"""

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

    def test_scenario_argusDb_000_streamGroupCRUD(self, ArgusdbApi, config_obj):
        """ 测试创建streamGroup CRUD """
        """
        1. 测试创建streamGroup,pedur填写，size不填，期望创建成功
        2. 测试获取streamGroup,期望获取成功
        3. 测试修改streamGroup，修改callback为空，期望修改成功
        4. 测试获取streamGroup,期望获取成功
        5. 测试删除streamGroup，ak正确，groupid正确，期望删除成功
        """
        ak = config_obj.Argus.ak
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4),time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 6000000
        bind_groups = None
        group_tag = None
        expired_time = 100
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        resp = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.group_id") == group_id
        assert resp.json_get("list.0.group_mold") == group_mold
        assert resp.json_get("list.0.group_size") == group_size
        assert resp.json_get("list.0.group_name") == group_name
        assert resp.json_get("list.0.pedes_cb_url") == pedes_cb_url
        assert resp.json_get("list.0.expired_time") == expired_time

        update_group_name = "%s_update" % group_name
        update_group_mold = "FACE"
        update_expired_time = 18
        update_pedes_cb_url = ""
        resp = ArgusdbApi.DB_UpdateStreamGroupPostApi(ak=ak, group_id=group_id, group_name=update_group_name,
                                                      group_mold=update_group_mold, expired_time=update_expired_time,
                                                      pedes_cb_url=update_pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.group_id") == group_id
        assert resp.json_get("list.0.group_mold") == update_group_mold
        assert resp.json_get("list.0.group_size") == group_size
        assert resp.json_get("list.0.group_name") == update_group_name
        assert resp.json_get("list.0.pedes_cb_url") == update_pedes_cb_url
        assert resp.json_get("list.0.expired_time") == update_expired_time

        resp = ArgusdbApi.DB_DeleteStreamGroupPostApi(ak=ak, group_id=group_id)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

    def test_scenario_argusDb_001_streamGroupNameDuplicateFailed(self, ArgusdbApi, config_obj):
        """ 测试创建streamGroup,groupname重复，期望创建失败"""
        ak = config_obj.Argus.ak
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4),time_utils.get_timestamp())
        group_mold = None
        group_size = None
        bind_groups = None
        group_tag = None
        expired_time = 180
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        group_mold = "FACE"
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 409
        assert resp.json_get("error_code") == 6
        assert resp.json_get("error_msg") == "ALREADY_EXITS: group already exist"
        assert not resp.json_get("group_id")
        assert not resp.json_get("feature_version")

    @pytest.mark.parametrize("group_size", [99999, 12000001])
    def test_scenario_argusDb_002_groupSizeOutOfRangeFailed(self, ArgusdbApi, config_obj, group_size):
        """ 测试创建streamGroup,groupsize不在范围内10万-1200万，期望创建失败"""
        ak = config_obj.Argus.ak
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = None
        bind_groups = None
        group_tag = None
        expired_time = 180
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, group_size, min: 100000, max: 12000000"

    @pytest.mark.parametrize("invalidParam", [
        ('ak', ''),
        # ('ak', 'invalidAk'), # 有关ak的校验，不会报错
        ('group_name', ''),
    ])
    def test_scenario_argusDb_003_streamGroupCreateInvaildParams(self, ArgusdbApi, config_obj, invalidParam):
        """ 测试创建streamGroup,ak或groupname未填写,ak填写错误即不存在,期望报失败"""
        ak = config_obj.Argus.ak
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = None
        group_size = None
        bind_groups = None
        group_tag = None
        expired_time = 100
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        intef = ArgusdbApi.DB_CreateStreamGroupPostApi(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        if invalidParam[0] == "ak" and invalidParam[1] == "invalidAk":
            assert resp.status_code == 404
            assert resp.json_get("error_code") == 5
            assert resp.json_get("error_msg") == "NOT_FOUND: get ak err, sql: no rows in result set"
        else:
            assert resp.status_code == 400
            assert resp.json_get("error_code") == 3
            assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, ak or group_name or opq_model is required"

    def test_scenario_argusDb_004_streamGroupList(self, ArgusdbApi, config_obj):
        """ 测试获取streamGroupList,期望获取成功"""
        ak = config_obj.Argus.ak
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 6000000
        bind_groups = None
        group_tag = None
        expired_time = 180
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        group_id = resp.json_get("group_id")

        resp = ArgusdbApi.DB_ListStreamGroupGetApi(ak=ak)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) >= 1

        for info in resp.json_get("list"):
            if info["group_id"] == group_id:
                assert info["pedes_cb_url"] == pedes_cb_url
                assert info["expired_time"] == expired_time
                assert info["group_mold"] == group_mold
                assert info["group_size"] == group_size
                break
        else:
            assert None,"DB_ListStreamGroupGetApi未查询到db：%s" % group_id

    @pytest.mark.parametrize("invalidParam", [
        # ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
    ])
    def test_scenario_argusDb_005_ListStreamGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """ 测试获取streamGroupList,ak错误，期望获取失败"""
        ak = config_obj.Argus.ak
        group_type = None
        intef = ArgusdbApi.DB_ListStreamGroupGetApi(ak=ak, group_type=group_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") =="INVALID_ARGUMENT: invalid parameter, ak is required"

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak', 404,5, "NOT_FOUND: group not found"),
        ('ak', '', 400, 3, "INVALID_ARGUMENT: invalid parameter, ak or group_id is required"),
        ('ak', None, 400, 3, "INVALID_ARGUMENT: invalid parameter, ak or group_id is required"),
        ('group_id', 'invalidgroup_id', 404, 5, "NOT_FOUND: group not found"),
        ('group_id', '', 400,3, "INVALID_ARGUMENT: invalid parameter, ak or group_id is required"),
        ('group_id', None, 400,3, "INVALID_ARGUMENT: invalid parameter, ak or group_id is required"),
    ])
    def test_scenario_argusDb_006_GetStreamGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  测试获取streamGroup,ak或者groupid错误，期望获取失败"""
        ak = config_obj.Argus.ak
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4),time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 6000000
        bind_groups = None
        group_tag = None
        expired_time = 100
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        intef = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code == invalidParam[2]
        assert resp.json_get("error_code") ==invalidParam[3]
        assert resp.json_get("error_msg") == invalidParam[4]

    @pytest.mark.parametrize("invalidParam", [
        # ('group_name', 'existGroup', 409 ,6 , "ALREADY_EXITS: group already exist"),
        ('group_name', '', 400, 3, "INVALID_ARGUMENT: invalid group name"),
        # ('group_name', None, 400, 3, "INVALID_ARGUMENT: invalid group name"),
        ('group_id', 'invalidgroup_id', 404, 5, "NOT_FOUND: group not found"),
        ('group_id', '', 404, 5, "NOT_FOUND: group not found"),
        ('group_id', None, 404, 5, "NOT_FOUND: group not found"),
        ('ak', 'invalidak', 404, 5, "NOT_FOUND: group not found"),
        ('ak', '', 404, 5, "NOT_FOUND: group not found"),
        ('ak', None, 404, 5, "NOT_FOUND: group not found"),
    ])
    def test_scenario_argusDb_007_UpdateStreamGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """ 测试修改streamGroup，修改名称为空或者重复，期望修改失败 """
        ak = config_obj.Argus.ak
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
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        intef = ArgusdbApi.DB_UpdateStreamGroupPostApi(ak=ak, bind_groups=bind_groups,
                                                       expired_time=expired_time, group_id=group_id,
                                                       group_mold=group_mold, group_name=group_name,
                                                       pedes_cb_url=pedes_cb_url, sendRequest=False)
        if invalidParam[0] == "group_name" and  invalidParam[1] == "existGroup":
            intef.update_body(invalidParam[0], group_name)
        else:
            intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code == invalidParam[2]
        assert resp.json_get("error_code") == invalidParam[3]
        assert resp.json_get("error_msg") == invalidParam[4]

    def test_scenario_argusDb_008_staticGroupCRUD(self, ArgusdbApi, config_obj):
        """ 测试创建staticGroup，CRUD """
        """
        1. 测试创建staticGroup，ak正确，pedurl为空，size为500万，期望创建成功
        2. 测试获取staticGroup,期望获取成功
        3. 测试修改staticGroup，修改callback为空，期望修改成功
        4. 测试删除staticGroup，ak正确，groupid正确，期望删除成功
        """
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        resp = ArgusdbApi.DB_GetStaticGroupGetApi(ak=ak, group_id=group_id)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.group_id") == group_id
        assert resp.json_get("list.0.group_mold") == group_mold
        assert resp.json_get("list.0.group_size") == group_size
        assert resp.json_get("list.0.group_name") == group_name
        assert resp.json_get("list.0.pedes_cb_url") == pedes_cb_url

        update_group_name = "%s_update" % group_name
        update_pedes_cb_url = ""
        resp = ArgusdbApi.DB_UpdateStaticGroupPostApi(ak=ak, group_id=group_id, group_name=update_group_name,
                                                      pedes_cb_url=update_pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_GetStaticGroupGetApi(ak=ak, group_id=group_id)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.group_id") == group_id
        assert resp.json_get("list.0.group_mold") == group_mold
        assert resp.json_get("list.0.group_size") == group_size
        assert resp.json_get("list.0.group_name") == update_group_name
        assert resp.json_get("list.0.pedes_cb_url") == update_pedes_cb_url

        resp = ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=group_id)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

    def test_scenario_argusDb_009_staticGroupNameDuplicateFailed(self, ArgusdbApi, config_obj):
        """ 测试创建staticGroup,名称重复，期望创建失败 """
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = ""
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 409
        assert resp.json_get("error_code") == 6
        assert resp.json_get("error_msg") == "ALREADY_EXITS: group already exist"

    @pytest.mark.parametrize("invalidParam", [
        ('group_mold', 'invalidgroup_mold', 400,3,  "INVALID_ARGUMENT: invalid parameter, static group type invalid"),
        ('group_mold', 'PEDESTRIAN', 400,3,  "INVALID_ARGUMENT: invalid parameter, static group type invalid"),
        ('group_size', 99999, 400, 3, "INVALID_ARGUMENT: invalid parameter, group_size, min: 100000, max: 12000000"),
        ('group_size', 12000001, 400, 3, "INVALID_ARGUMENT: invalid parameter, group_size, min: 100000, max: 12000000"),
        ('ak', '', 400, 3, "INVALID_ARGUMENT: invalid parameter, ak, group_name required"),
        ('ak', None, 400, 3, "INVALID_ARGUMENT: invalid parameter, ak, group_name required"),
        # ('ak', 'invalidak', 404, 5, "NOT_FOUND: get ak err, sql: no rows in result set"),
        ('group_name', '', 400, 3, "INVALID_ARGUMENT: invalid parameter, ak, group_name required"),
        ('group_name', None, 400, 3, "INVALID_ARGUMENT: invalid parameter, ak, group_name required"),
    ])
    def test_scenario_argusDb_010_CreateStaticGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """ 测试创建staticGroup异常参数 """
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = ""
        intef = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code == invalidParam[2]
        assert resp.json_get("error_code") == invalidParam[3]
        assert resp.json_get("error_msg") == invalidParam[4]

    def test_scenario_argusDb_011_staticGroupList(self, ArgusdbApi, config_obj):
        """ 测试获取staticGroupList,期望获取成功"""
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = ""
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        resp = ArgusdbApi.DB_ListStaticGroupGetApi(ak=ak)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) >= 1

        for info in resp.json_get("list"):
            if info["group_id"] == group_id:
                assert info["pedes_cb_url"] == pedes_cb_url
                assert info["group_mold"] == group_mold
                assert info["group_size"] == group_size
                break
        else:
            assert None,"DB_ListStaticGroupGetApi未查询到db：%s" % group_id

    @pytest.mark.parametrize("invalidParam", [
        # ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
    ])
    def test_scenario_argusDb_012_ListStaticGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """ 测试获取staticGroupList,ak错误，期望获取失败 """
        ak = config_obj.Argus.ak
        group_type = None
        intef = ArgusdbApi.DB_ListStaticGroupGetApi(ak=ak, group_type=group_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: invalid parameter, ak is required"

    def test_scenario_argusDb_013_GetStaticGroupWithStreamGroupIdFailed(self, ArgusdbApi, config_obj):
        """ 测试获取staticGroup,groupid为stream，期望获取失败"""
        ak = config_obj.Argus.ak
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
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        resp = ArgusdbApi.DB_GetStaticGroupGetApi(ak=ak, group_id=group_id)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

    def test_scenario_argusDb_014_GetStreamGroupWithStaticGroupIdFailed(self, ArgusdbApi, config_obj):
        """ 测试获取streamGroup,groupid为static，期望获取失败"""
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = ""
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        resp = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak', 404,5,"NOT_FOUND: group not found"),
        ('ak', '', 400, 3, "INVALID_ARGUMENT: invalid parameter, ak or group_id is required"),
        ('ak', None, 400, 3, "INVALID_ARGUMENT: invalid parameter, ak or group_id is required"),
        ('group_id', 'invalidgroup_id', 404, 5, "NOT_FOUND: group not found"),
        ('group_id', '', 400, 3, "INVALID_ARGUMENT: invalid parameter, ak or group_id is required"),
        ('group_id', None, 400, 3, "INVALID_ARGUMENT: invalid parameter, ak or group_id is required"),
    ])
    def test_scenario_argusDb_015_GetStaticGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  测试获取staticGroup,ak或者groupid错误，期望获取失败"""
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = ""
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        group_id = resp.json_get("group_id")

        intef = ArgusdbApi.DB_GetStaticGroupGetApi(ak=ak, group_id=group_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code == invalidParam[2]
        assert resp.json_get("error_code") == invalidParam[3]
        assert resp.json_get("error_msg") == invalidParam[4]

    def test_scenario_argusDb_016_UpdateStaticGroupWithStreamGroupIdFailed(self, ArgusdbApi, config_obj):
        """ 测试修改staticGroup,groupid为stream，期望修改失败"""
        ak = config_obj.Argus.ak
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
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        update_group_name = "%s_update" % group_name
        update_pedes_cb_url = ""
        resp = ArgusdbApi.DB_UpdateStaticGroupPostApi(ak=ak, group_id=group_id, group_name=update_group_name,
                                                      pedes_cb_url=update_pedes_cb_url)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found(auto is true)"

    def test_scenario_argusDb_017_UpdateStreamGroupWithStaticGroupIdFailed(self, ArgusdbApi, config_obj):
        """ 测试修改streamGroup,groupid为static，期望修改失败"""
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = ""
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        update_group_name = "%s_update" % group_name
        update_group_mold = "PEDESTRIAN"
        update_expired_time = 18
        update_pedes_cb_url = ""
        resp = ArgusdbApi.DB_UpdateStreamGroupPostApi(ak=ak, group_id=group_id, group_name=update_group_name,
                                                      group_mold=update_group_mold, expired_time=update_expired_time,
                                                      pedes_cb_url=update_pedes_cb_url)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found(auto is true)"

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak', 404,5,"NOT_FOUND: group not found"),
        ('ak', '', 404,5,"NOT_FOUND: group not found"),
        ('ak', None, 404,5,"NOT_FOUND: group not found"),
        ('group_id', 'invalidgroup_id', 404,5,"NOT_FOUND: group not found"),
        ('group_id', '',404,5,"NOT_FOUND: group not found"),
        ('group_id', None,404,5,"NOT_FOUND: group not found"),
        # ('group_name', 'existGroup', 409,6,"ALREADY_EXITS: group already exists"),
        ('group_name', '',400,3,"INVALID_ARGUMENT: invalid group name"),
        # ('group_name', None,400,3,"INVALID_ARGUMENT: invalid group name"),
    ])
    def test_scenario_argusDb_019_UpdateStaticGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  测试修改staticGroup，修改名称为空或者重复，期望修改失败"""
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        intef = ArgusdbApi.DB_UpdateStaticGroupPostApi(ak=ak, group_id=group_id, group_mold=group_mold,
                                                       group_name=group_name, pedes_cb_url=pedes_cb_url, sendRequest=False)
        if invalidParam[0] == "group_name" and invalidParam[1] == "existGroup":
            intef.update_body(invalidParam[0], group_name)
        else:
            intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code == invalidParam[2]
        assert resp.json_get("error_code") == invalidParam[3]
        assert resp.json_get("error_msg") == invalidParam[4]

    def test_scenario_argusDb_020_DeleteStaticGroupWithStreamGroupIdFailed(self, ArgusdbApi, config_obj):
        """ 测试删除staticGroup,groupid为stream，期望删除失败"""
        ak = config_obj.Argus.ak
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
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        resp = ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=group_id)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

    def test_scenario_argusDb_021_DeleteStreamGroupWithStaticGroupIdFailed(self, ArgusdbApi, config_obj):
        """ 测试删除streamGroup,groupid为static，期望删除失败"""
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = ""
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        resp = ArgusdbApi.DB_DeleteStreamGroupPostApi(ak=ak, group_id=group_id)
        assert resp.status_code == 404
        assert resp.json_get("error_code") == 5
        assert resp.json_get("error_msg") == "NOT_FOUND: group not found"

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak',404,5,"NOT_FOUND: group not found"),
        ('ak', '',400,3,"INVALID_ARGUMENT: invalid parameter, request format error"),
        ('ak', None,400,3,"INVALID_ARGUMENT: invalid parameter, request format error"),
        ('group_id', 'invalidgroup_id', 404,5,"NOT_FOUND: group not found"),
        ('group_id', '',400,3,"INVALID_ARGUMENT: invalid parameter, request format error"),
        ('group_id', None,400,3,"INVALID_ARGUMENT: invalid parameter, request format error"),
    ])
    def test_scenario_argusDb_022_DeleteStreamGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """ 测试删除streamGroup，ak正确，groupid为static，期望删除失败"""
        ak = config_obj.Argus.ak
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
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        intef = ArgusdbApi.DB_DeleteStreamGroupPostApi(ak=ak, group_id=group_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code == invalidParam[2]
        assert resp.json_get("error_code") == invalidParam[3]
        assert resp.json_get("error_msg") == invalidParam[4]

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak', 404,5,"NOT_FOUND: group not found"),
        ('ak', '', 400,3, "INVALID_ARGUMENT: invalid parameter, request format error"),
        ('ak', None, 400,3, "INVALID_ARGUMENT: invalid parameter, request format error"),
        ('group_id', 'invalidgroup_id', 404,5,"NOT_FOUND: group not found"),
        ('group_id', '', 400,3, "INVALID_ARGUMENT: invalid parameter, request format error"),
        ('group_id', None, 400,3, "INVALID_ARGUMENT: invalid parameter, request format error"),
    ])
    def test_scenario_argusDb_023_DeleteStaticGroupInvalidParam(self, invalidParam, config_obj, ArgusdbApi):
        """  测试删除staticGroup，ak正确，ak或者groupid不存在，期望删除失败 """
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        intef = ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=group_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code == invalidParam[2]
        assert resp.json_get("error_code") == invalidParam[3]
        assert resp.json_get("error_msg") == invalidParam[4]

    def test_scenario_argusDb_024_StreamGroupBindStaticGroup(self, config_obj, ArgusdbApi):
        """ 测试创建streamGroup, 绑定bindgroups正确有两个，期望创建成功"""
        """
        1. 测试创建streamGroup, 绑定bindgroups正确有两个，期望创建成功
        2. 测试获取streamGroup,期望获取成功，绑定groups有2个
        3. 测试获取streamGroupList,期望获取成功，绑定groups有2个
        4. 测试修改streamGroup，修改bindgroups为空，期望修改成功
        5. 测试获取streamGroupList,期望获取成功, 绑定groups修改为空
        6. 测试修改streamGroup，修改bindgroups为2个，期望修改成功
        7. 测试获取streamGroupList,期望获取成功，绑定groups有2个
        8. 添加一个人员cyf后，删除staticmGroup，ak正确，groupid正确，期望删除成功
        9. 测试获取streamGroup,期望获取成功，绑定groups有1个
        10. 添加一个人员zxq后，删除staticmGroup
        11. 删除streamGroup，期望删除成功
        """
        ak = config_obj.Argus.ak
        group_name1 = "staticDb_1_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_name2 = "staticDb_2_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold1 = "FACE"
        group_mold2 = ""
        group_size = 5000000
        group_tag = None
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold1, group_name=group_name1,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        group_id1 = resp.json_get("group_id")
        time_utils.sleep(1)
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold2, group_name=group_name2,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        group_id2 = resp.json_get("group_id")
        time_utils.sleep(1)

        log().info("static group1:%s" % group_id1)
        log().info("static group2:%s" % group_id2)

        # 1. 测试创建streamGroup, 绑定bindgroups正确有两个，期望创建成功
        group_name3 = "streamDb_bind_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold3 = "FACE"
        group_size = 6000000
        bind_groups = [group_id1, group_id2]
        group_tag = None
        expired_time = 100
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold3, group_name=group_name3,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id3 = resp.json_get("group_id")
        log().info("stream group3:%s" % group_id3)
        time_utils.sleep(1)

        # 2. 测试获取streamGroup,期望获取成功，绑定groups有2个
        resp = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id3)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.group_id") == group_id3
        assert resp.json_get("list.0.group_mold") == group_mold3
        assert resp.json_get("list.0.group_size") == group_size
        assert resp.json_get("list.0.group_name") == group_name3
        assert len(resp.json_get("list.0.bind_groups")) == 2

        # 3. 测试获取streamGroupList,期望获取成功，绑定groups有2个
        resp = ArgusdbApi.DB_ListStreamGroupGetApi(ak=ak)
        assert resp.status_code == 200
        assert len(resp.json_get("list")) >= 1
        for info in resp.json_get("list"):
            if info["group_id"] == group_id3:
                assert len(info["bind_groups"]) == 2
                break
        else:
            assert None, "not found groupID:%s" % group_id3

        # 4. 测试修改streamGroup，修改bindgroups为空，期望修改成功
        resp = ArgusdbApi.DB_UpdateStreamGroupPostApi(ak=ak, group_id=group_id3, bind_groups=[])
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        # 5. 测试获取streamGroupList,期望获取成功, 绑定groups修改为空
        resp = ArgusdbApi.DB_ListStreamGroupGetApi(ak=ak)
        assert resp.status_code == 200
        assert len(resp.json_get("list")) >= 1
        for info in resp.json_get("list"):
            if info["group_id"] == group_id3:
                assert "bind_groups" not in info
                # with check: assert len(info["bind_groups"]) == 0 # TODO 开发不改，目前是不反悔该字段
                break
        else:
            assert None, "not found groupID:%s" % group_id3

        # 6. 测试修改streamGroup，修改bindgroups为2个，期望修改成功
        resp = ArgusdbApi.DB_UpdateStreamGroupPostApi(ak=ak, group_id=group_id3, bind_groups=[group_id1, group_id2])
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        # 7. 测试获取streamGroupList,期望获取成功，绑定groups有2个
        resp = ArgusdbApi.DB_ListStreamGroupGetApi(ak=ak)
        assert resp.status_code == 200
        assert len(resp.json_get("list")) >= 1
        for info in resp.json_get("list"):
            if info["group_id"] == group_id3:
                assert len(info["bind_groups"]) == 2
                break
        else:
            assert None, "not found groupID:%s" % group_id3

        # 8. 添加一个人员cyf后，删除staticmGroup，ak正确，groupid正确，期望删除成功
        personID = "cyf1"
        override = "0"
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=group_id1, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        resp = ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=group_id1)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        time_utils.sleep(2)

        # 9. 测试获取streamGroup,期望获取成功，绑定groups有1个
        resp = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id3)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.group_id") == group_id3
        assert len(resp.json_get("list.0.bind_groups")) == 1

        # 10. 添加一个人员zxq后，删除staticmGroup
        personID = "zxq1"
        override = "0"
        file_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        resp = ArgusdbApi.CreatePersonPostFromFile(file_path, ak=ak, group_id=group_id2, person_id=personID,
                                                   override=override)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("person_id") == personID
        time_utils.sleep(2)

        # 11. 删除streamGroup，期望删除成功
        resp = ArgusdbApi.DB_DeleteStaticGroupPostApi(ak=ak, group_id=group_id2)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        time_utils.sleep(2)

        resp = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id3)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.group_id") == group_id3
        # assert len(resp.json_get("list.0.bind_groups")) == 0

        resp = ArgusdbApi.DB_DeleteStreamGroupPostApi(ak=ak, group_id=group_id3)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"

        resp = ArgusdbApi.DB_GetStreamGroupGetApi(ak=ak, group_id=group_id3)
        assert resp.status_code == 404
        # assert resp.json_get("error_code") == 0
        # assert resp.json_get("error_msg") == "OK"

    def test_scenario_argusDb_025_StreamGroupBindInvaildGroupIDFailed(self, ArgusdbApi, config_obj):
        """ 测试创建streamGroup,绑定bindgroups不正确非本公司，期望创建失败 """
        ak = config_obj.Argus.ak
        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 6000000
        bind_groups = ["invaildgroupID"]
        group_tag = None
        expired_time = 100
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3

    def test_scenario_argusDb_026_StreamGroupBindStreamGroupFailed(self, ArgusdbApi, config_obj):
        """ 测试创建streamGroup,绑定bindgroups不正确为动态库，期望创建失败 """
        ak = config_obj.Argus.ak
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
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 6000000
        bind_groups = [group_id]
        group_tag = None
        expired_time = 100
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3

    def test_scenario_argusDb_027_StreamGroupBindNumGt10Failed(self, ArgusdbApi, config_obj):
        """ 测试创建streamGroup,绑定bindgroups超过10个，期望创建失败 """
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")

        group_name = "streamDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "PEDESTRIAN"
        group_size = 6000000
        bind_groups = [group_id for x in range(11)]
        group_tag = None
        expired_time = 100
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        merge_cb_url = None
        resp = ArgusdbApi.CreateStreamGroup(ak=ak, bind_groups=bind_groups, expired_time=expired_time,
                                            group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag, merge_cb_url=merge_cb_url,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3

    def test_scenario_argusDb_028_createPersonByfeature(self, ArgusdbApi, ArgusipsApi, config_obj):
        """ 根据feature创建person"""
        ak = config_obj.Argus.ak
        group_name = "staticDb_%s_%s" % (sign_utils.getUuid(4), time_utils.get_timestamp())
        group_mold = "FACE"
        group_size = 5000000
        group_tag = None
        pedes_cb_url = config_obj.Argus.pedes_cb_url
        resp = ArgusdbApi.CreateStaticGroup(ak=ak, group_mold=group_mold, group_name=group_name,
                                            group_size=group_size, group_tag=group_tag,
                                            pedes_cb_url=pedes_cb_url)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert resp.json_get("group_id")
        assert resp.json_get("feature_version") == config_obj.Argus.feature_version
        group_id = resp.json_get("group_id")
        time_utils.sleep(2)

        image_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        image = {
            "data": ArgusdbApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        blob1 = resp.json_get("response.feature.blob")

        person_id = "cyf1"
        resp = ArgusdbApi.DB_CreatePersonByFeaturePostApi(ak=ak, feature=blob1, group_id=group_id,
                                                          person_id=person_id, override="0")
        assert resp.status_code == 200
        assert resp.json_get("person_id") == person_id

        # 2. 测试search图片，期望接口返回成功
        file_path = image_path
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=group_id, threshold="0.9", top_k="5")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.person_id") == person_id
        assert resp.json_get("list.0.score") >= 0.999

        # 更新feature face/zpc/pengcheng1.jpg
        image_path = os.path.join(config.goimage_path, "face/zpc/pengcheng1.jpg")
        image = {
            "data": ArgusdbApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        blob2 = resp.json_get("response.feature.blob")

        # 更新feature
        person_id = "cyf1"
        resp = ArgusdbApi.DB_CreatePersonByFeaturePostApi(ak=ak, feature=blob2, group_id=group_id,
                                                          person_id=person_id, override="1")
        assert resp.status_code == 200
        assert resp.json_get("person_id") == person_id

        # 使用新图片查询
        file_path = image_path
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=group_id, threshold="0.9", top_k="5")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 1
        assert resp.json_get("list.0.person_id") == person_id
        assert resp.json_get("list.0.score") >= 0.999

        # 再次使用原图片查询
        file_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        resp = ArgusdbApi.SearchImagePostFromFile(file_path, ak=ak, group_id=group_id, threshold="0.9", top_k="5")
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert resp.json_get("error_msg") == "OK"
        assert len(resp.json_get("list")) == 0
        # assert resp.json_get("list.0.person_id") == person_id
        # assert resp.json_get("list.0.score") <= 0.02

    def test_scenario_argusDb_029_BatchFaceImageSearch_oneImage_oneGroup(self, ArgusdbApi, ArgusipsApi, config_obj, groups4BatchImageSearch):
        """ 一个image对应一个group,测试点默认topk为3"""
        """
            staticid1：shihan1~shihan6，cyf1
            staticid2：cyf1
            streamid1：cyf1， shihan4
            streamid2：空
        """
        staticid1 = groups4BatchImageSearch[0]
        staticid2 = groups4BatchImageSearch[1]
        streamid1 = groups4BatchImageSearch[2]
        streamid2 = groups4BatchImageSearch[3]

        log().info("staticid1:%s, staticid2:%s, streamid1:%s, streamid2:%s" % (staticid1, staticid2, streamid1, streamid2))
        ak = config_obj.Argus.ak
        # 一个image对应一个group, 测试点默认topk为3
        images = [
                     {"data": ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/wsh/shihan3.jpg"))}
                 ]
        search_configs = [
            {
                "group_id": staticid1,
                "threshold": 0.6,
            }
        ]
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 1
        for res in resp.json_get("results"):
            with check: assert res["code"] == 0
            with check: assert res["group_id"] == staticid1
            with check: assert len(res["feature_results"]) == 1
            for featureRes in res["feature_results"]:
                with check: assert featureRes["code"] == 0
                with check: assert len(featureRes["list"]) == 3
                for personRes in featureRes["list"]:
                    with check: assert personRes["score"] >= 0.6
                    with check: assert "shihan" in personRes["person_id"]

    def test_scenario_argusDb_030_BatchFaceImageSearch_oneImage_MutilGroup(self, ArgusdbApi, ArgusipsApi, config_obj, groups4BatchImageSearch):
        """ 多个image对应多个group，其中一个group没有数据"""
        """
            staticid1：shihan1~shihan6，cyf1
            staticid2：cyf1
            streamid1：cyf1， shihan4
            streamid2：空
        """
        staticid1 = groups4BatchImageSearch[0]
        staticid2 = groups4BatchImageSearch[1]
        streamid1 = groups4BatchImageSearch[2]
        streamid2 = groups4BatchImageSearch[3]

        ak = config_obj.Argus.ak
        # 多个image对应多个group，其中一个group没有数据 ？？TODO 感觉实际是一个图片 多个group
        expecteds =[3, 0, 1, 0] # 预期结果数量
        personName = ["shihan"]
        images = [
                     {"data": ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/wsh/shihan3.jpg"))}
                 ]
        search_configs = [
            {
                "group_id": staticid1,
                "threshold": 0.09,
            },
            {
                "group_id": staticid2,
                "threshold": 0.05,
            },
            {
                "group_id": streamid1,
                "threshold": 0.05
            },
            {
                "group_id": streamid2,
                "threshold": 0.3,
            }
        ]
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 4
        for j, res in enumerate(resp.json_get("results")):
            with check: assert res["code"] == 0
            with check: assert res["group_id"] == search_configs[j]["group_id"]
            with check: assert len(res["feature_results"]) == 1
            for k, featureRes in enumerate(res["feature_results"]):
                with check: assert featureRes["code"] == 0
                with check: assert len(featureRes["list"]) if featureRes["list"] else 0 == expecteds[j]
                if featureRes["list"]:
                    for i, personRes in enumerate(featureRes["list"]):
                        with check: assert personRes["score"] >= search_configs[i]["threshold"]
                        if j <= 1:
                            with check: assert personName[k] in personRes["person_id"]

    def test_scenario_argusDb_031_BatchFaceImageSearch_errorGroupID(self, ArgusdbApi, ArgusipsApi, config_obj):
        """ BatchFaceImageSearch接口，验证groupID填写错误情况"""
        ak = config_obj.Argus.ak
        images = [
            {"data": ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/wsh/shihan3.jpg"))}
        ]
        search_configs = [
            {
                "group_id": "invalidGroupID",
                "threshold": 0.6,
                "top_k": 5
            }
        ]
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak,images=images, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert "not found" in resp.json_get("results.0.feature_results.0.msg")

    def test_scenario_argusDb_032_BatchFaceImageSearch_errorGroupNum(self, ArgusdbApi, ArgusipsApi, config_obj,groups4BatchImageSearch):
        """ BatchFaceImageSearch接口 验证group个数超过10个报错"""
        """
            staticid1：shihan1~shihan6，cyf1
            staticid2：cyf1
            streamid1：cyf1， shihan4
            streamid2：空
        """
        staticid1 = groups4BatchImageSearch[0]
        staticid2 = groups4BatchImageSearch[1]
        streamid1 = groups4BatchImageSearch[2]
        streamid2 = groups4BatchImageSearch[3]

        ak = config_obj.Argus.ak
        images = [
                     {"data": ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/wsh/shihan3.jpg"))}
                 ]
        search_configs = []
        for x in range(11):
            search_configs.append(
                {
                    "group_id": staticid1,
                    "threshold": 0.6,
                    "top_k": 5
                })
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 400
        assert resp.json_get("error_code") == 3
        assert resp.json_get("error_msg") == "INVALID_ARGUMENT: search_configs'length is between 1 and 10"

    def test_scenario_argusDb_033_BatchFaceImageSearch_faceQualityLow(self, ArgusdbApi, ArgusipsApi, config_obj, groups4BatchImageSearch):
        """ BatchFaceImageSearch，看不清人脸，验证返回质量分低"""
        """
            staticid1：shihan1~shihan6，cyf1
            staticid2：cyf1
            streamid1：cyf1， shihan4
            streamid2：空
        """
        staticid1 = groups4BatchImageSearch[0]
        staticid2 = groups4BatchImageSearch[1]
        streamid1 = groups4BatchImageSearch[2]
        streamid2 = groups4BatchImageSearch[3]
        ak = config_obj.Argus.ak
        images = [
                     {"data": ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "noface.jpg"))}
                 ]
        search_configs = [
            {
                "group_id": staticid1,
                "threshold": 0.6,
                "top_k": 5
            }
        ]
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 1
        for res in resp.json_get("results"):
            with check: assert res["code"] == 0
            with check: assert res["group_id"] == staticid1
            with check: assert len(res["feature_results"]) == 1
            for featureRes in res["feature_results"]:
                with check: assert featureRes["code"] == -1
                with check: assert "face quality too low" in featureRes["msg"]

        image_path = os.path.join(config.goimage_path, "noface.jpg")
        img = Image.open(image_path)
        width = img.width
        height = img.height
        images = [
                     {"data": ArgusdbApi.imageToBase64(image_path),
                      "bounding": {
                          "vertices": [
                              {"x": 0,"y": 0},
                              {"x": width,"y": height},
                          ]
                      },
                      }
                 ]
        search_configs = [
            {
                "group_id": staticid1,
                "threshold": 0.6,
                "top_k": 5
            }
        ]
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 1
        for res in resp.json_get("results"):
            with check: assert res["code"] == 0
            with check: assert res["group_id"] == staticid1
            with check: assert len(res["feature_results"]) == 1
            for featureRes in res["feature_results"]:
                with check: assert featureRes["code"] == -1
                with check: assert "face quality too low" in featureRes["msg"]

    def test_scenario_argusDb_034_BatchFaceImageSearch_noface(self, ArgusdbApi, ArgusipsApi, config_obj, groups4BatchImageSearch):
        """ BatchFaceImageSearch，无人脸，验证返回noface"""
        """
            staticid1：shihan1~shihan6，cyf1
            staticid2：cyf1
            streamid1：cyf1， shihan4
            streamid2：空
        """
        staticid1 = groups4BatchImageSearch[0]
        staticid2 = groups4BatchImageSearch[1]
        streamid1 = groups4BatchImageSearch[2]
        streamid2 = groups4BatchImageSearch[3]
        ak = config_obj.Argus.ak
        images = [
                     {"data": ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "nobody.jpg"))}
                 ]
        search_configs = [
            {
                "group_id": staticid1,
                "threshold": 0.6,
                "top_k": 5
            }
        ]
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 1
        for res in resp.json_get("results"):
            with check:
                assert res["code"] == 0
            with check:
                assert res["group_id"] == staticid1
            with check:
                assert len(res["feature_results"]) == 1
            for featureRes in res["feature_results"]:
                with check: assert featureRes["code"] == -1
                with check: assert "no face" in featureRes["msg"]

        image_path = os.path.join(config.goimage_path, "nobody.jpg")
        img = Image.open(image_path)
        width = img.width
        height = img.height
        images = [
                     {"data": ArgusdbApi.imageToBase64(image_path),
                      "bounding": {
                          "vertices": [
                              {"x": 0, "y": 0},
                              {"x": width, "y": height},
                          ]
                      },
                      }
                 ]
        search_configs = [
            {
                "group_id": staticid1,
                "threshold": 0.6,
                "top_k": 5
            }
        ]
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 1
        for res in resp.json_get("results"):
            with check:
                assert res["code"] == 0
            with check:
                assert res["group_id"] == staticid1
            with check:
                assert len(res["feature_results"]) == 1
            for featureRes in res["feature_results"]:
                with check: assert featureRes["code"] == -1
                with check: assert "no face" in featureRes["msg"]

    def test_scenario_argusDb_035_BatchFaceImageSearch_topk(self, ArgusdbApi, ArgusipsApi, config_obj,groups4BatchImageSearch):
        """ BatchFaceImageSearch接口的topk的测试"""
        """
            staticid1：shihan1~shihan6，cyf1
            staticid2：cyf1
            streamid1：cyf1， shihan4
            streamid2：空
        """
        staticid1 = groups4BatchImageSearch[0]
        staticid2 = groups4BatchImageSearch[1]
        streamid1 = groups4BatchImageSearch[2]
        streamid2 = groups4BatchImageSearch[3]
        ak = config_obj.Argus.ak
        images = [
                     {"data": ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/wsh/shihan3.jpg"))}
                 ]
        search_configs = [
            {
                "group_id": staticid1,
                "threshold": 0.5,
                "top_k": 4
            },
            {
                "group_id": staticid2,
                "threshold": 0.5,
                "top_k": 5
            }
        ]
        personName = ["shihan", "shihan"]
        expecteds = [4,0]
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 2
        for j, res in enumerate(resp.json_get("results")):
            with check: assert res["code"] == 0
            with check: assert res["group_id"] == search_configs[j]["group_id"]
            with check: assert len(res["feature_results"]) == 1
            for featureRes in res["feature_results"]:
                with check: assert featureRes["code"] == 0
                with check: assert len(featureRes["list"]) if featureRes["list"] else 0 == expecteds[j]
                if featureRes["list"]:
                    for personRes in featureRes["list"]:
                        with check: assert personRes["score"] >= 0.5
                        with check: assert personName[j] in personRes["person_id"]

    def test_scenario_argusDb_035_BatchFaceImageSearch_oneImage_MutilGroup_bounding(self, ArgusdbApi, ArgusipsApi, config_obj,groups4BatchImageSearch):
        """ 多个image对应多个group，存在Bounding，其中一个group没有数据"""
        """
            staticid1：shihan1~shihan6，cyf1
            staticid2：cyf1
            streamid1：cyf1， shihan4
            streamid2：空
        """
        staticid1 = groups4BatchImageSearch[0]
        staticid2 = groups4BatchImageSearch[1]
        streamid1 = groups4BatchImageSearch[2]
        streamid2 = groups4BatchImageSearch[3]
        ak = config_obj.Argus.ak
        image_path = os.path.join(config.goimage_path, "face/wsh/shihan3.jpg")
        img = Image.open(image_path)
        width = img.width
        height = img.height
        images = [
                     {"data": ArgusdbApi.imageToBase64(image_path),
                      "bounding": {
                          "vertices": [
                              {"x": 0, "y": 0},
                              {"x": width, "y": height},
                          ]
                      },
            }
        ]
        search_configs = [
            {
                "group_id": staticid1,
                "threshold": 0.09,
                # "top_k": 4
            },
            {
                "group_id": staticid2,
                "threshold": 0.05,
                # "top_k": 5
            },
            {
                "group_id": streamid1,
                "threshold": 0.05,
                # "top_k": 5
            },
            {
                "group_id": streamid2,
                "threshold": 0.3,
                # "top_k": 5
            }
        ]
        personName = ["shihan"]
        expecteds = [3, 0, 1, 0]
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 4
        for j, res in enumerate(resp.json_get("results")):
            with check: assert res["code"] == 0
            with check: assert res["group_id"] == search_configs[j]["group_id"]
            with check: assert len(res["feature_results"]) == 1
            for k, featureRes in enumerate(res["feature_results"]):
                with check: assert featureRes["code"] == 0
                with check: assert len(featureRes["list"]) if featureRes["list"] else 0 == expecteds[j]
                if featureRes["list"]:
                    for i, personRes in enumerate(featureRes["list"]):
                        with check: assert personRes["score"] >= search_configs[i]["threshold"]
                        if j == 2:
                            pass
                        else:
                            with check: assert personName[k] in personRes["person_id"]

    def test_scenario_argusDb_036_BatchFaceImageSearch_oneImage_MutilGroup_bounding_noface(self, ArgusdbApi, ArgusipsApi,
                                                                                    config_obj,
                                                                                    groups4BatchImageSearch):
        """ 多个image对应多个group，存在Bounding，框中没有人脸"""
        """
            staticid1：shihan1~shihan6，cyf1
            staticid2：cyf1
            streamid1：cyf1， shihan4
            streamid2：空
        """
        staticid1 = groups4BatchImageSearch[0]
        staticid2 = groups4BatchImageSearch[1]
        streamid1 = groups4BatchImageSearch[2]
        streamid2 = groups4BatchImageSearch[3]
        ak = config_obj.Argus.ak
        image_path = os.path.join(config.goimage_path, "face/wsh/shihan3.jpg")
        img = Image.open(image_path)
        width = img.width
        height = img.height
        images = [
                     {"data": ArgusdbApi.imageToBase64(image_path),
                      "bounding": {
                          "vertices": [
                              {"x": 0, "y": 0},
                              {"x": int(width/5), "y": int(height/5)},
                          ]
                      },
                      }
                 ]
        search_configs = [
            {
                "group_id": staticid1,
                "threshold": 0.09,
                # "top_k": 4
            },
            {
                "group_id": staticid2,
                "threshold": 0.05,
                # "top_k": 5
            },
            {
                "group_id": streamid1,
                "threshold": 0.05,
                # "top_k": 5
            },
            {
                "group_id": streamid2,
                "threshold": 0.3,
                # "top_k": 5
            }
        ]
        personName = ["shihan"]
        expecteds = [0, 0, 0, 0]
        resp = ArgusdbApi.DB_BatchSearchImagePostApi(ak=ak, images=images, search_configs=search_configs)
        assert resp.status_code == 200
        assert resp.json_get("error_code") == 0
        assert len(resp.json_get("results")) == 4
        for j, res in enumerate(resp.json_get("results")):
            with check:
                assert res["code"] == 0
            with check:
                assert res["group_id"] == search_configs[j]["group_id"]
            with check:
                assert len(res["feature_results"]) == 1
            for k, featureRes in enumerate(res["feature_results"]):
                with check: assert featureRes["code"] == -1
                with check: assert "overlap failed: no face" in featureRes["msg"]
                with check: assert len(featureRes["list"]) if featureRes["list"] else 0== expecteds[j]
