#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
import random
from commonlib.config import ids_face1vn_search_person_image_path
import time
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
from commonlib.api_lib.AES_new import *

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

    def test_api_FaceService_SearchPerson_01(self, config_obj, FaceApi,db_operation):
        """人员搜索单接口_验证face1:n的对比功能_image和入库图片设置为相同图片_预期搜索结果的top1是预先入库的图片对应的person"""
        #step1创建库
        #db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []
        #step2入库两组人员，a1,b1
        #第一组
        person_id = "a"
        a_image1=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        a_image2=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image2.jpg")
        images = [a_image1,a_image2]
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_ids = None
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #第二组
        person_id = "b"
        b_image1=FaceApi.idsImageToBase64(f"face1vn/search_person/b_image1.jpg")
        b_image2=FaceApi.idsImageToBase64(f"face1vn/search_person/b_image2.jpg")
        images = [b_image1,b_image2]
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_ids = None
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)        
        person_ids.append(person_id)
        #step3检索
        time.sleep(3)
        image_query = a_image1
        top_k = 10
        min_score = 0
        auto_rotate = None
        min_quality_level = None
        detect_liveness = None
        tag_ids = None
        with_detail = None
        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        #校验逻辑
        assert resp.status_code == 200        
        assert resp.json_get("results")
        results=resp.json_get("results")
        top1=results[0]
        assert top1["person"]["person_id"]=="a"#top1必定是"a"
        for result in results:
            result_score=result["score"]
            assert result_score>=min_score#结果分数必须大于min_score
        num=len(results)
        assert num<=top_k#返回的结果必定小于top_k

        

    def test_api_FaceService_SearchPerson_02(self, config_obj, FaceApi,test_tag_search_person,db_operation):
        """人员搜索单接口_验证标签的有效性_预先创建不同的标签_检索时使用不同的检索组合"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []
        tag_ids_all = []
        #step2入库两组人员，a1,b1
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
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_names=["t1","t2","t3","t4","t5","t6"]
        tag_ids=FaceApi.transfromNameToId(tag_names,tag_name_id)
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #第二组
        person_id = "b"
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_names = ["t1","t2","t3"]
        tag_ids=FaceApi.transfromNameToId(tag_names,tag_name_id)
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)        
        person_ids.append(person_id)
        #第三组
        person_id = "c"
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_names = ["t4","t5","t6"]
        tag_ids=FaceApi.transfromNameToId(tag_names,tag_name_id)
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)        
        person_ids.append(person_id)
        #step3检索
         
        image_query = image
        top_k = 10
        min_score = 0
        auto_rotate = None
        min_quality_level = None
        detect_liveness = None
        tag_ids =FaceApi.transfromNameToId(test_tag_search_person,tag_name_id)      
        with_detail = None
        time.sleep(3)
        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        # 清理-删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        # 清理-删除标签    
        for id in tag_ids_all:
            FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=id)   
        
        #校验逻辑
        assert resp.status_code == 200        
        #不同的输入query的tag
        #有搜索结果的情况["t1"],["t1","t2"],["t2","t1"],["t1","t2","t3"],["t4","t5","t6"],["t1","t2","t3","t4","t5","t6"]
        #无搜索结果的情况[],["t6","t7"],["t7","t8"]，此次预期是无符合条件的搜索，即result=[]
        #搜索结果个数的判别、搜索结果人员的判别
        if "t7" in test_tag_search_person:#["t6","t7"],["t7","t8"]
            assert resp.resp_json=={}
        else:
            results=resp.json_get("results")
            person_ids=[]
            for result in results:
                person_ids.append(result["person"]["person_id"])
            if test_tag_search_person==["t1","t2","t3","t4","t5","t6"]:
                assert len(results)==1
                assert "a" in person_ids
            elif test_tag_search_person==["t4","t5","t6"]:
                assert len(results)==2
                assert "a" in person_ids
                assert "c" in person_ids
            elif "t1" in test_tag_search_person:#["t1"],["t1","t2"],["t2","t1"],["t1","t2","t3"]
                assert len(results)==2
                assert "a" in person_ids
                assert "b" in person_ids
            elif test_tag_search_person==[]:
                assert len(results)==3
                assert "a" in person_ids
                assert "b" in person_ids
                assert "c" in person_ids


    def test_api_FaceService_SearchPerson_03(self, config_obj, FaceApi,db_operation):
        """人员搜索单接口_验证min_score的有效性_预期搜索结果的分数均大于min_score且分数为降序排列"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []
        index=0
        #step2入库10组人员
        for i in range(10):
            index=index+1
            person_id = "a"+str(index)
            pick_image=FaceApi.randomSelectOneImage(ids_face1vn_search_person_image_path)
            image= FaceApi.imageToBase64(pick_image)
            images = [image]
            extra_info = None
            auto_rotate = None
            min_quality_level = None
            tag_ids = None
            encrypt_info = None
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
            person_ids.append(person_id)
        #step3检索
        time.sleep(3)
        image_query = image
        top_k = 10
        min_score = 0.08
        auto_rotate = None
        min_quality_level = None
        detect_liveness = None
        tag_ids = None
        with_detail = None
        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        #校验逻辑，检索得到的结果分数必须大于min_score，而且顺序是降序
        assert resp.status_code == 200        
        assert resp.json_get("results")
        results=resp.json_get("results")
        score_list=[]
        for result in results:
            result_score=result["score"]
            score_list.append(result_score)
            assert result_score>=min_score#结果分数必须大于min_score
        #score_list必定是降序排序
        for i in range((len(score_list)-1)):
            assert score_list[i]>=score_list[i+1]
        
    def test_api_FaceService_SearchPerson_04(self, config_obj, FaceApi,test_tag_search_person,db_operation):
        """人员搜索单接口_验证复杂情况下的检索正确性_设置分数过滤和标签过滤"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []
        tag_ids_all = []

        #step2入库两组人员，a1,b1
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
        a_image1=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        images = [a_image1]
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_names = ["t1","t2","t3","t4","t5","t6"]
        tag_ids=FaceApi.transfromNameToId(tag_names,tag_name_id)
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #第二组
        person_id = "b"
        b_image1=FaceApi.idsImageToBase64(f"face1vn/search_person/b_image1.jpg")
        images = [b_image1]
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_names = ["t1","t2","t3"]
        tag_ids=FaceApi.transfromNameToId(tag_names,tag_name_id)
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)        
        person_ids.append(person_id)
        #第三组
        person_id = "c"
        c_image1=a_image1
        images = [c_image1]
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_names = ["t4","t5","t6"]
        tag_ids=FaceApi.transfromNameToId(tag_names,tag_name_id)
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)        
        person_ids.append(person_id)
        #打印出不过滤的搜素结果
        time.sleep(3)
        image_query = a_image1
        top_k = 10
        min_score = 0
        auto_rotate = None
        min_quality_level = None
        detect_liveness = None
        with_detail = None
        resp_test = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=None, with_detail=with_detail)
        #step3检索
         
        image_query = a_image1
        top_k = 10
        min_score = 0.90#和用例2的区别在于score不为0，除去标签的过滤，还有分数的过滤
        auto_rotate = None
        min_quality_level = None
        detect_liveness = None
        tag_ids =FaceApi.transfromNameToId(test_tag_search_person,tag_name_id)      
        with_detail = None
        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        # 清理-删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        # 清理-删除标签    
        for id in tag_ids_all:
            FaceApi.FaceService_DeleteTagPostApi(db_id=db_id, tag_id=id)       
        #校验逻辑
        assert resp.status_code == 200        
        #和用例2的区别在于score不为0，除去标签的过滤，还有分数的过滤，为了突出分数的过滤，其中入库的图片设置的不一致
        #为此结果标签和分数过滤，写预期。
        #有搜索结果的情况["t1"],["t1","t2"],["t2","t1"],["t1","t2","t3"],["t4","t5","t6"],["t1","t2","t3","t4","t5","t6"]
        #相比用例2,加入分数过滤，["t1"],["t1","t2"],["t2","t1"],["t1","t2","t3"]仅会命中a,不会命中b
        #无搜索结果的情况[],["t6","t7"],["t7","t8"]，此次预期是无符合条件的搜索，即result=[]
        if "t7" in test_tag_search_person:#["t6","t7"],["t7","t8"]
            assert resp.resp_json=={}
        else:
            results=resp.json_get("results")
            person_ids=[]
            for result in results:
                person_ids.append(result["person"]["person_id"])
            if test_tag_search_person==["t1","t2","t3","t4","t5","t6"]:
                assert len(results)==1
                assert "a" in person_ids
            elif test_tag_search_person==["t4","t5","t6"]:
                assert len(results)==2
                assert "a" in person_ids
                assert "c" in person_ids
            elif "t1" in test_tag_search_person:#["t1"],["t1","t2"],["t2","t1"],["t1","t2","t3"]
                assert len(results)==1
                assert "a" in person_ids
            elif test_tag_search_person==[]:
                assert len(results)==2
                assert "a" in person_ids
                assert "c" in person_ids
        
    def test_api_FaceService_SearchPerson_05(self, config_obj, FaceApi,test_topk,db_operation):
        """人员搜索单接口_验证topk参数的有效性"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []

        #step2入库两组人员，a1,b1
        #第一组
        person_id = "a"
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        images = [image]
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_ids = None
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #第二组
        person_id = "b"
        extra_info = None
        auto_rotate = None
        min_quality_level = None
        tag_ids = None
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)        
        person_ids.append(person_id)
        #step3检索
        time.sleep(3)
        image_query = image
        min_score = 0
        auto_rotate = None
        min_quality_level = None
        detect_liveness = None
        tag_ids = None
        with_detail = None
        resp= FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=test_topk, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)      
        #校验逻辑,topk=1的时候只有1返回
        assert resp.status_code == 200        
        assert resp.json_get("results")
        results=resp.json_get("results")
        assert len(results)==test_topk
        
    def test_api_FaceService_SearchPerson_06(self, config_obj, FaceApi,testImage_rotate,db_operation):
        """人员搜索单接口_验证自动旋转的有效性"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []

        #step2入库两组人员，a1,b1
        #第一组
        person_id = "a"
        image=FaceApi.idsImageToBase64(testImage_rotate.base_image)
        images = [image]
        extra_info = None
        auto_rotate = True
        min_quality_level = None
        tag_ids = None
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        
        #step3检索1-不开启自动旋转
         
        image_query = FaceApi.idsImageToBase64(testImage_rotate.image)
        min_score = 0
        top_k = 10
        auto_rotate = False
        min_quality_level = None
        detect_liveness = None
        tag_ids = None
        with_detail = None
        resp1 = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        
        #step3检索2-开启自动旋转
        time.sleep(3)
        image_query = FaceApi.idsImageToBase64(testImage_rotate.image)
        min_score = 0
        auto_rotate = True
        min_quality_level = None
        detect_liveness = None
        tag_ids = None
        with_detail = None
        resp2 = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)        
        #校验逻辑
        #不开启旋转的，返回失败
        assert resp1.status_code != 200   
        assert resp1.json_get("error")     
        error=resp1.json_get("error")
        assert "no face" in error["message"]
        #开启旋转，返回成功
        assert resp2.status_code == 200        
        assert resp2.json_get("results")
        results2=resp2.json_get("results")
        assert results2[0]["person"]["person_id"]=="a"
        

    def test_api_FaceService_SearchPerson_07(self, config_obj, FaceApi,db_operation):
        """人员搜索单接口_检测活体的有效性"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []

        #step2入库两组人员，a1,b1
        #第一组
        person_id = "a"
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/liveness.jpg")
        images = [image]
        extra_info = None
        auto_rotate = True
        min_quality_level = None
        tag_ids = None
        top_k=10
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #step3检索1-使用非活体
        time.sleep(3)
        image_query = FaceApi.idsImageToBase64(f"face1vn/search_person/not_liveness.png")
        min_score = 0
        auto_rotate = None
        min_quality_level = None
        detect_liveness = True
        tag_ids = None
        with_detail = None
        resp1 = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        #step3检索1-使用活体
        image_query = FaceApi.idsImageToBase64(f"face1vn/search_person/liveness.jpg")
        min_score = 0
        auto_rotate = None
        min_quality_level = None
        detect_liveness = True
        tag_ids = None
        with_detail = None
        resp2 = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=top_k, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        #校验逻辑

        #resp1返回不过，resp2返回正常
        assert resp1.status_code!= 200        
        assert resp2.status_code == 200        
        results2=resp2.json_get("results")
        assert len(results2)==1
        
        

    def test_api_FaceService_SearchPerson_08(self, config_obj, FaceApi,testImages_badQuality,db_operation):
        """人员搜索单接口_质量过滤的有效性"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []

        #step2入库两组人员，a1,b1
        #第一组
        person_id = "a"
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        images = [image]
        extra_info = None
        auto_rotate = True
        min_quality_level = None
        tag_ids = None
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #step3检索-使用低质量图片
        time.sleep(3)
        image_query = FaceApi.idsImageToBase64(testImages_badQuality.base_image)
        min_score = 0
        auto_rotate = None
        min_quality_level = "HIGH"   
        detect_liveness = None
        tag_ids = None
        with_detail = None
        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=1, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        #校验逻辑
        assert resp.status_code != 200
        assert resp.json_get("error")     
        error=resp.json_get("error")
        assert "low quality face" in error["message"]


    def test_api_FaceService_SearchPerson_09(self, config_obj, FaceApi,testImages_badQuality,db_operation):
        """人员搜索单接口_with_detail的有效性"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []
        #step2入库两组人员，a1,b1
        #第一组
        person_id = "a"
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        images = [image]
        extra_info = f"i am a student"
        auto_rotate = True
        min_quality_level = None
        tag_ids = None
        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #step3检索-使用低质量图片
        time.sleep(3)
        image_query = FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        min_score = 0
        auto_rotate = None
        min_quality_level = None 
        detect_liveness = None
        tag_ids = None
        with_detail = True
        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=image_query, top_k=1, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail)
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        #校验逻辑
        assert resp.status_code == 200   
        assert resp.json_get("results")    
        results=resp.json_get("results")    
        assert results[0]["person"]["extra_info"]
        assert results[0]["person"]["created_at"]
        # assert results[0]["person"]["updated_at"]



    def test_api_FaceService_SearchPerson_10(self, config_obj, FaceApi,user_info,db_operation):
        """人员搜索单接口_验证AES_CBC加密"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []
        #step2入库两组人员，a1,b1
        #第一组
        person_id = "a"
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        images = [image]
        extra_info = f"i am a student"
        auto_rotate = True
        min_quality_level = None
        tag_ids = None

        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #step3检索-使用低质量图片
        time.sleep(3)
        min_score = 0
        auto_rotate = None
        min_quality_level = None 
        detect_liveness = None
        tag_ids = None
        with_detail = True

        cryptor = AESCipher(user_info.sk)
        jstr = {"image": FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")}
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields":  ["image"],
            "data": cypher
        }
        

        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=None, top_k=1, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail,encrypt_info=encrypt_info)
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        #校验逻辑
        assert resp.status_code == 200   
        assert resp.json_get("results")    
        results=resp.json_get("results")    
        assert results[0]["score"]

    def test_api_FaceService_SearchPerson_11(self, config_obj, FaceApi,user_info,db_operation):
        """人员搜索单接口_验证AES_GCM加密"""
        #step1创建库
        # db_id=FaceApi.newDB()
        db_id = db_operation[0]
        person_ids = []
        #step2入库两组人员，a1,b1
        #第一组
        person_id = "a"
        image=FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")
        images = [image]
        extra_info = f"i am a student"
        auto_rotate = True
        min_quality_level = None
        tag_ids = None

        encrypt_info = None
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, extra_info=extra_info, auto_rotate=auto_rotate, min_quality_level=min_quality_level, tag_ids=tag_ids, encrypt_info=encrypt_info)
        person_ids.append(person_id)
        #step3检索-使用低质量图片
        time.sleep(3)
        min_score = 0
        auto_rotate = None
        min_quality_level = None 
        detect_liveness = None
        tag_ids = None
        with_detail = True

        cryptor = AESGCMCryptor(user_info.sk)
        jstr = {"image": FaceApi.idsImageToBase64(f"face1vn/search_person/a_image1.jpg")}
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields":  ["image"],
            "data": cypher
        }
        

        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=None, top_k=1, min_score=min_score, auto_rotate=auto_rotate, min_quality_level=min_quality_level, detect_liveness=detect_liveness, tag_ids=tag_ids, with_detail=with_detail,encrypt_info=encrypt_info)
        # 删除人员
        for id in person_ids:
            FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=id)   
        #校验逻辑
        assert resp.status_code == 200   
        assert resp.json_get("results")    
        results=resp.json_get("results")    
        assert results[0]["score"]


if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])