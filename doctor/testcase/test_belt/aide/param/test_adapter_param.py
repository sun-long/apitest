#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestAdapterParam(object):
    """ adapter Param测试"""

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
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('db_size', 'invaliddb_size'),
        ('db_size', ''),
        ('db_size', None),
        ('create_bucket', 'invalidcreate_bucket'),
        ('create_bucket', ''),
        ('create_bucket', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
        ('bucket_flattened', 'invalidbucket_flattened'),
        ('bucket_flattened', ''),
        ('bucket_flattened', None),
        ('bucket_encrypt', 'invalidbucket_encrypt'),
        ('bucket_encrypt', ''),
        ('bucket_encrypt', None),
        ('enable_isolated_feature_table', 'invalidenable_isolated_feature_table'),
        ('enable_isolated_feature_table', ''),
        ('enable_isolated_feature_table', None),
    ])
    def test_api_NewDBInvalidParam(self, invalidParam, config_obj, AdapterApi):
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
        intef = AdapterApi.NewDBPostApi(name=name, feature_version=feature_version, description=description,
                                        db_size=db_size, create_bucket=create_bucket, type=type,
                                        extra_db_type=extra_db_type, bucket_flattened=bucket_flattened,
                                        bucket_encrypt=bucket_encrypt,
                                        enable_isolated_feature_table=enable_isolated_feature_table, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('delete_bucket', 'invaliddelete_bucket'),
        ('delete_bucket', ''),
        ('delete_bucket', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
    ])
    def test_api_DeleteDBInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  DeleteDB """
        db_id = None
        delete_bucket = None
        type = None
        extra_db_type = None
        intef = AdapterApi.DeleteDBPostApi(db_id=db_id, delete_bucket=delete_bucket, type=type,
                                           extra_db_type=extra_db_type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('save_images', 'invalidsave_images'),
        ('save_images', ''),
        ('save_images', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
        ('auto_rotation', 'invalidauto_rotation'),
        ('auto_rotation', ''),
        ('auto_rotation', None),
    ])
    def test_api_BatchAddImageToDBInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  BatchAddImageToDB """
        db_id = None
        images = None
        save_images = None
        type = None
        extra_db_type = None
        auto_rotation = None
        intef = AdapterApi.BatchAddImageToDBPostApi(db_id=db_id, images=images, save_images=save_images, type=type,
                                                    extra_db_type=extra_db_type, auto_rotation=auto_rotation,
                                                    sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('key', 'invalidkey'),
        ('key', ''),
        ('key', None),
        ('feature_id', 'invalidfeature_id'),
        ('feature_id', ''),
        ('feature_id', None),
        ('delete_image', 'invaliddelete_image'),
        ('delete_image', ''),
        ('delete_image', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
    ])
    def test_api_DeleteImageFromDBInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  DeleteImageFromDB """
        db_id = None
        key = None
        feature_id = None
        delete_image = None
        type = None
        extra_db_type = None
        intef = AdapterApi.DeleteImageFromDBPostApi(db_id=db_id, key=key, feature_id=feature_id,
                                                    delete_image=delete_image, type=type, extra_db_type=extra_db_type,
                                                    sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('col_id', 'invalidcol_id'),
        ('col_id', ''),
        ('col_id', None),
        ('items', 'invaliditems'),
        ('items', ''),
        ('items', None),
    ])
    def test_api_FeatureBatchAddInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  FeatureBatchAdd """
        db_type = None
        col_id = None
        items = None
        intef = AdapterApi.FeatureBatchAddPostApi(db_type, col_id, items=items, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_DetectAndExtractInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  DetectAndExtract """
        image = None
        feature_version = None
        intef = AdapterApi.DetectAndExtractPostApi(image=image, feature_version=feature_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('one', 'invalidone'),
        ('one', ''),
        ('one', None),
        ('other', 'invalidother'),
        ('other', ''),
        ('other', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
    ])
    def test_api_CompareOneToOneInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  CompareOneToOne """
        one = None
        other = None
        feature_version = None
        intef = AdapterApi.CompareOneToOnePostApi(one=one, other=other, feature_version=feature_version,
                                                  sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('dbs', 'invaliddbs'),
        ('dbs', ''),
        ('dbs', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('dropped_fields', 'invaliddropped_fields'),
        ('dropped_fields', ''),
        ('dropped_fields', None),
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
    ])
    def test_api_SearchImageInDBsInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  SearchImageInDBs """
        image = None
        dbs = None
        type = None
        dropped_fields = None
        extra_db_type = None
        intef = AdapterApi.SearchImageInDBsPostApi(image=image, dbs=dbs, type=type, dropped_fields=dropped_fields,
                                                   extra_db_type=extra_db_type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('col_id', 'invalidcol_id'),
        ('col_id', ''),
        ('col_id', None),
        ('feature', 'invalidfeature'),
        ('feature', ''),
        ('feature', None),
        ('consistency', 'invalidconsistency'),
        ('consistency', ''),
        ('consistency', None),
        ('top_k', 'invalidtop_k'),
        ('top_k', ''),
        ('top_k', None),
        ('min_score', 'invalidmin_score'),
        ('min_score', ''),
        ('min_score', None),
        ('return_raw_feature', 'invalidreturn_raw_feature'),
        ('return_raw_feature', ''),
        ('return_raw_feature', None),
        ('dropped_fields', 'invaliddropped_fields'),
        ('dropped_fields', ''),
        ('dropped_fields', None),
    ])
    def test_api_FeatureBatchSearchInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  FeatureBatchSearch """
        db_type = None
        col_id = None
        feature = None
        consistency = None
        top_k = None
        min_score = None
        return_raw_feature = None
        dropped_fields = None
        intef = AdapterApi.FeatureBatchSearchPostApi(db_type, col_id, feature=feature, consistency=consistency,
                                                     top_k=top_k, min_score=min_score,
                                                     return_raw_feature=return_raw_feature,
                                                     dropped_fields=dropped_fields, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('col_id', 'invalidcol_id'),
        ('col_id', ''),
        ('col_id', None),
        ('consistency', 'invalidconsistency'),
        ('consistency', ''),
        ('consistency', None),
        ('ignore_details', 'invalidignore_details'),
        ('ignore_details', ''),
        ('ignore_details', None),
        ('keys', 'invalidkeys'),
        ('keys', ''),
        ('keys', None),
    ])
    def test_api_FeatureBatchGetByKeyInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  FeatureBatchGetByKey """
        db_type = None
        col_id = None
        consistency = None
        ignore_details = None
        keys = None
        intef = AdapterApi.FeatureBatchGetByKeyPostApi(db_type, col_id, consistency=consistency,
                                                       ignore_details=ignore_details, keys=keys, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    # liangchen
    @pytest.mark.parametrize("invalidParam", [
        # roi传None是连roi这个key都去掉,ROI框的个数和点的个数没有限制
        # 坐标点不符合要求，包含负数,#key,value, status_code, message
        ('task.task_object_config.algo_config.data.rules.0.roi.vertices.1.x', -1, 500,
         "roi points vertex must between 0 and 1"),
        # roi只有1个坐标点
        ('task.task_object_config.algo_config.data.rules.0.roi.vertices', [{"x": 0, "y": 0}], 500,
         "roi must have at least 2 points"),
        # roi有0个坐标点,目前可以成功，预期不能成功，有bug
        # ('task.task_object_config.algo_config.data.rules.0.roi.vertices', [], 500,
        #  "roi must have at least 2 points"),
        # roi不是list
        ('task.task_object_config.algo_config.data.rules.0.roi', -1, 500, "cannot unmarshal number into Go struct "
                                                                          "field Algo"),
        # rtsp流不填
        ('task.source_address', "invalidrtsp", 500, "address must begin with rtsp:// or file")

    ])
    def test_api_TaskNewInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  TaskNew """
        camera_info = config_obj.Clients.SubDevice.camera2
        source_address = camera_info['rtsp']
        i = 1
        task = {
            "object_type": "OBJECT_ALGO",
            "source_address": source_address,
            "camera_info": {
                "camera_id": "99999999999999999999",
                "internal_id": {
                    "region_id": 2,
                    "camera_idx": 2
                }
            },
            "task_object_config": {
                "algo_config": {
                    "app_name": "com.sensetime.algo.home.based.care",
                    "app_version": 10001,
                    "data": {
                        "rules": [
                            {
                                "rule_id": "99999999999999999999",
                                "type": "ST_TUMBLE",
                                "roi": {
                                    "vertices": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        },
                                        {
                                            "x": 1,
                                            "y": 0
                                        },
                                        {
                                            "x": 1,
                                            "y": 1
                                        },
                                        {
                                            "x": 0,
                                            "y": 1
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            }
        }
        intef = AdapterApi.TaskNewPostApi(task=task, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        i = 1
        assert resp.status_code == invalidParam[2]
        assert invalidParam[3] in resp.json_get("error.message")

    @pytest.mark.parametrize("invalidParam", [
        ('page_request_offset', 'invalidpage_request_offset'),
        ('page_request_offset', ''),
        ('page_request_offset', None),
        ('page_request_limit', 'invalidpage_request_limit'),
        ('page_request_limit', ''),
        ('page_request_limit', None),
        ('page_request_total', 'invalidpage_request_total'),
        ('page_request_total', ''),
        ('page_request_total', None),
    ])
    def test_api_TaskListInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  TaskList """
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = AdapterApi.TaskListGetApi(page_request_offset=page_request_offset,
                                          page_request_limit=page_request_limit, page_request_total=page_request_total,
                                          sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_TaskDeleteInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  TaskDelete """
        task_id = None
        intef = AdapterApi.TaskDeleteDeleteApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('one', 'invalidone'),
        ('one', ''),
        ('one', None),
        ('other', 'invalidother'),
        ('other', ''),
        ('other', None),
    ])
    def test_api_CompareFeatureInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  CompareFeature """
        one = None
        other = None
        intef = AdapterApi.CompareFeaturePostApi(one=one, other=other, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_DownloadObjectInvalidParam(self, invalidParam, config_obj, AdapterApi):
        """  DownloadObject """
        bucket_name = None
        object_key = None
        intef = AdapterApi.DownloadObjectGetApi(bucket_name, object_key, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200
