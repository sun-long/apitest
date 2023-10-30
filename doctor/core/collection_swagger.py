#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   collection.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/26 上午9:48   wangan      1.0         测试集合类
'''
import copy
import json
import re

from commonlib import config
from commonlib.log_utils import log
from core import interface_swagger


class CollectionsSwagger(object):
    """ 测试接口集合"""
    def __init__(self, items, values=None, ret_class=None):
        self.origin_items = items
        self.origin_values = values
        self.items = self._gen_items()
        self._test_obj = None  # 测试对象
        self._custom_func_name = None  # 自定义方法名称
        self._conf = None  # 配置文件集合，用于填充配置
        self._ext_info = None
        self.name = None
        self.swagger_dir_name = None

    def init(self, test_obj, custom_func_name=None, conf=None, ext_info=None):
        self._test_obj = test_obj
        self._custom_func_name = custom_func_name
        self._conf = conf
        self._ext_info = ext_info

    def _gen_items(self):
        _dict = {}
        for col_name, info in self.origin_items.items():
            col_dict = {}
            paths = info["paths"]
            title = info["info"]["title"] if "info" in info and "title" in info["info"] else ""
            for _path, method_dict in paths.items():
                for _method, interface in method_dict.items():
                    if 'operationId' not in interface:
                        i = 1
                    operationId = interface["operationId"] if 'operationId' in interface else interface['summary']
                    if operationId in col_dict:
                        log().info("重名operationId(summary)：%s. SKIP" % operationId)
                        continue
                    col_dict[operationId] = interface
                    col_dict[operationId].update({
                        "path": _path,
                        "method": _method,
                        "collection_title": title,
                        "swagger_file_name": col_name,
                    })

            _dict[col_name] = col_dict

        return _dict

    @staticmethod
    def read_json(path):
        with open(path, 'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict

    @staticmethod
    def _select_interface(method_name):
        if method_name.lower() == "get":
            return interface_swagger.GetInterface
        elif method_name.lower() == "post":
            return interface_swagger.PostInterface
        elif method_name.lower() == "put":
            return interface_swagger.PutInterface
        elif method_name.lower() == "delete":
            return interface_swagger.DeleteInterface
        elif method_name.lower() == "patch":
            return interface_swagger.PatchInterface
        else:
            raise Exception("未支持的method name: %s" % method_name)

    def interface(self, collection_name, interface_name, req_name=None):
        if collection_name not in self.items:
            raise Exception("测试集中不包含%s" % collection_name)
        if interface_name not in self.items[collection_name]:
            raise Exception("%s测试集中不包含接口%s" % (collection_name, interface_name))
        item = self.items[collection_name][interface_name]
        values = self.origin_items[collection_name]['definitions']
        method = item['method']
        item = copy.deepcopy(item)  # 数据隔离
        obj = self._select_interface(method)(item, values)
        obj.set_pm_info(collection_name, interface_name, swagger_dir_name=self.swagger_dir_name)
        obj.set_ext_info(self._ext_info)
        # if req_name:
        #     req_path = os.path.join(config.pm_req_path, collection_name, "%s.json" % req_name)
        #     if not os.path.isfile(req_path):
        #         raise Exception("请求json文件未找到，请检查路径：%s" % req_path)
        #     req_json = self.read_json(req_path)
        #     obj.body_dict = self.format_conf_variables(self._conf, req_json)
        #     log().debug("请求报文已替换.源文件:%s" % req_path)
        self.call_init_interface(obj)
        return obj

    @staticmethod
    def format_conf_variables(conf_obj, json_dict):
        """ 替换配置变量"""
        if conf_obj and json_dict:
            json_str = json.dumps(json_dict)
            for key, value in conf_obj._ext.items():
                json_str = re.sub(r"\$\(%s\)" % key, str(value), json_str, count=0, flags=0)
            json_dict = json.loads(json_str)
        return json_dict

    def call_init_interface(self, inte_obj):
        """ 调用初始化接口方法, 对接口对象进行初始化,如有包含自定义方法的话，默认的init_interface就不生效了"""
        if self._custom_func_name:
            if hasattr(self._test_obj, self._custom_func_name):
                log().debug("接口初始化开始：")
                _func = getattr(self._test_obj, self._custom_func_name)
                _func(inte_obj)
            return

        if hasattr(self._test_obj, 'init_interface'):
            log().debug("接口初始化开始：")
            self._test_obj.init_interface(inte_obj)

