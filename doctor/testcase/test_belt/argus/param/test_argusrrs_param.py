#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestArgusrrsParam(object):
    """ argusRrs Param测试"""

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
        ('rgroup', 'invalidrgroup'),
        ('rgroup', ''),
        ('rgroup', None),
    ])
    def test_api_Tenant_AddRGroupInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        rgroup = None
        intef = ArgusrrsApi.Tenant_AddRGroupPostApi(rgroup=rgroup, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('rgroup', 'invalidrgroup'),
        ('rgroup', ''),
        ('rgroup', None),
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
    ])
    def test_api_Tenant_AddRGroupAkRelationInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        rgroup = None
        ak = None
        intef = ArgusrrsApi.Tenant_AddRGroupAkRelationPostApi(rgroup=rgroup, ak=ak, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('unit', 'invalidunit'),
        ('unit', ''),
        ('unit', None),
    ])
    def test_api_Tenant_AddResourceInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        unit = None
        intef = ArgusrrsApi.Tenant_AddResourcePostApi(unit=unit, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('tag', 'invalidtag'),
        ('tag', ''),
        ('tag', None),
    ])
    def test_api_Tenant_AddTagInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        tag = None
        intef = ArgusrrsApi.Tenant_AddTagPostApi(tag=tag, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('rgroup', 'invalidrgroup'),
        ('rgroup', ''),
        ('rgroup', None),
    ])
    def test_api_Tenant_DeleteRGroupInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        rgroup = None
        intef = ArgusrrsApi.Tenant_DeleteRGroupPostApi(rgroup=rgroup, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('resource_id', 'invalidresource_id'),
        ('resource_id', ''),
        ('resource_id', None),
    ])
    def test_api_Tenant_DeleteResourceInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        resource_id = None
        intef = ArgusrrsApi.Tenant_DeleteResourcePostApi(resource_id=resource_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('tag', 'invalidtag'),
        ('tag', ''),
        ('tag', None),
    ])
    def test_api_Tenant_DeleteTagInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        tag = None
        intef = ArgusrrsApi.Tenant_DeleteTagPostApi(tag=tag, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('header_request_id', 'invalidheader_request_id'),
        ('header_request_id', ''),
        ('header_request_id', None),
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
    ])
    def test_api_Tenant_GetRgroupByAkInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        ak = None
        intef = ArgusrrsApi.Tenant_GetRgroupByAkGetApi(header_request_id=header_request_id, ak=ak, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('header_request_id', 'invalidheader_request_id'),
        ('header_request_id', ''),
        ('header_request_id', None),
        ('rstype', 'invalidrstype'),
        ('rstype', ''),
        ('rstype', None),
    ])
    def test_api_Tenant_ListAllocateGroupInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        rstype = None
        intef = ArgusrrsApi.Tenant_ListAllocateGroupGetApi(header_request_id=header_request_id, rstype=rstype, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('header_request_id', 'invalidheader_request_id'),
        ('header_request_id', ''),
        ('header_request_id', None),
    ])
    def test_api_Tenant_ListRGroupInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        intef = ArgusrrsApi.Tenant_ListRGroupGetApi(header_request_id=header_request_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('header_request_id', 'invalidheader_request_id'),
        ('header_request_id', ''),
        ('header_request_id', None),
    ])
    def test_api_Tenant_ListRGroupAkRelationInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        intef = ArgusrrsApi.Tenant_ListRGroupAkRelationGetApi(header_request_id=header_request_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('header_request_id', 'invalidheader_request_id'),
        ('header_request_id', ''),
        ('header_request_id', None),
        ('rgroup', 'invalidrgroup'),
        ('rgroup', ''),
        ('rgroup', None),
    ])
    def test_api_Tenant_ListResourceInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        rgroup = None
        intef = ArgusrrsApi.Tenant_ListResourceGetApi(header_request_id=header_request_id, rgroup=rgroup, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('header_request_id', 'invalidheader_request_id'),
        ('header_request_id', ''),
        ('header_request_id', None),
        ('rstype', 'invalidrstype'),
        ('rstype', ''),
        ('rstype', None),
    ])
    def test_api_Tenant_ListResourceByRsTypeInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        rstype = None
        intef = ArgusrrsApi.Tenant_ListResourceByRsTypeGetApi(header_request_id=header_request_id, rstype=rstype, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('header_request_id', 'invalidheader_request_id'),
        ('header_request_id', ''),
        ('header_request_id', None),
    ])
    def test_api_Tenant_ListTagInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        header_request_id = None
        intef = ArgusrrsApi.Tenant_ListTagGetApi(header_request_id=header_request_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('tags', 'invalidtags'),
        ('tags', ''),
        ('tags', None),
        ('rsType', 'invalidrsType'),
        ('rsType', ''),
        ('rsType', None),
    ])
    def test_api_Tenant_LookupInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        ak = None
        tags = None
        rsType = None
        intef = ArgusrrsApi.Tenant_LookupPostApi(ak=ak, tags=tags, rsType=rsType, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('rgroup', 'invalidrgroup'),
        ('rgroup', ''),
        ('rgroup', None),
        ('new_rgroup', 'invalidnew_rgroup'),
        ('new_rgroup', ''),
        ('new_rgroup', None),
    ])
    def test_api_Tenant_UpdateRGroupInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        rgroup = None
        new_rgroup = None
        intef = ArgusrrsApi.Tenant_UpdateRGroupPostApi(rgroup=rgroup, new_rgroup=new_rgroup, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('unit', 'invalidunit'),
        ('unit', ''),
        ('unit', None),
    ])
    def test_api_Tenant_UpdateResourceInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        unit = None
        intef = ArgusrrsApi.Tenant_UpdateResourcePostApi(unit=unit, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('tag', 'invalidtag'),
        ('tag', ''),
        ('tag', None),
    ])
    def test_api_Tenant_UpdateTagInvalidParam(self, invalidParam, config_obj, ArgusrrsApi):
        """   """
        tag = None
        intef = ArgusrrsApi.Tenant_UpdateTagPostApi(tag=tag, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
