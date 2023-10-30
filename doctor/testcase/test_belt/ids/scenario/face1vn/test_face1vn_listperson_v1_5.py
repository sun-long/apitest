#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
import time
from commonlib import config, time_utils, sign_utils, utils
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
# @pytest.mark.Regression
@pytest.mark.P0
@pytest.mark.Regression
class TestFace1vnListPersonScenario(object):
    """ Face 1vn Person mangement scenario test"""

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

    @pytest.mark.P0
    def test_scenario_get_personlist_pages_01(self, config_obj, FaceApi ,test_person_id,db_operation):
        """ 查询人员列表接口_验证加入person_id过滤_id都在库内_使用正确person_id的规范"""
        db_id = db_operation[0]
        person_ids = []
        # 添加人员
        for i in range(10):
            person_id = "user_{}_{}".format(i, sign_utils.getUuid(5))
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids.append(person_id)
            assert resp.status_code == 200
            

        person_id = test_person_id
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        person_ids.append(person_id)
        assert resp.status_code == 200

        page_offset = 0
        page_limit = 5
        filter_person_id=test_person_id
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit,filter_person_id=filter_person_id)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) == 1
        persons=resp.json_get("persons")
        assert persons[0]["person_id"]==test_person_id
        assert resp.json_get("page")["total"]
        
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)
            


    @pytest.mark.P0
    def test_scenario_get_personlist_pages_02(self, config_obj, FaceApi ,test_person_id_not_in_db,db_operation):
        """ 查询人员列表接口_验证加入person_id过滤_id都不在库内_预期报错"""

        db_id = db_operation[0]
        person_ids = []
        # 添加人员
        for i in range(2):
            person_id = "user_{}_{}".format(i, sign_utils.getUuid(5))
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids.append(person_id)
            assert resp.status_code == 200

        page_offset = 0
        page_limit = 5
        filter_person_id=test_person_id_not_in_db
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit,filter_person_id=filter_person_id)
        assert resp.status_code!=200
        assert resp.json_get("error.details.0.message") == "the record is not found in db"
        assert resp.json_get("error.details.0.reason") == 12005001
        
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)


    @pytest.mark.P0
    def test_scenario_get_personlist_pages_03(self, config_obj, FaceApi ,test_person_id_not_true,db_operation):
        """ 查询人员列表接口_验证加入person_id过滤_使用错误person_id的规范"""

        db_id = db_operation[0]
        person_ids = []
        # 添加人员
        for i in range(2):
            person_id = "user_{}_{}".format(i, sign_utils.getUuid(5))
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids.append(person_id)
            assert resp.status_code == 200

        person_id = test_person_id_not_true
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        person_ids.append(person_id)
        assert resp.status_code != 200

        page_offset = 0
        page_limit = 5
        filter_person_id=test_person_id_not_true
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit,filter_person_id=filter_person_id)
        assert resp.status_code!=200
        assert resp.json_get("error.details.0.message") == "the person id is invalid"
        assert resp.json_get("error.details.0.reason") == 12003055
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)


    @pytest.mark.P0
    def test_scenario_get_personlist_pages_04(self, config_obj, FaceApi,db_operation ):
        """ 查询人员列表接口_验证marker功能_直接使用"""

        db_id = db_operation[0]
        person_ids = []
        # 添加人员
        for i in range(10):
            person_id = "user_{}_{}".format(i, sign_utils.getUuid(5))
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids.append(person_id)
            assert resp.status_code == 200
        page_limit = 5
        marker="marker"
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_marker= marker)
        assert resp.status_code!=200
        assert resp.json_get("error.details.0.message") == "invalid marker"
        assert resp.json_get("error.details.0.reason") == 12003042
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)


    # @pytest.mark.P0
    # def test_scenario_get_personlist_pages_05(self, config_obj, FaceApi ):
    #     """ 查询人员列表接口_验证marker功能_第一次使用offset_offset=0_limit=0_使用marker_limit=5_总共入库10"""
    #     db_id = FaceApi.newDB()
    #     # 添加人员
    #     for i in range(10):
    #         person_id = "user_{}".format(i)
    #         images = []
    #         images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
    #         resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
    #         assert resp.status_code == 200
    #     #第一次使用offset
    #     page_limit = 0
    #     page_offset=0
    #     resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset)
    #     assert resp.status_code == 200
    #     assert len(resp.json_get("persons")) ==0
    #     #第二次使用marker
    #     page_limit = 5
    #     resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_marker= marker)
    #     assert resp.status_code == 200
    #     assert len(resp.json_get("persons")) == 5
    #     assert resp.json_get("page")["total"]
    #     #删除库
    #     FaceApi.FaceService_DeletePersonDBPostApi(id=db_id)

    @pytest.mark.P0
    def test_scenario_get_personlist_pages_06(self, config_obj, FaceApi ,db_operation):
        """ 查询人员列表接口_验证marker功能_第一次使用offset_offset=0_limit=1_使用marker_limit=5_总共入库10"""

        db_id = db_operation[0]
        person_ids_all = []
        # 添加人员
        for i in range(10):
            person_id = "user_{}".format(i)
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids_all.append(person_id)
            assert resp.status_code == 200
        #第一次使用offset
        page_limit = 1
        page_offset=0
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) ==1
        marker=resp.json_get("page.marker")
        #第二次使用marker
        page_limit = 5
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_marker=marker)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) == 5
        person_ids=[]
        for person in resp.json_get("persons"):
            person_ids.append(person["person_id"])
        #验证顺序相关
        assert "user_5" in person_ids
        assert resp.json_get("page")["total"]
        # 删除人员
        for id in person_ids_all:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)



    @pytest.mark.P0
    def test_scenario_get_personlist_pages_07(self, config_obj, FaceApi,db_operation ):
        """ 查询人员列表接口_验证marker功能_第一次使用offset_offset=0_limit=1_使用marker_limit=20_超出总数_总共入库10"""

        db_id = db_operation[0]
        person_ids_all = []
        # 添加人员
        for i in range(10):
            person_id = "user_{}".format(i)
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids_all.append(person_id)
            assert resp.status_code == 200
        #第一次使用offset
        page_limit = 1
        page_offset=0
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) ==1
        marker=resp.json_get("page.marker")
        #第二次使用marker
        page_limit = 20
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_marker=marker)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) == 9
        person_ids=[]
        for person in resp.json_get("persons"):
            person_ids.append(person["person_id"])
        #验证顺序相关
        assert "user_9" in person_ids
        # 删除人员
        for id in person_ids_all:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)
        
    @pytest.mark.P0
    def test_scenario_get_personlist_pages_08(self, config_obj, FaceApi ,db_operation):
        """ 查询人员列表接口_验证marker功能_第一次使用offset_offset=0_limit=1_同时使用marker_offset_总共入库10"""
        db_id = db_operation[0]
        person_ids_all = []
        # 添加人员
        for i in range(10):
            person_id = "user_{}".format(i)
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids_all.append(person_id)
            assert resp.status_code == 200
        #第一次使用offset
        page_limit = 1
        page_offset=0
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) ==1
        marker=resp.json_get("page.marker")
        #第二次使用marker和offset
        page_limit = 2
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=0,page_marker= marker)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) == 2
        person_ids=[]
        for person in resp.json_get("persons"):
            person_ids.append(person["person_id"])
        #验证顺序相关
        assert "user_2" in person_ids
        assert resp.json_get("page")["total"]
        # 删除人员
        for id in person_ids_all:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)

        
    @pytest.mark.P0
    def test_scenario_get_personlist_pages_09(self, config_obj, FaceApi,db_operation ):
        """ 查询人员列表接口_验证marker功能_直接同时使用marker_offset_总共入库10"""
        db_id = db_operation[0]
        person_ids_all = []
        # 添加人员
        for i in range(10):
            person_id = "user_{}".format(i)
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids_all.append(person_id)
            assert resp.status_code == 200
        #直接使用marker和offset
        page_limit = 2
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=0,page_marker= "marker")
        assert resp.status_code != 200
        assert resp.json_get("error.details.0.message") == "invalid marker"
        assert resp.json_get("error.details.0.reason") == 12003042
        # 删除人员
        for id in person_ids_all:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)

        
        
    @pytest.mark.P0
    def test_scenario_get_personlist_pages_10(self, config_obj, FaceApi,db_operation ):
        """ 查询人员列表接口_验证marker功能_第一次使用offset_offset=0_limit=1_验证两种方式的顺序_使用marker_limit=5_使用offset_limit=5总共入库10"""

        db_id = db_operation[0]
        person_ids_all = []
        # 添加人员
        for i in range(10):
            person_id = "user_{}".format(i)
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids_all.append(person_id)
            assert resp.status_code == 200
        #第一次使用offset
        page_limit = 1
        page_offset=0
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) ==1
        marker=resp.json_get("page.marker")
        #第二次使用marker
        page_limit = 2
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_marker= marker)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) == 2
        person_ids_marker=[]
        for person in resp.json_get("persons"):
            person_ids_marker.append(person["person_id"])
        #验证顺序相关
        assert "user_2" in person_ids_marker
        #第三次使用offset
        page_limit = 2
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=1)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) == 2
        person_ids_offset=[]
        for person in resp.json_get("persons"):
            person_ids_offset.append(person["person_id"])
        #验证顺序相关
        assert "user_2" in person_ids_marker
        #验证顺序完全相同
        assert person_ids_marker==person_ids_offset
        # 删除人员
        for id in person_ids_all:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)



    @pytest.mark.P0
    def test_scenario_get_personlist_pages_11(self, config_obj, FaceApi,db_operation ):
        """ 查询人员列表接口_验证list和filter同时使用功能_填写了filter_person_id_使用offset_总共入库10"""

        db_id = db_operation[0]
        person_ids_all = []
        # 添加人员
        for i in range(10):
            person_id = "user_{}".format(i)
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids_all.append(person_id)
            assert resp.status_code == 200
        person_id = "test_person_id"
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        person_ids_all.append(person_id)
        assert resp.status_code == 200
        #第一次使用offset和filter,page_offset=0,page_limit = 1
        page_limit = 1
        page_offset=0
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset,filter_person_id="test_person_id")
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) ==1
        assert resp.json_get("persons")[0]["person_id"]=="test_person_id"
        #第一次使用offset和filter,page_offset=1,page_limit = 1
        page_limit = 1
        page_offset=1
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset,filter_person_id="test_person_id")
        assert resp.status_code == 200
        assert resp.resp_json =={}
        #验证顺序相关
        #第一次使用offset和filter,page_offset=1,page_limit = 1
        page_limit = 2
        page_offset=2
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset,filter_person_id="test_person_id")
        assert resp.status_code == 200
        assert resp.resp_json =={}
        # 删除人员
        for id in person_ids_all:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)

        

    @pytest.mark.P0
    def test_scenario_get_personlist_pages_12(self, config_obj, FaceApi,db_operation ):
        """ 查询人员列表接口_验证list和filter同时使用功能_填写了filter_person_id_使用marker_总共入库10"""
    
        db_id = db_operation[0]
        person_ids_all = []
        # 添加人员
        for i in range(10):
            person_id = "user_{}".format(i)
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids_all.append(person_id)
            assert resp.status_code == 200
        person_id = "test_person_id"
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        person_ids_all.append(person_id)
        assert resp.status_code == 200
        #第一次使用offset
        page_limit = 1
        page_offset=0
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset,filter_person_id="test_person_id")
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) ==1
        marker=resp.json_get("page.marker")
        #第二次使用marker和filter
        page_limit =1
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_marker= marker,filter_person_id="test_person_id")
        assert resp.status_code == 200
        assert resp.resp_json =={}
        # 删除人员
        for id in person_ids_all:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)



    @pytest.mark.P0
    def test_scenario_get_personlist_pages_13(self, config_obj, FaceApi,db_operation ):
        """ 查询人员列表接口_验证正反向参数_总共入库10"""

        db_id = db_operation[0]
        person_ids_all = []
        # 添加人员
        for i in range(10):
            person_id = "user_{}".format(i)
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            person_ids_all.append(person_id)
            assert resp.status_code == 200
        #第一次使用offset
        page_limit = 5
        page_offset=0
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset)
        assert resp.status_code == 200
        marker=resp.json_get("page.marker")
        #第二次使用marker,向后翻页
        page_limit =5
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset,page_backward=False,page_marker=marker)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) ==5

        person_ids=[]
        for person in resp.json_get("persons"):
            person_ids.append(person["person_id"])
        #验证顺序相关
        assert "user_8" in person_ids
        marker=resp.json_get("page.marker")
        #第三次使用marker,向前翻页
        page_limit =5
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_limit=page_limit,page_offset=page_offset,page_backward=True,page_marker=marker)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) ==5
        person_ids=[]
        for person in resp.json_get("persons"):
            person_ids.append(person["person_id"])
        #验证顺序相关
        assert "user_2" in person_ids
        # 删除人员
        for id in person_ids_all:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)




if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])