#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestArgusdatacenterParam(object):
    """ argusDatacenter Param测试"""

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
        ('ak', 'invalidak'),
        ('ak', ''),
        ('ak', None),
        ('store_id', 'invalidstore_id'),
        ('store_id', ''),
        ('store_id', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('camera_id', 'invalidcamera_id'),
        ('camera_id', ''),
        ('camera_id', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', None),
        ('request_id', 'invalidrequest_id'),
        ('request_id', ''),
        ('request_id', None),
        ('start_time', 'invalidstart_time'),
        ('start_time', ''),
        ('start_time', None),
        ('end_time', 'invalidend_time'),
        ('end_time', ''),
        ('end_time', None),
        ('page_number', 'invalidpage_number'),
        ('page_number', ''),
        ('page_number', None),
        ('page_size', 'invalidpage_size'),
        ('page_size', ''),
        ('page_size', None),
        ('mis_request_ids', 'invalidmis_request_ids'),
        ('mis_request_ids', ''),
        ('mis_request_ids', None),
    ])
    def test_api_DC_GetOriginMetaInfoInvalidParam(self, invalidParam, config_obj, ArgusdatacenterApi):
        """  origin_meta_info API """
        ak = None
        store_id = None
        device_id = None
        camera_id = None
        person_id = None
        request_id = None
        start_time = None
        end_time = None
        page_number = None
        page_size = None
        mis_request_ids = None
        intef = ArgusdatacenterApi.DC_GetOriginMetaInfoGetApi(ak=ak, store_id=store_id, device_id=device_id, camera_id=camera_id, person_id=person_id, request_id=request_id, start_time=start_time, end_time=end_time, page_number=page_number, page_size=page_size, mis_request_ids=mis_request_ids, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200
