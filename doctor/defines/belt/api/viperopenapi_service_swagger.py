#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.api_lib.base_api import BaseApi
from core.swagger_utils import load_swagger

"""
使用说明：


"""


collections = load_swagger("belt")


class ViperopenapiSwaggerApi(BaseApi):
    """ web接口"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        self.host = host
        self.ext_info = ext_info
        self.config_obj = config_obj
        self.token = token
        self.host_map = self.readHostMap(collections.name)
        self.TOKEN_NAME = ""
        self.TOKEN_VALUE = "%s"  # token默认信息
        collections.init(self, conf=config_obj, ext_info=ext_info)

    def genPostMan(self):
        """ 生成postman接口文件"""
        self.ext_info.isRequestOpened = True
        self.genPostManFromSwagger(collections)

    def kafkaCallbackExampleCallbackPostApi(self, batch_objects=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  Callback """
        """  path: [post]/_YOUR_CALLBACK_SERVICE_/_YOUR_CALLBACK_SERVICE_URL_ API """
        """  body: 
                {
                    "batch_objects": [
                        {
                            "camera_info": {},
                            "captured_time": "",
                            "extra_fields": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "extra_info": "",
                            "feature": {},
                            "ns_id": "",
                            "object": {},
                            "object_index_in_frame": 0,
                            "panoramic_image": {},
                            "portrait_image": {},
                            "producer_annotation": {},
                            "received_time": "",
                            "relative_time": "",
                            "track_event": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "kafkaCallbackExampleCallback")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("batch_objects", batch_objects)
        return intef.request() if sendRequest else intef

    def streamMessageCallbackPostApi(self, messages=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  Callback """
        """  path: [post]/_YOUR_CALLBACK_SERVICE_PATH_ API """
        """  body: 
                {
                    "messages": [
                        {
                            "applet_name": "",
                            "applet_version": 0,
                            "camera": {},
                            "creation_time": "",
                            "data": {},
                            "data_type": "",
                            "ns_id": "",
                            "task_type": ""
                        }
                    ]
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "streamMessageCallback")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("messages", messages)
        return intef.request() if sendRequest else intef

    def batchVideoProcessJobListGetApi(self, page_offset=None, page_limit=None, page_total=None, period_start=None, period_end=None, status=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobList """
        """  path: [get]/batch/batch-video-process/v1/jobs API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
                参数名称：period.start　类型：string　描述：开始时间, 区间包含.
                参数名称：period.end　类型：string　描述：结束时间, 区间不包含.
                参数名称：status　类型：array　描述：可选, 过滤状态
        """
        """  resp:
                200():
                {
                    "jobs": [
                        {
                            "canceled_at": "",
                            "config": {},
                            "created_at": "",
                            "deleted_at": "",
                            "events": [
                                {
                                    "code": 0,
                                    "event_level": {},
                                    "reason": "",
                                    "timestamp": ""
                                }
                            ],
                            "finished_at": "",
                            "id": "",
                            "outputs": [
                                {
                                    "fragments": [
                                        {
                                            "end_time": "",
                                            "result": {},
                                            "start_time": "",
                                            "url": ""
                                        }
                                    ],
                                    "resolution": {},
                                    "result": {},
                                    "source_index": 0,
                                    "url": "",
                                    "video_total_analysis_duration": "",
                                    "video_total_duration": ""
                                }
                            ],
                            "result": {}
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "batchVideoProcessJobList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.update_params("period.start", period_start)
        intef.update_params("period.end", period_end)
        intef.update_params("status", status)
        return intef.request() if sendRequest else intef

    def batchVideoProcessJobNewPostApi(self, config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobNew """
        """  path: [post]/batch/batch-video-process/v1/jobs API """
        """  body: 
                {
                    "config": {}
                }
        """
        """  resp:
                200():
                {
                    "job_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "batchVideoProcessJobNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("config", config)
        return intef.request() if sendRequest else intef

    def batchVideoProcessJobDeleteDeleteApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobDelete """
        """  path: [delete]/batch/batch-video-process/v1/jobs/{job_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "batchVideoProcessJobDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def batchVideoProcessJobGetGetApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobGet """
        """  path: [get]/batch/batch-video-process/v1/jobs/{job_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "job": {}
                }

        """
        intef = collections.interface("viperOpenApi", "batchVideoProcessJobGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def batchVideoProcessJobCancelPostApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobCancel """
        """  path: [post]/batch/batch-video-process/v1/jobs/{job_id}/cancel API """
        """  body: 
                {}
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "batchVideoProcessJobCancel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def clusteringJobMgrDeleteClusterBeforeDatePostApi(self, Threshold=None, date=None, is_delete_anonymous_cluster=None, is_delete_identified_cluster=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteClusterBeforeDate """
        """  path: [post]/batch/clustering-job-manager/v1/delete_cluster_before_date API """
        """  body: 
                {
                    "Threshold": 0,
                    "date": "",
                    "is_delete_anonymous_cluster": false,
                    "is_delete_identified_cluster": false
                }
        """
        """  resp:
                200():
                {
                    "id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "clusteringJobMgrDeleteClusterBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("Threshold", Threshold)
        intef.update_body("date", date)
        intef.update_body("is_delete_anonymous_cluster", is_delete_anonymous_cluster)
        intef.update_body("is_delete_identified_cluster", is_delete_identified_cluster)
        return intef.request() if sendRequest else intef

    def clusteringJobMgrLabelingByExtraDataSourcesPostApi(self, data_sources=None, min_score=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  LabelingByExtraDataSources """
        """  path: [post]/batch/clustering-job-manager/v1/labeling_by_extra_data_sources API """
        """  body: 
                {
                    "data_sources": [
                        {
                            "db_id": "",
                            "db_type": {}
                        }
                    ],
                    "min_score": 0
                }
        """
        """  resp:
                200():
                {
                    "id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "clusteringJobMgrLabelingByExtraDataSources")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("data_sources", data_sources)
        intef.update_body("min_score", min_score)
        return intef.request() if sendRequest else intef

    def clusteringJobMgrMatrixGenerationPostApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  MatrixGeneration """
        """  path: [post]/batch/clustering-job-manager/v1/matrix API """
        """  body: 
                {}
        """
        """  resp:
                200():
                {
                    "id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "clusteringJobMgrMatrixGeneration")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def dataFusionDeleteJobsBeforeDatePostApi(self, catalog=None, date=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteJobsBeforeDate """
        """  path: [post]/batch/data-fusion/v1/delete_jobs_before_date API """
        """  body: 
                {
                    "catalog": "",
                    "date": ""
                }
        """
        """  resp:
                200():
                {
                    "deleted_jobs": 0
                }

        """
        intef = collections.interface("viperOpenApi", "dataFusionDeleteJobsBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("catalog", catalog)
        intef.update_body("date", date)
        return intef.request() if sendRequest else intef

    def dataFusionGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/batch/data-fusion/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "catalogs": [
                        {
                            "catalog": "",
                            "first_job_time": "",
                            "last_job_time": ""
                        }
                    ],
                    "es_info": {
                        "available_mb": "",
                        "total_mb": "",
                        "total_used_mb": ""
                    },
                    "first_job_time": "",
                    "hdfs_info": {
                        "capacity": "",
                        "remaining": "",
                        "used": ""
                    },
                    "last_job_time": ""
                }

        """
        intef = collections.interface("viperOpenApi", "dataFusionGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def dataFusionJobListGetApi(self, type=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobList """
        """  path: [get]/batch/data-fusion/v1/jobs API """
        """  params: 
                参数名称：type　类型：string　描述：要查找的job类型.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "jobs": [
                        {
                            "canceled_at": "",
                            "config": {},
                            "created_at": "",
                            "deleted_at": "",
                            "finished_at": "",
                            "id": "",
                            "output": {},
                            "result": {}
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "dataFusionJobList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("type", type)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def dataFusionJobNewPostApi(self, config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobNew """
        """  path: [post]/batch/data-fusion/v1/jobs API """
        """  body: 
                {
                    "config": {}
                }
        """
        """  resp:
                200():
                {
                    "job_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "dataFusionJobNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("config", config)
        return intef.request() if sendRequest else intef

    def dataFusionJobDeleteDeleteApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobDelete """
        """  path: [delete]/batch/data-fusion/v1/jobs/{job_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "dataFusionJobDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def dataFusionJobGetGetApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobGet """
        """  path: [get]/batch/data-fusion/v1/jobs/{job_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "job": {}
                }

        """
        intef = collections.interface("viperOpenApi", "dataFusionJobGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def dataFusionJobCancelPostApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobCancel """
        """  path: [post]/batch/data-fusion/v1/jobs/{job_id}/cancel API """
        """  body: 
                {}
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "dataFusionJobCancel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def batchDBIntersectionJobListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobList """
        """  path: [get]/batch/db-intersection/v1/jobs API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "jobs": [
                        {
                            "canceled_at": "",
                            "config": {},
                            "created_at": "",
                            "deleted_at": "",
                            "finished_at": "",
                            "id": "",
                            "output": {},
                            "result": {}
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "batchDBIntersectionJobList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def batchDBIntersectionJobNewPostApi(self, config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobNew """
        """  path: [post]/batch/db-intersection/v1/jobs API """
        """  body: 
                {
                    "config": {}
                }
        """
        """  resp:
                200():
                {
                    "job_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "batchDBIntersectionJobNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("config", config)
        return intef.request() if sendRequest else intef

    def batchDBIntersectionJobDeleteDeleteApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobDelete """
        """  path: [delete]/batch/db-intersection/v1/jobs/{job_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "batchDBIntersectionJobDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def batchDBIntersectionJobGetGetApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobGet """
        """  path: [get]/batch/db-intersection/v1/jobs/{job_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "job": {}
                }

        """
        intef = collections.interface("viperOpenApi", "batchDBIntersectionJobGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def batchDBIntersectionJobCancelPostApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobCancel """
        """  path: [post]/batch/db-intersection/v1/jobs/{job_id}/cancel API """
        """  body: 
                {}
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "batchDBIntersectionJobCancel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def infraBatchMgrBatchManagerFileDownloadGetApi(self, path, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchManagerFileDownload """
        """  path: [get]/components/batch-manager-default/file/_/{path} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                ""

        """
        intef = collections.interface("viperOpenApi", "infraBatchMgrBatchManagerFileDownload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("path", path)
        return intef.request() if sendRequest else intef

    def infraBatchMgrBatchManagerHdfsDownloadGetApi(self, path, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchManagerHdfsDownload """
        """  path: [get]/components/batch-manager-default/hdfs/_/{path} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                ""

        """
        intef = collections.interface("viperOpenApi", "infraBatchMgrBatchManagerHdfsDownload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("path", path)
        return intef.request() if sendRequest else intef

    def infraBatchMgrGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/components/batch-manager-default/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "catalogs": [
                        {
                            "catalog": "",
                            "first_job_time": "",
                            "last_job_time": ""
                        }
                    ],
                    "first_job_time": "",
                    "hdfs_info": {},
                    "last_job_time": "",
                    "resource_pools": [
                        {
                            "nodes": [
                                {
                                    "labels": {
                                        "additionalProp1": "",
                                        "additionalProp2": "",
                                        "additionalProp3": ""
                                    },
                                    "name": ""
                                }
                            ],
                            "queue_length": 0,
                            "resource_pool": "",
                            "scheduled_jobs": 0
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "infraBatchMgrGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraBatchMgrJobListGetApi(self, page_offset=None, page_limit=None, page_total=None, catalog=None, period_start=None, period_end=None, status=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobList """
        """  path: [get]/components/batch-manager-default/v1/jobs API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
                参数名称：catalog　类型：string　描述：可选, 如不为空, 则只列出指定类型的任务.
                参数名称：period.start　类型：string　描述：开始时间, 区间包含.
                参数名称：period.end　类型：string　描述：结束时间, 区间不包含.
                参数名称：status　类型：array　描述：可选, 过滤状态
        """
        """  resp:
                200():
                {
                    "jobs": [
                        {
                            "application_master": {},
                            "canceled_at": "",
                            "catalog": "",
                            "created_at": "",
                            "deleted_at": "",
                            "finished_at": "",
                            "id": "",
                            "job_type": {},
                            "name": "",
                            "parameters": "",
                            "priority": {},
                            "resource_pool": "",
                            "result": {},
                            "retries": 0,
                            "role_status": [
                                {
                                    "error_message": "",
                                    "pod_status": [
                                        {
                                            "host_ip": "",
                                            "ip": "",
                                            "name": "",
                                            "role": ""
                                        }
                                    ],
                                    "role_name": "",
                                    "scheduled_uuid": "",
                                    "status": {},
                                    "total_restarts": 0
                                }
                            ],
                            "running_at": "",
                            "timeout": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraBatchMgrJobList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.update_params("catalog", catalog)
        intef.update_params("period.start", period_start)
        intef.update_params("period.end", period_end)
        intef.update_params("status", status)
        return intef.request() if sendRequest else intef

    def infraBatchMgrJobNewPostApi(self, job=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobNew """
        """  path: [post]/components/batch-manager-default/v1/jobs API """
        """  body: 
                {
                    "job": {
                        "application_master": {},
                        "canceled_at": "",
                        "catalog": "",
                        "created_at": "",
                        "deleted_at": "",
                        "finished_at": "",
                        "id": "",
                        "job_type": {},
                        "name": "",
                        "parameters": "",
                        "priority": {},
                        "resource_pool": "",
                        "result": {},
                        "retries": 0,
                        "role_status": [
                            {
                                "error_message": "",
                                "pod_status": [
                                    {
                                        "host_ip": "",
                                        "ip": "",
                                        "name": "",
                                        "role": ""
                                    }
                                ],
                                "role_name": "",
                                "scheduled_uuid": "",
                                "status": {},
                                "total_restarts": 0
                            }
                        ],
                        "running_at": "",
                        "timeout": ""
                    }
                }
        """
        """  resp:
                200():
                {
                    "job_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "infraBatchMgrJobNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("job", job)
        return intef.request() if sendRequest else intef

    def infraBatchMgrJobDeleteDeleteApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobDelete """
        """  path: [delete]/components/batch-manager-default/v1/jobs/{job_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraBatchMgrJobDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def infraBatchMgrJobGetGetApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobGet """
        """  path: [get]/components/batch-manager-default/v1/jobs/{job_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "events": [
                        {
                            "code": 0,
                            "event_level": "[INFO]INFO/WARN/ERROR/FATAL",
                            "reason": "",
                            "timestamp": ""
                        }
                    ],
                    "job": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraBatchMgrJobGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def infraBatchMgrJobCancelPostApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobCancel """
        """  path: [post]/components/batch-manager-default/v1/jobs/{job_id}/cancel API """
        """  body: 
                {}
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraBatchMgrJobCancel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def infraBatchMgrDeleteJobsBeforeDatePostApi(self, catalog=None, date=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteJobsBeforeDate """
        """  path: [post]/components/batch-manager-default/v1/jobs_delete_before_date API """
        """  body: 
                {
                    "catalog": "",
                    "date": ""
                }
        """
        """  resp:
                200():
                {
                    "deleted_jobs": 0
                }

        """
        intef = collections.interface("viperOpenApi", "infraBatchMgrDeleteJobsBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("catalog", catalog)
        intef.update_body("date", date)
        return intef.request() if sendRequest else intef

    def infraConsoleCertificateInfosGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CertificateInfos """
        """  path: [get]/components/console-default/v1/certificate_infos API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "certificate_infos": [
                        {
                            "certificate_type": {},
                            "dongle_id": "",
                            "expired_at": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "infraConsoleCertificateInfos")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraConsoleComponentListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ComponentList """
        """  path: [get]/components/console-default/v1/components API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "components": [
                        {
                            "image": "",
                            "name": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraConsoleComponentList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def infraConsoleDeleteESBeforeDatePostApi(self, date=None, index_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteESBeforeDate """
        """  path: [post]/components/console-default/v1/delete_es_before_date API """
        """  body: 
                {
                    "date": "",
                    "index_type": {}
                }
        """
        """  resp:
                200():
                {
                    "code": 0
                }

        """
        intef = collections.interface("viperOpenApi", "infraConsoleDeleteESBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("date", date)
        intef.update_body("index_type", index_type)
        return intef.request() if sendRequest else intef

    def infraConsoleFeatureVersionsGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureVersions """
        """  path: [get]/components/console-default/v1/feature_versions API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "versions": {
                        "additionalProp1": 0,
                        "additionalProp2": 0,
                        "additionalProp3": 0
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "infraConsoleFeatureVersions")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraConsoleGetFilteredStorageConfigGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetFilteredStorageConfig """
        """  path: [get]/components/console-default/v1/filtered_storage_config API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "filtered_storage_disable": false
                }

        """
        intef = collections.interface("viperOpenApi", "infraConsoleGetFilteredStorageConfig")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraConsoleUpdateFilteredStorageConfigPostApi(self, filtered_storage_disable=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  UpdateFilteredStorageConfig """
        """  path: [post]/components/console-default/v1/filtered_storage_config API """
        """  body: 
                {
                    "filtered_storage_disable": false
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraConsoleUpdateFilteredStorageConfig")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("filtered_storage_disable", filtered_storage_disable)
        return intef.request() if sendRequest else intef

    def infraConsoleGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/components/console-default/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "es_info": {},
                    "infra_buildtime": "",
                    "infra_version": "",
                    "product_mode": ""
                }

        """
        intef = collections.interface("viperOpenApi", "infraConsoleGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraConsoleStatisticsModuleGetApi(self, module_name, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  StatisticsModule """
        """  path: [get]/components/console-default/v1/statistics/modules/{module_name} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "module_metric_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraConsoleStatisticsModule")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("module_name", module_name)
        return intef.request() if sendRequest else intef

    def infraConsoleStatisticsModuleByCameraPostApi(self, module_name, camera_id=None, device_id=None, task_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  StatisticsModuleByCamera """
        """  path: [post]/components/console-default/v1/statistics/modules/{module_name}/camera API """
        """  body: 
                {
                    "camera_id": "",
                    "device_id": "",
                    "module_name": {},
                    "task_id": ""
                }
        """
        """  resp:
                200():
                {
                    "module_metric_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraConsoleStatisticsModuleByCamera")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("module_name", module_name)
        intef.update_body("camera_id", camera_id)
        intef.update_body("device_id", device_id)
        intef.update_body("module_name", module_name)
        intef.update_body("task_id", task_id)
        return intef.request() if sendRequest else intef

    def infraConsoleStatisticsNodeListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  StatisticsNodeList """
        """  path: [get]/components/console-default/v1/statistics/nodes API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "node_metric_infos": [
                        {
                            "ip": "",
                            "node_metrics": [
                                {
                                    "description": "",
                                    "name": "",
                                    "values": [
                                        {
                                            "timestamp": "",
                                            "value": 0
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraConsoleStatisticsNodeList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def infraConsoleAPIUserCredentialGetPostApi(self, username, password=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  APIUserCredentialGet """
        """  path: [post]/components/console-default/v1/user_credential/{username} API """
        """  body: 
                {
                    "password": "",
                    "username": ""
                }
        """
        """  resp:
                200():
                {
                    "data": [
                        {
                            "access_key": "",
                            "credential_name": "",
                            "secret_key": "",
                            "username": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "infraConsoleAPIUserCredentialGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("username", username)
        intef.update_body("password", password)
        intef.update_body("username", username)
        return intef.request() if sendRequest else intef

    def infraModelMgrBlobDownloadGetApi(self, blob_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BlobDownload """
        """  path: [get]/components/model-manager-default/v1/blobs/{blob_id} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                ""

        """
        intef = collections.interface("viperOpenApi", "infraModelMgrBlobDownload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("blob_id", blob_id)
        return intef.request() if sendRequest else intef

    def infraModelMgrBlobUploadPostApi(self, blob_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BlobUpload """
        """  path: [post]/components/model-manager-default/v1/blobs/{blob_id} API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                ""

        """
        intef = collections.interface("viperOpenApi", "infraModelMgrBlobUpload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("blob_id", blob_id)
        return intef.request() if sendRequest else intef

    def infraModelMgrGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/components/model-manager-default/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "storage": {},
                    "synchronized_at": ""
                }

        """
        intef = collections.interface("viperOpenApi", "infraModelMgrGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraModelMgrModelListGetApi(self, model_path_type=None, model_path_sub_type=None, model_path_runtime=None, model_path_hardware=None, model_path_name=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ModelList """
        """  path: [get]/components/model-manager-default/v1/models API """
        """  params: 
                参数名称：model_path.type　类型：string　描述：模型类型.
                参数名称：model_path.sub_type　类型：string　描述：模型子类型, 大小写字母,阿拉伯数字和下划线组合, 最长支持32个字符.
                参数名称：model_path.runtime　类型：string　描述：模型依赖软件运行时, 大小写字母, 阿拉伯数字和下划线组合, 最长支持32个字符.
                参数名称：model_path.hardware　类型：string　描述：模型依赖硬件型号, 大小写字母, 阿拉伯数字和下划线组合, 最长支持32个字符.
                参数名称：model_path.name　类型：string　描述：模型名称, 大小写字母, 阿拉伯数字和下划线组合, 最长支持127个字符
        """
        """  resp:
                200():
                {
                    "models": [
                        {
                            "checksum": "",
                            "created_at": "",
                            "description": "",
                            "model_path": {
                                "hardware": "",
                                "name": "",
                                "runtime": "",
                                "sub_type": "",
                                "type": {}
                            },
                            "oid": "",
                            "size": "",
                            "tags": [],
                            "user_meta": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "version": 0
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "infraModelMgrModelList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("model_path.type", model_path_type)
        intef.update_params("model_path.sub_type", model_path_sub_type)
        intef.update_params("model_path.runtime", model_path_runtime)
        intef.update_params("model_path.hardware", model_path_hardware)
        intef.update_params("model_path.name", model_path_name)
        return intef.request() if sendRequest else intef

    def infraModelMgrModelNewPostApi(self, model=None, overwrite=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ModelNew """
        """  path: [post]/components/model-manager-default/v1/models API """
        """  body: 
                {
                    "model": {},
                    "overwrite": false
                }
        """
        """  resp:
                200():
                {
                    "model": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraModelMgrModelNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("model", model)
        intef.update_body("overwrite", overwrite)
        return intef.request() if sendRequest else intef

    def infraModelMgrModelSynchronizePostApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ModelSynchronize """
        """  path: [post]/components/model-manager-default/v1/models/synchronize API """
        """  body: 
                {}
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraModelMgrModelSynchronize")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    # def infraModelMgrModelDeleteDeleteApi(self, path.type, path.sub_type, path.runtime, path.hardware, path.name, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  ModelDelete """
    #     """  path: [delete]/components/model-manager-default/v1/models/{path.type}/{path.sub_type}/{path.runtime}/{path.hardware}/{path.name} API """
    #     """  params:
    #
    #     """
    #     """  resp:
    #             200():
    #             {}
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "infraModelMgrModelDelete")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("path.type", path.type)
    #     intef.set_path_param("path.sub_type", path.sub_type)
    #     intef.set_path_param("path.runtime", path.runtime)
    #     intef.set_path_param("path.hardware", path.hardware)
    #     intef.set_path_param("path.name", path.name)
    #     return intef.request() if sendRequest else intef
    #
    # def infraModelMgrModelGetGetApi(self, path.type, path.sub_type, path.runtime, path.hardware, path.name, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  ModelGet """
    #     """  path: [get]/components/model-manager-default/v1/models/{path.type}/{path.sub_type}/{path.runtime}/{path.hardware}/{path.name} API """
    #     """  params:
    #
    #     """
    #     """  resp:
    #             200():
    #             {
    #                 "model": {},
    #                 "raw_meta": ""
    #             }
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "infraModelMgrModelGet")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("path.type", path.type)
    #     intef.set_path_param("path.sub_type", path.sub_type)
    #     intef.set_path_param("path.runtime", path.runtime)
    #     intef.set_path_param("path.hardware", path.hardware)
    #     intef.set_path_param("path.name", path.name)
    #     return intef.request() if sendRequest else intef

    def infraOSGDownloadObjectGetApi(self, bucket_name, object_key, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DownloadObject """
        """  path: [get]/components/osg-default/_/{bucket_name}/{object_key} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                ""

        """
        intef = collections.interface("viperOpenApi", "infraOSGDownloadObject")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("bucket_name", bucket_name)
        intef.set_path_param("object_key", object_key)
        return intef.request() if sendRequest else intef

    def infraOSGListBucketsGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListBuckets """
        """  path: [get]/components/osg-default/v1 API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "buckets": [
                        {
                            "creation_time": "",
                            "encryption_method": {},
                            "is_deleted": false,
                            "is_flattened": false,
                            "name": "",
                            "save_days": 0
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "infraOSGListBuckets")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraOSGCreateBucketPutApi(self, bucket_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CreateBucket """
        """  path: [put]/components/osg-default/v1 API """
        """  body: 
                {
                    "bucket_info": {}
                }
        """
        """  resp:
                200():
                {
                    "bucket_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraOSGCreateBucket")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bucket_info", bucket_info)
        return intef.request() if sendRequest else intef

    def infraOSGGetSystemInfoPostApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [post]/components/osg-default/v1/get_system_info API """
        """  body: 
                {}
        """
        """  resp:
                200():
                {
                    "bucket_summaries": [
                        {
                            "earliest_date": "",
                            "name": "",
                            "total_used_bytes": ""
                        }
                    ],
                    "nas_summaries": [
                        {
                            "path": "",
                            "slot": 0,
                            "total_bytes": "",
                            "total_used_bytes": ""
                        }
                    ],
                    "supported_encryption_methods": [
                        "[ENCRYPTION_METHOD_AES128]ENCRYPTION_METHOD_AES128/ENCRYPTION_METHOD_NONE"
                    ],
                    "total_bytes": "",
                    "total_used_bytes": ""
                }

        """
        intef = collections.interface("viperOpenApi", "infraOSGGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraOSGDeleteBucketDeleteApi(self, bucket_name, force=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteBucket """
        """  path: [delete]/components/osg-default/v1/{bucket_name} API """
        """  params: 
                参数名称：force　类型：boolean　描述：可选, True 表示可删除非空 bucket, False表示不可删除非空bucket
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraOSGDeleteBucket")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("force", force)
        intef.set_path_param("bucket_name", bucket_name)
        return intef.request() if sendRequest else intef

    def infraOSGListObjectsGetApi(self, bucket_name, date=None, marker=None, limit=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListObjects """
        """  path: [get]/components/osg-default/v1/{bucket_name} API """
        """  params: 
                参数名称：date　类型：string　描述：可选, 指定某一天查询, 格式为 '20171113'.
                参数名称：marker　类型：string　描述：可选, 表示查询起始位置, 可代入最后一次调用 `ListObjects` 范围的 `ListObjectsResponse.next_marker` 得到, 用于翻页功能.
                参数名称：limit　类型：integer　描述：请求对象个数, 范围: (0, 5000]
        """
        """  resp:
                200():
                {
                    "next_marker": "",
                    "object_info": [
                        {
                            "key": "",
                            "metadata": {}
                        }
                    ],
                    "truncated": false
                }

        """
        intef = collections.interface("viperOpenApi", "infraOSGListObjects")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("date", date)
        intef.update_params("marker", marker)
        intef.update_params("limit", limit)
        intef.set_path_param("bucket_name", bucket_name)
        return intef.request() if sendRequest else intef

    def infraOSGUpdateBucketPutApi(self, bucket_name, encryption_method=None, save_days=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  UpdateBucket """
        """  path: [put]/components/osg-default/v1/{bucket_name} API """
        """  body: 
                {
                    "bucket_name": "",
                    "encryption_method": "[ENCRYPTION_METHOD_AES128]ENCRYPTION_METHOD_AES128/ENCRYPTION_METHOD_NONE",
                    "save_days": 0
                }
        """
        """  resp:
                200():
                {
                    "bucket_name": "",
                    "encryption_method": "[ENCRYPTION_METHOD_AES128]ENCRYPTION_METHOD_AES128/ENCRYPTION_METHOD_NONE",
                    "save_days": 0
                }

        """
        intef = collections.interface("viperOpenApi", "infraOSGUpdateBucket")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("bucket_name", bucket_name)
        intef.update_body("bucket_name", bucket_name)
        intef.update_body("encryption_method", encryption_method)
        intef.update_body("save_days", save_days)
        return intef.request() if sendRequest else intef

    def infraOSGDeleteObjectsBeforeDatePostApi(self, bucket_name, date=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteObjectsBeforeDate """
        """  path: [post]/components/osg-default/v1/{bucket_name}/delete_before_date API """
        """  body: 
                {
                    "bucket_name": "",
                    "date": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraOSGDeleteObjectsBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("bucket_name", bucket_name)
        intef.update_body("bucket_name", bucket_name)
        intef.update_body("date", date)
        return intef.request() if sendRequest else intef

    def infraOSGDeleteObjectsByDatePostApi(self, bucket_name, date=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteObjectsByDate """
        """  path: [post]/components/osg-default/v1/{bucket_name}/delete_by_date API """
        """  body: 
                {
                    "bucket_name": "",
                    "date": ""
                }
        """
        """  resp:
                200():
                {
                    "deleted_objects": 0,
                    "deleted_total_size": ""
                }

        """
        intef = collections.interface("viperOpenApi", "infraOSGDeleteObjectsByDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("bucket_name", bucket_name)
        intef.update_body("bucket_name", bucket_name)
        intef.update_body("date", date)
        return intef.request() if sendRequest else intef

    def infraOSGPutObjectPostApi(self, bucket_name, blob=None, object_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PutObject """
        """  path: [post]/components/osg-default/v1/{bucket_name}/put_object API """
        """  body: 
                {
                    "blob": "",
                    "bucket_name": "",
                    "object_info": {}
                }
        """
        """  resp:
                200():
                {
                    "object_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraOSGPutObject")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("bucket_name", bucket_name)
        intef.update_body("blob", blob)
        intef.update_body("bucket_name", bucket_name)
        intef.update_body("object_info", object_info)
        return intef.request() if sendRequest else intef

    def infraOSGReserveObjectKeysPostApi(self, bucket_name, object_count=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ReserveObjectKeys """
        """  path: [post]/components/osg-default/v1/{bucket_name}/reserve_object_keys API """
        """  body: 
                {
                    "bucket_name": "",
                    "object_count": 0
                }
        """
        """  resp:
                200():
                {
                    "expiration_time": "",
                    "object_infos": [
                        {
                            "key": "",
                            "metadata": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "infraOSGReserveObjectKeys")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("bucket_name", bucket_name)
        intef.update_body("bucket_name", bucket_name)
        intef.update_body("object_count", object_count)
        return intef.request() if sendRequest else intef

    def infraOSGScanObjectsPostApi(self, bucket_name, date=None, limit=None, marker=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ScanObjects """
        """  path: [post]/components/osg-default/v1/{bucket_name}/scan_object API """
        """  body: 
                {
                    "bucket_name": "",
                    "date": "",
                    "limit": 0,
                    "marker": ""
                }
        """
        """  resp:
                200():
                {
                    "next_marker": "",
                    "objects": [
                        {
                            "blob": "",
                            "info": {}
                        }
                    ],
                    "truncated": false
                }

        """
        intef = collections.interface("viperOpenApi", "infraOSGScanObjects")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("bucket_name", bucket_name)
        intef.update_body("bucket_name", bucket_name)
        intef.update_body("date", date)
        intef.update_body("limit", limit)
        intef.update_body("marker", marker)
        return intef.request() if sendRequest else intef

    def infraOSGDeleteObjectDeleteApi(self, bucket_name, object_key, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteObject """
        """  path: [delete]/components/osg-default/v1/{bucket_name}/{object_key} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraOSGDeleteObject")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("bucket_name", bucket_name)
        intef.set_path_param("object_key", object_key)
        return intef.request() if sendRequest else intef

    def infraOSGGetObjectGetApi(self, bucket_name, object_key, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetObject """
        """  path: [get]/components/osg-default/v1/{bucket_name}/{object_key} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "blob": "",
                    "object_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraOSGGetObject")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("bucket_name", bucket_name)
        intef.set_path_param("object_key", object_key)
        return intef.request() if sendRequest else intef

    def infraRaidExporterGetRaidInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetRaidInfo """
        """  path: [get]/components/raid-exporter-default/v1/get_raid_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "nodes": {
                        "additionalProp1": {
                            "Controllers": [
                                {
                                    "Driver": "",
                                    "DriverVersion": "",
                                    "Eid": 0,
                                    "FwCache": 0,
                                    "Id": 0,
                                    "InterfaceSpeed": "",
                                    "InterfaceType": "",
                                    "JBODEnable": "",
                                    "Mode": "",
                                    "Model": "",
                                    "PhysicalDriveCount": 0,
                                    "RaidSupported": "",
                                    "SN": "",
                                    "Status": "",
                                    "VirtualDriveCount": 0,
                                    "VirtualDrives": [
                                        {
                                            "Access": "",
                                            "Boot": false,
                                            "Capacity": "",
                                            "DiskCache": "",
                                            "IOPolicy": "",
                                            "Id": 0,
                                            "PhysicalDrives": [
                                                {
                                                    "Attr": "",
                                                    "Capacity": "",
                                                    "Id": 0,
                                                    "Model": "",
                                                    "SN": "",
                                                    "Slot": 0,
                                                    "SmartStatus": false,
                                                    "State": ""
                                                }
                                            ],
                                            "Raid": "",
                                            "ReadCache": "",
                                            "State": "",
                                            "WriteCache": "",
                                            "name": ""
                                        }
                                    ],
                                    "WWN": ""
                                }
                            ],
                            "HostName": "",
                            "Ip": "",
                            "Ready": false
                        },
                        "additionalProp2": {
                            "Controllers": [
                                {
                                    "Driver": "",
                                    "DriverVersion": "",
                                    "Eid": 0,
                                    "FwCache": 0,
                                    "Id": 0,
                                    "InterfaceSpeed": "",
                                    "InterfaceType": "",
                                    "JBODEnable": "",
                                    "Mode": "",
                                    "Model": "",
                                    "PhysicalDriveCount": 0,
                                    "RaidSupported": "",
                                    "SN": "",
                                    "Status": "",
                                    "VirtualDriveCount": 0,
                                    "VirtualDrives": [
                                        {
                                            "Access": "",
                                            "Boot": false,
                                            "Capacity": "",
                                            "DiskCache": "",
                                            "IOPolicy": "",
                                            "Id": 0,
                                            "PhysicalDrives": [
                                                {
                                                    "Attr": "",
                                                    "Capacity": "",
                                                    "Id": 0,
                                                    "Model": "",
                                                    "SN": "",
                                                    "Slot": 0,
                                                    "SmartStatus": false,
                                                    "State": ""
                                                }
                                            ],
                                            "Raid": "",
                                            "ReadCache": "",
                                            "State": "",
                                            "WriteCache": "",
                                            "name": ""
                                        }
                                    ],
                                    "WWN": ""
                                }
                            ],
                            "HostName": "",
                            "Ip": "",
                            "Ready": false
                        },
                        "additionalProp3": {
                            "Controllers": [
                                {
                                    "Driver": "",
                                    "DriverVersion": "",
                                    "Eid": 0,
                                    "FwCache": 0,
                                    "Id": 0,
                                    "InterfaceSpeed": "",
                                    "InterfaceType": "",
                                    "JBODEnable": "",
                                    "Mode": "",
                                    "Model": "",
                                    "PhysicalDriveCount": 0,
                                    "RaidSupported": "",
                                    "SN": "",
                                    "Status": "",
                                    "VirtualDriveCount": 0,
                                    "VirtualDrives": [
                                        {
                                            "Access": "",
                                            "Boot": false,
                                            "Capacity": "",
                                            "DiskCache": "",
                                            "IOPolicy": "",
                                            "Id": 0,
                                            "PhysicalDrives": [
                                                {
                                                    "Attr": "",
                                                    "Capacity": "",
                                                    "Id": 0,
                                                    "Model": "",
                                                    "SN": "",
                                                    "Slot": 0,
                                                    "SmartStatus": false,
                                                    "State": ""
                                                }
                                            ],
                                            "Raid": "",
                                            "ReadCache": "",
                                            "State": "",
                                            "WriteCache": "",
                                            "name": ""
                                        }
                                    ],
                                    "WWN": ""
                                }
                            ],
                            "HostName": "",
                            "Ip": "",
                            "Ready": false
                        }
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "infraRaidExporterGetRaidInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrArtifactListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ArtifactList """
        """  path: [get]/components/spark-job-manager-default/v1/artifacts API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "artifacts": [
                        {
                            "created_at": "",
                            "file_size": "",
                            "modified_at": "",
                            "name": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrArtifactList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrArtifactDownloadGetApi(self, name, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ArtifactDownload """
        """  path: [get]/components/spark-job-manager-default/v1/artifacts/_/{name} API """
        """  params: 

        """
        """  resp:
                200(A successful response.):
                ""

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrArtifactDownload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("name", name)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrArtifactUploadPostApi(self, name, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ArtifactUpload """
        """  path: [post]/components/spark-job-manager-default/v1/artifacts/_/{name} API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                ""

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrArtifactUpload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("name", name)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrArtifactDeleteDeleteApi(self, name, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ArtifactDelete """
        """  path: [delete]/components/spark-job-manager-default/v1/artifacts/{name} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrArtifactDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("name", name)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrArtifactGetGetApi(self, name, return_content=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ArtifactGet """
        """  path: [get]/components/spark-job-manager-default/v1/artifacts/{name} API """
        """  params: 
                参数名称：return_content　类型：boolean　描述：nul
        """
        """  resp:
                200():
                {
                    "artifact": {},
                    "content": ""
                }

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrArtifactGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("return_content", return_content)
        intef.set_path_param("name", name)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrArtifactNewPostApi(self, name, allow_overwrite=None, blob=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ArtifactNew """
        """  path: [post]/components/spark-job-manager-default/v1/artifacts/{name} API """
        """  body: 
                {
                    "allow_overwrite": false,
                    "blob": "",
                    "name": ""
                }
        """
        """  resp:
                200():
                {
                    "artifact": {
                        "created_at": "",
                        "file_size": "",
                        "modified_at": "",
                        "name": ""
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrArtifactNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("name", name)
        intef.update_body("allow_overwrite", allow_overwrite)
        intef.update_body("blob", blob)
        intef.update_body("name", name)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrJobListGetApi(self, page_offset=None, page_limit=None, page_total=None, catalog=None, period_start=None, period_end=None, status=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobList """
        """  path: [get]/components/spark-job-manager-default/v1/jobs API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
                参数名称：catalog　类型：string　描述：可选, 如不为空, 则只列出指定类型的任务.
                参数名称：period.start　类型：string　描述：开始时间, 区间包含.
                参数名称：period.end　类型：string　描述：结束时间, 区间不包含.
                参数名称：status　类型：array　描述：可选, 过滤状态
        """
        """  resp:
                200():
                {
                    "jobs": [
                        {
                            "canceled_at": "",
                            "catalog": "",
                            "confs": [],
                            "created_at": "",
                            "deleted_at": "",
                            "environments": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "files": [],
                            "finished_at": "",
                            "id": "",
                            "jars": [],
                            "job_priority": {},
                            "job_type": {},
                            "language": "[PYTHON]PYTHON/JAVA",
                            "main_class": "",
                            "name": "",
                            "packages": [],
                            "parameters": "",
                            "py_files": [],
                            "result": {},
                            "timeout": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrJobList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.update_params("catalog", catalog)
        intef.update_params("period.start", period_start)
        intef.update_params("period.end", period_end)
        intef.update_params("status", status)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrJobNewPostApi(self, job=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobNew """
        """  path: [post]/components/spark-job-manager-default/v1/jobs API """
        """  body: 
                {
                    "job": {
                        "canceled_at": "",
                        "catalog": "",
                        "confs": [],
                        "created_at": "",
                        "deleted_at": "",
                        "environments": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        },
                        "files": [],
                        "finished_at": "",
                        "id": "",
                        "jars": [],
                        "job_priority": {},
                        "job_type": {},
                        "language": "[PYTHON]PYTHON/JAVA",
                        "main_class": "",
                        "name": "",
                        "packages": [],
                        "parameters": "",
                        "py_files": [],
                        "result": {},
                        "timeout": ""
                    }
                }
        """
        """  resp:
                200():
                {
                    "job_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrJobNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("job", job)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrJobDeleteDeleteApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobDelete """
        """  path: [delete]/components/spark-job-manager-default/v1/jobs/{job_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrJobDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrJobGetGetApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobGet """
        """  path: [get]/components/spark-job-manager-default/v1/jobs/{job_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "job": {}
                }

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrJobGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def infraSparkJobMgrJobCancelPostApi(self, job_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  JobCancel """
        """  path: [post]/components/spark-job-manager-default/v1/jobs/{job_id}/cancel API """
        """  body: 
                {}
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraSparkJobMgrJobCancel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("job_id", job_id)
        return intef.request() if sendRequest else intef

    def infraStorageMgrNamespaceListGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  NamespaceList """
        """  path: [get]/components/storage-manager-default/v1/namespaces API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "ns_ids": []
                }

        """
        intef = collections.interface("viperOpenApi", "infraStorageMgrNamespaceList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraStorageMgrNamespaceDeleteDeleteApi(self, ns_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  NamespaceDelete """
        """  path: [delete]/components/storage-manager-default/v1/namespaces/{ns_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraStorageMgrNamespaceDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("ns_id", ns_id)
        return intef.request() if sendRequest else intef

    def infraStorageMgrNamespaceNewPostApi(self, ns_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  NamespaceNew """
        """  path: [post]/components/storage-manager-default/v1/namespaces/{ns_id} API """
        """  body: 
                {
                    "ns_id": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraStorageMgrNamespaceNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("ns_id", ns_id)
        intef.update_body("ns_id", ns_id)
        return intef.request() if sendRequest else intef

    def infraStorageMgrOSGStorageGetGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  OSGStorageGet """
        """  path: [get]/components/storage-manager-default/v1/osg_storage API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "local_storage": {},
                    "mode": {},
                    "nas_overall_usage_in_gb_threshold": 0,
                    "nas_storages": [
                        {
                            "capacity": "",
                            "error_message": "",
                            "slot": 0,
                            "status": {},
                            "url": "",
                            "usage": ""
                        }
                    ],
                    "osg_status": {},
                    "status_crash_message": ""
                }

        """
        intef = collections.interface("viperOpenApi", "infraStorageMgrOSGStorageGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraStorageMgrOSGStorageReplacePutApi(self, force=None, mode=None, nas_infos=None, nas_overall_usage_in_gb_threshold=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  OSGStorageReplace """
        """  path: [put]/components/storage-manager-default/v1/osg_storage API """
        """  body: 
                {
                    "force": false,
                    "mode": {},
                    "nas_infos": [
                        {
                            "offline": false,
                            "slot": 0,
                            "url": ""
                        }
                    ],
                    "nas_overall_usage_in_gb_threshold": 0
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraStorageMgrOSGStorageReplace")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("force", force)
        intef.update_body("mode", mode)
        intef.update_body("nas_infos", nas_infos)
        intef.update_body("nas_overall_usage_in_gb_threshold", nas_overall_usage_in_gb_threshold)
        return intef.request() if sendRequest else intef

    def infraStorageMgrStorageProtectPolicyGetGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  StorageProtectPolicyGet """
        """  path: [get]/components/storage-manager-default/v1/storage_protect_policy API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "policy": "[POLICY_RETENTION]POLICY_RETENTION/POLICY_HIBERNATION"
                }

        """
        intef = collections.interface("viperOpenApi", "infraStorageMgrStorageProtectPolicyGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraStorageMgrStorageProtectPolicyReplacePutApi(self, policy=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  StorageProtectPolicyReplace """
        """  path: [put]/components/storage-manager-default/v1/storage_protect_policy API """
        """  body: 
                {
                    "policy": "[POLICY_RETENTION]POLICY_RETENTION/POLICY_HIBERNATION"
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraStorageMgrStorageProtectPolicyReplace")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("policy", policy)
        return intef.request() if sendRequest else intef

    def infraStorageMgrStorageRuleListGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  StorageRuleList """
        """  path: [get]/components/storage-manager-default/v1/storage_rules API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "rules": [
                        {
                            "cascade": false,
                            "retention_days": 0,
                            "storage_target": {},
                            "watermark": 0
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "infraStorageMgrStorageRuleList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def infraStorageMgrStorageRuleReplacePutApi(self, rule=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  StorageRuleReplace """
        """  path: [put]/components/storage-manager-default/v1/storage_rules API """
        """  body: 
                {
                    "rule": {
                        "cascade": false,
                        "retention_days": 0,
                        "storage_target": {},
                        "watermark": 0
                    }
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "infraStorageMgrStorageRuleReplace")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("rule", rule)
        return intef.request() if sendRequest else intef

    def algoStoreAppTemplateListGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppTemplateList """
        """  path: [get]/engine/algo-store/v1/app_templates API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "templates": [
                        {
                            "algo_type": {},
                            "id": "",
                            "models": {},
                            "name": "",
                            "template_path": "",
                            "version": 0
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppTemplateList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def algoStoreAppTemplateNewPostApi(self, template=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppTemplateNew """
        """  path: [post]/engine/algo-store/v1/app_templates API """
        """  body: 
                {
                    "template": {}
                }
        """
        """  resp:
                200():
                {
                    "template_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppTemplateNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("template", template)
        return intef.request() if sendRequest else intef

    def algoStoreAppTemplateDeleteDeleteApi(self, template_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppTemplateDelete """
        """  path: [delete]/engine/algo-store/v1/app_templates/{template_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppTemplateDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("template_id", template_id)
        return intef.request() if sendRequest else intef

    def algoStoreAppListGetApi(self, filters_period_start=None, filters_period_end=None, filters_user_algo_name=None, filters_algo_types=None, filters_tag_ids=None, filters_status=None, filters_sale_type=None, page_offset=None, page_limit=None, page_total=None, reversed=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppList """
        """  path: [get]/engine/algo-store/v1/apps API """
        """  params: 
                参数名称：filters.period.start　类型：string　描述：开始时间, 区间包含.
                参数名称：filters.period.end　类型：string　描述：结束时间, 区间不包含.
                参数名称：filters.user_algo_name　类型：string　描述：用户定义算法应用名称.
                参数名称：filters.algo_types　类型：array　描述：算法应用类型(或解析处理类型).
                参数名称：filters.tag_ids　类型：array　描述：按算法标签过滤.
                参数名称：filters.status　类型：array　描述：根据授权状态过滤, 默认为空，不过滤.
                参数名称：filters.sale_type　类型：string　描述：根据售卖类别过滤.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
                参数名称：reversed　类型：boolean　描述：是否按创建时间逆序排列, 默认为false
        """
        """  resp:
                200():
                {
                    "app_metas": [
                        {
                            "algo_type": {},
                            "app_id": "",
                            "author": "",
                            "created_at": "",
                            "description": "",
                            "display_name": "",
                            "expired_at": "",
                            "icon": {},
                            "sale_type": {},
                            "status": {},
                            "tags": [
                                {
                                    "description": "",
                                    "id": "",
                                    "name": ""
                                }
                            ],
                            "user_algo_name": "",
                            "version": 0
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("filters.period.start", filters_period_start)
        intef.update_params("filters.period.end", filters_period_end)
        intef.update_params("filters.user_algo_name", filters_user_algo_name)
        intef.update_params("filters.algo_types", filters_algo_types)
        intef.update_params("filters.tag_ids", filters_tag_ids)
        intef.update_params("filters.status", filters_status)
        intef.update_params("filters.sale_type", filters_sale_type)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.update_params("reversed", reversed)
        return intef.request() if sendRequest else intef

    def algoStoreAppNewFromTemplatePostApi(self, meta=None, models=None, process_configs=None, template_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppNewFromTemplate """
        """  path: [post]/engine/algo-store/v1/apps/new_from_template API """
        """  body: 
                {
                    "meta": {},
                    "models": {},
                    "process_configs": [
                        {
                            "config_spec": {},
                            "hardware": ""
                        }
                    ],
                    "template_id": ""
                }
        """
        """  resp:
                200():
                {
                    "app_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppNewFromTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("meta", meta)
        intef.update_body("models", models)
        intef.update_body("process_configs", process_configs)
        intef.update_body("template_id", template_id)
        return intef.request() if sendRequest else intef

    def algoStoreAppUploadPostApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppUpload """
        """  path: [post]/engine/algo-store/v1/apps/upload API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                "Not Support allOf"

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppUpload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def algoStoreAppDeleteDeleteApi(self, app_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppDelete """
        """  path: [delete]/engine/algo-store/v1/apps/{app_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("app_id", app_id)
        return intef.request() if sendRequest else intef

    def algoStoreAppGetGetApi(self, app_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppGet """
        """  path: [get]/engine/algo-store/v1/apps/{app_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "algo_app": {}
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("app_id", app_id)
        return intef.request() if sendRequest else intef

    def algoStoreAppUpdatePatchApi(self, app_id, tag_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppUpdate """
        """  path: [patch]/engine/algo-store/v1/apps/{app_id} API """
        """  body: 
                {
                    "app_id": "",
                    "tag_ids": []
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("app_id", app_id)
        intef.update_body("app_id", app_id)
        intef.update_body("tag_ids", tag_ids)
        return intef.request() if sendRequest else intef

    def algoStoreAppInstanceNewPostApi(self, app_id, user_configs=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppInstanceNew """
        """  path: [post]/engine/algo-store/v1/apps/{app_id}/instances API """
        """  body: 
                {
                    "app_id": "",
                    "user_configs": {}
                }
        """
        """  resp:
                200():
                {
                    "instance_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppInstanceNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("app_id", app_id)
        intef.update_body("app_id", app_id)
        intef.update_body("user_configs", user_configs)
        return intef.request() if sendRequest else intef

    def algoStoreAppInstanceDeleteDeleteApi(self, app_id, instance_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppInstanceDelete """
        """  path: [delete]/engine/algo-store/v1/apps/{app_id}/instances/{instance_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppInstanceDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("app_id", app_id)
        intef.set_path_param("instance_id", instance_id)
        return intef.request() if sendRequest else intef

    def algoStoreAppInstanceGetGetApi(self, app_id, instance_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppInstanceGet """
        """  path: [get]/engine/algo-store/v1/apps/{app_id}/instances/{instance_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "instance_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppInstanceGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("app_id", app_id)
        intef.set_path_param("instance_id", instance_id)
        return intef.request() if sendRequest else intef

    def algoStoreAppInstanceUpdatePatchApi(self, app_id, instance_id, hardware=None, replicas=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppInstanceUpdate """
        """  path: [patch]/engine/algo-store/v1/apps/{app_id}/instances/{instance_id} API """
        """  body: 
                {
                    "app_id": "",
                    "hardware": "",
                    "instance_id": "",
                    "replicas": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppInstanceUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("app_id", app_id)
        intef.set_path_param("instance_id", instance_id)
        intef.update_body("app_id", app_id)
        intef.update_body("hardware", hardware)
        intef.update_body("instance_id", instance_id)
        intef.update_body("replicas", replicas)
        return intef.request() if sendRequest else intef

    def algoStoreAppGetByNameVersionGetApi(self, user_algo_name, version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppGetByNameVersion """
        """  path: [get]/engine/algo-store/v1/apps/{user_algo_name}/{version} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "algo_app": {}
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreAppGetByNameVersion")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("user_algo_name", user_algo_name)
        intef.set_path_param("version", version)
        return intef.request() if sendRequest else intef

    def algoStoreDocDownloadGetApi(self, user_algo_name, version, doc_name, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DocDownload """
        """  path: [get]/engine/algo-store/v1/apps/{user_algo_name}/{version}/doc/{doc_name} API """
        """  params: 

        """
        """  resp:
                200(OK):
                ""

        """
        intef = collections.interface("viperOpenApi", "algoStoreDocDownload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("user_algo_name", user_algo_name)
        intef.set_path_param("version", version)
        intef.set_path_param("doc_name", doc_name)
        return intef.request() if sendRequest else intef

    def algoStoreInstanceListByNameVersionGetApi(self, user_algo_name, version, reversed=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  InstanceListByNameVersion """
        """  path: [get]/engine/algo-store/v1/apps/{user_algo_name}/{version}/instances API """
        """  params: 
                参数名称：reversed　类型：boolean　描述：按创建时间逆序排列, 默认为false: 不做逆序排列.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "instances": [
                        {
                            "algo_type": {},
                            "app_id": "",
                            "created_at": "",
                            "display_name": "",
                            "endpoint": "",
                            "error_info": "",
                            "id": "",
                            "load": {},
                            "state": {},
                            "user_algo_name": "",
                            "user_configs": {},
                            "version": 0,
                            "workers": [
                                {
                                    "hardware": "",
                                    "message": "",
                                    "name": "",
                                    "restart_count": 0,
                                    "status": ""
                                }
                            ]
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreInstanceListByNameVersion")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("reversed", reversed)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("user_algo_name", user_algo_name)
        intef.set_path_param("version", version)
        return intef.request() if sendRequest else intef

    def algoStoreEdgeInstanceListGetApi(self, app_id=None, device_id=None, algo_types=None, states=None, period_start=None, period_end=None, reversed=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  EdgeInstanceList """
        """  path: [get]/engine/algo-store/v1/edge_instances API """
        """  params: 
                参数名称：app_id　类型：string　描述：算法应用标识, 默认为空，则不对APP过滤.
                参数名称：device_id　类型：string　描述：算法应用实例所在边侧设备的ID, 默认为空，则不对设备过滤.
                参数名称：algo_types　类型：array　描述：按算法类型过滤, 默认空, 则不对算法类型过滤.
                参数名称：states　类型：array　描述：算法运行状态, 默认为空, 不对状态过滤.
                参数名称：period.start　类型：string　描述：开始时间, 区间包含.
                参数名称：period.end　类型：string　描述：结束时间, 区间不包含.
                参数名称：reversed　类型：boolean　描述：按创建时间逆序排列, 默认为false: 不做逆序排列.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "instances": [
                        {
                            "algo_type": {},
                            "app_id": "",
                            "created_at": "",
                            "device_id": "",
                            "display_name": "",
                            "error_info": "",
                            "registry_id": "",
                            "state": {},
                            "user_algo_name": "",
                            "user_configs": {},
                            "uuid": "",
                            "version": 0
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreEdgeInstanceList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("app_id", app_id)
        intef.update_params("device_id", device_id)
        intef.update_params("algo_types", algo_types)
        intef.update_params("states", states)
        intef.update_params("period.start", period_start)
        intef.update_params("period.end", period_end)
        intef.update_params("reversed", reversed)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def algoStoreEdgeInstanceNewPostApi(self, app_id=None, device_id=None, registry_id=None, user_configs=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  EdgeInstanceNew """
        """  path: [post]/engine/algo-store/v1/edge_instances API """
        """  body: 
                {
                    "app_id": "",
                    "device_id": "",
                    "registry_id": "",
                    "user_configs": {}
                }
        """
        """  resp:
                200():
                {
                    "instance_uuid": ""
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreEdgeInstanceNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("app_id", app_id)
        intef.update_body("device_id", device_id)
        intef.update_body("registry_id", registry_id)
        intef.update_body("user_configs", user_configs)
        return intef.request() if sendRequest else intef

    def algoStoreEdgeInstanceDeleteDeleteApi(self, instance_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  EdgeInstanceDelete """
        """  path: [delete]/engine/algo-store/v1/edge_instances/{instance_uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "algoStoreEdgeInstanceDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("instance_uuid", instance_uuid)
        return intef.request() if sendRequest else intef

    def algoStoreEdgeInstanceGetGetApi(self, instance_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  EdgeInstanceGet """
        """  path: [get]/engine/algo-store/v1/edge_instances/{instance_uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "instance_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreEdgeInstanceGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("instance_uuid", instance_uuid)
        return intef.request() if sendRequest else intef

    def algoStoreEdgeInstanceUpdatePatchApi(self, instance_uuid, user_configs=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  EdgeInstanceUpdate """
        """  path: [patch]/engine/algo-store/v1/edge_instances/{instance_uuid} API """
        """  body: 
                {
                    "instance_uuid": "",
                    "user_configs": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "algoStoreEdgeInstanceUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("instance_uuid", instance_uuid)
        intef.update_body("instance_uuid", instance_uuid)
        intef.update_body("user_configs", user_configs)
        return intef.request() if sendRequest else intef

    def algoStoreGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/algo-store/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "group_resources": [
                        {
                            "group_id": "",
                            "resources": {
                                "additionalProp1": {
                                    "available": "",
                                    "total": "",
                                    "used": ""
                                },
                                "additionalProp2": {
                                    "available": "",
                                    "total": "",
                                    "used": ""
                                },
                                "additionalProp3": {
                                    "available": "",
                                    "total": "",
                                    "used": ""
                                }
                            },
                            "worker_limit": 0
                        }
                    ],
                    "ips_resources": {
                        "additionalProp1": {
                            "available": "",
                            "total": "",
                            "used": ""
                        },
                        "additionalProp2": {
                            "available": "",
                            "total": "",
                            "used": ""
                        },
                        "additionalProp3": {
                            "available": "",
                            "total": "",
                            "used": ""
                        }
                    },
                    "vps_resources": {
                        "additionalProp1": {
                            "available": "",
                            "total": "",
                            "used": ""
                        },
                        "additionalProp2": {
                            "available": "",
                            "total": "",
                            "used": ""
                        },
                        "additionalProp3": {
                            "available": "",
                            "total": "",
                            "used": ""
                        }
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def algoStoreInstanceListGetApi(self, filters_algo_types=None, filters_states=None, filters_period_start=None, filters_period_end=None, reversed=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  InstanceList """
        """  path: [get]/engine/algo-store/v1/instances API """
        """  params: 
                参数名称：filters.algo_types　类型：array　描述：按算法类型过滤, 默认空, 则不对算法类型过滤.
                参数名称：filters.states　类型：array　描述：算法运行状态, 默认为空, 不对状态过滤.
                参数名称：filters.period.start　类型：string　描述：开始时间, 区间包含.
                参数名称：filters.period.end　类型：string　描述：结束时间, 区间不包含.
                参数名称：reversed　类型：boolean　描述：按创建时间逆序排列, 默认为false: 不做逆序排列.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "instances": [
                        {
                            "algo_type": {},
                            "app_id": "",
                            "created_at": "",
                            "display_name": "",
                            "endpoint": "",
                            "error_info": "",
                            "id": "",
                            "load": {},
                            "state": {},
                            "user_algo_name": "",
                            "user_configs": {},
                            "version": 0,
                            "workers": [
                                {
                                    "hardware": "",
                                    "message": "",
                                    "name": "",
                                    "restart_count": 0,
                                    "status": ""
                                }
                            ]
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreInstanceList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("filters.algo_types", filters_algo_types)
        intef.update_params("filters.states", filters_states)
        intef.update_params("filters.period.start", filters_period_start)
        intef.update_params("filters.period.end", filters_period_end)
        intef.update_params("reversed", reversed)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def algoStoreReallocateResourcePostApi(self, group_resource_quotas=None, ips_resource_quotas=None, vps_resource_quotas=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ReallocateResource """
        """  path: [post]/engine/algo-store/v1/reallocate_resource API """
        """  body: 
                {
                    "group_resource_quotas": [
                        {
                            "group_id": "",
                            "group_quotas": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            }
                        }
                    ],
                    "ips_resource_quotas": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    },
                    "vps_resource_quotas": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    }
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "algoStoreReallocateResource")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("group_resource_quotas", group_resource_quotas)
        intef.update_body("ips_resource_quotas", ips_resource_quotas)
        intef.update_body("vps_resource_quotas", vps_resource_quotas)
        return intef.request() if sendRequest else intef

    def algoStoreTagListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TagList """
        """  path: [get]/engine/algo-store/v1/tags API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "tags": [
                        {
                            "description": "",
                            "id": "",
                            "name": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreTagList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def algoStoreTagNewPostApi(self, tag=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TagNew """
        """  path: [post]/engine/algo-store/v1/tags API """
        """  body: 
                {
                    "tag": {}
                }
        """
        """  resp:
                200():
                {
                    "tag_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "algoStoreTagNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("tag", tag)
        return intef.request() if sendRequest else intef

    def algoStoreTagDeleteDeleteApi(self, tag_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TagDelete """
        """  path: [delete]/engine/algo-store/v1/tags/{tag_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "algoStoreTagDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("tag_id", tag_id)
        return intef.request() if sendRequest else intef

    def searchWrapperBatchComparePostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchCompare """
        """  path: [post]/engine/api-wrapper/v1/batch_compare API """
        """  body: 
                {
                    "requests": [
                        {
                            "compare_pairs": [
                                {
                                    "one": {},
                                    "other": {},
                                    "weight": 0
                                }
                            ],
                            "mode": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ],
                    "scores": []
                }

        """
        intef = collections.interface("viperOpenApi", "searchWrapperBatchCompare")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def searchWrapperBatchCompareByImagePostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchCompareByImage """
        """  path: [post]/engine/api-wrapper/v1/batch_compare_by_image API """
        """  body: 
                {
                    "requests": [
                        {
                            "compare_config": [
                                {
                                    "carplate_text": {},
                                    "feature": {},
                                    "weight": 0
                                }
                            ],
                            "mode": {},
                            "one": {},
                            "other": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ],
                    "scores": []
                }

        """
        intef = collections.interface("viperOpenApi", "searchWrapperBatchCompareByImage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def apiWrapperBatchAddImageToDBPostApi(self, auto_rotation=None, db_id=None, extra_db_type=None, images=None, save_images=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchAddImageToDB """
        """  path: [post]/engine/api-wrapper/v1/face/batch_add_image_to_db API """
        """  body: 
                {
                    "auto_rotation": false,
                    "db_id": "",
                    "extra_db_type": "",
                    "images": [
                        {
                            "extra_info": "",
                            "image": {
                                "bounding": {},
                                "face_selection": {},
                                "image": {}
                            },
                            "key": "",
                            "quality_threshold": 0
                        }
                    ],
                    "save_images": false,
                    "type": "[STATIC_FEATURE_DB]STATIC_FEATURE_DB/ALERT_FEATURE_DB/IDENTIFICATION_FEATURE_DB/EXTRA_FEATURE_DB"
                }
        """
        """  resp:
                200():
                {
                    "items": [
                        {
                            "face_info": {
                                "algo": {},
                                "associations": [
                                    {
                                        "associated_object_info": {},
                                        "association_type": "",
                                        "object_id": "",
                                        "type": {}
                                    }
                                ],
                                "automobile": {},
                                "carplate": {},
                                "crowd": {},
                                "cyclist": {},
                                "diagnosis": {},
                                "event": {},
                                "face": {},
                                "human_powered_vehicle": {},
                                "object_id": "",
                                "other": {},
                                "pedestrian": {},
                                "portrait_image_location": {},
                                "trajectory": {},
                                "type": {},
                                "watercraft": {}
                            },
                            "feature_id": "",
                            "image_url": "",
                            "orientation_type": {}
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "apiWrapperBatchAddImageToDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("auto_rotation", auto_rotation)
        intef.update_body("db_id", db_id)
        intef.update_body("extra_db_type", extra_db_type)
        intef.update_body("images", images)
        intef.update_body("save_images", save_images)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def apiWrapperCompareImageInDBPostApi(self, db_id=None, extra_db_type=None, feature_id=None, image=None, key=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CompareImageInDB """
        """  path: [post]/engine/api-wrapper/v1/face/compare_image_in_db API """
        """  body: 
                {
                    "db_id": "",
                    "extra_db_type": "",
                    "feature_id": "",
                    "image": {
                        "bounding": {},
                        "face_selection": {},
                        "image": {}
                    },
                    "key": "",
                    "type": "[STATIC_FEATURE_DB]STATIC_FEATURE_DB/ALERT_FEATURE_DB/IDENTIFICATION_FEATURE_DB/EXTRA_FEATURE_DB"
                }
        """
        """  resp:
                200():
                {
                    "compare_results": [
                        {
                            "db_face_info": {
                                "algo": {},
                                "associations": [
                                    {
                                        "associated_object_info": {},
                                        "association_type": "",
                                        "object_id": "",
                                        "type": {}
                                    }
                                ],
                                "automobile": {},
                                "carplate": {},
                                "crowd": {},
                                "cyclist": {},
                                "diagnosis": {},
                                "event": {},
                                "face": {},
                                "human_powered_vehicle": {},
                                "object_id": "",
                                "other": {},
                                "pedestrian": {},
                                "portrait_image_location": {},
                                "trajectory": {},
                                "type": {},
                                "watercraft": {}
                            },
                            "feature_id": "",
                            "key": "",
                            "score": 0
                        }
                    ],
                    "query_face_info": {
                        "algo": {},
                        "associations": [
                            {
                                "associated_object_info": {},
                                "association_type": "",
                                "object_id": "",
                                "type": {}
                            }
                        ],
                        "automobile": {},
                        "carplate": {},
                        "crowd": {},
                        "cyclist": {},
                        "diagnosis": {},
                        "event": {},
                        "face": {},
                        "human_powered_vehicle": {},
                        "object_id": "",
                        "other": {},
                        "pedestrian": {},
                        "portrait_image_location": {},
                        "trajectory": {},
                        "type": {},
                        "watercraft": {}
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "apiWrapperCompareImageInDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("extra_db_type", extra_db_type)
        intef.update_body("feature_id", feature_id)
        intef.update_body("image", image)
        intef.update_body("key", key)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def apiWrapperCompareOneToOnePostApi(self, feature_version=None, one=None, other=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CompareOneToOne """
        """  path: [post]/engine/api-wrapper/v1/face/compare_one_to_one API """
        """  body: 
                {
                    "feature_version": 0,
                    "one": {
                        "bounding": {},
                        "face_selection": {},
                        "image": {}
                    },
                    "other": {
                        "bounding": {},
                        "face_selection": {},
                        "image": {}
                    }
                }
        """
        """  resp:
                200():
                {
                    "one": {
                        "algo": {},
                        "associations": [
                            {
                                "associated_object_info": {},
                                "association_type": "",
                                "object_id": "",
                                "type": {}
                            }
                        ],
                        "automobile": {},
                        "carplate": {},
                        "crowd": {},
                        "cyclist": {},
                        "diagnosis": {},
                        "event": {},
                        "face": {},
                        "human_powered_vehicle": {},
                        "object_id": "",
                        "other": {},
                        "pedestrian": {},
                        "portrait_image_location": {},
                        "trajectory": {},
                        "type": {},
                        "watercraft": {}
                    },
                    "other": {
                        "algo": {},
                        "associations": [
                            {
                                "associated_object_info": {},
                                "association_type": "",
                                "object_id": "",
                                "type": {}
                            }
                        ],
                        "automobile": {},
                        "carplate": {},
                        "crowd": {},
                        "cyclist": {},
                        "diagnosis": {},
                        "event": {},
                        "face": {},
                        "human_powered_vehicle": {},
                        "object_id": "",
                        "other": {},
                        "pedestrian": {},
                        "portrait_image_location": {},
                        "trajectory": {},
                        "type": {},
                        "watercraft": {}
                    },
                    "score": 0
                }

        """
        intef = collections.interface("viperOpenApi", "apiWrapperCompareOneToOne")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("feature_version", feature_version)
        intef.update_body("one", one)
        intef.update_body("other", other)
        return intef.request() if sendRequest else intef

    def apiWrapperDeleteDBPostApi(self, db_id=None, delete_bucket=None, extra_db_type=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteDB """
        """  path: [post]/engine/api-wrapper/v1/face/delete_db API """
        """  body: 
                {
                    "db_id": "",
                    "delete_bucket": false,
                    "extra_db_type": "",
                    "type": "[STATIC_FEATURE_DB]STATIC_FEATURE_DB/ALERT_FEATURE_DB/IDENTIFICATION_FEATURE_DB/EXTRA_FEATURE_DB"
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "apiWrapperDeleteDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("delete_bucket", delete_bucket)
        intef.update_body("extra_db_type", extra_db_type)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def apiWrapperDeleteImageFromDBPostApi(self, db_id=None, delete_image=None, extra_db_type=None, feature_id=None, key=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteImageFromDB """
        """  path: [post]/engine/api-wrapper/v1/face/delete_image_from_db API """
        """  body: 
                {
                    "db_id": "",
                    "delete_image": false,
                    "extra_db_type": "",
                    "feature_id": "",
                    "key": "",
                    "type": "[STATIC_FEATURE_DB]STATIC_FEATURE_DB/ALERT_FEATURE_DB/IDENTIFICATION_FEATURE_DB/EXTRA_FEATURE_DB"
                }
        """
        """  resp:
                200():
                {
                    "items": [
                        {
                            "feature_id": "",
                            "image_url": ""
                        }
                    ],
                    "key": "",
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "apiWrapperDeleteImageFromDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("db_id", db_id)
        intef.update_body("delete_image", delete_image)
        intef.update_body("extra_db_type", extra_db_type)
        intef.update_body("feature_id", feature_id)
        intef.update_body("key", key)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def apiWrapperDetectAndExtractPostApi(self, feature_version=None, image=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DetectAndExtract """
        """  path: [post]/engine/api-wrapper/v1/face/detect_and_extract API """
        """  body: 
                {
                    "feature_version": 0,
                    "image": {
                        "auto_rotation_thresh": 0,
                        "face_selection": {},
                        "image": {}
                    }
                }
        """
        """  resp:
                200():
                {
                    "annotation": {
                        "algo": {},
                        "associations": [
                            {
                                "associated_object_info": {},
                                "association_type": "",
                                "object_id": "",
                                "type": {}
                            }
                        ],
                        "automobile": {},
                        "carplate": {},
                        "crowd": {},
                        "cyclist": {},
                        "diagnosis": {},
                        "event": {},
                        "face": {},
                        "human_powered_vehicle": {},
                        "object_id": "",
                        "other": {},
                        "pedestrian": {},
                        "portrait_image_location": {},
                        "trajectory": {},
                        "type": {},
                        "watercraft": {}
                    },
                    "feature": {
                        "blob": "",
                        "type": "",
                        "version": 0
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "apiWrapperDetectAndExtract")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("feature_version", feature_version)
        intef.update_body("image", image)
        return intef.request() if sendRequest else intef

    def apiWrapperGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/api-wrapper/v1/face/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "max_add_image_to_db_batch_size": 0,
                    "max_dbs_per_query": 0
                }

        """
        intef = collections.interface("viperOpenApi", "apiWrapperGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def apiWrapperNewDBPostApi(self, bucket_encrypt=None, bucket_flattened=None, create_bucket=None, db_size=None, description=None, enable_isolated_feature_table=None, extra_db_type=None, feature_version=None, name=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  NewDB """
        """  path: [post]/engine/api-wrapper/v1/face/new_db API """
        """  body: 
                {
                    "bucket_encrypt": false,
                    "bucket_flattened": false,
                    "create_bucket": false,
                    "db_size": "",
                    "description": "",
                    "enable_isolated_feature_table": false,
                    "extra_db_type": "",
                    "feature_version": 0,
                    "name": "",
                    "type": "[STATIC_FEATURE_DB]STATIC_FEATURE_DB/ALERT_FEATURE_DB/IDENTIFICATION_FEATURE_DB/EXTRA_FEATURE_DB"
                }
        """
        """  resp:
                200():
                {
                    "db_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "apiWrapperNewDB")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bucket_encrypt", bucket_encrypt)
        intef.update_body("bucket_flattened", bucket_flattened)
        intef.update_body("create_bucket", create_bucket)
        intef.update_body("db_size", db_size)
        intef.update_body("description", description)
        intef.update_body("enable_isolated_feature_table", enable_isolated_feature_table)
        intef.update_body("extra_db_type", extra_db_type)
        intef.update_body("feature_version", feature_version)
        intef.update_body("name", name)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def apiWrapperSearchImageInDBsPostApi(self, dbs=None, dropped_fields=None, extra_db_type=None, image=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  SearchImageInDBs """
        """  path: [post]/engine/api-wrapper/v1/face/search_image_in_dbs API """
        """  body: 
                {
                    "dbs": [
                        {
                            "db_id": "",
                            "min_score": 0,
                            "top_k": 0
                        }
                    ],
                    "dropped_fields": [
                        "[ITEM_EXTRA_INFO]ITEM_EXTRA_INFO/ITEM_META_DATA"
                    ],
                    "extra_db_type": "",
                    "image": {
                        "bounding": {},
                        "face_selection": {},
                        "image": {}
                    },
                    "type": "[STATIC_FEATURE_DB]STATIC_FEATURE_DB/ALERT_FEATURE_DB/IDENTIFICATION_FEATURE_DB/EXTRA_FEATURE_DB"
                }
        """
        """  resp:
                200():
                {
                    "query_face_info": {
                        "algo": {},
                        "associations": [
                            {
                                "associated_object_info": {},
                                "association_type": "",
                                "object_id": "",
                                "type": {}
                            }
                        ],
                        "automobile": {},
                        "carplate": {},
                        "crowd": {},
                        "cyclist": {},
                        "diagnosis": {},
                        "event": {},
                        "face": {},
                        "human_powered_vehicle": {},
                        "object_id": "",
                        "other": {},
                        "pedestrian": {},
                        "portrait_image_location": {},
                        "trajectory": {},
                        "type": {},
                        "watercraft": {}
                    },
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ],
                    "search_results": [
                        {
                            "db_id": "",
                            "similar_results": [
                                {
                                    "item": {},
                                    "score": 0
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "apiWrapperSearchImageInDBs")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("dbs", dbs)
        intef.update_body("dropped_fields", dropped_fields)
        intef.update_body("extra_db_type", extra_db_type)
        intef.update_body("image", image)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def imageProcessWrapperBatchCompareFeaturePostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchCompareFeature """
        """  path: [post]/engine/api-wrapper/v1/image_process/batch_compare_feature API """
        """  body: 
                {
                    "requests": [
                        {
                            "one": {},
                            "other": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ],
                    "score": []
                }

        """
        intef = collections.interface("viperOpenApi", "imageProcessWrapperBatchCompareFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageProcessWrapperBatchDetectPostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetect """
        """  path: [post]/engine/api-wrapper/v1/image_process/batch_detect API """
        """  body: 
                {
                    "requests": [
                        {
                            "detect_mode": {},
                            "image": {},
                            "image_type": {},
                            "object_type": [
                                "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "info": [
                                {
                                    "algo": {},
                                    "associations": [
                                        {
                                            "associated_object_info": {},
                                            "association_type": "",
                                            "object_id": "",
                                            "type": {}
                                        }
                                    ],
                                    "automobile": {},
                                    "carplate": {},
                                    "crowd": {},
                                    "cyclist": {},
                                    "diagnosis": {},
                                    "event": {},
                                    "face": {},
                                    "human_powered_vehicle": {},
                                    "object_id": "",
                                    "other": {},
                                    "pedestrian": {},
                                    "portrait_image_location": {},
                                    "trajectory": {},
                                    "type": {},
                                    "watercraft": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageProcessWrapperBatchDetect")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageProcessWrapperBatchDetectAndExtractAllPostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetectAndExtractAll """
        """  path: [post]/engine/api-wrapper/v1/image_process/batch_detect_and_extract_all API """
        """  body: 
                {
                    "requests": [
                        {
                            "detect_mode": {},
                            "image": {},
                            "image_type": {},
                            "object_type": [
                                "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "objects": [
                        {
                            "infos": [
                                {
                                    "face_score": 0,
                                    "feature": {},
                                    "object_info": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageProcessWrapperBatchDetectAndExtractAll")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageProcessWrapperBatchExtractWithLocationPostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchExtractWithLocation """
        """  path: [post]/engine/api-wrapper/v1/image_process/batch_extract_with_location API """
        """  body: 
                {
                    "requests": [
                        {
                            "bounding": {},
                            "image": {},
                            "object_type": [
                                "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                            ],
                            "points": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "objects": [
                        {
                            "infos": [
                                {
                                    "face_score": 0,
                                    "feature": {},
                                    "object_info": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageProcessWrapperBatchExtractWithLocation")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def searchWrapperSearchPostApi(self, common_config=None, engine_configs=None, filters=None, search_mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  Search """
        """  path: [post]/engine/api-wrapper/v1/search API """
        """  body: 
                {
                    "common_config": {},
                    "engine_configs": [
                        {
                            "carplate_text": {},
                            "config": {},
                            "feature": {},
                            "weight": 0
                        }
                    ],
                    "filters": [
                        {
                            "filters": [
                                {
                                    "bool_value": false,
                                    "field": "",
                                    "filter_logic_type": {},
                                    "float_array": [],
                                    "float_value": 0,
                                    "integer_array": [],
                                    "integer_value": "",
                                    "string_array": [],
                                    "string_value": "",
                                    "type": {}
                                }
                            ],
                            "object_type": {}
                        }
                    ],
                    "search_mode": {}
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "score": 0,
                            "search_objects": [
                                {
                                    "cluster_id": "",
                                    "extra_info": "",
                                    "object": {},
                                    "object_id": {},
                                    "panoramic_image": {},
                                    "portrait_image": {},
                                    "score": 0
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "searchWrapperSearch")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("common_config", common_config)
        intef.update_body("engine_configs", engine_configs)
        intef.update_body("filters", filters)
        intef.update_body("search_mode", search_mode)
        return intef.request() if sendRequest else intef

    def searchWrapperSearchByImagePostApi(self, boundings=None, image=None, search_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  SearchByImage """
        """  path: [post]/engine/api-wrapper/v1/search_by_image API """
        """  body: 
                {
                    "boundings": [
                        {
                            "bounding": {},
                            "object_type": {}
                        }
                    ],
                    "image": {},
                    "search_request": {}
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "score": 0,
                            "search_objects": [
                                {
                                    "cluster_id": "",
                                    "extra_info": "",
                                    "object": {},
                                    "object_id": {},
                                    "panoramic_image": {},
                                    "portrait_image": {},
                                    "score": 0
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "searchWrapperSearchByImage")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("boundings", boundings)
        intef.update_body("image", image)
        intef.update_body("search_request", search_request)
        return intef.request() if sendRequest else intef

    def cameraManagerExportCamerasPostApi(self, tags=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ExportCameras """
        """  path: [post]/engine/camera-manager/v1/export_cameras API """
        """  body: 
                {
                    "tags": []
                }
        """
        """  resp:
                200():
                {
                    "cameras": [
                        {
                            "camera_calibration_info": {},
                            "camera_status": {},
                            "config": {},
                            "created_at": "",
                            "description": "",
                            "device_id": "",
                            "display_name": "",
                            "extra_info": "",
                            "geo_point": {},
                            "id": "",
                            "ingress_type": {},
                            "origin_device_id": "",
                            "removed": false,
                            "tags": [],
                            "tasks_count": 0,
                            "updated_at": "",
                            "uuid": "",
                            "zone_uuid": ""
                        }
                    ],
                    "export_timestamp": "",
                    "version": "",
                    "zones": [
                        {
                            "camera_count": 0,
                            "created_at": "",
                            "description": "",
                            "display_name": "",
                            "extra_info": "",
                            "id": "",
                            "updated_at": "",
                            "uuid": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerExportCameras")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("tags", tags)
        return intef.request() if sendRequest else intef

    # def cameraManagerGB28181LocalConfigReplacePutApi(self, configRequest.local_uuid, configRequest=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  GB28181LocalConfigReplace """
    #     """  path: [put]/engine/camera-manager/v1/gb28181_local_configs/{configRequest.local_uuid} API """
    #     """  body:
    #             {
    #                 "configRequest": {}
    #             }
    #     """
    #     """  resp:
    #             200():
    #             {}
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "cameraManagerGB28181LocalConfigReplace")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("configRequest.local_uuid", configRequest.local_uuid)
    #     intef.update_body("configRequest", configRequest)
    #     return intef.request() if sendRequest else intef

    def cameraManagerGB28181LocalConfigInfoGetApi(self, uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GB28181LocalConfigInfo """
        """  path: [get]/engine/camera-manager/v1/gb28181_local_configs/{uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "config": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerGB28181LocalConfigInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("uuid", uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerGetCamerasByInternalIDPostApi(self, bypass_cache=None, internal_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetCamerasByInternalID """
        """  path: [post]/engine/camera-manager/v1/get_cameras_by_internal_id API """
        """  body: 
                {
                    "bypass_cache": false,
                    "internal_ids": [
                        {
                            "camera_idx": 0,
                            "region_id": 0
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "cameras": [
                        {
                            "camera_calibration_info": {},
                            "camera_status": {},
                            "config": {},
                            "created_at": "",
                            "description": "",
                            "device_id": "",
                            "display_name": "",
                            "extra_info": "",
                            "geo_point": {},
                            "id": "",
                            "ingress_type": {},
                            "origin_device_id": "",
                            "removed": false,
                            "tags": [],
                            "tasks_count": 0,
                            "updated_at": "",
                            "uuid": "",
                            "zone_uuid": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerGetCamerasByInternalID")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("bypass_cache", bypass_cache)
        intef.update_body("internal_ids", internal_ids)
        return intef.request() if sendRequest else intef

    def cameraManagerImportCamerasPostApi(self, cameras=None, export_timestamp=None, version=None, zones=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ImportCameras """
        """  path: [post]/engine/camera-manager/v1/import_cameras API """
        """  body: 
                {
                    "cameras": [
                        {
                            "camera_calibration_info": {},
                            "camera_status": {},
                            "config": {},
                            "created_at": "",
                            "description": "",
                            "device_id": "",
                            "display_name": "",
                            "extra_info": "",
                            "geo_point": {},
                            "id": "",
                            "ingress_type": {},
                            "origin_device_id": "",
                            "removed": false,
                            "tags": [],
                            "tasks_count": 0,
                            "updated_at": "",
                            "uuid": "",
                            "zone_uuid": ""
                        }
                    ],
                    "export_timestamp": "",
                    "version": "",
                    "zones": [
                        {
                            "camera_count": 0,
                            "created_at": "",
                            "description": "",
                            "display_name": "",
                            "extra_info": "",
                            "id": "",
                            "updated_at": "",
                            "uuid": ""
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "failed_cameras": [
                        {
                            "code": {},
                            "error": "",
                            "uuid": ""
                        }
                    ],
                    "failed_zones": [
                        {
                            "code": {},
                            "error": "",
                            "uuid": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerImportCameras")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("cameras", cameras)
        intef.update_body("export_timestamp", export_timestamp)
        intef.update_body("version", version)
        intef.update_body("zones", zones)
        return intef.request() if sendRequest else intef

    def cameraManagerNamespaceListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  NamespaceList """
        """  path: [get]/engine/camera-manager/v1/namespaces API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "namespace_infos": [
                        {
                            "name": "",
                            "ns_id": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerNamespaceList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    # def cameraManagerNamespaceNewPostApi(self, namespace_request.ns_id, namespace_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  NamespaceNew """
    #     """  path: [post]/engine/camera-manager/v1/namespaces/{namespace_request.ns_id} API """
    #     """  body:
    #             {
    #                 "namespace_request": {}
    #             }
    #     """
    #     """  resp:
    #             200():
    #             {
    #                 "namespace_info": {}
    #             }
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "cameraManagerNamespaceNew")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("namespace_request.ns_id", namespace_request.ns_id)
    #     intef.update_body("namespace_request", namespace_request)
    #     return intef.request() if sendRequest else intef
    #
    # def cameraManagerNamespaceReplacePutApi(self, namespace_request.ns_id, namespace_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  NamespaceReplace """
    #     """  path: [put]/engine/camera-manager/v1/namespaces/{namespace_request.ns_id} API """
    #     """  body:
    #             {
    #                 "namespace_request": {}
    #             }
    #     """
    #     """  resp:
    #             200():
    #             {}
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "cameraManagerNamespaceReplace")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("namespace_request.ns_id", namespace_request.ns_id)
    #     intef.update_body("namespace_request", namespace_request)
    #     return intef.request() if sendRequest else intef

    def cameraManagerNamespaceDeleteDeleteApi(self, ns_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  NamespaceDelete """
        """  path: [delete]/engine/camera-manager/v1/namespaces/{ns_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerNamespaceDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("ns_id", ns_id)
        return intef.request() if sendRequest else intef

    def cameraManagerNamespaceInfoGetApi(self, ns_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  NamespaceInfo """
        """  path: [get]/engine/camera-manager/v1/namespaces/{ns_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "namespace_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerNamespaceInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("ns_id", ns_id)
        return intef.request() if sendRequest else intef

    def cameraManagerPlatformListGetApi(self, platform_type=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PlatformList """
        """  path: [get]/engine/camera-manager/v1/platforms API """
        """  params: 
                参数名称：platform_type　类型：string　描述：可选, 平台类型， 为空时获取所有平台参数, 一种类型平台下支持多个平台配置.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "platform_configs": [
                        {
                            "created_at": "",
                            "description": "",
                            "display_name": "",
                            "external_task_uuid": "",
                            "gb28181_local_config": {},
                            "id_in_config": "",
                            "platform_id": "",
                            "platform_parameter": {},
                            "status": {},
                            "updated_at": "",
                            "uuid": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerPlatformList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("platform_type", platform_type)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def cameraManagerPlatformNewPostApi(self, platform_config_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PlatformNew """
        """  path: [post]/engine/camera-manager/v1/platforms API """
        """  body: 
                {
                    "platform_config_request": {}
                }
        """
        """  resp:
                200():
                {
                    "id": "",
                    "platform_config": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerPlatformNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("platform_config_request", platform_config_request)
        return intef.request() if sendRequest else intef

    def cameraManagerPlatformDeleteDeleteApi(self, platform_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PlatformDelete """
        """  path: [delete]/engine/camera-manager/v1/platforms/{platform_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerPlatformDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def cameraManagerPlatformInfoGetApi(self, platform_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PlatformInfo """
        """  path: [get]/engine/camera-manager/v1/platforms/{platform_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "platform_config": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerPlatformInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def cameraManagerPlatformReplacePutApi(self, platform_id, platform_config_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PlatformReplace """
        """  path: [put]/engine/camera-manager/v1/platforms/{platform_id} API """
        """  body: 
                {
                    "platform_config_request": {},
                    "platform_id": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerPlatformReplace")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("platform_id", platform_id)
        intef.update_body("platform_config_request", platform_config_request)
        intef.update_body("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def cameraManagerPlatformCameraListGetApi(self, platform_id, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PlatformCameraList """
        """  path: [get]/engine/camera-manager/v1/platforms/{platform_id}/cameras API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "cameras": [
                        {
                            "camera_calibration_info": {},
                            "camera_status": {},
                            "config": {},
                            "created_at": "",
                            "description": "",
                            "device_id": "",
                            "display_name": "",
                            "extra_info": "",
                            "geo_point": {},
                            "id": "",
                            "ingress_type": {},
                            "origin_device_id": "",
                            "removed": false,
                            "tags": [],
                            "tasks_count": 0,
                            "updated_at": "",
                            "uuid": "",
                            "zone_uuid": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerPlatformCameraList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def cameraManagerGetCamerasFromPlatformGetApi(self, platform_id, device_id=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetCamerasFromPlatform """
        """  path: [get]/engine/camera-manager/v1/platforms/{platform_id}/cameras_third_party API """
        """  params: 
                参数名称：device_id　类型：string　描述：设备/区域/系统ID.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "platform_cameras": [
                        {
                            "dahua": {},
                            "gat1400": {},
                            "gb28181": {},
                            "onvif": {},
                            "platform_type": {},
                            "xinghuo": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerGetCamerasFromPlatform")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("device_id", device_id)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def cameraManagerPlatformCatalogItemsGetApi(self, platform_id, item_type=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PlatformCatalogItems """
        """  path: [get]/engine/camera-manager/v1/platforms/{platform_id}/catalog_items API """
        """  params: 
                参数名称：item_type　类型：string　描述：目录项类型.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "catalog_items": [
                        {
                            "dahua": {},
                            "gat1400": {},
                            "gb28181": {},
                            "item_type": {},
                            "onvif": {},
                            "xinghuo": {}
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerPlatformCatalogItems")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("item_type", item_type)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def cameraManagerPlatformCatalogSendPostApi(self, platform_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PlatformCatalogSend """
        """  path: [post]/engine/camera-manager/v1/platforms/{platform_id}/catalog_send API """
        """  body: 
                {
                    "platform_id": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerPlatformCatalogSend")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("platform_id", platform_id)
        intef.update_body("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def cameraManagerBatchDeleteSharedDevicesDeleteApi(self, platform_id, device_uuids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDeleteSharedDevices """
        """  path: [delete]/engine/camera-manager/v1/platforms/{platform_id}/share_devices API """
        """  params: 
                参数名称：device_uuids　类型：array　描述：设备uuid
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerBatchDeleteSharedDevices")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("device_uuids", device_uuids)
        intef.set_path_param("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def cameraManagerBatchAddSharedDevicesPostApi(self, platform_id, device_uuids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchAddSharedDevices """
        """  path: [post]/engine/camera-manager/v1/platforms/{platform_id}/share_devices API """
        """  body: 
                {
                    "device_uuids": [],
                    "platform_id": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerBatchAddSharedDevices")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("platform_id", platform_id)
        intef.update_body("device_uuids", device_uuids)
        intef.update_body("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def cameraManagerPlatformSubscribeListGetApi(self, platform_id, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PlatformSubscribeList """
        """  path: [get]/engine/camera-manager/v1/platforms/{platform_id}/subscribes API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "platform_subscribes": [
                        {
                            "created_at": "",
                            "external_subscribe_id": "",
                            "id": "",
                            "parameter": {},
                            "platform_id": "",
                            "subscribe_tag": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerPlatformSubscribeList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def cameraManagerPlatformSubscribeDeleteDeleteApi(self, platform_id, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PlatformSubscribeDelete """
        """  path: [delete]/engine/camera-manager/v1/platforms/{platform_id}/subscribes/{id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerPlatformSubscribeDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("platform_id", platform_id)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    # def cameraManagerPlatformSubscribeNewPostApi(self, platform_subscribe_request.platform_id, platform_subscribe_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  PlatformSubscribeNew """
    #     """  path: [post]/engine/camera-manager/v1/platforms/{platform_subscribe_request.platform_id}/subscribes API """
    #     """  body:
    #             {
    #                 "platform_subscribe_request": {}
    #             }
    #     """
    #     """  resp:
    #             200():
    #             {
    #                 "platform_subscribe": {}
    #             }
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "cameraManagerPlatformSubscribeNew")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("platform_subscribe_request.platform_id", platform_subscribe_request.platform_id)
    #     intef.update_body("platform_subscribe_request", platform_subscribe_request)
    #     return intef.request() if sendRequest else intef

    def cameraManagerSearchCamerasPostApi(self, camera_uuid=None, created_time_range=None, display_name=None, include_removed=None, ingress_types=None, page=None, platform_id=None, source_types=None, status=None, time_ascended=None, zone_uuid=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  SearchCameras """
        """  path: [post]/engine/camera-manager/v1/search_cameras API """
        """  body: 
                {
                    "camera_uuid": "",
                    "created_time_range": {},
                    "display_name": "",
                    "include_removed": {},
                    "ingress_types": [
                        "[VIDEO]VIDEO/IMAGE"
                    ],
                    "page": {},
                    "platform_id": "",
                    "source_types": [
                        "[UNKNOWN]UNKNOWN/VN_RTSP/VN_ONVIF/VN_HLS/VN_RTMP/VP_GB28181_STD/VP_HUAWEI_VCN/VP_XINGHUO/VP_ALIYUN/VP_SJK/VP_DH_VIDEO_CLOUD/VP_SYMPHONY_NEBULA/FC_HK/FC_HK_ISAPI/FC_DAHUA/FC_YUSHI/FC_YUNTIAN/FC_HUAWEI/FC_SENSETIME_001/FC_SENSETIME_002/FC_SENSETIME_D/FC_DEEPGLINT/FC_KEDA/FC_TIANDY/FC_MEGVII/FC_SYMPHONY_NEBULA/FC_SYMPHONY_PASS/FC_GAT1400_APE/FC_DUMMY/FC_FTP/FC_HTTP/FP_XINGHUO/FP_GAT1400_PLATFORM/FP_TAOAN_PLATFORM/FP_WANGLI_PLATFORM/FP_SECURITY_FIRST_PLATFORM/FP_SECURITY_THIRD_PLATFORM/FP_BAIDU_PLATFORM"
                    ],
                    "status": [
                        "[CAMERA_STATUS_UNKNOWN]CAMERA_STATUS_UNKNOWN/CAMERA_STATUS_ON/CAMERA_STATUS_OFF/CAMERA_STATUS_UNAVAILABLE/CAMERA_STATUS_DELETING"
                    ],
                    "time_ascended": false,
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "cameras": [
                        {
                            "camera_calibration_info": {},
                            "camera_status": {},
                            "config": {},
                            "created_at": "",
                            "description": "",
                            "device_id": "",
                            "display_name": "",
                            "extra_info": "",
                            "geo_point": {},
                            "id": "",
                            "ingress_type": {},
                            "origin_device_id": "",
                            "removed": false,
                            "tags": [],
                            "tasks_count": 0,
                            "updated_at": "",
                            "uuid": "",
                            "zone_uuid": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerSearchCameras")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("created_time_range", created_time_range)
        intef.update_body("display_name", display_name)
        intef.update_body("include_removed", include_removed)
        intef.update_body("ingress_types", ingress_types)
        intef.update_body("page", page)
        intef.update_body("platform_id", platform_id)
        intef.update_body("source_types", source_types)
        intef.update_body("status", status)
        intef.update_body("time_ascended", time_ascended)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerSearchCamerasInBoundingPostApi(self, tags=None, bounding=None, page=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  SearchCamerasInBounding """
        """  path: [post]/engine/camera-manager/v1/search_cameras_in_bounding API """
        """  body: 
                {
                    "bounding": {},
                    "page": {},
                    "tags": []
                }
        """
        """  resp:
                200():
                {
                    "cameras": [
                        {
                            "camera_calibration_info": {},
                            "camera_status": {},
                            "config": {},
                            "created_at": "",
                            "description": "",
                            "device_id": "",
                            "display_name": "",
                            "extra_info": "",
                            "geo_point": {},
                            "id": "",
                            "ingress_type": {},
                            "origin_device_id": "",
                            "removed": false,
                            "tags": [],
                            "tasks_count": 0,
                            "updated_at": "",
                            "uuid": "",
                            "zone_uuid": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerSearchCamerasInBounding")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("tags", tags)
        intef.update_body("bounding", bounding)
        intef.update_body("page", page)
        return intef.request() if sendRequest else intef

    def cameraManagerSearchNearestCamerasPostApi(self, tags=None, distance=None, geo_point=None, nearest_k=None, page=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  SearchNearestCameras """
        """  path: [post]/engine/camera-manager/v1/search_nearest_cameras API """
        """  body: 
                {
                    "distance": 0,
                    "geo_point": {},
                    "nearest_k": 0,
                    "page": {},
                    "tags": []
                }
        """
        """  resp:
                200():
                {
                    "cameras": [
                        {
                            "camera_calibration_info": {},
                            "camera_status": {},
                            "config": {},
                            "created_at": "",
                            "description": "",
                            "device_id": "",
                            "display_name": "",
                            "extra_info": "",
                            "geo_point": {},
                            "id": "",
                            "ingress_type": {},
                            "origin_device_id": "",
                            "removed": false,
                            "tags": [],
                            "tasks_count": 0,
                            "updated_at": "",
                            "uuid": "",
                            "zone_uuid": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerSearchNearestCameras")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("tags", tags)
        intef.update_body("distance", distance)
        intef.update_body("geo_point", geo_point)
        intef.update_body("nearest_k", nearest_k)
        intef.update_body("page", page)
        return intef.request() if sendRequest else intef

    def cameraManagerSearchTasksPostApi(self, camera_uuid=None, created_time_range=None, id=None, ingress_types=None, object_types=None, page=None, status=None, time_ascended=None, zone_uuid=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  SearchTasks """
        """  path: [post]/engine/camera-manager/v1/search_tasks API """
        """  body: 
                {
                    "camera_uuid": "",
                    "created_time_range": {},
                    "id": "",
                    "ingress_types": [
                        "[VIDEO]VIDEO/IMAGE"
                    ],
                    "object_types": [
                        "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                    ],
                    "page": {},
                    "status": [
                        "[UNKNOWN]UNKNOWN/PENDING/OK/END/ERROR/UNAVAILABLE/PAUSED/RESUMED/NOLIC"
                    ],
                    "time_ascended": false,
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "page": {},
                    "tasks": [
                        {
                            "camera_uuid": "",
                            "created_at": "",
                            "data_mining": false,
                            "extra_parameter": {},
                            "feature_version": 0,
                            "id": "",
                            "ingress_type": {},
                            "internal_task_uuid": "",
                            "object_type": {},
                            "playback_config": {},
                            "storage_policy": {},
                            "symphony_device_task": {},
                            "task_object_config": {},
                            "task_status": {},
                            "updated_at": "",
                            "user_data": "",
                            "uuid": "",
                            "video_parameter": {},
                            "zone_uuid": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerSearchTasks")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("created_time_range", created_time_range)
        intef.update_body("id", id)
        intef.update_body("ingress_types", ingress_types)
        intef.update_body("object_types", object_types)
        intef.update_body("page", page)
        intef.update_body("status", status)
        intef.update_body("time_ascended", time_ascended)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerTagListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TagList """
        """  path: [get]/engine/camera-manager/v1/tags API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "tags": []
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerTagList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneList """
        """  path: [get]/engine/camera-manager/v1/zones API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "zones": [
                        {
                            "camera_count": 0,
                            "created_at": "",
                            "description": "",
                            "display_name": "",
                            "extra_info": "",
                            "id": "",
                            "updated_at": "",
                            "uuid": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    # def cameraManagerZoneCameraNewPostApi(self, camera_request.zone_uuid, camera_request.uuid, camera_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  ZoneCameraNew """
    #     """  path: [post]/engine/camera-manager/v1/zones/{camera_request.zone_uuid}/cameras/{camera_request.uuid} API """
    #     """  body:
    #             {
    #                 "camera_request": {}
    #             }
    #     """
    #     """  resp:
    #             200():
    #             {
    #                 "camera": {}
    #             }
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraNew")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("camera_request.zone_uuid", camera_request.zone_uuid)
    #     intef.set_path_param("camera_request.uuid", camera_request.uuid)
    #     intef.update_body("camera_request", camera_request)
    #     return intef.request() if sendRequest else intef

    # def cameraManagerZoneCameraReplacePutApi(self, camera_request.zone_uuid, camera_request.uuid, camera_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  ZoneCameraReplace """
    #     """  path: [put]/engine/camera-manager/v1/zones/{camera_request.zone_uuid}/cameras/{camera_request.uuid} API """
    #     """  body:
    #             {
    #                 "camera_request": {}
    #             }
    #     """
    #     """  resp:
    #             200():
    #             {}
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraReplace")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("camera_request.zone_uuid", camera_request.zone_uuid)
    #     intef.set_path_param("camera_request.uuid", camera_request.uuid)
    #     intef.update_body("camera_request", camera_request)
    #     return intef.request() if sendRequest else intef
    #
    # def cameraManagerZoneNewPostApi(self, zone_request.uuid, zone_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  ZoneNew """
    #     """  path: [post]/engine/camera-manager/v1/zones/{zone_request.uuid} API """
    #     """  body:
    #             {
    #                 "zone_request": {}
    #             }
    #     """
    #     """  resp:
    #             200():
    #             {
    #                 "zone": {}
    #             }
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "cameraManagerZoneNew")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("zone_request.uuid", zone_request.uuid)
    #     intef.update_body("zone_request", zone_request)
    #     return intef.request() if sendRequest else intef
    #
    # def cameraManagerZoneReplacePutApi(self, zone_request.uuid, zone_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  ZoneReplace """
    #     """  path: [put]/engine/camera-manager/v1/zones/{zone_request.uuid} API """
    #     """  body:
    #             {
    #                 "zone_request": {}
    #             }
    #     """
    #     """  resp:
    #             200():
    #             {}
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "cameraManagerZoneReplace")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("zone_request.uuid", zone_request.uuid)
    #     intef.update_body("zone_request", zone_request)
    #     return intef.request() if sendRequest else intef

    def cameraManagerZoneDeleteDeleteApi(self, zone_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneDelete """
        """  path: [delete]/engine/camera-manager/v1/zones/{zone_uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneInfoGetApi(self, zone_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneInfo """
        """  path: [get]/engine/camera-manager/v1/zones/{zone_uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "zone": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraListGetApi(self, zone_uuid, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraList """
        """  path: [get]/engine/camera-manager/v1/zones/{zone_uuid}/cameras API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "cameras": [
                        {
                            "camera_calibration_info": {},
                            "camera_status": {},
                            "config": {},
                            "created_at": "",
                            "description": "",
                            "device_id": "",
                            "display_name": "",
                            "extra_info": "",
                            "geo_point": {},
                            "id": "",
                            "ingress_type": {},
                            "origin_device_id": "",
                            "removed": false,
                            "tags": [],
                            "tasks_count": 0,
                            "updated_at": "",
                            "uuid": "",
                            "zone_uuid": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraDeleteDeleteApi(self, zone_uuid, camera_uuid, force=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraDelete """
        """  path: [delete]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid} API """
        """  params: 
                参数名称：force　类型：boolean　描述：可选, force默认为false, 表示移除相机（软删除）.
force为true时表示彻底删除相机记录，并回收对应的CameraIdentifier供重新分配;注意此操作可能会导致时空库的旧数据与相机信息不一致
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("force", force)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraInfoGetApi(self, zone_uuid, camera_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraInfo """
        """  path: [get]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "camera": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraActivatePostApi(self, zone_uuid, camera_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraActivate """
        """  path: [post]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/activate API """
        """  body: 
                {
                    "camera_uuid": "",
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraActivate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraFIControlPutApi(self, zone_uuid, camera_uuid, fi_control_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraFIControl """
        """  path: [put]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/fi_control API """
        """  body: 
                {
                    "camera_uuid": "",
                    "fi_control_request": {},
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraFIControl")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("fi_control_request", fi_control_request)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraGenerateRTMPAddressPostApi(self, zone_uuid, camera_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraGenerateRTMPAddress """
        """  path: [post]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/generate_rtmp_address API """
        """  body: 
                {
                    "camera_uuid": "",
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "rtmp_url": ""
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraGenerateRTMPAddress")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraGenerateRTSPAddressPostApi(self, zone_uuid, camera_uuid, command_type=None, media_protocol_type=None, playback_config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraGenerateRTSPAddress """
        """  path: [post]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/generate_rtsp_address API """
        """  body: 
                {
                    "camera_uuid": "",
                    "command_type": {},
                    "media_protocol_type": {},
                    "playback_config": {},
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "is_absolute": false,
                    "url": ""
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraGenerateRTSPAddress")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("command_type", command_type)
        intef.update_body("media_protocol_type", media_protocol_type)
        intef.update_body("playback_config", playback_config)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraHomePositionSetPutApi(self, zone_uuid, camera_uuid, home_position_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraHomePositionSet """
        """  path: [put]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/home_position_set API """
        """  body: 
                {
                    "camera_uuid": "",
                    "home_position_request": {},
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraHomePositionSet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("home_position_request", home_position_request)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraMultiTaskListGetApi(self, zone_uuid, camera_uuid, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraMultiTaskList """
        """  path: [get]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/multi_tasks API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "tasks": [
                        {
                            "camera_uuid": "",
                            "default_task": {},
                            "id": "",
                            "internal_task_uuid": "",
                            "task_list": [
                                {
                                    "camera_uuid": "",
                                    "created_at": "",
                                    "data_mining": false,
                                    "extra_parameter": {},
                                    "feature_version": 0,
                                    "id": "",
                                    "ingress_type": {},
                                    "internal_task_uuid": "",
                                    "object_type": {},
                                    "playback_config": {},
                                    "storage_policy": {},
                                    "symphony_device_task": {},
                                    "task_object_config": {},
                                    "task_status": {},
                                    "updated_at": "",
                                    "user_data": "",
                                    "uuid": "",
                                    "video_parameter": {},
                                    "zone_uuid": ""
                                }
                            ],
                            "uuid": "",
                            "zone_uuid": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraMultiTaskList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraMultiTaskNewPostApi(self, zone_uuid, camera_uuid, default_task=None, multi_tasks=None, user_data=None, uuid=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraMultiTaskNew """
        """  path: [post]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/multi_tasks API """
        """  body: 
                {
                    "camera_uuid": "",
                    "default_task": {},
                    "multi_tasks": [
                        {
                            "extra_parameter": {},
                            "feature_version": 0,
                            "object_type": {},
                            "storage_policy": {},
                            "task_object_config": {},
                            "uuid": ""
                        }
                    ],
                    "user_data": "",
                    "uuid": "",
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "task": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraMultiTaskNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("default_task", default_task)
        intef.update_body("multi_tasks", multi_tasks)
        intef.update_body("user_data", user_data)
        intef.update_body("uuid", uuid)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraMultiTaskDeleteDeleteApi(self, zone_uuid, camera_uuid, uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraMultiTaskDelete """
        """  path: [delete]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/multi_tasks/{uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraMultiTaskDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.set_path_param("uuid", uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraMultiTaskInfoGetApi(self, zone_uuid, camera_uuid, uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraMultiTaskInfo """
        """  path: [get]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/multi_tasks/{uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "task": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraMultiTaskInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.set_path_param("uuid", uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraMultiTaskUpdatePutApi(self, zone_uuid, camera_uuid, uuid, multi_tasks=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraMultiTaskUpdate """
        """  path: [put]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/multi_tasks/{uuid} API """
        """  body: 
                {
                    "camera_uuid": "",
                    "multi_tasks": [
                        {
                            "extra_parameter": {},
                            "feature_version": 0,
                            "object_type": {},
                            "storage_policy": {},
                            "task_object_config": {},
                            "uuid": ""
                        }
                    ],
                    "uuid": "",
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "camera_uuid": "",
                    "task": {},
                    "zone_uuid": ""
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraMultiTaskUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.set_path_param("uuid", uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("multi_tasks", multi_tasks)
        intef.update_body("uuid", uuid)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraPresetListGetApi(self, zone_uuid, camera_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraPresetList """
        """  path: [get]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/presets API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "presets": [
                        {
                            "name": "",
                            "position": {},
                            "preset_id": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraPresetList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraPresetSetPutApi(self, zone_uuid, camera_uuid, preset=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraPresetSet """
        """  path: [put]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/presets API """
        """  body: 
                {
                    "camera_uuid": "",
                    "preset": {},
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraPresetSet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("preset", preset)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraPresetDeleteDeleteApi(self, zone_uuid, camera_uuid, preset_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraPresetDelete """
        """  path: [delete]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/presets/{preset_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraPresetDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.set_path_param("preset_id", preset_id)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraPresetGotoPutApi(self, zone_uuid, camera_uuid, preset_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraPresetGoto """
        """  path: [put]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/presets/{preset_id}/goto API """
        """  body: 
                {
                    "camera_uuid": "",
                    "preset_id": "",
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraPresetGoto")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.set_path_param("preset_id", preset_id)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("preset_id", preset_id)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraPTZControlPutApi(self, zone_uuid, camera_uuid, ptz_control_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraPTZControl """
        """  path: [put]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/ptz_control API """
        """  body: 
                {
                    "camera_uuid": "",
                    "ptz_control_request": {},
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraPTZControl")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("ptz_control_request", ptz_control_request)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraPTZControlTransparentPutApi(self, zone_uuid, camera_uuid, ptz_command=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraPTZControlTransparent """
        """  path: [put]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/ptz_control_transparent API """
        """  body: 
                {
                    "camera_uuid": "",
                    "ptz_command": "",
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraPTZControlTransparent")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("ptz_command", ptz_command)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraRecordInfoPostApi(self, zone_uuid, camera_uuid, record_info_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraRecordInfo """
        """  path: [post]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/record_info API """
        """  body: 
                {
                    "camera_uuid": "",
                    "record_info_request": {},
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "records": [
                        {
                            "address": "",
                            "device_id": "",
                            "file_path": "",
                            "file_size": "",
                            "name": "",
                            "record_type": {},
                            "recorder_id": "",
                            "secrecy": 0,
                            "start_time": "",
                            "stop_time": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraRecordInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("record_info_request", record_info_request)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraTaskListGetApi(self, zone_uuid, camera_uuid, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraTaskList """
        """  path: [get]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/tasks API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "tasks": [
                        {
                            "camera_uuid": "",
                            "created_at": "",
                            "data_mining": false,
                            "extra_parameter": {},
                            "feature_version": 0,
                            "id": "",
                            "ingress_type": {},
                            "internal_task_uuid": "",
                            "object_type": {},
                            "playback_config": {},
                            "storage_policy": {},
                            "symphony_device_task": {},
                            "task_object_config": {},
                            "task_status": {},
                            "updated_at": "",
                            "user_data": "",
                            "uuid": "",
                            "video_parameter": {},
                            "zone_uuid": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraTaskList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraTaskNewPostApi(self, zone_uuid, camera_uuid, extra_parameter=None, feature_version=None, object_type=None, playback_config=None, storage_policy=None, symphony_device_task=None, task_object_config=None, user_data=None, uuid=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraTaskNew """
        """  path: [post]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/tasks API """
        """  body: 
                {
                    "camera_uuid": "",
                    "extra_parameter": {},
                    "feature_version": 0,
                    "object_type": {},
                    "playback_config": {},
                    "storage_policy": {},
                    "symphony_device_task": {},
                    "task_object_config": {},
                    "user_data": "",
                    "uuid": "",
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "task": {}
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraTaskNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("extra_parameter", extra_parameter)
        intef.update_body("feature_version", feature_version)
        intef.update_body("object_type", object_type)
        intef.update_body("playback_config", playback_config)
        intef.update_body("storage_policy", storage_policy)
        intef.update_body("symphony_device_task", symphony_device_task)
        intef.update_body("task_object_config", task_object_config)
        intef.update_body("user_data", user_data)
        intef.update_body("uuid", uuid)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraTaskDeleteDeleteApi(self, zone_uuid, camera_uuid, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraTaskDelete """
        """  path: [delete]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/tasks/{id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraTaskDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.set_path_param("id", id)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraTaskUpdatePutApi(self, zone_uuid, camera_uuid, id, task_object_config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraTaskUpdate """
        """  path: [put]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/tasks/{id} API """
        """  body: 
                {
                    "camera_uuid": "",
                    "id": "",
                    "task_object_config": {},
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "camera_uuid": "",
                    "task": {},
                    "zone_uuid": ""
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraTaskUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.set_path_param("id", id)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("id", id)
        intef.update_body("task_object_config", task_object_config)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraTaskGenerateRTSPAddressPostApi(self, zone_uuid, camera_uuid, id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraTaskGenerateRTSPAddress """
        """  path: [post]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/tasks/{id}/generate_rtsp_address API """
        """  body: 
                {
                    "camera_uuid": "",
                    "id": "",
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "is_absolute": false,
                    "url": ""
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraTaskGenerateRTSPAddress")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.set_path_param("id", id)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("id", id)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraTeleBootPutApi(self, zone_uuid, camera_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraTeleBoot """
        """  path: [put]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/tele_boot API """
        """  body: 
                {
                    "camera_uuid": "",
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraTeleBoot")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraVideoCapturePostApi(self, zone_uuid, camera_uuid, command_type=None, media_protocol_type=None, playback_config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraVideoCapture """
        """  path: [post]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/video_capture API """
        """  body: 
                {
                    "camera_uuid": "",
                    "command_type": {},
                    "media_protocol_type": {},
                    "playback_config": {},
                    "zone_uuid": ""
                }
        """
        """  resp:
                200():
                {
                    "camera_uuid": "",
                    "image_data": "",
                    "image_format": {},
                    "image_length": ""
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraVideoCapture")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        intef.update_body("camera_uuid", camera_uuid)
        intef.update_body("command_type", command_type)
        intef.update_body("media_protocol_type", media_protocol_type)
        intef.update_body("playback_config", playback_config)
        intef.update_body("zone_uuid", zone_uuid)
        return intef.request() if sendRequest else intef

    def cameraManagerZoneCameraVideoParameterGetApi(self, zone_uuid, camera_uuid, media_protocol_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ZoneCameraVideoParameter """
        """  path: [get]/engine/camera-manager/v1/zones/{zone_uuid}/cameras/{camera_uuid}/video_parameter API """
        """  params: 
                参数名称：media_protocol_type　类型：string　描述：可选, 视频源媒体交互协议类型, 默认为TCP, 此参数会替代相机中的视频源媒体交互协议类型 [SINCE v5.1.0]
        """
        """  resp:
                200():
                {
                    "video_parameters": [
                        {
                            "bit_rate": 0,
                            "bit_rate_type": {},
                            "frame_rate": 0,
                            "height": 0,
                            "i_frame_interval": 0,
                            "stream_type": {},
                            "video_format": {},
                            "width": 0
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "cameraManagerZoneCameraVideoParameter")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("media_protocol_type", media_protocol_type)
        intef.set_path_param("zone_uuid", zone_uuid)
        intef.set_path_param("camera_uuid", camera_uuid)
        return intef.request() if sendRequest else intef

    def entityDBAddOutsideOplogAsyncPostApi(self, oplogs=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AddOutsideOplogAsync """
        """  path: [post]/engine/entity-service/v1/add_outside_oplog_async API """
        """  body: 
                {
                    "oplogs": [
                        {
                            "op_add_cluster": {},
                            "op_add_features": {},
                            "op_add_index": {},
                            "op_add_ped_cluster": {},
                            "op_delete_cluster": {},
                            "op_delete_cluster_user_key": {},
                            "op_delete_feature": {},
                            "op_delete_feature_cluster_id": {},
                            "op_delete_index": {},
                            "op_delete_ped_cluster": {},
                            "op_merge_cluster": {},
                            "op_update_cluster": {},
                            "op_update_cluster_preview_images": {},
                            "op_update_cluster_user_key": {},
                            "op_update_feature_cluster_id": {},
                            "op_update_ped_cluster": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBAddOutsideOplogAsync")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("oplogs", oplogs)
        return intef.request() if sendRequest else intef

    def entityDBBatchUpdateEntityClusterPostApi(self, cluster_update_items=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchUpdateEntityCluster """
        """  path: [post]/engine/entity-service/v1/batch_update_entity_cluster API """
        """  body: 
                {
                    "cluster_update_items": [
                        {
                            "cluster_id": "",
                            "key_source": "",
                            "user_key": ""
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBBatchUpdateEntityCluster")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("cluster_update_items", cluster_update_items)
        return intef.request() if sendRequest else intef

    def entityDBDeleteEventsDataBeforeDatePostApi(self, date=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteEventsDataBeforeDate """
        """  path: [post]/engine/entity-service/v1/delete_events_before_date API """
        """  body: 
                {
                    "date": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "entityDBDeleteEventsDataBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("date", date)
        return intef.request() if sendRequest else intef

    def entityDBDeleteHumanVehicleTracksBeforeDatePostApi(self, date=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteHumanVehicleTracksBeforeDate """
        """  path: [post]/engine/entity-service/v1/delete_human_powered_vehicle_tracks_before_date API """
        """  body: 
                {
                    "date": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "entityDBDeleteHumanVehicleTracksBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("date", date)
        return intef.request() if sendRequest else intef

    def entityDBDeleteTracksBeforeDatePostApi(self, date=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteTracksBeforeDate """
        """  path: [post]/engine/entity-service/v1/delete_tracks_before_date API """
        """  body: 
                {
                    "date": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "entityDBDeleteTracksBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("date", date)
        return intef.request() if sendRequest else intef

    def entityDBDeleteVehicleTracksBeforeDatePostApi(self, date=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteVehicleTracksBeforeDate """
        """  path: [post]/engine/entity-service/v1/delete_vehicle_tracks_before_date API """
        """  body: 
                {
                    "date": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "entityDBDeleteVehicleTracksBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("date", date)
        return intef.request() if sendRequest else intef

    def entityDBEntityListPostApi(self, marker=None, order_field=None, page_size=None, period=None, reversed=None, types=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  EntityList """
        """  path: [post]/engine/entity-service/v1/entities API """
        """  body: 
                {
                    "marker": "",
                    "order_field": {},
                    "page_size": 0,
                    "period": {},
                    "reversed": false,
                    "types": [
                        "[PERSON_ANONYMOUS]PERSON_ANONYMOUS/PERSON_IDENTIFIED"
                    ]
                }
        """
        """  resp:
                200():
                {
                    "entities": [
                        {
                            "created_at": "",
                            "entity_id": {},
                            "extra_info": "",
                            "key_sources": [],
                            "modified_at": "",
                            "pedestrian_preview_images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ],
                            "preview_images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ],
                            "score": 0
                        }
                    ],
                    "marker": ""
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBEntityList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("marker", marker)
        intef.update_body("order_field", order_field)
        intef.update_body("page_size", page_size)
        intef.update_body("period", period)
        intef.update_body("reversed", reversed)
        intef.update_body("types", types)
        return intef.request() if sendRequest else intef

    def entityDBBatchDeleteEntitiesPostApi(self, entity_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDeleteEntities """
        """  path: [post]/engine/entity-service/v1/entities/batch_delete API """
        """  body: 
                {
                    "entity_ids": [
                        {
                            "entity_type": {},
                            "id": ""
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBBatchDeleteEntities")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("entity_ids", entity_ids)
        return intef.request() if sendRequest else intef

    def entityDBEntityBatchGetPostApi(self, entity_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  EntityBatchGet """
        """  path: [post]/engine/entity-service/v1/entities/batch_get API """
        """  body: 
                {
                    "entity_ids": [
                        {
                            "entity_type": {},
                            "id": ""
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "entities": [
                        {
                            "created_at": "",
                            "entity_id": {},
                            "extra_info": "",
                            "key_sources": [],
                            "modified_at": "",
                            "pedestrian_preview_images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ],
                            "preview_images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ],
                            "score": 0
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBEntityBatchGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("entity_ids", entity_ids)
        return intef.request() if sendRequest else intef

    def entityDBEntitySearchPostApi(self, camera_ids=None, feature=None, min_score=None, period=None, top_k=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  EntitySearch """
        """  path: [post]/engine/entity-service/v1/entities/search API """
        """  body: 
                {
                    "camera_ids": [
                        {
                            "camera_idx": 0,
                            "region_id": 0
                        }
                    ],
                    "feature": {},
                    "min_score": 0,
                    "period": {},
                    "top_k": 0
                }
        """
        """  resp:
                200():
                {
                    "entities": [
                        {
                            "created_at": "",
                            "entity_id": {},
                            "extra_info": "",
                            "key_sources": [],
                            "modified_at": "",
                            "pedestrian_preview_images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ],
                            "preview_images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ],
                            "score": 0
                        }
                    ],
                    "preview_pedestrian_track": [
                        {
                            "camera_id": {},
                            "captured_time": "",
                            "cluster_id": "",
                            "entity_id": {},
                            "extra_info": "",
                            "is_deleted": false,
                            "object": {},
                            "panoramic_image": {},
                            "portrait_image": {},
                            "track_id": {}
                        }
                    ],
                    "statistics": {}
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBEntitySearch")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("camera_ids", camera_ids)
        intef.update_body("feature", feature)
        intef.update_body("min_score", min_score)
        intef.update_body("period", period)
        intef.update_body("top_k", top_k)
        return intef.request() if sendRequest else intef

    # def entityDBTrackListByEntityPostApi(self, entity_id.entity_type, entity_id.id, entity_id=None, marker=None, page_size=None, period=None, reversed=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
    #     """  TrackListByEntity """
    #     """  path: [post]/engine/entity-service/v1/entities/{entity_id.entity_type}/{entity_id.id}/tracks API """
    #     """  body:
    #             {
    #                 "entity_id": {},
    #                 "marker": "",
    #                 "page_size": 0,
    #                 "period": {},
    #                 "reversed": false
    #             }
    #     """
    #     """  resp:
    #             200():
    #             {
    #                 "marker": "",
    #                 "tracks": [
    #                     {
    #                         "camera_id": {},
    #                         "captured_time": "",
    #                         "cluster_id": "",
    #                         "entity_id": {},
    #                         "extra_info": "",
    #                         "is_deleted": false,
    #                         "object": {},
    #                         "panoramic_image": {},
    #                         "portrait_image": {},
    #                         "track_id": {}
    #                     }
    #                 ]
    #             }
    #
    #     """
    #     intef = collections.interface("viperOpenApi", "entityDBTrackListByEntity")
    #     intef.set_print_log(print_log)
    #     intef.set_description(interface_desc)
    #     if loginToken:
    #         intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
    #     intef.set_path_param("entity_id.entity_type", entity_id.entity_type)
    #     intef.set_path_param("entity_id.id", entity_id.id)
    #     intef.update_body("entity_id", entity_id)
    #     intef.update_body("marker", marker)
    #     intef.update_body("page_size", page_size)
    #     intef.update_body("period", period)
    #     intef.update_body("reversed", reversed)
    #     return intef.request() if sendRequest else intef

    def entityDBEntitiesByTimeSpacePostApi(self, camera_ids=None, paging=None, period=None, reversed=None, types=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  EntitiesByTimeSpace """
        """  path: [post]/engine/entity-service/v1/entities_by_time_space API """
        """  body: 
                {
                    "camera_ids": [
                        {
                            "camera_idx": 0,
                            "region_id": 0
                        }
                    ],
                    "paging": {},
                    "period": {},
                    "reversed": false,
                    "types": [
                        "[PERSON_ANONYMOUS]PERSON_ANONYMOUS/PERSON_IDENTIFIED"
                    ]
                }
        """
        """  resp:
                200():
                {
                    "entities": [
                        {
                            "created_at": "",
                            "entity_id": {},
                            "extra_info": "",
                            "key_sources": [],
                            "modified_at": "",
                            "pedestrian_preview_images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ],
                            "preview_images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ],
                            "score": 0
                        }
                    ],
                    "paging": {}
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBEntitiesByTimeSpace")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("camera_ids", camera_ids)
        intef.update_body("paging", paging)
        intef.update_body("period", period)
        intef.update_body("reversed", reversed)
        intef.update_body("types", types)
        return intef.request() if sendRequest else intef

    def entityDBGenerateCentroidPostApi(self, features=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GenerateCentroid """
        """  path: [post]/engine/entity-service/v1/generate_centroid API """
        """  body: 
                {
                    "features": [
                        {
                            "blob": "",
                            "type": "",
                            "version": 0
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "centroid": {}
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBGenerateCentroid")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("features", features)
        return intef.request() if sendRequest else intef

    def entityDBBatchDeleteTracksPostApi(self, is_async=None, track_delete_items=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDeleteTracks """
        """  path: [post]/engine/entity-service/v1/tracks/batch_delete API """
        """  body: 
                {
                    "is_async": false,
                    "track_delete_items": [
                        {
                            "camera_id": {},
                            "captured_time": "",
                            "cluster_id": "",
                            "track_id": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBBatchDeleteTracks")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("is_async", is_async)
        intef.update_body("track_delete_items", track_delete_items)
        return intef.request() if sendRequest else intef

    def entityDBTrackBatchGetPostApi(self, track_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TrackBatchGet """
        """  path: [post]/engine/entity-service/v1/tracks/batch_get API """
        """  body: 
                {
                    "track_ids": [
                        {
                            "object_id": "",
                            "sequence": 0,
                            "type": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ],
                    "tracks": [
                        {
                            "camera_id": {},
                            "captured_time": "",
                            "cluster_id": "",
                            "entity_id": {},
                            "extra_info": "",
                            "is_deleted": false,
                            "object": {},
                            "panoramic_image": {},
                            "portrait_image": {},
                            "track_id": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBTrackBatchGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("track_ids", track_ids)
        return intef.request() if sendRequest else intef

    def entityDBTracksByEntitySortedBySimilarityPostApi(self, camera_ids=None, entity_id=None, feature=None, period=None, top_k=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TracksByEntitySortedBySimilarity """
        """  path: [post]/engine/entity-service/v1/tracks_by_entity_sorted_by_similarity API """
        """  body: 
                {
                    "camera_ids": [
                        {
                            "camera_idx": 0,
                            "region_id": 0
                        }
                    ],
                    "entity_id": {},
                    "feature": {},
                    "period": {},
                    "top_k": 0
                }
        """
        """  resp:
                200():
                {
                    "tracks": [
                        {
                            "camera_id": {},
                            "captured_time": "",
                            "cluster_id": "",
                            "entity_id": {},
                            "extra_info": "",
                            "is_deleted": false,
                            "object": {},
                            "panoramic_image": {},
                            "portrait_image": {},
                            "track_id": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBTracksByEntitySortedBySimilarity")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("camera_ids", camera_ids)
        intef.update_body("entity_id", entity_id)
        intef.update_body("feature", feature)
        intef.update_body("period", period)
        intef.update_body("top_k", top_k)
        return intef.request() if sendRequest else intef

    def entityDBEntityListV2PostApi(self, paging=None, period=None, reversed=None, types=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  EntityListV2 """
        """  path: [post]/engine/entity-service/v2/entities API """
        """  body: 
                {
                    "paging": {},
                    "period": {},
                    "reversed": false,
                    "types": [
                        "[PERSON_ANONYMOUS]PERSON_ANONYMOUS/PERSON_IDENTIFIED"
                    ]
                }
        """
        """  resp:
                200():
                {
                    "entities": [
                        {
                            "created_at": "",
                            "entity_id": {},
                            "extra_info": "",
                            "key_sources": [],
                            "modified_at": "",
                            "pedestrian_preview_images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ],
                            "preview_images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ],
                            "score": 0
                        }
                    ],
                    "paging": {}
                }

        """
        intef = collections.interface("viperOpenApi", "entityDBEntityListV2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("paging", paging)
        intef.update_body("period", period)
        intef.update_body("reversed", reversed)
        intef.update_body("types", types)
        return intef.request() if sendRequest else intef



    def featureConvertBatchConvertFeaturePostApi(self, features=None, source_system=None, target_systems=None, target_version=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchConvertFeature """
        """  path: [post]/engine/feature-convert/v1/batch_convert_feature API """
        """  body: 
                {
                    "features": [
                        {
                            "blob": "",
                            "type": "",
                            "version": 0
                        }
                    ],
                    "source_system": "",
                    "target_systems": [],
                    "target_version": 0
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "features": [
                                {
                                    "blob": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "results": [
                                {
                                    "code": 0,
                                    "error": "",
                                    "status": {}
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "featureConvertBatchConvertFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("features", features)
        intef.update_body("source_system", source_system)
        intef.update_body("target_systems", target_systems)
        intef.update_body("target_version", target_version)
        return intef.request() if sendRequest else intef

    def imageEgressObjectDownloadGetApi(self, platform_id, object_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ObjectDownload """
        """  path: [get]/engine/image-egress/_/{platform_id}/{object_id} API """
        """  params: 

        """
        """  resp:
                200(以二进制形式在HTTP Body中返回对象内容.):
                ""

        """
        intef = collections.interface("viperOpenApi", "imageEgressObjectDownload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("platform_id", platform_id)
        intef.set_path_param("object_id", object_id)
        return intef.request() if sendRequest else intef

    def imageEgressManagerVIIDListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  VIIDList """
        """  path: [get]/engine/image-egress/manager/v1/viids API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "list": [
                        {
                            "config": {},
                            "status": {}
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "imageEgressManagerVIIDList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def imageEgressManagerVIIDDeleteDeleteApi(self, viid_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  VIIDDelete """
        """  path: [delete]/engine/image-egress/manager/v1/viids/{viid_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "imageEgressManagerVIIDDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("viid_id", viid_id)
        return intef.request() if sendRequest else intef

    def imageEgressManagerVIIDInfoGetApi(self, viid_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  VIIDInfo """
        """  path: [get]/engine/image-egress/manager/v1/viids/{viid_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "imageEgressManagerVIIDInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("viid_id", viid_id)
        return intef.request() if sendRequest else intef

    def imageEgressManagerVIIDAPEListGetApi(self, viid_id, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  VIIDAPEList """
        """  path: [get]/engine/image-egress/manager/v1/viids/{viid_id}/apes API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "ape_infos": [
                        {
                            "ape_uuid": "",
                            "item": {}
                        }
                    ],
                    "page": {},
                    "viid_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "imageEgressManagerVIIDAPEList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("viid_id", viid_id)
        return intef.request() if sendRequest else intef

    def imageEgressManagerBatchAddVIIDAPEPostApi(self, viid_id, ape_infos=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchAddVIIDAPE """
        """  path: [post]/engine/image-egress/manager/v1/viids/{viid_id}/apes API """
        """  body: 
                {
                    "ape_infos": [
                        {
                            "ape_uuid": "",
                            "item": {}
                        }
                    ],
                    "viid_id": ""
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageEgressManagerBatchAddVIIDAPE")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("viid_id", viid_id)
        intef.update_body("ape_infos", ape_infos)
        intef.update_body("viid_id", viid_id)
        return intef.request() if sendRequest else intef

    def imageEgressManagerBatchDelVIIDAPEPostApi(self, viid_id, ape_uuids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDelVIIDAPE """
        """  path: [post]/engine/image-egress/manager/v1/viids/{viid_id}/apes/delete API """
        """  body: 
                {
                    "ape_uuids": [],
                    "viid_id": ""
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageEgressManagerBatchDelVIIDAPE")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("viid_id", viid_id)
        intef.update_body("ape_uuids", ape_uuids)
        intef.update_body("viid_id", viid_id)
        return intef.request() if sendRequest else intef

    def imageEgressManagerVIIDSubscriptionListGetApi(self, viid_id, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  VIIDSubscriptionList """
        """  path: [get]/engine/image-egress/manager/v1/viids/{viid_id}/subscriptions API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "subscription_list": [
                        {
                            "applicant_name": "",
                            "applicant_org": "",
                            "begin_time": "",
                            "cancel_reason": "",
                            "cancel_time": "",
                            "end_time": "",
                            "extra_info": "",
                            "operator_type": "",
                            "reason": "",
                            "receive_addr": "",
                            "report_interval": "",
                            "resource_class": "",
                            "resource_uri": "",
                            "result_feature_declare": "",
                            "result_image_declare": "",
                            "subscribe_cancel_org": "",
                            "subscribe_cancel_person": "",
                            "subscribe_detail": "",
                            "subscribe_id": "",
                            "subscribe_status": "",
                            "tab_id": "",
                            "title": ""
                        }
                    ],
                    "viid_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "imageEgressManagerVIIDSubscriptionList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("viid_id", viid_id)
        return intef.request() if sendRequest else intef



    def imageEgressBatchPutObjectPostApi(self, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchPutObject """
        """  path: [post]/engine/image-egress/v1/batch_put_object API """
        """  body: 
                {
                    "requests": [
                        {
                            "object_info": {},
                            "platform_id": ""
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "panoramic_image_uri": "",
                            "portrait_image_uri": ""
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageEgressBatchPutObject")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageEgressObjectPutPostApi(self, platform_id, object_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ObjectPut """
        """  path: [post]/engine/image-egress/v1/objects/{platform_id} API """
        """  body: 
                {
                    "object_info": {},
                    "platform_id": ""
                }
        """
        """  resp:
                200():
                {
                    "panoramic_image_uri": "",
                    "portrait_image_uri": ""
                }

        """
        intef = collections.interface("viperOpenApi", "imageEgressObjectPut")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("platform_id", platform_id)
        intef.update_body("object_info", object_info)
        intef.update_body("platform_id", platform_id)
        return intef.request() if sendRequest else intef

    def imageEgressObjectGetGetApi(self, platform_id, object_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ObjectGet """
        """  path: [get]/engine/image-egress/v1/objects/{platform_id}/{object_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "blob": "",
                    "object_id": "",
                    "platform_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "imageEgressObjectGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("platform_id", platform_id)
        intef.set_path_param("object_id", object_id)
        return intef.request() if sendRequest else intef

    def imageIngressGAT1400SubscribeDeleteDeleteApi(self, task_id=None, subscribe_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GAT1400SubscribeDelete """
        """  path: [delete]/engine/image-ingress/v1/gat1400subscribe API """
        """  params: 
                参数名称：task_id　类型：string　描述：所属平台任务id.
                参数名称：subscribe_id　类型：string　描述：订阅id
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "imageIngressGAT1400SubscribeDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("task_id", task_id)
        intef.update_params("subscribe_id", subscribe_id)
        return intef.request() if sendRequest else intef

    def imageIngressGAT1400SubscribeNewPostApi(self, parameter=None, task_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GAT1400SubscribeNew """
        """  path: [post]/engine/image-ingress/v1/gat1400subscribe API """
        """  body: 
                {
                    "parameter": {},
                    "task_id": ""
                }
        """
        """  resp:
                200():
                {
                    "status_code": 0,
                    "status_string": "",
                    "subscribe_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "imageIngressGAT1400SubscribeNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("parameter", parameter)
        intef.update_body("task_id", task_id)
        return intef.request() if sendRequest else intef

    def imageIngressGetCamerasFromPlatformGetApi(self, task_id, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetCamerasFromPlatform """
        """  path: [get]/engine/image-ingress/v1/platforms/{task_id}/cameras API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条; 默认值为0.
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 总任务数, 请求无须填此参数, 响应时填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "platform_cameras": [
                        {
                            "gat1400": {},
                            "platform_type": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageIngressGetCamerasFromPlatform")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def imageIngressTaskListGetApi(self, page_request_offset=None, page_request_limit=None, page_request_total=None, is_passive=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskList """
        """  path: [get]/engine/image-ingress/v1/tasks API """
        """  params: 
                参数名称：page_request.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条; 默认值为0.
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page_request.limit　类型：integer　描述：长度, 取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page_request.total　类型：integer　描述：可选, 总任务数, 请求无须填此参数, 响应时填写.
                参数名称：is_passive　类型：boolean　描述：查询过滤flag: false表示只查询主动模式任务列表 true表示只查询被动模式任务列表, 默认值是false
        """
        """  resp:
                200():
                {
                    "page_response": {},
                    "tasks": [
                        {
                            "status": {},
                            "task": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageIngressTaskList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        intef.update_params("is_passive", is_passive)
        return intef.request() if sendRequest else intef

    def imageIngressTaskNewPostApi(self, task_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskNew """
        """  path: [post]/engine/image-ingress/v1/tasks API """
        """  body: 
                {
                    "task_request": {}
                }
        """
        """  resp:
                200():
                {
                    "task_response": {}
                }

        """
        intef = collections.interface("viperOpenApi", "imageIngressTaskNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task_request", task_request)
        return intef.request() if sendRequest else intef

    def imageIngressTaskDeleteDeleteApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskDelete """
        """  path: [delete]/engine/image-ingress/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "imageIngressTaskDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def imageIngressTaskStatusGetApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskStatus """
        """  path: [get]/engine/image-ingress/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "task": {}
                }

        """
        intef = collections.interface("viperOpenApi", "imageIngressTaskStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def imageFpachExtractBatchCompareFeaturePostApi(self, face_feature_version, pedestrian_feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchCompareFeature """
        """  path: [post]/engine/image-process/common_fpach_{face_feature_version}_{pedestrian_feature_version}/v1/batch_compare_feature API """
        """  body: 
                {
                    "requests": [
                        {
                            "one": {},
                            "other": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ],
                    "score": []
                }

        """
        intef = collections.interface("viperOpenApi", "imageFpachExtractBatchCompareFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFpachExtractBatchDetectPostApi(self, face_feature_version, pedestrian_feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetect """
        """  path: [post]/engine/image-process/common_fpach_{face_feature_version}_{pedestrian_feature_version}/v1/batch_detect API """
        """  body: 
                {
                    "requests": [
                        {
                            "detect_mode": {},
                            "image": {},
                            "image_type": {},
                            "object_type": [
                                "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "info": [
                                {
                                    "algo": {},
                                    "associations": [
                                        {
                                            "associated_object_info": {},
                                            "association_type": "",
                                            "object_id": "",
                                            "type": {}
                                        }
                                    ],
                                    "automobile": {},
                                    "carplate": {},
                                    "crowd": {},
                                    "cyclist": {},
                                    "diagnosis": {},
                                    "event": {},
                                    "face": {},
                                    "human_powered_vehicle": {},
                                    "object_id": "",
                                    "other": {},
                                    "pedestrian": {},
                                    "portrait_image_location": {},
                                    "trajectory": {},
                                    "type": {},
                                    "watercraft": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFpachExtractBatchDetect")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFpachExtractBatchDetectAndExtractAllPostApi(self, face_feature_version, pedestrian_feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetectAndExtractAll """
        """  path: [post]/engine/image-process/common_fpach_{face_feature_version}_{pedestrian_feature_version}/v1/batch_detect_and_extract_all API """
        """  body: 
                {
                    "requests": [
                        {
                            "detect_mode": {},
                            "image": {},
                            "image_type": {},
                            "object_type": [
                                "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "objects": [
                        {
                            "infos": [
                                {
                                    "face_score": 0,
                                    "feature": {},
                                    "object_info": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFpachExtractBatchDetectAndExtractAll")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFpachExtractBatchExtractWithLocationPostApi(self, face_feature_version, pedestrian_feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchExtractWithLocation """
        """  path: [post]/engine/image-process/common_fpach_{face_feature_version}_{pedestrian_feature_version}/v1/batch_extract_with_location API """
        """  body: 
                {
                    "requests": [
                        {
                            "bounding": {},
                            "image": {},
                            "object_type": [
                                "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                            ],
                            "points": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "objects": [
                        {
                            "infos": [
                                {
                                    "face_score": 0,
                                    "feature": {},
                                    "object_info": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFpachExtractBatchExtractWithLocation")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFpachExtractGetSystemInfoGetApi(self, face_feature_version, pedestrian_feature_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/image-process/common_fpach_{face_feature_version}_{pedestrian_feature_version}/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "models_info": {
                        "additionalProp1": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp2": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp3": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        }
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "imageFpachExtractGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        return intef.request() if sendRequest else intef

    def imageFaceExtractBatchCompareFeaturePostApi(self, feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchCompareFeature """
        """  path: [post]/engine/image-process/face_{feature_version}/v1/batch_compare_feature API """
        """  body: 
                {
                    "requests": [
                        {
                            "one": {},
                            "other": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "score": 0
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceExtractBatchCompareFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceExtractBatchDetectPostApi(self, feature_version, detect_mode=None, face_type=None, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetect """
        """  path: [post]/engine/image-process/face_{feature_version}/v1/batch_detect API """
        """  body: 
                {
                    "detect_mode": {},
                    "face_type": {},
                    "requests": [
                        {
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "face_info": [
                                {
                                    "algo": {},
                                    "associations": [
                                        {
                                            "associated_object_info": {},
                                            "association_type": "",
                                            "object_id": "",
                                            "type": {}
                                        }
                                    ],
                                    "automobile": {},
                                    "carplate": {},
                                    "crowd": {},
                                    "cyclist": {},
                                    "diagnosis": {},
                                    "event": {},
                                    "face": {},
                                    "human_powered_vehicle": {},
                                    "object_id": "",
                                    "other": {},
                                    "pedestrian": {},
                                    "portrait_image_location": {},
                                    "trajectory": {},
                                    "type": {},
                                    "watercraft": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceExtractBatchDetect")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("face_type", face_type)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceExtractBatchDetectAndExtractPostApi(self, feature_version, detect_mode=None, face_type=None, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetectAndExtract """
        """  path: [post]/engine/image-process/face_{feature_version}/v1/batch_detect_and_extract API """
        """  body: 
                {
                    "detect_mode": {},
                    "face_type": {},
                    "requests": [
                        {
                            "auto_rotation_thresh": 0,
                            "face_selection": {},
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "face_info": {},
                            "feature": {},
                            "images_orientation": {}
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceExtractBatchDetectAndExtract")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("face_type", face_type)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceExtractBatchDetectAndExtractAll2PostApi(self, feature_version, detect_mode=None, face_type=None, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetectAndExtractAll2 """
        """  path: [post]/engine/image-process/face_{feature_version}/v1/batch_detect_and_extract_all_2 API """
        """  body: 
                {
                    "detect_mode": {},
                    "face_type": {},
                    "requests": [
                        {
                            "auto_rotation_thresh": 0,
                            "face_selection": {},
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "responses": [
                                {
                                    "face_info": {},
                                    "feature": {},
                                    "images_orientation": {}
                                }
                            ],
                            "results": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceExtractBatchDetectAndExtractAll2")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("face_type", face_type)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceExtractBatchDetectAndExtractMultiModelPostApi(self, feature_version, detect_mode=None, face_type=None, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetectAndExtractMultiModel """
        """  path: [post]/engine/image-process/face_{feature_version}/v1/batch_detect_and_extract_multi_model API """
        """  body: 
                {
                    "detect_mode": {},
                    "face_type": {},
                    "requests": [
                        {
                            "auto_rotation_thresh": 0,
                            "face_selection": {},
                            "feature_versions": [],
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "face_info": {},
                            "features": [
                                {
                                    "blob": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "images_orientation": {},
                            "results": [
                                {
                                    "code": 0,
                                    "error": "",
                                    "status": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceExtractBatchDetectAndExtractMultiModel")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("face_type", face_type)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceExtractBatchDetectAndExtractAllPostApi(self, feature_version, detect_mode=None, face_type=None, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetectAndExtractAll """
        """  path: [post]/engine/image-process/face_{feature_version}/v1/batch_detect_and_extractall API """
        """  body: 
                {
                    "detect_mode": {},
                    "face_type": {},
                    "requests": [
                        {
                            "auto_rotation_thresh": 0,
                            "face_selection": {},
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "responses": [
                                {
                                    "face_info": {},
                                    "feature": {},
                                    "images_orientation": {}
                                }
                            ],
                            "results": [
                                {
                                    "code": 0,
                                    "error": "",
                                    "status": {}
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceExtractBatchDetectAndExtractAll")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("detect_mode", detect_mode)
        intef.update_body("face_type", face_type)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceExtractBatchExtractWithBoundingPostApi(self, feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchExtractWithBounding """
        """  path: [post]/engine/image-process/face_{feature_version}/v1/batch_extract_with_bounding API """
        """  body: 
                {
                    "requests": [
                        {
                            "bounding": {},
                            "crop_image": false,
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "align_score": 0,
                            "face_score": 0,
                            "feature": {}
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceExtractBatchExtractWithBounding")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceExtractBatchExtractWithPointsPostApi(self, feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchExtractWithPoints """
        """  path: [post]/engine/image-process/face_{feature_version}/v1/batch_extract_with_points API """
        """  body: 
                {
                    "requests": [
                        {
                            "image": {},
                            "points": [
                                {
                                    "x": 0,
                                    "y": 0
                                }
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "face_info": {},
                            "feature": {}
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceExtractBatchExtractWithPoints")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceExtractCompareFeaturePostApi(self, feature_version, one=None, other=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CompareFeature """
        """  path: [post]/engine/image-process/face_{feature_version}/v1/compare_feature API """
        """  body: 
                {
                    "one": {},
                    "other": {}
                }
        """
        """  resp:
                200():
                {
                    "score": 0
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceExtractCompareFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("one", one)
        intef.update_body("other", other)
        return intef.request() if sendRequest else intef

    def imageFaceExtractGetSystemInfoGetApi(self, feature_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/image-process/face_{feature_version}/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "models_info": {
                        "additionalProp1": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp2": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp3": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        }
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceExtractGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def imageFacepedExtratBatchCompareFeaturePostApi(self, face_feature_version, pedestrian_feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchCompareFeature """
        """  path: [post]/engine/image-process/faceped_{face_feature_version}_{pedestrian_feature_version}/v1/batch_compare_feature API """
        """  body: 
                {
                    "requests": [
                        {
                            "one": {},
                            "other": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "score": 0
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFacepedExtratBatchCompareFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFacepedExtratBatchDetectPostApi(self, face_feature_version, pedestrian_feature_version, mode=None, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetect """
        """  path: [post]/engine/image-process/faceped_{face_feature_version}_{pedestrian_feature_version}/v1/batch_detect API """
        """  body: 
                {
                    "mode": {},
                    "requests": [
                        {
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "info": [
                                {
                                    "algo": {},
                                    "associations": [
                                        {
                                            "associated_object_info": {},
                                            "association_type": "",
                                            "object_id": "",
                                            "type": {}
                                        }
                                    ],
                                    "automobile": {},
                                    "carplate": {},
                                    "crowd": {},
                                    "cyclist": {},
                                    "diagnosis": {},
                                    "event": {},
                                    "face": {},
                                    "human_powered_vehicle": {},
                                    "object_id": "",
                                    "other": {},
                                    "pedestrian": {},
                                    "portrait_image_location": {},
                                    "trajectory": {},
                                    "type": {},
                                    "watercraft": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFacepedExtratBatchDetect")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        intef.update_body("mode", mode)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFacepedExtratBatchDetectAndExtractPostApi(self, face_feature_version, pedestrian_feature_version, mode=None, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetectAndExtract """
        """  path: [post]/engine/image-process/faceped_{face_feature_version}_{pedestrian_feature_version}/v1/batch_detect_and_extract API """
        """  body: 
                {
                    "mode": {},
                    "requests": [
                        {
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "face": {
                                "feature": {},
                                "object_info": {}
                            }
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFacepedExtratBatchDetectAndExtract")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        intef.update_body("mode", mode)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFacepedExtratBatchDetectAndExtractAllPostApi(self, face_feature_version, pedestrian_feature_version, mode=None, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetectAndExtractAll """
        """  path: [post]/engine/image-process/faceped_{face_feature_version}_{pedestrian_feature_version}/v1/batch_detect_and_extract_all API """
        """  body: 
                {
                    "mode": {},
                    "requests": [
                        {
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "objects": [
                                {
                                    "feature": {},
                                    "object_info": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFacepedExtratBatchDetectAndExtractAll")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        intef.update_body("mode", mode)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFacepedExtratBatchExtractWithLocationPostApi(self, face_feature_version, pedestrian_feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchExtractWithLocation """
        """  path: [post]/engine/image-process/faceped_{face_feature_version}_{pedestrian_feature_version}/v1/batch_extract_with_location API """
        """  body: 
                {
                    "requests": [
                        {
                            "image": {},
                            "object_type": {},
                            "points": [
                                {
                                    "x": 0,
                                    "y": 0
                                }
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "feature": {},
                            "score": 0
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFacepedExtratBatchExtractWithLocation")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFacepedExtratGetSystemInfoGetApi(self, face_feature_version, pedestrian_feature_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/image-process/faceped_{face_feature_version}_{pedestrian_feature_version}/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "models_info": {
                        "additionalProp1": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp2": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp3": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        }
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "imageFacepedExtratGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("face_feature_version", face_feature_version)
        intef.set_path_param("pedestrian_feature_version", pedestrian_feature_version)
        return intef.request() if sendRequest else intef

    def imageFaceVehicleExtractBatchCompareFeaturePostApi(self, feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchCompareFeature """
        """  path: [post]/engine/image-process/facevehicle_{feature_version}/v1/batch_compare_feature API """
        """  body: 
                {
                    "requests": [
                        {
                            "one": {},
                            "other": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ],
                    "score": []
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceVehicleExtractBatchCompareFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceVehicleExtractBatchDetectPostApi(self, feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetect """
        """  path: [post]/engine/image-process/facevehicle_{feature_version}/v1/batch_detect API """
        """  body: 
                {
                    "requests": [
                        {
                            "detect_mode": {},
                            "image": {},
                            "image_type": {},
                            "object_type": [
                                "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "info": [
                                {
                                    "algo": {},
                                    "associations": [
                                        {
                                            "associated_object_info": {},
                                            "association_type": "",
                                            "object_id": "",
                                            "type": {}
                                        }
                                    ],
                                    "automobile": {},
                                    "carplate": {},
                                    "crowd": {},
                                    "cyclist": {},
                                    "diagnosis": {},
                                    "event": {},
                                    "face": {},
                                    "human_powered_vehicle": {},
                                    "object_id": "",
                                    "other": {},
                                    "pedestrian": {},
                                    "portrait_image_location": {},
                                    "trajectory": {},
                                    "type": {},
                                    "watercraft": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceVehicleExtractBatchDetect")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceVehicleExtractBatchDetectAndExtractAllPostApi(self, feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetectAndExtractAll """
        """  path: [post]/engine/image-process/facevehicle_{feature_version}/v1/batch_detect_and_extract_all API """
        """  body: 
                {
                    "requests": [
                        {
                            "detect_mode": {},
                            "image": {},
                            "image_type": {},
                            "object_type": [
                                "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "objects": [
                        {
                            "infos": [
                                {
                                    "face_score": 0,
                                    "feature": {},
                                    "object_info": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceVehicleExtractBatchDetectAndExtractAll")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceVehicleExtractBatchExtractWithLocationPostApi(self, feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchExtractWithLocation """
        """  path: [post]/engine/image-process/facevehicle_{feature_version}/v1/batch_extract_with_location API """
        """  body: 
                {
                    "requests": [
                        {
                            "bounding": {},
                            "image": {},
                            "object_type": [
                                "[OBJECT_UNKNOWN]OBJECT_UNKNOWN/OBJECT_FACE/OBJECT_PEDESTRIAN/OBJECT_AUTOMOBILE/OBJECT_CYCLIST/OBJECT_HUMAN_POWERED_VEHICLE/OBJECT_SCENARIO/OBJECT_CROWD/OBJECT_ALGO/OBJECT_SNAPSHOT/OBJECT_FACE_EXTEND_PEDESTRIAN/OBJECT_EVENT/OBJECT_VIDEO_SOURCE_DIAGNOSIS/OBJECT_AUTOMOBILE_DETECT/OBJECT_CARPLATE/OBJECT_AUTOMOBILE_IR/OBJECT_FACE_EXTEND_PEDESTRIAN_NON_AUTOMOBILE/OBJECT_WATERCRAFT/OBJECT_FILTERED/OBJECT_MULTI_PACH/OBJECT_SCENARIO_CITY_MANAGEMENT/OBJECT_FACE_PEDESTRIAN/OBJECT_SCENARIO_AUTOMOBILE_THROW/OBJECT_MULTI_FACE_PACH/OBJECT_TRAFFIC_AUTOMOBILE_COUNT/OBJECT_TRAFFIC_MULTI_PACH/OBJECT_HUMAN_ACTION/OBJECT_TRAFFIC_ANOMALY_EVENT/OBJECT_TRAFFIC_CAMERA_VISION_INFO/OBJECT_OTHER"
                            ],
                            "points": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "objects": [
                        {
                            "infos": [
                                {
                                    "face_score": 0,
                                    "feature": {},
                                    "object_info": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceVehicleExtractBatchExtractWithLocation")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageFaceVehicleExtractGetSystemInfoGetApi(self, feature_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/image-process/facevehicle_{feature_version}/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "models_info": {
                        "additionalProp1": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp2": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp3": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        }
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "imageFaceVehicleExtractGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def imageStructExtractBatchCompareFeaturePostApi(self, feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchCompareFeature """
        """  path: [post]/engine/image-process/multi_pach_{feature_version}/v1/batch_compare_feature API """
        """  body: 
                {
                    "requests": [
                        {
                            "one": {},
                            "other": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "score": 0
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageStructExtractBatchCompareFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageStructExtractBatchDetectPostApi(self, feature_version, mode=None, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetect """
        """  path: [post]/engine/image-process/multi_pach_{feature_version}/v1/batch_detect API """
        """  body: 
                {
                    "mode": {},
                    "requests": [
                        {
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_infos": [
                                {
                                    "algo": {},
                                    "associations": [
                                        {
                                            "associated_object_info": {},
                                            "association_type": "",
                                            "object_id": "",
                                            "type": {}
                                        }
                                    ],
                                    "automobile": {},
                                    "carplate": {},
                                    "crowd": {},
                                    "cyclist": {},
                                    "diagnosis": {},
                                    "event": {},
                                    "face": {},
                                    "human_powered_vehicle": {},
                                    "object_id": "",
                                    "other": {},
                                    "pedestrian": {},
                                    "portrait_image_location": {},
                                    "trajectory": {},
                                    "type": {},
                                    "watercraft": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageStructExtractBatchDetect")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("mode", mode)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageStructExtractBatchDetectAndExtractPostApi(self, feature_version, mode=None, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDetectAndExtract """
        """  path: [post]/engine/image-process/multi_pach_{feature_version}/v1/batch_detect_and_extract API """
        """  body: 
                {
                    "mode": {},
                    "requests": [
                        {
                            "image": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "objects": [
                                {
                                    "feature": {},
                                    "object_info": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageStructExtractBatchDetectAndExtract")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("mode", mode)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageStructExtractBatchExtractWithBoundingPostApi(self, feature_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchExtractWithBounding """
        """  path: [post]/engine/image-process/multi_pach_{feature_version}/v1/batch_extract_with_bounding API """
        """  body: 
                {
                    "requests": [
                        {
                            "bounding": {},
                            "crop_image": false,
                            "image": {},
                            "object_type": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "feature": {},
                            "object_info": {}
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageStructExtractBatchExtractWithBounding")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageStructExtractGetSystemInfoGetApi(self, feature_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/image-process/multi_pach_{feature_version}/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "models_info": {
                        "additionalProp1": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp2": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp3": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        }
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "imageStructExtractGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def imageOCRExtractBatchCustomTemplatePostApi(self, images=None, template_data=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchCustomTemplate """
        """  path: [post]/engine/image-process/ocr/v1/batch_custom_template_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "template_data": "",
                    "type": {}
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {},
                                    "textline": {},
                                    "type": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageOCRExtractBatchCustomTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("images", images)
        intef.update_body("template_data", template_data)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def imageOCRExtractBatchPlainTextPostApi(self, images=None, region_type=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchPlainText """
        """  path: [post]/engine/image-process/ocr/v1/batch_plaintext_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "region_type": {},
                    "type": {}
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {},
                                    "textline": {},
                                    "type": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageOCRExtractBatchPlainText")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("images", images)
        intef.update_body("region_type", region_type)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def imageOCRExtractBatchSpecialTemplatePostApi(self, images=None, template_db_ids=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchSpecialTemplate """
        """  path: [post]/engine/image-process/ocr/v1/batch_special_template_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "template_db_ids": [],
                    "type": {}
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {},
                                    "textline": {},
                                    "type": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageOCRExtractBatchSpecialTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("images", images)
        intef.update_body("template_db_ids", template_db_ids)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def imageOCRExtractBatchTemplatePostApi(self, images=None, region_type=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchTemplate """
        """  path: [post]/engine/image-process/ocr/v1/batch_template_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "region_type": {},
                    "type": ""
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {},
                                    "textline": {},
                                    "type": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageOCRExtractBatchTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("images", images)
        intef.update_body("region_type", region_type)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def imageOCRExtractGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/image-process/ocr/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "custom_template": [],
                    "models_info": {
                        "additionalProp1": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp2": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        },
                        "additionalProp3": {
                            "models": [
                                {
                                    "err_msg": "",
                                    "name": "",
                                    "oid": "",
                                    "path": "",
                                    "type": "",
                                    "version": 0
                                }
                            ],
                            "status": ""
                        }
                    },
                    "region_info": {
                        "additionalProp1": {
                            "plain_text": [],
                            "template": []
                        },
                        "additionalProp2": {
                            "plain_text": [],
                            "template": []
                        },
                        "additionalProp3": {
                            "plain_text": [],
                            "template": []
                        }
                    },
                    "special_template": []
                }

        """
        intef = collections.interface("viperOpenApi", "imageOCRExtractGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def imageAlgoProcessBatchProcessPostApi(self, app_id, app_version, requests=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchProcess """
        """  path: [post]/engine/image-process/{app_id}-{app_version}/v1/batch_process API """
        """  body: 
                {
                    "requests": [
                        {
                            "config": {},
                            "images": [
                                {
                                    "cache_url": "",
                                    "data": "",
                                    "format": {},
                                    "image_id": "",
                                    "url": ""
                                }
                            ]
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "response": {
                                "type_url": "",
                                "value": ""
                            },
                            "response_items": [
                                {
                                    "type_url": "",
                                    "value": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "imageAlgoProcessBatchProcess")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("app_id", app_id)
        intef.set_path_param("app_version", app_version)
        intef.update_body("requests", requests)
        return intef.request() if sendRequest else intef

    def imageAlgoProcessGetSystemInfoGetApi(self, app_id, app_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/image-process/{app_id}-{app_version}/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "app_name": "",
                    "app_version": 0,
                    "load": {},
                    "models_info": {
                        "additionalProp1": {
                            "err_msg": "",
                            "name": "",
                            "oid": "",
                            "path": "",
                            "type": "",
                            "version": 0
                        },
                        "additionalProp2": {
                            "err_msg": "",
                            "name": "",
                            "oid": "",
                            "path": "",
                            "type": "",
                            "version": 0
                        },
                        "additionalProp3": {
                            "err_msg": "",
                            "name": "",
                            "oid": "",
                            "path": "",
                            "type": "",
                            "version": 0
                        }
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "imageAlgoProcessGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("app_id", app_id)
        intef.set_path_param("app_version", app_version)
        return intef.request() if sendRequest else intef

    def ocrApiWrapperBatchOCRCustomTemplatePostApi(self, images=None, template_data=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchOCRCustomTemplate """
        """  path: [post]/engine/ocr-api-wrapper/v1/batch_custom_template_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "template_data": "",
                    "type": {}
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {},
                                    "textline": {},
                                    "type": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "ocrApiWrapperBatchOCRCustomTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("images", images)
        intef.update_body("template_data", template_data)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def ocrApiWrapperBatchOCRPlainTextPostApi(self, images=None, region_type=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchOCRPlainText """
        """  path: [post]/engine/ocr-api-wrapper/v1/batch_plaintext_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "region_type": {},
                    "type": {}
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {},
                                    "textline": {},
                                    "type": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "ocrApiWrapperBatchOCRPlainText")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("images", images)
        intef.update_body("region_type", region_type)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def ocrApiWrapperBatchOCRSpecialTemplatePostApi(self, images=None, template_db_ids=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchOCRSpecialTemplate """
        """  path: [post]/engine/ocr-api-wrapper/v1/batch_special_template_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "template_db_ids": [],
                    "type": {}
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {},
                                    "textline": {},
                                    "type": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "ocrApiWrapperBatchOCRSpecialTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("images", images)
        intef.update_body("template_db_ids", template_db_ids)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def ocrApiWrapperBatchOCRTemplatePostApi(self, images=None, region_type=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchOCRTemplate """
        """  path: [post]/engine/ocr-api-wrapper/v1/batch_template_extract API """
        """  body: 
                {
                    "images": [
                        {
                            "cache_url": "",
                            "data": "",
                            "format": {},
                            "image_id": "",
                            "url": ""
                        }
                    ],
                    "region_type": {},
                    "type": ""
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "object_array": [
                                {
                                    "classification_score": 0,
                                    "document_retrieve_feature": {
                                        "blob": "",
                                        "type": "",
                                        "version": 0
                                    },
                                    "extra_type": "",
                                    "form_line": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "key_points": [
                                        {
                                            "x": 0,
                                            "y": 0
                                        }
                                    ],
                                    "object_detection_info": {
                                        "confidence": 0,
                                        "id": 0,
                                        "label": 0,
                                        "roi": [
                                            {
                                                "x": 0,
                                                "y": 0
                                            }
                                        ]
                                    },
                                    "rectify_matrix": {},
                                    "textline": {},
                                    "type": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "ocrApiWrapperBatchOCRTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("images", images)
        intef.update_body("region_type", region_type)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def ocrApiWrapperOCRCustomTemplatePostApi(self, image=None, template_data=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  OCRCustomTemplate """
        """  path: [post]/engine/ocr-api-wrapper/v1/custom_template_extract API """
        """  body: 
                {
                    "image": {},
                    "template_data": "",
                    "type": {}
                }
        """
        """  resp:
                200():
                {
                    "object_array": [
                        {
                            "classification_score": 0,
                            "document_retrieve_feature": {
                                "blob": "",
                                "type": "",
                                "version": 0
                            },
                            "extra_type": "",
                            "form_line": [
                                {
                                    "x": 0,
                                    "y": 0
                                }
                            ],
                            "key_points": [
                                {
                                    "x": 0,
                                    "y": 0
                                }
                            ],
                            "object_detection_info": {
                                "confidence": 0,
                                "id": 0,
                                "label": 0,
                                "roi": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ]
                            },
                            "rectify_matrix": {},
                            "textline": {},
                            "type": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "ocrApiWrapperOCRCustomTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("template_data", template_data)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def ocrApiWrapperOCRPlainTextPostApi(self, image=None, region_type=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  OCRPlainText """
        """  path: [post]/engine/ocr-api-wrapper/v1/plaintext_extract API """
        """  body: 
                {
                    "image": {},
                    "region_type": {},
                    "type": {}
                }
        """
        """  resp:
                200():
                {
                    "object_array": [
                        {
                            "classification_score": 0,
                            "document_retrieve_feature": {
                                "blob": "",
                                "type": "",
                                "version": 0
                            },
                            "extra_type": "",
                            "form_line": [
                                {
                                    "x": 0,
                                    "y": 0
                                }
                            ],
                            "key_points": [
                                {
                                    "x": 0,
                                    "y": 0
                                }
                            ],
                            "object_detection_info": {
                                "confidence": 0,
                                "id": 0,
                                "label": 0,
                                "roi": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ]
                            },
                            "rectify_matrix": {},
                            "textline": {},
                            "type": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "ocrApiWrapperOCRPlainText")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("region_type", region_type)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def ocrApiWrapperOCRSpecialTemplatePostApi(self, image=None, template_db_ids=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  OCRSpecialTemplate """
        """  path: [post]/engine/ocr-api-wrapper/v1/special_template_extract API """
        """  body: 
                {
                    "image": {},
                    "template_db_ids": [],
                    "type": {}
                }
        """
        """  resp:
                200():
                {
                    "object_array": [
                        {
                            "classification_score": 0,
                            "document_retrieve_feature": {
                                "blob": "",
                                "type": "",
                                "version": 0
                            },
                            "extra_type": "",
                            "form_line": [
                                {
                                    "x": 0,
                                    "y": 0
                                }
                            ],
                            "key_points": [
                                {
                                    "x": 0,
                                    "y": 0
                                }
                            ],
                            "object_detection_info": {
                                "confidence": 0,
                                "id": 0,
                                "label": 0,
                                "roi": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ]
                            },
                            "rectify_matrix": {},
                            "textline": {},
                            "type": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "ocrApiWrapperOCRSpecialTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("template_db_ids", template_db_ids)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def ocrApiWrapperOCRTemplatePostApi(self, image=None, region_type=None, type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  OCRTemplate """
        """  path: [post]/engine/ocr-api-wrapper/v1/template_extract API """
        """  body: 
                {
                    "image": {},
                    "region_type": {},
                    "type": ""
                }
        """
        """  resp:
                200():
                {
                    "object_array": [
                        {
                            "classification_score": 0,
                            "document_retrieve_feature": {
                                "blob": "",
                                "type": "",
                                "version": 0
                            },
                            "extra_type": "",
                            "form_line": [
                                {
                                    "x": 0,
                                    "y": 0
                                }
                            ],
                            "key_points": [
                                {
                                    "x": 0,
                                    "y": 0
                                }
                            ],
                            "object_detection_info": {
                                "confidence": 0,
                                "id": 0,
                                "label": 0,
                                "roi": [
                                    {
                                        "x": 0,
                                        "y": 0
                                    }
                                ]
                            },
                            "rectify_matrix": {},
                            "textline": {},
                            "type": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "ocrApiWrapperOCRTemplate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image", image)
        intef.update_body("region_type", region_type)
        intef.update_body("type", type)
        return intef.request() if sendRequest else intef

    def kafkaCallbackGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/process-http-callback/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "kafka_comsumer_group": "",
                    "kafka_topics": [],
                    "statistics": {},
                    "transport_config": {},
                    "url": ""
                }

        """
        intef = collections.interface("viperOpenApi", "kafkaCallbackGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def kafkaCallbackSetCallbackURLPostApi(self, transport_config=None, url=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  SetCallbackURL """
        """  path: [post]/engine/process-http-callback/v1/set_callback_url API """
        """  body: 
                {
                    "transport_config": {},
                    "url": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "kafkaCallbackSetCallbackURL")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("transport_config", transport_config)
        intef.update_body("url", url)
        return intef.request() if sendRequest else intef

    def protocolIngressBatchDeleteDevicePostApi(self, device_uuids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchDeleteDevice """
        """  path: [post]/engine/protocol-ingress/v1/batch_delete_device API """
        """  body: 
                {
                    "device_uuids": []
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressBatchDeleteDevice")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_uuids", device_uuids)
        return intef.request() if sendRequest else intef

    def protocolIngressBatchNewDevicePostApi(self, devices=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchNewDevice """
        """  path: [post]/engine/protocol-ingress/v1/batch_new_device API """
        """  body: 
                {
                    "devices": [
                        {
                            "device_id": "",
                            "device_parameter": {},
                            "device_type": {},
                            "device_uuid": "",
                            "display_name": "",
                            "source_type": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "devices": [
                        {
                            "created_at": "",
                            "device_id": "",
                            "device_parameter": {},
                            "device_type": {},
                            "device_uuid": "",
                            "display_name": "",
                            "source_type": {},
                            "status": {},
                            "updated_at": ""
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressBatchNewDevice")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("devices", devices)
        return intef.request() if sendRequest else intef



    def protocolIngressDeviceDeleteDeleteApi(self, device_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeviceDelete """
        """  path: [delete]/engine/protocol-ingress/v1/devices/{device_uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressDeviceDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        return intef.request() if sendRequest else intef

    def protocolIngressDeviceInfoGetApi(self, device_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeviceInfo """
        """  path: [get]/engine/protocol-ingress/v1/devices/{device_uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "device": {}
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressDeviceInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        return intef.request() if sendRequest else intef

    def protocolIngressAbsolutePTZMovePutApi(self, device_uuid, position=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AbsolutePTZMove """
        """  path: [put]/engine/protocol-ingress/v1/devices/{device_uuid}/absolute_ptz_move API """
        """  body: 
                {
                    "device_uuid": "",
                    "position": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressAbsolutePTZMove")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("position", position)
        return intef.request() if sendRequest else intef

    def protocolIngressAbsolutePTZPositionGetApi(self, device_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AbsolutePTZPosition """
        """  path: [get]/engine/protocol-ingress/v1/devices/{device_uuid}/absolute_ptz_position API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "position": {}
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressAbsolutePTZPosition")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        return intef.request() if sendRequest else intef

    def protocolIngressDeviceCatalogListGetApi(self, device_uuid, page_offset=None, page_limit=None, page_total=None, item_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeviceCatalogList """
        """  path: [get]/engine/protocol-ingress/v1/devices/{device_uuid}/catalog_items API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
                参数名称：item_type　类型：string　描述：可选，根据目录项类型来过滤结果 [SINCE v5.1.0]
        """
        """  resp:
                200():
                {
                    "devices": [
                        {
                            "created_at": "",
                            "device_id": "",
                            "device_parameter": {},
                            "device_type": {},
                            "device_uuid": "",
                            "display_name": "",
                            "source_type": {},
                            "status": {},
                            "updated_at": ""
                        }
                    ],
                    "items": [
                        {
                            "item_type": {},
                            "parameter": {}
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressDeviceCatalogList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.update_params("item_type", item_type)
        intef.set_path_param("device_uuid", device_uuid)
        return intef.request() if sendRequest else intef

    def protocolIngressDeviceCatalogSendPutApi(self, device_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeviceCatalogSend """
        """  path: [put]/engine/protocol-ingress/v1/devices/{device_uuid}/catalog_send API """
        """  body: 
                {}
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressDeviceCatalogSend")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        return intef.request() if sendRequest else intef

    def protocolIngressFIControlPutApi(self, device_uuid, focus=None, iris=None, stop_enable=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FIControl """
        """  path: [put]/engine/protocol-ingress/v1/devices/{device_uuid}/fi_control API """
        """  body: 
                {
                    "device_uuid": "",
                    "focus": {},
                    "iris": {},
                    "stop_enable": false
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressFIControl")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("focus", focus)
        intef.update_body("iris", iris)
        intef.update_body("stop_enable", stop_enable)
        return intef.request() if sendRequest else intef

    def protocolIngressDeviceMediaInfoGetApi(self, device_uuid, stream_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeviceMediaInfo """
        """  path: [get]/engine/protocol-ingress/v1/devices/{device_uuid}/media_info API """
        """  params: 
                参数名称：stream_type　类型：string　描述：可选, 码流类型, 目前只有 ONVIF 直连摄像机支持
        """
        """  resp:
                200():
                {
                    "media": {}
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressDeviceMediaInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("stream_type", stream_type)
        intef.set_path_param("device_uuid", device_uuid)
        return intef.request() if sendRequest else intef

    def protocolIngressPresetListGetApi(self, device_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PresetList """
        """  path: [get]/engine/protocol-ingress/v1/devices/{device_uuid}/presets API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "device_uuid": "",
                    "presets": [
                        {
                            "name": "",
                            "position": {},
                            "preset_id": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressPresetList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        return intef.request() if sendRequest else intef

    def protocolIngressPresetSetPutApi(self, device_uuid, preset=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PresetSet """
        """  path: [put]/engine/protocol-ingress/v1/devices/{device_uuid}/presets API """
        """  body: 
                {
                    "device_uuid": "",
                    "preset": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressPresetSet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("preset", preset)
        return intef.request() if sendRequest else intef

    def protocolIngressPresetDeleteDeleteApi(self, device_uuid, preset_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PresetDelete """
        """  path: [delete]/engine/protocol-ingress/v1/devices/{device_uuid}/presets/{preset_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressPresetDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.set_path_param("preset_id", preset_id)
        return intef.request() if sendRequest else intef

    def protocolIngressPresetGotoPutApi(self, device_uuid, preset_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PresetGoto """
        """  path: [put]/engine/protocol-ingress/v1/devices/{device_uuid}/presets/{preset_id}/goto API """
        """  body: 
                {
                    "device_uuid": "",
                    "preset_id": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressPresetGoto")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.set_path_param("preset_id", preset_id)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("preset_id", preset_id)
        return intef.request() if sendRequest else intef

    def protocolIngressHomePositionSetPutApi(self, device_uuid, preset_id, enabled=None, reset_time=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  HomePositionSet """
        """  path: [put]/engine/protocol-ingress/v1/devices/{device_uuid}/presets/{preset_id}/home_position_set API """
        """  body: 
                {
                    "device_uuid": "",
                    "enabled": false,
                    "preset_id": "",
                    "reset_time": 0
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressHomePositionSet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.set_path_param("preset_id", preset_id)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("enabled", enabled)
        intef.update_body("preset_id", preset_id)
        intef.update_body("reset_time", reset_time)
        return intef.request() if sendRequest else intef

    def protocolIngressPTZControlPutApi(self, device_uuid, pan=None, stop_enable=None, tilt=None, zoom=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PTZControl """
        """  path: [put]/engine/protocol-ingress/v1/devices/{device_uuid}/ptz_control API """
        """  body: 
                {
                    "device_uuid": "",
                    "pan": {},
                    "stop_enable": false,
                    "tilt": {},
                    "zoom": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressPTZControl")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("pan", pan)
        intef.update_body("stop_enable", stop_enable)
        intef.update_body("tilt", tilt)
        intef.update_body("zoom", zoom)
        return intef.request() if sendRequest else intef

    def protocolIngressPTZControlTransparentPutApi(self, device_uuid, ptz_command=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  PTZControlTransparent """
        """  path: [put]/engine/protocol-ingress/v1/devices/{device_uuid}/ptz_control_transparent API """
        """  body: 
                {
                    "device_uuid": "",
                    "ptz_command": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressPTZControlTransparent")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("ptz_command", ptz_command)
        return intef.request() if sendRequest else intef

    def protocolIngressRecordInfoPostApi(self, device_uuid, address=None, file_path=None, record_type=None, recorder_id=None, secrecy=None, start_time=None, stop_time=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  RecordInfo """
        """  path: [post]/engine/protocol-ingress/v1/devices/{device_uuid}/record_info API """
        """  body: 
                {
                    "address": "",
                    "device_uuid": "",
                    "file_path": "",
                    "record_type": {},
                    "recorder_id": "",
                    "secrecy": 0,
                    "start_time": "",
                    "stop_time": ""
                }
        """
        """  resp:
                200():
                {
                    "device_uuid": "",
                    "records": [
                        {
                            "address": "",
                            "device_id": "",
                            "file_path": "",
                            "file_size": "",
                            "name": "",
                            "record_type": {},
                            "recorder_id": "",
                            "secrecy": 0,
                            "start_time": "",
                            "stop_time": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressRecordInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.update_body("address", address)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("file_path", file_path)
        intef.update_body("record_type", record_type)
        intef.update_body("recorder_id", recorder_id)
        intef.update_body("secrecy", secrecy)
        intef.update_body("start_time", start_time)
        intef.update_body("stop_time", stop_time)
        return intef.request() if sendRequest else intef

    def protocolIngressDeviceSubscribePostApi(self, device_uuid, event=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeviceSubscribe """
        """  path: [post]/engine/protocol-ingress/v1/devices/{device_uuid}/subscribe API """
        """  body: 
                {
                    "device_uuid": "",
                    "event": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressDeviceSubscribe")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("event", event)
        return intef.request() if sendRequest else intef

    def protocolIngressTeleBootPutApi(self, device_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TeleBoot """
        """  path: [put]/engine/protocol-ingress/v1/devices/{device_uuid}/tele_boot API """
        """  body: 
                {
                    "device_uuid": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressTeleBoot")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.update_body("device_uuid", device_uuid)
        return intef.request() if sendRequest else intef

    def protocolIngressDeviceUnsubscribePostApi(self, device_uuid, event=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeviceUnsubscribe """
        """  path: [post]/engine/protocol-ingress/v1/devices/{device_uuid}/unsubscribe API """
        """  body: 
                {
                    "device_uuid": "",
                    "event": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressDeviceUnsubscribe")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("device_uuid", device_uuid)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("event", event)
        return intef.request() if sendRequest else intef

    def protocolIngressDeviceSearchPostApi(self, device_type=None, device_uuid=None, page=None, source_type=None, video_source=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeviceSearch """
        """  path: [post]/engine/protocol-ingress/v1/devices_search API """
        """  body: 
                {
                    "device_type": {},
                    "device_uuid": "",
                    "page": {},
                    "source_type": {},
                    "video_source": {}
                }
        """
        """  resp:
                200():
                {
                    "devices": [
                        {
                            "created_at": "",
                            "device_id": "",
                            "device_parameter": {},
                            "device_type": {},
                            "device_uuid": "",
                            "display_name": "",
                            "source_type": {},
                            "status": {},
                            "updated_at": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressDeviceSearch")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("device_type", device_type)
        intef.update_body("device_uuid", device_uuid)
        intef.update_body("page", page)
        intef.update_body("source_type", source_type)
        intef.update_body("video_source", video_source)
        return intef.request() if sendRequest else intef

    def protocolIngressGB28181LocalConfigListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GB28181LocalConfigList """
        """  path: [get]/engine/protocol-ingress/v1/gb28181_local_configs API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "configs": [
                        {
                            "created_at": "",
                            "device_id": "",
                            "ip": "",
                            "local_uuid": "",
                            "port": 0
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressGB28181LocalConfigList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef



    def protocolIngressGB28181LocalConfigDeleteDeleteApi(self, local_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GB28181LocalConfigDelete """
        """  path: [delete]/engine/protocol-ingress/v1/gb28181_local_configs/{local_uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "protocolIngressGB28181LocalConfigDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("local_uuid", local_uuid)
        return intef.request() if sendRequest else intef

    def protocolIngressGB28181LocalConfigInfoGetApi(self, local_uuid, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GB28181LocalConfigInfo """
        """  path: [get]/engine/protocol-ingress/v1/gb28181_local_configs/{local_uuid} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "config": {}
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressGB28181LocalConfigInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("local_uuid", local_uuid)
        return intef.request() if sendRequest else intef

    def protocolIngressGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/protocol-ingress/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "device_statistics": {},
                    "node_statistics": {}
                }

        """
        intef = collections.interface("viperOpenApi", "protocolIngressGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def shortVideoStorageDataRecordDownloadGetApi(self, record_url, format=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  RecordDownload """
        """  path: [get]/engine/short-video-storage-data/_/{record_url} API """
        """  params: 
                参数名称：format　类型：string　描述：可选, 输出视频类型, 取值: mp4, hls; 默认值为mp4
        """
        """  resp:
                200(以二进制形式在HTTP Body中返回对象内容.):
                ""

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageDataRecordDownload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("format", format)
        intef.set_path_param("record_url", record_url)
        return intef.request() if sendRequest else intef

    def shortVideoStorageImageNewPostApi(self, image_times=None, ns_id=None, request_id=None, stream_id=None, task_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ImageNew """
        """  path: [post]/engine/short-video-storage/v1/images API """
        """  body: 
                {
                    "image_times": [],
                    "ns_id": "",
                    "request_id": "",
                    "stream_id": "",
                    "task_id": ""
                }
        """
        """  resp:
                200():
                {
                    "error_message": "",
                    "results": [
                        {
                            "data": "",
                            "image_time": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageImageNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("image_times", image_times)
        intef.update_body("ns_id", ns_id)
        intef.update_body("request_id", request_id)
        intef.update_body("stream_id", stream_id)
        intef.update_body("task_id", task_id)
        return intef.request() if sendRequest else intef

    def shortVideoStorageRecordListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  RecordList """
        """  path: [get]/engine/short-video-storage/v1/records API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "records": [
                        {
                            "append_record_seconds": 0,
                            "creation_time": "",
                            "error_message": "",
                            "ns_id": "",
                            "prerecord_seconds": 0,
                            "record_at": "",
                            "record_id": "",
                            "record_status": {},
                            "record_url": "",
                            "stream_id": "",
                            "task_id": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageRecordList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def shortVideoStorageRecordNewPostApi(self, append_record_seconds=None, ns_id=None, prerecord_seconds=None, record_at=None, record_id=None, stream_id=None, task_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  RecordNew """
        """  path: [post]/engine/short-video-storage/v1/records API """
        """  body: 
                {
                    "append_record_seconds": 0,
                    "ns_id": "",
                    "prerecord_seconds": 0,
                    "record_at": "",
                    "record_id": "",
                    "stream_id": "",
                    "task_id": ""
                }
        """
        """  resp:
                200():
                {
                    "record_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageRecordNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("append_record_seconds", append_record_seconds)
        intef.update_body("ns_id", ns_id)
        intef.update_body("prerecord_seconds", prerecord_seconds)
        intef.update_body("record_at", record_at)
        intef.update_body("record_id", record_id)
        intef.update_body("stream_id", stream_id)
        intef.update_body("task_id", task_id)
        return intef.request() if sendRequest else intef

    def shortVideoStorageRecordDeleteDeleteApi(self, record_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  RecordDelete """
        """  path: [delete]/engine/short-video-storage/v1/records/{record_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageRecordDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("record_id", record_id)
        return intef.request() if sendRequest else intef

    def shortVideoStorageRecordInfoGetApi(self, record_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  RecordInfo """
        """  path: [get]/engine/short-video-storage/v1/records/{record_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "record_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageRecordInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("record_id", record_id)
        return intef.request() if sendRequest else intef

    def shortVideoStorageSearchRecordsPostApi(self, object_id=None, page=None, record_at=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  SearchRecords """
        """  path: [post]/engine/short-video-storage/v1/search_records API """
        """  body: 
                {
                    "object_id": "",
                    "page": {},
                    "record_at": ""
                }
        """
        """  resp:
                200():
                {
                    "page": {},
                    "records": [
                        {
                            "append_record_seconds": 0,
                            "creation_time": "",
                            "error_message": "",
                            "ns_id": "",
                            "prerecord_seconds": 0,
                            "record_at": "",
                            "record_id": "",
                            "record_status": {},
                            "record_url": "",
                            "stream_id": "",
                            "task_id": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageSearchRecords")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("object_id", object_id)
        intef.update_body("page", page)
        intef.update_body("record_at", record_at)
        return intef.request() if sendRequest else intef

    def shortVideoStorageTaskListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskList """
        """  path: [get]/engine/short-video-storage/v1/tasks API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "tasks": [
                        {
                            "camera_identifier": {},
                            "creation_time": "",
                            "ns_id": "",
                            "record_callback_address": {},
                            "source_address": "",
                            "task_id": "",
                            "task_parameter": {},
                            "task_status": {},
                            "task_type": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageTaskList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def shortVideoStorageTaskNewPostApi(self, task_request=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskNew """
        """  path: [post]/engine/short-video-storage/v1/tasks API """
        """  body: 
                {
                    "task_request": {}
                }
        """
        """  resp:
                200():
                {
                    "task_info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageTaskNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task_request", task_request)
        return intef.request() if sendRequest else intef

    def shortVideoStorageTaskDeleteDeleteApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskDelete """
        """  path: [delete]/engine/short-video-storage/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageTaskDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def shortVideoStorageTaskInfoGetApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskInfo """
        """  path: [get]/engine/short-video-storage/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "info": {}
                }

        """
        intef = collections.interface("viperOpenApi", "shortVideoStorageTaskInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef



    def streamAPIAppletListGetApi(self, filter_name=None, filter_tags=None, filter_auth_state=None, filter_created_time_range_start=None, filter_created_time_range_end=None, page_offset=None, page_limit=None, page_total=None, reversed=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletList """
        """  path: [get]/engine/streaming-api/v1/applets API """
        """  params: 
                参数名称：filter.name　类型：string　描述：用户定义算法应用名称.
                参数名称：filter.tags　类型：array　描述：按算法标签过滤.
                参数名称：filter.auth_state　类型：array　描述：根据授权状态过滤, 默认为空，不过滤.
                参数名称：filter.created_time_range.start　类型：string　描述：开始时间, 区间包含.
                参数名称：filter.created_time_range.end　类型：string　描述：结束时间, 区间不包含.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
                参数名称：reversed　类型：boolean　描述：是否按创建时间逆序排列, 默认为false
        """
        """  resp:
                200():
                {
                    "applets": [
                        {
                            "applet_id": "",
                            "auth_state": {},
                            "bundle_path": "",
                            "checksum": "",
                            "created_at": "",
                            "deploy_spec": {},
                            "icon": {},
                            "spec": {},
                            "tags": []
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPIAppletList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("filter.name", filter_name)
        intef.update_params("filter.tags", filter_tags)
        intef.update_params("filter.auth_state", filter_auth_state)
        intef.update_params("filter.created_time_range.start", filter_created_time_range_start)
        intef.update_params("filter.created_time_range.end", filter_created_time_range_end)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.update_params("reversed", reversed)
        return intef.request() if sendRequest else intef

    def streamAPIAppletDeleteDeleteApi(self, applet_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletDelete """
        """  path: [delete]/engine/streaming-api/v1/applets/{applet_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "streamAPIAppletDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("applet_id", applet_id)
        return intef.request() if sendRequest else intef

    def streamAPIAppletGetGetApi(self, applet_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletGet """
        """  path: [get]/engine/streaming-api/v1/applets/{applet_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "applet": {}
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPIAppletGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("applet_id", applet_id)
        return intef.request() if sendRequest else intef

    def streamAPIAppletUpdatePatchApi(self, applet_id, tags=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletUpdate """
        """  path: [patch]/engine/streaming-api/v1/applets/{applet_id} API """
        """  body: 
                {
                    "applet_id": "",
                    "tags": []
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "streamAPIAppletUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("applet_id", applet_id)
        intef.update_body("tags", tags)
        intef.update_body("applet_id", applet_id)
        return intef.request() if sendRequest else intef

    def streamAPIAppletGetByNameVersionGetApi(self, applet_name, applet_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletGetByNameVersion """
        """  path: [get]/engine/streaming-api/v1/applets/{applet_name}/{applet_version} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "applet": {}
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPIAppletGetByNameVersion")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("applet_name", applet_name)
        intef.set_path_param("applet_version", applet_version)
        return intef.request() if sendRequest else intef

    def streamAPITaskBatchGetPostApi(self, task_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskBatchGet """
        """  path: [post]/engine/streaming-api/v1/batch_get_task API """
        """  body: 
                {
                    "task_ids": []
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ],
                    "tasks": [
                        {
                            "algo_type": {},
                            "applet_name": "",
                            "applet_version": 0,
                            "camera": {},
                            "creation_time": "",
                            "data": {},
                            "error_message": "",
                            "ns_id": "",
                            "state": {},
                            "task_id": "",
                            "task_types": [],
                            "update_at": "",
                            "user_data": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskBatchGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task_ids", task_ids)
        return intef.request() if sendRequest else intef

    def streamAPITaskBatchUpdateStatePatchApi(self, tasks=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskBatchUpdateState """
        """  path: [patch]/engine/streaming-api/v1/batch_update_task_state API """
        """  body: 
                {
                    "tasks": [
                        {
                            "error_message": "",
                            "state": {},
                            "task_id": ""
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskBatchUpdateState")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("tasks", tasks)
        return intef.request() if sendRequest else intef

    def streamAPICamerasGetByAppletNameVersionGetApi(self, applet_name, applet_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  CamerasGetByAppletNameVersion """
        """  path: [get]/engine/streaming-api/v1/cameras/{applet_name}/{applet_version} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "cameras": [
                        {
                            "camera": {},
                            "update_at": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPICamerasGetByAppletNameVersion")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("applet_name", applet_name)
        intef.set_path_param("applet_version", applet_version)
        return intef.request() if sendRequest else intef

    def streamAPIInstanceListGetApi(self, filter_states=None, filter_created_time_range_start=None, filter_created_time_range_end=None, reversed=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  InstanceList """
        """  path: [get]/engine/streaming-api/v1/instances API """
        """  params: 
                参数名称：filter.states　类型：array　描述：算法运行状态, 默认为空, 不对状态过滤.
                参数名称：filter.created_time_range.start　类型：string　描述：开始时间, 区间包含.
                参数名称：filter.created_time_range.end　类型：string　描述：结束时间, 区间不包含.
                参数名称：reversed　类型：boolean　描述：按创建时间逆序排列, 默认为false: 不做逆序排列.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "instances": [
                        {
                            "applet": {},
                            "created_at": "",
                            "deploy_item": {},
                            "error_message": "",
                            "instance_id": "",
                            "state": {},
                            "update_at": "",
                            "user_configs": {
                                "deploy_type": "[UNKNOWN]UNKNOWN/MINI/STANDARD",
                                "host": ""
                            }
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPIInstanceList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("filter.states", filter_states)
        intef.update_params("filter.created_time_range.start", filter_created_time_range_start)
        intef.update_params("filter.created_time_range.end", filter_created_time_range_end)
        intef.update_params("reversed", reversed)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def streamAPIAppletInstanceNewPostApi(self, applet_id=None, applet_name=None, applet_version=None, user_configs=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletInstanceNew """
        """  path: [post]/engine/streaming-api/v1/instances API """
        """  body: 
                {
                    "applet_id": "",
                    "applet_name": "",
                    "applet_version": 0,
                    "user_configs": {}
                }
        """
        """  resp:
                200():
                {
                    "instance_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPIAppletInstanceNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("applet_id", applet_id)
        intef.update_body("applet_name", applet_name)
        intef.update_body("applet_version", applet_version)
        intef.update_body("user_configs", user_configs)
        return intef.request() if sendRequest else intef

    def streamAPIAppletInstanceDeleteDeleteApi(self, instance_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletInstanceDelete """
        """  path: [delete]/engine/streaming-api/v1/instances/{instance_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "streamAPIAppletInstanceDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("instance_id", instance_id)
        return intef.request() if sendRequest else intef

    def streamAPIAppletInstanceGetGetApi(self, instance_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletInstanceGet """
        """  path: [get]/engine/streaming-api/v1/instances/{instance_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "instance": {}
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPIAppletInstanceGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("instance_id", instance_id)
        return intef.request() if sendRequest else intef

    def streamAPITaskTypeListGetApi(self, name=None, camera_region_id=None, camera_camera_idx=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskTypeList """
        """  path: [get]/engine/streaming-api/v1/task_type API """
        """  params: 
                参数名称：name　类型：string　描述：可选，任务类型名称
                参数名称：camera.region_id　类型：integer　描述：摄像头所属区域id, 0号id系统保留, 范围: [1, 16383].
                参数名称：camera.camera_idx　类型：integer　描述：摄像头在区域region_id内的下标, 0号id系统保留, 范围: [1, 127].
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "task_types": [
                        {
                            "algo_task_id": "",
                            "id": "",
                            "name": "",
                            "stream_task": {
                                "algo_type": {},
                                "applet_name": "",
                                "applet_version": 0,
                                "camera": {},
                                "creation_time": "",
                                "data": {},
                                "error_message": "",
                                "ns_id": "",
                                "state": {},
                                "task_id": "",
                                "task_types": [],
                                "update_at": "",
                                "user_data": ""
                            }
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskTypeList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("name", name)
        intef.update_params("camera.region_id", camera_region_id)
        intef.update_params("camera.camera_idx", camera_camera_idx)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def streamAPITaskTypeNewPostApi(self, algo_data=None, camera=None, name=None, stream_data=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskTypeNew """
        """  path: [post]/engine/streaming-api/v1/task_type API """
        """  body: 
                {
                    "algo_data": {
                        "type_url": "",
                        "value": ""
                    },
                    "camera": {},
                    "name": "",
                    "stream_data": {
                        "type_url": "",
                        "value": ""
                    }
                }
        """
        """  resp:
                200():
                {
                    "task_type_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskTypeNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("algo_data", algo_data)
        intef.update_body("camera", camera)
        intef.update_body("name", name)
        intef.update_body("stream_data", stream_data)
        return intef.request() if sendRequest else intef

    def streamAPITaskTypeDeleteDeleteApi(self, task_type_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskTypeDelete """
        """  path: [delete]/engine/streaming-api/v1/task_type/{task_type_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskTypeDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_type_id", task_type_id)
        return intef.request() if sendRequest else intef

    def streamAPITaskTypeGetGetApi(self, task_type_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskTypeGet """
        """  path: [get]/engine/streaming-api/v1/task_type/{task_type_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "task_type_info": {
                        "algo_task_id": "",
                        "id": "",
                        "name": "",
                        "stream_task": {
                            "algo_type": {},
                            "applet_name": "",
                            "applet_version": 0,
                            "camera": {},
                            "creation_time": "",
                            "data": {},
                            "error_message": "",
                            "ns_id": "",
                            "state": {},
                            "task_id": "",
                            "task_types": [],
                            "update_at": "",
                            "user_data": ""
                        }
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskTypeGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_type_id", task_type_id)
        return intef.request() if sendRequest else intef

    def streamAPITaskTypeUpdatePatchApi(self, task_type_id, algo_data=None, stream_data=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskTypeUpdate """
        """  path: [patch]/engine/streaming-api/v1/task_type/{task_type_id} API """
        """  body: 
                {
                    "algo_data": {
                        "type_url": "",
                        "value": ""
                    },
                    "stream_data": {
                        "type_url": "",
                        "value": ""
                    },
                    "task_type_id": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskTypeUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_type_id", task_type_id)
        intef.update_body("algo_data", algo_data)
        intef.update_body("stream_data", stream_data)
        intef.update_body("task_type_id", task_type_id)
        return intef.request() if sendRequest else intef

    def streamAPITaskListGetApi(self, filter_applet_applet_name=None, filter_applet_applet_version=None, filter_camera_region_id=None, filter_camera_camera_idx=None, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskList """
        """  path: [get]/engine/streaming-api/v1/tasks API """
        """  params: 
                参数名称：filter.applet.applet_name　类型：string　描述：算法应用名称.
                参数名称：filter.applet.applet_version　类型：integer　描述：算法应用版本号.
                参数名称：filter.camera.region_id　类型：integer　描述：摄像头所属区域id, 0号id系统保留, 范围: [1, 16383].
                参数名称：filter.camera.camera_idx　类型：integer　描述：摄像头在区域region_id内的下标, 0号id系统保留, 范围: [1, 127].
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "page": {},
                    "tasks": [
                        {
                            "algo_type": {},
                            "applet_name": "",
                            "applet_version": 0,
                            "camera": {},
                            "creation_time": "",
                            "data": {},
                            "error_message": "",
                            "ns_id": "",
                            "state": {},
                            "task_id": "",
                            "task_types": [],
                            "update_at": "",
                            "user_data": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("filter.applet.applet_name", filter_applet_applet_name)
        intef.update_params("filter.applet.applet_version", filter_applet_applet_version)
        intef.update_params("filter.camera.region_id", filter_camera_region_id)
        intef.update_params("filter.camera.camera_idx", filter_camera_camera_idx)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef

    def streamAPITaskNewPostApi(self, task=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskNew """
        """  path: [post]/engine/streaming-api/v1/tasks API """
        """  body: 
                {
                    "task": {}
                }
        """
        """  resp:
                200():
                {
                    "task": {}
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task", task)
        return intef.request() if sendRequest else intef

    def streamAPITaskDeleteDeleteApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskDelete """
        """  path: [delete]/engine/streaming-api/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def streamAPITaskGetGetApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskGet """
        """  path: [get]/engine/streaming-api/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "task": {}
                }

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def streamAPITaskUpdatePatchApi(self, task_id, data=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskUpdate """
        """  path: [patch]/engine/streaming-api/v1/tasks/{task_id} API """
        """  body: 
                {
                    "data": {},
                    "task_id": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "streamAPITaskUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        intef.update_body("data", data)
        intef.update_body("task_id", task_id)
        return intef.request() if sendRequest else intef

    def streamFileAppletUploadPostApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletUpload """
        """  path: [post]/engine/streaming-file/v1/applets/upload API """
        """  body: 
                {}
        """
        """  resp:
                200(A successful response.):
                "Not Support allOf"

        """
        intef = collections.interface("viperOpenApi", "streamFileAppletUpload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def streamFileAppletDownloadGetApi(self, applet_name, applet_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletDownload """
        """  path: [get]/engine/streaming-file/v1/applets/{applet_name}/{applet_version} API """
        """  params: 

        """
        """  resp:
                200(OK):
                "Not Support allOf"

        """
        intef = collections.interface("viperOpenApi", "streamFileAppletDownload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("applet_name", applet_name)
        intef.set_path_param("applet_version", applet_version)
        return intef.request() if sendRequest else intef

    def streamFileAppletDocDownloadGetApi(self, applet_name, applet_version, file_path, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AppletDocDownload """
        """  path: [get]/engine/streaming-file/v1/applets/{applet_name}/{applet_version}/{file_path} API """
        """  params: 

        """
        """  resp:
                200(OK):
                "Not Support allOf"

        """
        intef = collections.interface("viperOpenApi", "streamFileAppletDocDownload")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("applet_name", applet_name)
        intef.set_path_param("applet_version", applet_version)
        intef.set_path_param("file_path", file_path)
        return intef.request() if sendRequest else intef

    def structDBAggregatePostApi(self, camera_ids=None, end_time=None, filters=None, measures=None, object_type=None, options=None, start_time=None, time_interval=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  Aggregate """
        """  path: [post]/engine/struct-db/v1/aggregate API """
        """  body: 
                {
                    "camera_ids": [
                        {
                            "camera_idx": 0,
                            "region_id": 0
                        }
                    ],
                    "end_time": "",
                    "filters": [
                        {
                            "bool_value": false,
                            "field": "",
                            "filter_logic_type": {},
                            "float_array": [],
                            "float_value": 0,
                            "integer_array": [],
                            "integer_value": "",
                            "string_array": [],
                            "string_value": "",
                            "type": {}
                        }
                    ],
                    "measures": [
                        {
                            "field": "",
                            "type": {}
                        }
                    ],
                    "object_type": {},
                    "options": {},
                    "start_time": "",
                    "time_interval": {}
                }
        """
        """  resp:
                200():
                {
                    "dateframe_by_timestamp": [
                        {
                            "count": "",
                            "timestamp": "",
                            "values": []
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "structDBAggregate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("camera_ids", camera_ids)
        intef.update_body("end_time", end_time)
        intef.update_body("filters", filters)
        intef.update_body("measures", measures)
        intef.update_body("object_type", object_type)
        intef.update_body("options", options)
        intef.update_body("start_time", start_time)
        intef.update_body("time_interval", time_interval)
        return intef.request() if sendRequest else intef

    def structDBDeleteObjectsPostApi(self, unique_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteObjects """
        """  path: [post]/engine/struct-db/v1/delete_objects API """
        """  body: 
                {
                    "unique_ids": []
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "structDBDeleteObjects")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("unique_ids", unique_ids)
        return intef.request() if sendRequest else intef

    def structDBDeleteObjectsBeforeDatePostApi(self, date=None, object_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteObjectsBeforeDate """
        """  path: [post]/engine/struct-db/v1/delete_objects_before_date API """
        """  body: 
                {
                    "date": "",
                    "object_type": {}
                }
        """
        """  resp:
                200():
                {
                    "result": {}
                }

        """
        intef = collections.interface("viperOpenApi", "structDBDeleteObjectsBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("date", date)
        intef.update_body("object_type", object_type)
        return intef.request() if sendRequest else intef

    def structDBGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/struct-db/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "available_mb": "",
                    "failed_shards": "",
                    "total_mb": "",
                    "total_objects": "",
                    "total_shards": "",
                    "total_used_mb": "",
                    "types_info": [
                        {
                            "failed_shards": "",
                            "first_date_to_delete": "",
                            "object_type": {},
                            "objects": "",
                            "total_shards": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "structDBGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def structDBNamespaceListGetApi(self, page_offset=None, page_limit=None, page_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  NamespaceList """
        """  path: [get]/engine/struct-db/v1/namespaces API """
        """  params: 
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写
        """
        """  resp:
                200():
                {
                    "namespaces": [
                        {
                            "created_at": "",
                            "description": "",
                            "ns_id": ""
                        }
                    ],
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "structDBNamespaceList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        return intef.request() if sendRequest else intef



    def structDBNamespaceDeleteDeleteApi(self, ns_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  NamespaceDelete """
        """  path: [delete]/engine/struct-db/v1/namespaces/{ns_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "structDBNamespaceDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("ns_id", ns_id)
        return intef.request() if sendRequest else intef

    def structDBQueryPostApi(self, camera_ids=None, deduplication=None, end_time=None, filters=None, marker=None, object_id=None, object_type=None, options=None, page_limit=None, page_offset=None, start_time=None, timestamp_asc=None, track_total_hits=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  Query """
        """  path: [post]/engine/struct-db/v1/query API """
        """  body: 
                {
                    "camera_ids": [
                        {
                            "camera_idx": 0,
                            "region_id": 0
                        }
                    ],
                    "deduplication": false,
                    "end_time": "",
                    "filters": [
                        {
                            "bool_value": false,
                            "field": "",
                            "filter_logic_type": {},
                            "float_array": [],
                            "float_value": 0,
                            "integer_array": [],
                            "integer_value": "",
                            "string_array": [],
                            "string_value": "",
                            "type": {}
                        }
                    ],
                    "marker": "",
                    "object_id": "",
                    "object_type": {},
                    "options": {},
                    "page_limit": "",
                    "page_offset": "",
                    "start_time": "",
                    "timestamp_asc": false,
                    "track_total_hits": false
                }
        """
        """  resp:
                200():
                {
                    "marker": "",
                    "page_limit": "",
                    "page_offset": "",
                    "result": [
                        {
                            "automobile": {},
                            "crowd": {},
                            "cyclist": {},
                            "event": {},
                            "face": {},
                            "filtered": {},
                            "human_powered_vehicle": {},
                            "object_type": {},
                            "pedestrian": {},
                            "timestamp": "",
                            "watercraft": {}
                        }
                    ],
                    "total": ""
                }

        """
        intef = collections.interface("viperOpenApi", "structDBQuery")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("camera_ids", camera_ids)
        intef.update_body("deduplication", deduplication)
        intef.update_body("end_time", end_time)
        intef.update_body("filters", filters)
        intef.update_body("marker", marker)
        intef.update_body("object_id", object_id)
        intef.update_body("object_type", object_type)
        intef.update_body("options", options)
        intef.update_body("page_limit", page_limit)
        intef.update_body("page_offset", page_offset)
        intef.update_body("start_time", start_time)
        intef.update_body("timestamp_asc", timestamp_asc)
        intef.update_body("track_total_hits", track_total_hits)
        return intef.request() if sendRequest else intef

    def timespaceDBMultiV3DBListGetApi(self, deploy_type, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DBList """
        """  path: [get]/engine/timespace-{deploy_type}/v3/databases API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "dbs": [
                        {
                            "capacity": "",
                            "created_at": "",
                            "db_id": "",
                            "description": "",
                            "feature_version": 0,
                            "object_type": "",
                            "size": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBMultiV3DBList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        return intef.request() if sendRequest else intef

    def timespaceDBMultiV3DBNewPostApi(self, deploy_type, capacity=None, db_id=None, description=None, feature_version=None, object_type=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DBNew """
        """  path: [post]/engine/timespace-{deploy_type}/v3/databases API """
        """  body: 
                {
                    "capacity": "",
                    "db_id": "",
                    "description": "",
                    "feature_version": 0,
                    "object_type": ""
                }
        """
        """  resp:
                200():
                {
                    "db_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBMultiV3DBNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.update_body("capacity", capacity)
        intef.update_body("db_id", db_id)
        intef.update_body("description", description)
        intef.update_body("feature_version", feature_version)
        intef.update_body("object_type", object_type)
        return intef.request() if sendRequest else intef

    def timespaceDBMultiV3DBDeleteDeleteApi(self, deploy_type, db_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DBDelete """
        """  path: [delete]/engine/timespace-{deploy_type}/v3/databases/{db_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "timespaceDBMultiV3DBDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("db_id", db_id)
        return intef.request() if sendRequest else intef

    def timespaceDBMultiV3DBGetGetApi(self, deploy_type, db_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DBGet """
        """  path: [get]/engine/timespace-{deploy_type}/v3/databases/{db_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "db": {}
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBMultiV3DBGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("db_id", db_id)
        return intef.request() if sendRequest else intef

    def timespaceDBMultiV3GetSystemInfoV3GetApi(self, deploy_type, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfoV3 """
        """  path: [get]/engine/timespace-{deploy_type}/v3/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "system_db_infos": [
                        {
                            "available_gpu_memory_size": "",
                            "available_memory_size": "",
                            "capacity": "",
                            "cluster_shards": "",
                            "clusters": "",
                            "db_id": "",
                            "feature_version": 0,
                            "features": "",
                            "first_time_to_delete": "",
                            "metadata": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "object_type": "",
                            "offline_workers": [],
                            "online_workers": [],
                            "regions": [
                                {
                                    "features": "",
                                    "period": {},
                                    "region_id": 0
                                }
                            ],
                            "shards": "",
                            "total_gpu_memory_size": "",
                            "total_memory_size": "",
                            "worker_infos": [
                                {
                                    "cluster_shards": "",
                                    "clusters": "",
                                    "features": "",
                                    "region_ids": 0,
                                    "shards": "",
                                    "worker_id": ""
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBMultiV3GetSystemInfoV3")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        return intef.request() if sendRequest else intef

    def timespaceDBAddFeatureAsyncPostApi(self, deploy_type, object_type, feature_version, db_id=None, object_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  AddFeatureAsync """
        """  path: [post]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/add_feature_async API """
        """  body: 
                {
                    "db_id": "",
                    "object_info": {
                        "camera_info": {},
                        "captured_time": "",
                        "extra_fields": {
                            "additionalProp1": "",
                            "additionalProp2": "",
                            "additionalProp3": ""
                        },
                        "extra_info": "",
                        "feature": {},
                        "ns_id": "",
                        "object": {},
                        "object_index_in_frame": 0,
                        "panoramic_image": {},
                        "portrait_image": {},
                        "producer_annotation": {},
                        "received_time": "",
                        "relative_time": "",
                        "track_event": {}
                    }
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "timespaceDBAddFeatureAsync")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("db_id", db_id)
        intef.update_body("object_info", object_info)
        return intef.request() if sendRequest else intef

    def timespaceDBBatchGetFeatureByObjectIDPostApi(self, deploy_type, object_type, feature_version, db_id=None, ignore_feature=None, object_ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  BatchGetFeatureByObjectID """
        """  path: [post]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/batch_get_by_object_id API """
        """  body: 
                {
                    "db_id": "",
                    "ignore_feature": false,
                    "object_ids": []
                }
        """
        """  resp:
                200():
                {
                    "items": [
                        {
                            "items": [
                                {
                                    "feature": {},
                                    "result": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBBatchGetFeatureByObjectID")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("db_id", db_id)
        intef.update_body("ignore_feature", ignore_feature)
        intef.update_body("object_ids", object_ids)
        return intef.request() if sendRequest else intef

    def timespaceDBClusterGetByKeyGetApi(self, deploy_type, object_type, feature_version, key=None, period_start=None, period_end=None, load_mode=None, max_preview_load_count=None, results_filter_filter_mode=None, results_filter_preview_results_count=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ClusterGetByKey """
        """  path: [get]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/clusters/get_by_key API """
        """  params: 
                参数名称：key　类型：string　描述：用户自定义Key, 一般与静态库中的Key对应.
                参数名称：period.start　类型：string　描述：开始时间, 区间包含.
                参数名称：period.end　类型：string　描述：结束时间, 区间不包含.
                参数名称：load_mode　类型：string　描述：可选, 特征详情加载模式, 默认不加载特征详情 [DEPRECATED].
                参数名称：max_preview_load_count　类型：integer　描述：可选, 当load_mode为CLUSTER_LOAD_PREVIEW时, 加载指定数量的特征详情.
取值范围为: [1, 4] [DEPRECATED].
                参数名称：results_filter.filter_mode　类型：string　描述：- IGNORE_ALL_RESULTS: 忽略类中包含的特征列表.
                参数名称：results_filter.preview_results_count　类型：integer　描述：可选, 当加载方式为LOAD_PREVIEW_RESULTS时有效, 加载指定数量的特征详情.
取值范围为[0, 4]
        """
        """  resp:
                200():
                {
                    "clusters": [
                        {
                            "centroid": {},
                            "cluster_id": "",
                            "created_at": "",
                            "extra_info": "",
                            "key": "",
                            "key_source": "",
                            "modified_at": "",
                            "preview_results": [
                                {
                                    "cluster_id": "",
                                    "extra_info": "",
                                    "object": {},
                                    "object_id": {},
                                    "panoramic_image": {},
                                    "portrait_image": {},
                                    "score": 0
                                }
                            ],
                            "results": [
                                {
                                    "cluster_id": "",
                                    "extra_info": "",
                                    "object": {},
                                    "object_id": {},
                                    "panoramic_image": {},
                                    "portrait_image": {},
                                    "score": 0
                                }
                            ],
                            "score": 0
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBClusterGetByKey")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("key", key)
        intef.update_params("period.start", period_start)
        intef.update_params("period.end", period_end)
        intef.update_params("load_mode", load_mode)
        intef.update_params("max_preview_load_count", max_preview_load_count)
        intef.update_params("results_filter.filter_mode", results_filter_filter_mode)
        intef.update_params("results_filter.preview_results_count", results_filter_preview_results_count)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def timespaceDBClusterSearchPostApi(self, deploy_type, object_type, feature_version, config=None, feature=None, filter_configs=None, load_mode=None, max_preview_load_count=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ClusterSearch """
        """  path: [post]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/clusters/search API """
        """  body: 
                {
                    "config": {},
                    "feature": {},
                    "filter_configs": [
                        {
                            "results_filter": {
                                "filter_mode": "[IGNORE_ALL_RESULTS]IGNORE_ALL_RESULTS/LOAD_PREVIEW_RESULTS/LOAD_ALL_RESULTS",
                                "preview_results_count": 0
                            }
                        }
                    ],
                    "load_mode": {},
                    "max_preview_load_count": 0
                }
        """
        """  resp:
                200():
                {
                    "clusters": [
                        {
                            "centroid": {},
                            "cluster_id": "",
                            "created_at": "",
                            "extra_info": "",
                            "key": "",
                            "key_source": "",
                            "modified_at": "",
                            "preview_results": [
                                {
                                    "cluster_id": "",
                                    "extra_info": "",
                                    "object": {},
                                    "object_id": {},
                                    "panoramic_image": {},
                                    "portrait_image": {},
                                    "score": 0
                                }
                            ],
                            "results": [
                                {
                                    "cluster_id": "",
                                    "extra_info": "",
                                    "object": {},
                                    "object_id": {},
                                    "panoramic_image": {},
                                    "portrait_image": {},
                                    "score": 0
                                }
                            ],
                            "score": 0
                        }
                    ],
                    "post_process_time": "",
                    "search_time": "",
                    "success_shards": 0,
                    "success_workers": 0,
                    "total_shards": 0,
                    "total_workers": 0,
                    "version": ""
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBClusterSearch")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("config", config)
        intef.update_body("feature", feature)
        intef.update_body("filter_configs", filter_configs)
        intef.update_body("load_mode", load_mode)
        intef.update_body("max_preview_load_count", max_preview_load_count)
        return intef.request() if sendRequest else intef

    def timespaceDBClusterGetGetApi(self, deploy_type, object_type, feature_version, cluster_id, period_start=None, period_end=None, page_offset=None, page_limit=None, page_total=None, ignore_centroid=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ClusterGet """
        """  path: [get]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/clusters/{cluster_id} API """
        """  params: 
                参数名称：period.start　类型：string　描述：开始时间, 区间包含.
                参数名称：period.end　类型：string　描述：结束时间, 区间不包含.
                参数名称：page.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条, 默认值为0. 作为输出时,
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page.limit　类型：integer　描述：长度, 默认取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page.total　类型：integer　描述：可选, 请求无须填此参数, 响应时系统填写.
                参数名称：ignore_centroid　类型：boolean　描述：是否需要返回类中心特征, 默认false. false: 返回类中心特征; true: 不返回类中心特征
        """
        """  resp:
                200():
                {
                    "cluster": {},
                    "page": {}
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBClusterGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("period.start", period_start)
        intef.update_params("period.end", period_end)
        intef.update_params("page.offset", page_offset)
        intef.update_params("page.limit", page_limit)
        intef.update_params("page.total", page_total)
        intef.update_params("ignore_centroid", ignore_centroid)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.set_path_param("cluster_id", cluster_id)
        return intef.request() if sendRequest else intef

    def timespaceDBClusterPutPutApi(self, deploy_type, object_type, feature_version, cluster_id, extra_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ClusterPut """
        """  path: [put]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/clusters/{cluster_id} API """
        """  body: 
                {
                    "cluster_id": "",
                    "extra_info": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "timespaceDBClusterPut")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.set_path_param("cluster_id", cluster_id)
        intef.update_body("cluster_id", cluster_id)
        intef.update_body("extra_info", extra_info)
        return intef.request() if sendRequest else intef

    def timespaceDBDeleteFeaturePostApi(self, deploy_type, object_type, feature_version, db_id=None, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteFeature """
        """  path: [post]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/delete_feature API """
        """  body: 
                {
                    "db_id": "",
                    "id": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "timespaceDBDeleteFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("db_id", db_id)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def timespaceDBDeleteShardsBeforeDatePostApi(self, deploy_type, object_type, feature_version, date=None, db_id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DeleteShardsBeforeDate """
        """  path: [post]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/delete_shards_before_date API """
        """  body: 
                {
                    "date": "",
                    "db_id": ""
                }
        """
        """  resp:
                200():
                {
                    "deleted_features": "",
                    "deleted_shards": 0
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBDeleteShardsBeforeDate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("date", date)
        intef.update_body("db_id", db_id)
        return intef.request() if sendRequest else intef

    def timespaceDBGetFeaturePostApi(self, deploy_type, object_type, feature_version, db_id=None, id=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetFeature """
        """  path: [post]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/get_feature API """
        """  body: 
                {
                    "db_id": "",
                    "id": {}
                }
        """
        """  resp:
                200():
                {
                    "feature": {},
                    "result": {}
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBGetFeature")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("db_id", db_id)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def timespaceDBGetSystemInfoGetApi(self, deploy_type, object_type, feature_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "available_gpu_memory_size": "",
                    "available_memory_size": "",
                    "cluster_shards": "",
                    "clusters": "",
                    "features": "",
                    "first_time_to_delete": "",
                    "license_capacity": "",
                    "offline_workers": [],
                    "online_workers": [],
                    "region_infos": [
                        {
                            "features": "",
                            "period": {},
                            "region_id": 0
                        }
                    ],
                    "shards": "",
                    "system_metadata": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    },
                    "total_gpu_memory_size": "",
                    "total_memory_size": "",
                    "used_percentage": 0,
                    "worker_infos": [
                        {
                            "cluster_shards": "",
                            "clusters": "",
                            "features": "",
                            "region_ids": 0,
                            "shards": "",
                            "worker_id": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def timespaceDBLabelingDataSourcesSetPostApi(self, deploy_type, object_type, feature_version, data_sources=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  LabelingDataSourcesSet """
        """  path: [post]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/labeling/data_sources API """
        """  body: 
                {
                    "data_sources": [
                        {
                            "db_id": "",
                            "db_type": {}
                        }
                    ]
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "timespaceDBLabelingDataSourcesSet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("data_sources", data_sources)
        return intef.request() if sendRequest else intef

    def timespaceDBLabelingGetInfoGetApi(self, deploy_type, object_type, feature_version, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  LabelingGetInfo """
        """  path: [get]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/labeling/info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "data_sources": [
                        {
                            "db_id": "",
                            "db_type": {}
                        }
                    ],
                    "mode": "[LABELING_INCREMENTAL]LABELING_INCREMENTAL/LABELING_ALL/LABELING_UPDATED_CLUSTERS/LABELING_ALL_EXCEPT_EXTERNAL/LABELING_UPDATED_NOTIDENTIFIED_CLUSTERS/LABELING_ALL_ANONYMOUS_CLUSTERS"
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBLabelingGetInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        return intef.request() if sendRequest else intef

    def timespaceDBLabelingModeSetPostApi(self, deploy_type, object_type, feature_version, mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  LabelingModeSet """
        """  path: [post]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/labeling/mode API """
        """  body: 
                {
                    "mode": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "timespaceDBLabelingModeSet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("mode", mode)
        return intef.request() if sendRequest else intef

    def timespaceDBListFeaturesPostApi(self, deploy_type, object_type, feature_version, camera_ids=None, db_id=None, marker=None, page_size=None, period=None, reversed=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  ListFeatures """
        """  path: [post]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/list_features API """
        """  body: 
                {
                    "camera_ids": [
                        {
                            "camera_idx": 0,
                            "region_id": 0
                        }
                    ],
                    "db_id": "",
                    "marker": "",
                    "page_size": 0,
                    "period": {},
                    "reversed": false
                }
        """
        """  resp:
                200():
                {
                    "marker": "",
                    "results": [
                        {
                            "cluster_id": "",
                            "extra_info": "",
                            "object": {},
                            "object_id": {},
                            "panoramic_image": {},
                            "portrait_image": {},
                            "score": 0
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBListFeatures")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("camera_ids", camera_ids)
        intef.update_body("db_id", db_id)
        intef.update_body("marker", marker)
        intef.update_body("page_size", page_size)
        intef.update_body("period", period)
        intef.update_body("reversed", reversed)
        return intef.request() if sendRequest else intef

    def timespaceDBSearchPostApi(self, deploy_type, object_type, feature_version, config=None, feature=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  Search """
        """  path: [post]/engine/timespace-{deploy_type}/{object_type}_{feature_version}/v2/search API """
        """  body: 
                {
                    "config": {},
                    "feature": {}
                }
        """
        """  resp:
                200():
                {
                    "post_process_time": "",
                    "results": [
                        {
                            "cluster_id": "",
                            "extra_info": "",
                            "object": {},
                            "object_id": {},
                            "panoramic_image": {},
                            "portrait_image": {},
                            "score": 0
                        }
                    ],
                    "search_time": "",
                    "success_shards": 0,
                    "success_workers": 0,
                    "total_shards": 0,
                    "total_workers": 0
                }

        """
        intef = collections.interface("viperOpenApi", "timespaceDBSearch")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("deploy_type", deploy_type)
        intef.set_path_param("object_type", object_type)
        intef.set_path_param("feature_version", feature_version)
        intef.update_body("config", config)
        intef.update_body("feature", feature)
        return intef.request() if sendRequest else intef

    def videoIngressGenerateRTMPAddressPostApi(self, source_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GenerateRTMPAddress """
        """  path: [post]/engine/video-ingress/v1/generate_rtmp_address API """
        """  body: 
                {
                    "source_info": {}
                }
        """
        """  resp:
                200():
                {
                    "rtmp_url": ""
                }

        """
        intef = collections.interface("viperOpenApi", "videoIngressGenerateRTMPAddress")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("source_info", source_info)
        return intef.request() if sendRequest else intef

    def videoIngressGenerateRTSPAddressPostApi(self, source_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GenerateRTSPAddress """
        """  path: [post]/engine/video-ingress/v1/generate_rtsp_address API """
        """  body: 
                {
                    "source_info": {}
                }
        """
        """  resp:
                200():
                {
                    "is_absolute": false,
                    "url": ""
                }

        """
        intef = collections.interface("viperOpenApi", "videoIngressGenerateRTSPAddress")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("source_info", source_info)
        return intef.request() if sendRequest else intef

    def videoIngressGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/video-ingress/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "nodes": [
                        {
                            "input_streams": {
                                "additionalProp1": 0,
                                "additionalProp2": 0,
                                "additionalProp3": 0
                            },
                            "ip": "",
                            "is_manager": false,
                            "output_streams": 0,
                            "rtmp_port": 0,
                            "rtsp_port": 0,
                            "total_quota": 0,
                            "virtual_ip": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "videoIngressGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def videoIngressStreamInfoGetApi(self, url, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  StreamInfo """
        """  path: [get]/engine/video-ingress/v1/stream_infos/{url} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "node_endpoints": [],
                    "stream_id": ""
                }

        """
        intef = collections.interface("viperOpenApi", "videoIngressStreamInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("url", url)
        return intef.request() if sendRequest else intef

    def videoIngressGetStreamInformationPostApi(self, source_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetStreamInformation """
        """  path: [post]/engine/video-ingress/v1/stream_video_parameter API """
        """  body: 
                {
                    "source_info": {}
                }
        """
        """  resp:
                200():
                {
                    "video_parameter": {}
                }

        """
        intef = collections.interface("viperOpenApi", "videoIngressGetStreamInformation")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("source_info", source_info)
        return intef.request() if sendRequest else intef

    def videoProcessGetSystemInfoGetApi(self, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/video-process/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "algo_video_status": [
                        {
                            "algo_version": 0,
                            "group": {
                                "group_name": "",
                                "total_quota": 0
                            },
                            "resolution_stat": [
                                {
                                    "count": "",
                                    "resolution": "[RESOLUTION_UNKNOWN]RESOLUTION_UNKNOWN/RESOLUTION_QCIF/RESOLUTION_CIF/RESOLUTION_4CIF/RESOLUTION_D1/RESOLUTION_720P/RESOLUTION_1080P/RESOLUTION_2K/RESOLUTION_4K",
                                    "total_quota": ""
                                }
                            ],
                            "status_count": [
                                {
                                    "count": "",
                                    "status": "[PENDING]PENDING/OK/SOURCE_ERROR/INTERNAL_ERROR/FINISHED/DECODER_ERROR/CREATING/RESOLUTION_ERROR/CONFIG_UPDATE_ERROR"
                                }
                            ],
                            "user_algo_name": ""
                        }
                    ],
                    "video_status": [
                        {
                            "object_type": {},
                            "resolution_stat": [
                                {
                                    "count": "",
                                    "resolution": "[RESOLUTION_UNKNOWN]RESOLUTION_UNKNOWN/RESOLUTION_QCIF/RESOLUTION_CIF/RESOLUTION_4CIF/RESOLUTION_D1/RESOLUTION_720P/RESOLUTION_1080P/RESOLUTION_2K/RESOLUTION_4K",
                                    "total_quota": ""
                                }
                            ],
                            "status_count": [
                                {
                                    "count": "",
                                    "status": "[PENDING]PENDING/OK/SOURCE_ERROR/INTERNAL_ERROR/FINISHED/DECODER_ERROR/CREATING/RESOLUTION_ERROR/CONFIG_UPDATE_ERROR"
                                }
                            ],
                            "total_quota": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "videoProcessGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        return intef.request() if sendRequest else intef

    def videoProcessTaskListGetApi(self, page_request_offset=None, page_request_limit=None, page_request_total=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskList """
        """  path: [get]/engine/video-process/v1/tasks API """
        """  params: 
                参数名称：page_request.offset　类型：integer　描述：可选, 开始位置, 取值:>=0, 0为第一条; 默认值为0.
返回本次请求返回的第一条记录实际位置(一般与输入一致).
                参数名称：page_request.limit　类型：integer　描述：长度, 取值范围[1,100], 如果超出范围, 则返回失败; 在某些接口中limit范围可能会重新定义, 请以其接口的补充说明为准.
                参数名称：page_request.total　类型：integer　描述：可选, 总任务数, 请求无须填此参数, 响应时填写
        """
        """  resp:
                200():
                {
                    "page_response": {},
                    "tasks": [
                        {
                            "info": {},
                            "rtsp_preview_address": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "videoProcessTaskList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("page_request.offset", page_request_offset)
        intef.update_params("page_request.limit", page_request_limit)
        intef.update_params("page_request.total", page_request_total)
        return intef.request() if sendRequest else intef

    def videoProcessTaskNewPostApi(self, task=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskNew """
        """  path: [post]/engine/video-process/v1/tasks API """
        """  body: 
                {
                    "task": {}
                }
        """
        """  resp:
                200():
                {
                    "task": {}
                }

        """
        intef = collections.interface("viperOpenApi", "videoProcessTaskNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("task", task)
        return intef.request() if sendRequest else intef

    def videoProcessTaskDeleteDeleteApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskDelete """
        """  path: [delete]/engine/video-process/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "videoProcessTaskDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def videoProcessTaskStatusGetApi(self, task_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskStatus """
        """  path: [get]/engine/video-process/v1/tasks/{task_id} API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "info": {},
                    "rtsp_preview_address": "",
                    "status": {}
                }

        """
        intef = collections.interface("viperOpenApi", "videoProcessTaskStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        return intef.request() if sendRequest else intef

    def videoProcessTaskUpdatePostApi(self, task_id, task=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  TaskUpdate """
        """  path: [post]/engine/video-process/v1/tasks/{task_id} API """
        """  body: 
                {
                    "task": {
                        "task_object_config": {}
                    },
                    "task_id": ""
                }
        """
        """  resp:
                200():
                {
                    "task": {}
                }

        """
        intef = collections.interface("viperOpenApi", "videoProcessTaskUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("task_id", task_id)
        intef.update_body("task", task)
        intef.update_body("task_id", task_id)
        return intef.request() if sendRequest else intef

    def staticDBFeatureBatchSearchMultiPostApi(self, db_type, configs=None, dropped_fields=None, features=None, merge_top_k=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureBatchSearchMulti """
        """  path: [post]/engine/{db_type}-feature/v1/batch_search_multi API """
        """  body: 
                {
                    "configs": [
                        {
                            "col_id": "",
                            "consistency": {},
                            "min_score": 0,
                            "top_k": 0
                        }
                    ],
                    "dropped_fields": [
                        "[ITEM_EXTRA_INFO]ITEM_EXTRA_INFO/ITEM_META_DATA"
                    ],
                    "features": [
                        {
                            "blob": "",
                            "type": "",
                            "version": 0
                        }
                    ],
                    "merge_top_k": 0
                }
        """
        """  resp:
                200():
                {
                    "responses": [
                        {
                            "col_id": "",
                            "feature_results": [
                                {
                                    "results": [
                                        {
                                            "index_id": "",
                                            "item": {},
                                            "score": 0
                                        }
                                    ]
                                }
                            ],
                            "is_refined": false,
                            "results": [
                                {
                                    "code": 0,
                                    "error": "",
                                    "status": {}
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureBatchSearchMulti")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.update_body("configs", configs)
        intef.update_body("dropped_fields", dropped_fields)
        intef.update_body("features", features)
        intef.update_body("merge_top_k", merge_top_k)
        return intef.request() if sendRequest else intef

    def staticDBDBListGetApi(self, db_type, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DBList """
        """  path: [get]/engine/{db_type}-feature/v1/databases API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "db_infos": [
                        {
                            "cached": false,
                            "creation_time": "",
                            "db_id": "",
                            "default_opq_model": "",
                            "description": "",
                            "feature_version": 0,
                            "indexes": [
                                {
                                    "cache_raw_feature": false,
                                    "capacity": "",
                                    "creation_time": "",
                                    "default_opq_model": "",
                                    "feature_table": "",
                                    "feature_version": 0,
                                    "last_retrained_seq_id": "",
                                    "last_seq_id": "",
                                    "object_type": "",
                                    "size": "",
                                    "status": {},
                                    "uuid": "",
                                    "worker_id": ""
                                }
                            ],
                            "max_size": "",
                            "name": "",
                            "object_type": "",
                            "size": ""
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBDBList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        return intef.request() if sendRequest else intef

    def staticDBDBNewPostApi(self, db_type, db_size=None, description=None, feature_version=None, name=None, object_type=None, options=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DBNew """
        """  path: [post]/engine/{db_type}-feature/v1/databases API """
        """  body: 
                {
                    "db_size": "",
                    "description": "",
                    "feature_version": 0,
                    "name": "",
                    "object_type": "",
                    "options": {}
                }
        """
        """  resp:
                200():
                {
                    "creation_time": "",
                    "db_id": "",
                    "indexes": [
                        {
                            "cache_raw_feature": false,
                            "capacity": "",
                            "creation_time": "",
                            "default_opq_model": "",
                            "feature_table": "",
                            "feature_version": 0,
                            "last_retrained_seq_id": "",
                            "last_seq_id": "",
                            "object_type": "",
                            "size": "",
                            "status": {},
                            "uuid": "",
                            "worker_id": ""
                        }
                    ],
                    "name": "",
                    "object_type": ""
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBDBNew")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.update_body("db_size", db_size)
        intef.update_body("description", description)
        intef.update_body("feature_version", feature_version)
        intef.update_body("name", name)
        intef.update_body("object_type", object_type)
        intef.update_body("options", options)
        return intef.request() if sendRequest else intef

    def staticDBFeatureBatchAddPostApi(self, db_type, col_id, items=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureBatchAdd """
        """  path: [post]/engine/{db_type}-feature/v1/databases/{col_id}/batch_add API """
        """  body: 
                {
                    "col_id": "",
                    "items": [
                        {
                            "extra_info": "",
                            "feature": {},
                            "id": "",
                            "image_id": "",
                            "key": "",
                            "meta_data": "",
                            "seq_id": ""
                        }
                    ]
                }
        """
        """  resp:
                200():
                {
                    "ids": [],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureBatchAdd")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("items", items)
        return intef.request() if sendRequest else intef

    def staticDBFeatureBatchDeletePostApi(self, db_type, col_id, ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureBatchDelete """
        """  path: [post]/engine/{db_type}-feature/v1/databases/{col_id}/batch_delete API """
        """  body: 
                {
                    "col_id": "",
                    "ids": []
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureBatchDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("ids", ids)
        return intef.request() if sendRequest else intef

    def staticDBFeatureBatchDeleteByKeyPostApi(self, db_type, col_id, keys=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureBatchDeleteByKey """
        """  path: [post]/engine/{db_type}-feature/v1/databases/{col_id}/batch_delete_by_key API """
        """  body: 
                {
                    "col_id": "",
                    "keys": []
                }
        """
        """  resp:
                200():
                {
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureBatchDeleteByKey")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("keys", keys)
        return intef.request() if sendRequest else intef

    def staticDBFeatureBatchGetPostApi(self, db_type, col_id, consistency=None, ids=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureBatchGet """
        """  path: [post]/engine/{db_type}-feature/v1/databases/{col_id}/batch_get API """
        """  body: 
                {
                    "col_id": "",
                    "consistency": {},
                    "ids": []
                }
        """
        """  resp:
                200():
                {
                    "items": [
                        {
                            "extra_info": "",
                            "feature": {},
                            "id": "",
                            "image_id": "",
                            "key": "",
                            "meta_data": "",
                            "seq_id": ""
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureBatchGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("consistency", consistency)
        intef.update_body("ids", ids)
        return intef.request() if sendRequest else intef

    def staticDBFeatureBatchGetByKeyPostApi(self, db_type, col_id, consistency=None, ignore_details=None, keys=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureBatchGetByKey """
        """  path: [post]/engine/{db_type}-feature/v1/databases/{col_id}/batch_get_by_key API """
        """  body: 
                {
                    "col_id": "",
                    "consistency": {},
                    "ignore_details": false,
                    "keys": []
                }
        """
        """  resp:
                200():
                {
                    "items": [
                        {
                            "items": [
                                {
                                    "extra_info": "",
                                    "feature": {},
                                    "id": "",
                                    "image_id": "",
                                    "key": "",
                                    "meta_data": "",
                                    "seq_id": ""
                                }
                            ]
                        }
                    ],
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureBatchGetByKey")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("consistency", consistency)
        intef.update_body("ignore_details", ignore_details)
        intef.update_body("keys", keys)
        return intef.request() if sendRequest else intef

    def staticDBFeatureBatchGetByKeyPagingPostApi(self, db_type, col_id, consistency=None, ignore_details=None, keys=None, marker=None, page_size=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureBatchGetByKeyPaging """
        """  path: [post]/engine/{db_type}-feature/v1/databases/{col_id}/batch_get_by_key_paging API """
        """  body: 
                {
                    "col_id": "",
                    "consistency": {},
                    "ignore_details": false,
                    "keys": [],
                    "marker": "",
                    "page_size": 0
                }
        """
        """  resp:
                200():
                {
                    "items": [
                        {
                            "items": [
                                {
                                    "extra_info": "",
                                    "feature": {},
                                    "id": "",
                                    "image_id": "",
                                    "key": "",
                                    "meta_data": "",
                                    "seq_id": ""
                                }
                            ]
                        }
                    ],
                    "marker": "",
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureBatchGetByKeyPaging")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("consistency", consistency)
        intef.update_body("ignore_details", ignore_details)
        intef.update_body("keys", keys)
        intef.update_body("marker", marker)
        intef.update_body("page_size", page_size)
        return intef.request() if sendRequest else intef

    def staticDBFeatureBatchSearchPostApi(self, db_type, col_id, consistency=None, dropped_fields=None, features=None, min_score=None, return_raw_feature=None, top_k=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureBatchSearch """
        """  path: [post]/engine/{db_type}-feature/v1/databases/{col_id}/batch_search API """
        """  body: 
                {
                    "col_id": "",
                    "consistency": {},
                    "dropped_fields": [
                        "[ITEM_EXTRA_INFO]ITEM_EXTRA_INFO/ITEM_META_DATA"
                    ],
                    "features": [
                        {
                            "blob": "",
                            "type": "",
                            "version": 0
                        }
                    ],
                    "min_score": 0,
                    "return_raw_feature": false,
                    "top_k": 0
                }
        """
        """  resp:
                200():
                {
                    "col_id": "",
                    "feature_results": [
                        {
                            "results": [
                                {
                                    "index_id": "",
                                    "item": {},
                                    "score": 0
                                }
                            ]
                        }
                    ],
                    "is_refined": false,
                    "results": [
                        {
                            "code": 0,
                            "error": "",
                            "status": {}
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureBatchSearch")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("consistency", consistency)
        intef.update_body("dropped_fields", dropped_fields)
        intef.update_body("features", features)
        intef.update_body("min_score", min_score)
        intef.update_body("return_raw_feature", return_raw_feature)
        intef.update_body("top_k", top_k)
        return intef.request() if sendRequest else intef

    def staticDBFeatureListPostApi(self, db_type, col_id, marker=None, page_size=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureList """
        """  path: [post]/engine/{db_type}-feature/v1/databases/{col_id}/features API """
        """  body: 
                {
                    "col_id": "",
                    "marker": "",
                    "page_size": 0
                }
        """
        """  resp:
                200():
                {
                    "items": [
                        {
                            "extra_info": "",
                            "feature": {},
                            "id": "",
                            "image_id": "",
                            "key": "",
                            "meta_data": "",
                            "seq_id": ""
                        }
                    ],
                    "marker": ""
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureList")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.update_body("col_id", col_id)
        intef.update_body("marker", marker)
        intef.update_body("page_size", page_size)
        return intef.request() if sendRequest else intef

    def staticDBFeatureUpdatePatchApi(self, db_type, col_id, id, extra_info=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureUpdate """
        """  path: [patch]/engine/{db_type}-feature/v1/databases/{col_id}/features/{id} API """
        """  body: 
                {
                    "col_id": "",
                    "extra_info": "",
                    "id": ""
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.set_path_param("id", id)
        intef.update_body("col_id", col_id)
        intef.update_body("extra_info", extra_info)
        intef.update_body("id", id)
        return intef.request() if sendRequest else intef

    def staticDBFeatureUpdateByIDPatchApi(self, db_type, col_id, id, item=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  FeatureUpdateByID """
        """  path: [patch]/engine/{db_type}-feature/v1/databases/{col_id}/features/{id}/update_by_id API """
        """  body: 
                {
                    "col_id": "",
                    "id": "",
                    "item": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "staticDBFeatureUpdateByID")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("col_id", col_id)
        intef.set_path_param("id", id)
        intef.update_body("col_id", col_id)
        intef.update_body("id", id)
        intef.update_body("item", item)
        return intef.request() if sendRequest else intef

    def staticDBDBDeleteDeleteApi(self, db_type, db_id, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DBDelete """
        """  path: [delete]/engine/{db_type}-feature/v1/databases/{db_id} API """
        """  params: 

        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "staticDBDBDelete")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("db_id", db_id)
        return intef.request() if sendRequest else intef

    def staticDBDBGetGetApi(self, db_type, db_id, ignore_indexes_detail=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DBGet """
        """  path: [get]/engine/{db_type}-feature/v1/databases/{db_id} API """
        """  params: 
                参数名称：ignore_indexes_detail　类型：boolean　描述：只返回必要的库信息, 不返回各个子索引的详细信息, 所返回的信息同DBList
        """
        """  resp:
                200():
                {
                    "db_info": {
                        "cached": false,
                        "creation_time": "",
                        "db_id": "",
                        "default_opq_model": "",
                        "description": "",
                        "feature_version": 0,
                        "indexes": [
                            {
                                "cache_raw_feature": false,
                                "capacity": "",
                                "creation_time": "",
                                "default_opq_model": "",
                                "feature_table": "",
                                "feature_version": 0,
                                "last_retrained_seq_id": "",
                                "last_seq_id": "",
                                "object_type": "",
                                "size": "",
                                "status": {},
                                "uuid": "",
                                "worker_id": ""
                            }
                        ],
                        "max_size": "",
                        "name": "",
                        "object_type": "",
                        "size": ""
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBDBGet")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_params("ignore_indexes_detail", ignore_indexes_detail)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("db_id", db_id)
        return intef.request() if sendRequest else intef

    def staticDBDBUpdatePatchApi(self, db_type, db_id, description=None, name=None, object_type=None, options=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DBUpdate """
        """  path: [patch]/engine/{db_type}-feature/v1/databases/{db_id} API """
        """  body: 
                {
                    "db_id": "",
                    "description": "",
                    "name": "",
                    "object_type": "",
                    "options": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "staticDBDBUpdate")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("db_id", db_id)
        intef.update_body("db_id", db_id)
        intef.update_body("description", description)
        intef.update_body("name", name)
        intef.update_body("object_type", object_type)
        intef.update_body("options", options)
        return intef.request() if sendRequest else intef

    def staticDBDBTrainPostApi(self, db_type, db_id, mode=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  DBTrain """
        """  path: [post]/engine/{db_type}-feature/v1/databases/{db_id}/train API """
        """  body: 
                {
                    "db_id": "",
                    "mode": {}
                }
        """
        """  resp:
                200():
                {
                    "index_seq_ids": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    }
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBDBTrain")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        intef.set_path_param("db_id", db_id)
        intef.update_body("db_id", db_id)
        intef.update_body("mode", mode)
        return intef.request() if sendRequest else intef

    def staticDBGetSnapshotStatusGetApi(self, db_type, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSnapshotStatus """
        """  path: [get]/engine/{db_type}-feature/v1/get_snapshot_status API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "replicaset_snapshot_infos": [
                        {
                            "replica_set_id": "",
                            "snapshot_infos": [
                                {
                                    "index_id": "",
                                    "seq_id": ""
                                }
                            ],
                            "status": {}
                        }
                    ],
                    "result": {}
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBGetSnapshotStatus")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        return intef.request() if sendRequest else intef

    def staticDBGetSystemInfoGetApi(self, db_type, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  GetSystemInfo """
        """  path: [get]/engine/{db_type}-feature/v1/get_system_info API """
        """  params: 

        """
        """  resp:
                200():
                {
                    "db_summaries": [
                        {
                            "cached": false,
                            "db_id": "",
                            "deleted": false,
                            "indexes": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "max_size": "",
                            "total_capacity": "",
                            "total_size": ""
                        }
                    ],
                    "feature_version_infos": [
                        {
                            "feature_versions": [],
                            "object_type": ""
                        }
                    ],
                    "features": "",
                    "license_capacity": "",
                    "max_db_count": 0,
                    "max_query_per_second": 0,
                    "replica_set_summaries": [
                        {
                            "index_summaries": [
                                {
                                    "available_replicas": 0,
                                    "cached": false,
                                    "capacity": "",
                                    "index_uuid": "",
                                    "is_orphan": false,
                                    "size": ""
                                }
                            ],
                            "replica_set_id": "",
                            "worker_summaries": [
                                {
                                    "index_count": 0,
                                    "is_master": false,
                                    "is_offline": false,
                                    "last_seq_id": "",
                                    "license_capacity": "",
                                    "node_id": "",
                                    "total_capacity": "",
                                    "total_cpu_memory_bytes": "",
                                    "total_gpu_memory_bytes": "",
                                    "total_size": "",
                                    "used_cpu_memory_bytes": "",
                                    "used_gpu_memory_bytes": ""
                                }
                            ]
                        }
                    ]
                }

        """
        intef = collections.interface("viperOpenApi", "staticDBGetSystemInfo")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.set_path_param("db_type", db_type)
        return intef.request() if sendRequest else intef

    def imageIngressPassiveIngressStandardTargetImageAsyncPostApi(self, camera_info=None, capture_time=None, extra_fields=None, extra_info=None, full_image=None, ns_id=None, receive_time=None, storage_policy=None, target_images=None, task_object_config=None, loginToken=None, sendRequest=True, print_log=True, interface_desc=None):
        """  IngressStandardTargetImageAsync """
        """  path: [post]/v1/ingress_standard_target_image_async API """
        """  body: 
                {
                    "camera_info": {},
                    "capture_time": "",
                    "extra_fields": {
                        "additionalProp1": "",
                        "additionalProp2": "",
                        "additionalProp3": ""
                    },
                    "extra_info": "",
                    "full_image": {},
                    "ns_id": "",
                    "receive_time": "",
                    "storage_policy": {},
                    "target_images": [
                        {
                            "associations": [
                                {
                                    "associated_object_info": {},
                                    "association_type": "",
                                    "object_id": "",
                                    "type": {}
                                }
                            ],
                            "content": {},
                            "detection_mode": {},
                            "extra_info": "",
                            "feature_versions": {
                                "additionalProp1": "",
                                "additionalProp2": "",
                                "additionalProp3": ""
                            },
                            "target_info": {}
                        }
                    ],
                    "task_object_config": {}
                }
        """
        """  resp:
                200():
                {}

        """
        intef = collections.interface("viperOpenApi", "imageIngressPassiveIngressStandardTargetImageAsync")
        intef.set_print_log(print_log)
        intef.set_description(interface_desc)
        if loginToken:
            intef.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % loginToken)
        intef.update_body("camera_info", camera_info)
        intef.update_body("capture_time", capture_time)
        intef.update_body("extra_fields", extra_fields)
        intef.update_body("extra_info", extra_info)
        intef.update_body("full_image", full_image)
        intef.update_body("ns_id", ns_id)
        intef.update_body("receive_time", receive_time)
        intef.update_body("storage_policy", storage_policy)
        intef.update_body("target_images", target_images)
        intef.update_body("task_object_config", task_object_config)
        return intef.request() if sendRequest else intef

