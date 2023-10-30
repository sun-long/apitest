#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestIpsocrParam(object):
    """ ipsOcr Param测试"""

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

    @pytest.mark.skip
    @pytest.mark.parametrize("invalidParam", [
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('template_data', 'invalidtemplate_data'),
        ('template_data', ''),
        ('template_data', None),
    ])
    def test_api_BatchCustomTemplateInvalidParam(self, invalidParam, config_obj, IpsocrApi):
        """  对批量的图片中的文字进行用户自定义模板检测识别.  [INTERNAL] [EXPERIMENTAL... """
        type = None
        images = None
        template_data = None
        intef = IpsocrApi.BatchCustomTemplatePostApi(type=type, images=images, template_data=template_data, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.skip
    @pytest.mark.parametrize("invalidParam", [
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('region_type', 'invalidregion_type'),
        ('region_type', ''),
        ('region_type', None),
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
    ])
    def test_api_BatchPlainTextInvalidParam(self, invalidParam, config_obj, IpsocrApi):
        """  对批量的图片中的纯文本进行检测识别.  [SINCE v3.0.0].
[EN] Detection... """
        type = None
        region_type = None
        images = None
        intef = IpsocrApi.BatchPlainTextPostApi(type=type, region_type=region_type, images=images, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.skip
    @pytest.mark.parametrize("invalidParam", [
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('template_db_ids', 'invalidtemplate_db_ids'),
        ('template_db_ids', ''),
        ('template_db_ids', None),
    ])
    def test_api_BatchSpecialTemplateInvalidParam(self, invalidParam, config_obj, IpsocrApi):
        """  对批量的图片进行模板检测识别, 适用于特殊模板类型.  [SINCE v3.0.0].
[EN] O... """
        type = None
        images = None
        template_db_ids = None
        intef = IpsocrApi.BatchSpecialTemplatePostApi(type=type, images=images, template_db_ids=template_db_ids, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('region_type', 'invalidregion_type'),
        ('region_type', ''),
        ('region_type', None),
        ('type', 'invalidtype'),
        ('type', ''),
        ('type', None),
        ('images', 'invalidimages'),
        ('images', ''),
        ('images', None),
        ('images.0.data', 'invalidimages'),
        ('images.0.data', ''),
        ('images.0.data', None),
    ])
    def test_api_BatchTemplateInvalidParam(self, invalidParam, config_obj, IpsocrApi):
        """  对批量的图片中的文字进行模板检测识别, 需要指定模板的区域信息.  [SINCE v3.0.0].
... """
        # 准备测试数据
        image1 = os.path.join(config.image_path, "go_image/belt/tempidcardimgdata.jpeg")
        region_type = "CHINA"
        type = "OCR_IDCARD_CLASS"
        images = [
            {
                "format": "IMAGE_JPEG",
                "data": IpsocrApi.imageToBase64(image1)
            }
        ]
        intef = IpsocrApi.BatchTemplatePostApi(region_type=region_type, type=type, images=images, sendRequest=False)
        intef.update_body(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('X-Resource-Type', ''),
        ('X-Resource-Type', 'invalid'),
        ('X-Resource-Type', 'ocr'),
        ('X-Resource-Type', None),
        ('X-Object-Type', ''),
        ('X-Object-Type', 'invalid'),
        ('X-Object-Type', None),
        ('X-Object-Version', ''),
        ('X-Object-Version', 'invalid'),
        ('X-Object-Version', None),
        # ('X-Bot-Name', ''),  # 本期Bot-Name不做限制
        # ('X-Bot-Name', 'invalid'),
        # ('X-Bot-Name', None),
    ])
    def test_api_BatchTemplateInvalidHearderParam(self, invalidParam, config_obj, IpsocrApi):
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
        intef = IpsocrApi.BatchTemplatePostApi(region_type=region_type, type=type, images=images, sendRequest=False)
        intef.set_headers(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
    ])
    def test_api_GetSystemInfoInvalidParam(self, invalidParam, config_obj, IpsocrApi):
        """  获取系统信息. [SINCE v3.0.0].
[EN] Get system info which... """
        intef = IpsocrApi.GetSystemInfoGetApi(sendRequest=False)
        intef.update_params(invalidParam[0], invalidParam[1])

        resp = intef.request()
        assert resp.status_code != 200

    @pytest.mark.parametrize("invalidParam", [
        ('X-Resource-Type', ''),
        ('X-Resource-Type', 'invalid'),
        ('X-Resource-Type', 'ocr'),
        ('X-Resource-Type', None),
        ('X-Object-Type', ''),
        ('X-Object-Type', 'invalid'),
        ('X-Object-Type', None),
        ('X-Object-Version', ''),
        ('X-Object-Version', 'invalid'),
        ('X-Object-Version', None),
        # ('X-Bot-Name', ''),  # 本期Bot-Name不做限制
        # ('X-Bot-Name', 'invalid'),
        # ('X-Bot-Name', None),
    ])
    def test_api_GetSystemInfoInvalidHeaderParam(self, invalidParam, config_obj, IpsocrApi):
        """  获取系统信息. [SINCE v3.0.0].
[EN] Get system info which... """
        intef = IpsocrApi.GetSystemInfoGetApi(sendRequest=False)
        intef.set_headers(invalidParam[0], invalidParam[1])
        resp = intef.request()
        assert resp.status_code != 200