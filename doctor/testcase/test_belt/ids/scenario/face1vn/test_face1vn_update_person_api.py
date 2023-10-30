#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
import random
from commonlib.config import ids_face1vn_search_person_image_path


@pytest.mark.P0
@pytest.mark.Regression
class TestFace1vnApi(object):
    """ face Api测试"""

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

    def test_api_FaceService_UpdatePerson_01(self, config_obj, FaceApi,test_tag_update_person,test_extra_info,db_operation):
        """更新人员信息_验证更新标签以及extra_info功能_原本有人员信息，输入有效的标签和extraInfo,预期人员信息被更新"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []
        tag_ids_all = []

        #step2入库两组人员
        tag_name_id={}
        #入库前先创建标签
        for i in range(8):
            name = "t"+str(i)
            description = "用于测试人员创建标签"
            resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
            tag_name_id[name]=resp.json_get("tag_id")
            tag_ids_all.append(resp.json_get("tag_id"))
            
        #第一组
        person_id = "a"
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        images = [image]
        origanl_extra_info ="test extra_info"
        auto_rotate = None
        min_quality_level = None
        encrypt_info=None
        original_tag_names=["t1","t2","t3","t4","t5","t6"]
        original_tag_ids=FaceApi.transfromNameToId(original_tag_names,tag_name_id)
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=origanl_extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=original_tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #step3更新人员信息，更新的信息有多种
        extra_info = test_extra_info
        tag_names = test_tag_update_person
        tag_ids=FaceApi.transfromNameToId(tag_names,tag_name_id)
        tag_list={
            "ids":tag_ids
        }
        resp = FaceApi.FaceService_UpdatePersonPostApi(db_id=db_id, person_id=person_id, extra_info=extra_info, tag_list=tag_list)
        assert resp.status_code == 200        
        #校验查看更新后的人员信息是否符合预期
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200 
        # 清理-删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        # 清理-删除标签    
        for id in tag_ids_all:
            FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=id)       
        #验证标签
        tags=resp.json_get("tags")
        result_tag_ids=[]
        result_tag_names=[]
        for tag in tags:
            result_tag_ids.append(tag["id"])
            result_tag_names.append(tag["name"])
        result_tag_ids.sort()
        result_tag_names.sort()
        tag_ids.sort()
        tag_names.sort()
        assert result_tag_ids==tag_ids
        assert result_tag_names==tag_names
        #验证extrainfo
        person=resp.json_get("person")
        assert person["extra_info"]==test_extra_info

    def test_api_FaceService_UpdatePerson_02(self, config_obj, FaceApi,test_invalid_tag_update_person,test_invalid_extra_info,db_operation):
        """更新人员信息_验证更新标签以及extra_info功能_原本有人员信息，输入无效的标签和extraInfo,预期人员信息不被更新"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []
        tag_ids_all = []

        #step2入库两组人员
        tag_name_id={}
        #入库前先创建标签
        for i in range(8):
            name = "t"+str(i)
            description = "用于测试人员创建标签"
            resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
            tag_name_id[name]=resp.json_get("tag_id")
            tag_ids_all.append(resp.json_get("tag_id"))
            
        #第一组
        person_id = "a"
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        images = [image]
        orignal_extra_info = "test extra_info"
        auto_rotate = None
        min_quality_level = None
        encrypt_info=None
        original_tag_names=["t1","t2","t3","t4","t5","t6"]
        original_tag_ids=FaceApi.transfromNameToId(original_tag_names,tag_name_id)
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=orignal_extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=original_tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #step3更新人员信息，更新的信息有多种
        extra_info = test_invalid_extra_info
        tag_list={
            "ids":test_invalid_tag_update_person
        }
        resp = FaceApi.FaceService_UpdatePersonPostApi(db_id=db_id, person_id=person_id, extra_info=extra_info, tag_list=tag_list)
        #校验查看更新后的人员信息是否符合预期,原本信息不改变
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200 
        
        # 清理-删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        # 清理-删除标签    
        for id in tag_ids_all:
            FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=id)       
            
        tags=resp.json_get("tags")
        result_tag_ids=[]
        result_tag_names=[]
        for tag in tags:
            result_tag_ids.append(tag["id"])
            result_tag_names.append(tag["name"])
        result_tag_ids.sort()
        result_tag_names.sort()
        original_tag_ids.sort()
        original_tag_names.sort()
        assert result_tag_ids==original_tag_ids
        assert result_tag_names==original_tag_names
        #验证extrainfo
        person=resp.json_get("person")
        assert person["extra_info"]==orignal_extra_info



if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])