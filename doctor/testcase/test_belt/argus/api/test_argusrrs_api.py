#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestArgusrrsApi(object):
    """ argusRrs Api测试"""

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

    def test_api_Tenant_AddRGroup(self, config_obj, ArgusrrsApi):
        """   """
        rgroup = None
        resp = ArgusrrsApi.Tenant_AddRGroupPostApi(rgroup=rgroup)
        assert resp.status_code == 200

    def test_api_Tenant_AddRGroupAkRelation(self, config_obj, ArgusrrsApi):
        """   """
        rgroup = None
        ak = None
        resp = ArgusrrsApi.Tenant_AddRGroupAkRelationPostApi(rgroup=rgroup, ak=ak)
        assert resp.status_code == 200

    def test_api_Tenant_AddResource(self, config_obj, ArgusrrsApi):
        """   """
        unit = None
        resp = ArgusrrsApi.Tenant_AddResourcePostApi(unit=unit)
        assert resp.status_code == 200

    def test_api_Tenant_AddTag(self, config_obj, ArgusrrsApi):
        """   """
        tag = None
        resp = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag)
        assert resp.status_code == 200

    def test_api_Tenant_DeleteRGroup(self, config_obj, ArgusrrsApi):
        """   """
        rgroup = None
        resp = ArgusrrsApi.Tenant_DeleteRGroupPostApi(rgroup=rgroup)
        assert resp.status_code == 200

    def test_api_Tenant_DeleteResource(self, config_obj, ArgusrrsApi):
        """   """
        resource_id = None
        resp = ArgusrrsApi.Tenant_DeleteResourcePostApi(resource_id=resource_id)
        assert resp.status_code == 200

    def test_api_Tenant_DeleteTag(self, config_obj, ArgusrrsApi):
        """   """
        tag = None
        resp = ArgusrrsApi.Tenant_DeleteTagPostApi(tag=tag)
        assert resp.status_code == 200

    def test_api_Tenant_GetRgroupByAk(self, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        ak = None
        resp = ArgusrrsApi.Tenant_GetRgroupByAkGetApi(header_request_id=header_request_id, ak=ak)
        assert resp.status_code == 200

    def test_api_Tenant_ListAllocateGroup(self, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        rstype = None
        resp = ArgusrrsApi.Tenant_ListAllocateGroupGetApi(header_request_id=header_request_id, rstype=rstype)
        assert resp.status_code == 200

    def test_api_Tenant_ListRGroup(self, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        resp = ArgusrrsApi.Tenant_ListRGroupGetApi(header_request_id=header_request_id)
        assert resp.status_code == 200

    def test_api_Tenant_ListRGroupAkRelation(self, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        resp = ArgusrrsApi.Tenant_ListRGroupAkRelationGetApi(header_request_id=header_request_id)
        assert resp.status_code == 200

    def test_api_Tenant_ListResource(self, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        rgroup = None
        resp = ArgusrrsApi.Tenant_ListResourceGetApi(header_request_id=header_request_id, rgroup=rgroup)
        assert resp.status_code == 200

    def test_api_Tenant_ListResourceByRsType(self, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        rstype = None
        resp = ArgusrrsApi.Tenant_ListResourceByRsTypeGetApi(header_request_id=header_request_id, rstype=rstype)
        assert resp.status_code == 200

    def test_api_Tenant_ListTag(self, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        resp = ArgusrrsApi.Tenant_ListTagGetApi(header_request_id=header_request_id)
        assert resp.status_code == 200

    def test_api_Tenant_Lookup(self, config_obj, ArgusrrsApi):
        """   """
        ak = None
        tags = None
        rsType = None
        resp = ArgusrrsApi.Tenant_LookupPostApi(ak=ak, tags=tags, rsType=rsType)
        assert resp.status_code == 200

    def test_api_Tenant_UpdateRGroup(self, config_obj, ArgusrrsApi):
        """   """
        rgroup = None
        new_rgroup = None
        resp = ArgusrrsApi.Tenant_UpdateRGroupPostApi(rgroup=rgroup, new_rgroup=new_rgroup)
        assert resp.status_code == 200

    def test_api_Tenant_UpdateResource(self, config_obj, ArgusrrsApi):
        """   """
        unit = None
        resp = ArgusrrsApi.Tenant_UpdateResourcePostApi(unit=unit)
        assert resp.status_code == 200

    def test_api_Tenant_UpdateTag(self, config_obj, ArgusrrsApi):
        """   """
        tag = None
        resp = ArgusrrsApi.Tenant_UpdateTagPostApi(tag=tag)
        assert resp.status_code == 200
