#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestArgusrrsScenario(object):
    """ Argusrrs scenario test"""

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

    def test_scenario_rrs_001_r_Group_Add(self, config_obj, ArgusrrsApi):
        """ rgoup"""
        """
        1. rgroup name没有输入
        2. 正常创建
        3. 重复创建
        4. 删除rgroup
        5. 判断是否删除成功
        """
        # 1. rgroup name没有输入
        rgroup = ""
        resp = ArgusrrsApi.Tenant_AddRGroupPostApi(rgroup=rgroup)
        assert resp.status_code != 200

        # 2. 正常创建
        rgroup = "产品线_%s_%s" % (sign_utils.getUuid(5), time_utils.get_time_str())
        resp = ArgusrrsApi.Tenant_AddRGroupPostApi(rgroup=rgroup)
        assert resp.status_code == 200

        # 3. 重复创建
        resp = ArgusrrsApi.Tenant_AddRGroupPostApi(rgroup=rgroup)
        assert resp.status_code != 200

        # 4. 删除rgroup
        resp = ArgusrrsApi.Tenant_DeleteRGroupPostApi(rgroup=rgroup)
        assert resp.status_code == 200

        # 5. 判断是否删除成功
        resp = ArgusrrsApi.Tenant_ListRGroupGetApi()
        assert resp.status_code == 200
        assert len(resp.json_get("rgroups")) > 0
        for rgroup_info in resp.json_get("rgroups"):
            if rgroup_info["rgroup"] == rgroup:
                assert None, "%s rgroup删除失败" % rgroup

        # resp = ArgusrrsApi.Tenant_GetRgroupByAkGetApi()

    def test_scenario_rrs_002_tagCRD(self, config_obj, ArgusrrsApi):
        """ tag CRD"""
        """
        1. tag name没有输入
        2. 添加静态标签,value为空
        3. 添加静态标签,type类型不对
        4. 添加静态标签,score为0
        5. 添加静态标签,score为1
        6. 添加动态标签,score为1 value="test1;test2"
        7. 添加动态标签,score为1
        8. 查询tag
        9. 删除静态标签
        10. 删除动态标签
        11. 查询tag，预期数量减少2个
        """
        # 1. tag name没有输入
        tag =  {
            "name": "",
            "score": 1,
            # "type": "[STATIC]STATIC/DYNAMIC",
            "value": "dd"
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code != 200

        # 2.添加静态标签,value为空
        tag = {
            "name": "静态资源标签",
            "score": 1,
            # "type": "[STATIC]STATIC/DYNAMIC",
            "value": ""
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code != 200

        # 3. 添加静态标签,type类型不对
        tag = {
            "name": "静态资源标签",
            "score": 1,
            "type": "invalidType",
            "value": "tag"
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code != 200

        # 4. 添加静态标签,score为0
        tag = {
            "name": "静态资源标签",
            "score": 0,
            "type": "STATIC",
            "value": "test1"
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code != 200

        # 5. 添加静态标签,score为1
        tag = {
            "name": "静态资源标签",
            "score": 1,
            "type": "STATIC",
            "value": "test1;test2"
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code == 200

        # 6. 添加动态标签,score为1 value="test1;test2"
        tag = {
            "name": "动态资源标签",
            "score": 1,
            "type": "DYNAMIC",
            "value": "test1;test2"
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code != 200

        # 7. 添加动态标签,score为1
        tag = {
            "name": "动态资源标签",
            "score": 1,
            "type": "DYNAMIC",
            "value": ""
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code == 200

        # 8. 查询tag
        resp = ArgusrrsApi.Tenant_ListTagGetApi()
        assert resp.status_code == 200
        tag_count = len(resp.json_get("tags"))

        # 9.删除静态标签
        tag = "静态资源标签"
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag=tag)
        assert resp.status_code == 200

        # 10. 删除动态标签
        tag = "动态资源标签"
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag=tag)
        assert resp.status_code == 200

        # 11. 查询tag，预期数量减少2个
        resp = ArgusrrsApi.Tenant_ListTagGetApi()
        assert resp.status_code == 200
        assert len(resp.json_get("tags")) == tag_count - 2

    def test_scenario_rrs_003_tagUpdate(self, config_obj, ArgusrrsApi):
        """ tag update"""
        """
        1.添加静态标签,score为1. value:test1;test2
        2.添加动态标签,score为120, value=""
        3.更新动态标签,score为100
        4.更新静态标签,score为100，value:test1;test2;test4
        5.查询更新结果
        6.删除静态标签
        7.删除动态标签
        """
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag="静态资源标签")
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag="动态资源标签")
        # 1.添加静态标签,score为1. value:test1;test2
        tag = {
            "name": "静态资源标签",
            "score": 1,
            "type": "STATIC",
            "value": "test1;test2"
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code == 200
        # 2.添加动态标签,score为120, value=""
        tag = {
            "name": "动态资源标签",
            "score": 120,
            "type": "DYNAMIC",
            "value": ""
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code == 200
        # 3.更新动态标签,score为100
        tag = {
            "name": "动态资源标签",
            "score": 100,
            "type": "DYNAMIC",
            "value": ""
        }
        resp = ArgusrrsApi.Tenant_UpdateTagPostApi(tag=tag)
        assert resp.status_code == 200
        # 4.更新静态标签,score为100，value:test1;test2;test4
        tag = {
            "name": "静态资源标签",
            "score": 100,
            "type": "STATIC",
            "value": "test1;test2;test4"
        }
        resp = ArgusrrsApi.Tenant_UpdateTagPostApi(tag=tag)
        assert resp.status_code == 200
        # 5.查询更新结果
        resp = ArgusrrsApi.Tenant_ListTagGetApi()
        assert resp.status_code == 200
        assert len(resp.json_get("tags")) > 0
        for tag_info in resp.json_get("tags"):
            if tag_info["name"] == "静态资源标签":
                assert tag_info["score"] == 100
                assert tag_info["value"] == "test1;test2;test4"
            elif tag_info["name"] == "动态资源标签":
                assert tag_info["score"] == 100
                assert tag_info["value"] == ""
        # 6.删除静态标签
        tag = "静态资源标签"
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag=tag)
        assert resp.status_code == 200
        # 7.删除动态标签
        tag = "动态资源标签"
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag=tag)
        assert resp.status_code == 200

    def test_scenario_rrs_004_resourceCRD(self, config_obj, ArgusrrsApi):
        """ resource crd"""
        """
        1. 删除静态标签
        2. 删除动态标签
        3. 添加静态标签,score为1
        4. 添加动态标签,score为1
        5. 创建rgroup
        6. 添加资源，name为空，预期失败
        7. 添加资源，rgroup 不存在，预期失败
        8. 添加静态资源成功
        9. 添加动态资源成功
        10. 查询动态资源
        11. 添加资源， tag name 不存在，预期失败
        12. 添加资源， tag name 静态标签。value错误， 预期失败
        13. 查询静态资源
        14. 更新资源的静态标签
        15. 查询变更后查询结果
        16. 更新资源的动态标签
        17. 查询变更后查询结果
        18. 删除resource
        19. 查询resource， 预期删除后没有了
        20. 删除rgroup
        21. 删除静态标签
        22. 删除动态标签
        """

        rgroup1 = "产品线3_%s_%s" % (sign_utils.getUuid(5), time_utils.get_time_str())
        rgroup2 = "产品线4_%s_%s" % (sign_utils.getUuid(5), time_utils.get_time_str())
        resource1 = "资源1"
        resource2 = "资源2"
        tag_static = "静态资源标签"
        tag_dyna = "动态资源标签"
        resource_id1 = None
        resource_id2 = None
        # 1. 删除静态标签
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag=tag_static)
        # 2. 删除动态标签
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag=tag_dyna)
        # 3. 添加静态标签,score为1
        tag = {
            "name": tag_static,
            "score": 1,
            "type": "STATIC",
            "value": "test1;test2"
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code == 200
        # 4. 添加动态标签,score为1
        tag = {
            "name": tag_dyna,
            "score": 120,
            "type": "DYNAMIC",
            "value": ""
        }
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code == 200
        # 5. 创建rgroup
        resp = ArgusrrsApi.Tenant_AddRGroupPostApi(rgroup=rgroup1)
        assert resp.status_code == 200
        resp = ArgusrrsApi.Tenant_AddRGroupPostApi(rgroup=rgroup2)
        assert resp.status_code == 200
        # 6. 添加资源，name为空，预期失败
        unit = {
            "host": "",
            "name": "",
            "prom_name": "",
            # "resource_id": "",
            "rgroup": rgroup1,
            "rstype": "SFD",
            "tags": []
        }
        resp = ArgusrrsApi.Tenant_AddResourcePostApi(unit=unit)
        assert resp.status_code != 200
        # 7. 添加资源，rgroup 不存在，预期失败
        unit = {
            "host": "dgsd",
            "name": resource1,
            "prom_name": "12345",
            # "resource_id": "",
            "rgroup": "dd",
            "rstype": "SFD",
            "tags": []
        }
        resp = ArgusrrsApi.Tenant_AddResourcePostApi(unit=unit)
        assert resp.status_code != 200
        # 8. 添加静态资源成功
        unit = {
            "host": "static_host",
            "name": resource1,
            "prom_name": "kubernetes_name:static_host",
            # "resource_id": "",
            "rgroup": rgroup1,
            "rstype": "SFD",
            "tags": [
                {
                    "name": tag_static,
                    "score": 1,
                    "type": "STATIC",
                    "value": "test1"
                }
            ]
        }
        resp = ArgusrrsApi.Tenant_AddResourcePostApi(unit=unit)
        assert resp.status_code == 200
        # 9. 添加动态资源成功
        unit = {
            "host": "dynamic_host",
            "name": resource2,
            "prom_name": "kubernetes_name:dynamic_host",
            # "resource_id": "",
            "rgroup": rgroup2,
            "rstype": "SFD",
            "tags": [
                {
                    "name": tag_dyna,
                    # "score": 1,
                    "type": "DYNAMIC",
                    "value": "test1ddd"
                }
            ]
        }
        resp = ArgusrrsApi.Tenant_AddResourcePostApi(unit=unit)
        assert resp.status_code == 200
        # 10. 查询动态资源
        resp = ArgusrrsApi.Tenant_ListResourceGetApi(rgroup=rgroup2)
        assert resp.status_code == 200
        assert len(resp.json_get("units")) > 0
        for unit_info in resp.json_get("units"):
            if unit_info["name"] == resource2:
                assert unit_info["rgroup"] == rgroup2
                assert unit_info["host"] == "dynamic_host"
                assert unit_info["prom_name"] == "kubernetes_name:dynamic_host"
                assert unit_info["rstype"] == "SFD"
                assert unit_info["resource_id"]
                resource_id2 = unit_info["resource_id"]
                break
        else:
            assert None,"not found resource:%s" % resource2
        # 11. 添加资源， tag name 不存在，预期失败
        unit = {
            "host": "ddddd",
            "name": "动态",
            "prom_name": "12345",
            # "resource_id": "",
            "rgroup": rgroup2,
            "rstype": "SFD",
            "tags": [
                {
                    "name": "动态资源标签11",
                    # "score": 1,
                    "type": "DYNAMIC",
                    "value": "test1ddd"
                }
            ]
        }
        resp = ArgusrrsApi.Tenant_AddResourcePostApi(unit=unit)
        assert resp.status_code != 200
        # 12. 添加资源， tag name 静态标签。value错误， 预期失败
        unit = {
            "host": "ddddd",
            "name": "静态",
            "prom_name": "12345",
            # "resource_id": "",
            "rgroup": rgroup1,
            "rstype": "SFD",
            "tags": [
                {
                    "name": "静态资源标签",
                    # "score": 1,
                    "type": "STATIC",
                    "value": "test1ddd"
                }
            ]
        }
        resp = ArgusrrsApi.Tenant_AddResourcePostApi(unit=unit)
        assert resp.status_code != 200
        # 13. 查询静态资源
        resp = ArgusrrsApi.Tenant_ListResourceGetApi(rgroup=rgroup1)
        assert resp.status_code == 200
        assert len(resp.json_get("units")) > 0
        for unit_info in resp.json_get("units"):
            if unit_info["name"] == resource1:
                assert unit_info["rgroup"] == rgroup1
                assert unit_info["host"] == "static_host"
                assert unit_info["prom_name"] == "kubernetes_name:static_host"
                assert unit_info["rstype"] == "SFD"
                assert unit_info["resource_id"]
                resource_id1 = unit_info["resource_id"]
                break
        else:
            assert None, "not found resource:%s" % resource1
        # 14. 更新资源的静态标签
        unit = {
            "host": "static_host_test2",
            # "name": "",
            "prom_name": "kubernetes_name:static_host_test2",
            "resource_id": resource_id1,
            # "rgroup": "",
            "rstype": "SFD",
            "tags": [
                {
                    "name": tag_static,
                    "score": 1,
                    "type": "STATIC",
                    "value": "test1"
                },
                {
                    "name": tag_dyna,
                    "score": 1,
                    "type": "DYNAMIC",
                    "value": "dynamic"
                }
            ]
        }
        resp = ArgusrrsApi.Tenant_UpdateResourcePostApi(unit=unit)
        assert resp.status_code == 200
        # 15. 查询变更后查询结果
        resp = ArgusrrsApi.Tenant_ListResourceGetApi(rgroup=rgroup1)
        assert resp.status_code == 200
        assert len(resp.json_get("units")) > 0
        for unit_info in resp.json_get("units"):
            if unit_info["name"] == resource1:
                assert unit_info["rgroup"] == rgroup1
                assert unit_info["host"] == "static_host_test2"
                assert unit_info["prom_name"] == "kubernetes_name:static_host_test2"
                assert unit_info["rstype"] == "SFD"
                assert len(unit_info["tags"]) == 2
                break
        else:
            assert None, "not found resource:%s" % resource1
        # 16. 更新资源的动态标签
        unit = {
            "host": "dynamic_host",
            # "name": "",
            "prom_name": "kubernetes_name:dynamic_host",
            "resource_id": resource_id2,
            # "rgroup": "",
            "rstype": "SFD",
            "tags": [
                {
                    "name": tag_dyna,
                    "score": 1,
                    "type": "DYNAMIC",
                    "value": "dynamic_test"
                }
            ]
        }
        resp = ArgusrrsApi.Tenant_UpdateResourcePostApi(unit=unit)
        assert resp.status_code == 200
        # 17. 查询变更后查询结果
        resp = ArgusrrsApi.Tenant_ListResourceGetApi(rgroup=rgroup2)
        assert resp.status_code == 200
        assert len(resp.json_get("units")) > 0
        for unit_info in resp.json_get("units"):
            if unit_info["name"] == resource2:
                assert unit_info["rgroup"] == rgroup2
                assert unit_info["host"] == "dynamic_host"
                assert unit_info["prom_name"] == "kubernetes_name:dynamic_host"
                assert unit_info["rstype"] == "SFD"
                assert unit_info["tags"][0]["value"] == "dynamic_test"
                break
        else:
            assert None, "not found resource:%s" % resource2
        # 18. 删除resource
        resp = ArgusrrsApi.Tenant_DeleteResourcePostApi(resource_id=[resource_id1])
        assert resp.status_code == 200
        resp = ArgusrrsApi.Tenant_DeleteResourcePostApi(resource_id=[resource_id2])
        assert resp.status_code == 200
        # 19. 查询resource， 预期删除后没有了
        resp = ArgusrrsApi.Tenant_ListResourceGetApi(rgroup=rgroup1)
        assert resp.status_code == 200
        assert len(resp.json_get("units")) == 0
        resp = ArgusrrsApi.Tenant_ListResourceGetApi(rgroup=rgroup2)
        assert resp.status_code == 200
        assert len(resp.json_get("units")) == 0
        # 20. 删除rgroup
        resp = ArgusrrsApi.Tenant_DeleteRGroupPostApi(rgroup=rgroup1)
        assert resp.status_code == 200
        resp = ArgusrrsApi.Tenant_DeleteRGroupPostApi(rgroup=rgroup2)
        assert resp.status_code == 200
        # 21. 删除静态标签
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag=tag_static)
        assert resp.status_code == 200
        # 22. 删除动态标签
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag=tag_dyna)
        assert resp.status_code == 200

    def test_scenario_rrs_005_r_Group_AK(self, config_obj, ArgusrrsApi):
        """ """
        """
        1.正常创建
        2.rgroup name没有输入
        3.rgroup name输入错误
        4.删除rgroup
        """
        resp = ArgusrrsApi.Tenant_ListRGroupAkRelationGetApi()
        assert resp.status_code == 200

        # 1.正常创建
        rgroup = "产品线_%s_%s" % (sign_utils.getUuid(5), time_utils.get_time_str())
        resp = ArgusrrsApi.Tenant_AddRGroupPostApi(rgroup=rgroup)
        assert resp.status_code == 200

        # ak = config_obj.Argus.ak
        ak = "ak_%s" % time_utils.get_time_str()
        resp = ArgusrrsApi.Tenant_AddRGroupAkRelationPostApi(rgroup=rgroup, ak=ak)
        assert resp.status_code == 200

        resp = ArgusrrsApi.Tenant_GetRgroupByAkGetApi(header_request_id=None, ak=ak)
        assert resp.status_code == 200
        assert resp.json_get("rgroup") == rgroup
        # 2.rgroup name没有输入
        ak = config_obj.Argus.ak
        resp = ArgusrrsApi.Tenant_AddRGroupAkRelationPostApi(rgroup="", ak=ak)
        assert resp.status_code != 200
        # 3.rgroup name输入错误
        resp = ArgusrrsApi.Tenant_AddRGroupAkRelationPostApi(rgroup="xxxxxx", ak=ak)
        assert resp.status_code != 200
        # 4.删除rgroup
        resp = ArgusrrsApi.Tenant_DeleteRGroupPostApi(rgroup=rgroup)
        assert resp.status_code == 200