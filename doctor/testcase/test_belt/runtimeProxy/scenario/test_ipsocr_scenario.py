#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from pytest_check import check

from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestIpsocrScenario(object):
    """ Ipsocr scenario test"""

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

    def test_scenario_000_BatchCustomTemplateCheck(self, config_obj, IpsocrApi, ViperocrApi):
        """ 检查BatchCustomTemplate接口, 对比proxy及viper的接口返回结果"""
        # 准备测试数据
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
        # 1. 调用proxy接口
        resp_proxy = IpsocrApi.BatchCustomTemplatePostApi(type=type, images=images, template_data=template_data)

        # 2. 调用viper接口
        resp_viper = ViperocrApi.BatchCustomTemplatePostApi(type=type, images=images, template_data=template_data)

        # 3. 对比返回结果
        check_list = [
            "code",
            "error",
            "message",
        ]
        for item in check_list:
            proxy_value = resp_proxy.json_get(item)
            viper_value = resp_viper.json_get(item)
            with check: assert proxy_value == viper_value, "%s字段返回结果不一致,%s=%s" % (
                item, proxy_value, viper_value)

    def test_scenario_001_BatchPlainTextCheck(self, config_obj, IpsocrApi, ViperocrApi):
        """ 检查BatchPlainText接口, 对比proxy及viper的接口返回结果"""
        # 准备测试数据
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
        resp_proxy = IpsocrApi.BatchPlainTextPostApi(type=type, region_type=region_type, images=images)

        # 2. 调用viper接口
        resp_viper = ViperocrApi.BatchPlainTextPostApi(type=type, region_type=region_type, images=images)

        # 3. 对比返回结果
        check_list = [
            "code",
            "error",
            "message",
        ]
        for item in check_list:
            proxy_value = resp_proxy.json_get(item)
            viper_value = resp_viper.json_get(item)
            with check: assert proxy_value == viper_value, "%s字段返回结果不一致,%s=%s" % (
                item, proxy_value, viper_value)

    def test_scenario_002_BatchSpecialTemplateCheck(self, config_obj, IpsocrApi, ViperocrApi):
        """ 检查BatchSpecialTemplate接口, 对比proxy及viper的接口返回结果"""
        # 准备测试数据
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
        # 1. 调用proxy接口
        resp_proxy = IpsocrApi.BatchSpecialTemplatePostApi(type=type, images=images, template_db_ids=template_db_ids)

        # 2. 调用viper接口
        resp_viper = ViperocrApi.BatchSpecialTemplatePostApi(type=type, images=images, template_db_ids=template_db_ids)

        # 3. 对比返回结果
        check_list = [
            "code",
            "error",
            "message",
        ]
        for item in check_list:
            proxy_value = resp_proxy.json_get(item)
            viper_value = resp_viper.json_get(item)
            with check: assert proxy_value == viper_value, "%s字段返回结果不一致,%s=%s" % (
                item, proxy_value, viper_value)

    @pytest.mark.parametrize("imageNum", [1])
    def test_scenario_003_BatchTemplateCheck(self, config_obj, IpsocrApi, ViperocrApi, imageNum):
        """ 检查BatchTemplate接口, 对比proxy及viper的接口返回结果"""
        # 准备测试数据
        image1 = os.path.join(config.image_path, "go_image/belt/tempidcardimgdata.jpeg")
        region_type = "CHINA"
        type = "OCR_IDCARD_CLASS"
        images =[]
        for x in range(imageNum):
            images.append({
                    "format": "IMAGE_JPEG",
                    "data": IpsocrApi.imageToBase64(image1)
                })

        # 1. 调用proxy接口
        resp_proxy = IpsocrApi.BatchTemplatePostApi(region_type=region_type, type=type, images=images)
        proxy_time = resp_proxy.time
        # 2. 调用viper接口
        resp_viper = ViperocrApi.BatchTemplatePostApi(region_type=region_type, type=type, images=images)
        viper_time = resp_viper.time

        # 3. 对比返回结果
        check_list = ["responses",
                      "responses.0.object_array",
                      "responses.0.object_array.0.classification_score",
                      "responses.0.object_array.0.document_retrieve_feature",
                      "responses.0.object_array.0.object_detection_info.confidence",
                      "responses.0.object_array.0.object_detection_info.label",
                      "responses.0.object_array.0.object_detection_info.roi",
                      "responses.0.object_array.0.object_detection_info.roi.0.x",
                      "responses.0.object_array.0.object_detection_info.roi.0.y",
                      "responses.0.object_array.0.textline.childs",
                      "responses.0.object_array.0.textline.childs.0.chars",
                      "responses.0.object_array.0.textline.childs.0.chars.0.pos",
                      "responses.0.object_array.0.textline.childs.0.chars.0.score",
                      "responses.0.object_array.0.textline.childs.0.content",
                      ]
        for item in check_list:
            proxy_value = resp_proxy.json_get(item)
            viper_value = resp_viper.json_get(item)
            if isinstance(proxy_value, list):
                with check:
                    assert len(proxy_value) == len(viper_value), "%s字段返回结果不一致,%s=%s" % (
                        item, proxy_value, viper_value)
            else:
                with check:
                    assert proxy_value == viper_value, "%s字段返回结果不一致,%s=%s" % (
                        item, proxy_value, viper_value)
        log().info("proxy time:%s" % proxy_time)
        log().info("viper time:%s" % viper_time)

    def test_scenario_004_GetSystemInfoCheck(self, config_obj, IpsocrApi, ViperocrApi):
        """ 检查GetSystemInfo接口, 对比proxy及viper的接口返回结果"""
        # 准备测试数据
        # 1. 调用proxy接口
        resp_proxy = IpsocrApi.GetSystemInfoGetApi()
        assert resp_proxy.status_code == 200
        # 2. 调用viper接口
        resp_viper = ViperocrApi.GetSystemInfoGetApi()
        assert resp_viper.status_code == 200

        # 3. 对比返回结果
        check_list = ["custom_template",
                      "region_info.CHINA.plain_text",
                      "region_info.CHINA.template",
                      "region_info.HK",
                      "special_template",
                      ]
        for item in check_list:
            proxy_value = resp_proxy.json_get(item)
            viper_value = resp_viper.json_get(item)
            if isinstance(proxy_value, list):
                with check: assert len(proxy_value) == len(viper_value), "%s字段返回结果不一致,%s=%s" % (
                    item, proxy_value, viper_value)
            else:
                with check: assert proxy_value == viper_value, "%s字段返回结果不一致,%s=%s" % (
                    item, proxy_value, viper_value)

