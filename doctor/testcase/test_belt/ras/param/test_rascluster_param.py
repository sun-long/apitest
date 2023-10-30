#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


@pytest.mark.skip(msg="不对外")
class TestRasclusterParam(object):
    """ rasCluster Param测试"""

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

    @pytest.mark.parametrize("invalidParam", [
        ('siteIds', 'invalidsiteIds'),
        ('siteIds', ''),
        ('siteIds', None),
    ])
    def test_api_RasCluster_GetClustersInvalidParam(self, invalidParam, config_obj, RasclusterApi):
        """  GetClusters 外网使用，返回的 cluster 信息不包含 ingress 地址.
rou... """
        siteIds = None
        intef = RasclusterApi.RasCluster_GetClustersGetApi(siteIds=siteIds, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200
