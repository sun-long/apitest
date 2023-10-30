#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestAdapterApi(object):
    """ adapter Api测试"""

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
        resp = AdapterApi.NewDBPostApi(name=name, feature_version=feature_version, description=description, db_size=db_size, create_bucket=create_bucket, type=type, extra_db_type=extra_db_type, bucket_flattened=bucket_flattened, bucket_encrypt=bucket_encrypt, enable_isolated_feature_table=enable_isolated_feature_table)
        assert resp.status_code == 200

    def test_api_DeleteDB(self, config_obj, AdapterApi):
        """  DeleteDB """
        db_id = None
        delete_bucket = None
        type = None
        extra_db_type = None
        resp = AdapterApi.DeleteDBPostApi(db_id=db_id, delete_bucket=delete_bucket, type=type, extra_db_type=extra_db_type)
        assert resp.status_code == 200

    def test_api_BatchAddImageToDB(self, config_obj, AdapterApi):
        """  BatchAddImageToDB """
        db_id = None
        images = None
        save_images = None
        type = None
        extra_db_type = None
        auto_rotation = None
        resp = AdapterApi.BatchAddImageToDBPostApi(db_id=db_id, images=images, save_images=save_images, type=type, extra_db_type=extra_db_type, auto_rotation=auto_rotation)
        assert resp.status_code == 200

    def test_api_DeleteImageFromDB(self, config_obj, AdapterApi):
        """  DeleteImageFromDB """
        db_id = None
        key = None
        feature_id = None
        delete_image = None
        type = None
        extra_db_type = None
        resp = AdapterApi.DeleteImageFromDBPostApi(db_id=db_id, key=key, feature_id=feature_id, delete_image=delete_image, type=type, extra_db_type=extra_db_type)
        assert resp.status_code == 200

    def test_api_FeatureBatchAdd(self, config_obj, AdapterApi):
        """  FeatureBatchAdd """
        db_type = None
        col_id = None
        items = None
        resp = AdapterApi.FeatureBatchAddPostApi(db_type, col_id, items=items)
        assert resp.status_code == 200

    def test_api_DetectAndExtract(self, config_obj, AdapterApi):
        """  DetectAndExtract """
        image = None
        feature_version = None
        resp = AdapterApi.DetectAndExtractPostApi(image=image, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_CompareOneToOne(self, config_obj, AdapterApi):
        """  CompareOneToOne """
        one = None
        other = None
        feature_version = None
        resp = AdapterApi.CompareOneToOnePostApi(one=one, other=other, feature_version=feature_version)
        assert resp.status_code == 200

    def test_api_SearchImageInDBs(self, config_obj, AdapterApi):
        """  SearchImageInDBs """
        image = None
        dbs = None
        type = None
        dropped_fields = None
        extra_db_type = None
        resp = AdapterApi.SearchImageInDBsPostApi(image=image, dbs=dbs, type=type, dropped_fields=dropped_fields, extra_db_type=extra_db_type)
        assert resp.status_code == 200

    def test_api_FeatureBatchSearch(self, config_obj, AdapterApi):
        """  FeatureBatchSearch """
        db_type = None
        col_id = None
        feature = None
        consistency = None
        top_k = None
        min_score = None
        return_raw_feature = None
        dropped_fields = None
        resp = AdapterApi.FeatureBatchSearchPostApi(db_type, col_id, feature=feature, consistency=consistency, top_k=top_k, min_score=min_score, return_raw_feature=return_raw_feature, dropped_fields=dropped_fields)
        assert resp.status_code == 200

    def test_api_FeatureBatchGetByKey(self, config_obj, AdapterApi):
        """  FeatureBatchGetByKey """
        db_type = None
        col_id = None
        consistency = None
        ignore_details = None
        keys = None
        resp = AdapterApi.FeatureBatchGetByKeyPostApi(db_type, col_id, consistency=consistency, ignore_details=ignore_details, keys=keys)
        assert resp.status_code == 200

    def test_api_TaskNew(self, config_obj, AdapterApi):
        """  TaskNew """
        task = None
        resp = AdapterApi.TaskNewPostApi(task=task)
        assert resp.status_code == 200

    def test_api_TaskList(self, config_obj, AdapterApi):
        """  TaskList """
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = AdapterApi.TaskListGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    def test_api_TaskDelete(self, config_obj, AdapterApi):
        """  TaskDelete """
        task_id = None
        resp = AdapterApi.TaskDeleteDeleteApi(task_id)
        assert resp.status_code == 200

    def test_api_CompareFeature(self, config_obj, AdapterApi):
        """  CompareFeature """
        one = None
        other = None
        resp = AdapterApi.CompareFeaturePostApi(one=one, other=other)
        assert resp.status_code == 200

    def test_api_DownloadObject(self, config_obj, AdapterApi):
        """  DownloadObject """
        bucket_name = None
        object_key = None
        resp = AdapterApi.DownloadObjectGetApi(bucket_name, object_key)
        assert resp.status_code == 200
