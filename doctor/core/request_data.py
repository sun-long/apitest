# --*--coding: utf-8 --*--
import json
import re

from core import interface_code as interface


class BaseRequestData(object):
    """ interface base class
    """

    def __init__(self, conf=None):
        """ 规则
            url： 字符串， 如 http://10.1.1.1:1000/aaa/bbb/ccc
            method: [get, post, delete, put]
            headers:
                {}
                {'token': '123456', 'ak': '123456'}
            params: 用于get请求
                {}
                {'ak': '123456', device_id: ['123456', '78910']}
            body： 报文，用于post put delete等
            formdata： 用于post put delete等, 支持按照路径上传上传文件, 路径支持相对路径和绝对路径， 相对目录resource/images/*
                []
                [{'key': 'ak', ‘value’： ‘123456’, 'type': 'text'},
                 {'key': 'img_path', ‘value’: 'aaa.img', 'type': 'file'}]
            body 和formdata都存在的时候，默认body生效
        """
        key_list = ['url', 'method', 'headers', 'params', 'body', 'formdata', 'desc']
        for key in key_list:
            if not getattr(self, key, None):
                setattr(self, key, None)
        self._conf = conf

    def interface(self):
        self.check()
        obj = self._select_interface(self.method)(self)
        obj.body_dict = self.format_conf_variables(self._conf, obj.body_dict)
        obj.desc = self.format_conf_variables(self._conf, obj.origin_description)
        obj.origin_url = self.format_conf_variables(self._conf, obj.origin_url)
        obj.split_url()
        obj.origin_params = self.format_conf_variables(self._conf, obj.origin_params)
        obj.origin_body = self.format_conf_variables(self._conf, obj.origin_body)
        obj.origin_formdata = self.format_conf_variables(self._conf, obj.origin_formdata)
        return obj

    @staticmethod
    def format_conf_variables(conf_obj, json_dict):
        """ 替换配置变量"""
        if conf_obj and json_dict:
            # 目前仅支持dict 和str，有新类型再增加 TODO
            if isinstance(json_dict, (dict, list)):
                json_str = json.dumps(json_dict)
            elif isinstance(json_dict, str):
                json_str = json_dict
            else:
                raise Exception('类型不支持')
            for key, value in conf_obj._ext.items():
                json_str = re.sub(r"\$\(%s\)" % key, str(value), json_str, count=0, flags=0)

            if isinstance(json_dict, (dict, list)):
                json_dict = json.loads(json_str)
            else:
                json_dict = json_str
        return json_dict

    @staticmethod
    def _select_interface(method_name):
        if method_name.lower() == "get":
            return interface.GetInterface
        elif method_name.lower() == "post":
            return interface.PostInterface
        elif method_name.lower() == "put":
            return interface.PutInterface
        elif method_name.lower() == "delete":
            return interface.DeleteInterface
        else:
            raise Exception("未支持的method name: %s" % method_name)

    def check(self):
        if not self.method:
            raise Exception('method is required.')
