#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


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

    def test_api_FaceService_AddPerson(self, config_obj, FaceApi):
        """  添加人员信息到指定人员库. """
        db_id = None
        person_id = None
        images = None
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_ids = None
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        assert resp.status_code == 200

    def test_api_FaceService_AddPersonFace(self, config_obj, FaceApi):
        """  增加人员的人脸图. """
        db_id = None
        person_id = None
        image = None
        auto_rotate = None
        min_quality_level = None
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=image, auto_rotate=auto_rotate, min_quality_level=min_quality_level, encrypt_info=encrypt_info)
        assert resp.status_code == 200



    def test_api_FaceService_CreatePersonDB(self, config_obj, FaceApi):
        i=1
        """  创建人员库. """
        name = None
        description = None
        resp = FaceApi.FaceService_CreatePersonDBPostApi(name=name, description=description)
        assert resp.status_code == 200

    def test_api_FaceService_CreateTag(self, config_obj, FaceApi):
        """  创建人员在库中的业务标签. """
        db_id = None
        name = None
        description = None
        resp = FaceApi.FaceService_CreateTagPostApi(db_id=db_id, name=name, description=description)
        assert resp.status_code == 200

    def test_api_FaceService_DeletePerson(self, config_obj, FaceApi):
        """  获取人员详细信息. """
        db_id = None
        person_id = None
        resp = FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200

    def test_api_FaceService_DeletePersonDB(self, config_obj, FaceApi):
        """  删除指定人员库. """
        id = None
        resp = FaceApi.FaceService_DeletePersonDBPostApi(id=id)
        assert resp.status_code == 200

    def test_api_FaceService_DeletePersonFace(self, config_obj, FaceApi):
        """  删除人员的人脸特征. """
        db_id = None
        person_id = None
        face_id = None
        resp = FaceApi.FaceService_DeletePersonFacePostApi(db_id=db_id, person_id=person_id, face_id=face_id)
        assert resp.status_code == 200

    def test_api_FaceService_DeleteTag(self, config_obj, FaceApi):
        """  删除人员标签. """
        db_id = None
        tag_id = None
        resp = FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=tag_id)
        assert resp.status_code == 200



    def test_api_FaceService_GetPerson(self, config_obj, FaceApi):
        """  获取人员详细信息. """
        db_id = None
        person_id = None
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200

    def test_api_FaceService_ListPerson(self, config_obj, FaceApi):
        """  列举人员. """
        db_id = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_FaceService_ListPersonDB(self, config_obj, FaceApi):
        """  列举人员库. """
        page_offset = None
        page_limit = None
        page_total = None
        resp = FaceApi.FaceService_ListPersonDBGetApi(page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_FaceService_ListTag(self, config_obj, FaceApi):
        """  列举人员标签. """
        db_id = None
        page_offset = None
        page_limit = None
        page_total = None
        resp = FaceApi.FaceService_ListTagGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit, page_total=page_total)
        assert resp.status_code == 200

    def test_api_FaceService_SearchPerson(self, config_obj, FaceApi):
        """  提供人员库特征检索.
route prefix=ids internal_prefix=ids ac... """
        db_id = None
        image = None
        top_k = None
        min_score = None
        auto_rotate = None
        min_quality_level = None
        detect_liveness = None
        tag_ids = None
        with_detail = None
        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        assert resp.status_code == 200

    def test_api_FaceService_UpdatePerson(self, config_obj, FaceApi):
        """  修改人员信息，包括人员备注信息、标签，更新会覆盖原信息. """
        db_id = None
        person_id = None
        extra_info = None
        tag_ids = None
        resp = FaceApi.FaceService_UpdatePersonPostApi(db_id=db_id, person_id=person_id, extra_info=extra_info, tag_ids=tag_ids)
        assert resp.status_code == 200

    def test_api_FaceService_UpdatePersonDB(self, config_obj, FaceApi):
        """  更新指定人员库信息, 包括库名和特征版本. """
        id = None
        name = None
        description = None
        resp = FaceApi.FaceService_UpdatePersonDBPostApi(id=id, name=name, description=description)
        assert resp.status_code == 200
