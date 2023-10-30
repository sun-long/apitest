#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ret_utils.py
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/22 上午10:49   wangan      1.0         接口返回类
'''
import json

from google.protobuf import json_format

from commonlib import utils
from commonlib.log_utils import log


class RespRet(object):
    def __init__(self, resp, inte_obj):
        self.origin_resp = resp
        self._inter_obj = inte_obj
        self.log_obj = None  # 日志收集对象

    @property
    def resp_json(self):
        return self._get_json()

    @property
    def json(self):
        return self.resp_json

    @property
    def inte_obj(self):
        """ 接口对象"""
        return self._inter_obj

    def _get_json(self):
        if not self.origin_resp:
            return None
        try:
            ret = json_format.MessageToJson(self.origin_resp)
            if isinstance(ret, str):
                ret = json.loads(ret)
            return ret
        except Exception as e:
            log().error("resp.json fail.")
            raise

    def json_get(self, _path=None, unescape=False, escape=False):
        """ 获取指定路径的数据"""
        if _path:
            name_list = _path.split(".")
            target = self.json
            for name in name_list[:-1]:
                if name.isdigit():
                    target = target[int(name)]
                else:
                    target = target[name]
            if name_list[-1].isdigit():
                res = target[int(name_list[-1])]
            else:
                res = target[name_list[-1]]
        else:
            res = self.json

        if unescape:
            res = utils.dezhuanyi(res)
        if escape:
            res = utils.zhuanyi(res)
        return res

    def has_attr(self, _path):
        """ 判断是否有某个属性"""
        flag = True
        try:
            self.json_get(_path)
        except:
            flag = False
        return flag


class CommonRet(RespRet):
    """ 支持 常用的返回信息"""
    def __init__(self, resp, inte_obj=None, err_obj=None):
        super(CommonRet, self).__init__(resp, inte_obj)
        self.err_obj = err_obj
        self._error_code = self._get_error_code()
        self._error_msg = self._get_error_msg()
        self._error = self._get_error()
        self._request_id = self._get_request_id()

    def _get_error_code(self):
        ret = 0
        try:
            ret = self.err_obj.args[0].code.value[0]
        except:
            pass
        return ret

    def _get_error_msg(self):
        ret = ""
        try:
            ret = self.err_obj.args[0].debug_error_string
        except:
            pass
        return ret

    def _get_error(self):
        ret = ""
        try:
            ret = self.err_obj.args[0].code.value[1]
        except:
            pass
        return ret

    def _get_request_id(self):
        ret = ""
        try:
            ret = self.err_obj.args[0].initial_metadata[0].value
        except:
            pass
        return ret

    @property
    def error_code(self):
        return self._error_code

    @property
    def error_msg(self):
        return self._error_msg

    @property
    def request_id(self):
        return self._request_id

    @property
    def error(self):
        return self._error

