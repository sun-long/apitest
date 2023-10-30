#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ret_utils.py
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/22 上午10:49   wangan      1.0         接口返回类
'''
import copy
import json

from commonlib import utils
from commonlib.api_lib.validator import schema_validator
from commonlib.log_utils import log


class RespRet(object):
    def __init__(self, resp, inte_obj):
        self.origin_resp = resp
        self._inter_obj = inte_obj
        self.log_obj = None  # 日志收集对象
        inte_obj.resp_obj = self
        self.resp_json_cache = None

    @property
    def status_code(self):
        return self.origin_resp.status_code

    @property
    def reason(self):
        return self.origin_resp.reason

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

    def unescape_json(self, field=None):
        """ 修改字段 暂时只支持修改第一级字段"""
        self.resp_json_cache[field] = self.json_get(field, unescape=True)

    def _get_json(self):
        if self.resp_json_cache:
            return self.resp_json_cache
        try:
            if "Content-Type" in self.origin_resp.headers and \
                "application/json" in self.origin_resp.headers["Content-Type"]:
                self.resp_json_cache = self.origin_resp.json()
                return self.resp_json_cache
            else:
                # return json.loads(self.origin_resp.text)
                return None
        except Exception as e:
            log().error("resp.json fail.")
            # raise

    def json_get(self, _path, unescape=False, escape=False):
        """ 获取指定路径的数据"""
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
    def __init__(self, resp, inte_obj=None):
        super(CommonRet, self).__init__(resp, inte_obj)
        resp_json = self.resp_json
        if resp_json:
            self._error_code = resp_json["error_code"] if "error_code" in resp_json else 0
            self._error_msg = resp_json["error_msg"] if "error_msg" in resp_json else ""
            self._request_id = resp_json["request_id"] if "request_id" in resp_json else ""
            self._error = resp_json["error"] if "error" in resp_json else ""
        else:
            self._error_code = -1
            self._error_msg = "响应结果json解析失败"
            self._request_id = ""
            self._error = "响应结果json解析失败"

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

    @property
    def response_struct(self):
        """ swagger文档中的响应结果结构"""
        return self.inte_obj.responses

    def get_definitions_by_name(self, definition_name):
        """ define info"""
        return copy.deepcopy(self.inte_obj.definitions[definition_name])

    def schema_validator(self, required_list=None, response_type="200", resp_field=None):
        """ 返回结果验证"""
        """
            resp_field:响应结果中返回的结构（待验证的）
            required_list: 
            response_type: 验证返回的类型，参考swagger文档
        """
        check_ret = False
        origin_responses = self.inte_obj.origin_responses
        if response_type in origin_responses:
            if "schema" in origin_responses[response_type] and "$ref" in origin_responses[response_type]["schema"]:
                definitions_path = origin_responses[response_type]["schema"]["$ref"]
                definition_name = definitions_path.split("#/definitions/")[-1]
                response_schema = copy.deepcopy(self.inte_obj.definitions[definition_name])
                response_schema.update({"required": required_list})
                if resp_field:
                    check_ret = schema_validator(self.json_get(resp_field), response_schema)
                else:
                    check_ret = schema_validator(self.resp_json, response_schema)
            else:
                log().warn("%s 在swagger中的返回结果中不存在schema或$ref" % response_type)
        else:
            log().warn("%s 在swagger中的返回结果中不存在" % response_type)
        return check_ret

class CurlRet(object):
    def __init__(self, ret, output, err, inte_obj):
        self.ret = ret
        self.err = err
        if isinstance(output, bytes):
            self.origin_resp = output.decode()
        else:
            self.origin_resp = output

        self._inter_obj = inte_obj
        self.log_obj = None  # 日志收集对象

    @property
    def error(self):
        return self.err

    @property
    def text(self):
        txt = ""
        _list = self.origin_resp.split("**@@**")
        if _list:
           txt = _list[0]
        return txt

    @property
    def status_code(self):
        _code = 0
        _list = self.origin_resp.split("**@@**")
        if _list and len(_list) >= 2:
            res = _list[-1]
            res_list = res.split(",")
            for k_v in res_list:
                kv =k_v.split(":")
                if kv[0] == 'http_code':
                    return int(kv[1])
        return _code

    @property
    def reason(self):
        """ TODO"""
        return ""

    @property
    def resp_json(self):
        _json = None
        try:
            _json = self._get_json()
        except:
            pass
        return _json

    @property
    def json(self):
        return self.resp_json

    @property
    def inte_obj(self):
        """ 接口对象"""
        return self._inter_obj

    def _get_json(self):
        _dict = {}
        if self.ret:
            _list = self.origin_resp.split("**@@**")
            if _list and len(_list) > 0:
                _dict = json.loads(_list[0])
        return _dict

    def json_get(self, _path, unescape=False, escape=False):
        """ 获取指定路径的数据"""
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
