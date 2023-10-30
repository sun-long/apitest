#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestViperopenapiApi(object):
    """ viperOpenApi Api测试"""

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

    def test_api_kafkaCallbackExampleCallback(self, config_obj, ViperopenapiApi):
        """  Callback """
        batch_objects = None
        resp = ViperopenapiApi.kafkaCallbackExampleCallbackPostApi(batch_objects=batch_objects)
        assert resp.status_code == 200

    def test_api_streamMessageCallback(self, config_obj, ViperopenapiApi):
        """  Callback """
        messages = None
        resp = ViperopenapiApi.streamMessageCallbackPostApi(messages=messages)
        assert resp.status_code == 200

    def test_api_batchVideoProcessJobList(self, config_obj, ViperopenapiApi):
        """  JobList """
        page_offset = None
        page_limit = None
        page_total = None
        period_start = None
        period_end = None
        status = None
        resp = ViperopenapiApi.batchVideoProcessJobListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, period_start=period_start, period_end=period_end, status=status)
        assert resp.status_code == 200

    def test_api_batchVideoProcessJobNew(self, config_obj, ViperopenapiApi):
        """  JobNew """
        config = None
        resp = ViperopenapiApi.batchVideoProcessJobNewPostApi(config=config)
        assert resp.status_code == 200

    def test_api_batchVideoProcessJobDelete(self, config_obj, ViperopenapiApi):
        """  JobDelete """
        job_id = None
        resp = ViperopenapiApi.batchVideoProcessJobDeleteDeleteApi(job_id)
        assert resp.status_code == 200

    def test_api_batchVideoProcessJobGet(self, config_obj, ViperopenapiApi):
        """  JobGet """
        job_id = None
        resp = ViperopenapiApi.batchVideoProcessJobGetGetApi(job_id)
        assert resp.status_code == 200

    def test_api_batchVideoProcessJobCancel(self, config_obj, ViperopenapiApi):
        """  JobCancel """
        job_id = None
        resp = ViperopenapiApi.batchVideoProcessJobCancelPostApi(job_id)
        assert resp.status_code == 200

    def test_api_clusteringJobMgrDeleteClusterBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteClusterBeforeDate """
        Threshold = None
        date = None
        is_delete_anonymous_cluster = None
        is_delete_identified_cluster = None
        resp = ViperopenapiApi.clusteringJobMgrDeleteClusterBeforeDatePostApi(Threshold=Threshold, date=date, is_delete_anonymous_cluster=is_delete_anonymous_cluster, is_delete_identified_cluster=is_delete_identified_cluster)
        assert resp.status_code == 200

    def test_api_clusteringJobMgrLabelingByExtraDataSources(self, config_obj, ViperopenapiApi):
        """  LabelingByExtraDataSources """
        data_sources = None
        min_score = None
        resp = ViperopenapiApi.clusteringJobMgrLabelingByExtraDataSourcesPostApi(data_sources=data_sources, min_score=min_score)
        assert resp.status_code == 200

    def test_api_clusteringJobMgrMatrixGeneration(self, config_obj, ViperopenapiApi):
        """  MatrixGeneration """
        resp = ViperopenapiApi.clusteringJobMgrMatrixGenerationPostApi()
        assert resp.status_code == 200

    def test_api_dataFusionDeleteJobsBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteJobsBeforeDate """
        catalog = None
        date = None
        resp = ViperopenapiApi.dataFusionDeleteJobsBeforeDatePostApi(catalog=catalog, date=date)
        assert resp.status_code == 200

    def test_api_dataFusionGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.dataFusionGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_dataFusionJobList(self, config_obj, ViperopenapiApi):
        """  JobList """
        type = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.dataFusionJobListGetApi(type=type, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_dataFusionJobNew(self, config_obj, ViperopenapiApi):
        """  JobNew """
        config = None
        resp = ViperopenapiApi.dataFusionJobNewPostApi(config=config)
        assert resp.status_code == 200

    def test_api_dataFusionJobDelete(self, config_obj, ViperopenapiApi):
        """  JobDelete """
        job_id = None
        resp = ViperopenapiApi.dataFusionJobDeleteDeleteApi(job_id)
        assert resp.status_code == 200

    def test_api_dataFusionJobGet(self, config_obj, ViperopenapiApi):
        """  JobGet """
        job_id = None
        resp = ViperopenapiApi.dataFusionJobGetGetApi(job_id)
        assert resp.status_code == 200

    def test_api_dataFusionJobCancel(self, config_obj, ViperopenapiApi):
        """  JobCancel """
        job_id = None
        resp = ViperopenapiApi.dataFusionJobCancelPostApi(job_id)
        assert resp.status_code == 200

    def test_api_batchDBIntersectionJobList(self, config_obj, ViperopenapiApi):
        """  JobList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.batchDBIntersectionJobListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_batchDBIntersectionJobNew(self, config_obj, ViperopenapiApi):
        """  JobNew """
        config = None
        resp = ViperopenapiApi.batchDBIntersectionJobNewPostApi(config=config)
        assert resp.status_code == 200

    def test_api_batchDBIntersectionJobDelete(self, config_obj, ViperopenapiApi):
        """  JobDelete """
        job_id = None
        resp = ViperopenapiApi.batchDBIntersectionJobDeleteDeleteApi(job_id)
        assert resp.status_code == 200

    def test_api_batchDBIntersectionJobGet(self, config_obj, ViperopenapiApi):
        """  JobGet """
        job_id = None
        resp = ViperopenapiApi.batchDBIntersectionJobGetGetApi(job_id)
        assert resp.status_code == 200

    def test_api_batchDBIntersectionJobCancel(self, config_obj, ViperopenapiApi):
        """  JobCancel """
        job_id = None
        resp = ViperopenapiApi.batchDBIntersectionJobCancelPostApi(job_id)
        assert resp.status_code == 200

    def test_api_infraBatchMgrBatchManagerFileDownload(self, config_obj, ViperopenapiApi):
        """  BatchManagerFileDownload """
        path = None
        resp = ViperopenapiApi.infraBatchMgrBatchManagerFileDownloadGetApi(path)
        assert resp.status_code == 200

    def test_api_infraBatchMgrBatchManagerHdfsDownload(self, config_obj, ViperopenapiApi):
        """  BatchManagerHdfsDownload """
        path = None
        resp = ViperopenapiApi.infraBatchMgrBatchManagerHdfsDownloadGetApi(path)
        assert resp.status_code == 200

    def test_api_infraBatchMgrGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.infraBatchMgrGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_infraBatchMgrJobList(self, config_obj, ViperopenapiApi):
        """  JobList """
        page_offset = None
        page_limit = None
        page_total = None
        catalog = None
        period_start = None
        period_end = None
        status = None
        resp = ViperopenapiApi.infraBatchMgrJobListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, catalog=catalog, period_start=period_start, period_end=period_end, status=status)
        assert resp.status_code == 200

    def test_api_infraBatchMgrJobNew(self, config_obj, ViperopenapiApi):
        """  JobNew """
        job = None
        resp = ViperopenapiApi.infraBatchMgrJobNewPostApi(job=job)
        assert resp.status_code == 200

    def test_api_infraBatchMgrJobDelete(self, config_obj, ViperopenapiApi):
        """  JobDelete """
        job_id = None
        resp = ViperopenapiApi.infraBatchMgrJobDeleteDeleteApi(job_id)
        assert resp.status_code == 200

    def test_api_infraBatchMgrJobGet(self, config_obj, ViperopenapiApi):
        """  JobGet """
        job_id = None
        resp = ViperopenapiApi.infraBatchMgrJobGetGetApi(job_id)
        assert resp.status_code == 200

    def test_api_infraBatchMgrJobCancel(self, config_obj, ViperopenapiApi):
        """  JobCancel """
        job_id = None
        resp = ViperopenapiApi.infraBatchMgrJobCancelPostApi(job_id)
        assert resp.status_code == 200

    def test_api_infraBatchMgrDeleteJobsBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteJobsBeforeDate """
        catalog = None
        date = None
        resp = ViperopenapiApi.infraBatchMgrDeleteJobsBeforeDatePostApi(catalog=catalog, date=date)
        assert resp.status_code == 200

    def test_api_infraConsoleCertificateInfos(self, config_obj, ViperopenapiApi):
        """  CertificateInfos """
        resp = ViperopenapiApi.infraConsoleCertificateInfosGetApi()
        assert resp.status_code == 200

    def test_api_infraConsoleComponentList(self, config_obj, ViperopenapiApi):
        """  ComponentList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.infraConsoleComponentListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_infraConsoleDeleteESBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteESBeforeDate """
        date = None
        index_type = None
        resp = ViperopenapiApi.infraConsoleDeleteESBeforeDatePostApi(date=date, index_type=index_type)
        assert resp.status_code == 200

    def test_api_infraConsoleFeatureVersions(self, config_obj, ViperopenapiApi):
        """  FeatureVersions """
        resp = ViperopenapiApi.infraConsoleFeatureVersionsGetApi()
        assert resp.status_code == 200

    def test_api_infraConsoleGetFilteredStorageConfig(self, config_obj, ViperopenapiApi):
        """  GetFilteredStorageConfig """
        resp = ViperopenapiApi.infraConsoleGetFilteredStorageConfigGetApi()
        assert resp.status_code == 200

    def test_api_infraConsoleUpdateFilteredStorageConfig(self, config_obj, ViperopenapiApi):
        """  UpdateFilteredStorageConfig """
        filtered_storage_disable = None
        resp = ViperopenapiApi.infraConsoleUpdateFilteredStorageConfigPostApi(filtered_storage_disable=filtered_storage_disable)
        assert resp.status_code == 200

    def test_api_infraConsoleGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.infraConsoleGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_infraConsoleStatisticsModule(self, config_obj, ViperopenapiApi):
        """  StatisticsModule """
        module_name = None
        resp = ViperopenapiApi.infraConsoleStatisticsModuleGetApi(module_name)
        assert resp.status_code == 200

    def test_api_infraConsoleStatisticsModuleByCamera(self, config_obj, ViperopenapiApi):
        """  StatisticsModuleByCamera """
        module_name = None
        camera_id = None
        device_id = None
        task_id = None
        resp = ViperopenapiApi.infraConsoleStatisticsModuleByCameraPostApi(module_name, camera_id=camera_id, device_id=device_id, task_id=task_id)
        assert resp.status_code == 200

    def test_api_infraConsoleStatisticsNodeList(self, config_obj, ViperopenapiApi):
        """  StatisticsNodeList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.infraConsoleStatisticsNodeListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_infraConsoleAPIUserCredentialGet(self, config_obj, ViperopenapiApi):
        """  APIUserCredentialGet """
        username = None
        password = None
        resp = ViperopenapiApi.infraConsoleAPIUserCredentialGetPostApi(username, password=password)
        assert resp.status_code == 200

    def test_api_infraModelMgrBlobDownload(self, config_obj, ViperopenapiApi):
        """  BlobDownload """
        blob_id = None
        resp = ViperopenapiApi.infraModelMgrBlobDownloadGetApi(blob_id)
        assert resp.status_code == 200

    def test_api_infraModelMgrBlobUpload(self, config_obj, ViperopenapiApi):
        """  BlobUpload """
        blob_id = None
        resp = ViperopenapiApi.infraModelMgrBlobUploadPostApi(blob_id)
        assert resp.status_code == 200

    def test_api_infraModelMgrGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.infraModelMgrGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_infraModelMgrModelList(self, config_obj, ViperopenapiApi):
        """  ModelList """
        model_path_type = None
        model_path_sub_type = None
        model_path_runtime = None
        model_path_hardware = None
        model_path_name = None
        resp = ViperopenapiApi.infraModelMgrModelListGetApi(model_path_type=model_path_type, model_path_sub_type=model_path_sub_type, model_path_runtime=model_path_runtime, model_path_hardware=model_path_hardware, model_path_name=model_path_name)
        assert resp.status_code == 200

    def test_api_infraModelMgrModelNew(self, config_obj, ViperopenapiApi):
        """  ModelNew """
        model = None
        overwrite = None
        resp = ViperopenapiApi.infraModelMgrModelNewPostApi(model=model, overwrite=overwrite)
        assert resp.status_code == 200

    def test_api_infraModelMgrModelSynchronize(self, config_obj, ViperopenapiApi):
        """  ModelSynchronize """
        resp = ViperopenapiApi.infraModelMgrModelSynchronizePostApi()
        assert resp.status_code == 200



    def test_api_infraOSGDownloadObject(self, config_obj, ViperopenapiApi):
        """  DownloadObject """
        bucket_name = None
        object_key = None
        resp = ViperopenapiApi.infraOSGDownloadObjectGetApi(bucket_name, object_key)
        assert resp.status_code == 200

    def test_api_infraOSGListBuckets(self, config_obj, ViperopenapiApi):
        """  ListBuckets """
        resp = ViperopenapiApi.infraOSGListBucketsGetApi()
        assert resp.status_code == 200

    def test_api_infraOSGCreateBucket(self, config_obj, ViperopenapiApi):
        """  CreateBucket """
        bucket_info = None
        resp = ViperopenapiApi.infraOSGCreateBucketPutApi(bucket_info=bucket_info)
        assert resp.status_code == 200

    def test_api_infraOSGGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.infraOSGGetSystemInfoPostApi()
        assert resp.status_code == 200

    def test_api_infraOSGDeleteBucket(self, config_obj, ViperopenapiApi):
        """  DeleteBucket """
        bucket_name = None
        force = None
        resp = ViperopenapiApi.infraOSGDeleteBucketDeleteApi(bucket_name, force=force)
        assert resp.status_code == 200

    def test_api_infraOSGListObjects(self, config_obj, ViperopenapiApi):
        """  ListObjects """
        bucket_name = None
        date = None
        marker = None
        limit = None
        resp = ViperopenapiApi.infraOSGListObjectsGetApi(bucket_name, date=date, marker=marker, limit=limit)
        assert resp.status_code == 200

    def test_api_infraOSGUpdateBucket(self, config_obj, ViperopenapiApi):
        """  UpdateBucket """
        bucket_name = None
        encryption_method = None
        save_days = None
        resp = ViperopenapiApi.infraOSGUpdateBucketPutApi(bucket_name, encryption_method=encryption_method, save_days=save_days)
        assert resp.status_code == 200

    def test_api_infraOSGDeleteObjectsBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteObjectsBeforeDate """
        bucket_name = None
        date = None
        resp = ViperopenapiApi.infraOSGDeleteObjectsBeforeDatePostApi(bucket_name, date=date)
        assert resp.status_code == 200

    def test_api_infraOSGDeleteObjectsByDate(self, config_obj, ViperopenapiApi):
        """  DeleteObjectsByDate """
        bucket_name = None
        date = None
        resp = ViperopenapiApi.infraOSGDeleteObjectsByDatePostApi(bucket_name, date=date)
        assert resp.status_code == 200

    def test_api_infraOSGPutObject(self, config_obj, ViperopenapiApi):
        """  PutObject """
        bucket_name = None
        blob = None
        object_info = None
        resp = ViperopenapiApi.infraOSGPutObjectPostApi(bucket_name, blob=blob, object_info=object_info)
        assert resp.status_code == 200

    def test_api_infraOSGReserveObjectKeys(self, config_obj, ViperopenapiApi):
        """  ReserveObjectKeys """
        bucket_name = None
        object_count = None
        resp = ViperopenapiApi.infraOSGReserveObjectKeysPostApi(bucket_name, object_count=object_count)
        assert resp.status_code == 200

    def test_api_infraOSGScanObjects(self, config_obj, ViperopenapiApi):
        """  ScanObjects """
        bucket_name = None
        date = None
        limit = None
        marker = None
        resp = ViperopenapiApi.infraOSGScanObjectsPostApi(bucket_name, date=date, limit=limit, marker=marker)
        assert resp.status_code == 200

    def test_api_infraOSGDeleteObject(self, config_obj, ViperopenapiApi):
        """  DeleteObject """
        bucket_name = None
        object_key = None
        resp = ViperopenapiApi.infraOSGDeleteObjectDeleteApi(bucket_name, object_key)
        assert resp.status_code == 200

    def test_api_infraOSGGetObject(self, config_obj, ViperopenapiApi):
        """  GetObject """
        bucket_name = None
        object_key = None
        resp = ViperopenapiApi.infraOSGGetObjectGetApi(bucket_name, object_key)
        assert resp.status_code == 200

    def test_api_infraRaidExporterGetRaidInfo(self, config_obj, ViperopenapiApi):
        """  GetRaidInfo """
        resp = ViperopenapiApi.infraRaidExporterGetRaidInfoGetApi()
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrArtifactList(self, config_obj, ViperopenapiApi):
        """  ArtifactList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.infraSparkJobMgrArtifactListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrArtifactDownload(self, config_obj, ViperopenapiApi):
        """  ArtifactDownload """
        name = None
        resp = ViperopenapiApi.infraSparkJobMgrArtifactDownloadGetApi(name)
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrArtifactUpload(self, config_obj, ViperopenapiApi):
        """  ArtifactUpload """
        name = None
        resp = ViperopenapiApi.infraSparkJobMgrArtifactUploadPostApi(name)
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrArtifactDelete(self, config_obj, ViperopenapiApi):
        """  ArtifactDelete """
        name = None
        resp = ViperopenapiApi.infraSparkJobMgrArtifactDeleteDeleteApi(name)
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrArtifactGet(self, config_obj, ViperopenapiApi):
        """  ArtifactGet """
        name = None
        return_content = None
        resp = ViperopenapiApi.infraSparkJobMgrArtifactGetGetApi(name, return_content=return_content)
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrArtifactNew(self, config_obj, ViperopenapiApi):
        """  ArtifactNew """
        name = None
        allow_overwrite = None
        blob = None
        resp = ViperopenapiApi.infraSparkJobMgrArtifactNewPostApi(name, allow_overwrite=allow_overwrite, blob=blob)
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrJobList(self, config_obj, ViperopenapiApi):
        """  JobList """
        page_offset = None
        page_limit = None
        page_total = None
        catalog = None
        period_start = None
        period_end = None
        status = None
        resp = ViperopenapiApi.infraSparkJobMgrJobListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, catalog=catalog, period_start=period_start, period_end=period_end, status=status)
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrJobNew(self, config_obj, ViperopenapiApi):
        """  JobNew """
        job = None
        resp = ViperopenapiApi.infraSparkJobMgrJobNewPostApi(job=job)
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrJobDelete(self, config_obj, ViperopenapiApi):
        """  JobDelete """
        job_id = None
        resp = ViperopenapiApi.infraSparkJobMgrJobDeleteDeleteApi(job_id)
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrJobGet(self, config_obj, ViperopenapiApi):
        """  JobGet """
        job_id = None
        resp = ViperopenapiApi.infraSparkJobMgrJobGetGetApi(job_id)
        assert resp.status_code == 200

    def test_api_infraSparkJobMgrJobCancel(self, config_obj, ViperopenapiApi):
        """  JobCancel """
        job_id = None
        resp = ViperopenapiApi.infraSparkJobMgrJobCancelPostApi(job_id)
        assert resp.status_code == 200

    def test_api_infraStorageMgrNamespaceList(self, config_obj, ViperopenapiApi):
        """  NamespaceList """
        resp = ViperopenapiApi.infraStorageMgrNamespaceListGetApi()
        assert resp.status_code == 200

    def test_api_infraStorageMgrNamespaceDelete(self, config_obj, ViperopenapiApi):
        """  NamespaceDelete """
        ns_id = None
        resp = ViperopenapiApi.infraStorageMgrNamespaceDeleteDeleteApi(ns_id)
        assert resp.status_code == 200

    def test_api_infraStorageMgrNamespaceNew(self, config_obj, ViperopenapiApi):
        """  NamespaceNew """
        ns_id = None
        resp = ViperopenapiApi.infraStorageMgrNamespaceNewPostApi(ns_id)
        assert resp.status_code == 200

    def test_api_infraStorageMgrOSGStorageGet(self, config_obj, ViperopenapiApi):
        """  OSGStorageGet """
        resp = ViperopenapiApi.infraStorageMgrOSGStorageGetGetApi()
        assert resp.status_code == 200

    def test_api_infraStorageMgrOSGStorageReplace(self, config_obj, ViperopenapiApi):
        """  OSGStorageReplace """
        force = None
        mode = None
        nas_infos = None
        nas_overall_usage_in_gb_threshold = None
        resp = ViperopenapiApi.infraStorageMgrOSGStorageReplacePutApi(force=force, mode=mode, nas_infos=nas_infos, nas_overall_usage_in_gb_threshold=nas_overall_usage_in_gb_threshold)
        assert resp.status_code == 200

    def test_api_infraStorageMgrStorageProtectPolicyGet(self, config_obj, ViperopenapiApi):
        """  StorageProtectPolicyGet """
        resp = ViperopenapiApi.infraStorageMgrStorageProtectPolicyGetGetApi()
        assert resp.status_code == 200

    def test_api_infraStorageMgrStorageProtectPolicyReplace(self, config_obj, ViperopenapiApi):
        """  StorageProtectPolicyReplace """
        policy = None
        resp = ViperopenapiApi.infraStorageMgrStorageProtectPolicyReplacePutApi(policy=policy)
        assert resp.status_code == 200

    def test_api_infraStorageMgrStorageRuleList(self, config_obj, ViperopenapiApi):
        """  StorageRuleList """
        resp = ViperopenapiApi.infraStorageMgrStorageRuleListGetApi()
        assert resp.status_code == 200

    def test_api_infraStorageMgrStorageRuleReplace(self, config_obj, ViperopenapiApi):
        """  StorageRuleReplace """
        rule = None
        resp = ViperopenapiApi.infraStorageMgrStorageRuleReplacePutApi(rule=rule)
        assert resp.status_code == 200

    def test_api_algoStoreAppTemplateList(self, config_obj, ViperopenapiApi):
        """  AppTemplateList """
        resp = ViperopenapiApi.algoStoreAppTemplateListGetApi()
        assert resp.status_code == 200

    def test_api_algoStoreAppTemplateNew(self, config_obj, ViperopenapiApi):
        """  AppTemplateNew """
        template = None
        resp = ViperopenapiApi.algoStoreAppTemplateNewPostApi(template=template)
        assert resp.status_code == 200

    def test_api_algoStoreAppTemplateDelete(self, config_obj, ViperopenapiApi):
        """  AppTemplateDelete """
        template_id = None
        resp = ViperopenapiApi.algoStoreAppTemplateDeleteDeleteApi(template_id)
        assert resp.status_code == 200

    def test_api_algoStoreAppList(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.algoStoreAppListGetApi(filters_period_start=filters_period_start, filters_period_end=filters_period_end, filters_user_algo_name=filters_user_algo_name, filters_algo_types=filters_algo_types, filters_tag_ids=filters_tag_ids, filters_status=filters_status, filters_sale_type=filters_sale_type, page_offset=page_offset, page_limit=page_limit, page_total=page_total, reversed=reversed)
        assert resp.status_code == 200

    def test_api_algoStoreAppNewFromTemplate(self, config_obj, ViperopenapiApi):
        """  AppNewFromTemplate """
        meta = None
        models = None
        process_configs = None
        template_id = None
        resp = ViperopenapiApi.algoStoreAppNewFromTemplatePostApi(meta=meta, models=models, process_configs=process_configs, template_id=template_id)
        assert resp.status_code == 200

    def test_api_algoStoreAppUpload(self, config_obj, ViperopenapiApi):
        """  AppUpload """
        resp = ViperopenapiApi.algoStoreAppUploadPostApi()
        assert resp.status_code == 200

    def test_api_algoStoreAppDelete(self, config_obj, ViperopenapiApi):
        """  AppDelete """
        app_id = None
        resp = ViperopenapiApi.algoStoreAppDeleteDeleteApi(app_id)
        assert resp.status_code == 200

    def test_api_algoStoreAppGet(self, config_obj, ViperopenapiApi):
        """  AppGet """
        app_id = None
        resp = ViperopenapiApi.algoStoreAppGetGetApi(app_id)
        assert resp.status_code == 200

    def test_api_algoStoreAppUpdate(self, config_obj, ViperopenapiApi):
        """  AppUpdate """
        app_id = None
        tag_ids = None
        resp = ViperopenapiApi.algoStoreAppUpdatePatchApi(app_id, tag_ids=tag_ids)
        assert resp.status_code == 200

    def test_api_algoStoreAppInstanceNew(self, config_obj, ViperopenapiApi):
        """  AppInstanceNew """
        app_id = None
        user_configs = None
        resp = ViperopenapiApi.algoStoreAppInstanceNewPostApi(app_id, user_configs=user_configs)
        assert resp.status_code == 200

    def test_api_algoStoreAppInstanceDelete(self, config_obj, ViperopenapiApi):
        """  AppInstanceDelete """
        app_id = None
        instance_id = None
        resp = ViperopenapiApi.algoStoreAppInstanceDeleteDeleteApi(app_id, instance_id)
        assert resp.status_code == 200

    def test_api_algoStoreAppInstanceGet(self, config_obj, ViperopenapiApi):
        """  AppInstanceGet """
        app_id = None
        instance_id = None
        resp = ViperopenapiApi.algoStoreAppInstanceGetGetApi(app_id, instance_id)
        assert resp.status_code == 200

    def test_api_algoStoreAppInstanceUpdate(self, config_obj, ViperopenapiApi):
        """  AppInstanceUpdate """
        app_id = None
        instance_id = None
        hardware = None
        replicas = None
        resp = ViperopenapiApi.algoStoreAppInstanceUpdatePatchApi(app_id, instance_id, hardware=hardware, replicas=replicas)
        assert resp.status_code == 200

    def test_api_algoStoreAppGetByNameVersion(self, config_obj, ViperopenapiApi):
        """  AppGetByNameVersion """
        user_algo_name = None
        version = None
        resp = ViperopenapiApi.algoStoreAppGetByNameVersionGetApi(user_algo_name, version)
        assert resp.status_code == 200

    def test_api_algoStoreDocDownload(self, config_obj, ViperopenapiApi):
        """  DocDownload """
        user_algo_name = None
        version = None
        doc_name = None
        resp = ViperopenapiApi.algoStoreDocDownloadGetApi(user_algo_name, version, doc_name)
        assert resp.status_code == 200

    def test_api_algoStoreInstanceListByNameVersion(self, config_obj, ViperopenapiApi):
        """  InstanceListByNameVersion """
        user_algo_name = None
        version = None
        reversed = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.algoStoreInstanceListByNameVersionGetApi(user_algo_name, version, reversed=reversed, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_algoStoreEdgeInstanceList(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.algoStoreEdgeInstanceListGetApi(app_id=app_id, device_id=device_id, algo_types=algo_types, states=states, period_start=period_start, period_end=period_end, reversed=reversed, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_algoStoreEdgeInstanceNew(self, config_obj, ViperopenapiApi):
        """  EdgeInstanceNew """
        app_id = None
        device_id = None
        registry_id = None
        user_configs = None
        resp = ViperopenapiApi.algoStoreEdgeInstanceNewPostApi(app_id=app_id, device_id=device_id, registry_id=registry_id, user_configs=user_configs)
        assert resp.status_code == 200

    def test_api_algoStoreEdgeInstanceDelete(self, config_obj, ViperopenapiApi):
        """  EdgeInstanceDelete """
        instance_uuid = None
        resp = ViperopenapiApi.algoStoreEdgeInstanceDeleteDeleteApi(instance_uuid)
        assert resp.status_code == 200

    def test_api_algoStoreEdgeInstanceGet(self, config_obj, ViperopenapiApi):
        """  EdgeInstanceGet """
        instance_uuid = None
        resp = ViperopenapiApi.algoStoreEdgeInstanceGetGetApi(instance_uuid)
        assert resp.status_code == 200

    def test_api_algoStoreEdgeInstanceUpdate(self, config_obj, ViperopenapiApi):
        """  EdgeInstanceUpdate """
        instance_uuid = None
        user_configs = None
        resp = ViperopenapiApi.algoStoreEdgeInstanceUpdatePatchApi(instance_uuid, user_configs=user_configs)
        assert resp.status_code == 200

    def test_api_algoStoreGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.algoStoreGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_algoStoreInstanceList(self, config_obj, ViperopenapiApi):
        """  InstanceList """
        filters_algo_types = None
        filters_states = None
        filters_period_start = None
        filters_period_end = None
        reversed = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.algoStoreInstanceListGetApi(filters_algo_types=filters_algo_types, filters_states=filters_states, filters_period_start=filters_period_start, filters_period_end=filters_period_end, reversed=reversed, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_algoStoreReallocateResource(self, config_obj, ViperopenapiApi):
        """  ReallocateResource """
        group_resource_quotas = None
        ips_resource_quotas = None
        vps_resource_quotas = None
        resp = ViperopenapiApi.algoStoreReallocateResourcePostApi(group_resource_quotas=group_resource_quotas, ips_resource_quotas=ips_resource_quotas, vps_resource_quotas=vps_resource_quotas)
        assert resp.status_code == 200

    def test_api_algoStoreTagList(self, config_obj, ViperopenapiApi):
        """  TagList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.algoStoreTagListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_algoStoreTagNew(self, config_obj, ViperopenapiApi):
        """  TagNew """
        tag = None
        resp = ViperopenapiApi.algoStoreTagNewPostApi(tag=tag)
        assert resp.status_code == 200

    def test_api_algoStoreTagDelete(self, config_obj, ViperopenapiApi):
        """  TagDelete """
        tag_id = None
        resp = ViperopenapiApi.algoStoreTagDeleteDeleteApi(tag_id)
        assert resp.status_code == 200

    def test_api_searchWrapperBatchCompare(self, config_obj, ViperopenapiApi):
        """  BatchCompare """
        requests = None
        resp = ViperopenapiApi.searchWrapperBatchComparePostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_searchWrapperBatchCompareByImage(self, config_obj, ViperopenapiApi):
        """  BatchCompareByImage """
        requests = None
        resp = ViperopenapiApi.searchWrapperBatchCompareByImagePostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_apiWrapperBatchAddImageToDB(self, config_obj, ViperopenapiApi):
        """  BatchAddImageToDB """
        auto_rotation = None
        db_id = None
        extra_db_type = None
        images = None
        save_images = None
        type = None
        resp = ViperopenapiApi.apiWrapperBatchAddImageToDBPostApi(auto_rotation=auto_rotation, db_id=db_id, extra_db_type=extra_db_type, images=images, save_images=save_images, type=type)
        assert resp.status_code == 200

    def test_api_apiWrapperCompareImageInDB(self, config_obj, ViperopenapiApi):
        """  CompareImageInDB """
        db_id = None
        extra_db_type = None
        feature_id = None
        image = None
        key = None
        type = None
        resp = ViperopenapiApi.apiWrapperCompareImageInDBPostApi(db_id=db_id, extra_db_type=extra_db_type, feature_id=feature_id, image=image, key=key, type=type)
        assert resp.status_code == 200

    def test_api_apiWrapperCompareOneToOne(self, config_obj, ViperopenapiApi):
        """  CompareOneToOne """
        feature_version = None
        one = None
        other = None
        resp = ViperopenapiApi.apiWrapperCompareOneToOnePostApi(feature_version=feature_version, one=one, other=other)
        assert resp.status_code == 200

    def test_api_apiWrapperDeleteDB(self, config_obj, ViperopenapiApi):
        """  DeleteDB """
        db_id = None
        delete_bucket = None
        extra_db_type = None
        type = None
        resp = ViperopenapiApi.apiWrapperDeleteDBPostApi(db_id=db_id, delete_bucket=delete_bucket, extra_db_type=extra_db_type, type=type)
        assert resp.status_code == 200

    def test_api_apiWrapperDeleteImageFromDB(self, config_obj, ViperopenapiApi):
        """  DeleteImageFromDB """
        db_id = None
        delete_image = None
        extra_db_type = None
        feature_id = None
        key = None
        type = None
        resp = ViperopenapiApi.apiWrapperDeleteImageFromDBPostApi(db_id=db_id, delete_image=delete_image, extra_db_type=extra_db_type, feature_id=feature_id, key=key, type=type)
        assert resp.status_code == 200

    def test_api_apiWrapperDetectAndExtract(self, config_obj, ViperopenapiApi):
        """  DetectAndExtract """
        feature_version = None
        image = None
        resp = ViperopenapiApi.apiWrapperDetectAndExtractPostApi(feature_version=feature_version, image=image)
        assert resp.status_code == 200

    def test_api_apiWrapperGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.apiWrapperGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_apiWrapperNewDB(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.apiWrapperNewDBPostApi(bucket_encrypt=bucket_encrypt, bucket_flattened=bucket_flattened, create_bucket=create_bucket, db_size=db_size, description=description, enable_isolated_feature_table=enable_isolated_feature_table, extra_db_type=extra_db_type, feature_version=feature_version, name=name, type=type)
        assert resp.status_code == 200

    def test_api_apiWrapperSearchImageInDBs(self, config_obj, ViperopenapiApi):
        """  SearchImageInDBs """
        dbs = None
        dropped_fields = None
        extra_db_type = None
        image = None
        type = None
        resp = ViperopenapiApi.apiWrapperSearchImageInDBsPostApi(dbs=dbs, dropped_fields=dropped_fields, extra_db_type=extra_db_type, image=image, type=type)
        assert resp.status_code == 200

    def test_api_imageProcessWrapperBatchCompareFeature(self, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        requests = None
        resp = ViperopenapiApi.imageProcessWrapperBatchCompareFeaturePostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_imageProcessWrapperBatchDetect(self, config_obj, ViperopenapiApi):
        """  BatchDetect """
        requests = None
        resp = ViperopenapiApi.imageProcessWrapperBatchDetectPostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_imageProcessWrapperBatchDetectAndExtractAll(self, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll """
        requests = None
        resp = ViperopenapiApi.imageProcessWrapperBatchDetectAndExtractAllPostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_imageProcessWrapperBatchExtractWithLocation(self, config_obj, ViperopenapiApi):
        """  BatchExtractWithLocation """
        requests = None
        resp = ViperopenapiApi.imageProcessWrapperBatchExtractWithLocationPostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_searchWrapperSearch(self, config_obj, ViperopenapiApi):
        """  Search """
        common_config = None
        engine_configs = None
        filters = None
        search_mode = None
        resp = ViperopenapiApi.searchWrapperSearchPostApi(common_config=common_config, engine_configs=engine_configs, filters=filters, search_mode=search_mode)
        assert resp.status_code == 200

    def test_api_searchWrapperSearchByImage(self, config_obj, ViperopenapiApi):
        """  SearchByImage """
        boundings = None
        image = None
        search_request = None
        resp = ViperopenapiApi.searchWrapperSearchByImagePostApi(boundings=boundings, image=image, search_request=search_request)
        assert resp.status_code == 200

    def test_api_cameraManagerExportCameras(self, config_obj, ViperopenapiApi):
        """  ExportCameras """
        tags = None
        resp = ViperopenapiApi.cameraManagerExportCamerasPostApi(tags=tags)
        assert resp.status_code == 200

    def test_api_cameraManagerGB28181LocalConfigReplace(self, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigReplace """
        configRequest.local_uuid = None
        configRequest = None
        resp = ViperopenapiApi.cameraManagerGB28181LocalConfigReplacePutApi(configRequest.local_uuid, configRequest=configRequest)
        assert resp.status_code == 200

    def test_api_cameraManagerGB28181LocalConfigInfo(self, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigInfo """
        uuid = None
        resp = ViperopenapiApi.cameraManagerGB28181LocalConfigInfoGetApi(uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerGetCamerasByInternalID(self, config_obj, ViperopenapiApi):
        """  GetCamerasByInternalID """
        bypass_cache = None
        internal_ids = None
        resp = ViperopenapiApi.cameraManagerGetCamerasByInternalIDPostApi(bypass_cache=bypass_cache, internal_ids=internal_ids)
        assert resp.status_code == 200

    def test_api_cameraManagerImportCameras(self, config_obj, ViperopenapiApi):
        """  ImportCameras """
        cameras = None
        export_timestamp = None
        version = None
        zones = None
        resp = ViperopenapiApi.cameraManagerImportCamerasPostApi(cameras=cameras, export_timestamp=export_timestamp, version=version, zones=zones)
        assert resp.status_code == 200

    def test_api_cameraManagerNamespaceList(self, config_obj, ViperopenapiApi):
        """  NamespaceList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerNamespaceListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerNamespaceNew(self, config_obj, ViperopenapiApi):
        """  NamespaceNew """
        namespace_request.ns_id = None
        namespace_request = None
        resp = ViperopenapiApi.cameraManagerNamespaceNewPostApi(namespace_request.ns_id, namespace_request=namespace_request)
        assert resp.status_code == 200

    def test_api_cameraManagerNamespaceReplace(self, config_obj, ViperopenapiApi):
        """  NamespaceReplace """
        namespace_request.ns_id = None
        namespace_request = None
        resp = ViperopenapiApi.cameraManagerNamespaceReplacePutApi(namespace_request.ns_id, namespace_request=namespace_request)
        assert resp.status_code == 200

    def test_api_cameraManagerNamespaceDelete(self, config_obj, ViperopenapiApi):
        """  NamespaceDelete """
        ns_id = None
        resp = ViperopenapiApi.cameraManagerNamespaceDeleteDeleteApi(ns_id)
        assert resp.status_code == 200

    def test_api_cameraManagerNamespaceInfo(self, config_obj, ViperopenapiApi):
        """  NamespaceInfo """
        ns_id = None
        resp = ViperopenapiApi.cameraManagerNamespaceInfoGetApi(ns_id)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformList(self, config_obj, ViperopenapiApi):
        """  PlatformList """
        platform_type = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerPlatformListGetApi(platform_type=platform_type, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformNew(self, config_obj, ViperopenapiApi):
        """  PlatformNew """
        platform_config_request = None
        resp = ViperopenapiApi.cameraManagerPlatformNewPostApi(platform_config_request=platform_config_request)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformDelete(self, config_obj, ViperopenapiApi):
        """  PlatformDelete """
        platform_id = None
        resp = ViperopenapiApi.cameraManagerPlatformDeleteDeleteApi(platform_id)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformInfo(self, config_obj, ViperopenapiApi):
        """  PlatformInfo """
        platform_id = None
        resp = ViperopenapiApi.cameraManagerPlatformInfoGetApi(platform_id)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformReplace(self, config_obj, ViperopenapiApi):
        """  PlatformReplace """
        platform_id = None
        platform_config_request = None
        resp = ViperopenapiApi.cameraManagerPlatformReplacePutApi(platform_id, platform_config_request=platform_config_request)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformCameraList(self, config_obj, ViperopenapiApi):
        """  PlatformCameraList """
        platform_id = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerPlatformCameraListGetApi(platform_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerGetCamerasFromPlatform(self, config_obj, ViperopenapiApi):
        """  GetCamerasFromPlatform """
        platform_id = None
        device_id = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerGetCamerasFromPlatformGetApi(platform_id, device_id=device_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformCatalogItems(self, config_obj, ViperopenapiApi):
        """  PlatformCatalogItems """
        platform_id = None
        item_type = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerPlatformCatalogItemsGetApi(platform_id, item_type=item_type, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformCatalogSend(self, config_obj, ViperopenapiApi):
        """  PlatformCatalogSend """
        platform_id = None
        resp = ViperopenapiApi.cameraManagerPlatformCatalogSendPostApi(platform_id)
        assert resp.status_code == 200

    def test_api_cameraManagerBatchDeleteSharedDevices(self, config_obj, ViperopenapiApi):
        """  BatchDeleteSharedDevices """
        platform_id = None
        device_uuids = None
        resp = ViperopenapiApi.cameraManagerBatchDeleteSharedDevicesDeleteApi(platform_id, device_uuids=device_uuids)
        assert resp.status_code == 200

    def test_api_cameraManagerBatchAddSharedDevices(self, config_obj, ViperopenapiApi):
        """  BatchAddSharedDevices """
        platform_id = None
        device_uuids = None
        resp = ViperopenapiApi.cameraManagerBatchAddSharedDevicesPostApi(platform_id, device_uuids=device_uuids)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformSubscribeList(self, config_obj, ViperopenapiApi):
        """  PlatformSubscribeList """
        platform_id = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerPlatformSubscribeListGetApi(platform_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformSubscribeDelete(self, config_obj, ViperopenapiApi):
        """  PlatformSubscribeDelete """
        platform_id = None
        id = None
        resp = ViperopenapiApi.cameraManagerPlatformSubscribeDeleteDeleteApi(platform_id, id)
        assert resp.status_code == 200

    def test_api_cameraManagerPlatformSubscribeNew(self, config_obj, ViperopenapiApi):
        """  PlatformSubscribeNew """
        platform_subscribe_request.platform_id = None
        platform_subscribe_request = None
        resp = ViperopenapiApi.cameraManagerPlatformSubscribeNewPostApi(platform_subscribe_request.platform_id, platform_subscribe_request=platform_subscribe_request)
        assert resp.status_code == 200

    def test_api_cameraManagerSearchCameras(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.cameraManagerSearchCamerasPostApi(camera_uuid=camera_uuid, created_time_range=created_time_range, display_name=display_name, include_removed=include_removed, ingress_types=ingress_types, page=page, platform_id=platform_id, source_types=source_types, status=status, time_ascended=time_ascended, zone_uuid=zone_uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerSearchCamerasInBounding(self, config_obj, ViperopenapiApi):
        """  SearchCamerasInBounding """
        tags = None
        bounding = None
        page = None
        resp = ViperopenapiApi.cameraManagerSearchCamerasInBoundingPostApi(tags=tags, bounding=bounding, page=page)
        assert resp.status_code == 200

    def test_api_cameraManagerSearchNearestCameras(self, config_obj, ViperopenapiApi):
        """  SearchNearestCameras """
        tags = None
        distance = None
        geo_point = None
        nearest_k = None
        page = None
        resp = ViperopenapiApi.cameraManagerSearchNearestCamerasPostApi(tags=tags, distance=distance, geo_point=geo_point, nearest_k=nearest_k, page=page)
        assert resp.status_code == 200

    def test_api_cameraManagerSearchTasks(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.cameraManagerSearchTasksPostApi(camera_uuid=camera_uuid, created_time_range=created_time_range, id=id, ingress_types=ingress_types, object_types=object_types, page=page, status=status, time_ascended=time_ascended, zone_uuid=zone_uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerTagList(self, config_obj, ViperopenapiApi):
        """  TagList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerTagListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneList(self, config_obj, ViperopenapiApi):
        """  ZoneList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerZoneListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraNew(self, config_obj, ViperopenapiApi):
        """  ZoneCameraNew """
        camera_request.zone_uuid = None
        camera_request.uuid = None
        camera_request = None
        resp = ViperopenapiApi.cameraManagerZoneCameraNewPostApi(camera_request.zone_uuid, camera_request.uuid, camera_request=camera_request)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraReplace(self, config_obj, ViperopenapiApi):
        """  ZoneCameraReplace """
        camera_request.zone_uuid = None
        camera_request.uuid = None
        camera_request = None
        resp = ViperopenapiApi.cameraManagerZoneCameraReplacePutApi(camera_request.zone_uuid, camera_request.uuid, camera_request=camera_request)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneNew(self, config_obj, ViperopenapiApi):
        """  ZoneNew """
        zone_request.uuid = None
        zone_request = None
        resp = ViperopenapiApi.cameraManagerZoneNewPostApi(zone_request.uuid, zone_request=zone_request)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneReplace(self, config_obj, ViperopenapiApi):
        """  ZoneReplace """
        zone_request.uuid = None
        zone_request = None
        resp = ViperopenapiApi.cameraManagerZoneReplacePutApi(zone_request.uuid, zone_request=zone_request)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneDelete(self, config_obj, ViperopenapiApi):
        """  ZoneDelete """
        zone_uuid = None
        resp = ViperopenapiApi.cameraManagerZoneDeleteDeleteApi(zone_uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneInfo(self, config_obj, ViperopenapiApi):
        """  ZoneInfo """
        zone_uuid = None
        resp = ViperopenapiApi.cameraManagerZoneInfoGetApi(zone_uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraList(self, config_obj, ViperopenapiApi):
        """  ZoneCameraList """
        zone_uuid = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerZoneCameraListGetApi(zone_uuid, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraDelete(self, config_obj, ViperopenapiApi):
        """  ZoneCameraDelete """
        zone_uuid = None
        camera_uuid = None
        force = None
        resp = ViperopenapiApi.cameraManagerZoneCameraDeleteDeleteApi(zone_uuid, camera_uuid, force=force)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraInfo(self, config_obj, ViperopenapiApi):
        """  ZoneCameraInfo """
        zone_uuid = None
        camera_uuid = None
        resp = ViperopenapiApi.cameraManagerZoneCameraInfoGetApi(zone_uuid, camera_uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraActivate(self, config_obj, ViperopenapiApi):
        """  ZoneCameraActivate """
        zone_uuid = None
        camera_uuid = None
        resp = ViperopenapiApi.cameraManagerZoneCameraActivatePostApi(zone_uuid, camera_uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraFIControl(self, config_obj, ViperopenapiApi):
        """  ZoneCameraFIControl """
        zone_uuid = None
        camera_uuid = None
        fi_control_request = None
        resp = ViperopenapiApi.cameraManagerZoneCameraFIControlPutApi(zone_uuid, camera_uuid, fi_control_request=fi_control_request)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraGenerateRTMPAddress(self, config_obj, ViperopenapiApi):
        """  ZoneCameraGenerateRTMPAddress """
        zone_uuid = None
        camera_uuid = None
        resp = ViperopenapiApi.cameraManagerZoneCameraGenerateRTMPAddressPostApi(zone_uuid, camera_uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraGenerateRTSPAddress(self, config_obj, ViperopenapiApi):
        """  ZoneCameraGenerateRTSPAddress """
        zone_uuid = None
        camera_uuid = None
        command_type = None
        media_protocol_type = None
        playback_config = None
        resp = ViperopenapiApi.cameraManagerZoneCameraGenerateRTSPAddressPostApi(zone_uuid, camera_uuid, command_type=command_type, media_protocol_type=media_protocol_type, playback_config=playback_config)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraHomePositionSet(self, config_obj, ViperopenapiApi):
        """  ZoneCameraHomePositionSet """
        zone_uuid = None
        camera_uuid = None
        home_position_request = None
        resp = ViperopenapiApi.cameraManagerZoneCameraHomePositionSetPutApi(zone_uuid, camera_uuid, home_position_request=home_position_request)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraMultiTaskList(self, config_obj, ViperopenapiApi):
        """  ZoneCameraMultiTaskList """
        zone_uuid = None
        camera_uuid = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerZoneCameraMultiTaskListGetApi(zone_uuid, camera_uuid, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraMultiTaskNew(self, config_obj, ViperopenapiApi):
        """  ZoneCameraMultiTaskNew """
        zone_uuid = None
        camera_uuid = None
        default_task = None
        multi_tasks = None
        user_data = None
        uuid = None
        resp = ViperopenapiApi.cameraManagerZoneCameraMultiTaskNewPostApi(zone_uuid, camera_uuid, default_task=default_task, multi_tasks=multi_tasks, user_data=user_data, uuid=uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraMultiTaskDelete(self, config_obj, ViperopenapiApi):
        """  ZoneCameraMultiTaskDelete """
        zone_uuid = None
        camera_uuid = None
        uuid = None
        resp = ViperopenapiApi.cameraManagerZoneCameraMultiTaskDeleteDeleteApi(zone_uuid, camera_uuid, uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraMultiTaskInfo(self, config_obj, ViperopenapiApi):
        """  ZoneCameraMultiTaskInfo """
        zone_uuid = None
        camera_uuid = None
        uuid = None
        resp = ViperopenapiApi.cameraManagerZoneCameraMultiTaskInfoGetApi(zone_uuid, camera_uuid, uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraMultiTaskUpdate(self, config_obj, ViperopenapiApi):
        """  ZoneCameraMultiTaskUpdate """
        zone_uuid = None
        camera_uuid = None
        uuid = None
        multi_tasks = None
        resp = ViperopenapiApi.cameraManagerZoneCameraMultiTaskUpdatePutApi(zone_uuid, camera_uuid, uuid, multi_tasks=multi_tasks)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraPresetList(self, config_obj, ViperopenapiApi):
        """  ZoneCameraPresetList """
        zone_uuid = None
        camera_uuid = None
        resp = ViperopenapiApi.cameraManagerZoneCameraPresetListGetApi(zone_uuid, camera_uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraPresetSet(self, config_obj, ViperopenapiApi):
        """  ZoneCameraPresetSet """
        zone_uuid = None
        camera_uuid = None
        preset = None
        resp = ViperopenapiApi.cameraManagerZoneCameraPresetSetPutApi(zone_uuid, camera_uuid, preset=preset)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraPresetDelete(self, config_obj, ViperopenapiApi):
        """  ZoneCameraPresetDelete """
        zone_uuid = None
        camera_uuid = None
        preset_id = None
        resp = ViperopenapiApi.cameraManagerZoneCameraPresetDeleteDeleteApi(zone_uuid, camera_uuid, preset_id)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraPresetGoto(self, config_obj, ViperopenapiApi):
        """  ZoneCameraPresetGoto """
        zone_uuid = None
        camera_uuid = None
        preset_id = None
        resp = ViperopenapiApi.cameraManagerZoneCameraPresetGotoPutApi(zone_uuid, camera_uuid, preset_id)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraPTZControl(self, config_obj, ViperopenapiApi):
        """  ZoneCameraPTZControl """
        zone_uuid = None
        camera_uuid = None
        ptz_control_request = None
        resp = ViperopenapiApi.cameraManagerZoneCameraPTZControlPutApi(zone_uuid, camera_uuid, ptz_control_request=ptz_control_request)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraPTZControlTransparent(self, config_obj, ViperopenapiApi):
        """  ZoneCameraPTZControlTransparent """
        zone_uuid = None
        camera_uuid = None
        ptz_command = None
        resp = ViperopenapiApi.cameraManagerZoneCameraPTZControlTransparentPutApi(zone_uuid, camera_uuid, ptz_command=ptz_command)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraRecordInfo(self, config_obj, ViperopenapiApi):
        """  ZoneCameraRecordInfo """
        zone_uuid = None
        camera_uuid = None
        record_info_request = None
        resp = ViperopenapiApi.cameraManagerZoneCameraRecordInfoPostApi(zone_uuid, camera_uuid, record_info_request=record_info_request)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraTaskList(self, config_obj, ViperopenapiApi):
        """  ZoneCameraTaskList """
        zone_uuid = None
        camera_uuid = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.cameraManagerZoneCameraTaskListGetApi(zone_uuid, camera_uuid, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraTaskNew(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.cameraManagerZoneCameraTaskNewPostApi(zone_uuid, camera_uuid, extra_parameter=extra_parameter, feature_version=feature_version, object_type=object_type, playback_config=playback_config, storage_policy=storage_policy, symphony_device_task=symphony_device_task, task_object_config=task_object_config, user_data=user_data, uuid=uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraTaskDelete(self, config_obj, ViperopenapiApi):
        """  ZoneCameraTaskDelete """
        zone_uuid = None
        camera_uuid = None
        id = None
        resp = ViperopenapiApi.cameraManagerZoneCameraTaskDeleteDeleteApi(zone_uuid, camera_uuid, id)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraTaskUpdate(self, config_obj, ViperopenapiApi):
        """  ZoneCameraTaskUpdate """
        zone_uuid = None
        camera_uuid = None
        id = None
        task_object_config = None
        resp = ViperopenapiApi.cameraManagerZoneCameraTaskUpdatePutApi(zone_uuid, camera_uuid, id, task_object_config=task_object_config)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraTaskGenerateRTSPAddress(self, config_obj, ViperopenapiApi):
        """  ZoneCameraTaskGenerateRTSPAddress """
        zone_uuid = None
        camera_uuid = None
        id = None
        resp = ViperopenapiApi.cameraManagerZoneCameraTaskGenerateRTSPAddressPostApi(zone_uuid, camera_uuid, id)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraTeleBoot(self, config_obj, ViperopenapiApi):
        """  ZoneCameraTeleBoot """
        zone_uuid = None
        camera_uuid = None
        resp = ViperopenapiApi.cameraManagerZoneCameraTeleBootPutApi(zone_uuid, camera_uuid)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraVideoCapture(self, config_obj, ViperopenapiApi):
        """  ZoneCameraVideoCapture """
        zone_uuid = None
        camera_uuid = None
        command_type = None
        media_protocol_type = None
        playback_config = None
        resp = ViperopenapiApi.cameraManagerZoneCameraVideoCapturePostApi(zone_uuid, camera_uuid, command_type=command_type, media_protocol_type=media_protocol_type, playback_config=playback_config)
        assert resp.status_code == 200

    def test_api_cameraManagerZoneCameraVideoParameter(self, config_obj, ViperopenapiApi):
        """  ZoneCameraVideoParameter """
        zone_uuid = None
        camera_uuid = None
        media_protocol_type = None
        resp = ViperopenapiApi.cameraManagerZoneCameraVideoParameterGetApi(zone_uuid, camera_uuid, media_protocol_type=media_protocol_type)
        assert resp.status_code == 200

    def test_api_entityDBAddOutsideOplogAsync(self, config_obj, ViperopenapiApi):
        """  AddOutsideOplogAsync """
        oplogs = None
        resp = ViperopenapiApi.entityDBAddOutsideOplogAsyncPostApi(oplogs=oplogs)
        assert resp.status_code == 200

    def test_api_entityDBBatchUpdateEntityCluster(self, config_obj, ViperopenapiApi):
        """  BatchUpdateEntityCluster """
        cluster_update_items = None
        resp = ViperopenapiApi.entityDBBatchUpdateEntityClusterPostApi(cluster_update_items=cluster_update_items)
        assert resp.status_code == 200

    def test_api_entityDBDeleteEventsDataBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteEventsDataBeforeDate """
        date = None
        resp = ViperopenapiApi.entityDBDeleteEventsDataBeforeDatePostApi(date=date)
        assert resp.status_code == 200

    def test_api_entityDBDeleteHumanVehicleTracksBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteHumanVehicleTracksBeforeDate """
        date = None
        resp = ViperopenapiApi.entityDBDeleteHumanVehicleTracksBeforeDatePostApi(date=date)
        assert resp.status_code == 200

    def test_api_entityDBDeleteTracksBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteTracksBeforeDate """
        date = None
        resp = ViperopenapiApi.entityDBDeleteTracksBeforeDatePostApi(date=date)
        assert resp.status_code == 200

    def test_api_entityDBDeleteVehicleTracksBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteVehicleTracksBeforeDate """
        date = None
        resp = ViperopenapiApi.entityDBDeleteVehicleTracksBeforeDatePostApi(date=date)
        assert resp.status_code == 200

    def test_api_entityDBEntityList(self, config_obj, ViperopenapiApi):
        """  EntityList """
        marker = None
        order_field = None
        page_size = None
        period = None
        reversed = None
        types = None
        resp = ViperopenapiApi.entityDBEntityListPostApi(marker=marker, order_field=order_field, page_size=page_size, period=period, reversed=reversed, types=types)
        assert resp.status_code == 200

    def test_api_entityDBBatchDeleteEntities(self, config_obj, ViperopenapiApi):
        """  BatchDeleteEntities """
        entity_ids = None
        resp = ViperopenapiApi.entityDBBatchDeleteEntitiesPostApi(entity_ids=entity_ids)
        assert resp.status_code == 200

    def test_api_entityDBEntityBatchGet(self, config_obj, ViperopenapiApi):
        """  EntityBatchGet """
        entity_ids = None
        resp = ViperopenapiApi.entityDBEntityBatchGetPostApi(entity_ids=entity_ids)
        assert resp.status_code == 200

    def test_api_entityDBEntitySearch(self, config_obj, ViperopenapiApi):
        """  EntitySearch """
        camera_ids = None
        feature = None
        min_score = None
        period = None
        top_k = None
        resp = ViperopenapiApi.entityDBEntitySearchPostApi(camera_ids=camera_ids, feature=feature, min_score=min_score, period=period, top_k=top_k)
        assert resp.status_code == 200

    def test_api_entityDBTrackListByEntity(self, config_obj, ViperopenapiApi):
        """  TrackListByEntity """
        entity_id.entity_type = None
        entity_id.id = None
        entity_id = None
        marker = None
        page_size = None
        period = None
        reversed = None
        resp = ViperopenapiApi.entityDBTrackListByEntityPostApi(entity_id.entity_type, entity_id.id, entity_id=entity_id, marker=marker, page_size=page_size, period=period, reversed=reversed)
        assert resp.status_code == 200

    def test_api_entityDBEntitiesByTimeSpace(self, config_obj, ViperopenapiApi):
        """  EntitiesByTimeSpace """
        camera_ids = None
        paging = None
        period = None
        reversed = None
        types = None
        resp = ViperopenapiApi.entityDBEntitiesByTimeSpacePostApi(camera_ids=camera_ids, paging=paging, period=period, reversed=reversed, types=types)
        assert resp.status_code == 200

    def test_api_entityDBGenerateCentroid(self, config_obj, ViperopenapiApi):
        """  GenerateCentroid """
        features = None
        resp = ViperopenapiApi.entityDBGenerateCentroidPostApi(features=features)
        assert resp.status_code == 200

    def test_api_entityDBBatchDeleteTracks(self, config_obj, ViperopenapiApi):
        """  BatchDeleteTracks """
        is_async = None
        track_delete_items = None
        resp = ViperopenapiApi.entityDBBatchDeleteTracksPostApi(is_async=is_async, track_delete_items=track_delete_items)
        assert resp.status_code == 200

    def test_api_entityDBTrackBatchGet(self, config_obj, ViperopenapiApi):
        """  TrackBatchGet """
        track_ids = None
        resp = ViperopenapiApi.entityDBTrackBatchGetPostApi(track_ids=track_ids)
        assert resp.status_code == 200

    def test_api_entityDBTracksByEntitySortedBySimilarity(self, config_obj, ViperopenapiApi):
        """  TracksByEntitySortedBySimilarity """
        camera_ids = None
        entity_id = None
        feature = None
        period = None
        top_k = None
        resp = ViperopenapiApi.entityDBTracksByEntitySortedBySimilarityPostApi(camera_ids=camera_ids, entity_id=entity_id, feature=feature, period=period, top_k=top_k)
        assert resp.status_code == 200

    def test_api_entityDBEntityListV2(self, config_obj, ViperopenapiApi):
        """  EntityListV2 """
        paging = None
        period = None
        reversed = None
        types = None
        resp = ViperopenapiApi.entityDBEntityListV2PostApi(paging=paging, period=period, reversed=reversed, types=types)
        assert resp.status_code == 200

    def test_api_entityDBTrackListByEntityV2(self, config_obj, ViperopenapiApi):
        """  TrackListByEntityV2 """
        entity_id.id = None
        camera_ids = None
        entity_id = None
        paging = None
        period = None
        reversed = None
        resp = ViperopenapiApi.entityDBTrackListByEntityV2PostApi(entity_id.id, camera_ids=camera_ids, entity_id=entity_id, paging=paging, period=period, reversed=reversed)
        assert resp.status_code == 200

    def test_api_featureConvertBatchConvertFeature(self, config_obj, ViperopenapiApi):
        """  BatchConvertFeature """
        features = None
        source_system = None
        target_systems = None
        target_version = None
        resp = ViperopenapiApi.featureConvertBatchConvertFeaturePostApi(features=features, source_system=source_system, target_systems=target_systems, target_version=target_version)
        assert resp.status_code == 200

    def test_api_imageEgressObjectDownload(self, config_obj, ViperopenapiApi):
        """  ObjectDownload """
        platform_id = None
        object_id = None
        resp = ViperopenapiApi.imageEgressObjectDownloadGetApi(platform_id, object_id)
        assert resp.status_code == 200

    def test_api_imageEgressManagerVIIDList(self, config_obj, ViperopenapiApi):
        """  VIIDList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.imageEgressManagerVIIDListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_imageEgressManagerVIIDDelete(self, config_obj, ViperopenapiApi):
        """  VIIDDelete """
        viid_id = None
        resp = ViperopenapiApi.imageEgressManagerVIIDDeleteDeleteApi(viid_id)
        assert resp.status_code == 200

    def test_api_imageEgressManagerVIIDInfo(self, config_obj, ViperopenapiApi):
        """  VIIDInfo """
        viid_id = None
        resp = ViperopenapiApi.imageEgressManagerVIIDInfoGetApi(viid_id)
        assert resp.status_code == 200

    def test_api_imageEgressManagerVIIDAPEList(self, config_obj, ViperopenapiApi):
        """  VIIDAPEList """
        viid_id = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.imageEgressManagerVIIDAPEListGetApi(viid_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_imageEgressManagerBatchAddVIIDAPE(self, config_obj, ViperopenapiApi):
        """  BatchAddVIIDAPE """
        viid_id = None
        ape_infos = None
        resp = ViperopenapiApi.imageEgressManagerBatchAddVIIDAPEPostApi(viid_id, ape_infos=ape_infos)
        assert resp.status_code == 200

    def test_api_imageEgressManagerBatchDelVIIDAPE(self, config_obj, ViperopenapiApi):
        """  BatchDelVIIDAPE """
        viid_id = None
        ape_uuids = None
        resp = ViperopenapiApi.imageEgressManagerBatchDelVIIDAPEPostApi(viid_id, ape_uuids=ape_uuids)
        assert resp.status_code == 200

    def test_api_imageEgressManagerVIIDSubscriptionList(self, config_obj, ViperopenapiApi):
        """  VIIDSubscriptionList """
        viid_id = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.imageEgressManagerVIIDSubscriptionListGetApi(viid_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_imageEgressManagerVIIDNew(self, config_obj, ViperopenapiApi):
        """  VIIDNew """
        viid_request.viid_id = None
        viid_request = None
        resp = ViperopenapiApi.imageEgressManagerVIIDNewPostApi(viid_request.viid_id, viid_request=viid_request)
        assert resp.status_code == 200

    def test_api_imageEgressBatchPutObject(self, config_obj, ViperopenapiApi):
        """  BatchPutObject """
        requests = None
        resp = ViperopenapiApi.imageEgressBatchPutObjectPostApi(requests=requests)
        assert resp.status_code == 200

    def test_api_imageEgressObjectPut(self, config_obj, ViperopenapiApi):
        """  ObjectPut """
        platform_id = None
        object_info = None
        resp = ViperopenapiApi.imageEgressObjectPutPostApi(platform_id, object_info=object_info)
        assert resp.status_code == 200

    def test_api_imageEgressObjectGet(self, config_obj, ViperopenapiApi):
        """  ObjectGet """
        platform_id = None
        object_id = None
        resp = ViperopenapiApi.imageEgressObjectGetGetApi(platform_id, object_id)
        assert resp.status_code == 200

    def test_api_imageIngressGAT1400SubscribeDelete(self, config_obj, ViperopenapiApi):
        """  GAT1400SubscribeDelete """
        task_id = None
        subscribe_id = None
        resp = ViperopenapiApi.imageIngressGAT1400SubscribeDeleteDeleteApi(task_id=task_id, subscribe_id=subscribe_id)
        assert resp.status_code == 200

    def test_api_imageIngressGAT1400SubscribeNew(self, config_obj, ViperopenapiApi):
        """  GAT1400SubscribeNew """
        parameter = None
        task_id = None
        resp = ViperopenapiApi.imageIngressGAT1400SubscribeNewPostApi(parameter=parameter, task_id=task_id)
        assert resp.status_code == 200

    def test_api_imageIngressGetCamerasFromPlatform(self, config_obj, ViperopenapiApi):
        """  GetCamerasFromPlatform """
        task_id = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.imageIngressGetCamerasFromPlatformGetApi(task_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_imageIngressTaskList(self, config_obj, ViperopenapiApi):
        """  TaskList """
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        is_passive = None
        resp = ViperopenapiApi.imageIngressTaskListGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total, is_passive=is_passive)
        assert resp.status_code == 200

    def test_api_imageIngressTaskNew(self, config_obj, ViperopenapiApi):
        """  TaskNew """
        task_request = None
        resp = ViperopenapiApi.imageIngressTaskNewPostApi(task_request=task_request)
        assert resp.status_code == 200

    def test_api_imageIngressTaskDelete(self, config_obj, ViperopenapiApi):
        """  TaskDelete """
        task_id = None
        resp = ViperopenapiApi.imageIngressTaskDeleteDeleteApi(task_id)
        assert resp.status_code == 200

    def test_api_imageIngressTaskStatus(self, config_obj, ViperopenapiApi):
        """  TaskStatus """
        task_id = None
        resp = ViperopenapiApi.imageIngressTaskStatusGetApi(task_id)
        assert resp.status_code == 200

    def test_api_imageFpachExtractBatchCompareFeature(self, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFpachExtractBatchCompareFeaturePostApi(face_feature_version, pedestrian_feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFpachExtractBatchDetect(self, config_obj, ViperopenapiApi):
        """  BatchDetect """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFpachExtractBatchDetectPostApi(face_feature_version, pedestrian_feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFpachExtractBatchDetectAndExtractAll(self, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFpachExtractBatchDetectAndExtractAllPostApi(face_feature_version, pedestrian_feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFpachExtractBatchExtractWithLocation(self, config_obj, ViperopenapiApi):
        """  BatchExtractWithLocation """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFpachExtractBatchExtractWithLocationPostApi(face_feature_version, pedestrian_feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFpachExtractGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        face_feature_version = None
        pedestrian_feature_version = None
        resp = ViperopenapiApi.imageFpachExtractGetSystemInfoGetApi(face_feature_version, pedestrian_feature_version)
        assert resp.status_code == 200

    def test_api_imageFaceExtractBatchCompareFeature(self, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFaceExtractBatchCompareFeaturePostApi(feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceExtractBatchDetect(self, config_obj, ViperopenapiApi):
        """  BatchDetect """
        feature_version = None
        detect_mode = None
        face_type = None
        requests = None
        resp = ViperopenapiApi.imageFaceExtractBatchDetectPostApi(feature_version, detect_mode=detect_mode, face_type=face_type, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceExtractBatchDetectAndExtract(self, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtract """
        feature_version = None
        detect_mode = None
        face_type = None
        requests = None
        resp = ViperopenapiApi.imageFaceExtractBatchDetectAndExtractPostApi(feature_version, detect_mode=detect_mode, face_type=face_type, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceExtractBatchDetectAndExtractAll2(self, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll2 """
        feature_version = None
        detect_mode = None
        face_type = None
        requests = None
        resp = ViperopenapiApi.imageFaceExtractBatchDetectAndExtractAll2PostApi(feature_version, detect_mode=detect_mode, face_type=face_type, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceExtractBatchDetectAndExtractMultiModel(self, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractMultiModel """
        feature_version = None
        detect_mode = None
        face_type = None
        requests = None
        resp = ViperopenapiApi.imageFaceExtractBatchDetectAndExtractMultiModelPostApi(feature_version, detect_mode=detect_mode, face_type=face_type, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceExtractBatchDetectAndExtractAll(self, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll """
        feature_version = None
        detect_mode = None
        face_type = None
        requests = None
        resp = ViperopenapiApi.imageFaceExtractBatchDetectAndExtractAllPostApi(feature_version, detect_mode=detect_mode, face_type=face_type, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceExtractBatchExtractWithBounding(self, config_obj, ViperopenapiApi):
        """  BatchExtractWithBounding """
        feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFaceExtractBatchExtractWithBoundingPostApi(feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceExtractBatchExtractWithPoints(self, config_obj, ViperopenapiApi):
        """  BatchExtractWithPoints """
        feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFaceExtractBatchExtractWithPointsPostApi(feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceExtractCompareFeature(self, config_obj, ViperopenapiApi):
        """  CompareFeature """
        feature_version = None
        one = None
        other = None
        resp = ViperopenapiApi.imageFaceExtractCompareFeaturePostApi(feature_version, one=one, other=other)
        assert resp.status_code == 200

    def test_api_imageFaceExtractGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        feature_version = None
        resp = ViperopenapiApi.imageFaceExtractGetSystemInfoGetApi(feature_version)
        assert resp.status_code == 200

    def test_api_imageFacepedExtratBatchCompareFeature(self, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFacepedExtratBatchCompareFeaturePostApi(face_feature_version, pedestrian_feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFacepedExtratBatchDetect(self, config_obj, ViperopenapiApi):
        """  BatchDetect """
        face_feature_version = None
        pedestrian_feature_version = None
        mode = None
        requests = None
        resp = ViperopenapiApi.imageFacepedExtratBatchDetectPostApi(face_feature_version, pedestrian_feature_version, mode=mode, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFacepedExtratBatchDetectAndExtract(self, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtract """
        face_feature_version = None
        pedestrian_feature_version = None
        mode = None
        requests = None
        resp = ViperopenapiApi.imageFacepedExtratBatchDetectAndExtractPostApi(face_feature_version, pedestrian_feature_version, mode=mode, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFacepedExtratBatchDetectAndExtractAll(self, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll """
        face_feature_version = None
        pedestrian_feature_version = None
        mode = None
        requests = None
        resp = ViperopenapiApi.imageFacepedExtratBatchDetectAndExtractAllPostApi(face_feature_version, pedestrian_feature_version, mode=mode, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFacepedExtratBatchExtractWithLocation(self, config_obj, ViperopenapiApi):
        """  BatchExtractWithLocation """
        face_feature_version = None
        pedestrian_feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFacepedExtratBatchExtractWithLocationPostApi(face_feature_version, pedestrian_feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFacepedExtratGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        face_feature_version = None
        pedestrian_feature_version = None
        resp = ViperopenapiApi.imageFacepedExtratGetSystemInfoGetApi(face_feature_version, pedestrian_feature_version)
        assert resp.status_code == 200

    def test_api_imageFaceVehicleExtractBatchCompareFeature(self, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFaceVehicleExtractBatchCompareFeaturePostApi(feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceVehicleExtractBatchDetect(self, config_obj, ViperopenapiApi):
        """  BatchDetect """
        feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFaceVehicleExtractBatchDetectPostApi(feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceVehicleExtractBatchDetectAndExtractAll(self, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtractAll """
        feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFaceVehicleExtractBatchDetectAndExtractAllPostApi(feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceVehicleExtractBatchExtractWithLocation(self, config_obj, ViperopenapiApi):
        """  BatchExtractWithLocation """
        feature_version = None
        requests = None
        resp = ViperopenapiApi.imageFaceVehicleExtractBatchExtractWithLocationPostApi(feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageFaceVehicleExtractGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        feature_version = None
        resp = ViperopenapiApi.imageFaceVehicleExtractGetSystemInfoGetApi(feature_version)
        assert resp.status_code == 200

    def test_api_imageStructExtractBatchCompareFeature(self, config_obj, ViperopenapiApi):
        """  BatchCompareFeature """
        feature_version = None
        requests = None
        resp = ViperopenapiApi.imageStructExtractBatchCompareFeaturePostApi(feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageStructExtractBatchDetect(self, config_obj, ViperopenapiApi):
        """  BatchDetect """
        feature_version = None
        mode = None
        requests = None
        resp = ViperopenapiApi.imageStructExtractBatchDetectPostApi(feature_version, mode=mode, requests=requests)
        assert resp.status_code == 200

    def test_api_imageStructExtractBatchDetectAndExtract(self, config_obj, ViperopenapiApi):
        """  BatchDetectAndExtract """
        feature_version = None
        mode = None
        requests = None
        resp = ViperopenapiApi.imageStructExtractBatchDetectAndExtractPostApi(feature_version, mode=mode, requests=requests)
        assert resp.status_code == 200

    def test_api_imageStructExtractBatchExtractWithBounding(self, config_obj, ViperopenapiApi):
        """  BatchExtractWithBounding """
        feature_version = None
        requests = None
        resp = ViperopenapiApi.imageStructExtractBatchExtractWithBoundingPostApi(feature_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageStructExtractGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        feature_version = None
        resp = ViperopenapiApi.imageStructExtractGetSystemInfoGetApi(feature_version)
        assert resp.status_code == 200

    def test_api_imageOCRExtractBatchCustomTemplate(self, config_obj, ViperopenapiApi):
        """  BatchCustomTemplate """
        images = None
        template_data = None
        type = None
        resp = ViperopenapiApi.imageOCRExtractBatchCustomTemplatePostApi(images=images, template_data=template_data, type=type)
        assert resp.status_code == 200

    def test_api_imageOCRExtractBatchPlainText(self, config_obj, ViperopenapiApi):
        """  BatchPlainText """
        images = None
        region_type = None
        type = None
        resp = ViperopenapiApi.imageOCRExtractBatchPlainTextPostApi(images=images, region_type=region_type, type=type)
        assert resp.status_code == 200

    def test_api_imageOCRExtractBatchSpecialTemplate(self, config_obj, ViperopenapiApi):
        """  BatchSpecialTemplate """
        images = None
        template_db_ids = None
        type = None
        resp = ViperopenapiApi.imageOCRExtractBatchSpecialTemplatePostApi(images=images, template_db_ids=template_db_ids, type=type)
        assert resp.status_code == 200

    def test_api_imageOCRExtractBatchTemplate(self, config_obj, ViperopenapiApi):
        """  BatchTemplate """
        images = None
        region_type = None
        type = None
        resp = ViperopenapiApi.imageOCRExtractBatchTemplatePostApi(images=images, region_type=region_type, type=type)
        assert resp.status_code == 200

    def test_api_imageOCRExtractGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.imageOCRExtractGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_imageAlgoProcessBatchProcess(self, config_obj, ViperopenapiApi):
        """  BatchProcess """
        app_id = None
        app_version = None
        requests = None
        resp = ViperopenapiApi.imageAlgoProcessBatchProcessPostApi(app_id, app_version, requests=requests)
        assert resp.status_code == 200

    def test_api_imageAlgoProcessGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        app_id = None
        app_version = None
        resp = ViperopenapiApi.imageAlgoProcessGetSystemInfoGetApi(app_id, app_version)
        assert resp.status_code == 200

    def test_api_ocrApiWrapperBatchOCRCustomTemplate(self, config_obj, ViperopenapiApi):
        """  BatchOCRCustomTemplate """
        images = None
        template_data = None
        type = None
        resp = ViperopenapiApi.ocrApiWrapperBatchOCRCustomTemplatePostApi(images=images, template_data=template_data, type=type)
        assert resp.status_code == 200

    def test_api_ocrApiWrapperBatchOCRPlainText(self, config_obj, ViperopenapiApi):
        """  BatchOCRPlainText """
        images = None
        region_type = None
        type = None
        resp = ViperopenapiApi.ocrApiWrapperBatchOCRPlainTextPostApi(images=images, region_type=region_type, type=type)
        assert resp.status_code == 200

    def test_api_ocrApiWrapperBatchOCRSpecialTemplate(self, config_obj, ViperopenapiApi):
        """  BatchOCRSpecialTemplate """
        images = None
        template_db_ids = None
        type = None
        resp = ViperopenapiApi.ocrApiWrapperBatchOCRSpecialTemplatePostApi(images=images, template_db_ids=template_db_ids, type=type)
        assert resp.status_code == 200

    def test_api_ocrApiWrapperBatchOCRTemplate(self, config_obj, ViperopenapiApi):
        """  BatchOCRTemplate """
        images = None
        region_type = None
        type = None
        resp = ViperopenapiApi.ocrApiWrapperBatchOCRTemplatePostApi(images=images, region_type=region_type, type=type)
        assert resp.status_code == 200

    def test_api_ocrApiWrapperOCRCustomTemplate(self, config_obj, ViperopenapiApi):
        """  OCRCustomTemplate """
        image = None
        template_data = None
        type = None
        resp = ViperopenapiApi.ocrApiWrapperOCRCustomTemplatePostApi(image=image, template_data=template_data, type=type)
        assert resp.status_code == 200

    def test_api_ocrApiWrapperOCRPlainText(self, config_obj, ViperopenapiApi):
        """  OCRPlainText """
        image = None
        region_type = None
        type = None
        resp = ViperopenapiApi.ocrApiWrapperOCRPlainTextPostApi(image=image, region_type=region_type, type=type)
        assert resp.status_code == 200

    def test_api_ocrApiWrapperOCRSpecialTemplate(self, config_obj, ViperopenapiApi):
        """  OCRSpecialTemplate """
        image = None
        template_db_ids = None
        type = None
        resp = ViperopenapiApi.ocrApiWrapperOCRSpecialTemplatePostApi(image=image, template_db_ids=template_db_ids, type=type)
        assert resp.status_code == 200

    def test_api_ocrApiWrapperOCRTemplate(self, config_obj, ViperopenapiApi):
        """  OCRTemplate """
        image = None
        region_type = None
        type = None
        resp = ViperopenapiApi.ocrApiWrapperOCRTemplatePostApi(image=image, region_type=region_type, type=type)
        assert resp.status_code == 200

    def test_api_kafkaCallbackGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.kafkaCallbackGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_kafkaCallbackSetCallbackURL(self, config_obj, ViperopenapiApi):
        """  SetCallbackURL """
        transport_config = None
        url = None
        resp = ViperopenapiApi.kafkaCallbackSetCallbackURLPostApi(transport_config=transport_config, url=url)
        assert resp.status_code == 200

    def test_api_protocolIngressBatchDeleteDevice(self, config_obj, ViperopenapiApi):
        """  BatchDeleteDevice """
        device_uuids = None
        resp = ViperopenapiApi.protocolIngressBatchDeleteDevicePostApi(device_uuids=device_uuids)
        assert resp.status_code == 200

    def test_api_protocolIngressBatchNewDevice(self, config_obj, ViperopenapiApi):
        """  BatchNewDevice """
        devices = None
        resp = ViperopenapiApi.protocolIngressBatchNewDevicePostApi(devices=devices)
        assert resp.status_code == 200

    def test_api_protocolIngressDeviceNew(self, config_obj, ViperopenapiApi):
        """  DeviceNew """
        device.device_uuid = None
        device = None
        resp = ViperopenapiApi.protocolIngressDeviceNewPostApi(device.device_uuid, device=device)
        assert resp.status_code == 200

    def test_api_protocolIngressDeviceReplace(self, config_obj, ViperopenapiApi):
        """  DeviceReplace """
        device.device_uuid = None
        device = None
        resp = ViperopenapiApi.protocolIngressDeviceReplacePutApi(device.device_uuid, device=device)
        assert resp.status_code == 200

    def test_api_protocolIngressDeviceDelete(self, config_obj, ViperopenapiApi):
        """  DeviceDelete """
        device_uuid = None
        resp = ViperopenapiApi.protocolIngressDeviceDeleteDeleteApi(device_uuid)
        assert resp.status_code == 200

    def test_api_protocolIngressDeviceInfo(self, config_obj, ViperopenapiApi):
        """  DeviceInfo """
        device_uuid = None
        resp = ViperopenapiApi.protocolIngressDeviceInfoGetApi(device_uuid)
        assert resp.status_code == 200

    def test_api_protocolIngressAbsolutePTZMove(self, config_obj, ViperopenapiApi):
        """  AbsolutePTZMove """
        device_uuid = None
        position = None
        resp = ViperopenapiApi.protocolIngressAbsolutePTZMovePutApi(device_uuid, position=position)
        assert resp.status_code == 200

    def test_api_protocolIngressAbsolutePTZPosition(self, config_obj, ViperopenapiApi):
        """  AbsolutePTZPosition """
        device_uuid = None
        resp = ViperopenapiApi.protocolIngressAbsolutePTZPositionGetApi(device_uuid)
        assert resp.status_code == 200

    def test_api_protocolIngressDeviceCatalogList(self, config_obj, ViperopenapiApi):
        """  DeviceCatalogList """
        device_uuid = None
        page_offset = None
        page_limit = None
        page_total = None
        item_type = None
        resp = ViperopenapiApi.protocolIngressDeviceCatalogListGetApi(device_uuid, page_offset=page_offset, page_limit=page_limit, page_total=page_total, item_type=item_type)
        assert resp.status_code == 200

    def test_api_protocolIngressDeviceCatalogSend(self, config_obj, ViperopenapiApi):
        """  DeviceCatalogSend """
        device_uuid = None
        resp = ViperopenapiApi.protocolIngressDeviceCatalogSendPutApi(device_uuid)
        assert resp.status_code == 200

    def test_api_protocolIngressFIControl(self, config_obj, ViperopenapiApi):
        """  FIControl """
        device_uuid = None
        focus = None
        iris = None
        stop_enable = None
        resp = ViperopenapiApi.protocolIngressFIControlPutApi(device_uuid, focus=focus, iris=iris, stop_enable=stop_enable)
        assert resp.status_code == 200

    def test_api_protocolIngressDeviceMediaInfo(self, config_obj, ViperopenapiApi):
        """  DeviceMediaInfo """
        device_uuid = None
        stream_type = None
        resp = ViperopenapiApi.protocolIngressDeviceMediaInfoGetApi(device_uuid, stream_type=stream_type)
        assert resp.status_code == 200

    def test_api_protocolIngressPresetList(self, config_obj, ViperopenapiApi):
        """  PresetList """
        device_uuid = None
        resp = ViperopenapiApi.protocolIngressPresetListGetApi(device_uuid)
        assert resp.status_code == 200

    def test_api_protocolIngressPresetSet(self, config_obj, ViperopenapiApi):
        """  PresetSet """
        device_uuid = None
        preset = None
        resp = ViperopenapiApi.protocolIngressPresetSetPutApi(device_uuid, preset=preset)
        assert resp.status_code == 200

    def test_api_protocolIngressPresetDelete(self, config_obj, ViperopenapiApi):
        """  PresetDelete """
        device_uuid = None
        preset_id = None
        resp = ViperopenapiApi.protocolIngressPresetDeleteDeleteApi(device_uuid, preset_id)
        assert resp.status_code == 200

    def test_api_protocolIngressPresetGoto(self, config_obj, ViperopenapiApi):
        """  PresetGoto """
        device_uuid = None
        preset_id = None
        resp = ViperopenapiApi.protocolIngressPresetGotoPutApi(device_uuid, preset_id)
        assert resp.status_code == 200

    def test_api_protocolIngressHomePositionSet(self, config_obj, ViperopenapiApi):
        """  HomePositionSet """
        device_uuid = None
        preset_id = None
        enabled = None
        reset_time = None
        resp = ViperopenapiApi.protocolIngressHomePositionSetPutApi(device_uuid, preset_id, enabled=enabled, reset_time=reset_time)
        assert resp.status_code == 200

    def test_api_protocolIngressPTZControl(self, config_obj, ViperopenapiApi):
        """  PTZControl """
        device_uuid = None
        pan = None
        stop_enable = None
        tilt = None
        zoom = None
        resp = ViperopenapiApi.protocolIngressPTZControlPutApi(device_uuid, pan=pan, stop_enable=stop_enable, tilt=tilt, zoom=zoom)
        assert resp.status_code == 200

    def test_api_protocolIngressPTZControlTransparent(self, config_obj, ViperopenapiApi):
        """  PTZControlTransparent """
        device_uuid = None
        ptz_command = None
        resp = ViperopenapiApi.protocolIngressPTZControlTransparentPutApi(device_uuid, ptz_command=ptz_command)
        assert resp.status_code == 200

    def test_api_protocolIngressRecordInfo(self, config_obj, ViperopenapiApi):
        """  RecordInfo """
        device_uuid = None
        address = None
        file_path = None
        record_type = None
        recorder_id = None
        secrecy = None
        start_time = None
        stop_time = None
        resp = ViperopenapiApi.protocolIngressRecordInfoPostApi(device_uuid, address=address, file_path=file_path, record_type=record_type, recorder_id=recorder_id, secrecy=secrecy, start_time=start_time, stop_time=stop_time)
        assert resp.status_code == 200

    def test_api_protocolIngressDeviceSubscribe(self, config_obj, ViperopenapiApi):
        """  DeviceSubscribe """
        device_uuid = None
        event = None
        resp = ViperopenapiApi.protocolIngressDeviceSubscribePostApi(device_uuid, event=event)
        assert resp.status_code == 200

    def test_api_protocolIngressTeleBoot(self, config_obj, ViperopenapiApi):
        """  TeleBoot """
        device_uuid = None
        resp = ViperopenapiApi.protocolIngressTeleBootPutApi(device_uuid)
        assert resp.status_code == 200

    def test_api_protocolIngressDeviceUnsubscribe(self, config_obj, ViperopenapiApi):
        """  DeviceUnsubscribe """
        device_uuid = None
        event = None
        resp = ViperopenapiApi.protocolIngressDeviceUnsubscribePostApi(device_uuid, event=event)
        assert resp.status_code == 200

    def test_api_protocolIngressDeviceSearch(self, config_obj, ViperopenapiApi):
        """  DeviceSearch """
        device_type = None
        device_uuid = None
        page = None
        source_type = None
        video_source = None
        resp = ViperopenapiApi.protocolIngressDeviceSearchPostApi(device_type=device_type, device_uuid=device_uuid, page=page, source_type=source_type, video_source=video_source)
        assert resp.status_code == 200

    def test_api_protocolIngressGB28181LocalConfigList(self, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.protocolIngressGB28181LocalConfigListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_protocolIngressGB28181LocalConfigNew(self, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigNew """
        config.local_uuid = None
        config = None
        resp = ViperopenapiApi.protocolIngressGB28181LocalConfigNewPostApi(config.local_uuid, config=config)
        assert resp.status_code == 200

    def test_api_protocolIngressGB28181LocalConfigReplace(self, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigReplace """
        config.local_uuid = None
        config = None
        resp = ViperopenapiApi.protocolIngressGB28181LocalConfigReplacePutApi(config.local_uuid, config=config)
        assert resp.status_code == 200

    def test_api_protocolIngressGB28181LocalConfigDelete(self, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigDelete """
        local_uuid = None
        resp = ViperopenapiApi.protocolIngressGB28181LocalConfigDeleteDeleteApi(local_uuid)
        assert resp.status_code == 200

    def test_api_protocolIngressGB28181LocalConfigInfo(self, config_obj, ViperopenapiApi):
        """  GB28181LocalConfigInfo """
        local_uuid = None
        resp = ViperopenapiApi.protocolIngressGB28181LocalConfigInfoGetApi(local_uuid)
        assert resp.status_code == 200

    def test_api_protocolIngressGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.protocolIngressGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_shortVideoStorageDataRecordDownload(self, config_obj, ViperopenapiApi):
        """  RecordDownload """
        record_url = None
        format = None
        resp = ViperopenapiApi.shortVideoStorageDataRecordDownloadGetApi(record_url, format=format)
        assert resp.status_code == 200

    def test_api_shortVideoStorageImageNew(self, config_obj, ViperopenapiApi):
        """  ImageNew """
        image_times = None
        ns_id = None
        request_id = None
        stream_id = None
        task_id = None
        resp = ViperopenapiApi.shortVideoStorageImageNewPostApi(image_times=image_times, ns_id=ns_id, request_id=request_id, stream_id=stream_id, task_id=task_id)
        assert resp.status_code == 200

    def test_api_shortVideoStorageRecordList(self, config_obj, ViperopenapiApi):
        """  RecordList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.shortVideoStorageRecordListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_shortVideoStorageRecordNew(self, config_obj, ViperopenapiApi):
        """  RecordNew """
        append_record_seconds = None
        ns_id = None
        prerecord_seconds = None
        record_at = None
        record_id = None
        stream_id = None
        task_id = None
        resp = ViperopenapiApi.shortVideoStorageRecordNewPostApi(append_record_seconds=append_record_seconds, ns_id=ns_id, prerecord_seconds=prerecord_seconds, record_at=record_at, record_id=record_id, stream_id=stream_id, task_id=task_id)
        assert resp.status_code == 200

    def test_api_shortVideoStorageRecordDelete(self, config_obj, ViperopenapiApi):
        """  RecordDelete """
        record_id = None
        resp = ViperopenapiApi.shortVideoStorageRecordDeleteDeleteApi(record_id)
        assert resp.status_code == 200

    def test_api_shortVideoStorageRecordInfo(self, config_obj, ViperopenapiApi):
        """  RecordInfo """
        record_id = None
        resp = ViperopenapiApi.shortVideoStorageRecordInfoGetApi(record_id)
        assert resp.status_code == 200

    def test_api_shortVideoStorageSearchRecords(self, config_obj, ViperopenapiApi):
        """  SearchRecords """
        object_id = None
        page = None
        record_at = None
        resp = ViperopenapiApi.shortVideoStorageSearchRecordsPostApi(object_id=object_id, page=page, record_at=record_at)
        assert resp.status_code == 200

    def test_api_shortVideoStorageTaskList(self, config_obj, ViperopenapiApi):
        """  TaskList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.shortVideoStorageTaskListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_shortVideoStorageTaskNew(self, config_obj, ViperopenapiApi):
        """  TaskNew """
        task_request = None
        resp = ViperopenapiApi.shortVideoStorageTaskNewPostApi(task_request=task_request)
        assert resp.status_code == 200

    def test_api_shortVideoStorageTaskDelete(self, config_obj, ViperopenapiApi):
        """  TaskDelete """
        task_id = None
        resp = ViperopenapiApi.shortVideoStorageTaskDeleteDeleteApi(task_id)
        assert resp.status_code == 200

    def test_api_shortVideoStorageTaskInfo(self, config_obj, ViperopenapiApi):
        """  TaskInfo """
        task_id = None
        resp = ViperopenapiApi.shortVideoStorageTaskInfoGetApi(task_id)
        assert resp.status_code == 200

    def test_api_shortVideoStorageTaskUpdate(self, config_obj, ViperopenapiApi):
        """  TaskUpdate """
        task_request.task_id = None
        task_request = None
        resp = ViperopenapiApi.shortVideoStorageTaskUpdatePutApi(task_request.task_id, task_request=task_request)
        assert resp.status_code == 200

    def test_api_streamAPIAppletList(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.streamAPIAppletListGetApi(filter_name=filter_name, filter_tags=filter_tags, filter_auth_state=filter_auth_state, filter_created_time_range_start=filter_created_time_range_start, filter_created_time_range_end=filter_created_time_range_end, page_offset=page_offset, page_limit=page_limit, page_total=page_total, reversed=reversed)
        assert resp.status_code == 200

    def test_api_streamAPIAppletDelete(self, config_obj, ViperopenapiApi):
        """  AppletDelete """
        applet_id = None
        resp = ViperopenapiApi.streamAPIAppletDeleteDeleteApi(applet_id)
        assert resp.status_code == 200

    def test_api_streamAPIAppletGet(self, config_obj, ViperopenapiApi):
        """  AppletGet """
        applet_id = None
        resp = ViperopenapiApi.streamAPIAppletGetGetApi(applet_id)
        assert resp.status_code == 200

    def test_api_streamAPIAppletUpdate(self, config_obj, ViperopenapiApi):
        """  AppletUpdate """
        applet_id = None
        tags = None
        resp = ViperopenapiApi.streamAPIAppletUpdatePatchApi(applet_id, tags=tags)
        assert resp.status_code == 200

    def test_api_streamAPIAppletGetByNameVersion(self, config_obj, ViperopenapiApi):
        """  AppletGetByNameVersion """
        applet_name = None
        applet_version = None
        resp = ViperopenapiApi.streamAPIAppletGetByNameVersionGetApi(applet_name, applet_version)
        assert resp.status_code == 200

    def test_api_streamAPITaskBatchGet(self, config_obj, ViperopenapiApi):
        """  TaskBatchGet """
        task_ids = None
        resp = ViperopenapiApi.streamAPITaskBatchGetPostApi(task_ids=task_ids)
        assert resp.status_code == 200

    def test_api_streamAPITaskBatchUpdateState(self, config_obj, ViperopenapiApi):
        """  TaskBatchUpdateState """
        tasks = None
        resp = ViperopenapiApi.streamAPITaskBatchUpdateStatePatchApi(tasks=tasks)
        assert resp.status_code == 200

    def test_api_streamAPICamerasGetByAppletNameVersion(self, config_obj, ViperopenapiApi):
        """  CamerasGetByAppletNameVersion """
        applet_name = None
        applet_version = None
        resp = ViperopenapiApi.streamAPICamerasGetByAppletNameVersionGetApi(applet_name, applet_version)
        assert resp.status_code == 200

    def test_api_streamAPIInstanceList(self, config_obj, ViperopenapiApi):
        """  InstanceList """
        filter_states = None
        filter_created_time_range_start = None
        filter_created_time_range_end = None
        reversed = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.streamAPIInstanceListGetApi(filter_states=filter_states, filter_created_time_range_start=filter_created_time_range_start, filter_created_time_range_end=filter_created_time_range_end, reversed=reversed, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_streamAPIAppletInstanceNew(self, config_obj, ViperopenapiApi):
        """  AppletInstanceNew """
        applet_id = None
        applet_name = None
        applet_version = None
        user_configs = None
        resp = ViperopenapiApi.streamAPIAppletInstanceNewPostApi(applet_id=applet_id, applet_name=applet_name, applet_version=applet_version, user_configs=user_configs)
        assert resp.status_code == 200

    def test_api_streamAPIAppletInstanceDelete(self, config_obj, ViperopenapiApi):
        """  AppletInstanceDelete """
        instance_id = None
        resp = ViperopenapiApi.streamAPIAppletInstanceDeleteDeleteApi(instance_id)
        assert resp.status_code == 200

    def test_api_streamAPIAppletInstanceGet(self, config_obj, ViperopenapiApi):
        """  AppletInstanceGet """
        instance_id = None
        resp = ViperopenapiApi.streamAPIAppletInstanceGetGetApi(instance_id)
        assert resp.status_code == 200

    def test_api_streamAPITaskTypeList(self, config_obj, ViperopenapiApi):
        """  TaskTypeList """
        name = None
        camera_region_id = None
        camera_camera_idx = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.streamAPITaskTypeListGetApi(name=name, camera_region_id=camera_region_id, camera_camera_idx=camera_camera_idx, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_streamAPITaskTypeNew(self, config_obj, ViperopenapiApi):
        """  TaskTypeNew """
        algo_data = None
        camera = None
        name = None
        stream_data = None
        resp = ViperopenapiApi.streamAPITaskTypeNewPostApi(algo_data=algo_data, camera=camera, name=name, stream_data=stream_data)
        assert resp.status_code == 200

    def test_api_streamAPITaskTypeDelete(self, config_obj, ViperopenapiApi):
        """  TaskTypeDelete """
        task_type_id = None
        resp = ViperopenapiApi.streamAPITaskTypeDeleteDeleteApi(task_type_id)
        assert resp.status_code == 200

    def test_api_streamAPITaskTypeGet(self, config_obj, ViperopenapiApi):
        """  TaskTypeGet """
        task_type_id = None
        resp = ViperopenapiApi.streamAPITaskTypeGetGetApi(task_type_id)
        assert resp.status_code == 200

    def test_api_streamAPITaskTypeUpdate(self, config_obj, ViperopenapiApi):
        """  TaskTypeUpdate """
        task_type_id = None
        algo_data = None
        stream_data = None
        resp = ViperopenapiApi.streamAPITaskTypeUpdatePatchApi(task_type_id, algo_data=algo_data, stream_data=stream_data)
        assert resp.status_code == 200

    def test_api_streamAPITaskList(self, config_obj, ViperopenapiApi):
        """  TaskList """
        filter_applet_applet_name = None
        filter_applet_applet_version = None
        filter_camera_region_id = None
        filter_camera_camera_idx = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.streamAPITaskListGetApi(filter_applet_applet_name=filter_applet_applet_name, filter_applet_applet_version=filter_applet_applet_version, filter_camera_region_id=filter_camera_region_id, filter_camera_camera_idx=filter_camera_camera_idx, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_streamAPITaskNew(self, config_obj, ViperopenapiApi):
        """  TaskNew """
        task = None
        resp = ViperopenapiApi.streamAPITaskNewPostApi(task=task)
        assert resp.status_code == 200

    def test_api_streamAPITaskDelete(self, config_obj, ViperopenapiApi):
        """  TaskDelete """
        task_id = None
        resp = ViperopenapiApi.streamAPITaskDeleteDeleteApi(task_id)
        assert resp.status_code == 200

    def test_api_streamAPITaskGet(self, config_obj, ViperopenapiApi):
        """  TaskGet """
        task_id = None
        resp = ViperopenapiApi.streamAPITaskGetGetApi(task_id)
        assert resp.status_code == 200

    def test_api_streamAPITaskUpdate(self, config_obj, ViperopenapiApi):
        """  TaskUpdate """
        task_id = None
        data = None
        resp = ViperopenapiApi.streamAPITaskUpdatePatchApi(task_id, data=data)
        assert resp.status_code == 200

    def test_api_streamFileAppletUpload(self, config_obj, ViperopenapiApi):
        """  AppletUpload """
        resp = ViperopenapiApi.streamFileAppletUploadPostApi()
        assert resp.status_code == 200

    def test_api_streamFileAppletDownload(self, config_obj, ViperopenapiApi):
        """  AppletDownload """
        applet_name = None
        applet_version = None
        resp = ViperopenapiApi.streamFileAppletDownloadGetApi(applet_name, applet_version)
        assert resp.status_code == 200

    def test_api_streamFileAppletDocDownload(self, config_obj, ViperopenapiApi):
        """  AppletDocDownload """
        applet_name = None
        applet_version = None
        file_path = None
        resp = ViperopenapiApi.streamFileAppletDocDownloadGetApi(applet_name, applet_version, file_path)
        assert resp.status_code == 200

    def test_api_structDBAggregate(self, config_obj, ViperopenapiApi):
        """  Aggregate """
        camera_ids = None
        end_time = None
        filters = None
        measures = None
        object_type = None
        options = None
        start_time = None
        time_interval = None
        resp = ViperopenapiApi.structDBAggregatePostApi(camera_ids=camera_ids, end_time=end_time, filters=filters, measures=measures, object_type=object_type, options=options, start_time=start_time, time_interval=time_interval)
        assert resp.status_code == 200

    def test_api_structDBDeleteObjects(self, config_obj, ViperopenapiApi):
        """  DeleteObjects """
        unique_ids = None
        resp = ViperopenapiApi.structDBDeleteObjectsPostApi(unique_ids=unique_ids)
        assert resp.status_code == 200

    def test_api_structDBDeleteObjectsBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteObjectsBeforeDate """
        date = None
        object_type = None
        resp = ViperopenapiApi.structDBDeleteObjectsBeforeDatePostApi(date=date, object_type=object_type)
        assert resp.status_code == 200

    def test_api_structDBGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.structDBGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_structDBNamespaceList(self, config_obj, ViperopenapiApi):
        """  NamespaceList """
        page_offset = None
        page_limit = None
        page_total = None
        resp = ViperopenapiApi.structDBNamespaceListGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_structDBNamespaceNew(self, config_obj, ViperopenapiApi):
        """  NamespaceNew """
        namespace.ns_id = None
        namespace = None
        resp = ViperopenapiApi.structDBNamespaceNewPostApi(namespace.ns_id, namespace=namespace)
        assert resp.status_code == 200

    def test_api_structDBNamespaceDelete(self, config_obj, ViperopenapiApi):
        """  NamespaceDelete """
        ns_id = None
        resp = ViperopenapiApi.structDBNamespaceDeleteDeleteApi(ns_id)
        assert resp.status_code == 200

    def test_api_structDBQuery(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.structDBQueryPostApi(camera_ids=camera_ids, deduplication=deduplication, end_time=end_time, filters=filters, marker=marker, object_id=object_id, object_type=object_type, options=options, page_limit=page_limit, page_offset=page_offset, start_time=start_time, timestamp_asc=timestamp_asc, track_total_hits=track_total_hits)
        assert resp.status_code == 200

    def test_api_timespaceDBMultiV3DBList(self, config_obj, ViperopenapiApi):
        """  DBList """
        deploy_type = None
        resp = ViperopenapiApi.timespaceDBMultiV3DBListGetApi(deploy_type)
        assert resp.status_code == 200

    def test_api_timespaceDBMultiV3DBNew(self, config_obj, ViperopenapiApi):
        """  DBNew """
        deploy_type = None
        capacity = None
        db_id = None
        description = None
        feature_version = None
        object_type = None
        resp = ViperopenapiApi.timespaceDBMultiV3DBNewPostApi(deploy_type, capacity=capacity, db_id=db_id, description=description, feature_version=feature_version, object_type=object_type)
        assert resp.status_code == 200

    def test_api_timespaceDBMultiV3DBDelete(self, config_obj, ViperopenapiApi):
        """  DBDelete """
        deploy_type = None
        db_id = None
        resp = ViperopenapiApi.timespaceDBMultiV3DBDeleteDeleteApi(deploy_type, db_id)
        assert resp.status_code == 200

    def test_api_timespaceDBMultiV3DBGet(self, config_obj, ViperopenapiApi):
        """  DBGet """
        deploy_type = None
        db_id = None
        resp = ViperopenapiApi.timespaceDBMultiV3DBGetGetApi(deploy_type, db_id)
        assert resp.status_code == 200

    def test_api_timespaceDBMultiV3GetSystemInfoV3(self, config_obj, ViperopenapiApi):
        """  GetSystemInfoV3 """
        deploy_type = None
        resp = ViperopenapiApi.timespaceDBMultiV3GetSystemInfoV3GetApi(deploy_type)
        assert resp.status_code == 200

    def test_api_timespaceDBAddFeatureAsync(self, config_obj, ViperopenapiApi):
        """  AddFeatureAsync """
        deploy_type = None
        object_type = None
        feature_version = None
        db_id = None
        object_info = None
        resp = ViperopenapiApi.timespaceDBAddFeatureAsyncPostApi(deploy_type, object_type, feature_version, db_id=db_id, object_info=object_info)
        assert resp.status_code == 200

    def test_api_timespaceDBBatchGetFeatureByObjectID(self, config_obj, ViperopenapiApi):
        """  BatchGetFeatureByObjectID """
        deploy_type = None
        object_type = None
        feature_version = None
        db_id = None
        ignore_feature = None
        object_ids = None
        resp = ViperopenapiApi.timespaceDBBatchGetFeatureByObjectIDPostApi(deploy_type, object_type, feature_version, db_id=db_id, ignore_feature=ignore_feature, object_ids=object_ids)
        assert resp.status_code == 200

    def test_api_timespaceDBClusterGetByKey(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.timespaceDBClusterGetByKeyGetApi(deploy_type, object_type, feature_version, key=key, period_start=period_start, period_end=period_end, load_mode=load_mode, max_preview_load_count=max_preview_load_count, results_filter_filter_mode=results_filter_filter_mode, results_filter_preview_results_count=results_filter_preview_results_count)
        assert resp.status_code == 200

    def test_api_timespaceDBClusterSearch(self, config_obj, ViperopenapiApi):
        """  ClusterSearch """
        deploy_type = None
        object_type = None
        feature_version = None
        config = None
        feature = None
        filter_configs = None
        load_mode = None
        max_preview_load_count = None
        resp = ViperopenapiApi.timespaceDBClusterSearchPostApi(deploy_type, object_type, feature_version, config=config, feature=feature, filter_configs=filter_configs, load_mode=load_mode, max_preview_load_count=max_preview_load_count)
        assert resp.status_code == 200

    def test_api_timespaceDBClusterGet(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.timespaceDBClusterGetGetApi(deploy_type, object_type, feature_version, cluster_id, period_start=period_start, period_end=period_end, page_offset=page_offset, page_limit=page_limit, page_total=page_total, ignore_centroid=ignore_centroid)
        assert resp.status_code == 200

    def test_api_timespaceDBClusterPut(self, config_obj, ViperopenapiApi):
        """  ClusterPut """
        deploy_type = None
        object_type = None
        feature_version = None
        cluster_id = None
        extra_info = None
        resp = ViperopenapiApi.timespaceDBClusterPutPutApi(deploy_type, object_type, feature_version, cluster_id, extra_info=extra_info)
        assert resp.status_code == 200

    def test_api_timespaceDBDeleteFeature(self, config_obj, ViperopenapiApi):
        """  DeleteFeature """
        deploy_type = None
        object_type = None
        feature_version = None
        db_id = None
        id = None
        resp = ViperopenapiApi.timespaceDBDeleteFeaturePostApi(deploy_type, object_type, feature_version, db_id=db_id, id=id)
        assert resp.status_code == 200

    def test_api_timespaceDBDeleteShardsBeforeDate(self, config_obj, ViperopenapiApi):
        """  DeleteShardsBeforeDate """
        deploy_type = None
        object_type = None
        feature_version = None
        date = None
        db_id = None
        resp = ViperopenapiApi.timespaceDBDeleteShardsBeforeDatePostApi(deploy_type, object_type, feature_version, date=date, db_id=db_id)
        assert resp.status_code == 200

    def test_api_timespaceDBGetFeature(self, config_obj, ViperopenapiApi):
        """  GetFeature """
        deploy_type = None
        object_type = None
        feature_version = None
        db_id = None
        id = None
        resp = ViperopenapiApi.timespaceDBGetFeaturePostApi(deploy_type, object_type, feature_version, db_id=db_id, id=id)
        assert resp.status_code == 200

    def test_api_timespaceDBGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        deploy_type = None
        object_type = None
        feature_version = None
        resp = ViperopenapiApi.timespaceDBGetSystemInfoGetApi(deploy_type, object_type, feature_version)
        assert resp.status_code == 200

    def test_api_timespaceDBLabelingDataSourcesSet(self, config_obj, ViperopenapiApi):
        """  LabelingDataSourcesSet """
        deploy_type = None
        object_type = None
        feature_version = None
        data_sources = None
        resp = ViperopenapiApi.timespaceDBLabelingDataSourcesSetPostApi(deploy_type, object_type, feature_version, data_sources=data_sources)
        assert resp.status_code == 200

    def test_api_timespaceDBLabelingGetInfo(self, config_obj, ViperopenapiApi):
        """  LabelingGetInfo """
        deploy_type = None
        object_type = None
        feature_version = None
        resp = ViperopenapiApi.timespaceDBLabelingGetInfoGetApi(deploy_type, object_type, feature_version)
        assert resp.status_code == 200

    def test_api_timespaceDBLabelingModeSet(self, config_obj, ViperopenapiApi):
        """  LabelingModeSet """
        deploy_type = None
        object_type = None
        feature_version = None
        mode = None
        resp = ViperopenapiApi.timespaceDBLabelingModeSetPostApi(deploy_type, object_type, feature_version, mode=mode)
        assert resp.status_code == 200

    def test_api_timespaceDBListFeatures(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.timespaceDBListFeaturesPostApi(deploy_type, object_type, feature_version, camera_ids=camera_ids, db_id=db_id, marker=marker, page_size=page_size, period=period, reversed=reversed)
        assert resp.status_code == 200

    def test_api_timespaceDBSearch(self, config_obj, ViperopenapiApi):
        """  Search """
        deploy_type = None
        object_type = None
        feature_version = None
        config = None
        feature = None
        resp = ViperopenapiApi.timespaceDBSearchPostApi(deploy_type, object_type, feature_version, config=config, feature=feature)
        assert resp.status_code == 200

    def test_api_videoIngressGenerateRTMPAddress(self, config_obj, ViperopenapiApi):
        """  GenerateRTMPAddress """
        source_info = None
        resp = ViperopenapiApi.videoIngressGenerateRTMPAddressPostApi(source_info=source_info)
        assert resp.status_code == 200

    def test_api_videoIngressGenerateRTSPAddress(self, config_obj, ViperopenapiApi):
        """  GenerateRTSPAddress """
        source_info = None
        resp = ViperopenapiApi.videoIngressGenerateRTSPAddressPostApi(source_info=source_info)
        assert resp.status_code == 200

    def test_api_videoIngressGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.videoIngressGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_videoIngressStreamInfo(self, config_obj, ViperopenapiApi):
        """  StreamInfo """
        url = None
        resp = ViperopenapiApi.videoIngressStreamInfoGetApi(url)
        assert resp.status_code == 200

    def test_api_videoIngressGetStreamInformation(self, config_obj, ViperopenapiApi):
        """  GetStreamInformation """
        source_info = None
        resp = ViperopenapiApi.videoIngressGetStreamInformationPostApi(source_info=source_info)
        assert resp.status_code == 200

    def test_api_videoProcessGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        resp = ViperopenapiApi.videoProcessGetSystemInfoGetApi()
        assert resp.status_code == 200

    def test_api_videoProcessTaskList(self, config_obj, ViperopenapiApi):
        """  TaskList """
        page_request_offset = None
        page_request_limit = None
        page_request_total = None
        resp = ViperopenapiApi.videoProcessTaskListGetApi(page_request_offset=page_request_offset, page_request_limit=page_request_limit, page_request_total=page_request_total)
        assert resp.status_code == 200

    def test_api_videoProcessTaskNew(self, config_obj, ViperopenapiApi):
        """  TaskNew """
        task = None
        resp = ViperopenapiApi.videoProcessTaskNewPostApi(task=task)
        assert resp.status_code == 200

    def test_api_videoProcessTaskDelete(self, config_obj, ViperopenapiApi):
        """  TaskDelete """
        task_id = None
        resp = ViperopenapiApi.videoProcessTaskDeleteDeleteApi(task_id)
        assert resp.status_code == 200

    def test_api_videoProcessTaskStatus(self, config_obj, ViperopenapiApi):
        """  TaskStatus """
        task_id = None
        resp = ViperopenapiApi.videoProcessTaskStatusGetApi(task_id)
        assert resp.status_code == 200

    def test_api_videoProcessTaskUpdate(self, config_obj, ViperopenapiApi):
        """  TaskUpdate """
        task_id = None
        task = None
        resp = ViperopenapiApi.videoProcessTaskUpdatePostApi(task_id, task=task)
        assert resp.status_code == 200

    def test_api_staticDBFeatureBatchSearchMulti(self, config_obj, ViperopenapiApi):
        """  FeatureBatchSearchMulti """
        db_type = None
        configs = None
        dropped_fields = None
        features = None
        merge_top_k = None
        resp = ViperopenapiApi.staticDBFeatureBatchSearchMultiPostApi(db_type, configs=configs, dropped_fields=dropped_fields, features=features, merge_top_k=merge_top_k)
        assert resp.status_code == 200

    def test_api_staticDBDBList(self, config_obj, ViperopenapiApi):
        """  DBList """
        db_type = None
        resp = ViperopenapiApi.staticDBDBListGetApi(db_type)
        assert resp.status_code == 200

    def test_api_staticDBDBNew(self, config_obj, ViperopenapiApi):
        """  DBNew """
        db_type = None
        db_size = None
        description = None
        feature_version = None
        name = None
        object_type = None
        options = None
        resp = ViperopenapiApi.staticDBDBNewPostApi(db_type, db_size=db_size, description=description, feature_version=feature_version, name=name, object_type=object_type, options=options)
        assert resp.status_code == 200

    def test_api_staticDBFeatureBatchAdd(self, config_obj, ViperopenapiApi):
        """  FeatureBatchAdd """
        db_type = None
        col_id = None
        items = None
        resp = ViperopenapiApi.staticDBFeatureBatchAddPostApi(db_type, col_id, items=items)
        assert resp.status_code == 200

    def test_api_staticDBFeatureBatchDelete(self, config_obj, ViperopenapiApi):
        """  FeatureBatchDelete """
        db_type = None
        col_id = None
        ids = None
        resp = ViperopenapiApi.staticDBFeatureBatchDeletePostApi(db_type, col_id, ids=ids)
        assert resp.status_code == 200

    def test_api_staticDBFeatureBatchDeleteByKey(self, config_obj, ViperopenapiApi):
        """  FeatureBatchDeleteByKey """
        db_type = None
        col_id = None
        keys = None
        resp = ViperopenapiApi.staticDBFeatureBatchDeleteByKeyPostApi(db_type, col_id, keys=keys)
        assert resp.status_code == 200

    def test_api_staticDBFeatureBatchGet(self, config_obj, ViperopenapiApi):
        """  FeatureBatchGet """
        db_type = None
        col_id = None
        consistency = None
        ids = None
        resp = ViperopenapiApi.staticDBFeatureBatchGetPostApi(db_type, col_id, consistency=consistency, ids=ids)
        assert resp.status_code == 200

    def test_api_staticDBFeatureBatchGetByKey(self, config_obj, ViperopenapiApi):
        """  FeatureBatchGetByKey """
        db_type = None
        col_id = None
        consistency = None
        ignore_details = None
        keys = None
        resp = ViperopenapiApi.staticDBFeatureBatchGetByKeyPostApi(db_type, col_id, consistency=consistency, ignore_details=ignore_details, keys=keys)
        assert resp.status_code == 200

    def test_api_staticDBFeatureBatchGetByKeyPaging(self, config_obj, ViperopenapiApi):
        """  FeatureBatchGetByKeyPaging """
        db_type = None
        col_id = None
        consistency = None
        ignore_details = None
        keys = None
        marker = None
        page_size = None
        resp = ViperopenapiApi.staticDBFeatureBatchGetByKeyPagingPostApi(db_type, col_id, consistency=consistency, ignore_details=ignore_details, keys=keys, marker=marker, page_size=page_size)
        assert resp.status_code == 200

    def test_api_staticDBFeatureBatchSearch(self, config_obj, ViperopenapiApi):
        """  FeatureBatchSearch """
        db_type = None
        col_id = None
        consistency = None
        dropped_fields = None
        features = None
        min_score = None
        return_raw_feature = None
        top_k = None
        resp = ViperopenapiApi.staticDBFeatureBatchSearchPostApi(db_type, col_id, consistency=consistency, dropped_fields=dropped_fields, features=features, min_score=min_score, return_raw_feature=return_raw_feature, top_k=top_k)
        assert resp.status_code == 200

    def test_api_staticDBFeatureList(self, config_obj, ViperopenapiApi):
        """  FeatureList """
        db_type = None
        col_id = None
        marker = None
        page_size = None
        resp = ViperopenapiApi.staticDBFeatureListPostApi(db_type, col_id, marker=marker, page_size=page_size)
        assert resp.status_code == 200

    def test_api_staticDBFeatureUpdate(self, config_obj, ViperopenapiApi):
        """  FeatureUpdate """
        db_type = None
        col_id = None
        id = None
        extra_info = None
        resp = ViperopenapiApi.staticDBFeatureUpdatePatchApi(db_type, col_id, id, extra_info=extra_info)
        assert resp.status_code == 200

    def test_api_staticDBFeatureUpdateByID(self, config_obj, ViperopenapiApi):
        """  FeatureUpdateByID """
        db_type = None
        col_id = None
        id = None
        item = None
        resp = ViperopenapiApi.staticDBFeatureUpdateByIDPatchApi(db_type, col_id, id, item=item)
        assert resp.status_code == 200

    def test_api_staticDBDBDelete(self, config_obj, ViperopenapiApi):
        """  DBDelete """
        db_type = None
        db_id = None
        resp = ViperopenapiApi.staticDBDBDeleteDeleteApi(db_type, db_id)
        assert resp.status_code == 200

    def test_api_staticDBDBGet(self, config_obj, ViperopenapiApi):
        """  DBGet """
        db_type = None
        db_id = None
        ignore_indexes_detail = None
        resp = ViperopenapiApi.staticDBDBGetGetApi(db_type, db_id, ignore_indexes_detail=ignore_indexes_detail)
        assert resp.status_code == 200

    def test_api_staticDBDBUpdate(self, config_obj, ViperopenapiApi):
        """  DBUpdate """
        db_type = None
        db_id = None
        description = None
        name = None
        object_type = None
        options = None
        resp = ViperopenapiApi.staticDBDBUpdatePatchApi(db_type, db_id, description=description, name=name, object_type=object_type, options=options)
        assert resp.status_code == 200

    def test_api_staticDBDBTrain(self, config_obj, ViperopenapiApi):
        """  DBTrain """
        db_type = None
        db_id = None
        mode = None
        resp = ViperopenapiApi.staticDBDBTrainPostApi(db_type, db_id, mode=mode)
        assert resp.status_code == 200

    def test_api_staticDBGetSnapshotStatus(self, config_obj, ViperopenapiApi):
        """  GetSnapshotStatus """
        db_type = None
        resp = ViperopenapiApi.staticDBGetSnapshotStatusGetApi(db_type)
        assert resp.status_code == 200

    def test_api_staticDBGetSystemInfo(self, config_obj, ViperopenapiApi):
        """  GetSystemInfo """
        db_type = None
        resp = ViperopenapiApi.staticDBGetSystemInfoGetApi(db_type)
        assert resp.status_code == 200

    def test_api_imageIngressPassiveIngressStandardTargetImageAsync(self, config_obj, ViperopenapiApi):
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
        resp = ViperopenapiApi.imageIngressPassiveIngressStandardTargetImageAsyncPostApi(camera_info=camera_info, capture_time=capture_time, extra_fields=extra_fields, extra_info=extra_info, full_image=full_image, ns_id=ns_id, receive_time=receive_time, storage_policy=storage_policy, target_images=target_images, task_object_config=task_object_config)
        assert resp.status_code == 200
