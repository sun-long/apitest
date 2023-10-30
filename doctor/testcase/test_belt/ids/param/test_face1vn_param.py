#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestFace1vnParam(object):
    """ face Param测试"""

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

    person_id_too_long = sign_utils.getUuid(65)
    extra_info_too_long = 257*"a"
    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', 123),
        ('db_id', None),
       # ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', 12.45),
        ('person_id', None),
        ('person_id', person_id_too_long),
        ('person_id', 'abc,-$#123'),
        ('images', 'invalidimages'),
      #  ('images', ['']),
        ('images', [111,222,333]),
        ('images', []),
       # ('images', ['1111','2222']),
        ('images', None),
        ('extra_info', 1.0),
        ('extra_info', extra_info_too_long),
        ('auto_rotate', 'invalidauto_rotate'),
        ('auto_rotate', ''),
        ('min_quality_level', 'invalidmin_quality_level'),
        ('min_quality_level', ''),
        ('tag_ids', 'invalidtag_ids'),
        ('tag_ids', ['invalidtag_ids']),
        ('tag_ids', ''),
        ('encrypt_info', 'invalidencrypt_info'),
        ('encrypt_info', ''),
    ])
    def test_api_FaceService_AddPersonInvalidParam(self, invalidParam, config_obj, FaceApi,db_operation):
        """  添加人员信息到指定人员库. """
        db_id = db_operation[0]
        person_id = "autotest"+sign_utils.getUuid(5)
        images= []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        extra_info = "extra_info"
        auto_rotate = False
        min_quality_level = "QUALITY_LEVEL_NONE"
        tag_ids =  [db_operation[1][0]]
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        intef = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', None),
        ('image', 'invalidimage'),
        ('image', ''),
        ('image', None),
        ('auto_rotate', 'invalidauto_rotate'),
        ('auto_rotate', ''),
        ('auto_rotate', None),
        ('min_quality_level', 'invalidmin_quality_level'),
        ('min_quality_level', ''),
        ('min_quality_level', None),
        ('encrypt_info', 'invalidencrypt_info'),
        ('encrypt_info', ''),
        ('encrypt_info', None),
    ])
    def test_api_FaceService_AddPersonFaceInvalidParam(self, invalidParam, config_obj, FaceApi):
        """  增加人员的人脸图. """
        db_id = None
        person_id = None
        image = None
        auto_rotate = None
        min_quality_level = None
        encrypt_info = None
        intef = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=image, auto_rotate=auto_rotate, min_quality_level=min_quality_level, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200



    @pytest.mark.parametrize("invalidParam", [
        # ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
    ])
    def test_api_FaceService_CreatePersonDBInvalidParam(self, invalidParam, config_obj, FaceApi):
        """  创建人员库. """
        name = None
        description = None
        intef = FaceApi.FaceService_CreatePersonDBPostApi(name=name, description=description, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
    ])
    def test_api_FaceService_CreateTagInvalidParam(self, invalidParam, config_obj, FaceApi):
        """  创建人员在库中的业务标签. """
        db_id = None
        name = None
        description = None
        intef = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', 123),
        ('db_id', ''),
        ('db_id', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', 123),
        ('person_id', ''),
        ('person_id', None),
    ])
    def test_api_FaceService_DeletePersonInvalidParam(self, invalidParam, config_obj, FaceApi, db_operation):
        """  删除人员. """
        db_id = db_operation[0]
        person_id = "autotest"+sign_utils.getUuid(5)
        intef = FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=person_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
    ])
    def test_api_FaceService_DeletePersonDBInvalidParam(self, invalidParam, config_obj, FaceApi):
        """  删除指定人员库. """
        id = None
        intef = FaceApi.FaceService_DeletePersonDBPostApi(id=id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', None),
        ('face_id', 'invalidface_id'),
        ('face_id', ''),
        ('face_id', None),
    ])
    def test_api_FaceService_DeletePersonFaceInvalidParam(self, invalidParam, config_obj, FaceApi):
        """  删除人员的人脸特征. """
        db_id = None
        person_id = None
        face_id = None
        intef = FaceApi.FaceService_DeletePersonFacePostApi(db_id=db_id, person_id=person_id, face_id=face_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('tag_id', 'invalidtag_id'),
        ('tag_id', ''),
        ('tag_id', None),
    ])
    def test_api_FaceService_DeleteTagInvalidParam(self, invalidParam, config_obj, FaceApi):
        """  删除人员标签. """
        db_id = None
        tag_id = None
        intef = FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=tag_id, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200



    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', None),
    ])
    def test_api_FaceService_GetPersonInvalidParam(self, invalidParam, config_obj, FaceApi,db_operation):
        """  获取人员详细信息. """
        db_id = db_operation[0]
        person_id = None
        intef = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', 123),
        ('db_id', ''),
        ('db_id', None),
        ('page.offset', 'invalidpage_offset'),
        ('page.offset', ''),
        ('page.offset', -10),
        ('page.limit', 'invalidpage_limit'),
        ('page.limit', ''),
        ('page.limit', 101),
      #  ('page.total', 'invalidpage_total'),
      #  ('page.total', ''),
      #  ('page.total', -10),
    ])
    def test_api_FaceService_ListPersonInvalidParam(self, invalidParam, config_obj, FaceApi,db_operation):
        """  列举人员Invalid Param. """
        db_id = db_operation[0]
        page_offset = 0
        page_limit = 10
        page_total = 10
        intef = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('page.offset', 'invalidpage_offset'),
        ('page.offset', ''),
      #  ('page_offset', None),
        ('page.limit', 'invalidpage_limit'),
        ('page.limit', ''),
       # ('page_limit', None),
        ('page.total', 'invalidpage_total'),
        ('page.total', ''),
       # ('page_total', None),
    ])
    def test_api_FaceService_ListPersonDBInvalidParam(self, invalidParam, config_obj, FaceApi):
        """  列举人员库. """
        page_offset = 0
        page_limit = 10
        page_total = 20
        intef = FaceApi.FaceService_ListPersonDBGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
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
    def test_api_FaceService_ListTagInvalidParam(self, invalidParam, config_obj, FaceApi):
        """  列举人员标签. """
        db_id = None
        page_offset = None
        page_limit = None
        page_total = None
        intef = FaceApi.FaceService_ListTagGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total, sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200
    @pytest.mark.P2
    @pytest.mark.Regression
    @pytest.mark.parametrize("invalidParam", [
        ('db_id', '123'),
        ('db_id', ''),
        ('db_id', None),
        ('image', 'ewewewew'),
        ('image', ''),
        ('image', None),
        ('top_k', -1),
        ('top_k', ''),
        ('top_k', None),
        ('min_score', '-1'),
        ('min_score', ''),
        ('min_score', None),
        ('auto_rotate', 'ds'),
        ('auto_rotate', ''),
        ('auto_rotate', None),
        ('min_quality_level', 'ds'),
        ('min_quality_level', ''),
        ('detect_liveness', 'ds'),
        ('detect_liveness', ''),
        ('detect_liveness', None),
        ('tag_ids', {}),
        ('tag_ids', ''),
        ('tag_ids', None),
        ('with_detail', 'ds'),
        ('with_detail', ''),
        ('with_detail', None),
    ])
    def test_api_FaceService_SearchPersonInvalidParam(self, invalidParam, config_obj, FaceApi,db_operation):
        """人员搜索接口_验证非法入参_预期不奔溃 """
       #第一步：创建库
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id =  db_operation[0]
        #第二步：入库
        person_id = "a"
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        images = [image]
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_ids = None
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        #第三步：搜索
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        top_k = 1
        min_score = 0.8
        auto_rotate = True
        min_quality_level = True
        detect_liveness = True
        tag_ids = []
        with_detail = True
        intef = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        #第三步：删库
        # FaceApi.FaceService_DeletePersonDBPostApi(id=db_id)     
        #校验逻辑   
        assert resp.status_code != 200


    @pytest.mark.parametrize("invalidParam", [
        ('db_id', 'invaliddb_id'),
        ('db_id', ''),
        ('db_id', None),
        ('person_id', 'invalidperson_id'),
        ('person_id', ''),
        ('person_id', None),
        # ('extra_info', 'invalidextra_info'),
        # ('extra_info', ''),
        # ('extra_info', None),
        ('tag_list', 'invalidtag_list'),
        ('tag_list', ''),
        ('tag_list', None),
    ])
    def test_api_FaceService_UpdatePersonInvalidParam(self, invalidParam, config_obj, FaceApi):
        """  修改人员信息，包括人员备注信息、标签，更新会覆盖原信息.
route prefix=ids inte... """
        #step1创建库
        db_id=FaceApi.newDB()
        #step2入库两组人员
        tag_name_id={}
        #入库前先创建标签
        name = "t1"
        description = "用于测试人员创建标签"
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        tag_name_id[name]=resp.json_get("tag_id")
        #第一组
        person_id = "a"
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        images = [image]
        orignal_extra_info ="test extra_info"
        auto_rotate = None
        min_quality_level = None
        encrypt_info=None
        original_tag_names=["t1"]
        original_tag_ids=FaceApi.transfromNameToId(original_tag_names,tag_name_id)
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=orignal_extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=original_tag_ids, encrypt_info=encrypt_info)
        #更新信息
        extra_info = "test extra_info"
        tag_names = ["t1"]
        tag_ids=FaceApi.transfromNameToId(tag_names,tag_name_id)
        tag_list={
            "ids":tag_ids
        }
        intef = FaceApi.FaceService_UpdatePersonPostApi(db_id=db_id, person_id=person_id, extra_info=extra_info, tag_list=tag_list, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        # assert resp.status_code != 200        
        #校验查看更新后的人员信息是否符合预期,原本信息不改变
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200 
        tags=resp.json_get("tags")
        result_tag_ids=[]
        result_tag_names=[]
        for tag in tags:
            result_tag_ids.append(tag["id"])
            result_tag_names.append(tag["name"])
        result_tag_ids.sort()
        result_tag_names.sort
        original_tag_ids.sort()
        original_tag_names.sort()
        assert result_tag_ids==original_tag_ids
        assert result_tag_names==original_tag_names
        #验证extrainfo
        person=resp.json_get("person")
        assert person["extra_info"]==orignal_extra_info

    @pytest.mark.parametrize("invalidParam", [
        ('id', 'invalidid'),
        ('id', ''),
        ('id', None),
        ('name', 'invalidname'),
        ('name', ''),
        ('name', None),
        ('description', 'invaliddescription'),
        ('description', ''),
        ('description', None),
    ])
    def test_api_FaceService_UpdatePersonDBInvalidParam(self, invalidParam, config_obj, FaceApi):
        """  更新指定人员库信息, 包括库名和特征版本. """
        id = None
        name = None
        description = None
        intef = FaceApi.FaceService_UpdatePersonDBPostApi(id=id, name=name, description=description, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200
