#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
import datetime
import uuid
from commonlib.api_lib.AES_new import *
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

@pytest.mark.checkin
class TestIdentityH5Api(object):
    """ identity Api测试"""

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

    def test_api_OCRService_H5OCRIDCard_without_session(self, config_obj, OcrApi):
        """  异常：H5 调用的内部接口,检测识别图片中的身份证, 未传biz_token """
    
        front_image = None
        back_image = None
        encrypt_info = None
        resp = OcrApi.OCRService_H5OCRIDCardPostApi(front_image=front_image, back_image=back_image, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session id provided"
        assert resp.json_get("error.details.0.reason") == 12003028
        assert resp.json_get("error.message") == "E12003028: no session id provided"     
        
    def test_api_IdentityService_CreateSession_withoutocr_actions_colorful(self, config_obj, IdentityApi):
        """  正向：创建一个IDENTITY_VERIFICATION检测会话，不检测ocr,活体检测动作+炫彩"""
        session = {
        
            "session_type": "IDENTITY_VERIFICATION",
            "candidate_actions": [
                "BLINK_EYES",
                "OPEN_MOUTH",
                "SHAKE_HEAD",
                "NOD_HEAD"
            ],
            "h5_config": {
                "redirect_url": "https://baidu.com"
            },
            "id_verification": {
            "name": "金阳",
            "idcard_number": "11010219781027232X",
            "expiry_date": ""
            }

        }
        encrypt_info = None
        resp = IdentityApi.IdentityService_CreateSessionPostApi(session=session, encrypt_info=encrypt_info)
        assert resp.status_code == 200

    def test_api_IdentityService_H5GetSessionConfig_without_sessionId(self, config_obj, IdentityApi):
        """  异常：H5 调用的内部接口, 获取H5全流程相关配置，未传递session_id """
        session_id = None
        encrypt_info = None
        resp = IdentityApi.IdentityService_H5GetSessionConfigPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session id provided"
        assert resp.json_get("error.details.0.reason") == 12003028
        assert resp.json_get("error.message") == "E12003028: no session id provided"   

    def test_api_IdentityService_H5UpdateIDCard_without_session(self, config_obj, IdentityApi):
        """  异常：H5 内部接口三要素身份核验, 未传递biz_token"""
        name = "金阳"
        idcard_number = "11010219781027232X"
        expiry_date = datetime.datetime.now().strftime('%Y-%m-%d')
        encrypt_info = None
        resp = IdentityApi.IdentityService_H5UpdateIDCardPostApi(name=name, idcard_number=idcard_number, expiry_date=expiry_date, encrypt_info=encrypt_info)
        assert resp.status_code == 400
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session id provided"
        assert resp.json_get("error.details.0.reason") == 12003028
        assert resp.json_get("error.message") == "E12003028: no session id provided"      



    def test_api_IdentityService_GetSessionLivenessResult(self, config_obj, IdentityApi):
        """  获取活体检测会话的最终结果. """
        session_id = None
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionLivenessResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session id provided"
        assert resp.json_get("error.details.0.reason") == 12003028
        assert resp.json_get("error.message") == "E12003028: no session id provided"

    def test_api_IdentityService_GetSessionVerificationResult(self, config_obj, IdentityApi):
        """  获取身份核验检测会话的最终结果. """
        session_id = None
        encrypt_info = None
        resp = IdentityApi.IdentityService_GetSessionVerificationResultPostApi(session_id=session_id, encrypt_info=encrypt_info)
        assert resp.status_code == 400    
        assert resp.json_get("error.code") == 3
        assert resp.json_get("error.details.0.message") == "no session id provided"
        assert resp.json_get("error.details.0.reason") == 12003028
        assert resp.json_get("error.message") == "E12003028: no session id provided"