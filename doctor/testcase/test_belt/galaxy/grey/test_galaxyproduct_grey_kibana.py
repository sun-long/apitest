#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
import json
from commonlib import config, time_utils, sign_utils, utils
from commonlib.log_utils import log
from pytest_check import check

def getLogInfo():
    """ 获取日志信息"""
    log_dir = os.path.join(config.project_path, "result/belt_test/20230425_180605/galaxy")
    file_path_list = []
    for dirpath, dirnames, filenames in os.walk(log_dir):
        for filename in filenames:
            file_path_list.append(os.path.join(dirpath, filename))
    res_list = []
    for file_name in file_path_list:
        with open(file_name, "r", encoding="utf-8") as f:
            content = json.load(f)
            res_list.append(content)
    return res_list


class TestGalaxyproductGreyKibana(object):
    """ galaxyProduct 灰度测试"""

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

    @pytest.mark.parametrize("res", [x for x in getLogInfo()], ids=[
        "%s_%s_%s" % (x["galaxyTenant"]["name"],
                      x["galaxyDevice"]["name"],
                      x["interface_name"]) for x in getLogInfo()])
    def test_kibana_check(self, res, kibanaObj):
        """  kibana """
        request_id = res["request_id"]
        gte = time_utils.get_ago_timestamp(7)
        lte = time_utils.get_after_timestamp(1)
        current_time = time_utils.get_timestamp()
        resp = kibanaObj.msearchApi(request_id, gte, lte, current_time)
        info = resp.json()
        hits = info["responses"][0]["hits"]["hits"]

        log().info("requestId: %s" % request_id)
        log().info("url: %s" % res["url"])
        # log().info("hits:\n%s" % hits)
        res_belt, res_aliyun = None, None
        status_belt, status_aliyun = None, None
        if res['grey_info']["op"] == "CP":
            assert len(hits) > 0, "hits为null，没有查询到任何数据"
            assert "res_belt" in hits[0]["_source"] and hits[0]["_source"]["res_belt"], "res_belt没查询到数据"
            assert "res_aliyun" in hits[0]["_source"] and hits[0]["_source"]["res_aliyun"], "res_aliyun没查询到数据"
            res_belt = hits[0]["_source"]["res_belt"]
            res_aliyun = hits[0]["_source"]["res_aliyun"]
            status_belt = hits[0]["_source"]["status_belt"]
            status_aliyun = hits[0]["_source"]["status_aliyun"]
        elif res['grey_info']["op"] == "MV":
            assert len(hits) == 0, "[MV]hits为null.kibana没有数据"
            pytest.mark.skip("[MV]kibana没有数据")
            # assert "res_belt" in hits[0]["_source"] and hits[0]["_source"]["res_belt"], "res_belt没查询到数据"
            # assert "res_aliyun" not in hits[0]["_source"] or not hits[0]["_source"]["res_aliyun"], "res_aliyun有数据，预期没有"
            # res_belt = hits[0]["_source"]["res_belt"]
            # status_belt = hits[0]["_source"]["status_belt"]
        elif res['grey_info']["op"] == "NONE":
            assert len(hits) == 0, "[NONE]hits不为null，查询到数据，租户不参与灰度，预期查不到"
            pytest.mark.skip("[NONE]该租户不参与灰度")
        else:
            raise Exception("grey_info op error:%s" % res['grey_info']["op"])
        log().info("response_from_interface:\n%s" % res["response"])
        log().info("res_belt:\n%s" % res_belt)
        log().info("res_aliyun:\n%s" % res_aliyun)
        log().info("status_response:%s" % res["status_code"])
        log().info("status_belt:%s" % status_belt)
        log().info("status_aliyun:%s" % status_aliyun)
        if res_belt:
            self.kibana_check(res_belt, res, source="res_belt")
        if res_aliyun:
            self.kibana_check(res_aliyun, res, source="res_aliyun")

    def kibana_check(self, kibana_res, interface_res, source=None):
        if interface_res["interface_name"] in ["compareProduct_1", "compareProduct"]:
            self.verify_field("after_foreign_object_list", kibana_res, interface_res["response"], source=source)
            self.verify_field("before_foreign_object_list", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.errorDetail", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.error_code", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.error_msg", kibana_res, interface_res["response"], source=source)
            self.verify_field("resultCode", kibana_res, interface_res["response"], source=source)
            self.verify_field("sku", kibana_res, interface_res["response"], source=source)
            self.verify_field("warningCode", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["RecognizeMultipleProduct_1", "RecognizeMultipleProduct"]:
            self.verify_field("code", kibana_res, interface_res["response"], source=source)
            self.verify_field("data.multiRecognizeBody", kibana_res, interface_res["response"], source=source)
            self.verify_field("data.resultCode", kibana_res, interface_res["response"], source=source)
            self.verify_field("data.warningCode", kibana_res, interface_res["response"], source=source)
            self.verify_field("message", kibana_res, interface_res["response"], source=source)
            self.verify_field("success", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["recognizeProduct_1", "recognizeProduct"]:
            self.verify_field("foreign_object_list", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.errorDetail", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.error_code", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.error_msg", kibana_res, interface_res["response"], source=source)
            self.verify_field("resultCode", kibana_res, interface_res["response"], source=source)
            self.verify_field("sku", kibana_res, interface_res["response"], source=source)
            self.verify_field("warningCode", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["replenishCheck_1", "replenishCheck"]:
            self.verify_field("header.errorDetail", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.error_code", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.error_msg", kibana_res, interface_res["response"], source=source)
            self.verify_field("layers", kibana_res, interface_res["response"], source=source)
            self.verify_field("resultCode", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["cameraCheck_1", "cameraCheck"]:
            self.verify_field("fogResult", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.errorDetail", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.error_code", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.error_msg", kibana_res, interface_res["response"], source=source)
            self.verify_field("pass", kibana_res, interface_res["response"], source=source)
            self.verify_field("result", kibana_res, interface_res["response"], source=source)
            self.verify_field("resultCode", kibana_res, interface_res["response"], source=source)
            self.verify_field("warningCode", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["conflictProduct_1", "conflictProduct"]:
            self.verify_field("header.error_code", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.error_msg", kibana_res, interface_res["response"], source=source)
            self.verify_field("resultCode", kibana_res, interface_res["response"], source=source)
            self.verify_field("sku_composes", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["ProductNameSearch_1", "ProductNameSearch"]:
            self.verify_field("code", kibana_res, interface_res["response"], source=source)
            self.verify_field("data", kibana_res, interface_res["response"], source=source)
            self.verify_field("message", kibana_res, interface_res["response"], source=source)
            self.verify_field("success", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["ProductSyncInfo_1", "ProductSyncInfo"]:
            self.verify_field("code", kibana_res, interface_res["response"], source=source)
            self.verify_field("data", kibana_res, interface_res["response"], source=source)
            self.verify_field("message", kibana_res, interface_res["response"], source=source)
            self.verify_field("success", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["queryProductList_1", "queryProductList"]:
            self.verify_field("header.error_code", kibana_res, interface_res["response"], source=source)
            self.verify_field("header.error_msg", kibana_res, interface_res["response"], source=source)
            self.verify_field("images", kibana_res, interface_res["response"], source=source, verify_content="num")
            self.verify_field("resultCode", kibana_res, interface_res["response"], source=source)
            self.verify_field("sku_details", kibana_res, interface_res["response"], source=source, verify_content="num")
        elif interface_res["interface_name"] in ["tenantConflict_1", "tenantConflict"]:
            self.verify_field("code", kibana_res, interface_res["response"], source=source)
            self.verify_field("data", kibana_res, interface_res["response"], source=source)
            self.verify_field("message", kibana_res, interface_res["response"], source=source)
            self.verify_field("success", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["transactProductAsync_1", "transactProductAsync"]:
            self.verify_field("code", kibana_res, interface_res["response"], source=source)
            self.verify_field("data.transactCode", kibana_res, interface_res["response"], source=source, verify_content='hasValue')
            self.verify_field("message", kibana_res, interface_res["response"], source=source)
            self.verify_field("success", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["RecognizeProduct_1", "RecognizeProduct"]:
            self.verify_field("code", kibana_res, interface_res["response"], source=source)
            self.verify_field("data.recognizeBodyList", kibana_res, interface_res["response"], source=source, verify_content="num")
            self.verify_field("data.resultCode", kibana_res, interface_res["response"], source=source)
            self.verify_field("data.warningCode", kibana_res, interface_res["response"], source=source)
            self.verify_field("message", kibana_res, interface_res["response"], source=source)
            self.verify_field("success", kibana_res, interface_res["response"], source=source)
        elif interface_res["interface_name"] in ["asyncTransactStatus_1", "asyncTransactStatus"]:
            self.verify_field("code", kibana_res, interface_res["response"], source=source)
            self.verify_field("data.status", kibana_res, interface_res["response"], source=source)
            self.verify_field("message", kibana_res, interface_res["response"], source=source)
            self.verify_field("success", kibana_res, interface_res["response"], source=source)
        else:
            raise Exception("%s not found " % interface_res["interface_name"])
    def verify_field(self, field_str, res, res_origin, source=None, verify_content="value"):
        """ 验证"""
        if verify_content == "value":
            with check: assert utils.json_get(field_str, res) == utils.json_get(field_str, res_origin), "[%s]%s字段不一致" % (source, field_str)
        elif verify_content == "num":
            with check: assert len(utils.json_get(field_str, res)) == len(utils.json_get(field_str, res_origin)), "[%s]%s字段len不一致" % (source, field_str)
        elif verify_content == "hasValue":
            with check: assert utils.json_get(field_str, res), "[%s]%s字段没有值" % (source, field_str)
