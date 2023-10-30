#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib.log_utils import log
from commonlib.api_lib.validator import schema_validator
from commonlib.api_lib.AES_new import *

project_path=os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../../"))
schema_path=os.path.join(project_path,"data/swagger/belt/face.json")


class TestRasclusterApi(object):
    """ rasCluster Api测试"""

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

    def test_api_RasCluster_GetClusters(self, config_obj, RasclusterApi):
        """  GetClusters 外网使用，返回的 cluster 信息不包含 ingress 地址.
rou... """
        siteIds = None
        resp = RasclusterApi.RasCluster_GetClustersGetApi(siteIds=siteIds)
        assert resp.status_code == 200
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        faceCompareImageResponse_schema=schema["definitions"]["faceCompareImageResponse"]   
        required_list=["score","feature_version"]
        faceCompareImageResponse_schema.update({"required": required_list})  
        assert schema_validator(resp.resp_json,faceCompareImageResponse_schema)  
        assert resp.resp_json["score"]<=0.5


    
        
if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])