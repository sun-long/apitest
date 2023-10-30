#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


# @pytest.mark.checkin
@pytest.mark.AdapterApi
class TestAdapterApi(object):
    """ rasManager Api测试"""

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

    def test_api_NewDB(self, config_obj, AdapterApi):
        """  NewDB """
        name = None
        feature_version = None
        description = None
        db_size = None
        create_bucket = None
        type = None
        extra_db_type = None
        bucket_flattened = None
        bucket_encrypt = None
        enable_isolated_feature_table = None
        resp = AdapterApi.NewDBPostApi(name=name, feature_version=feature_version, description=description,
                                       db_size=db_size, create_bucket=create_bucket, type=type,
                                       extra_db_type=extra_db_type, bucket_flattened=bucket_flattened,
                                       bucket_encrypt=bucket_encrypt,
                                       enable_isolated_feature_table=enable_isolated_feature_table)
        assert resp.status_code == 400
        assert resp.json_get("error") == "requested feature db not exist"
        assert resp.json_get("code") == 3

    def test_api_DeleteDB(self, config_obj, AdapterApi):
        """  DeleteDB """
        db_id = None
        delete_bucket = None
        type = None
        extra_db_type = None
        resp = AdapterApi.DeleteDBPostApi(db_id=db_id, delete_bucket=delete_bucket, type=type,
                                          extra_db_type=extra_db_type)
        assert resp.status_code == 400
        assert resp.json_get("error") == "requested feature db not exist"
        assert resp.json_get("code") == 3

    def test_api_BatchAddImageToDB(self, config_obj, AdapterApi):
        """  BatchAddImageToDB """
        db_id = None
        images = None
        save_images = None
        type = None
        extra_db_type = None
        auto_rotation = None
        resp = AdapterApi.BatchAddImageToDBPostApi(db_id=db_id, images=images, save_images=save_images, type=type,
                                                   extra_db_type=extra_db_type, auto_rotation=auto_rotation)
        assert resp.status_code == 400
        assert resp.json_get("error") == "input image invalid"
        assert resp.json_get("code") == 3

    def test_api_DeleteImageFromDB(self, config_obj, AdapterApi):
        """  DeleteImageFromDB """
        db_id = None
        key = None
        feature_id = None
        delete_image = None
        type = None
        extra_db_type = None
        resp = AdapterApi.DeleteImageFromDBPostApi(db_id=db_id, key=key, feature_id=feature_id,
                                                   delete_image=delete_image, type=type, extra_db_type=extra_db_type)
        assert resp.status_code == 400
        assert resp.json_get("error") == "requested feature db not exist"
        assert resp.json_get("code") == 3

    def test_api_FeatureBatchAdd(self, config_obj, AdapterApi):
        """  FeatureBatchAdd """
        #不传ib id
        resp = AdapterApi.AdapterFeatureBatchAdd()
        assert resp.status_code == 400
        assert resp.json_get("error") == "invalid db id"
        assert resp.json_get("code") == 3


    def test_api_DetectAndExtract(self, config_obj, AdapterApi):
        """  DetectAndExtract """
        image = None
        feature_version = None
        resp = AdapterApi.DetectAndExtractPostApi(image=image, feature_version=feature_version)
        assert resp.status_code == 400
        assert resp.json_get("error") == "input image invalid"
        assert resp.json_get("code") == 3

    def test_api_CompareOneToOne(self, config_obj, AdapterApi):
        """  CompareOneToOne """
        one = None
        other = None
        feature_version = None
        resp = AdapterApi.CompareOneToOnePostApi(one=one, other=other, feature_version=feature_version)
        assert resp.status_code == 400
        assert resp.json_get("error") == "input image invalid"
        assert resp.json_get("code") == 3

    def test_api_SearchImageInDBs(self, config_obj, AdapterApi):
        """  SearchImageInDBs """
        image = None
        dbs = None
        type = None
        dropped_fields = None
        extra_db_type = None
        resp = AdapterApi.SearchImageInDBsPostApi(image=image, dbs=dbs, type=type, dropped_fields=dropped_fields,
                                                  extra_db_type=extra_db_type)
        assert resp.status_code == 400
        assert resp.json_get("error") == "input image invalid"
        assert resp.json_get("code") == 3

    def test_api_FeatureBatchSearch(self, config_obj, AdapterApi):
        """  FeatureBatchSearch """
        resp = AdapterApi.AdapterFeatureBatchSearch(features=None, db_id=None)
        assert resp.status_code == 400
        assert resp.json_get("error") == "empty features"

    def test_api_FeatureBatchGetByKey(self, config_obj, AdapterApi):
        """  FeatureBatchGetByKey """
        resp = AdapterApi.AdapterFeatureBatchGetByKey(db_id=None, key=None)
        assert resp.status_code == 400
        assert resp.json_get("error") == "empty user keys"

    def test_api_TaskNew(self, config_obj, AdapterApi):
        """  TaskNew """
        task = {}
        resp = AdapterApi.TaskNewPostApi(task=task)
        assert resp.status_code == 400
        assert resp.json_get("error.message") == "request field[task.object_type] is invalid"

    def test_api_TaskList(self, config_obj, AdapterApi):
        """  TaskList """
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = AdapterApi.TaskListGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit,
                                         page_request_total=page_request_total)
        assert resp.status_code == 200

    def test_api_TaskDelete(self, config_obj, AdapterApi):
        """  TaskDelete """
        task_id = None
        resp = AdapterApi.TaskDeleteDeleteApi(task_id)
        assert resp.status_code == 200

    # def test_api_CompareFeature(self, config_obj, AdapterApi):
    #     """  CompareFeature """
    #     one = None
    #     other = None
    #     resp = AdapterApi.CompareFeaturePostApi(one=one, other=other)
    #     assert resp.status_code == 400
    #     assert resp.json_get("error")=="feature missing"


    def test_api_DownloadObject(self, config_obj, AdapterApi):
        """  DownloadObject """
        bucket_name = None
        object_key = None
        resp = AdapterApi.DownloadObjectGetApi(bucket_name, object_key)
        assert resp.status_code == 404
        assert resp.json_get("error") == "bucketName:None not found"
