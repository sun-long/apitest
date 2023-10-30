#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import base64
import json
import os
import pytest
import requests
from commonlib.sign_utils import base64Encode,base64Decode

from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log


class TestIngressApi(object):
    """ ingress Api测试,用于测试打点， 业务信息验证"""

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



    @pytest.mark.parametrize("path_name", [
        "path1",
        # "path2",
        # "path3",
        # "path4",
    ])
    @pytest.mark.skip(reason="need human test")
    def test_api_dadian_xxxx(self, path_name):
        """  da dian  """
        # 1. 调用打点接口
        res = requests.get(path_name)
        assert res.status_code == 200
        # 2. 去查看日志，是否有打点信息 （手动）

    # 测试一个只有get权限的token正向流程，只可以访问get，不能访问Post
    def test_api_jwt_payload_normal(self):
        #1、根据不同场景构造jwt格式的token,只需要修改payload部分即可,header和VERIFY_SIGNATURE不进行校验
        header_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        VERIFY_SIGNATURE="VSvZposkmq7CvE9U4dbyqG5vwllH9gkexu034I6NBlc"

        #2、构造不同的token后访问不同的接口，有权限的返回200，没有权限的返回401,此处仅列举了一些简单场景，测试时还要具体根据实际情况
        #校验的时候，校验请求的headers中的"X-Belt-Action"字段中的值，如果该请求中的token的payload部分反解出来包含该字段，表明该token有权访问这个字段所在的接口
        payload={"sub":"1234567890","name":"John Doe","iat":1516239022,"allowaccess":["TestGet"]}
        payload_json = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        secret_payload=base64Encode(payload_json.encode())
        secret_payload=str(secret_payload,encoding = "utf-8")
        final_token=header_token+'.'+secret_payload+'.'+VERIFY_SIGNATURE
        #print(final_token)
        #secret_payload=base64Encode(payload_json.encode())
        #反解
        #print(base64Decode(base64Encode(payload_json.encode())))

        #3、通过不同的token访问不同接口，例如GetDeviceByID的token请求GetDeviceByID接口，应该返回200
        headers = {
            "X-Belt-Action": "TestGet",
            "X-Request-ID": "test1",
            "X-Belt-Token": final_token,
            "X-Belt-Version": "v1"
        }
        url='http://crd-test.sensetime.com/ras'
        # data="待定"
        res = requests.get(url=url,headers=headers, verify=False)
        assert res.status_code==200
        assert json.loads(res.text)["error_msg"]=="ok"

        #4、访问不具备权限的，例如TestGet的token请求TestPost接口，应该返回401
        headers = {
            "X-Belt-Action": "TestPost",
            "X-Request-ID": "test1",
            "X-Belt-Token": final_token,
            "X-Belt-Version": "v1"
        }
        url='http://crd-test.sensetime.com/ras'
        res = requests.post(url,headers=headers, verify=False)
        assert res.status_code==401
        assert json.loads(res.text)["message"] == "UNAUTHENTICATED"

    # 使用一个拥有既可以访问TestGet又可以访问TestPost的token
    def test_api_jwt_payload_both(self):
        header_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        VERIFY_SIGNATURE = "VSvZposkmq7CvE9U4dbyqG5vwllH9gkexu034I6NBlc"
        payload = {"sub": "1234567890", "name": "John Doe", "iat": 1516239022, "allowaccess": ["TestPost","TestGet"]}
        payload_json = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        secret_payload = base64Encode(payload_json.encode())
        secret_payload = str(secret_payload, encoding="utf-8")
        final_token = header_token + '.' + secret_payload + '.' + VERIFY_SIGNATURE

        #先调用get接口。看此token是否可用
        headers = {
            "X-Belt-Action": "TestGet",
            "X-Request-ID": "test1",
            "X-Belt-Token": final_token,
            "X-Belt-Version": "v1"
        }
        url='http://crd-test.sensetime.com/ras'
        # data="待定"
        res = requests.get(url=url,headers=headers, verify=False)
        assert res.status_code==200
        assert json.loads(res.text)["error_msg"]=="ok"

        #再调用post接口，看此token是否可用
        headers = {
            "X-Belt-Action": "TestPost",
            "X-Request-ID": "test1",
            "X-Belt-Token": final_token,
            "X-Belt-Version": "v1"
        }
        url='http://crd-test.sensetime.com/ras'
        res = requests.post(url,headers=headers, verify=False)
        assert res.status_code==200
        assert json.loads(res.text)["error_msg"]=="ok"


    @pytest.mark.parametrize("allowaccess", [
        ["ABC"],
        ["/"],
        [""],
    ])
    def test_api_jwt_payload_invalid(self,allowaccess):
        header_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        VERIFY_SIGNATURE = "VSvZposkmq7CvE9U4dbyqG5vwllH9gkexu034I6NBlc"
        payload={"allowaccess": allowaccess,"iat": 1516239022,"sub": "1234567890","name":"John Doe"}
        payload_json = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        secret_payload=base64Encode(payload_json.encode())
        secret_payload=str(secret_payload,encoding = "utf-8")
        final_token=header_token+'.'+secret_payload+'.'+VERIFY_SIGNATURE
        #3、通过不同的token访问不同接口，例如GetDeviceByID的token请求GetDeviceByID接口，应该返回200
        headers = {
            "X-Belt-Action": "TestGet",
            "X-Request-ID": "test1",
            "X-Belt-Token": final_token,
            "X-Belt-Version": "v1"
        }
        url='http://crd-test.sensetime.com/ras'
        res = requests.get(url=url,headers=headers, verify=False)
        assert res.status_code == 401
        assert json.loads(res.text)["message"] == "UNAUTHENTICATED"


    @pytest.mark.parametrize("allowaccess", [
        None,
        []
    ])
    def test_api_jwt_payload_AllowaccessIsNone(self,allowaccess):
        """Allowaccess字段key,value都不传，和只传[],结果都应该是200"""
        header_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        VERIFY_SIGNATURE = "VSvZposkmq7CvE9U4dbyqG5vwllH9gkexu034I6NBlc"
        if allowaccess is None:
            payload = {"iat": 1516239022, "sub": "1234567890", "name": "John Doe"}
        else:
            payload={"allowaccess": allowaccess,"iat": 1516239022,"sub": "1234567890","name":"John Doe"}
        payload_json = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        secret_payload=base64Encode(payload_json.encode())
        secret_payload=str(secret_payload,encoding = "utf-8")
        final_token=header_token+'.'+secret_payload+'.'+VERIFY_SIGNATURE


        #该token具有全部权限，访问get接口应该返回200，等同于"allowaccess": ["TestPost","TestGet"]
        headers = {
            "X-Belt-Action": "TestGet",
            "X-Request-ID": "test1",
            "X-Belt-Token": final_token,
            "X-Belt-Version": "v1"
        }
        url='http://crd-test.sensetime.com/ras'
        res = requests.get(url=url,headers=headers, verify=False)
        assert res.status_code==200
        assert json.loads(res.text)["error_msg"]=="ok"


        #该token具有全部权限，访问post接口应该返回200
        headers = {
            "X-Belt-Action": "TestPost",
            "X-Request-ID": "test1",
            "X-Belt-Token": final_token,
            "X-Belt-Version": "v1"
        }
        url='http://crd-test.sensetime.com/ras'
        res = requests.post(url,headers=headers, verify=False)
        assert res.status_code==200
        assert json.loads(res.text)["error_msg"]=="ok"



