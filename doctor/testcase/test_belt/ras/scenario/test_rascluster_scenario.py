#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestRasclusterScenario(object):
    """ Rascluster scenario test"""

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

    @pytest.mark.skip(msg="该接口不对外了")
    def test_scenario_000_getCluster(self, RasclusterApi, centerInfo, edgeDefaultInfo):
        """ func test"""
        siteIds = None
        resp = RasclusterApi.RasCluster_GetClustersGetApi(siteIds=siteIds)
        assert resp.status_code == 200
        assert resp.json_get("center.id") == centerInfo.id
        assert resp.json_get("center.name") == centerInfo.name
        assert resp.json_get("center.site_id") == centerInfo.site_id
        assert resp.json_get("center.type") == centerInfo.type

        assert resp.json_get("edges.0.id") == edgeDefaultInfo.id
        assert resp.json_get("edges.0.name") == edgeDefaultInfo.name
        assert resp.json_get("edges.0.site_id") == edgeDefaultInfo.site_id
        assert resp.json_get("edges.0.type") == edgeDefaultInfo.type

        siteIds = [edgeDefaultInfo.site_id]
        resp = RasclusterApi.RasCluster_GetClustersGetApi(siteIds=siteIds)
        assert resp.status_code == 200
