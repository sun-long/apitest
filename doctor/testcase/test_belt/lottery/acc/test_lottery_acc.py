#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log
from pytest_check import check


class TestLotteryAcc(object):
    """ Lottery scenario test"""

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

    @pytest.mark.parametrize("gt", [
        ["result-0129", "D:\Work\彩票\正-picture(5元-暗光)\正-picture(5元-暗光)"],
        ["result-0202", "D:\Work\彩票\正-HDPicture"]
    ])
    # @pytest.mark.skip("精度测试，不自动运行")
    def test_acc_000_common(self, config_obj, LotteryApi, gt):
        """  准确性测试"""
        image_dir = gt[1]
        gt_file_path = os.path.join(config.image_path, "go_image/belt/lottery/%s.csv" % gt[0])
        gt_list = LotteryApi.readGtFile(gt_file_path)
        security_code_total = 0
        security_code_success = 0
        ticket_code_total = 0
        ticket_code_success = 0
        for idx, gt_info in enumerate(gt_list):
            # if idx > 5:
            #     break
            image_path = os.path.join(image_dir, "%s.jpg" % gt_info["name"])
            if not os.path.exists(image_path):
                gt_list[idx]["log"] = "ImageNotExist"
                continue
            image = LotteryApi.imageToBase64(image_path)
            resp = LotteryApi.BotLotteryService_LotteryOcrPostApi(image=image)
            gt_list[idx]["delay"] = resp.time
            if resp.status_code != 200:
                gt_list[idx]["log"] = "StatusCode:%s,Reason:%s" % (resp.status_code, resp.reason)
                continue
            security_code = resp.json_get("scratch_ticket.security_code")
            ticket_code = resp.json_get("scratch_ticket.ticket_code")
            gt_list[idx]["security_code"] = security_code
            gt_list[idx]["ticket_code"] = ticket_code
            gt_list[idx]["security_compare"] = "SUCCESS" if security_code == gt_info["gt_safe_code"] else "FAIL"
            gt_list[idx]["ticket_compare"] = "SUCCESS" if ticket_code == gt_info["gt_ticket_code"] else "FAIL"
            gt_list[idx]["log"] = "Finish"

            if gt_info["gt_safe_desc"] in ["正确", "错误", "重复样本"]:
                security_code_total += 1
                if security_code == gt_info["gt_safe_code"]:
                    security_code_success += 1
            if gt_info["gt_ticket_desc"] in ["正确", "错误", "重复样本"]:
                ticket_code_total += 1
                if ticket_code == gt_info["gt_ticket_code"]:
                    ticket_code_success += 1
        log().info("\n%s:\nsecurity_code:%s%%(%s/%s)\nticket_code:%s%%(%s/%s)\n统计【正确，错误，重复样本】" % (gt[0],
            round(security_code_success/security_code_total*100.0, 2), security_code_success, security_code_total,
            round(ticket_code_success/ticket_code_total*100.0, 2), ticket_code_success, ticket_code_total))
        LotteryApi.writeCsvFile("%s_res.csv" % gt[0], gt_list)

    @pytest.mark.parametrize("gt", [
        ["result-20230512", "D:\Work\彩票\[第三批]20230512\[第三批]20230512"],
    ])
    # @pytest.mark.skip("精度测试，不自动运行")
    def test_acc_001_noGt(self, config_obj, LotteryApi, gt):
        """  没有真值"""
        image_dir = gt[1]
        gt_file_path = os.path.join(config.image_path, "go_image/belt/lottery/%s.csv" % gt[0])
        gt_list = []
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                gt_list.append({
                    "name": file,
                    "security_code": "",
                    "ticket_code": "",
                    "log": "",
                })
        for idx, gt_info in enumerate(gt_list):
            # if idx > 5:
            #     break
            image_path = os.path.join(image_dir, gt_info["name"])
            if not os.path.exists(image_path):
                gt_list[idx]["log"] = "ImageNotExist"
                continue
            image = LotteryApi.imageToBase64(image_path)
            resp = LotteryApi.BotLotteryService_LotteryOcrPostApi(image=image)
            gt_list[idx]["delay"] = resp.time
            if resp.status_code != 200:
                gt_list[idx]["log"] = "StatusCode:%s,Reason:%s" % (resp.status_code, resp.reason)
                continue
            security_code = resp.json_get("scratch_ticket.security_code")
            ticket_code = resp.json_get("scratch_ticket.ticket_code")
            gt_list[idx]["security_code"] = security_code
            gt_list[idx]["ticket_code"] = ticket_code
            gt_list[idx]["log"] = "Finish"

        LotteryApi.writeCsvGtFile("%s.csv" % gt[0], gt_list)
