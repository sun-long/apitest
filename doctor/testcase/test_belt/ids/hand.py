#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config
from commonlib.log_utils import log
from commonlib.api_lib.base_api import BaseApi
from commonlib.api_lib.validator import schema_validator, digit_number_validator, idc_verify
from commonlib.api_lib.AES_new import *
# import cv2

class TestOcrApi(object):
    """ ocr Api测试"""

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

    # def test_api_OCRBankcard_01(self, config_obj, OcrApi):
    #     """验证银行卡单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_正例"""
    #     path=f"/Users/weishuting/Downloads/竖版银行卡"
    #     for image in os.listdir(path):
    #         resp = OcrApi.OCRBankcard(os.path.join(path,image))
    #         import codecs
    #         with codecs.open("log.json", 'a', encoding="utf-8") as f:
    #              f.write(os.path.join(path,image))
    #              json.dump(resp.resp_json,f,indent=4, ensure_ascii=False)


    def test_api_OCRIDCard_01(self, config_obj, OcrApi):
        """验证身份证单接口_验证支持不同图像format功能_输入不同image格式_jpeg_jpg_bmp_png_正面_正例. """
        testImage_ocr_idcard_01="ocr/idcard/idcard_50.jpg"
        # testImage_ocr_idcard_01="ocr/idcard/idcard_jiangyinglun.jpg"
        side = 'FRONT'              
        resp = OcrApi.OCRIDCard(testImage_ocr_idcard_01, side=side)
        assert resp.status_code == 200
        required_list=["side","name","sex","nation","birth_date","address","number"]
        assert resp.schema_validator(required_list=required_list, response_type="200", resp_field="idcard"), "Json_schema验证失败"
        assert idc_verify(resp.resp_json["idcard"]["number"])
        resp.json_get("idcard.side")=='FRONT'



if __name__ == "__main__":
    import datetime

    utc_time_now = datetime.datetime.utcnow()
    time = str(utc_time_now).split(".")[0].replace("-", "").replace(":", "").replace(" ", "")
    pytest.main(['-rav --capture=no', os.path.abspath(__file__)])