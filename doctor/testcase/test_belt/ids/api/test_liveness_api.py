#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config
from commonlib.api_lib.AES_new import *
from commonlib.log_utils import log
from commonlib.api_lib.aes_crypto_gcm import  AESGCMCryptor
@pytest.mark.P0
@pytest.mark.Regression
class TestFaceLivenessApi(object):
    """ face Liveness Api测试"""

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

    @pytest.mark.parametrize("Parameters",[
        ('min_quality_level', 'QUALITY_LEVEL_NONE'),
        ('min_quality_level', 'LOW'),
        ('min_quality_level', 'NORMAL'),
        ('min_quality_level', 'HIGH'),
      #  ('min_quality_level', 'EXTREMELY_HIGH'),
    ])
    def test_api_Liveness_normal(self, Parameters, config_obj, FaceApi):
        """  提供图片静默活体检测-正常人脸. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q1.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = True
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 5,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        intef = FaceApi.FaceService_DetectLivenessPostApi(
            image=image, min_quality_level=min_quality_level, disable_defake=disable_defake, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(Parameters[0], Parameters[1])
        resp = intef.request()
        
        assert resp.status_code == 200
        assert resp.resp_json['liveness_score'] > 0.9
        
        
    def test_api_Liveness_CreateEncrypt_face(self, config_obj, user_info, FaceApi):
        """  提供图片静默活体检测-加密. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q1.jpg")
        jstr = {
            "image":FaceApi.imageToBase64(image_path),
            "min_quality_level":"LOW",
            "disable_defake":False
        }
        cryptor = AESCipher(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_CBC",
            "version": 0,
            "encrypted_fields": [
                "image","min_quality_level","disable_defake"
            ],
            "data": cypher
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.resp_json['liveness_score'] > 0.9 

    def test_api_Liveness_CreateEncrypt_face_GCM(self, config_obj, user_info, FaceApi):
        """  提供图片静默活体检测-GCM加密. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q1.jpg")
        jstr = {
            "image":FaceApi.imageToBase64(image_path),
            "min_quality_level":"LOW",
            "disable_defake":False
        }
        cryptor = AESGCMCryptor(user_info.sk)
        cypher = cryptor.encrypt(json.dumps(jstr))
        encrypt_info = {
            "algorithm": "AES_256_GCM",
            "version": 0,
            "encrypted_fields": [
                "image","min_quality_level","disable_defake"
            ],
            "data": cypher
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.resp_json['liveness_score'] > 0.9

    def test_api_Liveness_Multiple_faces(self, config_obj, FaceApi):
        """  提供图片静默活体检测-多张人脸. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/mul.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "LOW"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "multiple faces detected"
        assert resp.json_get("error.details.0.reason") == 12003021
        assert resp.json_get("error.message") == "E12003021: multiple faces detected"     
        
    @pytest.mark.parametrize("Parameters",[
        ('min_quality_level', 'QUALITY_LEVEL_NONE'),
        ('min_quality_level', 'LOW'),
  #      ('min_quality_level', 'NORMAL'),
 #       ('min_quality_level', 'HIGH'),
 #       ('min_quality_level', 'EXTREMELY_HIGH'),
    ])
    def test_api_Liveness_low_quality_face(self, Parameters,config_obj, FaceApi):
        """  提供图片静默活体检测-低质量人脸. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q18.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = True
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        intef = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info, sendRequest=False)
        intef.update_body(Parameters[0], Parameters[1])
        resp = intef.request()
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") < 0.9

    def test_api_Liveness_black_and_white_face(self, config_obj, FaceApi):
        """  提供图片静默活体检测-黑白照片. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q20.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "LOW"
        disable_defake = True
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        quality_items=resp.json_get("quality_items") 
        for quality_item in quality_items:
            assert quality_item["quality_type"]

    def test_api_Liveness_Face_maskings1(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸遮挡-鼻子. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q8.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = True
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "low quality face"
        assert resp.json_get("error.details.0.reason") == 12003022
        assert resp.json_get("error.message") == "E12003022: low quality face"
        
    @pytest.mark.skip("精度case,随着精度模型的变化有变化")
    def test_api_Liveness_Face_maskings2(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸遮挡-左脸颊. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q3.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") > 0.9
        

    def test_api_Liveness_Face_maskings3(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸遮挡-右脸颊. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q2.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = None
        disable_defake = True
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") > 0.9

    def test_api_Liveness_Face_maskings4(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸遮挡-眼睛. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q4.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = None
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") > 0.9

    def test_api_Liveness_Face_maskings5(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸遮挡-眉毛. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q5.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") > 0.9
        

    def test_api_Liveness_Face_maskings6(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸遮挡-下巴. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q6.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "low quality face"
        assert resp.json_get("error.details.0.reason") == 12003022
        assert resp.json_get("error.message") == "E12003022: low quality face"
        

    def test_api_Liveness_Face_maskings7(self, config_obj, FaceApi):
        """  提供图片静默活体检测-口罩遮挡. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q11.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "low quality face"
        assert resp.json_get("error.details.0.reason") == 12003022
        assert resp.json_get("error.message") == "E12003022: low quality face"
        

    def test_api_Liveness_Face_maskings8(self, config_obj, FaceApi):
        """  提供图片静默活体检测-眼镜遮挡. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q11.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "low quality face"
        assert resp.json_get("error.details.0.reason") == 12003022
        assert resp.json_get("error.message") == "E12003022: low quality face"
        
    def test_api_Liveness_Face_maskings9(self, config_obj, FaceApi):
        """  提供图片静默活体检测-额头遮挡. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q11.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "low quality face"
        assert resp.json_get("error.details.0.reason") == 12003022
        assert resp.json_get("error.message") == "E12003022: low quality face"
        

    @pytest.mark.skip("精度case,随着精度模型的变化有变化")    
    def test_api_Liveness_Face_share1(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸占比-距离屏幕过近的人脸. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q11.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "NORMAL"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") < 0.5
        

    def test_api_Liveness_Face_share2(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸占比-距离屏幕过远的人脸. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q7.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") > 0.9
        

    @pytest.mark.skip("精度case,随着精度模型的变化有变化")
    def test_api_Liveness_Face_brightness1(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸亮度-强光下的人脸. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q9.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "low quality face"
        assert resp.json_get("error.details.0.reason") == 12003022
        assert resp.json_get("error.message") == "E12003022: low quality face"
        
    @pytest.mark.skip("精度case,随着精度模型的变化有变化")
    def test_api_Liveness_Face_brightness2(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸亮度-弱光下的人脸. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q15.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") > 0.9
        
    @pytest.mark.skip("精度case,随着精度模型的变化有变化")
    def test_api_Liveness_Face_angle1(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸角度-俯仰角度偏大的人脸. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q12.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "low quality face"
        assert resp.json_get("error.details.0.reason") == 12003022
        assert resp.json_get("error.message") == "E12003022: low quality face"
        
        

    def test_api_Liveness_Face_angle2(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸角度-左右转头角度过大的人脸. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q13.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "LOW"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") > 0.9
        

    def test_api_Liveness_not_Face_image(self, config_obj, FaceApi):
        """  提供图片静默活体检测-图片无人脸. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/5M.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "QUALITY_LEVEL_NONE"
        disable_defake = True
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no face detected"
        assert resp.json_get("error.details.0.reason") == 12003020
        assert resp.json_get("error.message") == "E12003020: no face detected"     
        

    def test_api_Liveness_Face_image_format1(self, config_obj, FaceApi):
        """  提供图片静默活体检测-图片格式 png. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q16_png.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") > 0.9
        

    def test_api_Liveness_Face_image_format2(self, config_obj, FaceApi):
        """  提供图片静默活体检测-图片格式 jpeg. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q16_jpeg.jpeg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") > 0.9

    def test_api_Liveness_Face_image_format3(self, config_obj, FaceApi):
        """  提供图片静默活体检测-图片格式 bmp. """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q1_bmp.bmp")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "LOW"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("liveness_score") > 0.85
        

    def test_api_Liveness_Dummy_face1(self, config_obj, FaceApi):
        """  提供图片静默活体检测-假人人脸(1:照片,2:屏幕翻拍,3:纸质面具，
        4:三维面具,5:三维头模,6:AI换脸,7:对抗攻击(如T型眼镜),8:其他). """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q24.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("defake_score") > 0.5
        
    @pytest.mark.skip("精度case,随着精度模型的变化有变化")
    def test_api_Liveness_Dummy_face2(self, config_obj, FaceApi):
        """  提供图片静默活体检测-假人人脸-5:三维头模 """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q14.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("defake_score") < 0.1
        

    def test_api_Liveness_Dummy_face3(self, config_obj, FaceApi):
        """  提供图片静默活体检测-假人人脸-2:屏幕翻拍 """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q17.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "LOW"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("defake_score") < 0.1
        

    def test_api_Liveness_Dummy_face4(self, config_obj, FaceApi):
        """  提供图片静默活体检测-假人人脸-三维面具 """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q21.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "LOW"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("defake_score") > 0.7
        

    def test_api_Liveness_Dummy_face5(self, config_obj, FaceApi):
        """  提供图片静默活体检测-假人人脸-AI换脸 """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q25.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = None
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("defake_score") > 0.98
        
    @pytest.mark.skip("精度case,随着精度模型的变化有变化")
    def test_api_Liveness_Dummy_face6(self, config_obj, FaceApi):
        """  提供图片静默活体检测-假人人脸-T形眼镜 """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q28.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "LOW"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "low quality face"
        

    def test_api_Liveness_Dummy_face7(self, config_obj, FaceApi):
        """  提供图片静默活体检测-假人人脸-纸质面具 """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q29.jpg")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "LOW"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 200
        assert resp.json_get("defake_score") 
        

    def test_api_Liveness_4M(self, config_obj, FaceApi):
        """  提供图片静默活体检测-人脸图超过4M """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q19.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "image size is exceeded"
        assert resp.json_get("error.details.0.reason") == 12003005
        assert resp.json_get("error.message") == "E12003005: image size is exceeded"     

    def test_api_Liveness_image_empty(self, config_obj, FaceApi):
        """  提供图片静默活体检测-图片为空 """
        image = ''
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "image data is empty"
        assert resp.json_get("error.details.0.reason") == 12003006
        assert resp.json_get("error.message") == "E12003006: image data is empty" 
        
    def test_api_Liveness_invalid_image(self, config_obj, FaceApi):
        """  提供图片静默活体检测-图片格式错误 """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/invalid_image.pdf")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "invalid image"
        assert resp.json_get("error.details.0.reason") == 12003007
        assert resp.json_get("error.message") == "E12003007: invalid image"    

    def test_api_Liveness_quality_items_low(self, config_obj, FaceApi):
        """  提供图片静默活体检测-验证低质量时-输出quality_items """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q19.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "image size is exceeded"
        assert resp.json_get("error.details.0.reason") == 12003005
        assert resp.json_get("error.message") == "E12003005: image size is exceeded"     


    def test_api_Liveness_quality_items_high(self, config_obj, FaceApi):
        """  提供图片静默活体检测-验证高质量时-不输出quality_items """
        image_path = os.path.join(
            config.image_path, "go_image/ids_face/Q19.png")
        image = FaceApi.imageToBase64(image_path)
        min_quality_level = "HIGH"
        disable_defake = False
        encrypt_info = {
            "algorithm": "ENCRPT_ALGORITHM_NONE",
            "version": 0,
            "iv": "string",
            "encrypted_fields": [
                "string"
            ],
            "data": "string"
        }
        resp = FaceApi.FaceService_DetectLivenessPostApi(image=image, min_quality_level=min_quality_level,
                                                         disable_defake=disable_defake, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.details.0.message") == "image size is exceeded"

if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])