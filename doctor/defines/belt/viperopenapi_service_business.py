#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os

from commonlib import sign_utils, config
from commonlib.decorator import wait
from commonlib.log_utils import log
from defines.belt.api.viperopenapi_service_swagger import ViperopenapiSwaggerApi

"""
使用说明：


"""
def getTaskByIDUntilSuccessFunc(resp_viper):
    """ 仅适用于仅有1个ingressType的情况"""
    if resp_viper.json["status"]["status"] == "OK":
        log().info("任务状态成功")
        return True

    else:
        log().info("任务状态尚未成功，继续查询")
        return False


# business相当于中间层，调最底层api
class ViperopenapiSwaggerBusiness(ViperopenapiSwaggerApi):
    """ 业务类代码写在这里"""

    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(ViperopenapiSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "Authorization"
        self.TOKEN_VALUE = "Bearer %s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)

    # 创建一个alert类型的布控库
    def create_NewDb(self, name=None, feature=None, db_size=None, type=None):
        # 随机生成一个库名字
        key = sign_utils.getUuid(6)
        name = "TestDB" + key
        feature_version = 25000
        description = "test"
        db_size = 500
        create_bucket = True
        type = 1
        resp_viper = self.apiWrapperNewDBPostApi(
            db_size=db_size,
            description=description,
            create_bucket=create_bucket,
            feature_version=feature_version,
            name=name,
            type=type)
        return resp_viper

    def create_db_and_delete(self,is_delete=True):
        resp=self.create_NewDb()
        db_id=resp.json["db_id"]

        #添加clear up,创建完后删除,self.DeleteDB等运行完case后再执行删除


        def clearUp():
            self.DeleteDB(db_id=db_id)

        # 此处self.ext_info and is_delete判断为True
        if self.ext_info and is_delete:
        # self.after_list={AttributeError}'ViperopenapiSwaggerBusiness' object has no attribute 'after_list'
            self.ext_info.addAfterFunc(clearUp)

        return resp

    def batch_add_image(self, db_id=None, image=None):
        images = [
            {
                "image": {
                    "image": {
                        "data": image
                    },
                    "face_selection": "LargestFace"
                },
                "quality_threshold": 0.3
            }
        ]
        resp_viper = self.apiWrapperBatchAddImageToDBPostApi(auto_rotation=None,
                                                             db_id=db_id,
                                                             extra_db_type="",
                                                             images=images,
                                                             save_images=True,
                                                             type="ALERT_FEATURE_DB",
                                                             loginToken=None,
                                                             sendRequest=True,
                                                             print_log=True,
                                                             interface_desc=None)

        assert resp_viper.status_code == 200
        assert resp_viper.json["results"][0]["status"] == "OK"
        image_url = resp_viper.json['items'][0]['image_url']
        bucket_name = image_url.split("/")[0]
        object_key = image_url.split("/")[1]
        # 传入图片的时候得到的特征id如下，留作删除时候用
        feature_id = resp_viper.json["items"][0]["feature_id"]
        return bucket_name, object_key, feature_id

    def Search_image_in_DB(self, db_id=None, image=None):
        dbs = [
            {
                "db_id": db_id,
                "top_k": 20,
                "min_score": 0.8
            }
        ]
        type = 1
        dropped_fields = [1]
        images = {
            "image": {
                "format": "IMAGE_UNKNOWN",
                "url": "",
                "data": image
            },
            "bounding": None,
            "face_selection": "LargestFace"
        }
        resp_viper = self.apiWrapperSearchImageInDBsPostApi(dbs=dbs,
                                                            dropped_fields=dropped_fields,
                                                            extra_db_type=None,
                                                            image=images,
                                                            type=type,
                                                            loginToken=None,
                                                            sendRequest=True,
                                                            print_log=True,
                                                            interface_desc=None)
        return resp_viper

    def DetectAndExtractPost(self, image=None):
        images = {
            "image": {
                "format": "IMAGE_UNKNOWN",
                "url": "",
                "data": image
            },
            "bounding": None,
            "face_selection": "LargestFace"
        }

        resp_viper = self.apiWrapperDetectAndExtractPostApi(feature_version=None,
                                                            image=images,
                                                            loginToken=None,
                                                            sendRequest=True,
                                                            print_log=True,
                                                            interface_desc=None)
        return resp_viper

    def staticDBFeatureBatchAdd(self,feature=None,db_id=None):
        #随机找的一个6个字符
        key = sign_utils.getUuid(6)
        db_type = "alert"
        items = [{
            "feature": feature,
            "image_id": "0",
            "key": key,
            "extra_info": "test"}]
        resp_viper = self.staticDBFeatureBatchAddPostApi(db_type=db_type,
                                                         col_id=db_id,
                                                         items=items,
                                                         loginToken=None,
                                                         sendRequest=True,
                                                         print_log=True,
                                                         interface_desc=None)
        return resp_viper,key

    def staticDBFeatureBatchGetByKey(self,db_id=None,key=None):
        db_type = "alert"
        resp_viper = self.staticDBFeatureBatchGetByKeyPostApi(db_type,
                                                                         col_id=db_id,
                                                                         consistency=None,
                                                                         ignore_details=None,
                                                                         keys=key,
                                                                         loginToken=None,
                                                                         sendRequest=True,
                                                                         print_log=True,
                                                                         interface_desc=None)
        return resp_viper

    def Image_CompareOneToOne(self, image1=None, image2=None):
        one = {
            "image": {
                "format": "IMAGE_UNKNOWN",
                "url": "",
                "data": image1
            },
            "bounding": None,
            "face_selection": "LargestFace"
        }
        other = {
            "image": {
                "format": "IMAGE_UNKNOWN",
                "url": "",
                "data": image2
            },
            "bounding": None,
            "face_selection": "LargestFace"
        }
        resp_viper = self.apiWrapperCompareOneToOnePostApi(feature_version=None,
                                                           one=one,
                                                           other=other,
                                                           loginToken=None,
                                                           sendRequest=True,
                                                           print_log=True,
                                                           interface_desc=None)
        return resp_viper

        #staticDBFeatureBatchSearch

    def staticDBFeatureBatchSearch(self,features=None,db_id=None):
        db_type = "alert"
        resp_viper = self.staticDBFeatureBatchSearchPostApi(db_type=db_type,
                                                            col_id=db_id,
                                                            consistency=None,
                                                            dropped_fields=None,
                                                            features=features,
                                                            min_score=0.8,
                                                            return_raw_feature=False,
                                                            top_k=20,
                                                            loginToken=None,
                                                            sendRequest=True,
                                                            print_log=True,
                                                            interface_desc=None)
        return resp_viper

    def imageFaceExtractCompareFeature(self,one=None,other=None):
        feature_version = 25000
        resp_viper = self.imageFaceExtractCompareFeaturePostApi(feature_version,
                                                            one=one,
                                                            other=other,
                                                            loginToken=None,
                                                            sendRequest=True,
                                                            print_log=True,
                                                            interface_desc=None)
        return resp_viper

    def OSGDownloadObjectGet(self,bucket_name=None,object_key=None):
        resp_viper = self.infraOSGDownloadObjectGetApi(bucket_name, object_key, print_log=False)
        return resp_viper

    def DeleteImageFromDB(self,feature_id=None,db_id=None):
        resp_viper = self.apiWrapperDeleteImageFromDBPostApi(db_id=db_id,
                                                                        delete_image=True,
                                                                        extra_db_type=None,
                                                                        feature_id=feature_id,
                                                                        key=None,
                                                                        type=1,
                                                                        loginToken=None,
                                                                        sendRequest=True,
                                                                        print_log=True,
                                                                        interface_desc=None)
        return resp_viper

    def DeleteDB(self,db_id=None):
        resp_viper = self.apiWrapperDeleteDBPostApi(db_id=db_id,
                                                    delete_bucket=True,
                                                    extra_db_type=None,
                                                    type=1,
                                                    loginToken=None,
                                                    sendRequest=True,
                                                    print_log=True,
                                                    interface_desc=None)
        return resp_viper

    def videoProcessTaskNewFire(self,source_address=None):
        task= {
        "object_type": "OBJECT_ALGO",
        "source_address": source_address,
        "camera_info": {
            "camera_id": "",
            "device_id": "",
            "device_type": "",
            "place_code": "",
            "place_name": "",
            "tollgate_id": "",
            "tollgate_name": "",
            "source_id": "",
            "internal_id": {
                "region_id": 128,
                "camera_idx": 1
            },
            "zone_id": ""
        },
        "feature_version": 0,
        "task_object_config": {
            "rules": [],
            "algo_config": {
                "app_name": "com.sensetime.algo.fire",
                "app_version": 20401,
                "data": {
                    "@jsonpb_type": "com.sensetime.algo.fire.task",
                    "rules": [
                        {
                            "activate_seconds": 1,
                            "cooldown_seconds": 1,
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
                            },
                            "type": "ST_CITY_FIRE"
                        }
                    ]
                }
            },
            "face_config": None,
            "faceped_config": None,
            "pach_config": None,
            "decoder_config": None,
            "snapshot_config": None,
            "crowd_config": None,
            "crowd_v2": None
        },
        "video_parameter": None,
        "storage_policy": None,
        "ns_id": "",
        "schedule_config": None
    }
        resp_viper=self.videoProcessTaskNewPostApi(task=task,
                                                   loginToken=None,
                                                   sendRequest=True,
                                                   print_log=True,
                                                   interface_desc=None)
        task_id=resp_viper.resp_json["task"]["task_id"]
        return resp_viper,task_id

    def videoProcessTaskNewOldFell(self,source_address=None,roi=None):
        if roi==None:
            task= {
            "object_type": "OBJECT_ALGO",
            "source_address": source_address,
            "camera_info": {
                "camera_id": "68679266",
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
                                "rule_id": "abcdefg",
                                "type": "ST_TUMBLE",
                            }
                        ]
                    }
                }
            }
            }
        else:
            task = {
                "object_type": "OBJECT_ALGO",
                "source_address": source_address,
                "camera_info": {
                    "camera_id": "68679266",
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
                                    "rule_id": "abcdefg",
                                    "type": "ST_TUMBLE",
                                    "roi": roi
                                }
                            ]
                        }
                    }
                }
            }
        resp_viper=self.videoProcessTaskNewPostApi(task=task,
                                                   loginToken=None,
                                                   sendRequest=True,
                                                   print_log=True,
                                                   interface_desc=None)
        task_id=resp_viper.resp_json["task"]["task_id"]
        return resp_viper,task_id
    def videoProcessTaskListGet(self):
        resp_viper=self.videoProcessTaskListGetApi(page_request_offset=0,
                                                   page_request_limit=100,
                                                   page_request_total=10000,
                                                   loginToken=None,
                                                   sendRequest=True,
                                                   print_log=True,
                                                   interface_desc=None)
        task_list=[]
        for task in resp_viper.json["tasks"]:
            task_id=task["info"]["task_id"]
            task_list.append(task_id)
        return resp_viper,task_list

    def videoProcessTaskDeleteDelete(self,task_id=None):
        resp_viper=self.videoProcessTaskDeleteDeleteApi(task_id=task_id,
                                                     loginToken=None,
                                                     sendRequest=True,
                                                     print_log=True,
                                                     interface_desc=None)
        return resp_viper

    def videoProcessDeleteAlltask(self,task_list=None):
        for task_id in task_list:
            resp_viper=self.videoProcessTaskDeleteDeleteApi(task_id=task_id,
                                                         loginToken=None,
                                                         sendRequest=True,
                                                         print_log=True,
                                                         interface_desc=None)
        return resp_viper

    @wait(timeout=60, interval=2, util_func=getTaskByIDUntilSuccessFunc, raise_exception=True)
    def gettaskByIDUntilAvailable(self,task_id=None):
        """ 查询任务直到可用"""
        #查询单个任务状态请求
        return self.videoProcessTaskStatusGetApi(task_id=task_id)