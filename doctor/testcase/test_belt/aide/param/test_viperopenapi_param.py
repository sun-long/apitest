#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestViperopenapiParam(object):
    """ viperOpenApi Param测试"""

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
        ('batch_objects', 'invalidbatch_objects'),
        ('batch_objects', ''),
        ('batch_objects', None),
    ])
    def test_api_kafkaCallbackExampleCallbackInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  Callback """
        batch_objects = None
        intef = ViperopenapiApi.kafkaCallbackExampleCallbackPostApi(batch_objects=batch_objects, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('messages', 'invalidmessages'),
        ('messages', ''),
        ('messages', None),
    ])
    def test_api_streamMessageCallbackInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  Callback """
        messages = None
        intef = ViperopenapiApi.streamMessageCallbackPostApi(messages=messages, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
        ('period_start', 'invalidperiod_start'),
        ('period_start', ''),
        ('period_start', None),
        ('period_end', 'invalidperiod_end'),
        ('period_end', ''),
        ('period_end', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
    ])
    def test_api_batchVideoProcessJobListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobList """
        page_offset = None
        page_limit = None
        page_total = None
        period_start = None
        period_end = None
        status = None
        intef = ViperopenapiApi.batchVideoProcessJobListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, period_start=period_start, period_end=period_end, status=status, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
    ])
    def test_api_batchVideoProcessJobNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobNew """
        config = None
        intef = ViperopenapiApi.batchVideoProcessJobNewPostApi(config=config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_batchVideoProcessJobDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobDelete """
        job_id = None
        intef = ViperopenapiApi.batchVideoProcessJobDeleteDeleteApi(job_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_batchVideoProcessJobGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobGet """
        job_id = None
        intef = ViperopenapiApi.batchVideoProcessJobGetGetApi(job_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_batchVideoProcessJobCancelInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobCancel """
        job_id = None
        intef = ViperopenapiApi.batchVideoProcessJobCancelPostApi(job_id, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('Threshold', 'invalidThreshold'),
        ('Threshold', ''),
        ('Threshold', None),
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
        ('is_delete_anonymous_cluster', 'invalidis_delete_anonymous_cluster'),
        ('is_delete_anonymous_cluster', ''),
        ('is_delete_anonymous_cluster', None),
        ('is_delete_identified_cluster', 'invalidis_delete_identified_cluster'),
        ('is_delete_identified_cluster', ''),
        ('is_delete_identified_cluster', None),
    ])
    def test_api_clusteringJobMgrDeleteClusterBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteClusterBeforeDate """
        Threshold = None
        date = None
        is_delete_anonymous_cluster = None
        is_delete_identified_cluster = None
        intef = ViperopenapiApi.clusteringJobMgrDeleteClusterBeforeDatePostApi(Threshold=Threshold, date=date, is_delete_anonymous_cluster=is_delete_anonymous_cluster, is_delete_identified_cluster=is_delete_identified_cluster, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('data_sources', 'invaliddata_sources'),
        ('data_sources', ''),
        ('data_sources', None),
        ('min_score', 'invalidmin_score'),
        ('min_score', ''),
        ('min_score', None),
    ])
    def test_api_clusteringJobMgrLabelingByExtraDataSourcesInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  LabelingByExtraDataSources """
        data_sources = None
        min_score = None
        intef = ViperopenapiApi.clusteringJobMgrLabelingByExtraDataSourcesPostApi(data_sources=data_sources, min_score=min_score, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_clusteringJobMgrMatrixGenerationInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  MatrixGeneration """
        intef = ViperopenapiApi.clusteringJobMgrMatrixGenerationPostApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('catalog', 'invalidcatalog'),
        ('catalog', ''),
        ('catalog', None),
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
    ])
    def test_api_dataFusionDeleteJobsBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteJobsBeforeDate """
        catalog = None
        date = None
        intef = ViperopenapiApi.dataFusionDeleteJobsBeforeDatePostApi(catalog=catalog, date=date, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_dataFusionGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.dataFusionGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_dataFusionJobListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobList """
        type = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.dataFusionJobListGetApi(type=type, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
    ])
    def test_api_dataFusionJobNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobNew """
        config = None
        intef = ViperopenapiApi.dataFusionJobNewPostApi(config=config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_dataFusionJobDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobDelete """
        job_id = None
        intef = ViperopenapiApi.dataFusionJobDeleteDeleteApi(job_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_dataFusionJobGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobGet """
        job_id = None
        intef = ViperopenapiApi.dataFusionJobGetGetApi(job_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_dataFusionJobCancelInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobCancel """
        job_id = None
        intef = ViperopenapiApi.dataFusionJobCancelPostApi(job_id, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_batchDBIntersectionJobListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.batchDBIntersectionJobListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
    ])
    def test_api_batchDBIntersectionJobNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobNew """
        config = None
        intef = ViperopenapiApi.batchDBIntersectionJobNewPostApi(config=config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_batchDBIntersectionJobDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobDelete """
        job_id = None
        intef = ViperopenapiApi.batchDBIntersectionJobDeleteDeleteApi(job_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_batchDBIntersectionJobGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobGet """
        job_id = None
        intef = ViperopenapiApi.batchDBIntersectionJobGetGetApi(job_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_batchDBIntersectionJobCancelInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobCancel """
        job_id = None
        intef = ViperopenapiApi.batchDBIntersectionJobCancelPostApi(job_id, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraBatchMgrBatchManagerFileDownloadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchManagerFileDownload """
        path = None
        intef = ViperopenapiApi.infraBatchMgrBatchManagerFileDownloadGetApi(path, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraBatchMgrBatchManagerHdfsDownloadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchManagerHdfsDownload """
        path = None
        intef = ViperopenapiApi.infraBatchMgrBatchManagerHdfsDownloadGetApi(path, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraBatchMgrGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.infraBatchMgrGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
        ('catalog', 'invalidcatalog'),
        ('catalog', ''),
        ('catalog', None),
        ('period_start', 'invalidperiod_start'),
        ('period_start', ''),
        ('period_start', None),
        ('period_end', 'invalidperiod_end'),
        ('period_end', ''),
        ('period_end', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
    ])
    def test_api_infraBatchMgrJobListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobList """
        page_offset = None
        page_limit = None
        page_total = None
        catalog = None
        period_start = None
        period_end = None
        status = None
        intef = ViperopenapiApi.infraBatchMgrJobListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, catalog=catalog, period_start=period_start, period_end=period_end, status=status, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('job', 'invalidjob'),
        ('job', ''),
        ('job', None),
    ])
    def test_api_infraBatchMgrJobNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobNew """
        job = None
        intef = ViperopenapiApi.infraBatchMgrJobNewPostApi(job=job, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraBatchMgrJobDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobDelete """
        job_id = None
        intef = ViperopenapiApi.infraBatchMgrJobDeleteDeleteApi(job_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraBatchMgrJobGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobGet """
        job_id = None
        intef = ViperopenapiApi.infraBatchMgrJobGetGetApi(job_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraBatchMgrJobCancelInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobCancel """
        job_id = None
        intef = ViperopenapiApi.infraBatchMgrJobCancelPostApi(job_id, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('catalog', 'invalidcatalog'),
        ('catalog', ''),
        ('catalog', None),
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
    ])
    def test_api_infraBatchMgrDeleteJobsBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteJobsBeforeDate """
        catalog = None
        date = None
        intef = ViperopenapiApi.infraBatchMgrDeleteJobsBeforeDatePostApi(catalog=catalog, date=date, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraConsoleCertificateInfosInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  CertificateInfos """
        intef = ViperopenapiApi.infraConsoleCertificateInfosGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_infraConsoleComponentListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ComponentList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.infraConsoleComponentListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
        ('index_type', 'invalidindex_type'),
        ('index_type', ''),
        ('index_type', None),
    ])
    def test_api_infraConsoleDeleteESBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteESBeforeDate """
        date = None
        index_type = None
        intef = ViperopenapiApi.infraConsoleDeleteESBeforeDatePostApi(date=date, index_type=index_type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraConsoleFeatureVersionsInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureVersions """
        intef = ViperopenapiApi.infraConsoleFeatureVersionsGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraConsoleGetFilteredStorageConfigInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetFilteredStorageConfig """
        intef = ViperopenapiApi.infraConsoleGetFilteredStorageConfigGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('filtered_storage_disable', 'invalidfiltered_storage_disable'),
        ('filtered_storage_disable', ''),
        ('filtered_storage_disable', None),
    ])
    def test_api_infraConsoleUpdateFilteredStorageConfigInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  UpdateFilteredStorageConfig """
        filtered_storage_disable = None
        intef = ViperopenapiApi.infraConsoleUpdateFilteredStorageConfigPostApi(filtered_storage_disable=filtered_storage_disable, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraConsoleGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.infraConsoleGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraConsoleStatisticsModuleInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  StatisticsModule """
        module_name = None
        intef = ViperopenapiApi.infraConsoleStatisticsModuleGetApi(module_name, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_id', 'invalidcamera_id'),
        ('camera_id', ''),
        ('camera_id', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('module_name', 'invalidmodule_name'),
        ('module_name', ''),
        ('module_name', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
    ])
    def test_api_infraConsoleStatisticsModuleByCameraInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  StatisticsModuleByCamera """
        module_name = None
        camera_id = None
        device_id = None
        task_id = None
        intef = ViperopenapiApi.infraConsoleStatisticsModuleByCameraPostApi(module_name, camera_id=camera_id, device_id=device_id, task_id=task_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_infraConsoleStatisticsNodeListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  StatisticsNodeList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.infraConsoleStatisticsNodeListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('password', 'invalidpassword'),
        ('password', ''),
        ('password', None),
        ('username', 'invalidusername'),
        ('username', ''),
        ('username', None),
    ])
    def test_api_infraConsoleAPIUserCredentialGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  APIUserCredentialGet """
        username = None
        password = None
        intef = ViperopenapiApi.infraConsoleAPIUserCredentialGetPostApi(username, password=password, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraModelMgrBlobDownloadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BlobDownload """
        blob_id = None
        intef = ViperopenapiApi.infraModelMgrBlobDownloadGetApi(blob_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraModelMgrBlobUploadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BlobUpload """
        blob_id = None
        intef = ViperopenapiApi.infraModelMgrBlobUploadPostApi(blob_id, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraModelMgrGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.infraModelMgrGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('model_path_type', 'invalidmodel_path_type'),
        ('model_path_type', ''),
        ('model_path_type', None),
        ('model_path_sub_type', 'invalidmodel_path_sub_type'),
        ('model_path_sub_type', ''),
        ('model_path_sub_type', None),
        ('model_path_runtime', 'invalidmodel_path_runtime'),
        ('model_path_runtime', ''),
        ('model_path_runtime', None),
        ('model_path_hardware', 'invalidmodel_path_hardware'),
        ('model_path_hardware', ''),
        ('model_path_hardware', None),
        ('model_path_name', 'invalidmodel_path_name'),
        ('model_path_name', ''),
        ('model_path_name', None),
    ])
    def test_api_infraModelMgrModelListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ModelList """
        model_path_type = None
        model_path_sub_type = None
        model_path_runtime = None
        model_path_hardware = None
        model_path_name = None
        intef = ViperopenapiApi.infraModelMgrModelListGetApi(model_path_type=model_path_type, model_path_sub_type=model_path_sub_type, model_path_runtime=model_path_runtime, model_path_hardware=model_path_hardware, model_path_name=model_path_name, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('model', 'invalidmodel'),
        ('model', ''),
        ('model', None),
        ('overwrite', 'invalidoverwrite'),
        ('overwrite', ''),
        ('overwrite', None),
    ])
    def test_api_infraModelMgrModelNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ModelNew """
        model = None
        overwrite = None
        intef = ViperopenapiApi.infraModelMgrModelNewPostApi(model=model, overwrite=overwrite, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraModelMgrModelSynchronizeInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ModelSynchronize """
        intef = ViperopenapiApi.infraModelMgrModelSynchronizePostApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraModelMgrModelDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ModelDelete """
        path.type = None
        path.sub_type = None
        path.runtime = None
        path.hardware = None
        path.name = None
        intef = ViperopenapiApi.infraModelMgrModelDeleteDeleteApi(path.type, path.sub_type, path.runtime, path.hardware, path.name, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraModelMgrModelGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ModelGet """
        path.type = None
        path.sub_type = None
        path.runtime = None
        path.hardware = None
        path.name = None
        intef = ViperopenapiApi.infraModelMgrModelGetGetApi(path.type, path.sub_type, path.runtime, path.hardware, path.name, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraOSGDownloadObjectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DownloadObject """
        bucket_name = None
        object_key = None
        intef = ViperopenapiApi.infraOSGDownloadObjectGetApi(bucket_name, object_key, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraOSGListBucketsInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ListBuckets """
        intef = ViperopenapiApi.infraOSGListBucketsGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bucket_info', 'invalidbucket_info'),
        ('bucket_info', ''),
        ('bucket_info', None),
    ])
    def test_api_infraOSGCreateBucketInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  CreateBucket """
        bucket_info = None
        intef = ViperopenapiApi.infraOSGCreateBucketPutApi(bucket_info=bucket_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraOSGGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.infraOSGGetSystemInfoPostApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('force', 'invalidforce'),
        ('force', ''),
        ('force', None),
    ])
    def test_api_infraOSGDeleteBucketInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteBucket """
        bucket_name = None
        force = None
        intef = ViperopenapiApi.infraOSGDeleteBucketDeleteApi(bucket_name, force=force, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
        ('marker', 'invalidmarker'),
        ('marker', ''),
        ('marker', None),
        ('limit', 'invalidlimit'),
        ('limit', ''),
        ('limit', None),
    ])
    def test_api_infraOSGListObjectsInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ListObjects """
        bucket_name = None
        date = None
        marker = None
        limit = None
        intef = ViperopenapiApi.infraOSGListObjectsGetApi(bucket_name, date=date, marker=marker, limit=limit, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bucket_name', 'invalidbucket_name'),
        ('bucket_name', ''),
        ('bucket_name', None),
        ('encryption_method', 'invalidencryption_method'),
        ('encryption_method', ''),
        ('encryption_method', None),
        ('save_days', 'invalidsave_days'),
        ('save_days', ''),
        ('save_days', None),
    ])
    def test_api_infraOSGUpdateBucketInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  UpdateBucket """
        bucket_name = None
        encryption_method = None
        save_days = None
        intef = ViperopenapiApi.infraOSGUpdateBucketPutApi(bucket_name, encryption_method=encryption_method, save_days=save_days, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bucket_name', 'invalidbucket_name'),
        ('bucket_name', ''),
        ('bucket_name', None),
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
    ])
    def test_api_infraOSGDeleteObjectsBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteObjectsBeforeDate """
        bucket_name = None
        date = None
        intef = ViperopenapiApi.infraOSGDeleteObjectsBeforeDatePostApi(bucket_name, date=date, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bucket_name', 'invalidbucket_name'),
        ('bucket_name', ''),
        ('bucket_name', None),
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
    ])
    def test_api_infraOSGDeleteObjectsByDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteObjectsByDate """
        bucket_name = None
        date = None
        intef = ViperopenapiApi.infraOSGDeleteObjectsByDatePostApi(bucket_name, date=date, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('blob', 'invalidblob'),
        ('blob', ''),
        ('blob', None),
        ('bucket_name', 'invalidbucket_name'),
        ('bucket_name', ''),
        ('bucket_name', None),
        ('object_info', 'invalidobject_info'),
        ('object_info', ''),
        ('object_info', None),
    ])
    def test_api_infraOSGPutObjectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PutObject """
        bucket_name = None
        blob = None
        object_info = None
        intef = ViperopenapiApi.infraOSGPutObjectPostApi(bucket_name, blob=blob, object_info=object_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bucket_name', 'invalidbucket_name'),
        ('bucket_name', ''),
        ('bucket_name', None),
        ('object_count', 'invalidobject_count'),
        ('object_count', ''),
        ('object_count', None),
    ])
    def test_api_infraOSGReserveObjectKeysInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ReserveObjectKeys """
        bucket_name = None
        object_count = None
        intef = ViperopenapiApi.infraOSGReserveObjectKeysPostApi(bucket_name, object_count=object_count, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bucket_name', 'invalidbucket_name'),
        ('bucket_name', ''),
        ('bucket_name', None),
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
        ('limit', 'invalidlimit'),
        ('limit', ''),
        ('limit', None),
        ('marker', 'invalidmarker'),
        ('marker', ''),
        ('marker', None),
    ])
    def test_api_infraOSGScanObjectsInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ScanObjects """
        bucket_name = None
        date = None
        limit = None
        marker = None
        intef = ViperopenapiApi.infraOSGScanObjectsPostApi(bucket_name, date=date, limit=limit, marker=marker, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraOSGDeleteObjectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteObject """
        bucket_name = None
        object_key = None
        intef = ViperopenapiApi.infraOSGDeleteObjectDeleteApi(bucket_name, object_key, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraOSGGetObjectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetObject """
        bucket_name = None
        object_key = None
        intef = ViperopenapiApi.infraOSGGetObjectGetApi(bucket_name, object_key, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraRaidExporterGetRaidInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetRaidInfo """
        intef = ViperopenapiApi.infraRaidExporterGetRaidInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_infraSparkJobMgrArtifactListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ArtifactList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.infraSparkJobMgrArtifactListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraSparkJobMgrArtifactDownloadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ArtifactDownload """
        name = None
        intef = ViperopenapiApi.infraSparkJobMgrArtifactDownloadGetApi(name, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraSparkJobMgrArtifactUploadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ArtifactUpload """
        name = None
        intef = ViperopenapiApi.infraSparkJobMgrArtifactUploadPostApi(name, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraSparkJobMgrArtifactDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ArtifactDelete """
        name = None
        intef = ViperopenapiApi.infraSparkJobMgrArtifactDeleteDeleteApi(name, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('return_content', 'invalidreturn_content'),
        ('return_content', ''),
        ('return_content', None),
    ])
    def test_api_infraSparkJobMgrArtifactGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ArtifactGet """
        name = None
        return_content = None
        intef = ViperopenapiApi.infraSparkJobMgrArtifactGetGetApi(name, return_content=return_content, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('allow_overwrite', 'invalidallow_overwrite'),
        ('allow_overwrite', ''),
        ('allow_overwrite', None),
        ('blob', 'invalidblob'),
        ('blob', ''),
        ('blob', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
    ])
    def test_api_infraSparkJobMgrArtifactNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ArtifactNew """
        name = None
        allow_overwrite = None
        blob = None
        intef = ViperopenapiApi.infraSparkJobMgrArtifactNewPostApi(name, allow_overwrite=allow_overwrite, blob=blob, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
        ('catalog', 'invalidcatalog'),
        ('catalog', ''),
        ('catalog', None),
        ('period_start', 'invalidperiod_start'),
        ('period_start', ''),
        ('period_start', None),
        ('period_end', 'invalidperiod_end'),
        ('period_end', ''),
        ('period_end', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
    ])
    def test_api_infraSparkJobMgrJobListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobList """
        page_offset = None
        page_limit = None
        page_total = None
        catalog = None
        period_start = None
        period_end = None
        status = None
        intef = ViperopenapiApi.infraSparkJobMgrJobListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, catalog=catalog, period_start=period_start, period_end=period_end, status=status, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('job', 'invalidjob'),
        ('job', ''),
        ('job', None),
    ])
    def test_api_infraSparkJobMgrJobNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobNew """
        job = None
        intef = ViperopenapiApi.infraSparkJobMgrJobNewPostApi(job=job, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraSparkJobMgrJobDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobDelete """
        job_id = None
        intef = ViperopenapiApi.infraSparkJobMgrJobDeleteDeleteApi(job_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraSparkJobMgrJobGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobGet """
        job_id = None
        intef = ViperopenapiApi.infraSparkJobMgrJobGetGetApi(job_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraSparkJobMgrJobCancelInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  JobCancel """
        job_id = None
        intef = ViperopenapiApi.infraSparkJobMgrJobCancelPostApi(job_id, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraStorageMgrNamespaceListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceList """
        intef = ViperopenapiApi.infraStorageMgrNamespaceListGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraStorageMgrNamespaceDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceDelete """
        ns_id = None
        intef = ViperopenapiApi.infraStorageMgrNamespaceDeleteDeleteApi(ns_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ns_id', 'invalidns_id'),
        ('ns_id', ''),
        ('ns_id', None),
    ])
    def test_api_infraStorageMgrNamespaceNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceNew """
        ns_id = None
        intef = ViperopenapiApi.infraStorageMgrNamespaceNewPostApi(ns_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraStorageMgrOSGStorageGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  OSGStorageGet """
        intef = ViperopenapiApi.infraStorageMgrOSGStorageGetGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('force', 'invalidforce'),
        ('force', ''),
        ('force', None),
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('nas_infos', 'invalidnas_infos'),
        ('nas_infos', ''),
        ('nas_infos', None),
        ('nas_overall_usage_in_gb_threshold', 'invalidnas_overall_usage_in_gb_threshold'),
        ('nas_overall_usage_in_gb_threshold', ''),
        ('nas_overall_usage_in_gb_threshold', None),
    ])
    def test_api_infraStorageMgrOSGStorageReplaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  OSGStorageReplace """
        force = None
        mode = None
        nas_infos = None
        nas_overall_usage_in_gb_threshold = None
        intef = ViperopenapiApi.infraStorageMgrOSGStorageReplacePutApi(force=force, mode=mode, nas_infos=nas_infos, nas_overall_usage_in_gb_threshold=nas_overall_usage_in_gb_threshold, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraStorageMgrStorageProtectPolicyGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  StorageProtectPolicyGet """
        intef = ViperopenapiApi.infraStorageMgrStorageProtectPolicyGetGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('policy', 'invalidpolicy'),
        ('policy', ''),
        ('policy', None),
    ])
    def test_api_infraStorageMgrStorageProtectPolicyReplaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  StorageProtectPolicyReplace """
        policy = None
        intef = ViperopenapiApi.infraStorageMgrStorageProtectPolicyReplacePutApi(policy=policy, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_infraStorageMgrStorageRuleListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  StorageRuleList """
        intef = ViperopenapiApi.infraStorageMgrStorageRuleListGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('rule', 'invalidrule'),
        ('rule', ''),
        ('rule', None),
    ])
    def test_api_infraStorageMgrStorageRuleReplaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  StorageRuleReplace """
        rule = None
        intef = ViperopenapiApi.infraStorageMgrStorageRuleReplacePutApi(rule=rule, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreAppTemplateListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppTemplateList """
        intef = ViperopenapiApi.algoStoreAppTemplateListGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('template', 'invalidtemplate'),
        ('template', ''),
        ('template', None),
    ])
    def test_api_algoStoreAppTemplateNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppTemplateNew """
        template = None
        intef = ViperopenapiApi.algoStoreAppTemplateNewPostApi(template=template, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreAppTemplateDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppTemplateDelete """
        template_id = None
        intef = ViperopenapiApi.algoStoreAppTemplateDeleteDeleteApi(template_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('filters_period_start', 'invalidfilters_period_start'),
        ('filters_period_start', ''),
        ('filters_period_start', None),
        ('filters_period_end', 'invalidfilters_period_end'),
        ('filters_period_end', ''),
        ('filters_period_end', None),
        ('filters_user_algo_name', 'invalidfilters_user_algo_name'),
        ('filters_user_algo_name', ''),
        ('filters_user_algo_name', None),
        ('filters_algo_types', 'invalidfilters_algo_types'),
        ('filters_algo_types', ''),
        ('filters_algo_types', None),
        ('filters_tag_ids', 'invalidfilters_tag_ids'),
        ('filters_tag_ids', ''),
        ('filters_tag_ids', None),
        ('filters_status', 'invalidfilters_status'),
        ('filters_status', ''),
        ('filters_status', None),
        ('filters_sale_type', 'invalidfilters_sale_type'),
        ('filters_sale_type', ''),
        ('filters_sale_type', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
    ])
    def test_api_algoStoreAppListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppList """
        filters_period_start = None
        filters_period_end = None
        filters_user_algo_name = None
        filters_algo_types = None
        filters_tag_ids = None
        filters_status = None
        filters_sale_type = None
        page_offset = None
        page_limit = None
        page_total = None
        reversed = None
        intef = ViperopenapiApi.algoStoreAppListGetApi(filters_period_start=filters_period_start, filters_period_end=filters_period_end, filters_user_algo_name=filters_user_algo_name, filters_algo_types=filters_algo_types, filters_tag_ids=filters_tag_ids, filters_status=filters_status, filters_sale_type=filters_sale_type, page_offset=page_offset, page_limit=page_limit, page_total=page_total, reversed=reversed, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('meta', 'invalidmeta'),
        ('meta', ''),
        ('meta', None),
        ('models', 'invalidmodels'),
        ('models', ''),
        ('models', None),
        ('process_configs', 'invalidprocess_configs'),
        ('process_configs', ''),
        ('process_configs', None),
        ('template_id', 'invalidtemplate_id'),
        ('template_id', ''),
        ('template_id', None),
    ])
    def test_api_algoStoreAppNewFromTemplateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppNewFromTemplate """
        meta = None
        models = None
        process_configs = None
        template_id = None
        intef = ViperopenapiApi.algoStoreAppNewFromTemplatePostApi(meta=meta, models=models, process_configs=process_configs, template_id=template_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreAppUploadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppUpload """
        intef = ViperopenapiApi.algoStoreAppUploadPostApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreAppDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppDelete """
        app_id = None
        intef = ViperopenapiApi.algoStoreAppDeleteDeleteApi(app_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreAppGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppGet """
        app_id = None
        intef = ViperopenapiApi.algoStoreAppGetGetApi(app_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('app_id', 'invalidapp_id'),
        ('app_id', ''),
        ('app_id', None),
        ('tag_ids', 'invalidtag_ids'),
        ('tag_ids', ''),
        ('tag_ids', None),
    ])
    def test_api_algoStoreAppUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppUpdate """
        app_id = None
        tag_ids = None
        intef = ViperopenapiApi.algoStoreAppUpdatePatchApi(app_id, tag_ids=tag_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('app_id', 'invalidapp_id'),
        ('app_id', ''),
        ('app_id', None),
        ('user_configs', 'invaliduser_configs'),
        ('user_configs', ''),
        ('user_configs', None),
    ])
    def test_api_algoStoreAppInstanceNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppInstanceNew """
        app_id = None
        user_configs = None
        intef = ViperopenapiApi.algoStoreAppInstanceNewPostApi(app_id, user_configs=user_configs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreAppInstanceDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppInstanceDelete """
        app_id = None
        instance_id = None
        intef = ViperopenapiApi.algoStoreAppInstanceDeleteDeleteApi(app_id, instance_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreAppInstanceGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppInstanceGet """
        app_id = None
        instance_id = None
        intef = ViperopenapiApi.algoStoreAppInstanceGetGetApi(app_id, instance_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('app_id', 'invalidapp_id'),
        ('app_id', ''),
        ('app_id', None),
        ('hardware', 'invalidhardware'),
        ('hardware', ''),
        ('hardware', None),
        ('instance_id', 'invalidinstance_id'),
        ('instance_id', ''),
        ('instance_id', None),
        ('replicas', 'invalidreplicas'),
        ('replicas', ''),
        ('replicas', None),
    ])
    def test_api_algoStoreAppInstanceUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppInstanceUpdate """
        app_id = None
        instance_id = None
        hardware = None
        replicas = None
        intef = ViperopenapiApi.algoStoreAppInstanceUpdatePatchApi(app_id, instance_id, hardware=hardware, replicas=replicas, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreAppGetByNameVersionInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppGetByNameVersion """
        user_algo_name = None
        version = None
        intef = ViperopenapiApi.algoStoreAppGetByNameVersionGetApi(user_algo_name, version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreDocDownloadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DocDownload """
        user_algo_name = None
        version = None
        doc_name = None
        intef = ViperopenapiApi.algoStoreDocDownloadGetApi(user_algo_name, version, doc_name, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_algoStoreInstanceListByNameVersionInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  InstanceListByNameVersion """
        user_algo_name = None
        version = None
        reversed = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.algoStoreInstanceListByNameVersionGetApi(user_algo_name, version, reversed=reversed, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('app_id', 'invalidapp_id'),
        ('app_id', ''),
        ('app_id', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('algo_types', 'invalidalgo_types'),
        ('algo_types', ''),
        ('algo_types', None),
        ('states', 'invalidstates'),
        ('states', ''),
        ('states', None),
        ('period_start', 'invalidperiod_start'),
        ('period_start', ''),
        ('period_start', None),
        ('period_end', 'invalidperiod_end'),
        ('period_end', ''),
        ('period_end', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_algoStoreEdgeInstanceListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  EdgeInstanceList """
        app_id = None
        device_id = None
        algo_types = None
        states = None
        period_start = None
        period_end = None
        reversed = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.algoStoreEdgeInstanceListGetApi(app_id=app_id, device_id=device_id, algo_types=algo_types, states=states, period_start=period_start, period_end=period_end, reversed=reversed, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('app_id', 'invalidapp_id'),
        ('app_id', ''),
        ('app_id', None),
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('registry_id', 'invalidregistry_id'),
        ('registry_id', ''),
        ('registry_id', None),
        ('user_configs', 'invaliduser_configs'),
        ('user_configs', ''),
        ('user_configs', None),
    ])
    def test_api_algoStoreEdgeInstanceNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  EdgeInstanceNew """
        app_id = None
        device_id = None
        registry_id = None
        user_configs = None
        intef = ViperopenapiApi.algoStoreEdgeInstanceNewPostApi(app_id=app_id, device_id=device_id, registry_id=registry_id, user_configs=user_configs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreEdgeInstanceDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  EdgeInstanceDelete """
        instance_uuid = None
        intef = ViperopenapiApi.algoStoreEdgeInstanceDeleteDeleteApi(instance_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreEdgeInstanceGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  EdgeInstanceGet """
        instance_uuid = None
        intef = ViperopenapiApi.algoStoreEdgeInstanceGetGetApi(instance_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('instance_uuid', 'invalidinstance_uuid'),
        ('instance_uuid', ''),
        ('instance_uuid', None),
        ('user_configs', 'invaliduser_configs'),
        ('user_configs', ''),
        ('user_configs', None),
    ])
    def test_api_algoStoreEdgeInstanceUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  EdgeInstanceUpdate """
        instance_uuid = None
        user_configs = None
        intef = ViperopenapiApi.algoStoreEdgeInstanceUpdatePatchApi(instance_uuid, user_configs=user_configs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.algoStoreGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('filters_algo_types', 'invalidfilters_algo_types'),
        ('filters_algo_types', ''),
        ('filters_algo_types', None),
        ('filters_states', 'invalidfilters_states'),
        ('filters_states', ''),
        ('filters_states', None),
        ('filters_period_start', 'invalidfilters_period_start'),
        ('filters_period_start', ''),
        ('filters_period_start', None),
        ('filters_period_end', 'invalidfilters_period_end'),
        ('filters_period_end', ''),
        ('filters_period_end', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_algoStoreInstanceListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  InstanceList """
        filters_algo_types = None
        filters_states = None
        filters_period_start = None
        filters_period_end = None
        reversed = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.algoStoreInstanceListGetApi(filters_algo_types=filters_algo_types, filters_states=filters_states, filters_period_start=filters_period_start, filters_period_end=filters_period_end, reversed=reversed, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('group_resource_quotas', 'invalidgroup_resource_quotas'),
        ('group_resource_quotas', ''),
        ('group_resource_quotas', None),
        ('ips_resource_quotas', 'invalidips_resource_quotas'),
        ('ips_resource_quotas', ''),
        ('ips_resource_quotas', None),
        ('vps_resource_quotas', 'invalidvps_resource_quotas'),
        ('vps_resource_quotas', ''),
        ('vps_resource_quotas', None),
    ])
    def test_api_algoStoreReallocateResourceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ReallocateResource """
        group_resource_quotas = None
        ips_resource_quotas = None
        vps_resource_quotas = None
        intef = ViperopenapiApi.algoStoreReallocateResourcePostApi(group_resource_quotas=group_resource_quotas, ips_resource_quotas=ips_resource_quotas, vps_resource_quotas=vps_resource_quotas, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_algoStoreTagListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TagList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.algoStoreTagListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('tag', 'invalidtag'),
        ('tag', ''),
        ('tag', None),
    ])
    def test_api_algoStoreTagNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TagNew """
        tag = None
        intef = ViperopenapiApi.algoStoreTagNewPostApi(tag=tag, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_algoStoreTagDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TagDelete """
        tag_id = None
        intef = ViperopenapiApi.algoStoreTagDeleteDeleteApi(tag_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_searchWrapperBatchCompareInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchCompare """
        requests = None
        intef = ViperopenapiApi.searchWrapperBatchComparePostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_searchWrapperBatchCompareByImageInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchCompareByImage """
        requests = None
        intef = ViperopenapiApi.searchWrapperBatchCompareByImagePostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('auto_rotation', 'invalidauto_rotation'),
        ('auto_rotation', ''),
        ('auto_rotation', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('save_images', 'invalidsave_images'),
        ('save_images', ''),
        ('save_images', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_apiWrapperBatchAddImageToDBInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchAddImageToDB """
        auto_rotation = None
        db_id = None
        extra_db_type = None
        images = None
        save_images = None
        type = None
        intef = ViperopenapiApi.apiWrapperBatchAddImageToDBPostApi(auto_rotation=auto_rotation, db_id=db_id, extra_db_type=extra_db_type, images=images, save_images=save_images, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
        ('feature_id', 'invalidfeature_id'),
        ('feature_id', ''),
        ('feature_id', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('key', 'invalidkey'),
        ('key', ''),
        ('key', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_apiWrapperCompareImageInDBInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  CompareImageInDB """
        db_id = None
        extra_db_type = None
        feature_id = None
        image = None
        key = None
        type = None
        intef = ViperopenapiApi.apiWrapperCompareImageInDBPostApi(db_id=db_id, extra_db_type=extra_db_type, feature_id=feature_id, image=image, key=key, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('one', 'invalidone'),
        ('one', ''),
        ('one', None),
        ('other', 'invalidother'),
        ('other', ''),
        ('other', None),
    ])
    def test_api_apiWrapperCompareOneToOneInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  CompareOneToOne """
        feature_version = None
        one = None
        other = None
        intef = ViperopenapiApi.apiWrapperCompareOneToOnePostApi(feature_version=feature_version, one=one, other=other, sendRequest=False)
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
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_apiWrapperDeleteDBInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteDB """
        db_id = None
        delete_bucket = None
        extra_db_type = None
        type = None
        intef = ViperopenapiApi.apiWrapperDeleteDBPostApi(db_id=db_id, delete_bucket=delete_bucket, extra_db_type=extra_db_type, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('delete_image', 'invaliddelete_image'),
        ('delete_image', ''),
        ('delete_image', None),
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
        ('feature_id', 'invalidfeature_id'),
        ('feature_id', ''),
        ('feature_id', None),
        ('key', 'invalidkey'),
        ('key', ''),
        ('key', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_apiWrapperDeleteImageFromDBInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteImageFromDB """
        db_id = None
        delete_image = None
        extra_db_type = None
        feature_id = None
        key = None
        type = None
        intef = ViperopenapiApi.apiWrapperDeleteImageFromDBPostApi(db_id=db_id, delete_image=delete_image, extra_db_type=extra_db_type, feature_id=feature_id, key=key, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
    ])
    def test_api_apiWrapperDetectAndExtractInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DetectAndExtract """
        feature_version = None
        image = None
        intef = ViperopenapiApi.apiWrapperDetectAndExtractPostApi(feature_version=feature_version, image=image, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_apiWrapperGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.apiWrapperGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bucket_encrypt', 'invalidbucket_encrypt'),
        ('bucket_encrypt', ''),
        ('bucket_encrypt', None),
        ('bucket_flattened', 'invalidbucket_flattened'),
        ('bucket_flattened', ''),
        ('bucket_flattened', None),
        ('create_bucket', 'invalidcreate_bucket'),
        ('create_bucket', ''),
        ('create_bucket', None),
        ('db_size', 'invaliddb_size'),
        ('db_size', ''),
        ('db_size', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('enable_isolated_feature_table', 'invalidenable_isolated_feature_table'),
        ('enable_isolated_feature_table', ''),
        ('enable_isolated_feature_table', None),
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_apiWrapperNewDBInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NewDB """
        bucket_encrypt = None
        bucket_flattened = None
        create_bucket = None
        db_size = None
        description = None
        enable_isolated_feature_table = None
        extra_db_type = None
        feature_version = None
        name = None
        type = None
        intef = ViperopenapiApi.apiWrapperNewDBPostApi(bucket_encrypt=bucket_encrypt, bucket_flattened=bucket_flattened, create_bucket=create_bucket, db_size=db_size, description=description, enable_isolated_feature_table=enable_isolated_feature_table, extra_db_type=extra_db_type, feature_version=feature_version, name=name, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('dbs', 'invaliddbs'),
        ('dbs', ''),
        ('dbs', None),
        ('dropped_fields', 'invaliddropped_fields'),
        ('dropped_fields', ''),
        ('dropped_fields', None),
        ('extra_db_type', 'invalidextra_db_type'),
        ('extra_db_type', ''),
        ('extra_db_type', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_apiWrapperSearchImageInDBsInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  SearchImageInDBs """
        dbs = None
        dropped_fields = None
        extra_db_type = None
        image = None
        type = None
        intef = ViperopenapiApi.apiWrapperSearchImageInDBsPostApi(dbs=dbs, dropped_fields=dropped_fields, extra_db_type=extra_db_type, image=image, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageProcessWrapperBatchCompareFeatureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        requests = None
        intef = ViperopenapiApi.imageProcessWrapperBatchCompareFeaturePostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageProcessWrapperBatchDetectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetect """
        requests = None
        intef = ViperopenapiApi.imageProcessWrapperBatchDetectPostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageProcessWrapperBatchDetectAndExtractAllInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll """
        requests = None
        intef = ViperopenapiApi.imageProcessWrapperBatchDetectAndExtractAllPostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageProcessWrapperBatchExtractWithLocationInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchExtractWithLocation """
        requests = None
        intef = ViperopenapiApi.imageProcessWrapperBatchExtractWithLocationPostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('common_config', 'invalidcommon_config'),
        ('common_config', ''),
        ('common_config', None),
        ('engine_configs', 'invalidengine_configs'),
        ('engine_configs', ''),
        ('engine_configs', None),
        ('filters', 'invalidfilters'),
        ('filters', ''),
        ('filters', None),
        ('search_mode', 'invalidsearch_mode'),
        ('search_mode', ''),
        ('search_mode', None),
    ])
    def test_api_searchWrapperSearchInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  Search """
        common_config = None
        engine_configs = None
        filters = None
        search_mode = None
        intef = ViperopenapiApi.searchWrapperSearchPostApi(common_config=common_config, engine_configs=engine_configs, filters=filters, search_mode=search_mode, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('boundings', 'invalidboundings'),
        ('boundings', ''),
        ('boundings', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('search_request', 'invalidsearch_request'),
        ('search_request', ''),
        ('search_request', None),
    ])
    def test_api_searchWrapperSearchByImageInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  SearchByImage """
        boundings = None
        image = None
        search_request = None
        intef = ViperopenapiApi.searchWrapperSearchByImagePostApi(boundings=boundings, image=image, search_request=search_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('tags', 'invalidtags'),
        ('tags', ''),
        ('tags', None),
    ])
    def test_api_cameraManagerExportCamerasInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ExportCameras """
        tags = None
        intef = ViperopenapiApi.cameraManagerExportCamerasPostApi(tags=tags, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('configRequest', 'invalidconfigRequest'),
        ('configRequest', ''),
        ('configRequest', None),
    ])
    def test_api_cameraManagerGB28181LocalConfigReplaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigReplace """
        configRequest.local_uuid = None
        configRequest = None
        intef = ViperopenapiApi.cameraManagerGB28181LocalConfigReplacePutApi(configRequest.local_uuid, configRequest=configRequest, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerGB28181LocalConfigInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigInfo """
        uuid = None
        intef = ViperopenapiApi.cameraManagerGB28181LocalConfigInfoGetApi(uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('bypass_cache', 'invalidbypass_cache'),
        ('bypass_cache', ''),
        ('bypass_cache', None),
        ('internal_ids', 'invalidinternal_ids'),
        ('internal_ids', ''),
        ('internal_ids', None),
    ])
    def test_api_cameraManagerGetCamerasByInternalIDInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetCamerasByInternalID """
        bypass_cache = None
        internal_ids = None
        intef = ViperopenapiApi.cameraManagerGetCamerasByInternalIDPostApi(bypass_cache=bypass_cache, internal_ids=internal_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('cameras', 'invalidcameras'),
        ('cameras', ''),
        ('cameras', None),
        ('export_timestamp', 'invalidexport_timestamp'),
        ('export_timestamp', ''),
        ('export_timestamp', None),
        ('version', 'invalidversion'),
        ('version', ''),
        ('version', None),
        ('zones', 'invalidzones'),
        ('zones', ''),
        ('zones', None),
    ])
    def test_api_cameraManagerImportCamerasInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ImportCameras """
        cameras = None
        export_timestamp = None
        version = None
        zones = None
        intef = ViperopenapiApi.cameraManagerImportCamerasPostApi(cameras=cameras, export_timestamp=export_timestamp, version=version, zones=zones, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerNamespaceListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerNamespaceListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('namespace_request', 'invalidnamespace_request'),
        ('namespace_request', ''),
        ('namespace_request', None),
    ])
    def test_api_cameraManagerNamespaceNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceNew """
        namespace_request.ns_id = None
        namespace_request = None
        intef = ViperopenapiApi.cameraManagerNamespaceNewPostApi(namespace_request.ns_id, namespace_request=namespace_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('namespace_request', 'invalidnamespace_request'),
        ('namespace_request', ''),
        ('namespace_request', None),
    ])
    def test_api_cameraManagerNamespaceReplaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceReplace """
        namespace_request.ns_id = None
        namespace_request = None
        intef = ViperopenapiApi.cameraManagerNamespaceReplacePutApi(namespace_request.ns_id, namespace_request=namespace_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerNamespaceDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceDelete """
        ns_id = None
        intef = ViperopenapiApi.cameraManagerNamespaceDeleteDeleteApi(ns_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerNamespaceInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceInfo """
        ns_id = None
        intef = ViperopenapiApi.cameraManagerNamespaceInfoGetApi(ns_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('platform_type', 'invalidplatform_type'),
        ('platform_type', ''),
        ('platform_type', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerPlatformListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformList """
        platform_type = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerPlatformListGetApi(platform_type=platform_type, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('platform_config_request', 'invalidplatform_config_request'),
        ('platform_config_request', ''),
        ('platform_config_request', None),
    ])
    def test_api_cameraManagerPlatformNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformNew """
        platform_config_request = None
        intef = ViperopenapiApi.cameraManagerPlatformNewPostApi(platform_config_request=platform_config_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerPlatformDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformDelete """
        platform_id = None
        intef = ViperopenapiApi.cameraManagerPlatformDeleteDeleteApi(platform_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerPlatformInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformInfo """
        platform_id = None
        intef = ViperopenapiApi.cameraManagerPlatformInfoGetApi(platform_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('platform_config_request', 'invalidplatform_config_request'),
        ('platform_config_request', ''),
        ('platform_config_request', None),
        ('platform_id', 'invalidplatform_id'),
        ('platform_id', ''),
        ('platform_id', None),
    ])
    def test_api_cameraManagerPlatformReplaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformReplace """
        platform_id = None
        platform_config_request = None
        intef = ViperopenapiApi.cameraManagerPlatformReplacePutApi(platform_id, platform_config_request=platform_config_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerPlatformCameraListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformCameraList """
        platform_id = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerPlatformCameraListGetApi(platform_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_id', 'invaliddevice_id'),
        ('device_id', ''),
        ('device_id', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerGetCamerasFromPlatformInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetCamerasFromPlatform """
        platform_id = None
        device_id = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerGetCamerasFromPlatformGetApi(platform_id, device_id=device_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('item_type', 'invaliditem_type'),
        ('item_type', ''),
        ('item_type', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerPlatformCatalogItemsInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformCatalogItems """
        platform_id = None
        item_type = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerPlatformCatalogItemsGetApi(platform_id, item_type=item_type, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('platform_id', 'invalidplatform_id'),
        ('platform_id', ''),
        ('platform_id', None),
    ])
    def test_api_cameraManagerPlatformCatalogSendInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformCatalogSend """
        platform_id = None
        intef = ViperopenapiApi.cameraManagerPlatformCatalogSendPostApi(platform_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuids', 'invaliddevice_uuids'),
        ('device_uuids', ''),
        ('device_uuids', None),
    ])
    def test_api_cameraManagerBatchDeleteSharedDevicesInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDeleteSharedDevices """
        platform_id = None
        device_uuids = None
        intef = ViperopenapiApi.cameraManagerBatchDeleteSharedDevicesDeleteApi(platform_id, device_uuids=device_uuids, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuids', 'invaliddevice_uuids'),
        ('device_uuids', ''),
        ('device_uuids', None),
        ('platform_id', 'invalidplatform_id'),
        ('platform_id', ''),
        ('platform_id', None),
    ])
    def test_api_cameraManagerBatchAddSharedDevicesInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchAddSharedDevices """
        platform_id = None
        device_uuids = None
        intef = ViperopenapiApi.cameraManagerBatchAddSharedDevicesPostApi(platform_id, device_uuids=device_uuids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerPlatformSubscribeListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformSubscribeList """
        platform_id = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerPlatformSubscribeListGetApi(platform_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerPlatformSubscribeDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformSubscribeDelete """
        platform_id = None
        id = None
        intef = ViperopenapiApi.cameraManagerPlatformSubscribeDeleteDeleteApi(platform_id, id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('platform_subscribe_request', 'invalidplatform_subscribe_request'),
        ('platform_subscribe_request', ''),
        ('platform_subscribe_request', None),
    ])
    def test_api_cameraManagerPlatformSubscribeNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PlatformSubscribeNew """
        platform_subscribe_request.platform_id = None
        platform_subscribe_request = None
        intef = ViperopenapiApi.cameraManagerPlatformSubscribeNewPostApi(platform_subscribe_request.platform_id, platform_subscribe_request=platform_subscribe_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('created_time_range', 'invalidcreated_time_range'),
        ('created_time_range', ''),
        ('created_time_range', None),
        ('display_name', 'invaliddisplay_name'),
        ('display_name', ''),
        ('display_name', None),
        ('include_removed', 'invalidinclude_removed'),
        ('include_removed', ''),
        ('include_removed', None),
        ('ingress_types', 'invalidingress_types'),
        ('ingress_types', ''),
        ('ingress_types', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('platform_id', 'invalidplatform_id'),
        ('platform_id', ''),
        ('platform_id', None),
        ('source_types', 'invalidsource_types'),
        ('source_types', ''),
        ('source_types', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
        ('time_ascended', 'invalidtime_ascended'),
        ('time_ascended', ''),
        ('time_ascended', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerSearchCamerasInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  SearchCameras """
        camera_uuid = None
        created_time_range = None
        display_name = None
        include_removed = None
        ingress_types = None
        page = None
        platform_id = None
        source_types = None
        status = None
        time_ascended = None
        zone_uuid = None
        intef = ViperopenapiApi.cameraManagerSearchCamerasPostApi(camera_uuid=camera_uuid, created_time_range=created_time_range, display_name=display_name, include_removed=include_removed, ingress_types=ingress_types, page=page, platform_id=platform_id, source_types=source_types, status=status, time_ascended=time_ascended, zone_uuid=zone_uuid, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('tags', 'invalidtags'),
        ('tags', ''),
        ('tags', None),
        ('bounding', 'invalidbounding'),
        ('bounding', ''),
        ('bounding', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
    ])
    def test_api_cameraManagerSearchCamerasInBoundingInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  SearchCamerasInBounding """
        tags = None
        bounding = None
        page = None
        intef = ViperopenapiApi.cameraManagerSearchCamerasInBoundingPostApi(tags=tags, bounding=bounding, page=page, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('tags', 'invalidtags'),
        ('tags', ''),
        ('tags', None),
        ('distance', 'invaliddistance'),
        ('distance', ''),
        ('distance', None),
        ('geo_point', 'invalidgeo_point'),
        ('geo_point', ''),
        ('geo_point', None),
        ('nearest_k', 'invalidnearest_k'),
        ('nearest_k', ''),
        ('nearest_k', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
    ])
    def test_api_cameraManagerSearchNearestCamerasInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  SearchNearestCameras """
        tags = None
        distance = None
        geo_point = None
        nearest_k = None
        page = None
        intef = ViperopenapiApi.cameraManagerSearchNearestCamerasPostApi(tags=tags, distance=distance, geo_point=geo_point, nearest_k=nearest_k, page=page, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('created_time_range', 'invalidcreated_time_range'),
        ('created_time_range', ''),
        ('created_time_range', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
        ('ingress_types', 'invalidingress_types'),
        ('ingress_types', ''),
        ('ingress_types', None),
        ('object_types', 'invalidobject_types'),
        ('object_types', ''),
        ('object_types', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('status', 'invalidstatus'),
        ('status', ''),
        ('status', None),
        ('time_ascended', 'invalidtime_ascended'),
        ('time_ascended', ''),
        ('time_ascended', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerSearchTasksInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  SearchTasks """
        camera_uuid = None
        created_time_range = None
        id = None
        ingress_types = None
        object_types = None
        page = None
        status = None
        time_ascended = None
        zone_uuid = None
        intef = ViperopenapiApi.cameraManagerSearchTasksPostApi(camera_uuid=camera_uuid, created_time_range=created_time_range, id=id, ingress_types=ingress_types, object_types=object_types, page=page, status=status, time_ascended=time_ascended, zone_uuid=zone_uuid, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerTagListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TagList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerTagListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerZoneListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerZoneListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_request', 'invalidcamera_request'),
        ('camera_request', ''),
        ('camera_request', None),
    ])
    def test_api_cameraManagerZoneCameraNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraNew """
        camera_request.zone_uuid = None
        camera_request.uuid = None
        camera_request = None
        intef = ViperopenapiApi.cameraManagerZoneCameraNewPostApi(camera_request.zone_uuid, camera_request.uuid, camera_request=camera_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_request', 'invalidcamera_request'),
        ('camera_request', ''),
        ('camera_request', None),
    ])
    def test_api_cameraManagerZoneCameraReplaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraReplace """
        camera_request.zone_uuid = None
        camera_request.uuid = None
        camera_request = None
        intef = ViperopenapiApi.cameraManagerZoneCameraReplacePutApi(camera_request.zone_uuid, camera_request.uuid, camera_request=camera_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('zone_request', 'invalidzone_request'),
        ('zone_request', ''),
        ('zone_request', None),
    ])
    def test_api_cameraManagerZoneNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneNew """
        zone_request.uuid = None
        zone_request = None
        intef = ViperopenapiApi.cameraManagerZoneNewPostApi(zone_request.uuid, zone_request=zone_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('zone_request', 'invalidzone_request'),
        ('zone_request', ''),
        ('zone_request', None),
    ])
    def test_api_cameraManagerZoneReplaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneReplace """
        zone_request.uuid = None
        zone_request = None
        intef = ViperopenapiApi.cameraManagerZoneReplacePutApi(zone_request.uuid, zone_request=zone_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerZoneDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneDelete """
        zone_uuid = None
        intef = ViperopenapiApi.cameraManagerZoneDeleteDeleteApi(zone_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerZoneInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneInfo """
        zone_uuid = None
        intef = ViperopenapiApi.cameraManagerZoneInfoGetApi(zone_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerZoneCameraListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraList """
        zone_uuid = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerZoneCameraListGetApi(zone_uuid, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('force', 'invalidforce'),
        ('force', ''),
        ('force', None),
    ])
    def test_api_cameraManagerZoneCameraDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraDelete """
        zone_uuid = None
        camera_uuid = None
        force = None
        intef = ViperopenapiApi.cameraManagerZoneCameraDeleteDeleteApi(zone_uuid, camera_uuid, force=force, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerZoneCameraInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraInfo """
        zone_uuid = None
        camera_uuid = None
        intef = ViperopenapiApi.cameraManagerZoneCameraInfoGetApi(zone_uuid, camera_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraActivateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraActivate """
        zone_uuid = None
        camera_uuid = None
        intef = ViperopenapiApi.cameraManagerZoneCameraActivatePostApi(zone_uuid, camera_uuid, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('fi_control_request', 'invalidfi_control_request'),
        ('fi_control_request', ''),
        ('fi_control_request', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraFIControlInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraFIControl """
        zone_uuid = None
        camera_uuid = None
        fi_control_request = None
        intef = ViperopenapiApi.cameraManagerZoneCameraFIControlPutApi(zone_uuid, camera_uuid, fi_control_request=fi_control_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraGenerateRTMPAddressInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraGenerateRTMPAddress """
        zone_uuid = None
        camera_uuid = None
        intef = ViperopenapiApi.cameraManagerZoneCameraGenerateRTMPAddressPostApi(zone_uuid, camera_uuid, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('command_type', 'invalidcommand_type'),
        ('command_type', ''),
        ('command_type', None),
        ('media_protocol_type', 'invalidmedia_protocol_type'),
        ('media_protocol_type', ''),
        ('media_protocol_type', None),
        ('playback_config', 'invalidplayback_config'),
        ('playback_config', ''),
        ('playback_config', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraGenerateRTSPAddressInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraGenerateRTSPAddress """
        zone_uuid = None
        camera_uuid = None
        command_type = None
        media_protocol_type = None
        playback_config = None
        intef = ViperopenapiApi.cameraManagerZoneCameraGenerateRTSPAddressPostApi(zone_uuid, camera_uuid, command_type=command_type, media_protocol_type=media_protocol_type, playback_config=playback_config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('home_position_request', 'invalidhome_position_request'),
        ('home_position_request', ''),
        ('home_position_request', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraHomePositionSetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraHomePositionSet """
        zone_uuid = None
        camera_uuid = None
        home_position_request = None
        intef = ViperopenapiApi.cameraManagerZoneCameraHomePositionSetPutApi(zone_uuid, camera_uuid, home_position_request=home_position_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerZoneCameraMultiTaskListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraMultiTaskList """
        zone_uuid = None
        camera_uuid = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerZoneCameraMultiTaskListGetApi(zone_uuid, camera_uuid, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('default_task', 'invaliddefault_task'),
        ('default_task', ''),
        ('default_task', None),
        ('multi_tasks', 'invalidmulti_tasks'),
        ('multi_tasks', ''),
        ('multi_tasks', None),
        ('user_data', 'invaliduser_data'),
        ('user_data', ''),
        ('user_data', None),
        ('uuid', 'invaliduuid'),
        ('uuid', ''),
        ('uuid', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraMultiTaskNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraMultiTaskNew """
        zone_uuid = None
        camera_uuid = None
        default_task = None
        multi_tasks = None
        user_data = None
        uuid = None
        intef = ViperopenapiApi.cameraManagerZoneCameraMultiTaskNewPostApi(zone_uuid, camera_uuid, default_task=default_task, multi_tasks=multi_tasks, user_data=user_data, uuid=uuid, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerZoneCameraMultiTaskDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraMultiTaskDelete """
        zone_uuid = None
        camera_uuid = None
        uuid = None
        intef = ViperopenapiApi.cameraManagerZoneCameraMultiTaskDeleteDeleteApi(zone_uuid, camera_uuid, uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerZoneCameraMultiTaskInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraMultiTaskInfo """
        zone_uuid = None
        camera_uuid = None
        uuid = None
        intef = ViperopenapiApi.cameraManagerZoneCameraMultiTaskInfoGetApi(zone_uuid, camera_uuid, uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('multi_tasks', 'invalidmulti_tasks'),
        ('multi_tasks', ''),
        ('multi_tasks', None),
        ('uuid', 'invaliduuid'),
        ('uuid', ''),
        ('uuid', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraMultiTaskUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraMultiTaskUpdate """
        zone_uuid = None
        camera_uuid = None
        uuid = None
        multi_tasks = None
        intef = ViperopenapiApi.cameraManagerZoneCameraMultiTaskUpdatePutApi(zone_uuid, camera_uuid, uuid, multi_tasks=multi_tasks, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerZoneCameraPresetListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraPresetList """
        zone_uuid = None
        camera_uuid = None
        intef = ViperopenapiApi.cameraManagerZoneCameraPresetListGetApi(zone_uuid, camera_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('preset', 'invalidpreset'),
        ('preset', ''),
        ('preset', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraPresetSetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraPresetSet """
        zone_uuid = None
        camera_uuid = None
        preset = None
        intef = ViperopenapiApi.cameraManagerZoneCameraPresetSetPutApi(zone_uuid, camera_uuid, preset=preset, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerZoneCameraPresetDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraPresetDelete """
        zone_uuid = None
        camera_uuid = None
        preset_id = None
        intef = ViperopenapiApi.cameraManagerZoneCameraPresetDeleteDeleteApi(zone_uuid, camera_uuid, preset_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('preset_id', 'invalidpreset_id'),
        ('preset_id', ''),
        ('preset_id', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraPresetGotoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraPresetGoto """
        zone_uuid = None
        camera_uuid = None
        preset_id = None
        intef = ViperopenapiApi.cameraManagerZoneCameraPresetGotoPutApi(zone_uuid, camera_uuid, preset_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('ptz_control_request', 'invalidptz_control_request'),
        ('ptz_control_request', ''),
        ('ptz_control_request', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraPTZControlInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraPTZControl """
        zone_uuid = None
        camera_uuid = None
        ptz_control_request = None
        intef = ViperopenapiApi.cameraManagerZoneCameraPTZControlPutApi(zone_uuid, camera_uuid, ptz_control_request=ptz_control_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('ptz_command', 'invalidptz_command'),
        ('ptz_command', ''),
        ('ptz_command', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraPTZControlTransparentInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraPTZControlTransparent """
        zone_uuid = None
        camera_uuid = None
        ptz_command = None
        intef = ViperopenapiApi.cameraManagerZoneCameraPTZControlTransparentPutApi(zone_uuid, camera_uuid, ptz_command=ptz_command, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('record_info_request', 'invalidrecord_info_request'),
        ('record_info_request', ''),
        ('record_info_request', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraRecordInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraRecordInfo """
        zone_uuid = None
        camera_uuid = None
        record_info_request = None
        intef = ViperopenapiApi.cameraManagerZoneCameraRecordInfoPostApi(zone_uuid, camera_uuid, record_info_request=record_info_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_cameraManagerZoneCameraTaskListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraTaskList """
        zone_uuid = None
        camera_uuid = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.cameraManagerZoneCameraTaskListGetApi(zone_uuid, camera_uuid, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('extra_parameter', 'invalidextra_parameter'),
        ('extra_parameter', ''),
        ('extra_parameter', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('object_type', 'invalidobject_type'),
        ('object_type', ''),
        ('object_type', None),
        ('playback_config', 'invalidplayback_config'),
        ('playback_config', ''),
        ('playback_config', None),
        ('storage_policy', 'invalidstorage_policy'),
        ('storage_policy', ''),
        ('storage_policy', None),
        ('symphony_device_task', 'invalidsymphony_device_task'),
        ('symphony_device_task', ''),
        ('symphony_device_task', None),
        ('task_object_config', 'invalidtask_object_config'),
        ('task_object_config', ''),
        ('task_object_config', None),
        ('user_data', 'invaliduser_data'),
        ('user_data', ''),
        ('user_data', None),
        ('uuid', 'invaliduuid'),
        ('uuid', ''),
        ('uuid', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraTaskNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraTaskNew """
        zone_uuid = None
        camera_uuid = None
        extra_parameter = None
        feature_version = None
        object_type = None
        playback_config = None
        storage_policy = None
        symphony_device_task = None
        task_object_config = None
        user_data = None
        uuid = None
        intef = ViperopenapiApi.cameraManagerZoneCameraTaskNewPostApi(zone_uuid, camera_uuid, extra_parameter=extra_parameter, feature_version=feature_version, object_type=object_type, playback_config=playback_config, storage_policy=storage_policy, symphony_device_task=symphony_device_task, task_object_config=task_object_config, user_data=user_data, uuid=uuid, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_cameraManagerZoneCameraTaskDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraTaskDelete """
        zone_uuid = None
        camera_uuid = None
        id = None
        intef = ViperopenapiApi.cameraManagerZoneCameraTaskDeleteDeleteApi(zone_uuid, camera_uuid, id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
        ('task_object_config', 'invalidtask_object_config'),
        ('task_object_config', ''),
        ('task_object_config', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraTaskUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraTaskUpdate """
        zone_uuid = None
        camera_uuid = None
        id = None
        task_object_config = None
        intef = ViperopenapiApi.cameraManagerZoneCameraTaskUpdatePutApi(zone_uuid, camera_uuid, id, task_object_config=task_object_config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraTaskGenerateRTSPAddressInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraTaskGenerateRTSPAddress """
        zone_uuid = None
        camera_uuid = None
        id = None
        intef = ViperopenapiApi.cameraManagerZoneCameraTaskGenerateRTSPAddressPostApi(zone_uuid, camera_uuid, id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraTeleBootInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraTeleBoot """
        zone_uuid = None
        camera_uuid = None
        intef = ViperopenapiApi.cameraManagerZoneCameraTeleBootPutApi(zone_uuid, camera_uuid, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_uuid', 'invalidcamera_uuid'),
        ('camera_uuid', ''),
        ('camera_uuid', None),
        ('command_type', 'invalidcommand_type'),
        ('command_type', ''),
        ('command_type', None),
        ('media_protocol_type', 'invalidmedia_protocol_type'),
        ('media_protocol_type', ''),
        ('media_protocol_type', None),
        ('playback_config', 'invalidplayback_config'),
        ('playback_config', ''),
        ('playback_config', None),
        ('zone_uuid', 'invalidzone_uuid'),
        ('zone_uuid', ''),
        ('zone_uuid', None),
    ])
    def test_api_cameraManagerZoneCameraVideoCaptureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraVideoCapture """
        zone_uuid = None
        camera_uuid = None
        command_type = None
        media_protocol_type = None
        playback_config = None
        intef = ViperopenapiApi.cameraManagerZoneCameraVideoCapturePostApi(zone_uuid, camera_uuid, command_type=command_type, media_protocol_type=media_protocol_type, playback_config=playback_config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('media_protocol_type', 'invalidmedia_protocol_type'),
        ('media_protocol_type', ''),
        ('media_protocol_type', None),
    ])
    def test_api_cameraManagerZoneCameraVideoParameterInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ZoneCameraVideoParameter """
        zone_uuid = None
        camera_uuid = None
        media_protocol_type = None
        intef = ViperopenapiApi.cameraManagerZoneCameraVideoParameterGetApi(zone_uuid, camera_uuid, media_protocol_type=media_protocol_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('oplogs', 'invalidoplogs'),
        ('oplogs', ''),
        ('oplogs', None),
    ])
    def test_api_entityDBAddOutsideOplogAsyncInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AddOutsideOplogAsync """
        oplogs = None
        intef = ViperopenapiApi.entityDBAddOutsideOplogAsyncPostApi(oplogs=oplogs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('cluster_update_items', 'invalidcluster_update_items'),
        ('cluster_update_items', ''),
        ('cluster_update_items', None),
    ])
    def test_api_entityDBBatchUpdateEntityClusterInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchUpdateEntityCluster """
        cluster_update_items = None
        intef = ViperopenapiApi.entityDBBatchUpdateEntityClusterPostApi(cluster_update_items=cluster_update_items, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
    ])
    def test_api_entityDBDeleteEventsDataBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteEventsDataBeforeDate """
        date = None
        intef = ViperopenapiApi.entityDBDeleteEventsDataBeforeDatePostApi(date=date, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
    ])
    def test_api_entityDBDeleteHumanVehicleTracksBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteHumanVehicleTracksBeforeDate """
        date = None
        intef = ViperopenapiApi.entityDBDeleteHumanVehicleTracksBeforeDatePostApi(date=date, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
    ])
    def test_api_entityDBDeleteTracksBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteTracksBeforeDate """
        date = None
        intef = ViperopenapiApi.entityDBDeleteTracksBeforeDatePostApi(date=date, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
    ])
    def test_api_entityDBDeleteVehicleTracksBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteVehicleTracksBeforeDate """
        date = None
        intef = ViperopenapiApi.entityDBDeleteVehicleTracksBeforeDatePostApi(date=date, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('marker', 'invalidmarker'),
        ('marker', ''),
        ('marker', None),
        ('order_field', 'invalidorder_field'),
        ('order_field', ''),
        ('order_field', None),
        ('page_size', 'invalidpage_size'),
        ('page_size', ''),
        ('page_size', None),
        ('period', 'invalidperiod'),
        ('period', ''),
        ('period', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
        ('types', 'invalidtypes'),
        ('types', ''),
        ('types', None),
    ])
    def test_api_entityDBEntityListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  EntityList """
        marker = None
        order_field = None
        page_size = None
        period = None
        reversed = None
        types = None
        intef = ViperopenapiApi.entityDBEntityListPostApi(marker=marker, order_field=order_field, page_size=page_size, period=period, reversed=reversed, types=types, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('entity_ids', 'invalidentity_ids'),
        ('entity_ids', ''),
        ('entity_ids', None),
    ])
    def test_api_entityDBBatchDeleteEntitiesInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDeleteEntities """
        entity_ids = None
        intef = ViperopenapiApi.entityDBBatchDeleteEntitiesPostApi(entity_ids=entity_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('entity_ids', 'invalidentity_ids'),
        ('entity_ids', ''),
        ('entity_ids', None),
    ])
    def test_api_entityDBEntityBatchGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  EntityBatchGet """
        entity_ids = None
        intef = ViperopenapiApi.entityDBEntityBatchGetPostApi(entity_ids=entity_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_ids', 'invalidcamera_ids'),
        ('camera_ids', ''),
        ('camera_ids', None),
        ('feature', 'invalidfeature'),
        ('feature', ''),
        ('feature', None),
        ('min_score', 'invalidmin_score'),
        ('min_score', ''),
        ('min_score', None),
        ('period', 'invalidperiod'),
        ('period', ''),
        ('period', None),
        ('top_k', 'invalidtop_k'),
        ('top_k', ''),
        ('top_k', None),
    ])
    def test_api_entityDBEntitySearchInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  EntitySearch """
        camera_ids = None
        feature = None
        min_score = None
        period = None
        top_k = None
        intef = ViperopenapiApi.entityDBEntitySearchPostApi(camera_ids=camera_ids, feature=feature, min_score=min_score, period=period, top_k=top_k, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('entity_id', 'invalidentity_id'),
        ('entity_id', ''),
        ('entity_id', None),
        ('marker', 'invalidmarker'),
        ('marker', ''),
        ('marker', None),
        ('page_size', 'invalidpage_size'),
        ('page_size', ''),
        ('page_size', None),
        ('period', 'invalidperiod'),
        ('period', ''),
        ('period', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
    ])
    def test_api_entityDBTrackListByEntityInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TrackListByEntity """
        entity_id.entity_type = None
        entity_id.id = None
        entity_id = None
        marker = None
        page_size = None
        period = None
        reversed = None
        intef = ViperopenapiApi.entityDBTrackListByEntityPostApi(entity_id.entity_type, entity_id.id, entity_id=entity_id, marker=marker, page_size=page_size, period=period, reversed=reversed, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_ids', 'invalidcamera_ids'),
        ('camera_ids', ''),
        ('camera_ids', None),
        ('paging', 'invalidpaging'),
        ('paging', ''),
        ('paging', None),
        ('period', 'invalidperiod'),
        ('period', ''),
        ('period', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
        ('types', 'invalidtypes'),
        ('types', ''),
        ('types', None),
    ])
    def test_api_entityDBEntitiesByTimeSpaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  EntitiesByTimeSpace """
        camera_ids = None
        paging = None
        period = None
        reversed = None
        types = None
        intef = ViperopenapiApi.entityDBEntitiesByTimeSpacePostApi(camera_ids=camera_ids, paging=paging, period=period, reversed=reversed, types=types, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('features', 'invalidfeatures'),
        ('features', ''),
        ('features', None),
    ])
    def test_api_entityDBGenerateCentroidInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GenerateCentroid """
        features = None
        intef = ViperopenapiApi.entityDBGenerateCentroidPostApi(features=features, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('is_async', 'invalidis_async'),
        ('is_async', ''),
        ('is_async', None),
        ('track_delete_items', 'invalidtrack_delete_items'),
        ('track_delete_items', ''),
        ('track_delete_items', None),
    ])
    def test_api_entityDBBatchDeleteTracksInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDeleteTracks """
        is_async = None
        track_delete_items = None
        intef = ViperopenapiApi.entityDBBatchDeleteTracksPostApi(is_async=is_async, track_delete_items=track_delete_items, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('track_ids', 'invalidtrack_ids'),
        ('track_ids', ''),
        ('track_ids', None),
    ])
    def test_api_entityDBTrackBatchGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TrackBatchGet """
        track_ids = None
        intef = ViperopenapiApi.entityDBTrackBatchGetPostApi(track_ids=track_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_ids', 'invalidcamera_ids'),
        ('camera_ids', ''),
        ('camera_ids', None),
        ('entity_id', 'invalidentity_id'),
        ('entity_id', ''),
        ('entity_id', None),
        ('feature', 'invalidfeature'),
        ('feature', ''),
        ('feature', None),
        ('period', 'invalidperiod'),
        ('period', ''),
        ('period', None),
        ('top_k', 'invalidtop_k'),
        ('top_k', ''),
        ('top_k', None),
    ])
    def test_api_entityDBTracksByEntitySortedBySimilarityInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TracksByEntitySortedBySimilarity """
        camera_ids = None
        entity_id = None
        feature = None
        period = None
        top_k = None
        intef = ViperopenapiApi.entityDBTracksByEntitySortedBySimilarityPostApi(camera_ids=camera_ids, entity_id=entity_id, feature=feature, period=period, top_k=top_k, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('paging', 'invalidpaging'),
        ('paging', ''),
        ('paging', None),
        ('period', 'invalidperiod'),
        ('period', ''),
        ('period', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
        ('types', 'invalidtypes'),
        ('types', ''),
        ('types', None),
    ])
    def test_api_entityDBEntityListV2InvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  EntityListV2 """
        paging = None
        period = None
        reversed = None
        types = None
        intef = ViperopenapiApi.entityDBEntityListV2PostApi(paging=paging, period=period, reversed=reversed, types=types, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_ids', 'invalidcamera_ids'),
        ('camera_ids', ''),
        ('camera_ids', None),
        ('entity_id', 'invalidentity_id'),
        ('entity_id', ''),
        ('entity_id', None),
        ('paging', 'invalidpaging'),
        ('paging', ''),
        ('paging', None),
        ('period', 'invalidperiod'),
        ('period', ''),
        ('period', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
    ])
    def test_api_entityDBTrackListByEntityV2InvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TrackListByEntityV2 """
        entity_id.id = None
        camera_ids = None
        entity_id = None
        paging = None
        period = None
        reversed = None
        intef = ViperopenapiApi.entityDBTrackListByEntityV2PostApi(entity_id.id, camera_ids=camera_ids, entity_id=entity_id, paging=paging, period=period, reversed=reversed, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('features', 'invalidfeatures'),
        ('features', ''),
        ('features', None),
        ('source_system', 'invalidsource_system'),
        ('source_system', ''),
        ('source_system', None),
        ('target_systems', 'invalidtarget_systems'),
        ('target_systems', ''),
        ('target_systems', None),
        ('target_version', 'invalidtarget_version'),
        ('target_version', ''),
        ('target_version', None),
    ])
    def test_api_featureConvertBatchConvertFeatureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchConvertFeature """
        features = None
        source_system = None
        target_systems = None
        target_version = None
        intef = ViperopenapiApi.featureConvertBatchConvertFeaturePostApi(features=features, source_system=source_system, target_systems=target_systems, target_version=target_version, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageEgressObjectDownloadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ObjectDownload """
        platform_id = None
        object_id = None
        intef = ViperopenapiApi.imageEgressObjectDownloadGetApi(platform_id, object_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_imageEgressManagerVIIDListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  VIIDList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.imageEgressManagerVIIDListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageEgressManagerVIIDDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  VIIDDelete """
        viid_id = None
        intef = ViperopenapiApi.imageEgressManagerVIIDDeleteDeleteApi(viid_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageEgressManagerVIIDInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  VIIDInfo """
        viid_id = None
        intef = ViperopenapiApi.imageEgressManagerVIIDInfoGetApi(viid_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_imageEgressManagerVIIDAPEListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  VIIDAPEList """
        viid_id = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.imageEgressManagerVIIDAPEListGetApi(viid_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ape_infos', 'invalidape_infos'),
        ('ape_infos', ''),
        ('ape_infos', None),
        ('viid_id', 'invalidviid_id'),
        ('viid_id', ''),
        ('viid_id', None),
    ])
    def test_api_imageEgressManagerBatchAddVIIDAPEInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchAddVIIDAPE """
        viid_id = None
        ape_infos = None
        intef = ViperopenapiApi.imageEgressManagerBatchAddVIIDAPEPostApi(viid_id, ape_infos=ape_infos, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ape_uuids', 'invalidape_uuids'),
        ('ape_uuids', ''),
        ('ape_uuids', None),
        ('viid_id', 'invalidviid_id'),
        ('viid_id', ''),
        ('viid_id', None),
    ])
    def test_api_imageEgressManagerBatchDelVIIDAPEInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDelVIIDAPE """
        viid_id = None
        ape_uuids = None
        intef = ViperopenapiApi.imageEgressManagerBatchDelVIIDAPEPostApi(viid_id, ape_uuids=ape_uuids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_imageEgressManagerVIIDSubscriptionListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  VIIDSubscriptionList """
        viid_id = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.imageEgressManagerVIIDSubscriptionListGetApi(viid_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('viid_request', 'invalidviid_request'),
        ('viid_request', ''),
        ('viid_request', None),
    ])
    def test_api_imageEgressManagerVIIDNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  VIIDNew """
        viid_request.viid_id = None
        viid_request = None
        intef = ViperopenapiApi.imageEgressManagerVIIDNewPostApi(viid_request.viid_id, viid_request=viid_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageEgressBatchPutObjectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchPutObject """
        requests = None
        intef = ViperopenapiApi.imageEgressBatchPutObjectPostApi(requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('object_info', 'invalidobject_info'),
        ('object_info', ''),
        ('object_info', None),
        ('platform_id', 'invalidplatform_id'),
        ('platform_id', ''),
        ('platform_id', None),
    ])
    def test_api_imageEgressObjectPutInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ObjectPut """
        platform_id = None
        object_info = None
        intef = ViperopenapiApi.imageEgressObjectPutPostApi(platform_id, object_info=object_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageEgressObjectGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ObjectGet """
        platform_id = None
        object_id = None
        intef = ViperopenapiApi.imageEgressObjectGetGetApi(platform_id, object_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
        ('subscribe_id', 'invalidsubscribe_id'),
        ('subscribe_id', ''),
        ('subscribe_id', None),
    ])
    def test_api_imageIngressGAT1400SubscribeDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GAT1400SubscribeDelete """
        task_id = None
        subscribe_id = None
        intef = ViperopenapiApi.imageIngressGAT1400SubscribeDeleteDeleteApi(task_id=task_id, subscribe_id=subscribe_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('parameter', 'invalidparameter'),
        ('parameter', ''),
        ('parameter', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
    ])
    def test_api_imageIngressGAT1400SubscribeNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GAT1400SubscribeNew """
        parameter = None
        task_id = None
        intef = ViperopenapiApi.imageIngressGAT1400SubscribeNewPostApi(parameter=parameter, task_id=task_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_imageIngressGetCamerasFromPlatformInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetCamerasFromPlatform """
        task_id = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.imageIngressGetCamerasFromPlatformGetApi(task_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

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
        ('is_passive', 'invalidis_passive'),
        ('is_passive', ''),
        ('is_passive', None),
    ])
    def test_api_imageIngressTaskListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskList """
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        is_passive = None
        intef = ViperopenapiApi.imageIngressTaskListGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, is_passive=is_passive, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_request', 'invalidtask_request'),
        ('task_request', ''),
        ('task_request', None),
    ])
    def test_api_imageIngressTaskNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskNew """
        task_request = None
        intef = ViperopenapiApi.imageIngressTaskNewPostApi(task_request=task_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageIngressTaskDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskDelete """
        task_id = None
        intef = ViperopenapiApi.imageIngressTaskDeleteDeleteApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageIngressTaskStatusInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskStatus """
        task_id = None
        intef = ViperopenapiApi.imageIngressTaskStatusGetApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFpachExtractBatchCompareFeatureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFpachExtractBatchCompareFeaturePostApi(face_feature_version, pedestrian_feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFpachExtractBatchDetectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetect """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFpachExtractBatchDetectPostApi(face_feature_version, pedestrian_feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFpachExtractBatchDetectAndExtractAllInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFpachExtractBatchDetectAndExtractAllPostApi(face_feature_version, pedestrian_feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFpachExtractBatchExtractWithLocationInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchExtractWithLocation """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFpachExtractBatchExtractWithLocationPostApi(face_feature_version, pedestrian_feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageFpachExtractGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        face_feature_version = None
        pedestrian_feature_version = None
        intef = ViperopenapiApi.imageFpachExtractGetSystemInfoGetApi(face_feature_version, pedestrian_feature_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceExtractBatchCompareFeatureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFaceExtractBatchCompareFeaturePostApi(feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('face_type', 'invalidface_type'),
        ('face_type', ''),
        ('face_type', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceExtractBatchDetectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetect """
        feature_version = None
        detect_mode = None
        face_type = None
        requests = None
        intef = ViperopenapiApi.imageFaceExtractBatchDetectPostApi(feature_version, detect_mode=detect_mode, face_type=face_type, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('face_type', 'invalidface_type'),
        ('face_type', ''),
        ('face_type', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceExtractBatchDetectAndExtractInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtract """
        feature_version = None
        detect_mode = None
        face_type = None
        requests = None
        intef = ViperopenapiApi.imageFaceExtractBatchDetectAndExtractPostApi(feature_version, detect_mode=detect_mode, face_type=face_type, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('face_type', 'invalidface_type'),
        ('face_type', ''),
        ('face_type', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceExtractBatchDetectAndExtractAll2InvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll2 """
        feature_version = None
        detect_mode = None
        face_type = None
        requests = None
        intef = ViperopenapiApi.imageFaceExtractBatchDetectAndExtractAll2PostApi(feature_version, detect_mode=detect_mode, face_type=face_type, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('face_type', 'invalidface_type'),
        ('face_type', ''),
        ('face_type', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceExtractBatchDetectAndExtractMultiModelInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractMultiModel """
        feature_version = None
        detect_mode = None
        face_type = None
        requests = None
        intef = ViperopenapiApi.imageFaceExtractBatchDetectAndExtractMultiModelPostApi(feature_version, detect_mode=detect_mode, face_type=face_type, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('detect_mode', 'invaliddetect_mode'),
        ('detect_mode', ''),
        ('detect_mode', None),
        ('face_type', 'invalidface_type'),
        ('face_type', ''),
        ('face_type', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceExtractBatchDetectAndExtractAllInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll """
        feature_version = None
        detect_mode = None
        face_type = None
        requests = None
        intef = ViperopenapiApi.imageFaceExtractBatchDetectAndExtractAllPostApi(feature_version, detect_mode=detect_mode, face_type=face_type, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceExtractBatchExtractWithBoundingInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchExtractWithBounding """
        feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFaceExtractBatchExtractWithBoundingPostApi(feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceExtractBatchExtractWithPointsInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchExtractWithPoints """
        feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFaceExtractBatchExtractWithPointsPostApi(feature_version, requests=requests, sendRequest=False)
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
    ])
    def test_api_imageFaceExtractCompareFeatureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  CompareFeature """
        feature_version = None
        one = None
        other = None
        intef = ViperopenapiApi.imageFaceExtractCompareFeaturePostApi(feature_version, one=one, other=other, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageFaceExtractGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        feature_version = None
        intef = ViperopenapiApi.imageFaceExtractGetSystemInfoGetApi(feature_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFacepedExtratBatchCompareFeatureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFacepedExtratBatchCompareFeaturePostApi(face_feature_version, pedestrian_feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFacepedExtratBatchDetectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetect """
        face_feature_version = None
        pedestrian_feature_version = None
        mode = None
        requests = None
        intef = ViperopenapiApi.imageFacepedExtratBatchDetectPostApi(face_feature_version, pedestrian_feature_version, mode=mode, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFacepedExtratBatchDetectAndExtractInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtract """
        face_feature_version = None
        pedestrian_feature_version = None
        mode = None
        requests = None
        intef = ViperopenapiApi.imageFacepedExtratBatchDetectAndExtractPostApi(face_feature_version, pedestrian_feature_version, mode=mode, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFacepedExtratBatchDetectAndExtractAllInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll """
        face_feature_version = None
        pedestrian_feature_version = None
        mode = None
        requests = None
        intef = ViperopenapiApi.imageFacepedExtratBatchDetectAndExtractAllPostApi(face_feature_version, pedestrian_feature_version, mode=mode, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFacepedExtratBatchExtractWithLocationInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchExtractWithLocation """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFacepedExtratBatchExtractWithLocationPostApi(face_feature_version, pedestrian_feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageFacepedExtratGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        face_feature_version = None
        pedestrian_feature_version = None
        intef = ViperopenapiApi.imageFacepedExtratGetSystemInfoGetApi(face_feature_version, pedestrian_feature_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceVehicleExtractBatchCompareFeatureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFaceVehicleExtractBatchCompareFeaturePostApi(feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceVehicleExtractBatchDetectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetect """
        feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFaceVehicleExtractBatchDetectPostApi(feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceVehicleExtractBatchDetectAndExtractAllInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll """
        feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFaceVehicleExtractBatchDetectAndExtractAllPostApi(feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageFaceVehicleExtractBatchExtractWithLocationInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchExtractWithLocation """
        feature_version = None
        requests = None
        intef = ViperopenapiApi.imageFaceVehicleExtractBatchExtractWithLocationPostApi(feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageFaceVehicleExtractGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        feature_version = None
        intef = ViperopenapiApi.imageFaceVehicleExtractGetSystemInfoGetApi(feature_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageStructExtractBatchCompareFeatureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        feature_version = None
        requests = None
        intef = ViperopenapiApi.imageStructExtractBatchCompareFeaturePostApi(feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageStructExtractBatchDetectInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetect """
        feature_version = None
        mode = None
        requests = None
        intef = ViperopenapiApi.imageStructExtractBatchDetectPostApi(feature_version, mode=mode, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageStructExtractBatchDetectAndExtractInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtract """
        feature_version = None
        mode = None
        requests = None
        intef = ViperopenapiApi.imageStructExtractBatchDetectAndExtractPostApi(feature_version, mode=mode, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageStructExtractBatchExtractWithBoundingInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchExtractWithBounding """
        feature_version = None
        requests = None
        intef = ViperopenapiApi.imageStructExtractBatchExtractWithBoundingPostApi(feature_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageStructExtractGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        feature_version = None
        intef = ViperopenapiApi.imageStructExtractGetSystemInfoGetApi(feature_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('template_data', 'invalidtemplate_data'),
        ('template_data', ''),
        ('template_data', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_imageOCRExtractBatchCustomTemplateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchCustomTemplate """
        images = None
        template_data = None
        type = None
        intef = ViperopenapiApi.imageOCRExtractBatchCustomTemplatePostApi(images=images, template_data=template_data, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('region_type', 'invalidregion_type'),
        ('region_type', ''),
        ('region_type', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_imageOCRExtractBatchPlainTextInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchPlainText """
        images = None
        region_type = None
        type = None
        intef = ViperopenapiApi.imageOCRExtractBatchPlainTextPostApi(images=images, region_type=region_type, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('template_db_ids', 'invalidtemplate_db_ids'),
        ('template_db_ids', ''),
        ('template_db_ids', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_imageOCRExtractBatchSpecialTemplateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchSpecialTemplate """
        images = None
        template_db_ids = None
        type = None
        intef = ViperopenapiApi.imageOCRExtractBatchSpecialTemplatePostApi(images=images, template_db_ids=template_db_ids, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('region_type', 'invalidregion_type'),
        ('region_type', ''),
        ('region_type', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_imageOCRExtractBatchTemplateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchTemplate """
        images = None
        region_type = None
        type = None
        intef = ViperopenapiApi.imageOCRExtractBatchTemplatePostApi(images=images, region_type=region_type, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageOCRExtractGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.imageOCRExtractGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('requests', 'invalidrequests'),
        ('requests', ''),
        ('requests', None),
    ])
    def test_api_imageAlgoProcessBatchProcessInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchProcess """
        app_id = None
        app_version = None
        requests = None
        intef = ViperopenapiApi.imageAlgoProcessBatchProcessPostApi(app_id, app_version, requests=requests, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_imageAlgoProcessGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        app_id = None
        app_version = None
        intef = ViperopenapiApi.imageAlgoProcessGetSystemInfoGetApi(app_id, app_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('template_data', 'invalidtemplate_data'),
        ('template_data', ''),
        ('template_data', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_ocrApiWrapperBatchOCRCustomTemplateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchOCRCustomTemplate """
        images = None
        template_data = None
        type = None
        intef = ViperopenapiApi.ocrApiWrapperBatchOCRCustomTemplatePostApi(images=images, template_data=template_data, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('region_type', 'invalidregion_type'),
        ('region_type', ''),
        ('region_type', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_ocrApiWrapperBatchOCRPlainTextInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchOCRPlainText """
        images = None
        region_type = None
        type = None
        intef = ViperopenapiApi.ocrApiWrapperBatchOCRPlainTextPostApi(images=images, region_type=region_type, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('template_db_ids', 'invalidtemplate_db_ids'),
        ('template_db_ids', ''),
        ('template_db_ids', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_ocrApiWrapperBatchOCRSpecialTemplateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchOCRSpecialTemplate """
        images = None
        template_db_ids = None
        type = None
        intef = ViperopenapiApi.ocrApiWrapperBatchOCRSpecialTemplatePostApi(images=images, template_db_ids=template_db_ids, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('region_type', 'invalidregion_type'),
        ('region_type', ''),
        ('region_type', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_ocrApiWrapperBatchOCRTemplateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchOCRTemplate """
        images = None
        region_type = None
        type = None
        intef = ViperopenapiApi.ocrApiWrapperBatchOCRTemplatePostApi(images=images, region_type=region_type, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('template_data', 'invalidtemplate_data'),
        ('template_data', ''),
        ('template_data', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_ocrApiWrapperOCRCustomTemplateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  OCRCustomTemplate """
        image = None
        template_data = None
        type = None
        intef = ViperopenapiApi.ocrApiWrapperOCRCustomTemplatePostApi(image=image, template_data=template_data, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('region_type', 'invalidregion_type'),
        ('region_type', ''),
        ('region_type', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_ocrApiWrapperOCRPlainTextInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  OCRPlainText """
        image = None
        region_type = None
        type = None
        intef = ViperopenapiApi.ocrApiWrapperOCRPlainTextPostApi(image=image, region_type=region_type, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('template_db_ids', 'invalidtemplate_db_ids'),
        ('template_db_ids', ''),
        ('template_db_ids', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_ocrApiWrapperOCRSpecialTemplateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  OCRSpecialTemplate """
        image = None
        template_db_ids = None
        type = None
        intef = ViperopenapiApi.ocrApiWrapperOCRSpecialTemplatePostApi(image=image, template_db_ids=template_db_ids, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('region_type', 'invalidregion_type'),
        ('region_type', ''),
        ('region_type', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
    ])
    def test_api_ocrApiWrapperOCRTemplateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  OCRTemplate """
        image = None
        region_type = None
        type = None
        intef = ViperopenapiApi.ocrApiWrapperOCRTemplatePostApi(image=image, region_type=region_type, type=type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_kafkaCallbackGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.kafkaCallbackGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('transport_config', 'invalidtransport_config'),
        ('transport_config', ''),
        ('transport_config', None),
        ('url', 'invalidurl'),
        ('url', ''),
        ('url', None),
    ])
    def test_api_kafkaCallbackSetCallbackURLInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  SetCallbackURL """
        transport_config = None
        url = None
        intef = ViperopenapiApi.kafkaCallbackSetCallbackURLPostApi(transport_config=transport_config, url=url, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuids', 'invaliddevice_uuids'),
        ('device_uuids', ''),
        ('device_uuids', None),
    ])
    def test_api_protocolIngressBatchDeleteDeviceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchDeleteDevice """
        device_uuids = None
        intef = ViperopenapiApi.protocolIngressBatchDeleteDevicePostApi(device_uuids=device_uuids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('devices', 'invaliddevices'),
        ('devices', ''),
        ('devices', None),
    ])
    def test_api_protocolIngressBatchNewDeviceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchNewDevice """
        devices = None
        intef = ViperopenapiApi.protocolIngressBatchNewDevicePostApi(devices=devices, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device', 'invaliddevice'),
        ('device', ''),
        ('device', None),
    ])
    def test_api_protocolIngressDeviceNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeviceNew """
        device.device_uuid = None
        device = None
        intef = ViperopenapiApi.protocolIngressDeviceNewPostApi(device.device_uuid, device=device, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device', 'invaliddevice'),
        ('device', ''),
        ('device', None),
    ])
    def test_api_protocolIngressDeviceReplaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeviceReplace """
        device.device_uuid = None
        device = None
        intef = ViperopenapiApi.protocolIngressDeviceReplacePutApi(device.device_uuid, device=device, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_protocolIngressDeviceDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeviceDelete """
        device_uuid = None
        intef = ViperopenapiApi.protocolIngressDeviceDeleteDeleteApi(device_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_protocolIngressDeviceInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeviceInfo """
        device_uuid = None
        intef = ViperopenapiApi.protocolIngressDeviceInfoGetApi(device_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('position', 'invalidposition'),
        ('position', ''),
        ('position', None),
    ])
    def test_api_protocolIngressAbsolutePTZMoveInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AbsolutePTZMove """
        device_uuid = None
        position = None
        intef = ViperopenapiApi.protocolIngressAbsolutePTZMovePutApi(device_uuid, position=position, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_protocolIngressAbsolutePTZPositionInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AbsolutePTZPosition """
        device_uuid = None
        intef = ViperopenapiApi.protocolIngressAbsolutePTZPositionGetApi(device_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
        ('item_type', 'invaliditem_type'),
        ('item_type', ''),
        ('item_type', None),
    ])
    def test_api_protocolIngressDeviceCatalogListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeviceCatalogList """
        device_uuid = None
        page_offset = None
        page_limit = None
        page_total = None
        item_type = None
        intef = ViperopenapiApi.protocolIngressDeviceCatalogListGetApi(device_uuid, page_offset=page_offset, page_limit=page_limit, page_total=page_total, item_type=item_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_protocolIngressDeviceCatalogSendInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeviceCatalogSend """
        device_uuid = None
        intef = ViperopenapiApi.protocolIngressDeviceCatalogSendPutApi(device_uuid, sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('focus', 'invalidfocus'),
        ('focus', ''),
        ('focus', None),
        ('iris', 'invalidiris'),
        ('iris', ''),
        ('iris', None),
        ('stop_enable', 'invalidstop_enable'),
        ('stop_enable', ''),
        ('stop_enable', None),
    ])
    def test_api_protocolIngressFIControlInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FIControl """
        device_uuid = None
        focus = None
        iris = None
        stop_enable = None
        intef = ViperopenapiApi.protocolIngressFIControlPutApi(device_uuid, focus=focus, iris=iris, stop_enable=stop_enable, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('stream_type', 'invalidstream_type'),
        ('stream_type', ''),
        ('stream_type', None),
    ])
    def test_api_protocolIngressDeviceMediaInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeviceMediaInfo """
        device_uuid = None
        stream_type = None
        intef = ViperopenapiApi.protocolIngressDeviceMediaInfoGetApi(device_uuid, stream_type=stream_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_protocolIngressPresetListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PresetList """
        device_uuid = None
        intef = ViperopenapiApi.protocolIngressPresetListGetApi(device_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('preset', 'invalidpreset'),
        ('preset', ''),
        ('preset', None),
    ])
    def test_api_protocolIngressPresetSetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PresetSet """
        device_uuid = None
        preset = None
        intef = ViperopenapiApi.protocolIngressPresetSetPutApi(device_uuid, preset=preset, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_protocolIngressPresetDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PresetDelete """
        device_uuid = None
        preset_id = None
        intef = ViperopenapiApi.protocolIngressPresetDeleteDeleteApi(device_uuid, preset_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('preset_id', 'invalidpreset_id'),
        ('preset_id', ''),
        ('preset_id', None),
    ])
    def test_api_protocolIngressPresetGotoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PresetGoto """
        device_uuid = None
        preset_id = None
        intef = ViperopenapiApi.protocolIngressPresetGotoPutApi(device_uuid, preset_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('enabled', 'invalidenabled'),
        ('enabled', ''),
        ('enabled', None),
        ('preset_id', 'invalidpreset_id'),
        ('preset_id', ''),
        ('preset_id', None),
        ('reset_time', 'invalidreset_time'),
        ('reset_time', ''),
        ('reset_time', None),
    ])
    def test_api_protocolIngressHomePositionSetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  HomePositionSet """
        device_uuid = None
        preset_id = None
        enabled = None
        reset_time = None
        intef = ViperopenapiApi.protocolIngressHomePositionSetPutApi(device_uuid, preset_id, enabled=enabled, reset_time=reset_time, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('pan', 'invalidpan'),
        ('pan', ''),
        ('pan', None),
        ('stop_enable', 'invalidstop_enable'),
        ('stop_enable', ''),
        ('stop_enable', None),
        ('tilt', 'invalidtilt'),
        ('tilt', ''),
        ('tilt', None),
        ('zoom', 'invalidzoom'),
        ('zoom', ''),
        ('zoom', None),
    ])
    def test_api_protocolIngressPTZControlInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PTZControl """
        device_uuid = None
        pan = None
        stop_enable = None
        tilt = None
        zoom = None
        intef = ViperopenapiApi.protocolIngressPTZControlPutApi(device_uuid, pan=pan, stop_enable=stop_enable, tilt=tilt, zoom=zoom, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('ptz_command', 'invalidptz_command'),
        ('ptz_command', ''),
        ('ptz_command', None),
    ])
    def test_api_protocolIngressPTZControlTransparentInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  PTZControlTransparent """
        device_uuid = None
        ptz_command = None
        intef = ViperopenapiApi.protocolIngressPTZControlTransparentPutApi(device_uuid, ptz_command=ptz_command, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('address', 'invalidaddress'),
        ('address', ''),
        ('address', None),
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('file_path', 'invalidfile_path'),
        ('file_path', ''),
        ('file_path', None),
        ('record_type', 'invalidrecord_type'),
        ('record_type', ''),
        ('record_type', None),
        ('recorder_id', 'invalidrecorder_id'),
        ('recorder_id', ''),
        ('recorder_id', None),
        ('secrecy', 'invalidsecrecy'),
        ('secrecy', ''),
        ('secrecy', None),
        ('start_time', 'invalidstart_time'),
        ('start_time', ''),
        ('start_time', None),
        ('stop_time', 'invalidstop_time'),
        ('stop_time', ''),
        ('stop_time', None),
    ])
    def test_api_protocolIngressRecordInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  RecordInfo """
        device_uuid = None
        address = None
        file_path = None
        record_type = None
        recorder_id = None
        secrecy = None
        start_time = None
        stop_time = None
        intef = ViperopenapiApi.protocolIngressRecordInfoPostApi(device_uuid, address=address, file_path=file_path, record_type=record_type, recorder_id=recorder_id, secrecy=secrecy, start_time=start_time, stop_time=stop_time, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('event', 'invalidevent'),
        ('event', ''),
        ('event', None),
    ])
    def test_api_protocolIngressDeviceSubscribeInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeviceSubscribe """
        device_uuid = None
        event = None
        intef = ViperopenapiApi.protocolIngressDeviceSubscribePostApi(device_uuid, event=event, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
    ])
    def test_api_protocolIngressTeleBootInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TeleBoot """
        device_uuid = None
        intef = ViperopenapiApi.protocolIngressTeleBootPutApi(device_uuid, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('event', 'invalidevent'),
        ('event', ''),
        ('event', None),
    ])
    def test_api_protocolIngressDeviceUnsubscribeInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeviceUnsubscribe """
        device_uuid = None
        event = None
        intef = ViperopenapiApi.protocolIngressDeviceUnsubscribePostApi(device_uuid, event=event, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('device_type', 'invaliddevice_type'),
        ('device_type', ''),
        ('device_type', None),
        ('device_uuid', 'invaliddevice_uuid'),
        ('device_uuid', ''),
        ('device_uuid', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('source_type', 'invalidsource_type'),
        ('source_type', ''),
        ('source_type', None),
        ('video_source', 'invalidvideo_source'),
        ('video_source', ''),
        ('video_source', None),
    ])
    def test_api_protocolIngressDeviceSearchInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeviceSearch """
        device_type = None
        device_uuid = None
        page = None
        source_type = None
        video_source = None
        intef = ViperopenapiApi.protocolIngressDeviceSearchPostApi(device_type=device_type, device_uuid=device_uuid, page=page, source_type=source_type, video_source=video_source, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_protocolIngressGB28181LocalConfigListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.protocolIngressGB28181LocalConfigListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
    ])
    def test_api_protocolIngressGB28181LocalConfigNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigNew """
        config.local_uuid = None
        config = None
        intef = ViperopenapiApi.protocolIngressGB28181LocalConfigNewPostApi(config.local_uuid, config=config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
    ])
    def test_api_protocolIngressGB28181LocalConfigReplaceInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigReplace """
        config.local_uuid = None
        config = None
        intef = ViperopenapiApi.protocolIngressGB28181LocalConfigReplacePutApi(config.local_uuid, config=config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_protocolIngressGB28181LocalConfigDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigDelete """
        local_uuid = None
        intef = ViperopenapiApi.protocolIngressGB28181LocalConfigDeleteDeleteApi(local_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_protocolIngressGB28181LocalConfigInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigInfo """
        local_uuid = None
        intef = ViperopenapiApi.protocolIngressGB28181LocalConfigInfoGetApi(local_uuid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_protocolIngressGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.protocolIngressGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('format', 'invalidformat'),
        ('format', ''),
        ('format', None),
    ])
    def test_api_shortVideoStorageDataRecordDownloadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  RecordDownload """
        record_url = None
        format = None
        intef = ViperopenapiApi.shortVideoStorageDataRecordDownloadGetApi(record_url, format=format, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('image_times', 'invalidimage_times'),
        ('image_times', ''),
        ('image_times', None),
        ('ns_id', 'invalidns_id'),
        ('ns_id', ''),
        ('ns_id', None),
        ('request_id', 'invalidrequest_id'),
        ('request_id', ''),
        ('request_id', None),
        ('stream_id', 'invalidstream_id'),
        ('stream_id', ''),
        ('stream_id', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
    ])
    def test_api_shortVideoStorageImageNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ImageNew """
        image_times = None
        ns_id = None
        request_id = None
        stream_id = None
        task_id = None
        intef = ViperopenapiApi.shortVideoStorageImageNewPostApi(image_times=image_times, ns_id=ns_id, request_id=request_id, stream_id=stream_id, task_id=task_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_shortVideoStorageRecordListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  RecordList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.shortVideoStorageRecordListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('append_record_seconds', 'invalidappend_record_seconds'),
        ('append_record_seconds', ''),
        ('append_record_seconds', None),
        ('ns_id', 'invalidns_id'),
        ('ns_id', ''),
        ('ns_id', None),
        ('prerecord_seconds', 'invalidprerecord_seconds'),
        ('prerecord_seconds', ''),
        ('prerecord_seconds', None),
        ('record_at', 'invalidrecord_at'),
        ('record_at', ''),
        ('record_at', None),
        ('record_id', 'invalidrecord_id'),
        ('record_id', ''),
        ('record_id', None),
        ('stream_id', 'invalidstream_id'),
        ('stream_id', ''),
        ('stream_id', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
    ])
    def test_api_shortVideoStorageRecordNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  RecordNew """
        append_record_seconds = None
        ns_id = None
        prerecord_seconds = None
        record_at = None
        record_id = None
        stream_id = None
        task_id = None
        intef = ViperopenapiApi.shortVideoStorageRecordNewPostApi(append_record_seconds=append_record_seconds, ns_id=ns_id, prerecord_seconds=prerecord_seconds, record_at=record_at, record_id=record_id, stream_id=stream_id, task_id=task_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_shortVideoStorageRecordDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  RecordDelete """
        record_id = None
        intef = ViperopenapiApi.shortVideoStorageRecordDeleteDeleteApi(record_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_shortVideoStorageRecordInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  RecordInfo """
        record_id = None
        intef = ViperopenapiApi.shortVideoStorageRecordInfoGetApi(record_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('object_id', 'invalidobject_id'),
        ('object_id', ''),
        ('object_id', None),
        ('page', 'invalidpage'),
        ('page', ''),
        ('page', None),
        ('record_at', 'invalidrecord_at'),
        ('record_at', ''),
        ('record_at', None),
    ])
    def test_api_shortVideoStorageSearchRecordsInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  SearchRecords """
        object_id = None
        page = None
        record_at = None
        intef = ViperopenapiApi.shortVideoStorageSearchRecordsPostApi(object_id=object_id, page=page, record_at=record_at, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_shortVideoStorageTaskListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.shortVideoStorageTaskListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_request', 'invalidtask_request'),
        ('task_request', ''),
        ('task_request', None),
    ])
    def test_api_shortVideoStorageTaskNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskNew """
        task_request = None
        intef = ViperopenapiApi.shortVideoStorageTaskNewPostApi(task_request=task_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_shortVideoStorageTaskDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskDelete """
        task_id = None
        intef = ViperopenapiApi.shortVideoStorageTaskDeleteDeleteApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_shortVideoStorageTaskInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskInfo """
        task_id = None
        intef = ViperopenapiApi.shortVideoStorageTaskInfoGetApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_request', 'invalidtask_request'),
        ('task_request', ''),
        ('task_request', None),
    ])
    def test_api_shortVideoStorageTaskUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskUpdate """
        task_request.task_id = None
        task_request = None
        intef = ViperopenapiApi.shortVideoStorageTaskUpdatePutApi(task_request.task_id, task_request=task_request, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('filter_name', 'invalidfilter_name'),
        ('filter_name', ''),
        ('filter_name', None),
        ('filter_tags', 'invalidfilter_tags'),
        ('filter_tags', ''),
        ('filter_tags', None),
        ('filter_auth_state', 'invalidfilter_auth_state'),
        ('filter_auth_state', ''),
        ('filter_auth_state', None),
        ('filter_created_time_range_start', 'invalidfilter_created_time_range_start'),
        ('filter_created_time_range_start', ''),
        ('filter_created_time_range_start', None),
        ('filter_created_time_range_end', 'invalidfilter_created_time_range_end'),
        ('filter_created_time_range_end', ''),
        ('filter_created_time_range_end', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
    ])
    def test_api_streamAPIAppletListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletList """
        filter_name = None
        filter_tags = None
        filter_auth_state = None
        filter_created_time_range_start = None
        filter_created_time_range_end = None
        page_offset = None
        page_limit = None
        page_total = None
        reversed = None
        intef = ViperopenapiApi.streamAPIAppletListGetApi(filter_name=filter_name, filter_tags=filter_tags, filter_auth_state=filter_auth_state, filter_created_time_range_start=filter_created_time_range_start, filter_created_time_range_end=filter_created_time_range_end, page_offset=page_offset, page_limit=page_limit, page_total=page_total, reversed=reversed, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamAPIAppletDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletDelete """
        applet_id = None
        intef = ViperopenapiApi.streamAPIAppletDeleteDeleteApi(applet_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamAPIAppletGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletGet """
        applet_id = None
        intef = ViperopenapiApi.streamAPIAppletGetGetApi(applet_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('tags', 'invalidtags'),
        ('tags', ''),
        ('tags', None),
        ('applet_id', 'invalidapplet_id'),
        ('applet_id', ''),
        ('applet_id', None),
    ])
    def test_api_streamAPIAppletUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletUpdate """
        applet_id = None
        tags = None
        intef = ViperopenapiApi.streamAPIAppletUpdatePatchApi(applet_id, tags=tags, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamAPIAppletGetByNameVersionInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletGetByNameVersion """
        applet_name = None
        applet_version = None
        intef = ViperopenapiApi.streamAPIAppletGetByNameVersionGetApi(applet_name, applet_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task_ids', 'invalidtask_ids'),
        ('task_ids', ''),
        ('task_ids', None),
    ])
    def test_api_streamAPITaskBatchGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskBatchGet """
        task_ids = None
        intef = ViperopenapiApi.streamAPITaskBatchGetPostApi(task_ids=task_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('tasks', 'invalidtasks'),
        ('tasks', ''),
        ('tasks', None),
    ])
    def test_api_streamAPITaskBatchUpdateStateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskBatchUpdateState """
        tasks = None
        intef = ViperopenapiApi.streamAPITaskBatchUpdateStatePatchApi(tasks=tasks, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamAPICamerasGetByAppletNameVersionInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  CamerasGetByAppletNameVersion """
        applet_name = None
        applet_version = None
        intef = ViperopenapiApi.streamAPICamerasGetByAppletNameVersionGetApi(applet_name, applet_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('filter_states', 'invalidfilter_states'),
        ('filter_states', ''),
        ('filter_states', None),
        ('filter_created_time_range_start', 'invalidfilter_created_time_range_start'),
        ('filter_created_time_range_start', ''),
        ('filter_created_time_range_start', None),
        ('filter_created_time_range_end', 'invalidfilter_created_time_range_end'),
        ('filter_created_time_range_end', ''),
        ('filter_created_time_range_end', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_streamAPIInstanceListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  InstanceList """
        filter_states = None
        filter_created_time_range_start = None
        filter_created_time_range_end = None
        reversed = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.streamAPIInstanceListGetApi(filter_states=filter_states, filter_created_time_range_start=filter_created_time_range_start, filter_created_time_range_end=filter_created_time_range_end, reversed=reversed, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('applet_id', 'invalidapplet_id'),
        ('applet_id', ''),
        ('applet_id', None),
        ('applet_name', 'invalidapplet_name'),
        ('applet_name', ''),
        ('applet_name', None),
        ('applet_version', 'invalidapplet_version'),
        ('applet_version', ''),
        ('applet_version', None),
        ('user_configs', 'invaliduser_configs'),
        ('user_configs', ''),
        ('user_configs', None),
    ])
    def test_api_streamAPIAppletInstanceNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletInstanceNew """
        applet_id = None
        applet_name = None
        applet_version = None
        user_configs = None
        intef = ViperopenapiApi.streamAPIAppletInstanceNewPostApi(applet_id=applet_id, applet_name=applet_name, applet_version=applet_version, user_configs=user_configs, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamAPIAppletInstanceDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletInstanceDelete """
        instance_id = None
        intef = ViperopenapiApi.streamAPIAppletInstanceDeleteDeleteApi(instance_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamAPIAppletInstanceGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletInstanceGet """
        instance_id = None
        intef = ViperopenapiApi.streamAPIAppletInstanceGetGetApi(instance_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('camera_region_id', 'invalidcamera_region_id'),
        ('camera_region_id', ''),
        ('camera_region_id', None),
        ('camera_camera_idx', 'invalidcamera_camera_idx'),
        ('camera_camera_idx', ''),
        ('camera_camera_idx', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_streamAPITaskTypeListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskTypeList """
        name = None
        camera_region_id = None
        camera_camera_idx = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.streamAPITaskTypeListGetApi(name=name, camera_region_id=camera_region_id, camera_camera_idx=camera_camera_idx, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('algo_data', 'invalidalgo_data'),
        ('algo_data', ''),
        ('algo_data', None),
        ('camera', 'invalidcamera'),
        ('camera', ''),
        ('camera', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('stream_data', 'invalidstream_data'),
        ('stream_data', ''),
        ('stream_data', None),
    ])
    def test_api_streamAPITaskTypeNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskTypeNew """
        algo_data = None
        camera = None
        name = None
        stream_data = None
        intef = ViperopenapiApi.streamAPITaskTypeNewPostApi(algo_data=algo_data, camera=camera, name=name, stream_data=stream_data, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamAPITaskTypeDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskTypeDelete """
        task_type_id = None
        intef = ViperopenapiApi.streamAPITaskTypeDeleteDeleteApi(task_type_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamAPITaskTypeGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskTypeGet """
        task_type_id = None
        intef = ViperopenapiApi.streamAPITaskTypeGetGetApi(task_type_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('algo_data', 'invalidalgo_data'),
        ('algo_data', ''),
        ('algo_data', None),
        ('stream_data', 'invalidstream_data'),
        ('stream_data', ''),
        ('stream_data', None),
        ('task_type_id', 'invalidtask_type_id'),
        ('task_type_id', ''),
        ('task_type_id', None),
    ])
    def test_api_streamAPITaskTypeUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskTypeUpdate """
        task_type_id = None
        algo_data = None
        stream_data = None
        intef = ViperopenapiApi.streamAPITaskTypeUpdatePatchApi(task_type_id, algo_data=algo_data, stream_data=stream_data, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('filter_applet_applet_name', 'invalidfilter_applet_applet_name'),
        ('filter_applet_applet_name', ''),
        ('filter_applet_applet_name', None),
        ('filter_applet_applet_version', 'invalidfilter_applet_applet_version'),
        ('filter_applet_applet_version', ''),
        ('filter_applet_applet_version', None),
        ('filter_camera_region_id', 'invalidfilter_camera_region_id'),
        ('filter_camera_region_id', ''),
        ('filter_camera_region_id', None),
        ('filter_camera_camera_idx', 'invalidfilter_camera_camera_idx'),
        ('filter_camera_camera_idx', ''),
        ('filter_camera_camera_idx', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_streamAPITaskListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskList """
        filter_applet_applet_name = None
        filter_applet_applet_version = None
        filter_camera_region_id = None
        filter_camera_camera_idx = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.streamAPITaskListGetApi(filter_applet_applet_name=filter_applet_applet_name, filter_applet_applet_version=filter_applet_applet_version, filter_camera_region_id=filter_camera_region_id, filter_camera_camera_idx=filter_camera_camera_idx, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task', 'invalidtask'),
        ('task', ''),
        ('task', None),
    ])
    def test_api_streamAPITaskNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskNew """
        task = None
        intef = ViperopenapiApi.streamAPITaskNewPostApi(task=task, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamAPITaskDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskDelete """
        task_id = None
        intef = ViperopenapiApi.streamAPITaskDeleteDeleteApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamAPITaskGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskGet """
        task_id = None
        intef = ViperopenapiApi.streamAPITaskGetGetApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('data', 'invaliddata'),
        ('data', ''),
        ('data', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
    ])
    def test_api_streamAPITaskUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskUpdate """
        task_id = None
        data = None
        intef = ViperopenapiApi.streamAPITaskUpdatePatchApi(task_id, data=data, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamFileAppletUploadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletUpload """
        intef = ViperopenapiApi.streamFileAppletUploadPostApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamFileAppletDownloadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletDownload """
        applet_name = None
        applet_version = None
        intef = ViperopenapiApi.streamFileAppletDownloadGetApi(applet_name, applet_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_streamFileAppletDocDownloadInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AppletDocDownload """
        applet_name = None
        applet_version = None
        file_path = None
        intef = ViperopenapiApi.streamFileAppletDocDownloadGetApi(applet_name, applet_version, file_path, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_ids', 'invalidcamera_ids'),
        ('camera_ids', ''),
        ('camera_ids', None),
        ('end_time', 'invalidend_time'),
        ('end_time', ''),
        ('end_time', None),
        ('filters', 'invalidfilters'),
        ('filters', ''),
        ('filters', None),
        ('measures', 'invalidmeasures'),
        ('measures', ''),
        ('measures', None),
        ('object_type', 'invalidobject_type'),
        ('object_type', ''),
        ('object_type', None),
        ('options', 'invalidoptions'),
        ('options', ''),
        ('options', None),
        ('start_time', 'invalidstart_time'),
        ('start_time', ''),
        ('start_time', None),
        ('time_interval', 'invalidtime_interval'),
        ('time_interval', ''),
        ('time_interval', None),
    ])
    def test_api_structDBAggregateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  Aggregate """
        camera_ids = None
        end_time = None
        filters = None
        measures = None
        object_type = None
        options = None
        start_time = None
        time_interval = None
        intef = ViperopenapiApi.structDBAggregatePostApi(camera_ids=camera_ids, end_time=end_time, filters=filters, measures=measures, object_type=object_type, options=options, start_time=start_time, time_interval=time_interval, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('unique_ids', 'invalidunique_ids'),
        ('unique_ids', ''),
        ('unique_ids', None),
    ])
    def test_api_structDBDeleteObjectsInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteObjects """
        unique_ids = None
        intef = ViperopenapiApi.structDBDeleteObjectsPostApi(unique_ids=unique_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
        ('object_type', 'invalidobject_type'),
        ('object_type', ''),
        ('object_type', None),
    ])
    def test_api_structDBDeleteObjectsBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteObjectsBeforeDate """
        date = None
        object_type = None
        intef = ViperopenapiApi.structDBDeleteObjectsBeforeDatePostApi(date=date, object_type=object_type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_structDBGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.structDBGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
    ])
    def test_api_structDBNamespaceListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceList """
        page_offset = None
        page_limit = None
        page_total = None
        intef = ViperopenapiApi.structDBNamespaceListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('namespace', 'invalidnamespace'),
        ('namespace', ''),
        ('namespace', None),
    ])
    def test_api_structDBNamespaceNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceNew """
        namespace.ns_id = None
        namespace = None
        intef = ViperopenapiApi.structDBNamespaceNewPostApi(namespace.ns_id, namespace=namespace, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_structDBNamespaceDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  NamespaceDelete """
        ns_id = None
        intef = ViperopenapiApi.structDBNamespaceDeleteDeleteApi(ns_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_ids', 'invalidcamera_ids'),
        ('camera_ids', ''),
        ('camera_ids', None),
        ('deduplication', 'invaliddeduplication'),
        ('deduplication', ''),
        ('deduplication', None),
        ('end_time', 'invalidend_time'),
        ('end_time', ''),
        ('end_time', None),
        ('filters', 'invalidfilters'),
        ('filters', ''),
        ('filters', None),
        ('marker', 'invalidmarker'),
        ('marker', ''),
        ('marker', None),
        ('object_id', 'invalidobject_id'),
        ('object_id', ''),
        ('object_id', None),
        ('object_type', 'invalidobject_type'),
        ('object_type', ''),
        ('object_type', None),
        ('options', 'invalidoptions'),
        ('options', ''),
        ('options', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('start_time', 'invalidstart_time'),
        ('start_time', ''),
        ('start_time', None),
        ('timestamp_asc', 'invalidtimestamp_asc'),
        ('timestamp_asc', ''),
        ('timestamp_asc', None),
        ('track_total_hits', 'invalidtrack_total_hits'),
        ('track_total_hits', ''),
        ('track_total_hits', None),
    ])
    def test_api_structDBQueryInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  Query """
        camera_ids = None
        deduplication = None
        end_time = None
        filters = None
        marker = None
        object_id = None
        object_type = None
        options = None
        page_limit = None
        page_offset = None
        start_time = None
        timestamp_asc = None
        track_total_hits = None
        intef = ViperopenapiApi.structDBQueryPostApi(camera_ids=camera_ids, deduplication=deduplication, end_time=end_time, filters=filters, marker=marker, object_id=object_id, object_type=object_type, options=options, page_limit=page_limit, page_offset=page_offset, start_time=start_time, timestamp_asc=timestamp_asc, track_total_hits=track_total_hits, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_timespaceDBMultiV3DBListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DBList """
        deploy_type = None
        intef = ViperopenapiApi.timespaceDBMultiV3DBListGetApi(deploy_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('capacity', 'invalidcapacity'),
        ('capacity', ''),
        ('capacity', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('object_type', 'invalidobject_type'),
        ('object_type', ''),
        ('object_type', None),
    ])
    def test_api_timespaceDBMultiV3DBNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DBNew """
        deploy_type = None
        capacity = None
        db_id = None
        description = None
        feature_version = None
        object_type = None
        intef = ViperopenapiApi.timespaceDBMultiV3DBNewPostApi(deploy_type, capacity=capacity, db_id=db_id, description=description, feature_version=feature_version, object_type=object_type, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_timespaceDBMultiV3DBDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DBDelete """
        deploy_type = None
        db_id = None
        intef = ViperopenapiApi.timespaceDBMultiV3DBDeleteDeleteApi(deploy_type, db_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_timespaceDBMultiV3DBGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DBGet """
        deploy_type = None
        db_id = None
        intef = ViperopenapiApi.timespaceDBMultiV3DBGetGetApi(deploy_type, db_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_timespaceDBMultiV3GetSystemInfoV3InvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfoV3 """
        deploy_type = None
        intef = ViperopenapiApi.timespaceDBMultiV3GetSystemInfoV3GetApi(deploy_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('object_info', 'invalidobject_info'),
        ('object_info', ''),
        ('object_info', None),
    ])
    def test_api_timespaceDBAddFeatureAsyncInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  AddFeatureAsync """
        deploy_type = None
        object_type = None
        feature_version = None
        db_id = None
        object_info = None
        intef = ViperopenapiApi.timespaceDBAddFeatureAsyncPostApi(deploy_type, object_type, feature_version, db_id=db_id, object_info=object_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('ignore_feature', 'invalidignore_feature'),
        ('ignore_feature', ''),
        ('ignore_feature', None),
        ('object_ids', 'invalidobject_ids'),
        ('object_ids', ''),
        ('object_ids', None),
    ])
    def test_api_timespaceDBBatchGetFeatureByObjectIDInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  BatchGetFeatureByObjectID """
        deploy_type = None
        object_type = None
        feature_version = None
        db_id = None
        ignore_feature = None
        object_ids = None
        intef = ViperopenapiApi.timespaceDBBatchGetFeatureByObjectIDPostApi(deploy_type, object_type, feature_version, db_id=db_id, ignore_feature=ignore_feature, object_ids=object_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('key', 'invalidkey'),
        ('key', ''),
        ('key', None),
        ('period_start', 'invalidperiod_start'),
        ('period_start', ''),
        ('period_start', None),
        ('period_end', 'invalidperiod_end'),
        ('period_end', ''),
        ('period_end', None),
        ('load_mode', 'invalidload_mode'),
        ('load_mode', ''),
        ('load_mode', None),
        ('max_preview_load_count', 'invalidmax_preview_load_count'),
        ('max_preview_load_count', ''),
        ('max_preview_load_count', None),
        ('results_filter_filter_mode', 'invalidresults_filter_filter_mode'),
        ('results_filter_filter_mode', ''),
        ('results_filter_filter_mode', None),
        ('results_filter_preview_results_count', 'invalidresults_filter_preview_results_count'),
        ('results_filter_preview_results_count', ''),
        ('results_filter_preview_results_count', None),
    ])
    def test_api_timespaceDBClusterGetByKeyInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ClusterGetByKey """
        deploy_type = None
        object_type = None
        feature_version = None
        key = None
        period_start = None
        period_end = None
        load_mode = None
        max_preview_load_count = None
        results_filter_filter_mode = None
        results_filter_preview_results_count = None
        intef = ViperopenapiApi.timespaceDBClusterGetByKeyGetApi(deploy_type, object_type, feature_version, key=key, period_start=period_start, period_end=period_end, load_mode=load_mode, max_preview_load_count=max_preview_load_count, results_filter_filter_mode=results_filter_filter_mode, results_filter_preview_results_count=results_filter_preview_results_count, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
        ('feature', 'invalidfeature'),
        ('feature', ''),
        ('feature', None),
        ('filter_configs', 'invalidfilter_configs'),
        ('filter_configs', ''),
        ('filter_configs', None),
        ('load_mode', 'invalidload_mode'),
        ('load_mode', ''),
        ('load_mode', None),
        ('max_preview_load_count', 'invalidmax_preview_load_count'),
        ('max_preview_load_count', ''),
        ('max_preview_load_count', None),
    ])
    def test_api_timespaceDBClusterSearchInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ClusterSearch """
        deploy_type = None
        object_type = None
        feature_version = None
        config = None
        feature = None
        filter_configs = None
        load_mode = None
        max_preview_load_count = None
        intef = ViperopenapiApi.timespaceDBClusterSearchPostApi(deploy_type, object_type, feature_version, config=config, feature=feature, filter_configs=filter_configs, load_mode=load_mode, max_preview_load_count=max_preview_load_count, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('period_start', 'invalidperiod_start'),
        ('period_start', ''),
        ('period_start', None),
        ('period_end', 'invalidperiod_end'),
        ('period_end', ''),
        ('period_end', None),
        ('page_offset', 'invalidpage_offset'),
        ('page_offset', ''),
        ('page_offset', None),
        ('page_limit', 'invalidpage_limit'),
        ('page_limit', ''),
        ('page_limit', None),
        ('page_total', 'invalidpage_total'),
        ('page_total', ''),
        ('page_total', None),
        ('ignore_centroid', 'invalidignore_centroid'),
        ('ignore_centroid', ''),
        ('ignore_centroid', None),
    ])
    def test_api_timespaceDBClusterGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ClusterGet """
        deploy_type = None
        object_type = None
        feature_version = None
        cluster_id = None
        period_start = None
        period_end = None
        page_offset = None
        page_limit = None
        page_total = None
        ignore_centroid = None
        intef = ViperopenapiApi.timespaceDBClusterGetGetApi(deploy_type, object_type, feature_version, cluster_id, period_start=period_start, period_end=period_end, page_offset=page_offset, page_limit=page_limit, page_total=page_total, ignore_centroid=ignore_centroid, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('cluster_id', 'invalidcluster_id'),
        ('cluster_id', ''),
        ('cluster_id', None),
        ('extra_info', 'invalidextra_info'),
        ('extra_info', ''),
        ('extra_info', None),
    ])
    def test_api_timespaceDBClusterPutInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ClusterPut """
        deploy_type = None
        object_type = None
        feature_version = None
        cluster_id = None
        extra_info = None
        intef = ViperopenapiApi.timespaceDBClusterPutPutApi(deploy_type, object_type, feature_version, cluster_id, extra_info=extra_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_timespaceDBDeleteFeatureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteFeature """
        deploy_type = None
        object_type = None
        feature_version = None
        db_id = None
        id = None
        intef = ViperopenapiApi.timespaceDBDeleteFeaturePostApi(deploy_type, object_type, feature_version, db_id=db_id, id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('date', 'invaliddate'),
        ('date', ''),
        ('date', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
    ])
    def test_api_timespaceDBDeleteShardsBeforeDateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DeleteShardsBeforeDate """
        deploy_type = None
        object_type = None
        feature_version = None
        date = None
        db_id = None
        intef = ViperopenapiApi.timespaceDBDeleteShardsBeforeDatePostApi(deploy_type, object_type, feature_version, date=date, db_id=db_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_timespaceDBGetFeatureInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetFeature """
        deploy_type = None
        object_type = None
        feature_version = None
        db_id = None
        id = None
        intef = ViperopenapiApi.timespaceDBGetFeaturePostApi(deploy_type, object_type, feature_version, db_id=db_id, id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_timespaceDBGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        deploy_type = None
        object_type = None
        feature_version = None
        intef = ViperopenapiApi.timespaceDBGetSystemInfoGetApi(deploy_type, object_type, feature_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('data_sources', 'invaliddata_sources'),
        ('data_sources', ''),
        ('data_sources', None),
    ])
    def test_api_timespaceDBLabelingDataSourcesSetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  LabelingDataSourcesSet """
        deploy_type = None
        object_type = None
        feature_version = None
        data_sources = None
        intef = ViperopenapiApi.timespaceDBLabelingDataSourcesSetPostApi(deploy_type, object_type, feature_version, data_sources=data_sources, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_timespaceDBLabelingGetInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  LabelingGetInfo """
        deploy_type = None
        object_type = None
        feature_version = None
        intef = ViperopenapiApi.timespaceDBLabelingGetInfoGetApi(deploy_type, object_type, feature_version, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
    ])
    def test_api_timespaceDBLabelingModeSetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  LabelingModeSet """
        deploy_type = None
        object_type = None
        feature_version = None
        mode = None
        intef = ViperopenapiApi.timespaceDBLabelingModeSetPostApi(deploy_type, object_type, feature_version, mode=mode, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_ids', 'invalidcamera_ids'),
        ('camera_ids', ''),
        ('camera_ids', None),
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('marker', 'invalidmarker'),
        ('marker', ''),
        ('marker', None),
        ('page_size', 'invalidpage_size'),
        ('page_size', ''),
        ('page_size', None),
        ('period', 'invalidperiod'),
        ('period', ''),
        ('period', None),
        ('reversed', 'invalidreversed'),
        ('reversed', ''),
        ('reversed', None),
    ])
    def test_api_timespaceDBListFeaturesInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  ListFeatures """
        deploy_type = None
        object_type = None
        feature_version = None
        camera_ids = None
        db_id = None
        marker = None
        page_size = None
        period = None
        reversed = None
        intef = ViperopenapiApi.timespaceDBListFeaturesPostApi(deploy_type, object_type, feature_version, camera_ids=camera_ids, db_id=db_id, marker=marker, page_size=page_size, period=period, reversed=reversed, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('config', 'invalidconfig'),
        ('config', ''),
        ('config', None),
        ('feature', 'invalidfeature'),
        ('feature', ''),
        ('feature', None),
    ])
    def test_api_timespaceDBSearchInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  Search """
        deploy_type = None
        object_type = None
        feature_version = None
        config = None
        feature = None
        intef = ViperopenapiApi.timespaceDBSearchPostApi(deploy_type, object_type, feature_version, config=config, feature=feature, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('source_info', 'invalidsource_info'),
        ('source_info', ''),
        ('source_info', None),
    ])
    def test_api_videoIngressGenerateRTMPAddressInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GenerateRTMPAddress """
        source_info = None
        intef = ViperopenapiApi.videoIngressGenerateRTMPAddressPostApi(source_info=source_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('source_info', 'invalidsource_info'),
        ('source_info', ''),
        ('source_info', None),
    ])
    def test_api_videoIngressGenerateRTSPAddressInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GenerateRTSPAddress """
        source_info = None
        intef = ViperopenapiApi.videoIngressGenerateRTSPAddressPostApi(source_info=source_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_videoIngressGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.videoIngressGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_videoIngressStreamInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  StreamInfo """
        url = None
        intef = ViperopenapiApi.videoIngressStreamInfoGetApi(url, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('source_info', 'invalidsource_info'),
        ('source_info', ''),
        ('source_info', None),
    ])
    def test_api_videoIngressGetStreamInformationInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetStreamInformation """
        source_info = None
        intef = ViperopenapiApi.videoIngressGetStreamInformationPostApi(source_info=source_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_videoProcessGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        intef = ViperopenapiApi.videoProcessGetSystemInfoGetApi(sendRequest=False)

        resp = intef.request()
        assert resp.status_code != 200

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
    def test_api_videoProcessTaskListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskList """
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        intef = ViperopenapiApi.videoProcessTaskListGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task', 'invalidtask'),
        ('task', ''),
        ('task', None),
    ])
    def test_api_videoProcessTaskNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskNew """
        task = None
        intef = ViperopenapiApi.videoProcessTaskNewPostApi(task=task, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_videoProcessTaskDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskDelete """
        task_id = None
        intef = ViperopenapiApi.videoProcessTaskDeleteDeleteApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_videoProcessTaskStatusInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskStatus """
        task_id = None
        intef = ViperopenapiApi.videoProcessTaskStatusGetApi(task_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('task', 'invalidtask'),
        ('task', ''),
        ('task', None),
        ('task_id', 'invalidtask_id'),
        ('task_id', ''),
        ('task_id', None),
    ])
    def test_api_videoProcessTaskUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  TaskUpdate """
        task_id = None
        task = None
        intef = ViperopenapiApi.videoProcessTaskUpdatePostApi(task_id, task=task, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('configs', 'invalidconfigs'),
        ('configs', ''),
        ('configs', None),
        ('dropped_fields', 'invaliddropped_fields'),
        ('dropped_fields', ''),
        ('dropped_fields', None),
        ('features', 'invalidfeatures'),
        ('features', ''),
        ('features', None),
        ('merge_top_k', 'invalidmerge_top_k'),
        ('merge_top_k', ''),
        ('merge_top_k', None),
    ])
    def test_api_staticDBFeatureBatchSearchMultiInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureBatchSearchMulti """
        db_type = None
        configs = None
        dropped_fields = None
        features = None
        merge_top_k = None
        intef = ViperopenapiApi.staticDBFeatureBatchSearchMultiPostApi(db_type, configs=configs, dropped_fields=dropped_fields, features=features, merge_top_k=merge_top_k, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_staticDBDBListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DBList """
        db_type = None
        intef = ViperopenapiApi.staticDBDBListGetApi(db_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_size', 'invaliddb_size'),
        ('db_size', ''),
        ('db_size', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('feature_version', 'invalidfeature_version'),
        ('feature_version', ''),
        ('feature_version', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('object_type', 'invalidobject_type'),
        ('object_type', ''),
        ('object_type', None),
        ('options', 'invalidoptions'),
        ('options', ''),
        ('options', None),
    ])
    def test_api_staticDBDBNewInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DBNew """
        db_type = None
        db_size = None
        description = None
        feature_version = None
        name = None
        object_type = None
        options = None
        intef = ViperopenapiApi.staticDBDBNewPostApi(db_type, db_size=db_size, description=description, feature_version=feature_version, name=name, object_type=object_type, options=options, sendRequest=False)
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
    def test_api_staticDBFeatureBatchAddInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureBatchAdd """
        db_type = None
        col_id = None
        items = None
        intef = ViperopenapiApi.staticDBFeatureBatchAddPostApi(db_type, col_id, items=items, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('col_id', 'invalidcol_id'),
        ('col_id', ''),
        ('col_id', None),
        ('ids', 'invalidids'),
        ('ids', ''),
        ('ids', None),
    ])
    def test_api_staticDBFeatureBatchDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureBatchDelete """
        db_type = None
        col_id = None
        ids = None
        intef = ViperopenapiApi.staticDBFeatureBatchDeletePostApi(db_type, col_id, ids=ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('col_id', 'invalidcol_id'),
        ('col_id', ''),
        ('col_id', None),
        ('keys', 'invalidkeys'),
        ('keys', ''),
        ('keys', None),
    ])
    def test_api_staticDBFeatureBatchDeleteByKeyInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureBatchDeleteByKey """
        db_type = None
        col_id = None
        keys = None
        intef = ViperopenapiApi.staticDBFeatureBatchDeleteByKeyPostApi(db_type, col_id, keys=keys, sendRequest=False)
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
        ('ids', 'invalidids'),
        ('ids', ''),
        ('ids', None),
    ])
    def test_api_staticDBFeatureBatchGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureBatchGet """
        db_type = None
        col_id = None
        consistency = None
        ids = None
        intef = ViperopenapiApi.staticDBFeatureBatchGetPostApi(db_type, col_id, consistency=consistency, ids=ids, sendRequest=False)
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
    def test_api_staticDBFeatureBatchGetByKeyInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureBatchGetByKey """
        db_type = None
        col_id = None
        consistency = None
        ignore_details = None
        keys = None
        intef = ViperopenapiApi.staticDBFeatureBatchGetByKeyPostApi(db_type, col_id, consistency=consistency, ignore_details=ignore_details, keys=keys, sendRequest=False)
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
        ('marker', 'invalidmarker'),
        ('marker', ''),
        ('marker', None),
        ('page_size', 'invalidpage_size'),
        ('page_size', ''),
        ('page_size', None),
    ])
    def test_api_staticDBFeatureBatchGetByKeyPagingInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureBatchGetByKeyPaging """
        db_type = None
        col_id = None
        consistency = None
        ignore_details = None
        keys = None
        marker = None
        page_size = None
        intef = ViperopenapiApi.staticDBFeatureBatchGetByKeyPagingPostApi(db_type, col_id, consistency=consistency, ignore_details=ignore_details, keys=keys, marker=marker, page_size=page_size, sendRequest=False)
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
        ('dropped_fields', 'invaliddropped_fields'),
        ('dropped_fields', ''),
        ('dropped_fields', None),
        ('features', 'invalidfeatures'),
        ('features', ''),
        ('features', None),
        ('min_score', 'invalidmin_score'),
        ('min_score', ''),
        ('min_score', None),
        ('return_raw_feature', 'invalidreturn_raw_feature'),
        ('return_raw_feature', ''),
        ('return_raw_feature', None),
        ('top_k', 'invalidtop_k'),
        ('top_k', ''),
        ('top_k', None),
    ])
    def test_api_staticDBFeatureBatchSearchInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureBatchSearch """
        db_type = None
        col_id = None
        consistency = None
        dropped_fields = None
        features = None
        min_score = None
        return_raw_feature = None
        top_k = None
        intef = ViperopenapiApi.staticDBFeatureBatchSearchPostApi(db_type, col_id, consistency=consistency, dropped_fields=dropped_fields, features=features, min_score=min_score, return_raw_feature=return_raw_feature, top_k=top_k, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('col_id', 'invalidcol_id'),
        ('col_id', ''),
        ('col_id', None),
        ('marker', 'invalidmarker'),
        ('marker', ''),
        ('marker', None),
        ('page_size', 'invalidpage_size'),
        ('page_size', ''),
        ('page_size', None),
    ])
    def test_api_staticDBFeatureListInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureList """
        db_type = None
        col_id = None
        marker = None
        page_size = None
        intef = ViperopenapiApi.staticDBFeatureListPostApi(db_type, col_id, marker=marker, page_size=page_size, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('col_id', 'invalidcol_id'),
        ('col_id', ''),
        ('col_id', None),
        ('extra_info', 'invalidextra_info'),
        ('extra_info', ''),
        ('extra_info', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_staticDBFeatureUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureUpdate """
        db_type = None
        col_id = None
        id = None
        extra_info = None
        intef = ViperopenapiApi.staticDBFeatureUpdatePatchApi(db_type, col_id, id, extra_info=extra_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('col_id', 'invalidcol_id'),
        ('col_id', ''),
        ('col_id', None),
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
        ('item', 'invaliditem'),
        ('item', ''),
        ('item', None),
    ])
    def test_api_staticDBFeatureUpdateByIDInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  FeatureUpdateByID """
        db_type = None
        col_id = None
        id = None
        item = None
        intef = ViperopenapiApi.staticDBFeatureUpdateByIDPatchApi(db_type, col_id, id, item=item, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_staticDBDBDeleteInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DBDelete """
        db_type = None
        db_id = None
        intef = ViperopenapiApi.staticDBDBDeleteDeleteApi(db_type, db_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('ignore_indexes_detail', 'invalidignore_indexes_detail'),
        ('ignore_indexes_detail', ''),
        ('ignore_indexes_detail', None),
    ])
    def test_api_staticDBDBGetInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DBGet """
        db_type = None
        db_id = None
        ignore_indexes_detail = None
        intef = ViperopenapiApi.staticDBDBGetGetApi(db_type, db_id, ignore_indexes_detail=ignore_indexes_detail, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('object_type', 'invalidobject_type'),
        ('object_type', ''),
        ('object_type', None),
        ('options', 'invalidoptions'),
        ('options', ''),
        ('options', None),
    ])
    def test_api_staticDBDBUpdateInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DBUpdate """
        db_type = None
        db_id = None
        description = None
        name = None
        object_type = None
        options = None
        intef = ViperopenapiApi.staticDBDBUpdatePatchApi(db_type, db_id, description=description, name=name, object_type=object_type, options=options, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('mode', 'invalidmode'),
        ('mode', ''),
        ('mode', None),
    ])
    def test_api_staticDBDBTrainInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  DBTrain """
        db_type = None
        db_id = None
        mode = None
        intef = ViperopenapiApi.staticDBDBTrainPostApi(db_type, db_id, mode=mode, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_staticDBGetSnapshotStatusInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSnapshotStatus """
        db_type = None
        intef = ViperopenapiApi.staticDBGetSnapshotStatusGetApi(db_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_staticDBGetSystemInfoInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        db_type = None
        intef = ViperopenapiApi.staticDBGetSystemInfoGetApi(db_type, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('camera_info', 'invalidcamera_info'),
        ('camera_info', ''),
        ('camera_info', None),
        ('capture_time', 'invalidcapture_time'),
        ('capture_time', ''),
        ('capture_time', None),
        ('extra_fields', 'invalidextra_fields'),
        ('extra_fields', ''),
        ('extra_fields', None),
        ('extra_info', 'invalidextra_info'),
        ('extra_info', ''),
        ('extra_info', None),
        ('full_image', 'invalidfull_image'),
        ('full_image', ''),
        ('full_image', None),
        ('ns_id', 'invalidns_id'),
        ('ns_id', ''),
        ('ns_id', None),
        ('receive_time', 'invalidreceive_time'),
        ('receive_time', ''),
        ('receive_time', None),
        ('storage_policy', 'invalidstorage_policy'),
        ('storage_policy', ''),
        ('storage_policy', None),
        ('target_images', 'invalidtarget_images'),
        ('target_images', ''),
        ('target_images', None),
        ('task_object_config', 'invalidtask_object_config'),
        ('task_object_config', ''),
        ('task_object_config', None),
    ])
    def test_api_imageIngressPassiveIngressStandardTargetImageAsyncInvalidParam(self, invalidParam, config_obj, ViperopenapiApi):
        """  IngressStandardTargetImageAsync """
        camera_info = None
        capture_time = None
        extra_fields = None
        extra_info = None
        full_image = None
        ns_id = None
        receive_time = None
        storage_policy = None
        target_images = None
        task_object_config = None
        intef = ViperopenapiApi.imageIngressPassiveIngressStandardTargetImageAsyncPostApi(camera_info=camera_info, capture_time=capture_time, extra_fields=extra_fields, extra_info=extra_info, full_image=full_image, ns_id=ns_id, receive_time=receive_time, storage_policy=storage_policy, target_images=target_images, task_object_config=task_object_config, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
