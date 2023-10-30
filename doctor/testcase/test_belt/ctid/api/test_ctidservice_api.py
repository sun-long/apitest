#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config
from commonlib.log_utils import log


@pytest.mark.P0
@pytest.mark.Regression
class TestCtidServiceApi(object):
    """ ctid-service Api 测试"""

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

    @pytest.mark.parametrize("imgname",
                             ["normal_single_face_01.bmp",
                              "normal_single_face_02.jpeg",
                              "normal_single_face_03.png",
                              "normal_single_face_00.jpg",
                              # "normal_single_face_10.j2k"
                              ])
    def test_api_CTIDService_DetectFaces_001(self, config_obj, CtidServiceApi, imgname):
        """face-detect:不同格式的face-detect[bmp,jpg,jpeg,png]"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json['errCode'] == '000'

    @pytest.mark.parametrize("imgname",
                             ["normal_single_face_10.j2k",
                              "base_unsupport_tif.tif",
                              "base_unsupport_gif.gif",
                              "base_unsupport_webp.webp"
                              ])
    def test_api_CTIDService_DetectFaces_001_02(self, config_obj, CtidServiceApi, imgname):
        """   face-detect:传入不支持的不同格式的face-detect[j2k,tif,gif,webp]"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json['errCode'] == '003'

    @pytest.mark.parametrize("imgname",
                             ["normal_single_face_02.jpeg",
                              "normal_single_face_04_90.jpg",
                              "normal_single_face_05_180.jpg",
                              "normal_single_face_06_270.jpg"
                              ])
    def test_api_CTIDService_DetectFaces_002(self, config_obj, CtidServiceApi, imgname):
        """   face-detect:同一人的不同旋转角度的人脸[0,90,180,270]"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        # 人脸检测质量要求较高，暂不支持旋转
        # assert resp.resp_json['errCode'] == '000'

    @pytest.mark.parametrize("imgname", ["two.jpeg", "multi_faces.jpg"])
    def test_api_CTIDService_DetectFaces_003(self, config_obj, CtidServiceApi, imgname):
        """face-detect:多张人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json['errCode'] != '000'

    @pytest.mark.parametrize("imgname", ["base_noface.png"])
    def test_api_CTIDService_DetectFaces_004(self, config_obj, CtidServiceApi, imgname):
        """face-detect:noface"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json['errCode'] in ['005', '830']

    @pytest.mark.parametrize("imgname", ["base_too_dark.jpg"])
    def test_api_CTIDService_DetectFaces_005(self, config_obj, CtidServiceApi, imgname):
        """face-detect:too dark"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        # 关闭质量检测
        #errCode = resp.resp_json['errCode']
        #assert errCode in ['006', '830']

    @pytest.mark.parametrize("imgname", ["base_too_light.png"])
    def test_api_CTIDService_DetectFaces_006(self, config_obj, CtidServiceApi, imgname):
        """face-detect:too light"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        # 关闭质量检测
        #errCode = resp.resp_json['errCode']
        #assert errCode in ['007', '830']

    @pytest.mark.parametrize("imgname", ["boy_fuzzy1.jpeg"])
    def test_api_CTIDService_DetectFaces_007(self, config_obj, CtidServiceApi, imgname):
        """face-detect:too fuzzy"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        # 关闭质量检测
        #errCode = resp.resp_json['errCode']
        #assert errCode in ['010', '830']

    @pytest.mark.parametrize("imgname", ["face_yaw_mask.jpg", "face_yaw_mask1.jpg"])
    def test_api_CTIDService_DetectFaces_008(self, config_obj, CtidServiceApi, imgname):
        """face-detect:人脸存在遮挡"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        # 关闭质量检测
        #errCode = resp.resp_json['errCode']
        #assert errCode in ['011', '830']

    @pytest.mark.parametrize("imgname", ["bad_quality_01.jpg", "bad_quality_02.jpg"])
    def test_api_CTIDService_DetectFaces_009(self, config_obj, CtidServiceApi, imgname):
        """face-detect:人脸图片质量较差"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        # 关闭质量检测
        #errCode = resp.resp_json['errCode']
        #assert errCode != '000'

    @pytest.mark.parametrize("imgname",
                             ["diff_size_single_face_05_2560_1441_4KB.jpg",
                              "diff_size_single_face_05_2560_1441_10KB.jpg",
                              "diff_size_single_face_05_2560_1441_48KB.jpg"])
    def test_api_CTIDService_DetectFaces_010_01(self, config_obj, CtidServiceApi, imgname):
        """face-detect:人脸图片不同尺寸检测-normal size"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        # assert resp.resp_json['errCode'] == '000'

    @pytest.mark.parametrize("imgname",
                             ["diff_size_single_face_02_1KB.jpg",
                              "diff_size_single_face_02_2560_1441_1KB.png"
                              ])
    def test_api_CTIDService_DetectFaces_010_02(self, config_obj, CtidServiceApi, imgname):
        """face-detect:人脸图片不同尺寸检测-小于1KB"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        errCode = resp.resp_json['errCode']
        assert errCode in ['005', '009', '013', '830']

    @pytest.mark.parametrize("imgname",
                             ["diff_size_single_face_05_2560_1441_3MB.jpg"])
    def test_api_CTIDService_DetectFaces_010_03(self, config_obj, CtidServiceApi, imgname):
        """face-detect:人脸图片不同尺寸检测-大于300KB"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        errCode = resp.resp_json['errCode']
        assert errCode in ['012', '830']

    @pytest.mark.parametrize("imgname",
                             ["posePitch0.jpg",
                              "posePitch-1.jpg",
                              "posePitch-2.jpg",
                              "posePitch-3.jpg",
                              "posePitch10.jpg",
                              ])
    def test_api_CTIDService_DetectFaces_011(self, config_obj, CtidServiceApi, imgname):
        """   face-detect:不同姿态的face-detect"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_DetectFacesPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json['errCode'] == '000'
        assert resp.has_attr('facelist')

    @pytest.mark.parametrize("imgname",
                             ["normal_single_face_01.bmp",
                              "normal_single_face_02.jpeg",
                              "normal_single_face_03.png",
                              "normal_single_face_00.jpg",
                              # "normal_single_face_10.j2k"
                              ])
    def test_api_CTIDService_CheckQuality_001(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:不同格式"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'

    @pytest.mark.parametrize("imgname",
                             ["base_unsupport_tif.tif",
                              "base_unsupport_gif.gif",
                              "base_unsupport_webp.webp"])
    def test_api_CTIDService_CheckQuality_001_02(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:不同格式"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '003'

    @pytest.mark.parametrize("imgname",
                             ["normal_single_face_02.jpeg",
                              "normal_single_face_04_90.jpg",
                              "normal_single_face_05_180.jpg",
                              "normal_single_face_06_270.jpg"])
    def test_api_CTIDService_CheckQuality_002(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check：不同角度"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        # 暂不支持旋转
        # assert resp.resp_json["errCode"] == '000'
        # assert resp.resp_json["qualityScore"] != ''
        # assert len(resp.resp_json["qualityInfo"]) == 6

    @pytest.mark.parametrize("imgname",
                             ["face_yaw_mask.jpg",
                              "face_yaw_mask1.jpg"])
    def test_api_CTIDService_CheckQuality_003(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check：存在遮挡"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["qualityScore"] != ''
        assert len(resp.resp_json["qualityInfo"]) == 6

    @pytest.mark.parametrize("imgname",
                             ["bad_quality_01.jpg",
                              "bad_quality_02.jpg"])
    def test_api_CTIDService_CheckQuality_004(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:较差质量"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        if resp.resp_json["errCode"] == '000':
            assert resp.resp_json["qualityScore"] != ''
            assert len(resp.resp_json["qualityInfo"]) == 6
        else:
            assert resp.resp_json["errCode"] == '005'

    @pytest.mark.parametrize("imgname", ["base_noface.png"])
    def test_api_CTIDService_CheckQuality_005(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:noface"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '005'

    @pytest.mark.parametrize("imgname", ["base_too_dark.jpg"])
    def test_api_CTIDService_CheckQuality_006(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:too dark"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["qualityScore"] != ''
        assert len(resp.resp_json["qualityInfo"]) == 6

    @pytest.mark.parametrize("imgname", ["base_too_light.png"])
    def test_api_CTIDService_CheckQuality_007(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:too light"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["qualityScore"] != ''
        assert len(resp.resp_json["qualityInfo"]) == 6

    @pytest.mark.parametrize("imgname", ["boy_fuzzy1.jpeg"])
    def test_api_CTIDService_CheckQuality_008(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:too fuzzy"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["qualityScore"] != ''
        assert len(resp.resp_json["qualityInfo"]) == 6

    @pytest.mark.parametrize("imgname",
                             ["diff_size_single_face_05_2560_1441_4KB.jpg",
                              "diff_size_single_face_05_2560_1441_10KB.jpg",
                              "diff_size_single_face_05_2560_1441_48KB.jpg"
                              ])
    def test_api_CTIDService_CheckQuality_009_01(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:不同尺寸图像-normal"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["qualityScore"] != ''
        assert len(resp.resp_json["qualityInfo"]) == 6

    @pytest.mark.parametrize("imgname",
                             ["diff_size_single_face_02_1KB.jpg",
                              "diff_size_single_face_02_2560_1441_1KB.png"
                              ])
    def test_api_CTIDService_CheckQuality_009_02(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:不同尺寸图像-小于1KB"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        if resp.resp_json["errCode"] == '000':
            assert resp.resp_json["qualityScore"] != ''
            assert len(resp.resp_json["qualityInfo"]) == 6
        else:
            assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("imgname",
                             [  # "diff_size_single_face_03_2560_1441_101KB.png",
                                 # "diff_size_single_face_05_2560_1441_120KB.jpg"
                                 "diff_size_single_face_05_2560_1441_3MB.jpg"
                             ])
    def test_api_CTIDService_CheckQuality_009_03(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:不同尺寸图像-大于100KB"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '012'

    @pytest.mark.parametrize("imgname", ["two.jpeg", "multi_faces.jpg"])
    def test_api_CTIDService_CheckQuality_010(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:多张人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["qualityScore"] != ''
        assert len(resp.resp_json["qualityInfo"]) == 6

    @pytest.mark.parametrize("imgname",
                             ["posePicth_Yaw15+10.jpg",
                              "posePicthYaw-7-10.jpg",
                              "posePitch0.jpg",
                              "posePitch-1.jpg",
                              "posePitch-2.jpg",
                              "posePitch-3.jpg",
                              "posePitch-5.jpg",
                              "posePitch-9.jpg",
                              "posePitch-14.jpg",
                              "posePitch-15.jpg",
                              "posePitch-19.05.jpg",
                              "posePitch-19.65.jpg",
                              "posePitch-20.8.jpg",
                              "posePitch-30.2.jpg",
                              "posePitch-31.jpg",
                              "posePitchYawRoll13-14+28.jpg",
                              "posePitch5.jpg",
                              "posePitch10.jpg",
                              "posePitch15.jpg",
                              "posePitch18.jpg",
                              "posePitch19.jpg",
                              "posePitch20.jpg",
                              "posePitch21.jpg",
                              "poseRoll0.jpg",
                              "poseRoll-5.jpg",
                              "poseRoll-5(0).jpg",
                              "poseRoll10.jpg",
                              "poseRoll20.jpg",
                              "poseRoll-20.jpg",
                              "poseRoll-28.jpg",
                              "poseRoll-29.jpg",
                              "poseYaw_Pitch-20-19.jpg",
                              "poseYaw-5.jpg",
                              "poseYaw-10.8.jpg",
                              "poseYaw10 (2).jpg",
                              "poseYaw10.jpg",
                              "poseYaw-25.4.jpg",
                              "poseYaw-28.9.jpg",
                              "poseYaw23.jpg",
                              "poseYaw30.6.jpg",
                              ])
    def test_api_CTIDService_CheckQuality_011(self, config_obj, CtidServiceApi, imgname):
        """face-quality-check:不同格式"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_CheckQualityPostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["qualityScore"] != ''
        assert len(resp.resp_json["qualityInfo"]) == 6

    @pytest.mark.parametrize("params",
                             [("normal_single_face_01.bmp", "normal_single_face_01.bmp"),
                              ("normal_single_face_01.bmp", "normal_single_face_02.jpeg"),
                              ("normal_single_face_01.bmp", "normal_single_face_03.png"),
                              ("normal_single_face_01.bmp", "normal_single_face_00.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_03.png"),
                              ("normal_single_face_02.jpeg", "normal_single_face_00.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_01.bmp"),
                              ("normal_single_face_03.png", "normal_single_face_03.png"),
                              ("normal_single_face_03.png", "normal_single_face_02.jpeg"),
                              ("normal_single_face_03.png", "normal_single_face_01.bmp"),
                              ("normal_single_face_03.png", "normal_single_face_00.jpg"),
                              ("normal_single_face_00.jpg", "normal_single_face_00.jpg"),
                              ("normal_single_face_00.jpg", "normal_single_face_01.bmp"),
                              ("normal_single_face_00.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_00.jpg", "normal_single_face_03.png")
                              ])
    def test_api_CTIDService_CompareFeatures_001(self, config_obj, CtidServiceApi, params):
        """feature-compare :相同人脸，不同格式图像feature-compare """
        # 提取第一张图片特征
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        # 提取第二张图片特征
        bizSerialNo2 = "00112345620180420113286953123211563DD535DDGHG"
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp2 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo2, photoData=photoData2)
        assert resp2.status_code == 200, "校验失败，http响应码错误"
        assert resp2.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp2.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = "00112345620180420113286953123211563DD535DDDDD"
        feature1 = resp1.resp_json["feature"]
        feature2 = resp2.resp_json["feature"]
        resp = CtidServiceApi.CTIDService_CompareFeaturesPostApi(bizSerialNo=bizSerialNo, feature1=feature1,
                                                                 feature2=feature2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'

    '''
    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_04_90.jpg")
                              ])
    def test_api_CTIDService_CompareFeatures_002(self, config_obj, CtidServiceApi, params):
        """feature-compare :相同人脸，不同旋转角度的图像feature-compare """
        # 提取第一张图片特征
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        # 提取第二张图片特征
        bizSerialNo2 = "00112345620180420113286953123211563DD535DDGHG"
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp2 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo2, photoData=photoData2)
        assert resp2.status_code == 200, "校验失败，http响应码错误"
        assert resp2.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp2.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = "00112345620180420113286953123211563DD535DDDDD"
        feature1 = resp1.resp_json["feature"]
        feature2 = resp2.resp_json["feature"]
        resp = CtidServiceApi.CTIDService_CompareFeaturesPostApi(bizSerialNo=bizSerialNo, feature1=feature1,
                                                                 feature2=feature2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000' 
    
    '''

    @pytest.mark.parametrize("params",
                             [("diff_size_single_face_05_2560_1441_4KB.jpg", "base_normal_zr_02.jpeg"),
                              ("diff_size_single_face_05_2560_1441_10KB.jpg", "base_normal_zr_02.jpeg"),
                              ("diff_size_single_face_05_2560_1441_48KB.jpg", "base_normal_zr_02.jpeg"),
                              ("base_normal_zr_02.jpeg", "diff_size_single_face_05_2560_1441_48KB.jpg")
                              ])
    def test_api_CTIDService_CompareFeatures_003(self, config_obj, CtidServiceApi, params):
        """feature-compare :相同人脸，不同尺寸的图像feature-compare -normal"""
        # 提取第一张图片特征
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        # 提取第二张图片特征
        bizSerialNo2 = "00112345620180420113286953123211563DD535DDGHG"
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp2 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo2, photoData=photoData2)
        assert resp2.status_code == 200, "校验失败，http响应码错误"
        assert resp2.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp2.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = "00112345620180420113286953123211563DD535DDDDD"
        feature1 = resp1.resp_json["feature"]
        feature2 = resp2.resp_json["feature"]
        resp = CtidServiceApi.CTIDService_CompareFeaturesPostApi(bizSerialNo=bizSerialNo, feature1=feature1,
                                                                 feature2=feature2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'

    @pytest.mark.parametrize("params",
                             [("single_face_01.jpeg", "normal_single_face_02.jpeg")])
    def test_api_CTIDService_CompareFeatures_004(self, config_obj, CtidServiceApi, params):
        """feature-compare :不同人脸的图像feature-compare """
        # 提取第一张图片特征
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        # 提取第二张图片特征
        bizSerialNo2 = "00112345620180420113286953123211563DD535DDGHG"
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp2 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo2, photoData=photoData2)
        assert resp2.status_code == 200, "校验失败，http响应码错误"
        assert resp2.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp2.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = "00112345620180420113286953123211563DD535DDDDD"
        feature1 = resp1.resp_json["feature"]
        feature2 = resp2.resp_json["feature"]
        resp = CtidServiceApi.CTIDService_CompareFeaturesPostApi(bizSerialNo=bizSerialNo, feature1=feature1,
                                                                 feature2=feature2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["photoAuthResult"] == '1'

    @pytest.mark.parametrize("params",
                             [("man_left.jpg", "man_right.jpg"),
                              ("man2_left.jpg", "man2_right.jpg"),
                              ("boy_left.jpg", "boy_right.jpg"),
                              ("girl_left.jpg", "girl_right.jpg"),
                              ("girl_left2.jpg", "girl_right2.jpg")
                              ])
    def test_api_CTIDService_CompareFeatures_005(self, config_obj, CtidServiceApi, params):
        """feature-compare :双胞胎的图像feature-compare """
        # 提取第一张图片特征
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        # 提取第二张图片特征
        bizSerialNo2 = "00112345620180420113286953123211563DD535DDGHG"
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp2 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo2, photoData=photoData2)
        assert resp2.status_code == 200, "校验失败，http响应码错误"
        assert resp2.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp2.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = "00112345620180420113286953123211563DD535DDDDD"
        feature1 = resp1.resp_json["feature"]
        feature2 = resp2.resp_json["feature"]
        resp = CtidServiceApi.CTIDService_CompareFeaturesPostApi(bizSerialNo=bizSerialNo, feature1=feature1,
                                                                 feature2=feature2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        #assert resp.resp_json["photoAuthResult"] == '2'

    @pytest.mark.parametrize("params",
                             [("brother_01.jpg", "sister_01.jpg"),
                              ("brother_02.jpg", "sister_02.jpg"),
                              ("brother_03.jpg", "sister_03.jpg")
                              ])
    def test_api_CTIDService_CompareFeatures_006(self, config_obj, CtidServiceApi, params):
        """feature-compare :龙凤胎的图像feature-compare """
        # 提取第一张图片特征
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        # 提取第二张图片特征
        bizSerialNo2 = "00112345620180420113286953123211563DD535DDGHG"
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp2 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo2, photoData=photoData2)
        assert resp2.status_code == 200, "校验失败，http响应码错误"
        assert resp2.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp2.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = "00112345620180420113286953123211563DD535DDDDD"
        feature1 = resp1.resp_json["feature"]
        feature2 = resp2.resp_json["feature"]
        resp = CtidServiceApi.CTIDService_CompareFeaturesPostApi(bizSerialNo=bizSerialNo, feature1=feature1,
                                                                 feature2=feature2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["photoAuthResult"] == '1'

    @pytest.mark.parametrize("imgname",
                             ["normal_single_face_01.bmp",
                              "normal_single_face_02.jpeg",
                              "normal_single_face_03.png",
                              "normal_single_face_00.jpg",
                              # "normal_single_face_10.j2k"
                              ])
    def test_api_CTIDService_ExtractFeature_001(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:不同格式"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert len(resp.resp_json["feature"]) <= 4000

    @pytest.mark.parametrize("imgname",
                             ["base_unsupport_tif.tif",
                              "base_unsupport_gif.gif",
                              "base_unsupport_webp.webp"])
    def test_api_CTIDService_ExtractFeature_001_02(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:不同格式"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '003'


    @pytest.mark.parametrize("imgname",
                             ["normal_single_face_02.jpeg",
                              "normal_single_face_04_90.jpg",
                              "normal_single_face_05_180.jpg",
                              "normal_single_face_06_270.jpg"])
    def test_api_CTIDService_ExtractFeature_002(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:不同旋转角度"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000' 


    @pytest.mark.parametrize("imgname", ["two.jpeg", "multi_faces.jpg"])
    def test_api_CTIDService_ExtractFeature_003(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:多张人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert len(resp.resp_json["feature"]) <= 4000

    @pytest.mark.parametrize("imgname", ["base_noface.png"])
    def test_api_CTIDService_ExtractFeature_004(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:no faces"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '005'

    @pytest.mark.parametrize("imgname", ["base_too_dark.jpg"])
    def test_api_CTIDService_ExtractFeature_005(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:too dark"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert len(resp.resp_json["feature"]) <= 4000

    @pytest.mark.parametrize("imgname", ["base_too_light.png"])
    def test_api_CTIDService_ExtractFeature_006(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:too light"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert len(resp.resp_json["feature"]) <= 4000

    @pytest.mark.parametrize("imgname", ["boy_fuzzy1.jpeg"])
    def test_api_CTIDService_ExtractFeature_007(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:too fuzzy"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert len(resp.resp_json["feature"]) <= 4000

    @pytest.mark.parametrize("imgname", ["face_yaw_mask.jpg", "face_yaw_mask1.jpg"])
    def test_api_CTIDService_ExtractFeature_008(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:存在遮挡"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert len(resp.resp_json["feature"]) <= 4000

    @pytest.mark.parametrize("imgname", ["bad_quality_01.jpg", "bad_quality_02.jpg"])
    def test_api_CTIDService_ExtractFeature_009(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:人脸图片质量较差"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        if resp.resp_json["errCode"] == '000':
            assert len(resp.resp_json["feature"]) <= 4000
        else:
            assert resp.resp_json["errCode"] == '005'

    @pytest.mark.parametrize("imgname",
                             ["diff_size_single_face_05_2560_1441_4KB.jpg",
                              "diff_size_single_face_05_2560_1441_10KB.jpg",
                              "diff_size_single_face_05_2560_1441_48KB.jpg"])
    def test_api_CTIDService_ExtractFeature_010_01(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:人脸图片不同尺寸检测-normal"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert len(resp.resp_json["feature"]) <= 4000

    @pytest.mark.parametrize("imgname",
                             ["diff_size_single_face_02_1KB.jpg",
                              "diff_size_single_face_02_2560_1441_1KB.png"
                              ])
    def test_api_CTIDService_ExtractFeature_010_02(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:人脸图片不同尺寸检测-小于1KB"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] != '000'

    '''特征提取不限制上限100KB'''
    '''
    @pytest.mark.parametrize("imgname",
                             ["diff_size_single_face_03_2560_1441_101KB.png",
                              "diff_size_single_face_05_2560_1441_120KB.jpg"
                              ])
    def test_api_CTIDService_ExtractFeature_010_03(self, config_obj, CtidServiceApi, imgname):
        """feature-extract:人脸图片不同尺寸检测-大于100KB"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, imgname))
        log().info("image length:%s" % str(len(photoData)))
        resp = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '012'
    '''

    def test_api_CTIDService_CheckHealth(self, config_obj, CtidServiceApi):
        """心跳检测"""
        resp = CtidServiceApi.CTIDService_CheckHealthGetApi()
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_01.bmp", "normal_single_face_01.bmp"),
                              ("normal_single_face_01.bmp", "normal_single_face_02.jpeg"),
                              ("normal_single_face_01.bmp", "normal_single_face_03.png"),
                              ("normal_single_face_01.bmp", "normal_single_face_00.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_03.png"),
                              ("normal_single_face_02.jpeg", "normal_single_face_00.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_01.bmp"),
                              ("normal_single_face_03.png", "normal_single_face_03.png"),
                              ("normal_single_face_03.png", "normal_single_face_02.jpeg"),
                              ("normal_single_face_03.png", "normal_single_face_01.bmp"),
                              ("normal_single_face_03.png", "normal_single_face_00.jpg"),
                              ("normal_single_face_00.jpg", "normal_single_face_00.jpg"),
                              ("normal_single_face_00.jpg", "normal_single_face_01.bmp"),
                              ("normal_single_face_00.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_00.jpg", "normal_single_face_03.png"),
                              # ("normal_single_face_01.bmp", "normal_single_face_10.j2k")
                              ])
    def test_api_CTIDService_CompareImageAndFeature_001(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :相同人脸，不同格式"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["photoAuthResult"] == '0'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_01.bmp", "base_unsupport_tif.tif"),
                              ("normal_single_face_01.bmp", "base_unsupport_gif.gif"),
                              ("normal_single_face_01.bmp", "base_unsupport_webp.webp")
                              ])
    def test_api_CTIDService_CompareImageAndFeature_001_02(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :相同人脸，不同格式"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '003'

    '''
    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_04_90.jpg")
                              ])
    def test_api_CTIDService_CompareImageAndFeature_002(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :相同人脸，不同旋转角度"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
    

    @pytest.mark.parametrize("params",
                             [("diff_size_single_face_05_2560_1441_4KB.jpg", "base_normal_zr_02.jpeg"),
                              ("diff_size_single_face_05_2560_1441_10KB.jpg", "base_normal_zr_02.jpeg"),
                              ("diff_size_single_face_05_2560_1441_48KB.jpg", "base_normal_zr_02.jpeg"),
                              ("base_normal_zr_02.jpeg", "diff_size_single_face_05_2560_1441_48KB.jpg")
                              ])
    def test_api_CTIDService_CompareImageAndFeature_003(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :相同人脸，不同尺寸"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["photoAuthResult"] == '0'
    '''

    @pytest.mark.parametrize("params",
                             [("base_normal_zr_02.jpeg", "diff_size_single_face_02_1KB.jpg"),
                              ("base_normal_zr_02.jpeg", "diff_size_single_face_02_2560_1441_1KB.png")
                              ])
    def test_api_CTIDService_CompareImageAndFeature_003_02(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :相同人脸，不同尺寸，图像过小"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("base_normal_zr_02.jpeg", "diff_size_single_face_05_2560_1441_3MB.jpg")])
    def test_api_CTIDService_CompareImageAndFeature_003_03(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :相同人脸，不同尺寸,大于1MB"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '012'

    @pytest.mark.parametrize("params",
                             [("single_face_01.jpeg", "normal_single_face_02.jpeg")])
    def test_api_CTIDService_CompareImageAndFeature_004(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :不同人脸"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["photoAuthResult"] == '1'

    '''
    @pytest.mark.parametrize("params",
                             [("man_left.jpg", "man_right.jpg"),
                              ("man2_left.jpg", "man2_right.jpg"),
                              ("boy_left.jpg", "boy_right.jpg"),
                              ("girl_left.jpg", "girl_right.jpg"),
                              ("girl_left2.jpg", "girl_right2.jpg")
                              ])
    def test_api_CTIDService_CompareImageAndFeature_005(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :双胞胎人脸"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'

    @pytest.mark.parametrize("params",
                             [("brother_01.jpg", "sister_01.jpg"),
                              ("brother_02.jpg", "sister_02.jpg"),
                              ("brother_03.jpg", "sister_03.jpg")
                              ])
    def test_api_CTIDService_CompareImageAndFeature_006(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :龙凤胎胎人脸"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
    '''

    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "two.jpeg"),
                              ("normal_single_face_02.jpeg", "multi_faces.jpg")
                              ])
    def test_api_CTIDService_CompareImageAndFeature_007(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :存在多张人脸"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "base_noface.png")])
    def test_api_CTIDService_CompareImageAndFeature_008(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :存在无人脸"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '005'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "base_too_dark.jpg")])
    def test_api_CTIDService_CompareImageAndFeature_009(self, config_obj, CtidServiceApi, params):
        """  photo-feature-verify  :存在人脸过暗"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        #关闭质量检测
        #assert resp.resp_json["errCode"] == '006'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "base_too_light.png")])
    def test_api_CTIDService_CompareImageAndFeature_010(self, config_obj, CtidServiceApi, params):
        """photo-feature-verify  :存在人脸过亮"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        # 关闭质量检测
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "boy_fuzzy1.jpeg")])
    def test_api_CTIDService_CompareImageAndFeature_011(self, config_obj, CtidServiceApi, params):
        """photo-feature-verify  :存在人脸过于模糊"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        # 关闭质量检测
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "face_yaw_mask.jpg"),
                              ("normal_single_face_02.jpeg", "face_yaw_mask1.jpg")
                              ])
    def test_api_CTIDService_CompareImageAndFeature_012(self, config_obj, CtidServiceApi, params):
        """photo-feature-verify  :存在遮挡的人脸图像"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        # 关闭质量检测
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "bad_quality_01.jpg"),
                              ("normal_single_face_02.jpeg", "bad_quality_02.jpg")
                              ])
    def test_api_CTIDService_CompareImageAndFeature_013(self, config_obj, CtidServiceApi, params):
        """photo-feature-verify  :存在质量较差的人脸图像"""

        # 提取第一张图片特征
        bizSerialNo = f"00112345620180420113286953123211563DD535DDGHH"
        photoData = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image length:%s" % str(len(photoData)))
        resp1 = CtidServiceApi.CTIDService_ExtractFeaturePostApi(bizSerialNo=bizSerialNo, photoData=photoData)
        assert resp1.status_code == 200, "校验失败，http响应码错误"
        assert resp1.resp_json['errCode'] == '000', "校验失败，errcode 错误"
        assert resp1.has_attr("feature"), "校验失败，未返回feature字段"

        bizSerialNo = f"00112345620180420113286953123211563DD535DDGGG"
        feature = resp1.resp_json["feature"]
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImageAndFeaturePostApi(bizSerialNo=bizSerialNo, feature=feature,
                                                                        photoData=photoData2)
        assert resp.status_code == 200
        #关闭质量检测
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_01.bmp", "normal_single_face_01.bmp"),
                              ("normal_single_face_01.bmp", "normal_single_face_02.jpeg"),
                              ("normal_single_face_01.bmp", "normal_single_face_03.png"),
                              ("normal_single_face_01.bmp", "normal_single_face_00.jpg"),
                              # ("normal_single_face_01.bmp", "normal_single_face_10.j2k"),
                              ("normal_single_face_02.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_03.png"),
                              ("normal_single_face_02.jpeg", "normal_single_face_00.jpg"),
                              # ("normal_single_face_02.jpeg", "normal_single_face_10.j2k"),
                              ("normal_single_face_02.jpeg", "normal_single_face_01.bmp"),
                              ("normal_single_face_03.png", "normal_single_face_03.png"),
                              ("normal_single_face_03.png", "normal_single_face_02.jpeg"),
                              ("normal_single_face_03.png", "normal_single_face_01.bmp"),
                              ("normal_single_face_03.png", "normal_single_face_00.jpg"),
                              # ("normal_single_face_03.png", "normal_single_face_10.j2k"),
                              ("normal_single_face_00.jpg", "normal_single_face_00.jpg"),
                              ("normal_single_face_00.jpg", "normal_single_face_01.bmp"),
                              ("normal_single_face_00.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_00.jpg", "normal_single_face_03.png"),
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_001(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:相同人脸，不同格式"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image1 length:%s" % str(len(photoData1)))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'

    @pytest.mark.parametrize("params",
                             [("base_unsupport_tif.tif", "normal_single_face_02.jpeg"),
                              ("base_unsupport_gif.gif", "normal_single_face_02.jpeg"),
                              ("base_unsupport_webp.webp", "normal_single_face_02.jpeg"),
                              ("normal_single_face_10.j2k", "normal_single_face_02.jpeg")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_001_02(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:相同人脸，不同格式:第一张格式不支持"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image1 length:%s" % str(len(photoData1)))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '003'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_01.bmp", "base_unsupport_tif.tif"),
                              ("normal_single_face_01.bmp", "normal_single_face_10.j2k"),
                              ("normal_single_face_02.jpeg", "base_unsupport_gif.gif"),
                              ("normal_single_face_02.jpeg", "base_unsupport_webp.webp")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_001_03(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:相同人脸，不同格式，第2张格式不支持"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        log().info("image1 length:%s" % str(len(photoData1)))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '014'

    '''
    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_04_90.jpg")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_002(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:相同人脸，不同旋转角度"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
    '''

    @pytest.mark.parametrize("params",
                             [("two.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "two.jpeg"),
                              ("multi_faces.jpg", "two.jpeg"),
                              ("two.jpeg", "two.jpeg"),
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_003(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:存在多张人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        #已关闭质量检测
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("base_noface.png", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "base_noface.png"),
                              ("base_noface.png", "base_noface.png")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_004(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:存在无人脸图像"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '005' or resp.resp_json["errCode"] == '016'

    @pytest.mark.parametrize("params",
                             [("base_too_dark.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "base_too_dark.jpg"),
                              ("base_too_dark.jpg", "base_too_dark.jpg")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_005(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:存在过暗的人脸图像"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        # 已关闭质量检测
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("base_too_light.png", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "base_too_light.png"),
                              ("base_too_light.png", "base_too_light.png")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_006(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:存在过亮的人脸图像"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        # 已关闭质量检测
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("boy_fuzzy1.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "boy_fuzzy1.jpeg"),
                              ("boy_fuzzy1.jpeg", "boy_fuzzy1.jpeg")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_007(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:存在过于模糊的人脸图像"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        # 已关闭质量检测
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("face_yaw_mask.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "face_yaw_mask.jpg"),
                              ("face_yaw_mask.jpg", "face_yaw_mask.jpg"),
                              ("face_yaw_mask1.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "face_yaw_mask1.jpg"),
                              ("face_yaw_mask1.jpg", "face_yaw_mask1.jpg")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_008(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:存在遮挡的人脸图像"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        # 已关闭质量检测
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("bad_quality_01.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "bad_quality_01.jpg"),
                              ("bad_quality_01.jpg", "bad_quality_01.jpg"),
                              ("bad_quality_02.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "bad_quality_02.jpg"),
                              ("bad_quality_02.jpg", "bad_quality_02.jpg")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_009(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:存在质量较差的人脸图像"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        # 已关闭质量检测
        #assert resp.resp_json["errCode"] != '000'

    '''
    @pytest.mark.parametrize("params",
                             [("diff_size_single_face_05_2560_1441_4KB.jpg", "normal_single_face_02.jpeg"),
                              ("diff_size_single_face_05_2560_1441_10KB.jpg", "normal_single_face_02.jpeg"),
                              ("diff_size_single_face_05_2560_1441_48KB.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "diff_size_single_face_05_2560_1441_48KB.jpg")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_010_01(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:不同尺寸的人脸图像比对"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image1 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
    '''

    @pytest.mark.parametrize("params",
                             [("diff_size_single_face_02_1KB.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "diff_size_single_face_02_1KB.jpg"),
                              ("diff_size_single_face_02_2560_1441_1KB.png", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "diff_size_single_face_02_2560_1441_1KB.png"),
                              ("diff_size_single_face_02_1KB.jpg", "diff_size_single_face_02_2560_1441_1KB.png"),
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_010_02(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:不同尺寸的人脸图像比对-小于1KB"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image1 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [  # ("diff_size_single_face_03_2560_1441_101KB.png", "normal_single_face_02.jpeg"),
                                 # ("normal_single_face_02.jpeg", "diff_size_single_face_03_2560_1441_101KB.png"),
                                 # ("diff_size_single_face_05_2560_1441_120KB.jpg", "normal_single_face_02.jpeg"),
                                 # ("normal_single_face_02.jpeg", "diff_size_single_face_05_2560_1441_120KB.jpg"),
                                 # ("diff_size_single_face_05_2560_1441_120KB.jpg",
                                 # "diff_size_single_face_05_2560_1441_120KB.jpg"),
                                 # ("diff_size_single_face_03_2560_1441_101KB.png",
                                 # "diff_size_single_face_05_2560_1441_120KB.jpg")
                                 ("normal_single_face_02.jpeg", "diff_size_single_face_05_2560_1441_3MB.jpg"),
                                 ("diff_size_single_face_05_2560_1441_3MB.jpg", "normal_single_face_02.jpeg"),
                                 ("diff_size_single_face_05_2560_1441_3MB.jpg",
                                  "diff_size_single_face_05_2560_1441_3MB.jpg")
                             ])
    def test_api_CTIDService_CompareAndExtractFeature_010_03(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:不同尺寸的人脸图像比对-大于1MB"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image1 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] in ['012', '023']

    @pytest.mark.parametrize("params",
                             [("single_face_01.jpeg", "normal_single_face_02.jpeg")])
    def test_api_CTIDService_CompareAndExtractFeature_011(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:不同人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
        assert resp.resp_json["photoAuthResult"] == '1'

    '''
    @pytest.mark.parametrize("params",
                             [("man_left.jpg", "man_right.jpg"),
                              ("man2_left.jpg", "man2_right.jpg"),
                              ("boy_left.jpg", "boy_right.jpg"),
                              ("girl_left.jpg", "girl_right.jpg"),
                              ("girl_left2.jpg", "girl_right2.jpg")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_012(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:双胞胎人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'

    @pytest.mark.parametrize("params",
                             [("brother_01.jpg", "sister_01.jpg"),
                              ("brother_02.jpg", "sister_02.jpg"),
                              ("brother_03.jpg", "sister_03.jpg")
                              ])
    def test_api_CTIDService_CompareAndExtractFeature_013(self, config_obj, CtidServiceApi, params):
        """two-photos-feature-verify:龙凤胎人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareAndExtractFeaturePostApi(bizSerialNo=bizSerialNo,
                                                                          photoData1=photoData1, photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'
    '''

    @pytest.mark.parametrize("params",
                             [("normal_single_face_01.bmp", "normal_single_face_01.bmp"),
                              ("normal_single_face_01.bmp", "normal_single_face_02.jpeg"),
                              ("normal_single_face_01.bmp", "normal_single_face_03.png"),
                              ("normal_single_face_01.bmp", "normal_single_face_00.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_03.png"),
                              ("normal_single_face_02.jpeg", "normal_single_face_00.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_01.bmp"),
                              ("normal_single_face_03.png", "normal_single_face_03.png"),
                              ("normal_single_face_03.png", "normal_single_face_02.jpeg"),
                              ("normal_single_face_03.png", "normal_single_face_01.bmp"),
                              ("normal_single_face_03.png", "normal_single_face_00.jpg"),
                              ("normal_single_face_00.jpg", "normal_single_face_00.jpg"),
                              ("normal_single_face_00.jpg", "normal_single_face_01.bmp"),
                              ("normal_single_face_00.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_00.jpg", "normal_single_face_03.png")
                              ])
    def test_api_CTIDService_CompareImages_001(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:相同人脸，不同格式"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'

    @pytest.mark.parametrize("params",
                             [("base_unsupport_tif.tif", "normal_single_face_02.jpeg"),
                              ("base_unsupport_gif.gif", "normal_single_face_02.jpeg"),
                              ("base_unsupport_webp.webp", "normal_single_face_02.jpeg"),
                              ("normal_single_face_10.j2k", "normal_single_face_02.jpeg")
                              ])
    def test_api_CTIDService_CompareImages_001_02(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:相同人脸，不同格式，第一张格式不支持"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '003'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_01.bmp", "base_unsupport_tif.tif"),
                              ("normal_single_face_01.bmp", "normal_single_face_10.j2k"),
                              ("normal_single_face_02.jpeg", "base_unsupport_gif.gif"),
                              ("normal_single_face_02.jpeg", "base_unsupport_webp.webp")
                              ])
    def test_api_CTIDService_CompareImages_001_03(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:相同人脸，不同格式，第2张格式不支持"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '014'

    @pytest.mark.parametrize("params",
                             [("normal_single_face_02.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_02.jpeg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_04_90.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_04_90.jpg"),
                              ("normal_single_face_05_180.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_06_270.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_05_180.jpg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_06_270.jpg", "normal_single_face_04_90.jpg")
                              ])
    def test_api_CTIDService_CompareImages_002(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:相同人脸，不同旋转角度"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        # 暂不支持旋转，接口调用OK即可
        # assert resp.resp_json["errCode"] == '000'

    @pytest.mark.parametrize("params",
                             [("two.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "two.jpeg"),
                              ("multi_faces.jpg", "two.jpeg"),
                              ("two.jpeg", "two.jpeg"),
                              ])
    def test_api_CTIDService_CompareImages_003(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:存在多张人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("base_noface.png", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "base_noface.png"),
                              ("base_noface.png", "base_noface.png")
                              ])
    def test_api_CTIDService_CompareImages_004(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:无人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        # assert resp.resp_json["errCode"] in ['005', '016']
        assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("base_too_dark.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "base_too_dark.jpg"),
                              ("base_too_dark.jpg", "base_too_dark.jpg")
                              ])
    def test_api_CTIDService_CompareImages_005(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:存在过暗人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        # assert resp.resp_json["errCode"] in ['006', '017']
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("base_too_light.png", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "base_too_light.png"),
                              ("base_too_light.png", "base_too_light.png")
                              ])
    def test_api_CTIDService_CompareImages_006(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:存在过亮人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        # assert resp.resp_json["errCode"] in ['007','018']
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("boy_fuzzy1.jpeg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "boy_fuzzy1.jpeg"),
                              ("boy_fuzzy1.jpeg", "boy_fuzzy1.jpeg")
                              ])
    def test_api_CTIDService_CompareImages_007(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:存在过于模糊的人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        # assert resp.resp_json["errCode"] in ['010','021']
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("face_yaw_mask.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "face_yaw_mask.jpg"),
                              ("face_yaw_mask.jpg", "face_yaw_mask.jpg"),
                              ("face_yaw_mask1.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "face_yaw_mask1.jpg"),
                              ("face_yaw_mask1.jpg", "face_yaw_mask1.jpg")
                              ])
    def test_api_CTIDService_CompareImages_008(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:存在遮挡的人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        # assert resp.resp_json["errCode"] in ['011','022']
        #assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [("bad_quality_01.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "bad_quality_01.jpg"),
                              ("bad_quality_01.jpg", "bad_quality_01.jpg"),
                              ("bad_quality_02.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "bad_quality_02.jpg"),
                              ("bad_quality_02.jpg", "bad_quality_02.jpg")
                              ])
    def test_api_CTIDService_CompareImages_009(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:存在质量较差的人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        #assert resp.resp_json["errCode"] != '000'


    @pytest.mark.parametrize("params",
                             [("diff_size_single_face_05_2560_1441_4KB.jpg", "normal_single_face_02.jpeg"),
                              ("diff_size_single_face_05_2560_1441_10KB.jpg", "normal_single_face_02.jpeg"),
                              ("diff_size_single_face_05_2560_1441_48KB.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "diff_size_single_face_05_2560_1441_48KB.jpg")
                              ])
    def test_api_CTIDService_CompareImages_010_01(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:不同尺寸的人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image1 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'


    @pytest.mark.parametrize("params",
                             [("diff_size_single_face_02_1KB.jpg", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "diff_size_single_face_02_1KB.jpg"),
                              ("diff_size_single_face_02_2560_1441_1KB.png", "normal_single_face_02.jpeg"),
                              ("normal_single_face_02.jpeg", "diff_size_single_face_02_2560_1441_1KB.png"),
                              ("diff_size_single_face_02_1KB.jpg", "diff_size_single_face_02_2560_1441_1KB.png"),
                              ])
    def test_api_CTIDService_CompareImages_010_02(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:不同尺寸的人脸-小于1KB"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] != '000'

    @pytest.mark.parametrize("params",
                             [
                                 ("normal_single_face_02.jpeg", "diff_size_single_face_05_2560_1441_3MB.jpg"),
                                 ("diff_size_single_face_05_2560_1441_3MB.jpg", "normal_single_face_02.jpeg"),
                                 ("diff_size_single_face_05_2560_1441_3MB.jpg",
                                  "diff_size_single_face_05_2560_1441_3MB.jpg")
                             ])
    def test_api_CTIDService_CompareImages_010_03(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:不同尺寸的人脸-大于300KB"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image1 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] in ['012', '023']

    @pytest.mark.parametrize("params",
                             [("single_face_01.jpeg", "normal_single_face_02.jpeg")])
    def test_api_CTIDService_CompareImages_011(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:不同人的人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'


    @pytest.mark.parametrize("params",
                             [("man_left.jpg", "man_right.jpg"),
                              ("man2_left.jpg", "man2_right.jpg"),
                              ("boy_left.jpg", "boy_right.jpg"),
                              ("girl_left.jpg", "girl_right.jpg"),
                              ("girl_left2.jpg", "girl_right2.jpg")
                              ])
    def test_api_CTIDService_CompareImages_012(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:双胞胎的人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'

    @pytest.mark.parametrize("params",
                             [("brother_01.jpg", "sister_01.jpg"),
                              ("brother_02.jpg", "sister_02.jpg"),
                              ("brother_03.jpg", "sister_03.jpg")
                              ])
    def test_api_CTIDService_CompareImages_013(self, config_obj, CtidServiceApi, params):
        """two-photos-verify:龙凤胎的人脸"""
        bizSerialNo = "00112345620180420113286953123211563DD535DDGHH"
        photoData1 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[0]))
        photoData2 = CtidServiceApi.imageToBase64(os.path.join(config.ctid_image_path, params[1]))
        log().info("image1 length:%s" % str(len(photoData1)))
        log().info("image2 length:%s" % str(len(photoData2)))
        resp = CtidServiceApi.CTIDService_CompareImagesPostApi(bizSerialNo=bizSerialNo, photoData1=photoData1,
                                                               photoData2=photoData2)
        assert resp.status_code == 200
        assert resp.resp_json["errCode"] == '000'

