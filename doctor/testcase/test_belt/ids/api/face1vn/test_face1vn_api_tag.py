#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils, utils
from commonlib.log_utils import log

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


    def test_api_FaceService_CreateTag_1(self, config_obj, FaceApi,db_operation):
        """  创建人员在库中的业务标签. 正常"""
        db_id = db_operation[0]
        name = utils.getName()
        description = None
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        tag_id = resp.json_get("tag_id")
        assert resp.status_code == 200
        resp = FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=tag_id)
        assert resp.status_code == 200

        
        
    def test_api_FaceService_CreateTag_2(self, config_obj, FaceApi,db_operation):
        """  创建人员在库中的业务标签. 标签名称重复"""
        db_id = db_operation[0]
        name = "重复名称"
        description = None
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        assert resp.status_code == 200
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        assert resp.status_code == 409
        assert resp.json_get("error.details.0.message") == "already exists in db"

        
        
    def test_api_FaceService_CreateTag_3(self, config_obj, FaceApi,db_operation):
        """  创建人员在库中的业务标签. 标签名称超过60字符"""
        db_id = db_operation[0]
        name = "1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+"
        description = None
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "the tag name is too long"
        
        
    def test_api_FaceService_CreateTag_4(self, config_obj, FaceApi):
        """  创建人员在库中的业务标签. db_id不存在"""
        db_id = ""
        name = utils.getName()
        description = None
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        assert resp.status_code == 400
        
        
    def test_api_FaceService_CreateTag_5(self, config_obj, FaceApi):
        """  创建人员在库中的业务标签. db_id == None"""
        db_id = None
        name = utils.getName()
        description = None
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "the db id is empty"
        

    def test_api_FaceService_DeleteTag_1(self, config_obj, FaceApi,db_operation):
        """  删除人员标签.正常 """
        db_id = db_operation[0]
        name = utils.getName()
        description = None
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        tag_id = resp.json_get("tag_id")
        assert resp.status_code == 200
        resp = FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=tag_id)
        assert resp.status_code == 200
        
    def test_api_FaceService_DeleteTag_2(self, config_obj, FaceApi,db_operation):
        """  删除人员标签.正在使用的标签 """
        db_id = db_operation[0]
        name =utils.getName()
        description = None
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        tagid = resp.json_get("tag_id")
        person_id = sign_utils.getUuid(10)
        image_path = os.path.join(
        config.image_path, "go_image/ids_face/xueqi3.jpg")
        images = []
        images.append(FaceApi.imageToBase64(image_path))
        extra_info = "string"
        auto_rotate = True
        min_quality_level = "QUALITY_LEVEL_NONE"
        tag_ids = []
        tag_ids.append(tagid)
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        resp = FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=tagid)
        assert resp.status_code == 400 
        assert resp.json_get("error.details.0.message") == "the tag is currently in use and it cannot be deleted"
        
        
        
    def test_api_FaceService_DeleteTag_3(self, config_obj, FaceApi):
        """  删除人员标签.db_id = None """
        db_id = None
        tag_id = "167467213261907196"
        resp = FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=tag_id)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "the db id is empty"
        
    @pytest.mark.skip(reason="400标签被使用？")  
    def test_api_FaceService_DeleteTag_4(self, config_obj, FaceApi,db_operation):
        """  删除人员标签.tag_id = None """
        db_id = db_operation[0]
        tag_id = None
        resp = FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=tag_id)
        assert resp.status_code == 404
        assert resp.json_get("error.details.0.message") == "the tag is not found in db"
        

    def test_api_FaceService_ListTag_1(self, config_obj, FaceApi,db_operation):
        """  列举人员标签.正常 """
        db_id = db_operation[0]
        name = utils.getName()
        description = None
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        db_id = db_id
        page_offset = 0
        page_limit = 10
        page_total = 100
        resp = FaceApi.FaceService_ListTagGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200
        
    def test_api_FaceService_ListTag_2(self, config_obj, FaceApi):
        """  列举人员标签.db_id = None """
        db_id = None
        page_offset = 0
        page_limit = 1
        page_total = 100
        resp = FaceApi.FaceService_ListTagGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "the db id is empty"
        assert resp.json_get("error.message") == "E12003048: the db id is empty"
        
    def test_api_FaceService_ListTag_3(self, config_obj, FaceApi):
        """  列举人员标签.db_id 错误 """
        db_id = "54252354325425235"
        page_offset = 0
        page_limit = 1
        page_total = 100
        resp = FaceApi.FaceService_ListTagGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 404
        assert resp.json_get("error.message") == "E12005002: the person db is not found"
        
        
    def test_api_FaceService_ListTag_4(self, config_obj, FaceApi,db_operation):
        """  列举人员标签.page_offset < 0 """
        db_id = db_operation[0]
        page_offset = -1
        page_limit = 1
        page_total = 100
        resp = FaceApi.FaceService_ListTagGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "invalid page offset"
        
        
    def test_api_FaceService_ListTag_5(self, config_obj, FaceApi,db_operation):
        """  列举人员标签.page_limit < 0 """
        db_id = db_operation[0]
        page_offset = 0
        page_limit = -1
        page_total = 100
        resp = FaceApi.FaceService_ListTagGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "invalid page limit"
        
        
    def test_api_FaceService_ListTag_6(self, config_obj, FaceApi,db_operation):
        """  列举人员标签.page_limit > 100 """
        db_id = db_operation[0]
        page_offset = 0
        page_limit = 101
        page_total = 100
        resp = FaceApi.FaceService_ListTagGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "invalid page limit"
        
    