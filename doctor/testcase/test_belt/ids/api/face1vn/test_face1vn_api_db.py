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


    def test_api_FaceService_CreatePersonDB_1(self, config_obj, FaceApi):
        """  创建人员库-正常"""
        name = utils.getName()
        description = "None"
        resp = FaceApi.FaceService_CreatePersonDBPostApi(name=name, description = description)
        assert resp.status_code == 200
        id = resp.json_get("id")
        resp1 = FaceApi.FaceService_DeletePersonDBPostApi(id=id)
        assert resp1.status_code == 200
        
        
    def test_api_FaceService_CreatePersonDB_2(self, config_obj, FaceApi,db_operation):
        """  创建人员库-库名称重复"""
        id = db_operation[0]
        name = db_operation[2]
        description = "None"
        resp = FaceApi.FaceService_CreatePersonDBPostApi(name=name, description=description)
        assert resp.status_code == 409
        assert resp.json_get("error.details.0.message") == "person db name already exists"

        
    def test_api_FaceService_CreatePersonDB_3(self, config_obj, FaceApi):
        """  创建人员库-库名称超过60字符"""
        name = "1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+"
        description = "None"
        resp = FaceApi.FaceService_CreatePersonDBPostApi(name=name, description=description)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "the db name is too long"
        
        
    def test_api_FaceService_CreatePersonDB_4(self, config_obj, FaceApi):
        """  创建人员库-name为空"""
        name = ""
        description = ""
        resp = FaceApi.FaceService_CreatePersonDBPostApi(name=name, description=description)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "the db name is empty"


    def test_api_FaceService_UpdatePersonDB_1(self, config_obj, FaceApi,db_operation):
        """  更新指定人员库信息, 包括库名和特征版本.-正常 """
        id = db_operation[0]
        name = utils.getName()
        description = "None"
        resp = FaceApi.FaceService_UpdatePersonDBPostApi(id=id, name=name, description=description)
        assert resp.status_code == 200

        
        
    def test_api_FaceService_UpdatePersonDB_2(self, config_obj, FaceApi):
        """  更新指定人员库信息, 包括库名和特征版本.-库名称重复 """
        name = "重复名称1"
        description = "None"
        resp = FaceApi.FaceService_CreatePersonDBPostApi(name=name, description = description)
        assert resp.status_code == 200
        id = resp.json_get("id")
        resp = FaceApi.FaceService_UpdatePersonDBPostApi(id=id, name=name, description=description)
        assert resp.status_code == 200
        resp = FaceApi.FaceService_DeletePersonDBPostApi(id=id)
        assert resp.status_code == 200
        
        
    def test_api_FaceService_UpdatePersonDB_3(self, config_obj, FaceApi,db_operation):
        """  更新指定人员库信息, name为空 """
        id = db_operation[0]
        name = ""
        description = ""
        resp = FaceApi.FaceService_UpdatePersonDBPostApi(id=id, name=name, description=description)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "the db name is empty"

    def test_api_FaceService_UpdatePersonDB_4(self, config_obj, FaceApi,db_operation):
        """  更新指定人员库信息, name超出字符限制 """    
        id = db_operation[0]
        name = "1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+"
        description = "None"
        resp = FaceApi.FaceService_UpdatePersonDBPostApi(id=id, name=name, description=description)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "the db name is too long"

    def test_api_FaceService_DeletePersonDB(self, config_obj, FaceApi):
        """  删除指定人员库. 不存在的id"""
        id = ""
        resp = FaceApi.FaceService_DeletePersonDBPostApi(id=id)
        assert resp.status_code == 400
        
    def test_api_FaceService_ListPersonDB_1(self, config_obj, FaceApi,db_operation):
        """  列举人员库. 正常"""
        id = db_operation[0]
        page_offset = 0
        page_limit = 10
        page_total = None
        resp = FaceApi.FaceService_ListPersonDBGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200
        assert resp.json_get("page.limit") == 10
  
        
    def test_api_FaceService_ListPersonDB_2(self, config_obj, FaceApi):
        """  列举人员库. page_offset < 0"""
        page_offset = -1
        page_limit = 10
        page_total = None
        resp = FaceApi.FaceService_ListPersonDBGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "invalid page offset"
        
        
        
    def test_api_FaceService_ListPersonDB_3(self, config_obj, FaceApi):
        """  列举人员库. page_limit < 1"""
        page_offset = 0
        page_limit = -1
        page_total = None
        resp = FaceApi.FaceService_ListPersonDBGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "invalid page limit"
        
        
        
    def test_api_FaceService_ListPersonDB_4(self, config_obj, FaceApi):
        """  列举人员库. page_limit > 100"""
        page_offset = 0
        page_limit = 101
        page_total = None
        resp = FaceApi.FaceService_ListPersonDBGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "invalid page limit"
        
    #需要最后一个，会清理掉所有库   
    def test_api_FaceService_CreatePersonDB_5(self, config_obj, FaceApi):
        """创建人员库_限制物理库数量"""
        resp=FaceApi.FaceService_ListPersonDBGetApi(page_offset=0, page_limit=100, page_total=100)
        page=resp.json_get("page")
        if  "total" not in page.keys():
            now_number=0
        else:
            now_number=page["total"]
    
        #step1:如果库大于等于10个，清理库
        if now_number>=10:
            ids=[]
            resp=FaceApi.FaceService_ListPersonDBGetApi(page_offset=0, page_limit=100, page_total=100)
            for person_db in resp.json_get("person_dbs"):
                ids.append(person_db["id"])
            for id in ids:
                resp = FaceApi.FaceService_DeletePersonDBPostApi(id=id)
        #step2:当前库<10,继续创建，直到10个
        for i in range(10-now_number):
            name = "test_db_name_{}_{}".format(i, sign_utils.getUuid(5))
            description = ""
            resp = FaceApi.FaceService_CreatePersonDBPostApi(name=name, description=description)
            assert resp.status_code ==200
        #step3:此时达到库限制10，继续创建则报库限制
        name = "test_db_name_{}_{}".format(56, sign_utils.getUuid(5))
        resp = FaceApi.FaceService_CreatePersonDBPostApi(name=name, description=description)
        assert resp.status_code ==429
        assert resp.json_get("error.details.0.message") == "person db number limit exceeded"
        #step4:清理库
        ids=[]
        resp=FaceApi.FaceService_ListPersonDBGetApi(page_offset=0, page_limit=100, page_total=100)
        for person_db in resp.json_get("person_dbs"):
            ids.append(person_db["id"])
        for id in ids:
            resp = FaceApi.FaceService_DeletePersonDBPostApi(id=id)    
        





