#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os.path

from commonlib import utils
from commonlib.decorator import wait
from defines.belt.api.lottery_service_swagger import LotterySwaggerApi


"""
使用说明：


"""


class LotterySwaggerBusiness(LotterySwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(LotterySwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Signature"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)

        if inte_obj.path == '/v1/lottery/ocr':
            inte_obj.set_headers('X-Belt-Action', 'LotteryIdentity')
            inte_obj.set_headers('X-Belt-Version', 'v1')

    def writeCsvFile(self, file_name, data_list):
        """ 写csv文件"""
        titile = ["图片名字",
                  "保安区号真值",
                  "保安区识别结果",
                  "保安区对比结论",
                  "彩票号码真值",
                  "彩票号码识别结果",
                  "彩票号码对比结论",
                  "接口耗时",
                  "执行日志",
                  "原保安区识别结果",
                  "原彩票区识别结果",
                  ]
        res = []
        res.append(",".join(titile))
        for data in data_list:
            line = [
                "%s.json" % data["name"],
                data["gt_safe_code"],
                data["security_code"],
                data["security_compare"],
                data["gt_ticket_code"],
                data["ticket_code"],
                data["ticket_compare"],
                str(data["delay"]),
                data["log"],
                data["gt_safe_desc"],
                data["gt_ticket_desc"],
            ]
            res.append(",".join(line))
        res = "\n".join(res)
        with open(file_name, "w", encoding="utf_8_sig") as f:
            f.write(res)

    def writeCsvGtFile(self, file_name, data_list):
        """ 写csv文件"""
        titile = ["图片名字",
                  "保安区号真值",
                  "保安区识别结果",
                  "彩票号码",
                  "彩票号码识别结果",
                  "日志"
                  ]
        res = []
        res.append(",".join(titile))
        for data in data_list:
            line = [
                "%s.json" % data["name"].split(".")[0],
                data["security_code"],
                " ",
                data["ticket_code"],
                " ",
                data["log"],
            ]
            res.append(",".join(line))
        res = "\n".join(res)
        with open(file_name, "w", encoding="utf_8_sig") as f:
            f.write(res)


    def readGtFile(self, gt_file_path):
        """ 读取真值文件"""
        gt_res_list = []
        if os.path.exists(gt_file_path):
            gt_list = utils.read_csv(gt_file_path)
            for info in gt_list:
                if not info:
                    continue
                if info[0].startswith("#"):
                    continue
                gt_res_list.append({
                    "name": info[0].split(".")[0],
                    "gt_safe_code": info[1],
                    "gt_safe_desc": info[2],
                    "gt_ticket_code": info[3],
                    "gt_ticket_desc": info[4],
                    "log": "",
                    "delay": "",
                    "security_code": "",
                    "ticket_code": "",
                    "security_compare": "",
                    "ticket_compare": "",
                })
        return gt_res_list