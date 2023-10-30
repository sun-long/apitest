#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
import time
from commonlib import config, time_utils, sign_utils, utils
from commonlib.log_utils import log
from commonlib.api_lib.AES_new import *
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
@pytest.mark.Regression
class TestFace1vnPersonMgtScenario(object):
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
    def test_scenario_add_person_with_required_params(self, config_obj, FaceApi, db_operation):
        """ 验证添加人员仅必填参数"""
        
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, auto_rotate=True)
        assert resp.status_code == 200
        face_id = resp.json_get("results.0.face_id")
        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        assert resp.json_get("face_infos.0.face_id") == face_id
        time.sleep(3)
        query_image = FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.png")
        top_k = 1
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=query_image, top_k=top_k,encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("results.0.person.person_id") == person_id

    @pytest.mark.P0
    def test_scenario_add_person_with_all_params_minimal(self, config_obj, FaceApi, db_operation):
        """ 验证添加人员所有参数最小值_1张图片_1个标签"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.png"))
        extra_info = "备注信息"
        auto_rotate = False
        min_quality_level = "NORMAL"
        tag_ids = db_operation[1]
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images,
                                                    extra_info=extra_info, auto_rotate=auto_rotate,
                                                    min_quality_level=min_quality_level, tag_ids=tag_ids,
                                                    encrypt_info=encrypt_info)
        assert resp.status_code == 200
        face_id = resp.json_get("results.0.face_id")
        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        assert resp.json_get("person.extra_info") == extra_info
        assert resp.json_get("face_infos.0.face_id") == face_id

    @pytest.mark.P0
    def test_scenario_add_person_with_all_params(self, config_obj, FaceApi, db_operation):
        """ 验证添加人员所有参数最大值_5张图片PNG、JPG、JPEG、BMP_1个标签"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.png"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.jpeg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_03.bmp"))
        # 一个汉字三个字节算
        extra_info = 10 * "备注信息字符最大" + 16 * "a"
        # extra_info = 257*"a"
        auto_rotate = False
        min_quality_level = "QUALITY_LEVEL_NONE"
        tag_ids = db_operation[1]
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images,
                                                    extra_info=extra_info, auto_rotate=auto_rotate,
                                                    min_quality_level=min_quality_level, tag_ids=tag_ids,
                                                    encrypt_info=encrypt_info)
        assert resp.status_code == 200
        face_ids = []
        for i in range(len(resp.json_get("results"))):
            face_ids.append(resp.json_get(f"results.{i}.face_id"))

        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        assert resp.json_get("person.extra_info") == extra_info
        for i in range(len(resp.json_get("face_infos"))):
            assert resp.json_get(f"face_infos.{i}.face_id") == face_ids[i]
        for j in range(len(resp.json_get("tags"))):
            assert resp.json_get(f"tags.{j}.id") == db_operation[1][j]

    @pytest.mark.P0
    # 2.28pass
    def test_scenario_add_person_encrypt(self, config_obj, FaceApi, db_operation, user_info):
        """ 验证添加人员图片加密"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/single_face_0.jpeg"))

        jstr = {
            "images": images,
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["images"],
            "data": cypher
        }
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        face_id = resp.json_get("results.0.face_id")

        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        assert resp.json_get("face_infos.0.face_id") == face_id

        image = []
        image.append(FaceApi.idsImageToBase64("face1vn/single_face_180.jpeg"))
        image.append(FaceApi.idsImageToBase64("face1vn/single_face_270.jpeg"))
        image.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        image.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.jpg"))
        for i in range(len(image)):
            # print(i)
            jstr = {
                "image": image[i],
            }
            cryptor = AESCipher(user_info.sk)
            cypher = cryptor.encrypt(json.dumps(jstr))
            encrypt_info = {
                "algorithm": "AES_256_CBC",
                "version": 0,
                "encrypted_fields": ["image"],
                "data": cypher
            }
            res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=None,
                                                           auto_rotate=True,
                                                           min_quality_level=None, encrypt_info=encrypt_info)

            assert res.status_code == 200
        # 调用查询接口确认可以查询到结果,此时应该只有5张图片
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        assert len(resp.json_get("face_infos")) == 5

        # 再添加一张应该会报错
        res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=image[0],
                                                       auto_rotate=True,
                                                       min_quality_level=None, encrypt_info=None)

        assert res.status_code == 400
        assert res.json_get("error.message") == "E12003058: the person's image limit has been exceeded"
        res.json_get("error.details.0.metadata") == {'exists': '5', 'limit': '5'}

        # 删除一张后
        res = FaceApi.FaceService_DeletePersonFacePostApi(db_id=db_id, person_id=person_id, face_id=face_id)
        assert res.status_code == 200
        assert res

        # 判断剩余是不是4
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert len(resp.json_get("face_infos")) == 4

    @pytest.mark.P0
    # 2.28pass
    def test_scenario_add_person_encrypt_1(self, config_obj, FaceApi, db_operation, user_info):
        """ 验证添加人员图片GCM加密"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/single_face_0.jpeg"))

        jstr = {
            "images": images,
        }
        cryptor = AESGCMCryptor(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": ["images"],
            "data": cypher
        }
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        face_id = resp.json_get("results.0.face_id")

        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        assert resp.json_get("face_infos.0.face_id") == face_id

        image = []
        image.append(FaceApi.idsImageToBase64("face1vn/single_face_180.jpeg"))
        image.append(FaceApi.idsImageToBase64("face1vn/single_face_270.jpeg"))
        image.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        image.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.jpg"))
        for i in range(len(image)):
            # print(i)
            jstr = {
                "image": image[i],
            }
            cryptor = AESCipher(user_info.sk)
            cypher = cryptor.encrypt(json.dumps(jstr))
            encrypt_info = {
                "algorithm": "AES_256_CBC",
                "version": 0,
                "encrypted_fields": ["image"],
                "data": cypher
            }
            res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=None,
                                                           auto_rotate=True,
                                                           min_quality_level=None, encrypt_info=encrypt_info)

            assert res.status_code == 200
        # 调用查询接口确认可以查询到结果,此时应该只有5张图片
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        assert len(resp.json_get("face_infos")) == 5

        # 再添加一张应该会报错
        res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=image[0],
                                                       auto_rotate=True,
                                                       min_quality_level=None, encrypt_info=None)

        assert res.status_code == 400
        assert res.json_get("error.message") == "E12003058: the person's image limit has been exceeded"
        res.json_get("error.details.0.metadata") == {'exists': '5', 'limit': '5'}

        # 删除一张后
        res = FaceApi.FaceService_DeletePersonFacePostApi(db_id=db_id, person_id=person_id, face_id=face_id)
        assert res.status_code == 200
        assert res

        # 判断剩余是不是4
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert len(resp.json_get("face_infos")) == 4

    @pytest.mark.P0
    # 2.28pass
    def test_scenario_add_person_face_no_encrypt(self, config_obj, FaceApi, db_operation, user_info):
        """ 验证添加人员图片加密liangchen"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/single_face_0.jpeg"))

        jstr = {
            "images": images,
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["images"],
            "data": cypher
        }

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200

        # 调用查询接口确认可以查询到结果,此时应该只有一张图片
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        face_id = resp.json_get("face_infos.0.face_id")

        image = []
        image.append(FaceApi.idsImageToBase64("face1v1/is_liveness_high_01.jpg"))
        image.append(FaceApi.idsImageToBase64("face1v1/is_liveness_high_02.jpg"))
        image.append(FaceApi.idsImageToBase64("face1v1/is_liveness_low_01.jpg"))
        image.append(FaceApi.idsImageToBase64("face1v1/is_liveness_low_02.jpg"))
        i = 1
        for i in range(len(image)):
            # 调用添加人脸图片接口，再继续添加四张
            images = image[i]
            # images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.png"))
            # 不加密的情况
            res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=images,
                                                           auto_rotate=True, min_quality_level="QUALITY_LEVEL_NONE",
                                                           encrypt_info=None)
            assert res.status_code == 200
        # 调用查询接口确认可以查询到结果,此时应该只有5张图片
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        # 再添加一张应该会报错
        res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=images, auto_rotate=None,
                                                       min_quality_level=None, encrypt_info=None)

        assert res.status_code == 400
        assert res.json_get("error.message") == "E12003058: the person's image limit has been exceeded"
        res.json_get("error.details.0.metadata") == {'exists': '5', 'limit': '5'}

        # 删除一张后
        res = FaceApi.FaceService_DeletePersonFacePostApi(db_id=db_id, person_id=person_id, face_id=face_id)
        assert res.status_code == 200
        assert res

        # 判断剩余是不是4
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert len(resp.json_get("face_infos")) == 4


    @pytest.mark.P0
    # 2.28pass
    def test_scenario_add_person_face_no_encrypt(self, config_obj, FaceApi, db_operation, user_info):
        """ 验证添加人员图片GCM加密liangchen"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/single_face_0.jpeg"))

        jstr = {
            "images": images,
        }
        cryptor = AESGCMCryptor(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": ["images"],
            "data": cypher
        }

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200

        # 调用查询接口确认可以查询到结果,此时应该只有一张图片
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        face_id = resp.json_get("face_infos.0.face_id")

        image = []
        image.append(FaceApi.idsImageToBase64("face1v1/is_liveness_high_01.jpg"))
        image.append(FaceApi.idsImageToBase64("face1v1/is_liveness_high_02.jpg"))
        image.append(FaceApi.idsImageToBase64("face1v1/is_liveness_low_01.jpg"))
        image.append(FaceApi.idsImageToBase64("face1v1/is_liveness_low_02.jpg"))
        i = 1
        for i in range(len(image)):
            # 调用添加人脸图片接口，再继续添加四张
            images = image[i]
            # images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.png"))
            # 不加密的情况
            res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=images,
                                                           auto_rotate=True, min_quality_level="QUALITY_LEVEL_NONE",
                                                           encrypt_info=None)
            assert res.status_code == 200
        # 调用查询接口确认可以查询到结果,此时应该只有5张图片
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        # 再添加一张应该会报错
        res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=images, auto_rotate=None,
                                                       min_quality_level=None, encrypt_info=None)

        assert res.status_code == 400
        assert res.json_get("error.message") == "E12003058: the person's image limit has been exceeded"
        res.json_get("error.details.0.metadata") == {'exists': '5', 'limit': '5'}

        # 删除一张后
        res = FaceApi.FaceService_DeletePersonFacePostApi(db_id=db_id, person_id=person_id, face_id=face_id)
        assert res.status_code == 200
        assert res

        # 判断剩余是不是4
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert len(resp.json_get("face_infos")) == 4



    @pytest.mark.P0
    # 2.28pass
    def test_scenario_add_person_face_rotate(self, config_obj, FaceApi, db_operation, user_info):
        """ 验证添加人员旋转功能,旋转后能提取特征成功"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/single_face_180.jpeg"))

        jstr = {
            "images": images,
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["images"],
            "data": cypher
        }

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, auto_rotate=True,
                                                    encrypt_info=encrypt_info)
        assert resp.status_code == 200

        image = []
        image.append(FaceApi.idsImageToBase64("face1vn/single_face_0.jpeg"))
        jstr = {
            "image": image[0],
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["image"],
            "data": cypher
        }
        res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=None, auto_rotate=True,
                                                       min_quality_level=None, encrypt_info=encrypt_info)
        assert res.status_code == 200

        time.sleep(3)
        query_image = FaceApi.idsImageToBase64("face1vn/single_face_0.jpeg")
        # 这块虽然是topk=2，但是是按人返回的，因此results的长度只有1
        top_k = 2
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_SearchPersonPostApi(db_id=db_id, image=query_image, top_k=top_k,encrypt_info=encrypt_info)
        assert resp.status_code == 200

    @pytest.mark.P0
    # 2.28pass
    def test_scenario_add_person_face_min_quality_level(self, config_obj, FaceApi, db_operation, user_info):
        """人脸质量控制等级参数校验"""
        # 添加人
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/single_face_0.jpeg"))
        jstr = {
            "images": images,
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["images"],
            "data": cypher
        }

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, auto_rotate=True,
                                                    encrypt_info=encrypt_info)
        assert resp.status_code == 200

        # 添加图片，传一张黑色的图，应该报错
        image = []
        image.append(FaceApi.idsImageToBase64("face1vn/black.png"))
        jstr = {
            "image": image[0],
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["image"],
            "data": cypher
        }
        min_quality_level = ["QUALITY_LEVEL_NONE", "NORMAL", "HIGH"]
        for i in min_quality_level:
            res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=None,
                                                           auto_rotate=True,
                                                           min_quality_level=i, encrypt_info=encrypt_info)
            assert res.status_code == 400
            assert res.json_get("error.details.0.message") == 'no face detected'

    @pytest.mark.P0
    # 2.28pass
    def test_scenario_add_person_face_image_oversize(self, config_obj, FaceApi, db_operation, user_info):
        """人库图片大小超过阈值参数校验"""
        # 添加人
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/single_face_0.jpeg"))
        jstr = {
            "images": images,
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["images"],
            "data": cypher
        }

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, auto_rotate=True,
                                                    encrypt_info=encrypt_info)
        assert resp.status_code == 200

        # 添加图片，传一张黑色的图，应该报错
        image = []
        image.append(FaceApi.idsImageToBase64("face1v1/single_face_01_2560_1441_15MB.png"))
        jstr = {
            "image": image[0],
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["image"],
            "data": cypher
        }

        res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=None, auto_rotate=True,
                                                       min_quality_level="QUALITY_LEVEL_NONE",
                                                       encrypt_info=encrypt_info)
        assert res.status_code == 400
        assert res.json_get("error.details.0.message") == 'image size is exceeded'

    @pytest.mark.P0
    # 2.28pass
    def test_scenario_add_person_face_duplicated_picture(self, config_obj, FaceApi, db_operation, user_info):
        """ 验证添加人员图片加密liangchen"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.png"))

        jstr = {
            "images": images,
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": ["images"],
            "data": cypher
        }

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, encrypt_info=encrypt_info)
        assert resp.status_code == 200

        # 调用查询接口确认可以查询到结果,此时应该只有一张图片
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        face_id = resp.json_get("face_infos.0.face_id")

        # 重复添加同一张图片，应该报错
        res = FaceApi.FaceService_AddPersonFacePostApi(db_id=db_id, person_id=person_id, image=images[0],
                                                       auto_rotate=None, min_quality_level=None, encrypt_info=None)
        assert res.status_code != 200
        assert res.json_get("error.details.0.message") == "image duplicated"

        # 调用查询接口确认可以查询到结果,此时应该只有1张图片,第二张图片没入进去
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        assert len(resp.json_get("face_infos")) == 1

    @pytest.mark.P1
    def test_scenario_add_person_mutiface_image(self, config_obj, FaceApi, db_operation):
        """ 验证不允许添加多人脸照片"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_multi_faces.jpg"))
        min_quality_level = "NORMAL"
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images,
                                                    min_quality_level=min_quality_level)
        assert resp.status_code == 200
        assert resp.json_get("results.0.error.code") == 3
        assert resp.json_get("results.0.error.details.0.message") == "multiple faces detected"
        assert resp.json_get("results.0.error.details.0.reason") == 12003021
        assert resp.json_get("results.0.error.message") == "E12003021: multiple faces detected"

    @pytest.mark.parametrize("invalidImageType", [
        "base_normal_zr_02_90.jpg",
        "base_normal_zr_02_180.jpg",
        "base_normal_zr_02_270.jpg"
    ])
    def test_scenario_add_person_rotate_image(self, config_obj, FaceApi, db_operation, invalidImageType):
        """ 验证添加人员带角度的图片自动旋转True"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64(f"face1vn/{invalidImageType}"))
        auto_rotate = True
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images,
                                                    auto_rotate=auto_rotate)
        assert resp.status_code == 200
        face_id = resp.json_get("results.0.face_id")
        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        assert resp.json_get("face_infos.0.face_id") == face_id

    @pytest.mark.parametrize("invalidImageType", [
        "base_normal_zr_02_90.jpg",
        "base_normal_zr_02_180.jpg",
        "base_normal_zr_02_270.jpg"
    ])
    def test_scenario_negative_add_person_rotated_invalid(self, config_obj, FaceApi, db_operation, invalidImageType):
        """ 验证添加人员未开启自动旋转False，图片90 180 270不允许入库"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64(f"face1vn/{invalidImageType}"))
        auto_rotate = False
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images,
                                                    auto_rotate=auto_rotate)
        assert resp.status_code == 200

    @pytest.mark.P1
    def test_scenario_negative_add_person_duplicate(self, config_obj, FaceApi, db_operation):
        """ 验证不允许添加重复人员"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 200
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 409
        assert resp.json_get("error.code") == 6
        assert resp.json_get("error.details.0.message") == "already exists in db"
        assert resp.json_get("error.details.0.reason") == 12006001
        assert resp.json_get("error.message") == "E12006001: already exists in db"

    @pytest.mark.P1
    @pytest.mark.parametrize("invalidImageType", [
        "base_unsupport_gif.gif",
        "base_unsupport_tif.tif",
        "base_unsupport_webp.webp"
    ])
    def test_scenario_negative_add_person_imagetype(self, config_obj, FaceApi, db_operation, invalidImageType):
        """ 验证添加人员不支持的图片格式例如gif,tif,webp"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64(f"face1vn/{invalidImageType}"))

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 200
        assert resp.json_get("results.0.error.code") == 3
        assert resp.json_get("results.0.error.details.0.message") == "invalid image"
        assert resp.json_get("results.0.error.details.0.reason") == 12003007
        assert resp.json_get("results.0.error.message") == "E12003007: invalid image"

    @pytest.mark.P1
    def test_scenario_negative_add_person_sizeover4M(self, config_obj, FaceApi, db_operation):
        """ 验证添加人员图片超出4MB"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1v1/single_face_01_2560_1441_15MB.png"))

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 200
        assert resp.json_get("results.0.error.code") == 3
        assert resp.json_get("results.0.error.details.0.message") == "image size is exceeded"
        assert resp.json_get("results.0.error.details.0.reason") == 12003005
        assert resp.json_get("results.0.error.message") == "E12003005: image size is exceeded"

    @pytest.mark.P1
    def test_scenario_negative_add_person_lowresolution(self, config_obj, FaceApi, db_operation):
        """ 验证添加人员图片分辨率太低"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_low_resolution.jpg"))

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 200
        assert resp.json_get("results.0.error.code") == 3
        assert resp.json_get("results.0.error.details.0.message") == "low image resolution"
        assert resp.json_get("results.0.error.details.0.reason") == 12003009
        assert resp.json_get("results.0.error.message") == "E12003009: low image resolution"

    @pytest.mark.P1
    def test_scenario_negative_add_person_siximages(self, config_obj, FaceApi, db_operation):
        """ 验证人员不允许添加6张图片"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "the person's image limit has been exceeded"
        assert resp.json_get("error.details.0.reason") == 12003058
        assert resp.json_get("error.message") == "E12003058: the person's image limit has been exceeded"

    @pytest.mark.P1
    def test_scenario_negative_add_person_noface_image(self, config_obj, FaceApi, db_operation):
        """ 验证不允许添加无人脸照片"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_noface.png"))

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 200
        assert resp.json_get("results.0.error.code") == 3
        assert resp.json_get("results.0.error.details.0.message") == "no face detected"
        assert resp.json_get("results.0.error.details.0.reason") == 12003020
        assert resp.json_get("results.0.error.message") == "E12003020: no face detected"

    @pytest.mark.skip(reason="不做强制限制标签个数")
    def test_scenario_negative_add_person_with_11tags(self, config_obj, FaceApi, db_operation):
        """ 验证添加人员11个标签可以成功"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_02.png"))
        tag_ids = db_operation[1]

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, tag_ids=tag_ids)
        assert resp.status_code == 200
        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id
        for j in range(len(resp.json_get("tags"))):
            assert resp.json_get(f"tags.{j}.id") == db_operation[1][j]

    @pytest.mark.P0
    @pytest.mark.parametrize("image_low", [
        # "is_liveness_low_02.jpg",
        #    "bad_quality_01.jpg",
        "base_mask.jpg",
        "base_too_light.png",
        #    "base_too_dark.jpg",
        # "base_occlusion_01.jpg",
        "base_sunglass.png",
        # "face_yaw_mask1.jpg",
    ])
    def test_scenario_negative_add_person_quality_high(self, config_obj, FaceApi, db_operation, image_low):
        """ 验证添加人员质量等级为high图片质量不合格，一种以上"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64(f"face1vn/{image_low}"))
        min_quality_level = "HIGH"
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images,
                                                    min_quality_level=min_quality_level)
        assert resp.status_code == 200
        assert resp.json_get(f"results.0.error.code") == 3
        assert resp.json_get(f"results.0.error.details.0.message") == "low quality face"
        assert resp.json_get(f"results.0.error.details.0.reason") == 12003022
        assert resp.json_get(f"results.0.error.message") == "E12003022: low quality face"

    @pytest.mark.P0
    @pytest.mark.parametrize("image_low", [
        # "base_mask.jpg",
        "base_mask_fuzzy.jpg",
    ])
    def test_scenario_negative_add_person_quality_normal(self, config_obj, FaceApi, db_operation, image_low):
        """ 验证添加人员质量等级为normal图片质量不合格，两种以上"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64(f"face1vn/{image_low}"))
        min_quality_level = "NORMAL"
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images,
                                                    min_quality_level=min_quality_level)
        assert resp.status_code == 200
        assert resp.json_get(f"results.0.error.code") == 3
        assert resp.json_get(f"results.0.error.details.0.message") == "low quality face"
        assert resp.json_get(f"results.0.error.details.0.reason") == 12003022
        assert resp.json_get(f"results.0.error.message") == "E12003022: low quality face"

    @pytest.mark.parametrize("image_low", [
        "base_mask_fuzzy.jpg",
    ])
    @pytest.mark.P1
    @pytest.mark.skip(reason="需求调整不支持low")
    def test_scenario_negative_add_person_quality_low(self, config_obj, FaceApi, db_operation, image_low):
        """ 验证添加人员质量等级为low图片质量不合格,三种以上"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64(f"face1vn/{image_low}"))
        min_quality_level = "LOW"
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images,
                                                    min_quality_level=min_quality_level)
        assert resp.status_code == 200
        assert resp.json_get(f"results.0.error.code") == 3
        assert resp.json_get(f"results.0.error.details.0.message") == "low quality face"
        assert resp.json_get(f"results.0.error.details.0.reason") == 12003022
        assert resp.json_get(f"results.0.error.message") == "E12003022: low quality face"

    @pytest.mark.P0
    def test_scenario_add_person_some_image_error(self, config_obj, FaceApi, db_operation):
        """ 验证添加人员5张图片中3张不合格,人员添加成功,返回异常图片"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_sizeover_2M.bmp"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_low_resolution.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_unsupport_gif.gif"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_noface.png"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))

        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 200
        assert resp.json_get("results.1.error.code") == 3
        assert resp.json_get("results.1.error.details.0.message") == "low image resolution"
        assert resp.json_get("results.1.error.details.0.reason") == 12003009
        assert resp.json_get("results.1.error.message") == "E12003009: low image resolution"

        assert resp.json_get("results.2.error.code") == 3
        assert resp.json_get("results.2.error.details.0.message") == "invalid image"
        assert resp.json_get("results.2.error.details.0.reason") == 12003007
        assert resp.json_get("results.2.error.message") == "E12003007: invalid image"

        assert resp.json_get("results.3.error.code") == 3
        assert resp.json_get("results.3.error.details.0.message") == "no face detected"
        assert resp.json_get("results.3.error.details.0.reason") == 12003020
        assert resp.json_get("results.3.error.message") == "E12003020: no face detected"

        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id

    @pytest.mark.skip("精度case,随着精度模型的变化有变化")
    @pytest.mark.P0
    def test_scenario_add_person_some_image_low_quality(self, config_obj, FaceApi, db_operation):
        """ 验证添加人员5张图片中4张质量低,人员添加成功,返回异常图片"""
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_mask.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_too_light.png"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_black_white.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_sizeover_2M.bmp"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_too_dark.jpg"))
        min_quality_level = "HIGH"
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images,
                                                    min_quality_level=min_quality_level)
        assert resp.status_code == 200
        for i in range(3):
            assert resp.json_get(f"results.{i}.error.code") == 3
            assert resp.json_get(f"results.{i}.error.details.0.message") == "low quality face"
            assert resp.json_get(f"results.{i}.error.details.0.reason") == 12003022
            assert resp.json_get(f"results.{i}.error.message") == "E12003022: low quality face"

            # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id

    @pytest.mark.P1
    def test_scenario_get_person_misdb_negative(self, config_obj, FaceApi, db_operation):
        """验证查询人员详情错误的db_id"""
        # 创建人员
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 200

        # 调用查询接口确认不可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id="11111", person_id=person_id)
        assert resp.status_code == 404
        assert resp.json_get("error.code") == 5
        assert resp.json_get("error.details.0.reason") == 12005002
        assert resp.json_get("error.message") == "E12005002: the person db is not found"

        # 查询不到结果
        # assert resp.json_get("person.person_id") == person_id

    @pytest.mark.P0
    def test_scenario_get_personlist(self, config_obj, FaceApi, db_operation):
        """ 查询人员列表 """
        db_id = db_operation[0]
        # 添加人员
        for i in range(10):
            person_id = "user_{}_{}".format(i, sign_utils.getUuid(5))
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            assert resp.status_code == 200

        page_offset = 0
        page_limit = 10
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) == 10

    @pytest.mark.P0
    def test_scenario_get_personlist_pages(self, config_obj, FaceApi, db_operation):
        """ 查询人员列表,翻页 """
        db_id = db_operation[0]
        # 添加人员
        for i in range(10):
            person_id = "user_{}_{}".format(i, sign_utils.getUuid(5))
            images = []
            images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
            resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
            assert resp.status_code == 200

        page_offset = 0
        page_limit = 5
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) == 5

        page_offset = 5
        page_limit = 5
        resp = FaceApi.FaceService_ListPersonGetApi(db_id=db_id, page_offset=page_offset, page_limit=page_limit)
        assert resp.status_code == 200
        assert len(resp.json_get("persons")) == 5



    @pytest.mark.P0
    def test_scenario_del_person(self, config_obj, FaceApi, db_operation):
        """验证删除人员正向用例"""
        # 创建人员
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 200

        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id

        # 删除人员
        resp = FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200

        # 调用查询接口确认查询不到
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 404
        assert resp.json_get("error.code") == 5
        assert resp.json_get("error.details.0.message") == "the record is not found in db"
        assert resp.json_get("error.details.0.reason") == 12005001
        assert resp.json_get("error.message") == "E12005001: the record is not found in db"
        # assert resp.json_get("person.person_id") == person_id

    @pytest.mark.P1
    def test_scenario_del_twice_person(self, config_obj, FaceApi, db_operation):
        """验证重复删除人员"""
        # 创建人员
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 200

        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id

        # 第一次删除人员
        resp = FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200

        # 调用查询接口确认查询不到
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 404
        assert resp.json_get("error.code") == 5
        assert resp.json_get("error.details.0.message") == "the record is not found in db"
        assert resp.json_get("error.details.0.reason") == 12005001
        assert resp.json_get("error.message") == "E12005001: the record is not found in db"
        # assert resp.json_get("person.person_id") == person_id

        # 第二次删除人员
        resp = FaceApi.FaceService_DeletePersonPostApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 404
        assert resp.json_get("error.code") == 5
        assert resp.json_get("error.details.0.message") == "the record is not found in db"
        assert resp.json_get("error.details.0.reason") == 12005001
        assert resp.json_get("error.message") == "E12005001: the record is not found in db"

    @pytest.mark.P1
    def test_scenario_del_person_misdb_negative(self, config_obj, FaceApi, db_operation):
        """验证删除人员错误的db_id"""
        # 创建人员
        db_id = db_operation[0]
        person_id = "autotest" + sign_utils.getUuid(5)
        images = []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images)
        assert resp.status_code == 200

        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id

        # 删除人员
        resp = FaceApi.FaceService_DeletePersonPostApi(db_id="11111", person_id=person_id)
        assert resp.status_code == 404
        assert resp.json_get("error.code") == 5
        # assert resp.json_get("error.details.0.message") == the person db is not found"
        assert resp.json_get("error.details.0.reason") == 12005002
        assert resp.json_get("error.message") == "E12005002: the person db is not found"

        # 调用查询接口确认人员没有被删除
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id


    @pytest.mark.P0
    def test_scenario_add_person_with_same_images(self, config_obj, FaceApi,db_operation):
        """ 验证添加人员2张一样的图片"""
        db_id = db_operation[0]
        person_id = "autotest"+sign_utils.getUuid(5)
        images= []
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))
        images.append(FaceApi.idsImageToBase64("face1vn/base_normal_zr_01.jpg"))

        auto_rotate = False
        min_quality_level = "QUALITY_LEVEL_NONE"
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_AddPersonPostApi(db_id=db_id, person_id=person_id, images=images, auto_rotate=auto_rotate, min_quality_level=min_quality_level, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get(f"results.1.error.code") == 6
        assert resp.json_get(f"results.1.error.details.0.message") == "image duplicated"
        assert resp.json_get(f"results.1.error.details.0.reason") == 12006003

        # 调用查询接口确认可以查询到结果
        resp = FaceApi.FaceService_GetPersonGetApi(db_id=db_id, person_id=person_id)
        assert resp.status_code == 200
        assert resp.json_get("person.person_id") == person_id 

