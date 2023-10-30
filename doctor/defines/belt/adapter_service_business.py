#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from commonlib import sign_utils
from commonlib.decorator import wait
from commonlib.log_utils import log
from defines.belt.api.adapter_service_swagger import AdapterSwaggerApi

"""
使用说明：


"""



def getAdapterTaskByIDUntilSuccessFunc(resp):
    """ 查询单个任务状态是否OK"""
    if resp == "OK":
        log().info("任务状态已经OK")
        return True
    else:
        log().info("任务状态尚未OK，请等待")
        return False


class AdapterSwaggerBusiness(AdapterSwaggerApi):
    """ 业务类代码写在这里"""

    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(AdapterSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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
        name = "TestAlertDB" + key
        feature_version = 25000
        description = "test"
        db_size = 500
        create_bucket = True
        type = 1
        resp_viper = self.NewDBPostApi(
            db_size=db_size,
            description=description,
            create_bucket=create_bucket,
            feature_version=feature_version,
            name=name,
            type=type)
        return resp_viper

    def create_db_and_delete(self, is_delete=True):
        i = 1
        resp = self.create_NewDb()
        db_id = resp.json["db_id"]

        # 添加clear up,创建完后删除,self.DeleteDB等运行完case后再执行删除
        i = 1

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
        resp_viper = self.BatchAddImageToDBPostApi(auto_rotation=None,
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
        resp_viper = self.SearchImageInDBsPostApi(dbs=dbs,
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

        resp_viper = self.DetectAndExtractPostApi(feature_version=None,
                                                  image=images,
                                                  loginToken=None,
                                                  sendRequest=True,
                                                  print_log=True,
                                                  interface_desc=None)
        return resp_viper

    def staticDBFeatureBatchAdd(self, feature=None, db_id=None):
        # 随机找的一个6个字符
        key = sign_utils.getUuid(6)
        items = [{
            "feature": feature,
            "image_id": "0",
            "key": key,
            "extra_info": "test"}]
        resp_viper = self.FeatureBatchAddPostApi(
            col_id=db_id,
            items=items,
            loginToken=None,
            sendRequest=True,
            print_log=True,
            interface_desc=None)
        return resp_viper, key

    def staticDBFeatureBatchGetByKey(self, db_id=None, key=None):
        db_type = "alert"
        resp_viper = self.FeatureBatchGetByKeyPostApi(db_type,
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
        resp_viper = self.CompareOneToOnePostApi(feature_version=None,
                                                 one=one,
                                                 other=other,
                                                 loginToken=None,
                                                 sendRequest=True,
                                                 print_log=True,
                                                 interface_desc=None)
        return resp_viper

        # staticDBFeatureBatchSearch

    def staticDBFeatureBatchSearch(self, features=None, db_id=None):
        db_type = "alert"
        resp_viper = self.FeatureBatchSearchPostApi(db_type=db_type,
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

    def imageFaceExtractCompareFeature(self, one=None, other=None):
        feature_version = 25000
        resp_viper = self.CompareFeaturePostApi(
            one=one,
            other=other,
            loginToken=None,
            sendRequest=True,
            print_log=True,
            interface_desc=None)
        return resp_viper

    def OSGDownloadObjectGet(self, bucket_name=None, object_key=None):
        resp_viper = self.DownloadObjectGetApi(bucket_name, object_key, print_log=False)
        return resp_viper

    def DeleteImageFromDB(self, feature_id=None, db_id=None):
        resp_viper = self.DeleteImageFromDBPostApi(db_id=db_id,
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

    def DeleteDB(self, db_id=None):
        resp_viper = self.DeleteDBPostApi(db_id=db_id,
                                          delete_bucket=True,
                                          extra_db_type=None,
                                          type=1,
                                          loginToken=None,
                                          sendRequest=True,
                                          print_log=True,
                                          interface_desc=None)
        return resp_viper

    def AdapterTaskNew(self, source_address=None):
        task = {
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
                    "region_id": 2,
                    "camera_idx": 2
                },
                "zone_id": ""
            },
            "task_object_config": {
                "rules": [],
                "algo_config": {
                    "app_name": "com.sensetime.algo.home.based.care",
                    "app_version": 10101,
                    "data": {
                        "rules": [
                            {
                                "rule_id": "a",
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
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                },

            },
        }
        resp_viper = self.TaskNewPostApi(task=task,
                                         loginToken=None,
                                         sendRequest=True,
                                         print_log=True,
                                         interface_desc=None)
        task_id = resp_viper.resp_json["task"]["task_id"]
        return resp_viper, task_id

    def AdapterTaskNewFire(self, source_address=None):
        task = {
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
        resp_viper = self.TaskNewPostApi(task=task,
                                         loginToken=None,
                                         sendRequest=True,
                                         print_log=True,
                                         interface_desc=None)
        task_id = resp_viper.resp_json["task"]["task_id"]
        return resp_viper, task_id

    def AdapterTaskNewOldFell(self, source_address=None, roi=None):
        if roi == None:
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
        resp_viper = self.TaskNewPostApi(task=task,
                                         loginToken=None,
                                         sendRequest=True,
                                         print_log=True,
                                         interface_desc=None)
        task_id = resp_viper.resp_json["task"]["task_id"]
        return resp_viper, task_id

    def AdapterTaskListGet(self):
        resp_viper = self.TaskListGetApi(page_request_offset=0,
                                         page_request_limit=100,
                                         page_request_total=10000,
                                         loginToken=None,
                                         sendRequest=True,
                                         print_log=True,
                                         interface_desc=None)
        task_list = []
        for task in resp_viper.json["tasks"]:
            task_id = task["info"]["task_id"]
            task_list.append(task_id)
        return resp_viper, task_list

    #通过输入task_id查询当前任务状态,自己封装的
    def AdapterSignalTaskGet(self, task_id=None):
        resp_viper = self.TaskListGetApi(page_request_offset=0,
                                         page_request_limit=100,
                                         page_request_total=10000,
                                         loginToken=None,
                                         sendRequest=True,
                                         print_log=True,
                                         interface_desc=None)
        for task in resp_viper.json["tasks"]:
            if task_id==task["info"]["task_id"]:
                task_status=task["status"]["status"]
                log().info("当前的任务状态是%s"%task_status)
                return task_status

    def AdapterDeleteAlltask(self, task_list=None):
        for task_id in task_list:
            resp_viper = self.TaskDeleteDeleteApi(task_id=task_id,
                                                  loginToken=None,
                                                  sendRequest=True,
                                                  print_log=True,
                                                  interface_desc=None)
        return resp_viper

    def AdapterDeleteSignaltask(self, task_id=None):
        resp_viper = self.TaskDeleteDeleteApi(task_id=task_id,
                                              loginToken=None,
                                              sendRequest=True,
                                              print_log=True,
                                              interface_desc=None)
        return resp_viper


    @wait(timeout=120, interval=2, util_func=getAdapterTaskByIDUntilSuccessFunc,raise_exception=True)
    def getAdaptertaskByIDUntilAvailable(self,task_id=None):
        """ 查询任务直到可用"""
        # 查询单个任务状态请求 adapter没有这个接口
        return self.AdapterSignalTaskGet(task_id=task_id)


    def AdapterFeatureBatchAdd(self, feature=None, db_id=None, key=None):
        items = [
            {
                "feature": feature,
                "image_id": "testabc",
                "extra_info": "test",
                "key": key
            }
        ]
        intef = self.FeatureBatchAddPostApi(sendRequest=False, col_id=db_id, items=items)
        intef.set_path("v1/databases/%s/batch_add" % (db_id))
        res = intef.request()
        return res

    def AdapterFeatureBatchGetByKey(self, db_id=None, key=None):
        intef = self.FeatureBatchGetByKeyPostApi(sendRequest=False, col_id=db_id, keys=key,db_type=None)
        intef.set_path("v1/databases/%s/batch_get_by_key" % (db_id))
        res = intef.request()
        return res


    def AdapterFeatureBatchSearch(self, db_id=None, features=None):
        # top_k=20,
        # min_score=0.8,
        # return_raw_feature=False,
        # dropped_fields= [1]
        intef = self.FeatureBatchSearchPostApi(sendRequest=False, col_id=db_id, features=features,db_type=None,top_k=20,min_score=0.8,
                                               return_raw_feature=False,dropped_fields=None)
        intef.set_path("v1/databases/%s/batch_search" % (db_id))
        res = intef.request()
        return res

