import os
import pytest
import json
import requests
import asyncio
from commonlib import config
from commonlib.log_utils import log
from commonlib.sign_utils import encode_jwt_token_pt
from commonlib.websocket_idcard import *

class TestIdCardApi:
    """ IdCard Api测试"""

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
          
    def test_idcard_normal(self, config_obj):
        "身份证扫描-正常身份证人像面、国徽面"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_normal1.jpg')
        idcard_back_image = client.get_file_bytes('idcard_normal2.jpg')
        roi={'left': 0, 'top': 0, 'width': 1050, 'height': 670}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_msg') == 'ok'
        roi={'left': 0, 'top': 0, 'width': 550, 'height': 345}
        result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        assert result.get('detect_result').get('err_msg') == 'ok'

    def test_idcard_occlusion(self, config_obj):
        "身份证扫描-身份证人像面、国徽面遮挡"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_occlusion1.jpg')
        idcard_back_image = client.get_file_bytes('idcard_occlusion2.jpg')
        roi={'left': 0, 'top': 0, 'width': 1400, 'height': 850}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 211
        assert result.get('detect_result').get('err_msg') == 'idcard occlusion'
        # result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        # assert result.get('detect_result').get('err_code') == 211
        # assert result.get('detect_result').get('err_msg') == 'idcard occlusion'
        
    def test_idcard_not_in_ori(self, config_obj):
        "身份证扫描-身份证人像面、国徽面不在roi"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_not_in_ori1.jpg')
        idcard_back_image = client.get_file_bytes('idcard_not_in_ori2.jpg')
        roi={'left': 0, 'top': 0, 'width': 400, 'height': 200}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 203
        assert 'not in roi' in result.get('detect_result').get('err_msg')
        # result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        # assert result.get('detect_result').get('err_code') == 203
        # assert result.get('detect_result').get('err_msg') == 'idcard not in roi'
        
        
    def test_idcard_not_required_side(self, config_obj):
        "身份证扫描-身份证非指定面"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_not_required_side1.jpg')
        idcard_back_image = client.get_file_bytes('idcard_not_required_side2.jpg')
        roi={'left': 0, 'top': 0, 'width': 1050, 'height': 670}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_back_image, roi))
        roi={'left': 0, 'top': 0, 'width': 1050, 'height': 670}
        assert result.get('detect_result').get('err_code') == 206
        assert result.get('detect_result').get('err_msg') == 'idcard side not front'
        result = asyncio.run(client.send_idcard_back_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 206
        assert result.get('detect_result').get('err_msg') == 'idcard side not back'
    
    @pytest.mark.skip("精度问题，无法检出复印件")    
    def test_idcard_not_original(self, config_obj):
        "身份证扫描-身份证非原件-复印件"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_not_original1.jpg')
        idcard_back_image = client.get_file_bytes('idcard_not_original2.jpg')
        roi={'left': 0, 'top': 0, 'width': 1190, 'height': 790}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 207
        assert result.get('detect_result').get('err_msg') == 'idcard not original'
        result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        assert result.get('detect_result').get('err_code') == 207
        assert result.get('detect_result').get('err_msg') == 'idcard not original'
        
    @pytest.mark.skip("算法问题，无法检出非身份证件")    
    def test_not_idcard(self, config_obj):
        "身份证扫描-非身份证件"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('debit_card.jpg')
        idcard_back_image = client.get_file_bytes('debit_card.jpg')
        roi={'left': 0, 'top': 0, 'width': 340, 'height': 225}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 206
        assert result.get('detect_result').get('err_msg') == 'idcard side not front'
        result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        assert result.get('detect_result').get('err_code') == 206
        assert result.get('detect_result').get('err_msg') == 'idcard side not back'
        
        
    def test_idcard_cropped(self, config_obj):
        "身份证扫描-身份证被裁剪、不完整"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_cropped1.jpg')
        idcard_back_image = client.get_file_bytes('idcard_cropped2.jpg')
        roi={'left': 0, 'top': 0, 'width': 1120, 'height': 780}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 215
        assert result.get('detect_result').get('err_msg') == 'idcard cropped'
        result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        assert result.get('detect_result').get('err_code') == 215
        assert result.get('detect_result').get('err_msg') == 'idcard cropped'
        
    def test_idcard_screen_remake(self, config_obj):
        "身份证扫描-身份证屏幕翻拍"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_screen_remake1.jpg')
        idcard_back_image = client.get_file_bytes('idcard_screen_remake2.jpg')
        roi={'left': 0, 'top': 0, 'width': 1280, 'height': 837}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 207
        assert result.get('detect_result').get('err_msg') == 'idcard not original'
        result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        assert result.get('detect_result').get('err_code') == 207
        assert result.get('detect_result').get('err_msg') == 'idcard not original'
    
    def test_idcard_bright(self, config_obj):
        "身份证扫描-身份证强光"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_bright1.jpg')
        #idcard_back_image = client.get_file_bytes('6666.jpg')
        roi={'left': 0, 'top': 0, 'width': 1130, 'height': 740}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 212
        assert result.get('detect_result').get('err_msg') == 'idcard too bright'
        # result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        # assert result.get('detect_result').get('err_code') == 212
        # assert result.get('detect_result').get('err_msg') == 'idcard too bright'
        
    def test_idcard_dark(self, config_obj):
        "身份证扫描-身份证弱光"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_dark1.jpg')
        idcard_back_image = client.get_file_bytes('idcard_dark2.jpg')
        roi={'left': 0, 'top': 0, 'width': 1280, 'height': 837}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 213
        assert result.get('detect_result').get('err_msg') == 'idcard too dark'
        result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        assert result.get('detect_result').get('err_code') == 213
        assert result.get('detect_result').get('err_msg') == 'idcard too dark'
    
    @pytest.mark.skip()  
    def test_idcard_blur(self, config_obj):
        "身份证扫描-身份证模糊"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_blur1.jpg')
        idcard_back_image = client.get_file_bytes('idcard_blur2.jpg')
        roi={'left': 0, 'top': 0, 'width': 1050, 'height': 670}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 214
        assert result.get('detect_result').get('err_msg') == 'idcard too blur'
        # result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        # assert result.get('detect_result').get('err_code') == 214
        # assert result.get('detect_result').get('err_msg') == 'idcard too blur'
        
    def test_idcard_too_small(self, config_obj):
        "身份证扫描-身份证太小"
        client = TestWsApi()
        idcard_front_image = client.get_file_bytes('idcard_front_01.jpg')
        idcard_back_image = client.get_file_bytes('idcard_dark2.jpg')
        roi={'left': 0, 'top': 0, 'width': 7800, 'height': 10052}
        result = asyncio.run(client.send_idcard_front_and_wait(idcard_front_image, roi))
        assert result.get('detect_result').get('err_code') == 204
        assert 'too small' in result.get('detect_result').get('err_msg')
        result = asyncio.run(client.send_idcard_back_and_wait(idcard_back_image, roi))
        assert result.get('detect_result').get('err_code') == 204
        assert 'too small' in result.get('detect_result').get('err_msg')