#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import time

import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestViperopenapiScenario(object):
    """ Viperopenapi scenario test"""

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

    def test_scenario_000_demo(self):
        """ func test"""
        pass
    #12.6pass
    def Totest_scenario_000_Viper_Old_Interface_Check(self, config_obj, ViperopenapiApi):
        """ 检查NewDb接口 在 adapter 与 viper 的返回结果是否一致 王安写的"""
        # 0. 准备数据
        # name = "test_zero"
        # feature_version = 25000
        # description = "test"
        # db_size = 500
        # create_bucket = True
        # type = 1
        # extra_db_type = None
        # bucket_flattened = None
        # bucket_encrypt = None
        # enable_isolated_feature_table = None
        # # 1. 调adapter接口
        # resp_adapter = AdapterApi.NewDBPostApi(name=name, feature_version=feature_version, description=description,
        #                                        db_size=db_size, create_bucket=create_bucket, type=type,
        #                                        extra_db_type=extra_db_type, bucket_flattened=bucket_flattened,
        #                                        bucket_encrypt=bucket_encrypt,
        #                                        enable_isolated_feature_table=enable_isolated_feature_table)
        # assert resp_adapter.status_code == 200
        # 2. 调viper接口
        # resp_viper = ViperopenapiApi.apiWrapperNewDBPostApi(bucket_encrypt=bucket_encrypt,
        #                                                     bucket_flattened=bucket_flattened,
        #                                                     create_bucket=create_bucket,
        #                                                     db_size=db_size,
        #                                                     description=description,
        #                                                     enable_isolated_feature_table=enable_isolated_feature_table,
        #                                                     extra_db_type=extra_db_type, feature_version=feature_version,
        #                                                     name=name, type=type)
        # assert resp_viper.status_code == 200
        # # 3. 对比
        # assert resp_adapter.json_get("xxx.xxx.xxx") == resp_viper.json_get("xxx.xxx.xxx")
        # # demo
        # checkList = ["xxx.xxx.xxx",
        #              "yyyy.yyy.yyy"
        #              ]
        # for item in checkList:
        #     adapter_value = resp_adapter.json_get(item)
        #     viper_value = resp_viper.json_get(item)
        #     with check: assert adapter_value == viper_value, "%s字段返回结果不一致,%s=%s" % (
        #         item, adapter_value, viper_value)
        #

        #创建一个库 pass  AdapterApi
        res = ViperopenapiApi.create_NewDb()
        assert res.status_code == 200
        db_id = res.json["db_id"]


        # 往库里插入一张图片 pass
        image1_path = os.path.join(config.image_path, 'go_image/belt/face_record.jpeg')
        image1 = ViperopenapiApi.imageToBase64(image1_path)
        resp=ViperopenapiApi.batch_add_image(db_id=db_id,image=image1)
        bucket_name=resp[0]
        object_key=resp[1]
        feature_id=resp[2]

        # 在库里查询某一张图片pass
        resp=ViperopenapiApi.Search_image_in_DB(db_id=db_id,image=image1)
        assert resp.status_code == 200


        # 单张图片提取特征值 pass
        resp=ViperopenapiApi.DetectAndExtractPost(image=image1)
        assert resp.status_code == 200
        feature = resp.json["feature"]
        #feature_blob = resp.json["feature"]["blob"]


        # 将批量特征入静态库 pass
        resp=ViperopenapiApi.staticDBFeatureBatchAdd(feature=feature,db_id=db_id)
        key=resp[1]
        assert resp[0].status_code == 200


        # 通过用户自定义key在指定静态库中批量获取特征.key可以重复(用户自定义)
        db_id = db_id
        # 此处key是放在列表里的，需要加括号
        key=[key]
        resp=ViperopenapiApi.staticDBFeatureBatchGetByKey(db_id=db_id,key=key)
        assert resp.status_code == 200


        # 调用图片1:1接口 pass
        resp=ViperopenapiApi.Image_CompareOneToOne(image1=image1,image2=image1)
        assert resp.status_code == 200
        assert resp.json["score"] > 0.99


        # 在指定静态库（单库）中进行特征1：N检索 pass
        features = [feature]
        resp=ViperopenapiApi.staticDBFeatureBatchSearch(features=features,db_id=db_id)
        assert resp.status_code == 200
        assert resp.json["results"][0]["status"] == "OK"

        # 特征1：1比对.
        resp=ViperopenapiApi.imageFaceExtractCompareFeature(one=feature,other=feature)
        assert resp.status_code == 200
        assert resp.json["score"] > 0.99

        # 以二进制形式下载 Object 数据
        resp=ViperopenapiApi.OSGDownloadObjectGet(bucket_name=bucket_name,object_key=object_key)
        assert resp.status_code == 200
        # 下载的图片放在本机的tmp目录下
        with open(file='/tmp/b.jpeg', mode="wb") as f:
            f.write(resp.origin_resp.content)
        assert sign_utils.getMd5ByFile('/tmp/b.jpeg') == sign_utils.getMd5ByFile(image1_path)

        # 从库里删除一张图片 pass
        resp=ViperopenapiApi.DeleteImageFromDB(feature_id=feature_id,db_id=db_id)
        assert resp.status_code == 200
        assert resp.json["results"][0]["status"] == "OK"

        #删除一个库
        resp=ViperopenapiApi.DeleteDB(db_id=db_id)
        assert resp.status_code == 200
        assert resp.json == {}

    #没有applet资源暂时无法测试
    def Totest_scenario_001_Viper_Firetask_Check(self, config_obj, ViperopenapiApi):
        # vps创建任务
        source_address = "rtsp://10.4.132.35:8554/long_fire_yancheng.264"
        resp = ViperopenapiApi.videoProcessTaskNewFire(source_address)
        task_id = resp[1]
        assert resp[0].status_code == 200

        # 查询任务
        resp = ViperopenapiApi.videoProcessTaskListGet()
        task_list = resp[1]
        assert resp[0].status_code == 200
        # 从列表里看这该任务的状态是不是已经创建成功了
        assert task_id in task_list
        for i in resp[0].json["tasks"]:
            if task_id == i["info"]["task_id"]:
                assert i["status"]["status"] == "PENDING"

        # 查询一个任务直到成功为止
        resp = ViperopenapiApi.gettaskByIDUntilAvailable(task_id=task_id)
        assert resp.status_code == 200

    #pass
    def Totest_scenario_002_Viper_Old_Fell_Check(self, config_obj, ViperopenapiApi):
        # vps创建任务
        source_address = "rtsp://10.4.7.18:8554/fell.264"
        # 这里roi可以不传也可以传四个点，不要传２个点
        resp = ViperopenapiApi.videoProcessTaskNewOldFell(source_address, roi=None)
        task_id = resp[1]
        assert resp[0].status_code == 200

        # 查询任务
        resp = ViperopenapiApi.videoProcessTaskListGet()
        task_list = resp[1]
        assert resp[0].status_code  == 200
        # 从列表里看这该任务的状态是不是已经创建成功了
        assert task_id in task_list
        for i in resp[0].json["tasks"]:
            if task_id == i["info"]["task_id"]:
                assert i["status"]["status"] == "PENDING"

        # 查询一个任务直到成功为止
        resp=ViperopenapiApi.gettaskByIDUntilAvailable(task_id=task_id)
        assert resp.status_code == 200

    #12.6pass
    def Totest_scenario_003_Delete_All_task(self, config_obj, ViperopenapiApi):
        resp = ViperopenapiApi.videoProcessTaskListGet()
        task_list = resp[1]
        resp = ViperopenapiApi.videoProcessDeleteAlltask(task_list=task_list)
        assert resp.status_code == 200
        resp = ViperopenapiApi.videoProcessTaskListGet()
        task_list = resp[1]
        assert len(task_list)==0

