#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

class TestIpsocrApi(object):
    """ ipsOcr Api测试"""

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

    def test_api_BatchCustomTemplate(self, config_obj, IpsocrApi):
        """  对批量的图片中的文字进行用户自定义模板检测识别.  [INTERNAL] [EXPERIMENTAL... """
        image1 = os.path.join(config.image_path, "go_image/belt/tempidcardimgdata.jpeg")
        templatedata = os.path.join(config.image_path, "go_image/belt/templatedata.txt")
        type = "OCR_CUSTOM_TEMPLATE"
        images = [
            {
                "format": "IMAGE_JPEG",
                "data": IpsocrApi.imageToBase64(image1)
            }
          ]
        template_data = IpsocrApi.imageToBase64(templatedata)
        resp = IpsocrApi.BatchCustomTemplatePostApi(type=type, images=images, template_data=template_data)
        assert resp.status_code == 500

    def test_api_BatchPlainText(self, config_obj, IpsocrApi):
        """  对批量的图片中的纯文本进行检测识别.  [SINCE v3.0.0].
[EN] Detection... """
        image1 = os.path.join(config.image_path, "go_image/belt/tempidcardimgdata.jpeg")
        type = "OCR_GENERAL_PRINT"
        region_type = "CHINA"
        images = [
            {
                "format": "IMAGE_JPEG",
                "data": IpsocrApi.imageToBase64(image1)
            }
        ]
        # 1. 调用proxy接口
        resp = IpsocrApi.BatchPlainTextPostApi(type=type, region_type=region_type, images=images)
        assert resp.status_code == 404

    def test_api_BatchSpecialTemplate(self, config_obj, IpsocrApi):
        """  对批量的图片进行模板检测识别, 适用于特殊模板类型.  [SINCE v3.0.0].
[EN] O... """
        image1 = os.path.join(config.image_path, "go_image/belt/tempidcardimgdata.jpeg")
        type = "OCR_DOC_RETRIEVE"
        images = [
            {
                "format": "IMAGE_JPEG",
                "data": IpsocrApi.imageToBase64(image1)
            }
        ]
        template_db_ids = [
            "adipisicing"
        ]
        resp = IpsocrApi.BatchSpecialTemplatePostApi(type=type, images=images, template_db_ids=template_db_ids)
        assert resp.status_code == 500

    def test_api_BatchTemplate(self, config_obj, IpsocrApi):
        """  对批量的图片中的文字进行模板检测识别, 需要指定模板的区域信息.  [SINCE v3.0.0].
... """
        image1 = os.path.join(config.image_path, "go_image/belt/tempidcardimgdata.jpeg")
        region_type = "CHINA"
        type = "OCR_IDCARD_CLASS"
        images = [
            {
                "format": "IMAGE_JPEG",
                "data": IpsocrApi.imageToBase64(image1)
            }
        ]
        resp = IpsocrApi.BatchTemplatePostApi(region_type=region_type, type=type, images=images)
        assert resp.status_code == 200

    def test_api_GetSystemInfo(self, config_obj, IpsocrApi):
        """  获取系统信息. [SINCE v3.0.0].
[EN] Get system info which... """
        resp = IpsocrApi.GetSystemInfoGetApi()
        assert resp.status_code == 200
