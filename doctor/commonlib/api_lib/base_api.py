#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base_api.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/11/4 下午6:52   wangan      1.0         None
'''
import base64
import inspect
import os
from functools import reduce

from commonlib import time_utils, utils
from commonlib.log_utils import log


class BaseApi(object):
    """ Api base class"""

    @staticmethod
    def log_resp_info(resp):
        calframe = inspect.getouterframes(inspect.currentframe(), 2)
        if resp.status_code == 200:
            log().info("%s request success!" % calframe[1][3])
        else:
            log().fatal("%s request failed!" % calframe[1][3])

    def genPostManFromGrpc(self, collections):
        """ 生成postman接口文件"""
        interface_list = []
        for srv_name, srvInfo in collections.items.items():
            for method_name, methodInfo in srvInfo["methods"].items():
                interface_list.append((srv_name, method_name, methodInfo['input']['json_with_enum']))

        for srv_name, method_name, req in interface_list:
            intef = collections.interface(srv_name, method_name, req_data=req)
            if getattr(intef, 'request_http', None):
                resp = intef.request_http()

    @staticmethod
    def genPostManFromSwagger(collections):
        """ 生成postman接口文件"""
        interface_list = []
        for srv_name, srvInfo in collections.items.items():
            for method_name, methodInfo in srvInfo.items():
                interface_list.append((srv_name, method_name))

        for srv_name, method_name in interface_list:
            intef = collections.interface(srv_name, method_name)
            if getattr(intef, 'request', None):
                resp = intef.request()

    @staticmethod
    def imageToBase64(image_path):
        """ image to base64"""
        with open(image_path, "rb") as f:
            return str(base64.b64encode(f.read()), encoding="utf-8")

    def toolImageToBase64(self, image_path):
        """ image to base64"""
        return self.imageToBase64(image_path)

    def toolPrintSampleList(self, result_list, key_list=None, is_print=True):
        """ 打印简单列表"""
        enter_area = "\n%s"
        if not key_list:
            key_list = [key for key in result_list[0].keys()]
        ret = reduce(lambda x, y: "%s%s\t" % (x, y), key_list, "")[:-1] + "\n"
        for result in result_list:
            ret += reduce(lambda x, y: "%s%s\t" % (x, result[y] if y in key_list else " "), key_list, "")[:-1] + "\n"
        if is_print:
            log().info(enter_area % ret)
        return ret

    def readHostMap(self, swagger_dir, file_name="host_map.csv"):
        host_map_file = os.path.join(swagger_dir, file_name)
        host_map = {}
        if os.path.exists(host_map_file):
            host_map_list = utils.read_csv(host_map_file)
            for info in host_map_list:
                if not info:
                    continue
                if info[0].strip().startswith('#'):
                    continue
                level1_name = info[0]
                if level1_name not in host_map:
                    host_map[level1_name] = {}
                level2_name = info[1]
                if level2_name not in host_map[level1_name]:
                    host_map[level1_name][level2_name] = {
                        "host": info[2],
                        "prefix": info[3] if len(info) > 3 else ""
                    }
        return host_map

    def set_interface_prefix_path(self, inte_obj):
        """ 设置接口的前缀
            原因: 由于不同服务会存在请求路径中前缀不同的情况,即: host + prefix + path, 因此需要对存在改情况的前缀进行设置
        """
        prefix_path = None
        level1Name = inte_obj.swagger_file
        if self.host_map and level1Name in self.host_map:
            tag = inte_obj.item["tags"][0] if "tags" in inte_obj.item else None
            level1Info = self.host_map[level1Name]
            if not tag and "all" in level1Info:
                prefix_path = level1Info["all"]["prefix"]
            elif tag not in level1Info and "all" in level1Info:
                prefix_path = level1Info["all"]["prefix"]
            elif tag in level1Info:
                prefix_path = level1Info[tag]["prefix"]

        if prefix_path:
            inte_obj.set_path_prefix(prefix_path)

    def set_belt_defines(self, inte_obj):
        """ 设定belt的定义"""
        if inte_obj.path in self.configMap:
            info = self.configMap[inte_obj.path][inte_obj.method]
            inte_obj.set_headers('X-Belt-Action', info["action"])
            inte_obj.set_headers('X-Belt-Version', info["version"])
            inte_obj.set_path_prefix(info["paths"])
        else:
            raise Exception("no support PATH:%s" % inte_obj.path)

    def set_nova_defines(self, inte_obj):
        """ 设定belt的定义"""
        if inte_obj.path in self.configMap:
            info = self.configMap[inte_obj.path][inte_obj.method]
            inte_obj.set_headers('X-Sensenova-Action', info["action"])
            inte_obj.set_headers('X-Sensenova-Version', info["version"])
            inte_obj.set_path_prefix(info["paths"])
        else:
            raise Exception("no support PATH:%s" % inte_obj.path)